#!/usr/bin/env python3
"""Create sealed public / untrusted environment / private checker bundles.

Only training environment families may enter exploratory intervention trials.
Full 2,550-task source digest and union-find class/env-family partition checked
BEFORE writing any bundles. Test/dev family tasks cannot be selected. Unlike
the earlier single-task smoke selector, this does not require a no-arg read API.
No source code is evaluated by this script.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_split import partition
from owi_ec005_realtools_intake import DatasetBoundaryError, public_view, canonical
from owi_ec005_realtools_episode_select import write_json

def build(rows, indices, *, seed=4611):
    p=partition(rows,seed=seed)
    training={x["row_index"]:x for x in p["partitions"]["train"]}
    if not indices or len(indices)>8 or len(set(indices))!=len(indices):
        raise DatasetBoundaryError("bounded unique indices required")
    families=set()
    outputs=[]
    for i in indices:
        if i not in training:
            raise DatasetBoundaryError("nontraining family requested")
        fam=training[i]["environment_id_sha256"]
        if fam in families:
            raise DatasetBoundaryError("family overlap in trial cohort")
        families.add(fam)
        row=rows[i]
        extra=row.get("extra_info")
        if not isinstance(extra,dict):
            raise DatasetBoundaryError("missing separated source payloads")
        env, verifier=extra.get("environment"),extra.get("verifier")
        if not isinstance(env,dict) or not isinstance(verifier,dict):
            raise DatasetBoundaryError("invalid private payloads")
        if verifier.get("kind")!="checklist_func" or not isinstance(
                verifier.get("checklist"),list) or not verifier["checklist"]:
            raise DatasetBoundaryError("unsupported terminal checker")
        expected={"class_code","class_name","initial_state","tools"}
        if not all(k in env for k in expected):
            raise DatasetBoundaryError("missing executable task field")
        public=public_view(row)
        tools=[]
        for t in env["tools"]:
            fn=t.get("function",{}) if isinstance(t,dict) else {}
            if not isinstance(fn,dict) or not isinstance(fn.get("name"),str):
                raise DatasetBoundaryError("invalid tool declaration")
            tools.append({"name":fn["name"],"parameters":fn.get("parameters",{})})
        public["tools"]=tools
        outputs.append((i,fam,public,{k:env[k] for k in expected},
                        {"verifier":verifier}))
    return outputs

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--indices",default="0,2,3")
    ap.add_argument("--output-dir",type=Path,required=True)
    ap.add_argument("--lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    args=ap.parse_args()
    lock=json.loads(args.lock.read_text())
    rows=audit_source(lock)
    chosen=build(rows,[int(x) for x in args.indices.split(",")])
    for index,fam,public,env,private in chosen:
        target=args.output_dir/str(index)
        write_json(target/"public.json",public)
        write_json(target/"environment.json",env)
        write_json(target/"verifier.json",private)
        print("SEALED_TRAIN_TASK",json.dumps({
            "index":index,"partition":"train",
            "family_id_sha256":fam,
            "public_task_sha256":hashlib.sha256(canonical(public)).hexdigest(),
            "environment_source_sha256":hashlib.sha256(
                env["class_code"].encode()).hexdigest(),
            "private_checker_count":len(private["verifier"]["checklist"]),
            "private_payload_exported_to_actor":False,
            "source_sha256":lock["sha256"],
            "execution_performed":False},sort_keys=True))
if __name__=="__main__":
    main()
