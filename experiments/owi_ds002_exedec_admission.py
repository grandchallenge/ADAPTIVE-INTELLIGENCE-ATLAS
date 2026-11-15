#!/usr/bin/env python3
"""OWI-DS-002: bounded non-executing verifier for source-locked ExeDec DeepCoder tasks.

External task/reference-program custody is at pinned google-deepmind/exedec.
This module implements an independently written, typed DSL interpreter; it
NEVER execs/evals generated Python or invokes user-provided shell commands.
Success means finite bounded test agreement, NOT universal program equivalence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import random
import re
import tempfile
import time
import urllib.request

MANIFEST = Path(__file__).with_name("owi_ds002_exedec_manifest.json")
OPERATIONS = {
    "Head": ("L", "I"), "Last": ("L", "I"),
    "Take": ("IL", "L"), "Drop": ("IL", "L"), "Access": ("IL", "I"),
    "Minimum": ("L", "I"), "Maximum": ("L", "I"),
    "Reverse": ("L", "L"), "Sort": ("L", "L"), "Sum": ("L", "I"),
    "Map": ("UL", "L"), "Filter": ("PL", "L"), "Count": ("PL", "I"),
    "ZipWith": ("BLL", "L"), "Scanl1": ("BL", "L"),
}
UNARY = {"(+1)": lambda x: x + 1, "(-1)": lambda x: x - 1,
         "(*2)": lambda x: x * 2, "(/2)": lambda x: x // 2,
         "(*(-1))": lambda x: -x, "(**2)": lambda x: x * x,
         "(*3)": lambda x: x * 3, "(/3)": lambda x: x // 3,
         "(*4)": lambda x: x * 4, "(/4)": lambda x: x // 4}
PRED = {"(>0)": lambda x: x > 0, "(<0)": lambda x: x < 0,
        "(%2==0)": lambda x: x % 2 == 0,
        "(%2==1)": lambda x: x % 2 == 1}
BINARY = {"(+)": lambda a, b: a + b, "(-)": lambda a, b: a - b,
          "(*)": lambda a, b: a * b, "(min)": min, "(max)": max}
VAR = re.compile(r"x[0-9]\Z")
MAX_BYTES = 350_000
MAX_LINES = 10
MAX_LIST = 5
MAX_ABS = 50


class Rejected(ValueError):
    pass


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def manifest() -> dict:
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if m.get("schema") != "gcl.owi-ds002.exedec-deepcoder-source-lock.v1":
        raise Rejected("unexpected manifest schema")
    if m["origin"] != {
        "repository": "google-deepmind/exedec",
        "commit": "ef046ce2cc3fcd024e32f5dfe00e69700dac82ed",
    }:
        raise Rejected("source provenance drift")
    if set(m["splits"]) != {
        "NONE", "LENGTH_GENERALIZATION", "COMPOSE_DIFFERENT_CONCEPTS",
        "SWITCH_CONCEPT_ORDER", "COMPOSE_NEW_OP", "ADD_OP_FUNCTIONALITY",
    }:
        raise Rejected("missing/extra split")
    for split, row in m["splits"].items():
        if row["path"] != "data/llm_data/deepcoder/" + split + ".jsonl":
            raise Rejected("unsafe source path")
        if not re.fullmatch(r"[a-f0-9]{40}", row["git_blob_sha"]):
            raise Rejected("bad source blob identity")
        if row["count"] != 200:
            raise Rejected("split count drift")
    return m


def source_rows(split: str, cache: Path, offline: bool = False) -> tuple[list[dict], str]:
    m = manifest()
    if split not in m["splits"]:
        raise Rejected("unknown split")
    row = m["splits"][split]
    cache.mkdir(parents=True, exist_ok=True)
    target = cache / (split + ".jsonl")
    if target.exists():
        raw = target.read_bytes()
    else:
        if offline:
            raise Rejected("offline source not cached")
        url = ("https://raw.githubusercontent.com/" + m["origin"]["repository"]
               + "/" + m["origin"]["commit"] + "/" + row["path"])
        with urllib.request.urlopen(url, timeout=20) as response:
            raw = response.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES or git_blob(raw) != row["git_blob_sha"]:
            raise Rejected("downloaded source hash/size mismatch: " + split + " expected=" + row["git_blob_sha"] + " observed=" + git_blob(raw) + " size=" + str(len(raw)))
        with tempfile.NamedTemporaryFile(dir=cache, delete=False) as tmp:
            tmp.write(raw)
            tmp_path = Path(tmp.name)
        tmp_path.replace(target)
    if len(raw) > MAX_BYTES or git_blob(raw) != row["git_blob_sha"]:
        raise Rejected("cached source hash/size mismatch: " + split + " observed=" + git_blob(raw))
    rows = [json.loads(line) for line in raw.decode("utf-8").splitlines()]
    if len(rows) != row["count"] or [r.get("index") for r in rows] != list(range(row["count"])):
        raise Rejected("missing, reordered or duplicate source tasks")
    for r in rows:
        p = r.get("test_problem")
        if not isinstance(p, dict) or set(p) != {"inputs", "outputs", "program"}:
            raise Rejected("unexpected test_problem schema")
        if not isinstance(r.get("few_shot_examples"), list) or len(r["few_shot_examples"]) != 4:
            raise Rejected("few-shot corpus schema drift")
    return rows, row["git_blob_sha"]


def kind(x) -> str:
    if type(x) is int and -MAX_ABS <= x <= MAX_ABS:
        return "I"
    if (type(x) is list and len(x) <= MAX_LIST and
            all(type(v) is int and -MAX_ABS <= v <= MAX_ABS for v in x)):
        return "L"
    raise Rejected("unsupported/out-of-bound integer or list")


def validate_examples(problem: dict) -> tuple[list[str], dict[str, str], int]:
    inp = problem["inputs"]
    out = problem["outputs"]
    if not isinstance(inp, dict) or not 1 <= len(inp) <= 3:
        raise Rejected("unsupported input count")
    names = list(inp)
    if names != ["x" + str(i) for i in range(len(names))]:
        raise Rejected("noncanonical input names")
    if not isinstance(out, list) or not 1 <= len(out) <= 32:
        raise Rejected("unsupported example count")
    types = {}
    for v, batch in inp.items():
        if not isinstance(batch, list) or len(batch) != len(out):
            raise Rejected("invalid input batches")
        observed = {kind(x) for x in batch}
        if len(observed) != 1:
            raise Rejected("inconsistent input types")
        types[v] = next(iter(observed))
    for x in out:
        kind(x)
    return names, types, len(out)


def compile_program(src: str, names: list[str], types: dict[str, str]) -> list[tuple]:
    if not isinstance(src, str) or len(src) > 2048 or "\n" in src:
        raise Rejected("invalid program source")
    lines = [part.strip().split() for part in src.split("|")]
    if not len(names) < len(lines) <= MAX_LINES:
        raise Rejected("program must have bounded nonempty statements")
    code = []
    local_types = dict(types)
    for i, toks in enumerate(lines):
        dest = "x" + str(i)
        if len(toks) < 3 or toks[:2] != [dest, "="] or not VAR.fullmatch(dest):
            raise Rejected("malformed, reordered or reused variable")
        if i < len(names):
            if toks != [dest, "=", "INPUT"]:
                raise Rejected("input declaration mismatch")
            continue
        op = toks[2]
        if op not in OPERATIONS:
            raise Rejected("unknown operation")
        signature, out_type = OPERATIONS[op]
        args = toks[3:]
        if len(args) != len(signature):
            raise Rejected("operation arity mismatch")
        for token, required in zip(args, signature):
            if required == "U" and token not in UNARY:
                raise Rejected("illegal unary lambda")
            elif required == "P" and token not in PRED:
                raise Rejected("illegal predicate")
            elif required == "B" and token not in BINARY:
                raise Rejected("illegal binary lambda")
            elif required in ("I", "L") and local_types.get(token) != required:
                raise Rejected("unbound or wrongly typed input variable")
        code.append((dest, op, args))
        local_types[dest] = out_type
    return code


def execute(code: list[tuple], values: dict) -> int | list[int] | None:
    env = dict(values)
    for dest, op, arg in code:
        def v(i):
            return env[arg[i]]
        result = None
        if op == "Head":
            result = v(0)[0] if v(0) else None
        elif op == "Last":
            result = v(0)[-1] if v(0) else None
        elif op == "Access":
            result = v(1)[v(0)] if 0 <= v(0) < len(v(1)) else None
        elif op == "Minimum":
            result = min(v(0)) if v(0) else None
        elif op == "Maximum":
            result = max(v(0)) if v(0) else None
        elif op == "Take":
            result = v(1)[:v(0)]
        elif op == "Drop":
            result = v(1)[v(0):]
        elif op == "Reverse":
            result = list(reversed(v(0)))
        elif op == "Sort":
            result = sorted(v(0))
        elif op == "Sum":
            result = sum(v(0))
        elif op == "Map":
            result = [UNARY[arg[0]](x) for x in v(1)]
        elif op == "Filter":
            result = [x for x in v(1) if PRED[arg[0]](x)]
        elif op == "Count":
            result = sum(bool(PRED[arg[0]](x)) for x in v(1))
        elif op == "ZipWith":
            result = [BINARY[arg[0]](a, b) for a, b in zip(v(1), v(2))]
        elif op == "Scanl1":
            result = []
            for x in v(1):
                result.append(x if not result else BINARY[arg[0]](result[-1], x))
        else:
            raise Rejected("unreachable operation")
        if result is None:
            return None
        try:
            kind(result)  # Every *intermediate* must obey original ExeDec bounds.
        except Rejected:
            return None
        env[dest] = result
    return result


def examples(problem: dict):
    names, types, n = validate_examples(problem)
    for j in range(n):
        yield {v: problem["inputs"][v][j] for v in names}, problem["outputs"][j]


def participant_view(split: str, record: dict) -> dict:
    # Strict projection: target program and few-shot solution programs are withheld.
    p = record["test_problem"]
    return {"task_id": split + ":" + str(record["index"]),
            "inputs": p["inputs"], "outputs": p["outputs"],
            "input_output_examples": len(p["outputs"]),
            "target_program_exposed": False}


def source_audit(cache: Path, offline: bool) -> dict:
    result = {"source_revision": manifest()["origin"]["commit"], "splits": {},
              "reference_examples_checked": 0}
    for split in sorted(manifest()["splits"]):
        rows, digest = source_rows(split, cache, offline)
        for row in rows:
            p = row["test_problem"]
            names, typ, n = validate_examples(p)
            code = compile_program(p["program"], names, typ)
            for inp, expected in examples(p):
                if execute(code, inp) != expected:
                    raise Rejected("source/reference semantic disagreement: "
                                   + split + ":" + str(row["index"]))
                result["reference_examples_checked"] += 1
        result["splits"][split] = {"tasks": len(rows), "blob": digest}
    result["status"] = "SOURCE_LOCK_AND_REFERENCE_REPLAY_PASS"
    return result


def generated_inputs(problem: dict, seed: int):
    """Deterministic fresh inputs, shaped like the declared examples, evaluator-only."""
    rng = random.Random(seed)
    names, _, n = validate_examples(problem)
    for _ in range(1024):
        j = rng.randrange(n)
        values = {}
        for name in names:
            example = problem["inputs"][name][j]
            if type(example) is int:
                values[name] = rng.randint(-6, 6)
            else:
                values[name] = [rng.randint(-6, 6) for _ in range(len(example))]
        yield values


def verify(split: str, index: int, candidate: str, cache: Path,
           offline: bool = False, probes: int = 16) -> dict:
    if not 1 <= probes <= 128:
        raise Rejected("invalid probe count")
    rows, blob = source_rows(split, cache, offline)
    if not 0 <= index < len(rows):
        raise Rejected("task index outside source lock")
    p = rows[index]["test_problem"]
    names, typ, n = validate_examples(p)
    reference = compile_program(p["program"], names, typ)
    code = compile_program(candidate, names, typ)
    common = {"task_id": split + ":" + str(index), "source_blob": blob,
              "source_revision": manifest()["origin"]["commit"],
              "reference_sha256": hashlib.sha256(p["program"].encode()).hexdigest(),
              "candidate_sha256": hashlib.sha256(candidate.encode()).hexdigest(),
              "source_examples": n, "independent_valid_cases": 0,
              "probe_budget": probes, "status": "INCONCLUSIVE"}
    for inp, expected in examples(p):
        if execute(reference, inp) != expected:
            raise Rejected("source reference did not reproduce source output")
        if execute(code, inp) != expected:
            common["status"] = "REJECTED_PUBLIC_COUNTEREXAMPLE"
            return common
    seed = int(hashlib.sha256((blob + ":" + str(index)).encode()).hexdigest()[:16], 16)
    seen = set()
    for inp in generated_inputs(p, seed):
        key = json.dumps(inp, sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        expected = execute(reference, inp)
        if expected is None:
            continue
        common["independent_valid_cases"] += 1
        if execute(code, inp) != expected:
            common["status"] = "REJECTED_EVALUATOR_COUNTEREXAMPLE"
            return common
        if common["independent_valid_cases"] >= probes:
            common["status"] = "BOUNDED_EXECUTION_AGREEMENT_ONLY"
            return common
    common["status"] = "INCONCLUSIVE_INSUFFICIENT_VALID_PROBES"
    return common


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", required=True, choices=["audit", "preview", "verify"])
    ap.add_argument("--split", default="LENGTH_GENERALIZATION")
    ap.add_argument("--index", type=int, default=0)
    ap.add_argument("--candidate", default="", help="typed DSL, never Python code")
    ap.add_argument("--cache-dir", default="build/owi_ds002/exedec_sources")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--probes", type=int, default=16)
    ap.add_argument("--output", default="")
    args = ap.parse_args()
    start = time.perf_counter()
    try:
        cache = Path(args.cache_dir)
        if args.mode == "audit":
            result = source_audit(cache, args.offline)
        elif args.mode == "preview":
            rows, blob = source_rows(args.split, cache, args.offline)
            if not 0 <= args.index < len(rows):
                raise Rejected("invalid source task")
            result = participant_view(args.split, rows[args.index])
            result["source_blob"] = blob
        else:
            result = verify(args.split, args.index, args.candidate,
                            cache, args.offline, args.probes)
    except (Rejected, OSError, UnicodeError, ValueError) as exc:
        result = {"status": "REJECTED_OR_INCONCLUSIVE", "error": str(exc)}
    result["verification_wall_seconds"] = round(time.perf_counter() - start, 6)
    result["scientific_limit"] = ("Source-pinned examples and bounded executable "
        "reference-agreement probes; not a formal equivalence proof. "
        "No differential learner, no smooth/discrete derivative, no equal-compute comparison.")
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] in (
        "SOURCE_LOCK_AND_REFERENCE_REPLAY_PASS", "BOUNDED_EXECUTION_AGREEMENT_ONLY"
    ) or args.mode == "preview" and result.get("target_program_exposed") is False else 2


if __name__ == "__main__":
    raise SystemExit(main())
