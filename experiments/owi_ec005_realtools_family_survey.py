#!/usr/bin/env python3
"""OWI-EC005F: sealed-family, public-only discovery of real tool tasks.

Reads full pinned dataset bytes and verifies source digest before deriving
grouped train/dev/test partition. NEVER executes third-party code, NEVER
prints or saves test-family prompts, private initial state, checker/skill
code, or gold data. The test families are sealed before task selection.

Discovery reports are not a trained policy nor causal evidence.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import defaultdict, Counter
from pathlib import Path
from owi_ec005_realtools_intake import (
    DatasetBoundaryError, MAX_BYTES, MAX_LINE, REPO, FILE,
    public_view, remote_lines
)
from owi_ec005_realtools_split import partition


def audit_source(lock, *, lines=None):
    if (lock.get("repository") != REPO or lock.get("filename") != FILE
            or not isinstance(lock.get("observed_tasks"), int)):
        raise DatasetBoundaryError("source lock mismatch")
    digest = hashlib.sha256()
    rows, size = [], 0
    stream = remote_lines(lock["revision"]) if lines is None else lines
    for raw in stream:
        size += len(raw)
        if len(raw) > MAX_LINE or size > MAX_BYTES:
            raise DatasetBoundaryError("source size violation")
        digest.update(raw)
        if raw.strip():
            rows.append(json.loads(raw))
    if (digest.hexdigest() != lock["sha256"] or
            size != lock["size_bytes"] or
            len(rows) != lock["observed_tasks"]):
        raise DatasetBoundaryError("source identity/corpus count drift")
    return rows


def public_family_survey(rows, *, seed=4611, example_limit=2):
    if not 1 <= example_limit <= 3:
        raise DatasetBoundaryError("example bound must be 1..3")
    split=partition(rows,seed=seed)
    findings=[]
    summary={}
    for name in ("train","dev"):
        groups=defaultdict(list)
        for item in split["partitions"][name]:
            groups[item["environment_id_sha256"]].append(item)
        counts=Counter()
        for envhash, group in sorted(groups.items()):
            sample=sorted(group,key=lambda x:x["row_index"])[:example_limit]
            examples=[]
            for item in sample:
                i=item["row_index"]
                public=public_view(rows[i])
                env=rows[i]["extra_info"]["environment"]
                methods=[]
                for t in env.get("tools",[]):
                    if not isinstance(t,dict) or t.get("type")!="function":
                        raise DatasetBoundaryError("invalid public tool schema")
                    fn=t.get("function")
                    if not isinstance(fn,dict) or not isinstance(fn.get("name"),str):
                        raise DatasetBoundaryError("tool schema drift")
                    methods.append(fn["name"])
                if not methods:
                    raise DatasetBoundaryError("missing declared tools")
                counts["sampled_tasks"]+=1
                counts["public_tool_occurrences"]+=len(methods)
                counts["declared_read_occurrences"]+=sum(
                    name.startswith(("list_","get_","find_","search_"))
                    for name in methods)
                prompt=" ".join(x["content"] for x in public["messages"]
                                if x["role"]=="user")
                examples.append({
                    "row_index":i,
                    "public_prompt_sha256":item["public_prompt_sha256"],
                    "public_prompt_excerpt":prompt[:500],
                    "public_tool_names":sorted(set(methods)),
                })
            findings.append({
                "partition":name, "family_id_sha256":envhash,
                "group_task_count":len(group),
                "representatives":examples,
            })
        summary[name]=dict(counts)
    return {
        "contract":"OWI-EC005F-PUBLIC-FAMILY-SURVEY/1",
        "split_seed":seed,
        "source_digest_verified":True,
        "train_families":split["partition_group_counts"]["train"],
        "dev_families":split["partition_group_counts"]["dev"],
        "sealed_test_families":split["partition_group_counts"]["test"],
        "test_prompts_or_tools_inspected":False,
        "private_source_or_verifier_exported":False,
        "task_execution":"NONE",
        "outcome_learning":"NOT_PERFORMED",
        "summary":summary,
        "families":findings,
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    ap.add_argument("--output",type=Path,default=Path(
        "build/owi_ec005_realtools/heterogeneous_survey.json"))
    ap.add_argument("--examples-per-family",type=int,default=2)
    args=ap.parse_args()
    lock=json.loads(args.lock.read_text())
    rows=audit_source(lock)
    report=public_family_survey(rows,example_limit=args.examples_per_family)
    report["source_revision"]=lock["revision"]
    report["source_raw_sha256"]=lock["sha256"]
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    # Bounded public metadata only; no test task description or private code.
    for group in report["families"]:
        print("PUBLIC_FAMILY",json.dumps(group,sort_keys=True,ensure_ascii=False))
    print("FAMILY_AUDIT",json.dumps({
        k:v for k,v in report.items() if k!="families"},sort_keys=True))


if __name__=="__main__":
    main()
