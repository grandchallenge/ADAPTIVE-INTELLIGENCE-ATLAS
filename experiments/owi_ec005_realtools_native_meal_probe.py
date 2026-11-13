#!/usr/bin/env python3
"""Read only source-locked original allergen-safety task's public tool state.

The external source class runs only in an isolated nonroot no-network Docker
child. No native checker runs, no private final state is exported, and no
private task state/initial values are read by this public policy. This audit
exists to design a PREDECLARED truthful-vs-false allergen label contrast
without inventing value types or changing the native evaluation objective.
"""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
from owi_ec005_realtools_goal_policy import unpack_reply,WORKER
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint

ROW=2301
TARGET="MEAL102"

def public_meal_snapshot(public,reply):
    if not isinstance(public,dict) or set(public)!={"messages","tools"}:
        raise ValueError("public task boundary")
    prompt="\n".join(x["content"] for x in public["messages"]
                     if x["role"]=="user")
    if "cashews (cross-contact)" not in prompt or TARGET not in prompt:
        raise ValueError("public allergen-safety task drift")
    tools={t["name"]:t["parameters"] for t in public["tools"]}
    if (set(tools.get("get_meal_by_id",{}).get("required",[]))!={"meal_id"} or
        set(tools.get("update_meal_allergen_info",{}).get("required",[]))!=
             {"meal_id","new_allergen_info"}):
        raise ValueError("public allergen tool schema drift")
    if not isinstance(reply,dict) or reply.get("success") is not True:
        raise ValueError("failed selected meal observation")
    data=reply.get("data")
    if (not isinstance(data,dict) or data.get("meal_id")!=TARGET):
        raise ValueError("wrong public meal result")
    return {
        "public_meal_id":data["meal_id"],
        "public_meal_fields":sorted(data),
        "public_dietary_properties":data.get("dietary_properties"),
        "public_dietary_properties_type":type(
             data.get("dietary_properties")).__name__,
        "public_allergen_info":data.get("allergen_info"),
        "public_allergen_info_type":type(data.get("allergen_info")).__name__,
        "public_allergen_update_argument_schema":
              tools["update_meal_allergen_info"],
    }

def inspect(directory):
    folder=directory/str(ROW)
    public=json.loads((folder/"public.json").read_text())
    commands=[{"action":"call","tool":"get_meal_by_id",
               "arguments":{"meal_id":TARGET}},{"action":"finish"}]
    rows,wall=call_child(IMAGE,WORKER,folder/"environment.json",
            input_text="".join(json.dumps(x)+"\n" for x in commands))
    if (len(rows)!=3 or rows[0].get("kind")!="ready" or
        rows[0].get("verifier_present") is not False or
        rows[1].get("kind")!="observation" or
        rows[1].get("tool")!="get_meal_by_id" or
        rows[1].get("truncated") or
        rows[2].get("kind")!="private_final_state"):
        raise RuntimeError("isolated public source IPC drift")
    payload=public_meal_snapshot(public,unpack_reply(rows[1]["content"]))
    payload.update({
        "contract":"OWI-EC005J-PUBLIC-SAFETY-MEAL-SNAPSHOT/1",
        "original_source_task_row":ROW,
        "actual_selected_read_calls":1,
        "selected_response_sha256":fingerprint(rows[1]["content"]),
        "worker_container_seconds":wall,
        "private_checker_never_loaded":True,
        "private_final_state_discarded":True,
        "no_source_class_execution_on_host":True,
    })
    return payload

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",required=True,type=Path)
    a=p.parse_args()
    print("UNMODIFIED_NATIVE_MEAL_PUBLIC_SNAPSHOT",
          json.dumps(inspect(a.input_dir),sort_keys=True,ensure_ascii=False))

if __name__=="__main__":
    main()
