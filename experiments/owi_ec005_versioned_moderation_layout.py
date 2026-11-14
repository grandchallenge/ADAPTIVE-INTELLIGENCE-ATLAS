#!/usr/bin/env python3
"""Trusted-only limited structural diagnostic, no private values exported.

Runs original class in the original OS jail with no action; inspects only
post-constructor *top-level* state container keys, value types, and lists'
first-element keys. This is benchmark-author instrumentation, NOT policy input.
No original checker/answer/class code or private state values leave the host.
"""
import argparse,json
from pathlib import Path
from owi_ec005_realtools_randomized import IMAGE,call_child
from owi_ec005_realtools_goal_policy import WORKER

def layout(item):
    result={}
    for key,val in item.items():
        e={"type":type(val).__name__}
        if isinstance(val,dict):
            e["mapping_keys"]=list(val)[:20]
            if val:
                first=next(iter(val.values()))
                if isinstance(first,dict):
                    e["first_value_keys"]=list(first)[:25]
                elif isinstance(first,list) and first and isinstance(first[0],dict):
                    e["first_value_list_item_keys"]=list(first[0])[:25]
        elif isinstance(val,list):
            e["length"]=len(val)
            if val and isinstance(val[0],dict):
                e["first_item_keys"]=list(val[0])[:25]
        result[key]=e
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",required=True,type=Path)
    a=p.parse_args()
    rows,_=call_child(IMAGE,WORKER,a.input_dir/"710"/"environment.json",
                      input_text='{"action":"finish"}\n')
    if (len(rows)!=2 or rows[0].get("kind")!="ready" or
        rows[0].get("verifier_present") is not False or
        rows[1].get("kind")!="private_final_state" or
        rows[1].get("tool_calls")!=0):
        raise ValueError("original trusted no-action source state unavailable")
    x=rows[1]
    if not isinstance(x.get("state"),dict):
        raise ValueError("invalid private state type")
    print("OWI_EC005O_TRUSTED_SCHEMA_ONLY",json.dumps({
        "original_training_row":710,
        "source_original_class_unchanged":True,
        "no_original_checklist_loaded":True,
        "private_payload_values_emitted":False,
        "original_state_shape":layout(x["state"]),
        "original_initial_state_shape":layout(x["initial_state"])
    },sort_keys=True))
if __name__=="__main__":
    main()
