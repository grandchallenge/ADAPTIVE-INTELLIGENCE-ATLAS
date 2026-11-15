#!/usr/bin/env python3
"""OWI-DS-002: source-locked, fail-closed SyGuS loop-invariant admission.

This is an *independent candidate verifier*, not a synthesizer. It checks
three SMT obligations over the original SyGuS 2017 invariant-track problems:
  pre => invariant; invariant & transition => invariant'; invariant => post.
Unknown, timeout, counterexample, bad source hash, unsupported language, and
untyped candidates all FAIL admission. Source-independent real-world
correctness is not implied by passing the formal benchmark specification.

Dependencies: z3-solver. Official third-party benchmarks are fetched from a
pinned public revision and compared against their recorded Git blob SHA1.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import tempfile
import time
import urllib.request


MANIFEST = Path(__file__).with_name("owi_ds002_sygus_manifest.json")
ALLOWED_HEADS = {"set-logic", "synth-inv", "declare-primed-var",
                 "define-fun", "inv-constraint", "check-synth"}
NUM = re.compile(r"-?(?:0|[1-9][0-9]*)\Z")
SYMBOL = re.compile(r"[a-zA-Z_][a-zA-Z0-9_!.-]*\Z")


class AdmissionError(ValueError):
    pass


def parse(text: str) -> list:
    """Small non-executing S-expression parser; deliberately rejects strings."""
    if len(text) > 100_000 or '"' in text or "'" in text:
        raise AdmissionError("unsupported source length or quoted syntax")
    stripped = re.sub(r";[^\n]*", "", text)
    toks = re.findall(r"\(|\)|[^\s()]+", stripped)
    if len(toks) > 30_000:
        raise AdmissionError("source too large")
    pos = 0

    def item(depth: int):
        nonlocal pos
        if depth > 128 or pos >= len(toks):
            raise AdmissionError("truncated or too deeply nested expression")
        tok = toks[pos]
        pos += 1
        if tok == ")":
            raise AdmissionError("unmatched closing parenthesis")
        if tok != "(":
            return tok
        result = []
        while True:
            if pos >= len(toks):
                raise AdmissionError("unterminated list")
            if toks[pos] == ")":
                pos += 1
                return result
            result.append(item(depth + 1))

    expressions = []
    while pos < len(toks):
        expressions.append(item(0))
    return expressions


def emit(expr) -> str:
    return "(" + " ".join(map(emit, expr)) + ")" if isinstance(expr, list) else str(expr)


def git_blob(content: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(content)).encode() +
                        b"\0" + content).hexdigest()


def manifest_tasks(manifest: Path = MANIFEST) -> tuple[dict, dict]:
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if data.get("schema") != "gcl.owi-ds002.sygus-inv2017-source-lock.v1":
        raise AdmissionError("unexpected benchmark manifest schema")
    origin = data["origin"]
    if origin["repository"] != "SyGuS-Org/benchmarks" or not re.fullmatch(
            "[a-f0-9]{40}", origin["commit"]):
        raise AdmissionError("untrusted benchmark origin")
    tasks = {}
    for row in data["tasks"]:
        name = row["name"]
        if not re.fullmatch("[A-Za-z0-9_]{1,30}", name):
            raise AdmissionError("unsafe benchmark name")
        if (name in tasks or row["path"] !=
                f"comp/2017/Inv_Track/{name}.sl" or
                row["split"] not in ("dev", "heldout") or
                not re.fullmatch("[a-f0-9]{40}", row["git_blob_sha"])):
            raise AdmissionError("invalid, duplicate, or unpinned benchmark")
        tasks[name] = row
    if len(tasks) != 10:
        raise AdmissionError("benchmark cohort unexpectedly changed")
    return data, tasks


def locked_source(task: str, cache_dir: Path, *,
                  manifest: Path = MANIFEST, offline: bool = False) -> tuple[str, dict]:
    data, tasks = manifest_tasks(manifest)
    if task not in tasks:
        raise AdmissionError(f"task not in pinned cohort: {task}")
    record = tasks[task]
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"{task}.sl"
    if path.exists():
        raw = path.read_bytes()
        if git_blob(raw) != record["git_blob_sha"]:
            raise AdmissionError(f"source lock mismatch for {task}: cached file")
    else:
        if offline:
            raise AdmissionError(f"pinned source absent: {task}")
        url = ("https://raw.githubusercontent.com/SyGuS-Org/benchmarks/"
               + data["origin"]["commit"] + "/" + record["path"])
        with urllib.request.urlopen(url, timeout=20) as response:
            raw = response.read(100_001)
        if len(raw) > 100_000 or git_blob(raw) != record["git_blob_sha"]:
            raise AdmissionError(f"downloaded SyGuS source hash mismatch: {task}")
        with tempfile.NamedTemporaryFile(dir=cache_dir, delete=False) as tmp:
            tmp.write(raw)
            tmp_path = Path(tmp.name)
        tmp_path.replace(path)
    return raw.decode("utf-8"), record


def signature(form, expected_name, arity=None):
    if (not isinstance(form, list) or len(form) < 3 or
            form[0] != "define-fun" or form[1] != expected_name or
            not isinstance(form[2], list)):
        raise AdmissionError(f"missing/malformed {expected_name}")
    args = form[2]
    if any(not isinstance(v, list) or len(v) != 2 or
           not isinstance(v[0], str) or v[1] != "Int"
           for v in args):
        raise AdmissionError(f"unsupported variable sort in {expected_name}")
    if arity is not None and len(args) != arity:
        raise AdmissionError(f"wrong arity in {expected_name}")
    if len({v[0] for v in args}) != len(args):
        raise AdmissionError("duplicate function argument")
    if len(form) != 5 or form[3] != "Bool":
        raise AdmissionError(f"not a Bool defining equation: {expected_name}")
    return [v[0] for v in args]


def read_task(raw: str) -> dict:
    entries = parse(raw)
    named = {}
    primed = []
    for term in entries:
        if not isinstance(term, list) or not term or term[0] not in ALLOWED_HEADS:
            raise AdmissionError("unsupported or unrecognized SyGuS command")
        op = term[0]
        if op == "declare-primed-var":
            if len(term) != 3 or term[2] != "Int":
                raise AdmissionError("non-integer primed var")
            primed.append(term[1])
        elif op == "define-fun":
            if term[1] in named:
                raise AdmissionError("duplicate definition")
            named[term[1]] = term
        else:
            if op in named:
                raise AdmissionError("duplicate top-level command")
            named[op] = term
    if (named.get("set-logic") != ["set-logic", "LIA"] or
        named.get("check-synth") != ["check-synth"] or
        named.get("inv-constraint") !=
            ["inv-constraint", "inv-f", "pre-f", "trans-f", "post-f"]):
        raise AdmissionError("source is not an expected LIA invariant problem")
    synth = named.get("synth-inv")
    if (not isinstance(synth, list) or len(synth) != 3 or
            synth[1] != "inv-f" or not isinstance(synth[2], list) or
            any(not isinstance(v, list) or len(v) != 2 or v[1] != "Int"
                for v in synth[2])):
        raise AdmissionError("invalid synth-inv declaration")
    variables = [v[0] for v in synth[2]]
    if len(set(variables)) != len(variables) or not variables:
        raise AdmissionError("invalid synthesis arguments")
    if primed != variables:
        raise AdmissionError("primed variable order drift")
    trans_names = variables + [v + "!" for v in variables]
    if (signature(named.get("pre-f"), "pre-f", len(variables)) != variables or
        signature(named.get("post-f"), "post-f", len(variables)) != variables or
        signature(named.get("trans-f"), "trans-f", 2*len(variables)) != trans_names):
        raise AdmissionError("function argument order drift")
    return {"vars": variables, "definitions": [named[k] for k in
            ("pre-f", "trans-f", "post-f")]}


def typecheck(expr, variables: set[str], *, max_nodes=128) -> tuple[str, int]:
    """Bounded, typed SMT invariant with linear constant scaling and local let.

    Scoped SMT-LIB let bindings are simultaneous, not recursive. Neither an
    unknown function nor nonlinear multiplication is permitted.
    """
    count = 0

    def constant(e):
        if isinstance(e, str) and NUM.fullmatch(e):
            return int(e)
        if not isinstance(e, list) or not e:
            return None
        op, *terms = e
        xs = [constant(v) for v in terms]
        if not xs or any(x is None for x in xs):
            return None
        if op == "+":
            return sum(xs)
        if op == "-":
            return -xs[0] if len(xs) == 1 else xs[0] - sum(xs[1:])
        if op == "*":
            prod = 1
            for x in xs:
                prod *= x
            return prod
        return None

    def inner(e, depth, scope):
        nonlocal count
        count += 1
        if count > max_nodes or depth > 30:
            raise AdmissionError("candidate exceeds grammar size/depth")
        if isinstance(e, str):
            if e in scope:
                return scope[e]
            if NUM.fullmatch(e):
                return "Int"
            if e in ("true", "false"):
                return "Bool"
            raise AdmissionError(f"unknown candidate atom: {e}")
        if not isinstance(e, list) or not e or not isinstance(e[0], str):
            raise AdmissionError("malformed candidate AST")
        op, *args = e
        if op == "let":
            if (len(args) != 2 or not isinstance(args[0], list)
                    or not args[0] or len(args[0]) > 32):
                raise AdmissionError("invalid let binding list")
            definitions = {}
            for binding in args[0]:
                if (not isinstance(binding, list) or len(binding) != 2 or
                        not isinstance(binding[0], str) or
                        not SYMBOL.fullmatch(binding[0]) or
                        binding[0] in scope or binding[0] in definitions):
                    raise AdmissionError("duplicate, shadowing, or invalid let binding")
                definitions[binding[0]] = inner(binding[1], depth + 1, scope)
            local = dict(scope)
            local.update(definitions)
            return inner(args[1], depth + 1, local)
        sorts = [inner(arg, depth + 1, scope) for arg in args]
        if op in ("and", "or", "=>") and len(args) >= 2 and all(x == "Bool" for x in sorts):
            return "Bool"
        if op == "not" and sorts == ["Bool"]:
            return "Bool"
        if op == "=" and len(sorts) >= 2 and len(set(sorts)) == 1:
            return "Bool"
        if op in ("<", "<=", ">", ">=") and sorts == ["Int", "Int"]:
            return "Bool"
        if op in ("+", "-") and len(args) >= 1 and all(x == "Int" for x in sorts):
            return "Int"
        if op == "*" and sorts == ["Int", "Int"] and any(
                constant(arg) is not None for arg in args):
            return "Int"
        if op == "ite" and len(sorts) == 3 and sorts[0] == "Bool" and sorts[1] == sorts[2]:
            return sorts[1]
        raise AdmissionError(f"ill-typed or unsupported candidate operator: {op}")

    typ = inner(expr, 0, {v: "Int" for v in variables})
    if typ != "Bool":
        raise AdmissionError("invariant must have sort Bool")
    return typ, count


def verify(task: str, candidate: str, cache_dir: Path, *,
           manifest: Path = MANIFEST, offline: bool = False,
           timeout_ms: int = 10_000) -> dict:
    import z3

    if not 0 < timeout_ms <= 60_000:
        raise AdmissionError("invalid solver timeout")
    raw, record = locked_source(task, cache_dir, manifest=manifest, offline=offline)
    src = read_task(raw)
    exprs = parse(candidate)
    if len(exprs) != 1:
        raise AdmissionError("candidate must be exactly one typed expression")
    _, ast_nodes = typecheck(exprs[0], set(src["vars"]))
    variables = src["vars"]
    normal = " ".join(variables)
    primed = " ".join(v + "!" for v in variables)
    definitions = "\n".join(emit(defn) for defn in src["definitions"])
    inv_fun = ("(define-fun inv-f (" +
               " ".join(f"({v} Int)" for v in variables) + ") Bool " +
               emit(exprs[0]) + ")")
    decls = "\n".join(f"(declare-const {v} Int)" for v in
                      variables + [v + "!" for v in variables])
    base = "(set-logic LIA)\n" + definitions + "\n" + inv_fun + "\n" + decls + "\n"
    obligations = {
        "initiation": f"(and (pre-f {normal}) (not (inv-f {normal})))",
        "consecution": (f"(and (inv-f {normal}) (trans-f {normal} {primed}) "
                        f"(not (inv-f {primed})))"),
        "safety": f"(and (inv-f {normal}) (not (post-f {normal})))",
    }
    outcomes = {}
    start = time.perf_counter()
    for name, violating_formula in obligations.items():
        solver = z3.Solver()
        solver.set(timeout=timeout_ms)
        try:
            solver.from_string(base + f"(assert {violating_formula})\n")
        except z3.Z3Exception as exc:
            raise AdmissionError(f"cannot parse pinned formal specification: {exc}") from exc
        outcome = solver.check()
        value = str(outcome)
        row = {"result": value, "elapsed_seconds": None}
        if outcome == z3.sat:
            row["counterexample"] = str(solver.model())[:2048]
        if outcome == z3.unknown:
            row["reason_unknown"] = solver.reason_unknown()
        outcomes[name] = row
    elapsed = time.perf_counter() - start
    return {
        "task": task, "split": record["split"],
        "source_git_blob_sha": record["git_blob_sha"],
        "candidate_sha256": hashlib.sha256(candidate.encode()).hexdigest(),
        "candidate_nodes": ast_nodes,
        "solver": "z3", "solver_version": z3.get_version_string(),
        "timeout_per_vc_ms": timeout_ms,
        "vcs": outcomes,
        "status": ("SOLVER_CHECKED_RELATIVE_TO_PINNED_SYGUS_SPEC"
                   if all(v["result"] == "unsat" for v in outcomes.values())
                   else "REJECTED_OR_UNDECIDED"),
        "wall_seconds": elapsed,
        "scientific_limits": ("Solver checked 3 induction VCs against SyGuS formal "
                              "specification; not independent validation of "
                              "source intent, general synthesis or introspection."),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--candidate", required=True,
                    help="single candidate invariant as a typed SMT-LIB expression")
    ap.add_argument("--cache-dir", default="build/owi_ds002/sygus2017")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--timeout-ms", type=int, default=10_000)
    ap.add_argument("--output", default="")
    args = ap.parse_args()
    try:
        row = verify(args.task, args.candidate, Path(args.cache_dir),
                     offline=args.offline, timeout_ms=args.timeout_ms)
    except (AdmissionError, OSError, UnicodeError) as exc:
        row = {"task": args.task, "status": "REJECTED_OR_UNDECIDED",
               "error": str(exc)}
    data = json.dumps(row, indent=2, sort_keys=True)
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data + "\n")
    print(data)
    return 0 if row["status"] == "SOLVER_CHECKED_RELATIVE_TO_PINNED_SYGUS_SPEC" else 2


if __name__ == "__main__":
    raise SystemExit(main())
