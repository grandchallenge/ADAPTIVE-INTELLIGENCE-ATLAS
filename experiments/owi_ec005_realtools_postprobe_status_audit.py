#!/usr/bin/env python3
"""Trusted, bounded row-2 state-path diagnosis for counterfactual-free testing.

May inspect source-locked PRIVATE initial state for constructing controlled
test environments. Does NOT execute third-party code, train, expose private
checkers, or emit full initial-state contents. Exact target must be uniquely
identified. This AUDIT is a distinct privileged experiment-setup role;
the learner MUST NOT call this module or receive its state details.
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_split import partition
from owi_ec005_realtools_intake import DatasetBoundaryError

def candidate_paths(tree, *, user="USR002", path=()):
    if isinstance(tree,dict):
        status=tree.get("account_status")
        if isinstance(status,str):
            identifiers=[str(tree.get(k,"")) for k in
                         ("user_id","id","_id","uid","account_id")]
            if user in identifiers or user in map(str,path):
                yield {"path":list(path)+["account_status"],
                       "status":status,
                       "record_keys":sorted(map(str,tree.keys())),
                       "identifiers_match":True}
            else:
                yield {"path":list(path)+["account_status"],
                       "status":status,
                       "record_keys":sorted(map(str,tree.keys())),
                       "identifiers_match":False}
        for key,val in tree.items():
            yield from candidate_paths(val,user=user,path=path+(key,))
    elif isinstance(tree,list):
        for i,val in enumerate(tree):
            yield from candidate_paths(val,user=user,path=path+(i,))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    args=ap.parse_args()
    rows=audit_source(json.loads(args.lock.read_text()))
    split=partition(rows,seed=4611)
    train={r["row_index"] for r in split["partitions"]["train"]}
    if 2 not in train:
        raise DatasetBoundaryError("row 2 no longer in training partition")
    state=rows[2]["extra_info"]["environment"]["initial_state"]
    candidates=list(candidate_paths(state))
    matched=[x for x in candidates if x["identifiers_match"]]
    print("ROW2_PRIVILEGED_STATUS_PATH_AUDIT",json.dumps({
        "source_locked":True,"row_index":2,"partition":"train",
        "top_level_state_keys":sorted(map(str,state.keys())),
        "status_record_count":len(candidates),
        "matched_records":matched[:3],
        "nonmatched_record_count":len(candidates)-len(matched),
        "verifier_source_exposed":False,
        "hidden_record_values_exported":False,
        "not_a_learner_input":True},sort_keys=True))

if __name__=="__main__":
    main()
