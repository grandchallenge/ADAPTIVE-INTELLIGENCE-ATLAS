#!/usr/bin/env python3
"""OWI-EC-005: source-locked intake for *real* executable tool-use tasks.

This module NEVER executes dataset-provided code. It never publishes prompts,
environment code, verifier logic or reflection skills to its agent-facing view.
It is a provenance/leakage gate, not a trained tool agent or science result.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

REPO = "dongguanting/Agent-Reflex-RL-2K"
FILE = "train_envscaler_2550_with_skills.jsonl"
REVISION = re.compile(r"^[a-f0-9]{40}$")
MAX_BYTES = 256 * 1024 * 1024
MAX_LINE = 16 * 1024 * 1024
PRIVATE = frozenset({"extra_info", "reward_model", "rsd_skill", "rsd_skills",
                     "rsd_skill_meta", "environment", "verifier", "patch",
                     "test_patch", "gold_solution", "fault_identity"})


class DatasetBoundaryError(ValueError):
    pass


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")


def public_view(row: dict) -> dict:
    """Only public system/user prompt messages; no tool code or answers.

    The executable tool schema must be separately declared after a source audit;
    blindly exposing extra_info.environment would leak hidden state and code.
    """
    if not isinstance(row, dict) or not isinstance(row.get("prompt"), list):
        raise DatasetBoundaryError("invalid prompt shape")
    messages = []
    for m in row["prompt"]:
        if (not isinstance(m, dict) or m.get("role") not in ("system", "user")
                or not isinstance(m.get("content"), str)
                or set(m) - {"role", "content"}):
            raise DatasetBoundaryError("unexpected prompt message; stop intake")
        messages.append({"role": m["role"], "content": m["content"]})
    if not messages or not any(m["role"] == "user" for m in messages):
        raise DatasetBoundaryError("missing public user task")
    result = {"messages": messages}
    if any(key in result for key in PRIVATE):
        raise DatasetBoundaryError("private field in public view")
    return result


def private_inventory(row: dict) -> dict:
    x = row.get("extra_info")
    if not isinstance(x, dict) or "environment" not in x or "verifier" not in x:
        raise DatasetBoundaryError("missing executable environment/verifier")
    # Fingerprints use full private payload without leaking it to the agent.
    env = x["environment"]
    checksum = hashlib.sha256(canonical(env)).hexdigest()
    key_types = ({k: type(v).__name__ for k, v in env.items()}
                 if isinstance(env, dict) else {})
    return {"environment_type": type(env).__name__,
            "verifier_type": type(x["verifier"]).__name__,
            "private_keys": sorted(x),
            "environment_top_key_types": key_types,
            "environment_sha256": checksum,
            "has_skill_fields": any("skill" in k.lower() for k in x)}


def audit_lines(lines: Iterable[bytes], *, sha256_expected: str = "",
                source_revision: str = "offline-fixture") -> dict:
    """Process streamed JSONL with bounded per-row memory and no code execution."""
    source_hash = hashlib.sha256()
    counts = Counter()
    seen = set()
    environment_types = Counter()
    verifier_types = Counter()
    key_types = Counter()
    byte_count = 0
    sample_ids = []
    for index, raw in enumerate(lines):
        if len(raw) > MAX_LINE:
            raise DatasetBoundaryError(f"oversized task record at {index+1}")
        byte_count += len(raw)
        if byte_count > MAX_BYTES:
            raise DatasetBoundaryError("dataset exceeds source size bound")
        source_hash.update(raw)
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except ValueError as ex:
            raise DatasetBoundaryError(f"invalid JSONL record {index+1}") from ex
        view = public_view(row)
        internal = private_inventory(row)
        if any(k in row for k in ("rsd_skill", "rsd_skills", "rsd_skill_meta")):
            # Allowed in source file, never in training view.
            counts["source_top_level_skill_fields"] += 1
        if any(k in internal["private_keys"] for k in ("rsd_skill", "rsd_skills", "rsd_skill_meta")):
            counts["source_private_skill_fields"] += 1
        encoded = canonical(view)
        if b'"extra_info"' in encoded or b'"verifier"' in encoded or b'"rsd_skill"' in encoded:
            raise DatasetBoundaryError("private key serialization leaked")
        fingerprint = hashlib.sha256(encoded).hexdigest()
        if fingerprint in seen:
            counts["repeated_public_prompts"] += 1
        seen.add(fingerprint)
        if len(sample_ids) < 10:
            sample_ids.append(fingerprint[:16])
        counts["valid_tasks"] += 1
        counts["public_message_total"] += len(view["messages"])
        environment_types[internal["environment_type"]] += 1
        verifier_types[internal["verifier_type"]] += 1
        for key, type_name in internal["environment_top_key_types"].items():
            key_types[f"{key}:{type_name}"] += 1
        if internal["has_skill_fields"]:
            counts["private_skill_bearing_records"] += 1
    actual = source_hash.hexdigest()
    if sha256_expected and actual != sha256_expected:
        raise DatasetBoundaryError("source raw-byte SHA256 mismatch")
    if not counts["valid_tasks"]:
        raise DatasetBoundaryError("empty source dataset")
    return {"contract": "OWI-EC005-TOOL-DATA-INVENTORY/1",
            "source": REPO, "filename": FILE, "revision": source_revision,
            "raw_file_sha256": actual, "raw_bytes": byte_count,
            "counts": dict(sorted(counts.items())),
            "environment_types": dict(sorted(environment_types.items())),
            "verifier_types": dict(sorted(verifier_types.items())),
            "environment_top_key_types": dict(sorted(key_types.items())),
            "first_public_prompt_fingerprints": sample_ids,
            "no_private_payload_published": True,
            "code_execution": "none",
            "scientific_acceptance": "NOT_EVALUATED",
            "training": "NOT_PERFORMED"}


def discover_revision() -> str:
    url = f"https://huggingface.co/api/datasets/{REPO}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        obj = json.load(resp)
    rev = obj.get("sha")
    if not isinstance(rev, str) or not REVISION.fullmatch(rev):
        raise DatasetBoundaryError("remote revision was not a 40-hex SHA")
    return rev


def remote_lines(revision: str):
    if not REVISION.fullmatch(revision):
        raise DatasetBoundaryError("revision must be a fixed 40-hex commit")
    url = f"https://huggingface.co/datasets/{REPO}/resolve/{revision}/{FILE}"
    # The resolved response is only consumed as data, never imported/executed.
    with urllib.request.urlopen(url, timeout=120) as stream:
        for raw in stream:
            yield raw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--revision", required=False,
                    help="Pinned HF source SHA; if omitted, discover then pin in report")
    ap.add_argument("--source-file", type=Path,
                    help="Local JSONL for offline tests, no network")
    ap.add_argument("--source-sha256", default="")
    ap.add_argument("--source-lock", type=Path,
                    default=Path("governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    ap.add_argument("--output", type=Path,
                    default=Path("build/owi_ec005_realtools/source_inventory.json"))
    args = ap.parse_args()
    pinned_sha = args.source_sha256
    if args.source_file:
        revision = args.revision or "offline-fixture"
    else:
        if args.source_lock.exists():
            lock = json.loads(args.source_lock.read_text())
            if (lock.get("repository") != REPO or lock.get("filename") != FILE
                    or not REVISION.fullmatch(lock.get("revision", ""))
                    or not re.fullmatch(r"[a-f0-9]{64}", lock.get("sha256", ""))):
                raise DatasetBoundaryError("invalid pinned dataset lock")
            if args.revision and args.revision != lock["revision"]:
                raise DatasetBoundaryError("requested revision differs from source lock")
            if pinned_sha and pinned_sha != lock["sha256"]:
                raise DatasetBoundaryError("requested digest differs from source lock")
            revision, pinned_sha = lock["revision"], lock["sha256"]
        else:
            if not args.revision:
                raise DatasetBoundaryError("missing source lock or explicit pinned revision")
            revision = args.revision
    if args.source_file:
        with args.source_file.open("rb") as f:
            record = audit_lines(f, sha256_expected=pinned_sha,
                                 source_revision=revision)
    else:
        record = audit_lines(remote_lines(revision),
                             sha256_expected=pinned_sha,
                             source_revision=revision)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, sort_keys=True, indent=2) + "\n")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
