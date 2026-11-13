#!/usr/bin/env python3
"""Static schema and Python-AST audit of pinned, UNTRUSTED real tool environments.

No exec, eval, compile, imports from dataset or dataset-controlled subprocess.
Only public interface metadata and structural counts are retained.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from collections import Counter
from pathlib import Path

from owi_ec005_realtools_intake import (
    DatasetBoundaryError, REPO, FILE, MAX_BYTES, MAX_LINE, canonical,
    public_view, remote_lines,
)

ALLOWED_NAMES = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
MAX_CODE_CHARS = 500_000


def shape(row: dict) -> dict:
    public_view(row)
    info = row["extra_info"]
    env, verifier = info["environment"], info["verifier"]
    if not (isinstance(env, dict) and isinstance(verifier, dict)):
        raise DatasetBoundaryError("invalid private environment/verifier shape")
    if not isinstance(env.get("class_code"), str):
        raise DatasetBoundaryError("missing environment source code")
    code = env["class_code"]
    if len(code) > MAX_CODE_CHARS:
        raise DatasetBoundaryError("environment code too long for AST audit")
    tree = ast.parse(code)  # parse only, NEVER compile or execute
    functions = [n.name for c in ast.walk(tree) if isinstance(c, ast.ClassDef)
                 for n in c.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    imports = [n for n in ast.walk(tree)
               if isinstance(n, (ast.Import, ast.ImportFrom))]
    tools = env.get("tools")
    if not isinstance(tools, list):
        raise DatasetBoundaryError("missing declared tools list")
    tool_shapes = []
    for t in tools:
        if not isinstance(t, dict):
            raise DatasetBoundaryError("non-dict declared tool")
        tool_shapes.append(tuple(sorted(
            k + ":" + type(v).__name__ for k, v in t.items()
            if isinstance(k, str) and len(k) < 90 and set(k) <= ALLOWED_NAMES)))
    return {
        "env_keys": sorted(k for k in env if isinstance(k, str) and
                           len(k) < 90 and set(k) <= ALLOWED_NAMES),
        "verifier_field_types": sorted(
            k + ":" + type(v).__name__ for k, v in verifier.items()
            if isinstance(k, str) and len(k) < 90 and set(k) <= ALLOWED_NAMES),
        "tools_per_environment": len(tools),
        "tool_dict_shapes": tool_shapes,
        "top_level_imports": len(imports),
        "class_methods": sorted(set(functions)),
        "code_bytes": len(code.encode()),
    }


def run(revision: str, expected_digest: str, *, output: Path):
    source_digest = hashlib.sha256()
    seen_env = set()
    counts = Counter()
    tool_counts = Counter()
    methods = Counter()
    verifier = Counter()
    tool_shapes = Counter()
    env_keys = Counter()
    byte_count = 0
    for i, raw in enumerate(remote_lines(revision)):
        byte_count += len(raw)
        source_digest.update(raw)
        if len(raw) > MAX_LINE or byte_count > MAX_BYTES:
            raise DatasetBoundaryError("source bounded-size violation")
        if not raw.strip():
            continue
        record = json.loads(raw)
        r = shape(record)
        counts["records"] += 1
        counts["total_code_bytes"] += r["code_bytes"]
        counts["total_import_nodes"] += r["top_level_imports"]
        tool_counts[r["tools_per_environment"]] += 1
        methods.update(r["class_methods"])
        verifier.update(r["verifier_field_types"])
        env_keys.update(r["env_keys"])
        tool_shapes.update("/".join(s) for s in r["tool_dict_shapes"])
        identity = str(record["extra_info"]["environment"].get("env_id", ""))
        if identity in seen_env:
            counts["duplicate_env_ids"] += 1
        seen_env.add(identity)
    digest = source_digest.hexdigest()
    if digest != expected_digest:
        raise DatasetBoundaryError("source digest mismatch")
    if counts["records"] != 2550:
        raise DatasetBoundaryError("task count drift")
    report = {
        "contract": "OWI-EC005-REALTOOL-AST-AUDIT/1",
        "source": REPO, "filename": FILE, "revision": revision,
        "sha256": digest,
        "counts": dict(counts),
        "tool_counts": dict(sorted(tool_counts.items())),
        "environment_keys": dict(sorted(env_keys.items())),
        "verifier_field_types": dict(sorted(verifier.items())),
        "tool_dict_shapes": dict(sorted(tool_shapes.items())),
        "class_methods_top25": methods.most_common(25),
        "execution_performed": False,
        "interventions_performed": False,
        "scientific_learner": "NOT_TRAINED",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lock", type=Path,
                        default=Path("governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    parser.add_argument("--output", type=Path,
                        default=Path("build/owi_ec005_realtools/ast_schema.json"))
    args = parser.parse_args()
    lock = json.loads(args.lock.read_text())
    if lock["repository"] != REPO or lock["filename"] != FILE:
        raise DatasetBoundaryError("dataset lock source mismatch")
    result = run(lock["revision"], lock["sha256"], output=args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
