#!/usr/bin/env python3
"""Source-locked PUBLIC-only task-variant discovery in three train families.

Auditor may read full raw corpus for cryptographic integrity and grouped
partition but never disclose private verifier, hidden state, source class
or any held-out development/test task. Training-policy code does not import
this module; survey is expressly experimental design, not learned supervision.
"""
from __future__ import annotations
import argparse, json
from collections import defaultdict
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_intake import DatasetBoundaryError,public_view
from owi_ec005_realtools_split import partition

def survey(rows,anchors=(0,2,3),limit=16):
    if not 1<=limit<=30 or len(anchors)!=len(set(anchors)):
        raise DatasetBoundaryError("invalid selection bound")
    split=partition(rows,seed=4611)
    train={r["row_index"]:r for r in split["partitions"]["train"]}
    if any(i not in train for i in anchors):
        raise DatasetBoundaryError("nontraining anchor")
    groups=defaultdict(list)
    for row in train.values():
        groups[row["environment_id_sha256"]].append(row)
    out=[]
    for i in anchors:
        fam=train[i]["environment_id_sha256"]
        variants=sorted(groups[fam],key=lambda v:v["row_index"])
        selected=variants[:limit]
        for item in selected:
            j=item["row_index"]
            public=public_view(rows[j])
            prompt=" ".join(m["content"] for m in public["messages"]
                            if m["role"]=="user")
            if not isinstance(prompt,str) or not prompt:
                raise DatasetBoundaryError("missing public task")
            tool_names=[t["function"]["name"] for t in
                       rows[j]["extra_info"]["environment"]["tools"]]
            out.append({"anchor":i,"index":j,"family_sha256":fam,
                        "family_task_count":len(variants),
                        "public_task_excerpt":prompt[:1100],
                        "public_task_sha256":item["public_prompt_sha256"],
                        "public_tool_names":sorted(tool_names),
                        "partition":"train",
                        "private_state_source_verifier_exported":False})
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    ap.add_argument("--limit",type=int,default=16)
    args=ap.parse_args()
    rows=audit_source(json.loads(args.lock.read_text()))
    result=survey(rows,limit=args.limit)
    for item in result:
        print("PUBLIC_TRAIN_FAMILY_VARIANT",json.dumps(item,sort_keys=True,
                     ensure_ascii=False))
    print("PUBLIC_TRAIN_VARIANT_AUDIT",json.dumps({
        "family_anchors":[0,2,3],"returned":len(result),
        "source_digest_verified":True,
        "heldout_dev_test_family_prompts_exported":False,
        "private_payload_exported":False},sort_keys=True))

if __name__=="__main__":
    main()
