#!/usr/bin/env python3
"""OWI-EC005J: predeclared native-reward candidate interface and custody audit.

Privileged AUDITOR sees full source-locked dataset only for partition verification,
source *schema* and intact native checklist count. The returned records contain
PUBLIC task/prompts/declarations, identifiers only as already stated by the
PUBLIC user, and counts; no hidden state, private check source or RSD guidance.
This is an experiment DESIGN audit, not learned oracle supervision.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_family_prepare import build
from owi_ec005_realtools_intake import DatasetBoundaryError, canonical

CANDIDATES = (
    (2151,"conditional-review-moderation"),
    (2301,"allergenic-meal-cross-contact"),
    (2449,"medical-allergy-authorization"),
    (687,"claim-approval-authorization"),
    (710,"professional-review-moderation"),
)
SCOPE_MAX=5

def public_candidates(rows,indices=tuple(i for i,_ in CANDIDATES)):
    if (not indices or len(indices)>SCOPE_MAX or
        len(set(indices))!=len(indices) or
        any(i not in [j for j,_ in CANDIDATES] for i in indices)):
        raise DatasetBoundaryError("native candidate scope not predeclared")
    # build ensures all distinct TRAIN source-code/environment families.
    packages=build(rows,list(indices))
    manifest=[]
    for index,family,public,environment,private in packages:
        if set(public)!={"messages","tools"}:
            raise DatasetBoundaryError("public interface did not seal")
        task="\n".join(m["content"] for m in public["messages"]
                       if m["role"]=="user")
        if not task or len(task)>16000:
            raise DatasetBoundaryError("public prompt drift")
        ops=[]
        for entry in public["tools"]:
            name=entry["name"]
            par=entry["parameters"]
            if (not isinstance(name,str) or not isinstance(par,dict) or
                not isinstance(par.get("required",[]),list)):
                raise DatasetBoundaryError("tool metadata contract drift")
            ops.append({"name":name,
                        "required":par.get("required",[]),
                        "parameter_property_names":sorted(par.get("properties",{}))})
        state=environment["initial_state"]
        if not isinstance(state,dict):
            raise DatasetBoundaryError("initial state missing")
        manifest.append({
            "contract":"OWI-EC005J-PUBLIC-NATIVE-REWARD-CANDIDATE/1",
            "row":index,
            "research_label":dict(CANDIDATES)[index],
            "training_family_sha256":family,
            "public_task_sha256":hashlib.sha256(canonical(public)).hexdigest(),
            "public_task":task,
            "declared_public_tools":ops,
            "original_private_checker_count":len(private["verifier"]["checklist"]),
            "original_checker_unchanged":True,
            "original_checker_source_exported":False,
            "private_initial_state_only_schema_keys":sorted(state),
            "source_class_code_sha256":hashlib.sha256(
                environment["class_code"].encode()).hexdigest(),
            "class_source_and_private_initial_state_exported":False,
            "native_reward_augmented_or_reweighted":False,
            "physical_execution_performed":False})
    return manifest

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    a=p.parse_args()
    lock=json.loads(a.lock.read_text())
    rows=audit_source(lock)
    report=public_candidates(rows)
    for entry in report:
        print("SOURCE_PINNED_NATIVE_REWARD_PUBLIC_CANDIDATE",
              json.dumps(entry,sort_keys=True,ensure_ascii=False))
    print("NATIVE_CANDIDATE_BOUNDARY",json.dumps({
        "source_verified_sha256":lock["sha256"],
        "predeclared_train_groups":len(report),
        "indices":[x["row"] for x in report],
        "native_reward_not_modified":True,
        "no_private_checker_or_initial_state_content_released":True,
        "heldout_dev_test_task_information_exported":False,
        "no_training_or_mutation_claimed":True,
    },sort_keys=True))

if __name__=="__main__":
    main()
