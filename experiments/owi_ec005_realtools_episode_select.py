#!/usr/bin/env python3
"""Select one exact pinned real task into three disjoint private/public bundles.

No dataset source code is executed. Complete source digest is verified before
any selected payload is written. The public bundle carries only task messages
and declared tool function interface metadata, never initial_state/verifier or
reflection skills. Private files are ephemeral, never uploaded as CI artifacts.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from owi_ec005_realtools_intake import (
    DatasetBoundaryError, FILE, REPO, MAX_BYTES, MAX_LINE, canonical,
    public_view, remote_lines
)
from owi_ec005_realtools_select import eligible_methods

def choose(lock, index):
    if (lock.get("repository") != REPO or lock.get("filename") != FILE
            or not 0 <= index < lock.get("observed_tasks", 0)):
        raise DatasetBoundaryError("source identity/index mismatch")
    digest = hashlib.sha256()
    size, count, selected = 0, 0, None
    for raw in remote_lines(lock["revision"]):
        digest.update(raw)
        size += len(raw)
        if len(raw) > MAX_LINE or size > MAX_BYTES:
            raise DatasetBoundaryError("source size bound exceeded")
        if not raw.strip():
            continue
        if count == index:
            selected = json.loads(raw)
        count += 1
    if (digest.hexdigest() != lock["sha256"] or size != lock["size_bytes"]
            or count != lock["observed_tasks"] or selected is None):
        raise DatasetBoundaryError("pinned corpus digest/length drift")
    return selected

def split_selected(row):
    public = public_view(row)
    extra = row.get("extra_info", {})
    if not isinstance(extra, dict):
        raise DatasetBoundaryError("no private bundle")
    env, verifier = extra.get("environment"), extra.get("verifier")
    if not isinstance(env, dict) or not isinstance(verifier, dict):
        raise DatasetBoundaryError("missing env or verifier")
    if verifier.get("kind") != "checklist_func" or not verifier.get("checklist"):
        raise DatasetBoundaryError("unsupported private verification contract")
    read_candidates = list(eligible_methods(env))
    if not read_candidates:
        raise DatasetBoundaryError("no declared compatible read-only tool")
    environment = {k: env[k] for k in
                   ("class_code", "class_name", "initial_state", "tools")}
    private = {"verifier": verifier}
    names = [t["function"]["name"] for t in env["tools"]
             if isinstance(t, dict) and t.get("type") == "function"]
    tools = []
    for t in env["tools"]:
        fn = t["function"]
        tools.append({"name": fn["name"], "parameters": fn.get("parameters", {})})
    public["tools"] = tools
    public["candidate_read_tool"] = read_candidates[0]
    if not all(k not in public for k in
               ("extra_info", "verifier", "initial_state", "class_code",
                "rsd_skill", "rsd_skills", "rsd_skill_meta")):
        raise DatasetBoundaryError("private payload in public bundle")
    return public, environment, private

def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, sort_keys=True, ensure_ascii=False),
                    encoding="utf-8")
    path.chmod(0o444)  # UID 65534 in Docker must be able to read bind mount

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--row-index", type=int, default=1)
    ap.add_argument("--lock", type=Path, default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    ap.add_argument("--destination", type=Path, required=True)
    a = ap.parse_args()
    lock = json.loads(a.lock.read_text())
    row = choose(lock, a.row_index)
    public, env, private = split_selected(row)
    write_json(a.destination / "public.json", public)
    write_json(a.destination / "environment.json", env)
    write_json(a.destination / "verifier.json", private)
    print(json.dumps({
        "contract": "OWI-EC005-PRIVATE-SELECTOR/1",
        "row_index": a.row_index, "source_sha256": lock["sha256"],
        "source_revision": lock["revision"],
        "public_sha256": hashlib.sha256(canonical(public)).hexdigest(),
        "environment_class_sha256": hashlib.sha256(env["class_code"].encode()).hexdigest(),
        "candidate_read_tool": public["candidate_read_tool"],
        "private_check_count": len(private["verifier"]["checklist"]),
        "private_fields_exposed": False, "task_executed": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
