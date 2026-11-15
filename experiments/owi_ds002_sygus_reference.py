#!/usr/bin/env python3
"""OWI-DS-002: cvc5 SyGuS baseline with independent pinned-source Z3 admission.

The synthesis solver receives the full official source (never a manufactured
target answer). Its output is accepted ONLY if the separate Z3 verifier proves
all initiation, consecution and safety obligations. Every task is run in an
isolated subprocess with a wall deadline. Timeout and unsolved are recorded,
not treated as solver successes. This is a standard non-differential baseline.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time

from owi_ds002_sygus_admission import (
    AdmissionError, locked_source, manifest_tasks, parse, read_task,
    typecheck, emit, verify)


def extract_solution(output: str, expected_names: list[str]):
    """Extract exactly one admissible inv-f definition from solver output."""
    if len(output) > 100_000:
        raise AdmissionError("oversized SyGuS solver response")
    exprs = parse(output)
    defs = []
    def scan(node):
        if isinstance(node, list):
            if node and node[0] == "define-fun":
                defs.append(node)
                return
            for child in node:
                scan(child)
    for expr in exprs:
        scan(expr)
    matched = [d for d in defs if len(d) == 5 and d[1] == "inv-f"]
    if len(matched) != 1:
        raise AdmissionError("solver returned zero or ambiguous inv-f definitions")
    d = matched[0]
    if (not isinstance(d[2], list) or d[3] != "Bool" or
            d[2] != [[v, "Int"] for v in expected_names]):
        raise AdmissionError("solver solution signature drift")
    typecheck(d[4], set(expected_names))
    return emit(d[4])


def solver_input_sygus21(legacy_source: str) -> str:
    """Convert ONLY the SyGuS-2015 primed-variable sugar.

    The 2015 standard defines (declare-primed-var x Int) to mean exactly
    (declare-var x Int) plus (declare-var x! Int). Version 2.1 removed
    the sugar. The original bytes remain SHA-locked and are used unchanged
    for independent Z3 verification; only cvc5's input is translated.
    """
    read_task(legacy_source)
    rows = []
    for cmd in parse(legacy_source):
        if cmd[0] == "declare-primed-var":
            rows.extend((["declare-var", cmd[1], "Int"],
                         ["declare-var", cmd[1] + "!", "Int"]))
        else:
            rows.append(cmd)
    return "\n".join(emit(row) for row in rows) + "\n"


def worker(task: str, cache: Path) -> int:
    import cvc5

    source, record = locked_source(task, cache, offline=True)
    src = read_task(source)
    tm = cvc5.TermManager()
    solver = cvc5.Solver(tm)
    solver.setOption("sygus", "true")
    solver.setOption("incremental", "false")
    parser = cvc5.InputParser(solver)
    parser.setStringInput(cvc5.InputLanguage.SYGUS_2_1,
                          solver_input_sygus21(source),
                          f"pinned-{task}")
    mgr = parser.getSymbolManager()
    output = []
    while True:
        cmd = parser.nextCommand()
        if cmd.isNull():
            break
        result = cmd.invoke(solver, mgr)
        if result:
            output.append(str(result))
    joined = "\n".join(output)
    try:
        expression = extract_solution(joined, src["vars"])
    except AdmissionError as err:
        print(json.dumps({"worker": "SYGUS_NO_SUPPORTED_SOLUTION",
                          "reason": str(err), "solver_output": joined[:5000]}))
        return 0
    print(json.dumps({"worker": "CANDIDATE", "expression": expression,
                      "solver_output": joined[:5000]}))
    return 0


def solve(task: str, cache: Path, *, timeout_seconds: float = 15.,
          offline: bool = False) -> dict:
    if timeout_seconds <= 0 or timeout_seconds > 120:
        raise ValueError("bounded wall deadline required")
    source, record = locked_source(task, cache, offline=offline)
    src = read_task(source)
    start = time.perf_counter()
    try:
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()),
             "--worker", "--task", task, "--cache-dir", str(cache)],
            capture_output=True, text=True, timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        return {"task": task, "split": record["split"],
                "outcome": "TIMEOUT", "source_git_blob_sha": record["git_blob_sha"],
                "wall_seconds": time.perf_counter() - start}
    row = {"task": task, "split": record["split"],
           "source_git_blob_sha": record["git_blob_sha"],
           "solver": "cvc5", "solver_version_pin": "1.4.2",
           "wall_seconds": time.perf_counter()-start}
    if proc.returncode:
        row.update(outcome="SOLVER_ERROR", error=(proc.stderr or proc.stdout)[-1500:])
        return row
    try:
        report = json.loads(proc.stdout.strip())
    except (json.JSONDecodeError, ValueError):
        row.update(outcome="MALFORMED_SOLVER_OUTPUT", error=proc.stdout[-1500:])
        return row
    if report.get("worker") != "CANDIDATE":
        row.update(outcome="UNSOLVED_OR_UNSUPPORTED",
                   solver_trace=report.get("solver_output", "")[:2000],
                   reason=report.get("reason", ""))
        return row
    expression = report["expression"]
    # Absolutely independent of the cvc5 synth solution's self-report.
    try:
        cert = verify(task, expression, cache, offline=True)
    except (AdmissionError, ValueError) as err:
        row.update(outcome="REJECTED_BY_INDEPENDENT_VERIFIER",
                   candidate=expression, reason=str(err))
        return row
    row.update(
        outcome=("VERIFIED_INDUCTIVE_INVARIANT" if cert["status"] ==
                 "SOLVER_CHECKED_RELATIVE_TO_PINNED_SYGUS_SPEC"
                 else "REJECTED_BY_INDEPENDENT_VERIFIER"),
        candidate=expression, certificate=cert)
    return row


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--task", default="")
    p.add_argument("--all", action="store_true")
    p.add_argument("--worker", action="store_true")
    p.add_argument("--cache-dir", default="build/owi_ds002/sygus2017")
    p.add_argument("--timeout-seconds", type=float, default=15.)
    p.add_argument("--offline", action="store_true")
    p.add_argument("--output", default="")
    args = p.parse_args()
    cache = Path(args.cache_dir)
    if args.worker:
        return worker(args.task, cache)
    if args.all == bool(args.task):
        p.error("specify exactly one of --task or --all")
    _, catalog = manifest_tasks()
    names = list(catalog) if args.all else [args.task]
    if any(n not in catalog for n in names):
        p.error("unknown or unpinned task name")
    records = [solve(n, cache, timeout_seconds=args.timeout_seconds,
                     offline=args.offline) for n in names]
    report = {
        "research": "OWI-DS-002",
        "method": "cvc5-1.4.2 SyGuS reference, each output Z3-verified",
        "benchmarks": len(records),
        "verified": sum(r["outcome"] == "VERIFIED_INDUCTIVE_INVARIANT"
                        for r in records),
        "records": records,
        "budget": {"solver_per_task_wall_seconds": args.timeout_seconds,
                   "not_counted": ["original-source download",
                                   "independent certificate checking time"]},
        "limits": ("Observed solve rate relative to original pinned SyGuS "
                   "specifications, not self-improving reasoning or a "
                   "differential advantage; developer/heldout contamination "
                   "must be audited before research comparison."),
    }
    data = json.dumps(report, indent=2, sort_keys=True, allow_nan=False)
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data + "\n")
    print(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
