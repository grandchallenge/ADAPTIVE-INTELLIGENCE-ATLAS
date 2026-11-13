#!/usr/bin/env python3
"""Privileged, bounded source-locked subscription-state schema audit.

This preparatory AUDITOR sees the original private initial state only to
construct controlled environment variants. It never evaluates third-party
source code, publishes private checker text, or supplies the state to a
learning actor. Only field names, types and linked-ID shape are printed.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_family_prepare import build
from owi_ec005_realtools_intake import canonical, DatasetBoundaryError

ROW=0
USER="USR001"
TARGET_PRODUCT="PureView Daily Lens"

def find_related_records(env):
    state=env["initial_state"]
    if not isinstance(state,dict):
        raise DatasetBoundaryError("invalid source initial state")
    out={"initial_state_top_level_keys":sorted(state),
         "collection_shapes":{},
         "candidate_subscription_records":[]}
    for name,coll in state.items():
        if isinstance(coll,dict):
            samples=list(coll.items())[:2]
            out["collection_shapes"][name]={
                "kind":"mapping","entries":len(coll),
                "sample_record_field_names":[
                    sorted(v.keys()) if isinstance(v,dict) else []
                    for _,v in samples]}
        elif isinstance(coll,list):
            out["collection_shapes"][name]={
                "kind":"list","entries":len(coll),
                "sample_record_field_names":[
                    sorted(v.keys()) if isinstance(v,dict) else []
                    for v in coll[:2]]}
        else:
            out["collection_shapes"][name]={"kind":type(coll).__name__}
        if "subscri" in name.casefold():
            pairs=(list(coll.items()) if isinstance(coll,dict)
                   else list(enumerate(coll)) if isinstance(coll,list)
                   else [])
            for key,rec in pairs:
                if not isinstance(rec,dict):
                    continue
                # Emit only *schema* and non-sensitive target identity bits.
                out["candidate_subscription_records"].append({
                    "record_key_type":type(key).__name__,
                    "key_field_names":sorted(rec.keys()),
                    "key_looks_like_subscription_id":str(key).startswith(("SUB","sub")),
                    "user_id_matches_original_target":rec.get("user_id")==USER,
                    "subscription_status":rec.get("subscription_status"),
                    "product_id_present":isinstance(rec.get("product_id"),str),
                    "record_index_kind":type(key).__name__,
                })
    out["candidate_subscription_records"]=out["candidate_subscription_records"][:12]
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    ap.add_argument("--row",type=int,choices=(0,8),default=0)
    args=ap.parse_args()
    lock=json.loads(args.lock.read_text())
    rows=audit_source(lock)
    chosen=build(rows,[args.row])
    if len(chosen)!=1 or chosen[0][0]!=args.row:
        raise DatasetBoundaryError("source row drift")
    i,family,public,env,private=chosen[0]
    report=find_related_records(env)
    report.update({
        "contract":"OWI-EC005I-SUBSCRIPTION-STATE-AUDIT/1",
        "source_sha256":lock["sha256"],
        "source_row_index":args.row,
        "source_family_sha256":family,
        "public_sha256":hashlib.sha256(canonical(public)).hexdigest(),
        "external_class_sha256":hashlib.sha256(
            env["class_code"].encode()).hexdigest(),
        "private_verifier_sha256":hashlib.sha256(canonical(private)).hexdigest(),
        "private_verifier_code_exposed":False,
        "source_state_contents_exposed_to_policy":False,
        "source_class_executed_outside_jail":False})
    print("SOURCE_LOCKED_SUBSCRIPTION_AUDIT",json.dumps(report,sort_keys=True))

if __name__=="__main__":
    main()
