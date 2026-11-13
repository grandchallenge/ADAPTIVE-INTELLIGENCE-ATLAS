#!/usr/bin/env python3
"""Prepare row-8, publicly identified SUB1234 association failures.

Fixture setup only; NEVER an actor feature. Full source pin and training
grouping are verified before changes. The original external class, public
request/tool signatures, and private verifier remain byte-identical. Each
controlled variant deletes exactly one referenced linked-object map entry.
Held-out mechanism is product record deletion (not seen during training).
"""
from __future__ import annotations
import argparse,copy,hashlib,json,re
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_family_prepare import build
from owi_ec005_realtools_episode_select import write_json
from owi_ec005_realtools_intake import DatasetBoundaryError,canonical

ROW=8
TARGET="SUB1234"
VARIANTS=("valid","missing_user","missing_product")
TRAIN=("valid","missing_user")
MECHANISM_HOLDOUT="missing_product"

def target_fields(env):
    state=env["initial_state"]
    if not isinstance(state,dict) or any(not isinstance(state.get(k),dict)
                                        for k in ("subscriptions","users","products")):
        raise DatasetBoundaryError("unexpected linkable source schema")
    target=state["subscriptions"].get(TARGET)
    if not isinstance(target,dict) or target.get("subscription_id")!=TARGET:
        raise DatasetBoundaryError("source target ID absent or drifted")
    if target.get("subscription_status")!="active":
        raise DatasetBoundaryError("source target not active")
    uid,pid=target.get("user_id"),target.get("product_id")
    if uid not in state["users"] or pid not in state["products"]:
        raise DatasetBoundaryError("original source target link not complete")
    return uid,pid

def make_variant(env,name):
    if name not in VARIANTS:
        raise DatasetBoundaryError("unsupported association intervention")
    uid,pid=target_fields(env)
    copy_env=copy.deepcopy(env)
    st=copy_env["initial_state"]
    if name=="missing_user":
        del st["users"][uid]
    elif name=="missing_product":
        del st["products"][pid]
    if any(copy_env[k]!=env[k] for k in ("class_code","class_name","tools")):
        raise DatasetBoundaryError("source code/tool schema changed")
    for k in env["initial_state"]:
        if k not in ("users","products") and st[k]!=env["initial_state"][k]:
            raise DatasetBoundaryError("nonlink source state changed")
    for k,obj in env["initial_state"]["users"].items():
        if k!=uid or name!="missing_user":
            if st["users"][k]!=obj:raise DatasetBoundaryError("non-target user changed")
    for k,obj in env["initial_state"]["products"].items():
        if k!=pid or name!="missing_product":
            if st["products"][k]!=obj:raise DatasetBoundaryError("non-target product changed")
    return copy_env

def prepare(rows,root):
    _,fam,public,env,private=build(rows,[ROW])[0]
    prompt=" ".join(m["content"] for m in public["messages"]
                    if m["role"]=="user")
    if not re.search(r"\bCancel subscription SUB1234\b",prompt,re.IGNORECASE):
        raise DatasetBoundaryError("original public cancellation request changed")
    uid,pid=target_fields(env)
    expected_sha=hashlib.sha256(canonical(private)).hexdigest()
    class_sha=hashlib.sha256(env["class_code"].encode()).hexdigest()
    receipts={}
    for name in VARIANTS:
        v=make_variant(env,name)
        folder=root/name
        write_json(folder/"public.json",public)
        write_json(folder/"environment.json",v)
        write_json(folder/"verifier.json",private)
        receipts[name]={
            "state_sha256":hashlib.sha256(canonical(v["initial_state"])).hexdigest(),
            "source_class_sha256":class_sha,
            "original_private_checker_sha256":expected_sha,
            "one_link_key_removed":name!="valid",
            "deletion_type":"none" if name=="valid" else name,
            "controlled_not_natural_task":name!="valid",
            "actor_never_receives_fixture_label":True}
    return {
        "contract":"OWI-EC005I-KNOWN-ID-LINK-VARIANTS/1",
        "source_row":ROW,"source_family_sha256":fam,
        "train_variants":list(TRAIN),
        "heldout_mechanism_variant":MECHANISM_HOLDOUT,
        "original_task_public_sub_id":TARGET,
        "original_user_id_sha256":hashlib.sha256(uid.encode()).hexdigest(),
        "original_product_id_sha256":hashlib.sha256(pid.encode()).hexdigest(),
        "identical_original_public_request_and_tools":True,
        "source_class_private_checker_byte_identical":True,
        "synthetic_interventions_not_independent_tasks":True,
        "receipts":receipts}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output-dir",required=True,type=Path)
    p.add_argument("--lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    a=p.parse_args()
    lock=json.loads(a.lock.read_text())
    rows=audit_source(lock)
    manifest=prepare(rows,a.output_dir)
    manifest["source_lock_sha256"]=lock["sha256"]
    write_json(a.output_dir/"manifest.json",manifest)
    print("KNOWN_ID_LINK_VARIANT_CUSTODY",json.dumps(manifest,sort_keys=True))

if __name__=="__main__":
    main()
