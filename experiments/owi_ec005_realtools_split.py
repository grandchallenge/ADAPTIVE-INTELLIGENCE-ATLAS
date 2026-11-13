#!/usr/bin/env python3
"""Leakage-resistant environment-family split for pinned REAL tool-use tasks.

Group by connected components of env_id AND executable class_code digest.
This prevents code/template identity from leaking across train/dev/test.
No tool code, verifier, supervision or raw prompt is written to output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

from owi_ec005_realtools_intake import (
    DatasetBoundaryError, FILE, REPO, MAX_BYTES, MAX_LINE,
    canonical, public_view, remote_lines,
)


def sha(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, item):
        self.parent.setdefault(item, item)
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, a, b):
        x, y = self.find(a), self.find(b)
        self.parent[max(x, y)] = min(x, y)


def partition(rows: list[dict], *, seed: int = 4611) -> dict:
    if seed < 0:
        raise DatasetBoundaryError("negative split seed")
    uf = UnionFind()
    fingerprints = set()
    members = []
    id_counts, code_counts = Counter(), Counter()
    for i, row in enumerate(rows):
        public = public_view(row)
        env = row["extra_info"]["environment"]
        if not isinstance(env, dict) or not isinstance(env.get("class_code"), str):
            raise DatasetBoundaryError("missing executable class code")
        e = env.get("env_id")
        if not isinstance(e, str) or not e:
            raise DatasetBoundaryError("missing stable environment ID")
        envhash, codehash = sha(e), hashlib.sha256(env["class_code"].encode()).hexdigest()
        # Code identity and environment identity are both protected, even
        # where the dataset reuses one under multiple other IDs.
        uf.union("env:" + envhash, "code:" + codehash)
        id_counts[envhash] += 1
        code_counts[codehash] += 1
        fingerprint = sha(public)
        if fingerprint in fingerprints:
            raise DatasetBoundaryError("duplicate public prompt across samples")
        fingerprints.add(fingerprint)
        members.append((fingerprint, envhash, codehash, i))
    groups = defaultdict(list)
    for fingerprint, envhash, codehash, i in members:
        groups[uf.find("env:" + envhash)].append((fingerprint, envhash, codehash, i))
    if len(groups) < 5:
        raise DatasetBoundaryError("too few independent environments for grouped split")
    # Stable seeded hash order; no global RNG dependence or task-level shuffle.
    ranked = sorted(groups, key=lambda k: hashlib.sha256(
        f"{seed}/{k}".encode()).hexdigest())
    n = len(ranked)
    ntrain = int(n * 0.6)
    ndev = int(n * 0.2)
    assignment = {}
    for i, k in enumerate(ranked):
        assignment[k] = ("train" if i < ntrain else
                         "dev" if i < ntrain + ndev else "test")
    by_split = {name: [] for name in ("train", "dev", "test")}
    for k, tasks in groups.items():
        for fp, envhash, codehash, row_index in tasks:
            by_split[assignment[k]].append({
                "row_index": row_index, "public_prompt_sha256": fp,
                "environment_id_sha256": envhash, "class_code_sha256": codehash,
            })
    for name in by_split:
        by_split[name].sort(key=lambda r: r["row_index"])
        if not by_split[name]:
            raise DatasetBoundaryError(f"empty {name} split")
    # Mechanically prove both no environment IDs and no class code cross splits.
    for field in ("environment_id_sha256", "class_code_sha256",
                  "public_prompt_sha256"):
        sig = [{x[field] for x in by_split[split]}
               for split in ("train", "dev", "test")]
        if any(sig[i] & sig[j] for i in range(3) for j in range(i+1, 3)):
            raise DatasetBoundaryError(f"cross-partition {field} leakage")
    return {
        "contract": "OWI-EC005-REALTOOL-GROUP-SPLIT/1",
        "seed": seed, "source": REPO, "filename": FILE,
        "raw_task_count": len(rows),
        "independent_connected_environment_families": n,
        "distinct_env_ids": len(id_counts),
        "distinct_class_code_bodies": len(code_counts),
        "environment_family_size_histogram": dict(sorted(Counter(
            len(x) for x in groups.values()).items())),
        "partition_group_counts": dict(Counter(assignment.values())),
        "partition_task_counts": {k: len(v) for k, v in by_split.items()},
        "partitions": by_split,
        "invariants": {
            "no_shared_public_prompts": True,
            "no_shared_environment_ids": True,
            "no_shared_class_code": True,
            "class_code_not_exported": True,
            "verifier_not_exported": True,
            "reflection_skills_not_exported": True,
        },
        "outcome_training": "NOT_PERFORMED",
        "intervention_evaluation": "NOT_PERFORMED",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lock", type=Path,
                    default=Path("governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    ap.add_argument("--seed", type=int, default=4611)
    ap.add_argument("--output", type=Path,
                    default=Path("build/owi_ec005_realtools/group_split.json"))
    args = ap.parse_args()
    lock = json.loads(args.lock.read_text())
    if lock["repository"] != REPO or lock["filename"] != FILE:
        raise DatasetBoundaryError("source lock identity mismatch")
    h = hashlib.sha256()
    rows = []
    size = 0
    for raw in remote_lines(lock["revision"]):
        size += len(raw)
        if len(raw) > MAX_LINE or size > MAX_BYTES:
            raise DatasetBoundaryError("bounded source size exceeded")
        h.update(raw)
        if raw.strip():
            rows.append(json.loads(raw))
    if h.hexdigest() != lock["sha256"] or len(rows) != lock["observed_tasks"]:
        raise DatasetBoundaryError("source revision/digest/count not locked")
    report = partition(rows, seed=args.seed)
    report["source_revision"] = lock["revision"]
    report["source_raw_sha256"] = lock["sha256"]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items()
                      if k != "partitions"}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
