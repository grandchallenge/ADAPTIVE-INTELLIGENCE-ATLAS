#!/usr/bin/env python3
"""Trusted HOST selector: export one pinned, verifier-free real-tool environment.

Outputs private task payload only to ephemeral runner workspace. This selected
payload is mounted read-only in a network-disabled restricted child container.
No untrusted class code is imported, compiled or executed by this process.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

from owi_ec005_realtools_intake import DatasetBoundaryError, FILE, REPO, MAX_BYTES, MAX_LINE, remote_lines


def eligible_methods(env):
    tree = ast.parse(env["class_code"])
    defined = {m.name for c in ast.walk(tree) if isinstance(c, ast.ClassDef)
               for m in c.body if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef))}
    for tool in env["tools"]:
        fn = tool.get("function", {})
        name = fn.get("name")
        parameters = fn.get("parameters", {})
        if (isinstance(name, str) and name in defined
                and name.startswith(("list_", "get_", "find_", "search_"))
                and isinstance(parameters, dict)
                and not parameters.get("required", [])):
            yield name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lock", type=Path,
                    default=Path("governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    ap.add_argument("--output", type=Path, required=True)
    a = ap.parse_args()
    lock = json.loads(a.lock.read_text())
    if lock["repository"] != REPO or lock["filename"] != FILE:
        raise DatasetBoundaryError("incorrect source identity")
    selected = None
    digest = hashlib.sha256()
    count = 0
    size = 0
    for line in remote_lines(lock["revision"]):
        digest.update(line)
        size += len(line)
        if len(line) > MAX_LINE or size > MAX_BYTES:
            raise DatasetBoundaryError("source size violation")
        if not line.strip():
            continue
        row = json.loads(line)
        env = row["extra_info"]["environment"]
        if selected is None and list(eligible_methods(env)):
            selected = (count, {k: env[k] for k in
                        ("class_code", "class_name", "initial_state", "tools")})
        count += 1
    if digest.hexdigest() != lock["sha256"] or count != lock["observed_tasks"]:
        raise DatasetBoundaryError("untrusted dataset source drift")
    if selected is None:
        raise DatasetBoundaryError("no eligible real tool")
    index, payload = selected
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(payload, sort_keys=True))
    a.output.chmod(0o644)  # sandbox unprivileged user can read mounted file
    class_hash = hashlib.sha256(payload["class_code"].encode()).hexdigest()
    print(json.dumps({
        "source_revision": lock["revision"],
        "dataset_verified": True,
        "record_index": index,
        "class_code_sha256": class_hash,
        "eligible_read_tool_names": list(eligible_methods(payload)),
        "payload_keys": sorted(payload),
        "verifier_present": False,
        "reflection_skills_present": False,
        "training": "NOT_PERFORMED",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
