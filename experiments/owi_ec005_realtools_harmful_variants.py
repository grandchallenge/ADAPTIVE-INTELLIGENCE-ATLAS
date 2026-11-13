#!/usr/bin/env python3
"""Source-locked controlled subscription-association failures, privileged setup.

This fixture preparer may inspect source initial state but is NOT imported
by the learner. Execute no third-party code. Never pass variant labels,
initial-state differences, private checks or source contents to the actor.

Cases:
 VALID: original row-0 state, both links intact.
 USER_MISSING: remove only target user's key from users mapping; subscription
             and linked product remain intact.
 USER_ID_MISMATCH: change only target user record's _id to a nonmatching
             sentinel, preserving key; separate held-out mechanism diagnostic.
The verifier is exactly the original private checker, unchanged.
"""
from __future__ import annotations
import argparse,copy,hashlib,json
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_family_prepare import build
from owi_ec005_realtools_episode_select import write_json
from owi_ec005_realtools_intake import DatasetBoundaryError,canonical

ROW=0
USER="USR001"
PRODUCT_NAME="PureView Daily Lens"
VARIANTS=("valid","user_missing","user_id_mismatch")
TRAIN=("valid","user_missing")
HOLDOUT="user_id_mismatch"

def resolve_source_target(env):
    state=env["initial_state"]
    for name in ("users","subscriptions","products"):
        if not isinstance(state.get(name),dict):
            raise DatasetBoundaryError("controlled source schema drift")
    candidates=[]
    for sid,sub in state["subscriptions"].items():
        if not isinstance(sub,dict):
            continue
        pid=sub.get("product_id")
        product=state["products"].get(pid)
        if (sub.get("user_id")==USER and
            sub.get("subscription_status")=="active" and
            sub.get("recurrence_pattern")=="monthly" and
            isinstance(product,dict) and
            product.get("name")==PRODUCT_NAME and
            sub.get("subscription_id")==sid):
            candidates.append((sid,pid))
    if len(candidates)!=1:
        raise DatasetBoundaryError("target identity not unique in original source")
    if (USER not in state["users"] or
        state["users"][USER].get("_id")!=USER):
        raise DatasetBoundaryError("original target user record changed")
    return candidates[0]

def make_variant(env,scenario):
    if scenario not in VARIANTS:
        raise DatasetBoundaryError("undeclared link intervention")
    target,pid=resolve_source_target(env)
    clone=copy.deepcopy(env)
    if scenario=="user_missing":
        del clone["initial_state"]["users"][USER]
    elif scenario=="user_id_mismatch":
        clone["initial_state"]["users"][USER]["_id"]="__CONTROLLED_BROKEN_LINK__"
    if any(clone[k]!=env[k] for k in ("class_code","class_name","tools")):
        raise DatasetBoundaryError("external executable source was modified")
    if (clone["initial_state"]["subscriptions"]!=env["initial_state"]["subscriptions"]
        or clone["initial_state"]["products"]!=env["initial_state"]["products"]):
        raise DatasetBoundaryError("subscription or product target was modified")
    for key in ("payments","shipments","init_config"):
        if clone["initial_state"].get(key)!=env["initial_state"].get(key):
            raise DatasetBoundaryError("external records changed unexpectedly")
    for key,item in env["initial_state"]["users"].items():
        if key==USER:
            continue
        if clone["initial_state"]["users"][key]!=item:
            raise DatasetBoundaryError("non-target user record changed")
    return clone

def prepare(rows,output):
    chosen=build(rows,[ROW])
    _,family,public,env,private=chosen[0]
    target,pid=resolve_source_target(env)
    target_sha=hashlib.sha256(target.encode()).hexdigest()
    private_sha=hashlib.sha256(canonical(private)).hexdigest()
    code_sha=hashlib.sha256(env["class_code"].encode()).hexdigest()
    out={}
    for scenario in VARIANTS:
        variant=make_variant(env,scenario)
        d=output/scenario
        write_json(d/"public.json",public)
        write_json(d/"environment.json",variant)
        write_json(d/"verifier.json",private)
        out[scenario]={
            "initial_state_sha256":hashlib.sha256(canonical(
                variant["initial_state"])).hexdigest(),
            "target_subscription_id_sha256":target_sha,
            "external_class_sha256":code_sha,
            "private_verifier_sha256":private_sha,
            "alteration":"none" if scenario=="valid"
                else ("users target key removal" if scenario=="user_missing"
                    else "users target _id mismatch"),
            "artificial_controlled_initial_state":scenario!="valid",
            "used_for_learning":scenario in TRAIN,
        }
    return {"contract":"OWI-EC005I-SUBSCRIPTION-CONTROLLED-LINK/1",
            "source_row":ROW,"source_training_family_sha256":family,
            "public_description_sha256":hashlib.sha256(canonical(public)).hexdigest(),
            "public_text_and_tools_constant":True,
            "source_class_and_original_checker_constant":True,
            "target_identity_never_sent_to_policy":True,
            "synthetic_interventions_not_independent_source_tasks":True,
            "train_variants":list(TRAIN),"reserved_variant":HOLDOUT,
            "variant_receipts":out}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output-dir",type=Path,required=True)
    p.add_argument("--lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    a=p.parse_args()
    lock=json.loads(a.lock.read_text())
    data=audit_source(lock)
    manifest=prepare(data,a.output_dir)
    manifest["pinned_raw_source_sha256"]=lock["sha256"]
    write_json(a.output_dir/"manifest.json",manifest)
    print("SUBSCRIPTION_LINK_VARIANT_CUSTODY",json.dumps(manifest,sort_keys=True))

if __name__=="__main__":
    main()
