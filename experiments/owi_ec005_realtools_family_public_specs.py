#!/usr/bin/env python3
"""Exact public task and tool signatures for predeclared *training* families.

No private verifier/hidden class/state or reference solution is observed,
printed, or exported. Selection requires the source-locked partition to mark
every requested index as training, and distinct family identities.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_intake import DatasetBoundaryError,public_view
from owi_ec005_realtools_split import partition

def select(rows, indices, *, seed=4611):
    p=partition(rows,seed=seed)
    train={x["row_index"]:x for x in p["partitions"]["train"]}
    if not indices or len(indices)>8 or len(set(indices))!=len(indices):
        raise DatasetBoundaryError("invalid public task selection")
    families=set()
    tasks=[]
    for i in indices:
        if i not in train:
            raise DatasetBoundaryError("requested index not a training family")
        family=train[i]["environment_id_sha256"]
        if family in families:
            raise DatasetBoundaryError("selected duplicate environment family")
        families.add(family)
        public=public_view(rows[i])
        env=rows[i]["extra_info"]["environment"]
        tools=[]
        for t in env["tools"]:
            fn=t.get("function",{}) if isinstance(t,dict) else {}
            if not isinstance(fn,dict) or not isinstance(fn.get("name"),str):
                raise DatasetBoundaryError("invalid declared tool")
            tools.append({
                "name":fn["name"],
                "parameters":fn.get("parameters",{}),
                "description":str(fn.get("description",""))[:280],
            })
        tasks.append({
            "index":i,"partition":"train",
            "family_id_sha256":family,
            "public_prompt_sha256":train[i]["public_prompt_sha256"],
            "public_task":" ".join(m["content"] for m in public["messages"]
                                   if m["role"]=="user")[:4000],
            "public_tools":tools,
            "hidden_state_exposed":False,
            "verifier_exposed":False,
            "environment_source_executed":False,
        })
    return tasks

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--indices",default="0,2,3")
    ap.add_argument("--lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    args=ap.parse_args()
    indices=[int(x) for x in args.indices.split(",")]
    rows=audit_source(json.loads(args.lock.read_text()))
    for item in select(rows,indices):
        print("PREDECLARED_TRAIN_PUBLIC",json.dumps(item,sort_keys=True,
                                                   ensure_ascii=False))
if __name__=="__main__":
    main()
