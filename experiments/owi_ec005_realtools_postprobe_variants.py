#!/usr/bin/env python3
"""Produce controlled source-class-preserving account-state variants.

This is a PRIVILEGED fixture preparer, not a policy. It authenticates entire
pinned source, rejects non-training task, and alters precisely one element of
the initial-state JSON for the targeted account. The executable class source,
public prompt/tool schemas and the original private verifier are unchanged.
The variants are CONTROLLED TEST SCENARIOS, NOT authentic original corpus
tasks; keep their provenance explicit in every measurement.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path

from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_family_prepare import build
from owi_ec005_realtools_episode_select import write_json
from owi_ec005_realtools_intake import DatasetBoundaryError,canonical

INDEX=2
ACCOUNT="USR002"
STATUS_KEY=("users",ACCOUNT,"account_status")
VARIANTS=("suspended","active","closed")
TRAIN_VARIANTS=("suspended","active")
HELDOUT_VARIANT="closed"

def with_status(env,status):
    if status not in VARIANTS:
        raise DatasetBoundaryError("unapproved controlled state")
    if not isinstance(env,dict) or set(env)!={
            "class_code","class_name","initial_state","tools"}:
        raise DatasetBoundaryError("invalid sealed source code envelope")
    state=env["initial_state"]
    if not isinstance(state,dict) or not isinstance(state.get("users"),dict):
        raise DatasetBoundaryError("state schema drift")
    target=state["users"].get(ACCOUNT)
    if (not isinstance(target,dict) or target.get("account_status")!="suspended"
            or target.get("_id")!=ACCOUNT):
        raise DatasetBoundaryError("original target status/identity changed")
    cloned=copy.deepcopy(env)
    cloned["initial_state"]["users"][ACCOUNT]["account_status"]=status
    assert env["class_code"]==cloned["class_code"]
    assert env["tools"]==cloned["tools"]
    for other,val in state.items():
        if other!="users":
            assert cloned["initial_state"][other]==val
    for user,record in state["users"].items():
        if user!=ACCOUNT:
            assert cloned["initial_state"]["users"][user]==record
        else:
            for field,value in record.items():
                if field!="account_status":
                    assert cloned["initial_state"]["users"][user][field]==value
    return cloned

def prepare(rows,target):
    chosen=build(rows,[INDEX])
    if len(chosen)!=1 or chosen[0][0]!=INDEX:
        raise DatasetBoundaryError("source-locked row selection changed")
    i,fam,public,env,private=chosen[0]
    before=hashlib.sha256(canonical(env["initial_state"])).hexdigest()
    codehash=hashlib.sha256(env["class_code"].encode()).hexdigest()
    receipts={}
    for status in VARIANTS:
        scenario=with_status(env,status)
        folder=target/status
        write_json(folder/"public.json",public)
        write_json(folder/"environment.json",scenario)
        write_json(folder/"verifier.json",private)
        receipts[status]={
            "initial_state_sha256":hashlib.sha256(
                canonical(scenario["initial_state"])).hexdigest(),
            "executable_class_sha256":codehash,
            "verifier_code_sha256":hashlib.sha256(
                canonical(private)).hexdigest(),
            "changed_state_path":list(STATUS_KEY),
            "initial_state_controlled_not_original":status!="suspended",
            "train_variant":status in TRAIN_VARIANTS,
        }
    return {
        "contract":"OWI-EC005H-CONTROLLED-SOURCE-CLASS-VARIANTS/1",
        "original_row_index":INDEX,
        "split":"train",
        "original_environment_family_sha256":fam,
        "original_initial_state_sha256":before,
        "source_code_and_private_verifier_unchanged":True,
        "public_task_and_tool_schemas_unchanged":True,
        "scripted_state_variation_not_an_authentic_corpus_task":True,
        "train_variants":list(TRAIN_VARIANTS),
        "holdout_mechanism_variant":HELDOUT_VARIANT,
        "receipts":receipts,
        "private_checker_or_hidden_source_released_to_learner":False,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output-dir",type=Path,required=True)
    ap.add_argument("--lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    args=ap.parse_args()
    source_lock=json.loads(args.lock.read_text())
    rows=audit_source(source_lock)
    result=prepare(rows,args.output_dir)
    result["pinned_raw_source_sha256"]=source_lock["sha256"]
    write_json(args.output_dir/"variant_manifest.json",result)
    print("CONTROLLED_VARIANT_PROVENANCE",json.dumps(result,sort_keys=True))
if __name__=="__main__":
    main()
