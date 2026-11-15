#!/usr/bin/env python3
"""Independent-implementation semantic conformance versus pinned ExeDec DSL.

This trusted CI-only lane imports a hash-verified upstream reference module.
It does not execute candidate programs as Python and is not a synthesis solver.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import time
import urllib.request

import owi_ds002_exedec_admission as local


def replay(cache: Path, generated_per_task: int) -> dict:
    if not 0 <= generated_per_task <= 64:
        raise local.Rejected("invalid generated-per-task budget")
    m = local.manifest()
    original = m["reference_semantics"]
    url = ("https://raw.githubusercontent.com/" + m["origin"]["repository"] + "/"
           + m["origin"]["commit"] + "/" + original["path"])
    with urllib.request.urlopen(url, timeout=20) as response:
        code = response.read(local.MAX_BYTES + 1)
    if len(code) > local.MAX_BYTES or local.git_blob(code) != original["git_blob_sha"]:
        raise local.Rejected("pinned upstream executable DSL hash mismatch")
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "deepcoder_dsl.py"
        path.write_bytes(code)
        spec = importlib.util.spec_from_file_location("upstream_exedec_pinned", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Upstream uses absl flags as defaults for intermediate value bounds.
        from absl import flags
        if not flags.FLAGS.is_parsed():
            flags.FLAGS(["owi-ds002-semantic-audit"])
        total_tasks = 0
        fixed_cases = 0
        generated_cases = 0
        for split in sorted(m["splits"]):
            rows, _ = local.source_rows(split, cache, offline=True)
            for row in rows:
                p = row["test_problem"]
                names, types, _ = local.validate_examples(p)
                local_code = local.compile_program(p["program"], names, types)
                upstream = module.Program.from_str(p["program"])
                if upstream.input_variables != names:
                    raise local.Rejected("upstream input-binding mismatch")
                inputs = [x for x, _ in local.examples(p)]
                base_seed = int(hashlib.sha256(
                    (split + ":" + str(row["index"])).encode()).hexdigest()[:16], 16)
                inputs += list(local.generated_inputs(p, base_seed))[:generated_per_task]
                for case_index, values in enumerate(inputs):
                    state = upstream.run([values[k] for k in names])
                    expected = None if state is None else state.get_output()
                    observed = local.execute(local_code, values)
                    if type(expected) != type(observed) or expected != observed:
                        raise local.Rejected(
                            "independent interpreter mismatch split=" + split
                            + " task=" + str(row["index"])
                            + " case=" + str(case_index)
                            + " upstream=" + repr(expected)
                            + " local=" + repr(observed))
                    if case_index < len(p["outputs"]):
                        fixed_cases += 1
                    else:
                        generated_cases += 1
                total_tasks += 1
    return {
        "status": "BOUNDED_UPSTREAM_INTERPRETER_CONCORDANCE",
        "source_revision": m["origin"]["commit"],
        "upstream_dsl_blob": original["git_blob_sha"],
        "tasks": total_tasks,
        "published_example_comparisons": fixed_cases,
        "generated_example_comparisons": generated_cases,
        "generated_seed_rule": "sha256(split + ':' + index) first 64 bits",
        "scientific_limits": (
            "Two implementations agree on finite chosen inputs only. "
            "Upstream source is executable only after exact blob check. "
            "No universal equivalence or legal differentiable-program interpretation.")
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache-dir", default="build/owi_ds002/exedec_sources")
    ap.add_argument("--generated-per-task", type=int, default=8)
    ap.add_argument("--output", default="")
    args = ap.parse_args()
    start = time.perf_counter()
    try:
        result = replay(Path(args.cache_dir), args.generated_per_task)
    except (OSError, ValueError, RuntimeError) as exc:
        result = {"status": "REJECTED_OR_INCONCLUSIVE", "error": str(exc)}
    result["wall_seconds"] = round(time.perf_counter()-start, 6)
    if args.output:
        file = Path(args.output)
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0 if result["status"] == "BOUNDED_UPSTREAM_INTERPRETER_CONCORDANCE" else 2


if __name__ == "__main__":
    raise SystemExit(main())
