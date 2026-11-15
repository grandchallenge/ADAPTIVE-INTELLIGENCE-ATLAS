#!/usr/bin/env python3
"""OWI-DS-002: outcome-only, grammar-exact bounded enumerative DeepCoder baseline.

Search receives ONLY public I/O (no reference solution, evaluator probes or
external solver answer). Typed bottom-up observational-signature deduplication
and bounded breadth generate real discrete DeepCoder programs. This is a
reproducible *initial* enumerator, not a mature SyGuS/DeepCoder solver.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import itertools
import json
from pathlib import Path
import random
import resource
import time

import owi_ds002_exedec_admission as admission

DEFAULT_INDICES = (0, 17, 49, 101, 177)
DEFAULT_SEEDS = (1, 2, 3, 4, 5)
DEFAULT_SPLITS = (
    "NONE", "LENGTH_GENERALIZATION", "COMPOSE_DIFFERENT_CONCEPTS",
    "SWITCH_CONCEPT_ORDER", "COMPOSE_NEW_OP", "ADD_OP_FUNCTIONALITY",
)


@dataclass(eq=False, slots=True)
class Expr:
    typ: str
    values: tuple
    cost: int
    name: str = ""
    op: str = ""
    lam: str = ""
    children: tuple = ()


def _signature(values):
    # Preserve exact type: Python bool is not an integer in this DSL.
    return tuple(json.dumps(v, separators=(",", ":")) for v in values)


def _catalog():
    unary = []
    binary = []
    for op, (signature, _) in admission.OPERATIONS.items():
        lambdas = (
            sorted(admission.UNARY) if signature.startswith("U") else
            sorted(admission.PRED) if signature.startswith("P") else
            sorted(admission.BINARY) if signature.startswith("B") else
            ("",)
        )
        for lam in lambdas:
            if signature in ("L", "UL", "PL", "BL"):
                unary.append((op, lam, "L"))
            elif signature in ("IL", "BLL"):
                binary.append((op, lam, signature[-2], signature[-1]))
            else:
                raise ValueError("unexpected upstream operation signature: " + signature)
    return unary, binary


UNARY_OPS, BINARY_OPS = _catalog()


def extract(expr: Expr, input_names: list[str]) -> str:
    lines = [name + " = INPUT" for name in input_names]
    emitted = {}

    def emit(n):
        if n.cost == 0:
            return n.name
        if n in emitted:
            return emitted[n]
        args = [emit(child) for child in n.children]
        name = "x" + str(len(lines))
        terms = [name, "=", n.op]
        if n.lam:
            terms.append(n.lam)
        terms.extend(args)
        lines.append(" ".join(terms))
        emitted[n] = name
        return name

    emit(expr)
    if len(lines) > admission.MAX_LINES:
        raise admission.Rejected("extracted program exceeds variable count")
    return " | ".join(lines)


def _evaluate(op: str, lam: str, children: tuple[Expr, ...], example_count: int):
    args = ([lam] if lam else []) + ["x" + str(i) for i in range(len(children))]
    statement = [("x9", op, args)]
    results = []
    for j in range(example_count):
        variables = {"x" + str(i): child.values[j]
                     for i, child in enumerate(children)}
        observed = admission.execute(statement, variables)
        if observed is None:
            return None
        results.append(observed)
    return tuple(results)


def synthesize(public: dict, *, seed: int, max_nodes: int = 3,
               max_evals: int = 3000, max_width: int = 220) -> dict:
    """Only public I/O crosses this interface; never reference/evaluator data."""
    if not 1 <= max_nodes <= 6 or not 1 <= max_evals <= 2_000_000:
        raise ValueError("unsafe search budget")
    if not 2 <= max_width <= 20_000:
        raise ValueError("unsafe search width")
    if set(public) - {
        "status", "task_id", "inputs", "outputs", "input_output_examples",
        "target_program_exposed", "source_blob"
    }:
        raise admission.Rejected("search input contains unapproved fields")
    if public.get("target_program_exposed") is not False:
        raise admission.Rejected("target program custody not established")
    names, types, n = admission.validate_examples(public)
    rng = random.Random(seed)
    expected = _signature(public["outputs"])
    levels = [dict(I=[], L=[]) for _ in range(max_nodes + 1)]
    dedup = {"I": set(), "L": set()}
    for name in names:
        expr = Expr(types[name], tuple(public["inputs"][name]), 0, name=name)
        levels[0][expr.typ].append(expr)
        dedup[expr.typ].add(_signature(expr.values))
    counters = {"attempts": 0, "valid_expressions": 0,
                "new_observational_states": 0, "signature_collisions": 0,
                "invalid_intermediates": 0, "extraction_rejections": 0}
    found = None
    stage_evals = [0 for _ in range(max_nodes + 1)]
    # Keep a per-depth budget rather than permitting a single combinatorial
    # family to consume the entire experiment at depth two.
    per_layer = max(1, max_evals // max_nodes)
    start_wall, start_cpu = time.perf_counter(), time.process_time()

    def attempt(op, lam, children, depth):
        nonlocal found
        if counters["attempts"] >= max_evals or stage_evals[depth] >= per_layer:
            return False
        counters["attempts"] += 1
        stage_evals[depth] += 1
        values = _evaluate(op, lam, children, n)
        if values is None:
            counters["invalid_intermediates"] += 1
            return True
        counters["valid_expressions"] += 1
        typ = admission.OPERATIONS[op][1]
        expr = Expr(typ, values, depth, op=op, lam=lam, children=children)
        if _signature(values) == expected:
            try:
                program = extract(expr, names)
                code = admission.compile_program(program, names, types)
                if all(admission.execute(code, {key: public["inputs"][key][j]
                                                for key in names}) == public["outputs"][j]
                       for j in range(n)):
                    found = program
                    return False
            except admission.Rejected:
                counters["extraction_rejections"] += 1
        sig = _signature(values)
        if sig in dedup[typ]:
            counters["signature_collisions"] += 1
            return True
        dedup[typ].add(sig)
        if len(levels[depth][typ]) < max_width:
            levels[depth][typ].append(expr)
            counters["new_observational_states"] += 1
        return True

    for depth in range(1, max_nodes + 1):
        budget = min(per_layer, max_evals - counters["attempts"])
        if budget <= 0:
            break
        unary_budget = max(1, budget // 2)
        ops = list(UNARY_OPS)
        rng.shuffle(ops)
        per_unary_family = max(1, unary_budget // len(ops))
        for op, lam, child_type in ops:
            if found or stage_evals[depth] >= unary_budget:
                break
            pool = list(levels[depth - 1][child_type])
            rng.shuffle(pool)
            for child in pool[:per_unary_family]:
                if not attempt(op, lam, (child,), depth):
                    break
            if found:
                break
        if found:
            break
        if depth == 1:
            # Binary ops with both inputs at zero cost are legitimate.
            pass
        families = []
        for op, lam, left_type, right_type in BINARY_OPS:
            for left_cost in range(depth):
                right_cost = depth - 1 - left_cost
                families.append((op, lam, left_type, right_type,
                                 left_cost, right_cost))
        rng.shuffle(families)
        binary_budget = budget - stage_evals[depth]
        per_family = max(1, binary_budget // max(1, len(families)))
        for op, lam, left_typ, right_typ, lc, rc in families:
            if found or stage_evals[depth] >= budget:
                break
            left = list(levels[lc][left_typ])
            right = list(levels[rc][right_typ])
            rng.shuffle(left)
            rng.shuffle(right)
            for children in itertools.islice(itertools.product(left, right), per_family):
                if not attempt(op, lam, children, depth):
                    break
            if found:
                break
        if found:
            break

    elapsed_wall = time.perf_counter() - start_wall
    elapsed_cpu = time.process_time() - start_cpu
    return {
        "status": "PUBLIC_IO_CANDIDATE_FOUND" if found else "BOUNDED_SEARCH_NO_CANDIDATE",
        "program": found,
        "program_sha256": hashlib.sha256(found.encode()).hexdigest() if found else None,
        "seed": seed,
        "budget": {"max_nodes": max_nodes, "max_evals": max_evals,
                   "max_width_per_type_per_depth": max_width},
        "counts": {**counters, "per_layer_attempts": stage_evals[1:],
                   "retained_by_depth": [{k: len(v) for k, v in group.items()}
                                         for group in levels]},
        "synthesis_wall_seconds": elapsed_wall,
        "synthesis_cpu_seconds": elapsed_cpu,
        "rss_peak_kib_process": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "source_leakage_controls": "participant_view only; no source program, model gradients, or verifier queries in search",
    }


def _list_argument(raw: str, allowed: set, label: str):
    items = raw.split(",")
    if not items or len(set(items)) != len(items) or any(x not in allowed for x in items):
        raise ValueError("invalid " + label)
    return items


def run(splits: list[str], indices: list[int], seeds: list[int], *,
        cache: Path, offline: bool, max_nodes: int,
        max_evals: int, max_width: int, probes: int) -> dict:
    # Preflight every source lock before any search; avoids partial silent cohorts.
    sources = {}
    for split in splits:
        rows, blob = admission.source_rows(split, cache, offline=offline)
        sources[split] = (rows, blob)
        for index in indices:
            if not 0 <= index < len(rows):
                raise admission.Rejected("task index outside manifest")
    wall_start, cpu_start = time.perf_counter(), time.process_time()
    records = []
    for split in splits:
        rows, blob = sources[split]
        for index in indices:
            # The search receives only the exact public projection, not the
            # referenced target program from the source rows.
            public = admission.participant_view(split, rows[index])
            public["source_blob"] = blob
            public_hash = hashlib.sha256(json.dumps(
                public, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
            for seed in seeds:
                synthesized = synthesize(
                    public, seed=seed, max_nodes=max_nodes,
                    max_evals=max_evals, max_width=max_width)
                candidate = synthesized.pop("program")
                evaluation = None
                eval_wall = 0.
                if candidate is not None:
                    t = time.perf_counter()
                    evaluation = admission.verify(
                        split, index, candidate, cache, offline=True, probes=probes)
                    eval_wall = time.perf_counter() - t
                records.append({
                    "task_id": public["task_id"], "split": split, "index": index,
                    "reference_operations_evaluator_only":
                        len(rows[index]["test_problem"]["program"].split("|")) - len(public["inputs"]),
                    "seed": seed, "source_git_blob_sha": blob,
                    "public_projection_sha256": public_hash,
                    "search": synthesized,
                    "extracted_program": candidate,
                    "evaluator": evaluation,
                    "evaluator_wall_seconds": eval_wall,
                    "bounded_verified": evaluation is not None and
                        evaluation["status"] == "BOUNDED_EXECUTION_AGREEMENT_ONLY",
                })
    by_split = {}
    for split in splits:
        r = [v for v in records if v["split"] == split]
        by_split[split] = {
            "evaluated_cases": len(r), "public_io_candidates": sum(
                x["search"]["status"] == "PUBLIC_IO_CANDIDATE_FOUND" for x in r),
            "bounded_verified_cases": sum(x["bounded_verified"] for x in r),
        }
    return {
        "schema": "gcl.owi-ds002.exedec-enumerative-pbe.v1",
        "status": "INITIAL_OUTCOME_ONLY_ENUMERATOR_EVALUATED",
        "source_revision": admission.manifest()["origin"]["commit"],
        "protocol": {"splits": splits, "indices": indices, "seeds": seeds,
                     "max_nodes": max_nodes, "max_evals": max_evals,
                     "max_width": max_width, "evaluator_probes": probes,
                     "public_reference_program_used_for_search": False},
        "aggregate": {
            "cases": len(records),
            "public_io_candidates": sum(r["extracted_program"] is not None
                                        for r in records),
            "bounded_verified": sum(r["bounded_verified"] for r in records),
            "sum_search_attempts": sum(r["search"]["counts"]["attempts"] for r in records),
            "sum_synthesis_cpu_seconds": sum(r["search"]["synthesis_cpu_seconds"]
                                             for r in records),
            "sum_synthesis_wall_seconds": sum(r["search"]["synthesis_wall_seconds"]
                                              for r in records),
            "sum_evaluator_wall_seconds": sum(r["evaluator_wall_seconds"] for r in records),
            "end_to_end_wall_seconds": time.perf_counter() - wall_start,
            "end_to_end_cpu_seconds": time.process_time() - cpu_start,
            "rss_peak_kib_process": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        },
        "by_split": by_split, "records": records,
        "limitations": [
            "A bounded enumerative-search baseline; not a mature external DeepCoder solver",
            "Source reference programs are publicly distributed; no secret blind holdout",
            "Verification consists of published I/O and bounded evaluator-only reference agreement, not universal proof",
            "Finite observational dedup may discard extensionally distinct programs",
            "One subprocess, sequential cases; peak resident memory is process-level, not per-task",
            "Search budget is bounded candidate evaluations, not equal full compute across A/B/C/D",
            "No learned policy, chosen JVP, smooth/discrete differential bridge or causal intervention model",
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--splits", default=",".join(DEFAULT_SPLITS))
    ap.add_argument("--indices", default=",".join(map(str, DEFAULT_INDICES)))
    ap.add_argument("--seeds", default=",".join(map(str, DEFAULT_SEEDS)))
    ap.add_argument("--max-nodes", type=int, default=3)
    ap.add_argument("--max-evals", type=int, default=3000)
    ap.add_argument("--max-width", type=int, default=220)
    ap.add_argument("--probes", type=int, default=16)
    ap.add_argument("--cache-dir", default="build/owi_ds002/exedec_sources")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    try:
        splits = _list_argument(args.splits, set(DEFAULT_SPLITS), "splits")
        indices = [int(x) for x in args.indices.split(",")]
        seeds = [int(x) for x in args.seeds.split(",")]
        if (len(set(indices)) != len(indices) or
                len(set(seeds)) != len(seeds) or
                not 1 <= len(indices) <= 50 or not 1 <= len(seeds) <= 20 or
                any(i < 0 for i in indices) or any(not 0 <= s < 2**32 for s in seeds)):
            raise ValueError("invalid indices/seeds")
        result = run(splits, indices, seeds, cache=Path(args.cache_dir),
                     offline=args.offline, max_nodes=args.max_nodes,
                     max_evals=args.max_evals, max_width=args.max_width,
                     probes=args.probes)
    except (OSError, ValueError, admission.Rejected) as exc:
        result = {"status": "REJECTED_OR_INCONCLUSIVE", "error": str(exc)}
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "records"},
                     sort_keys=True, indent=2))
    return 0 if result["status"] == "INITIAL_OUTCOME_ONLY_ENUMERATOR_EVALUATED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
