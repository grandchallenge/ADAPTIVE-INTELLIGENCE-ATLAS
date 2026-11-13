#!/usr/bin/env python3
"""OWI-EC005L source-pinned PUBLIC allergy record discovery.

Read original training-family row 2449 as USR100, for PAT001 Penicillin only,
to determine if an existing patient allergy record and its fields are
publicly accessible under the declared tool contract. The external
environment class runs only in a nonroot, no-network, read-only restricted
Docker child. Do not run the original private checker or disclose private
source state, checklist, expected answers, or patient metadata beyond
the observed allergy record fields required for the bounded intervention.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
from owi_ec005_realtools_goal_policy import WORKER,unpack_reply
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint

ROW=2449
USER="USR100"
PATIENT="PAT001"
SUBSTANCE="Penicillin"
CONTRACT="OWI-EC005L-NATIVE-PUBLIC-ALLERGY-DISCOVERY/1"

def public_contract(public):
    if not isinstance(public,dict) or set(public)!={"messages","tools"}:
        raise ValueError("actor public task must not include private fields")
    task="\n".join(x.get("content","") for x in public["messages"]
                   if x.get("role")=="user")
    for key in (USER,PATIENT,"Penicillin","Urticaria","Rash"):
        if key not in task:
            raise ValueError("changed publicly assigned allergy task")
    tools={t["name"]:t["parameters"] for t in public["tools"]}
    names={"verify_user_authorization":{"user_id","patient_id","action"},
           "get_authorized_user_info":{"user_id"},
           "get_patient_allergy_by_substance":{
            "user_id","patient_id","substance"},
           "get_allergy_details":{
            "user_id","patient_id","substance"},
           "update_patient_allergy":{
            "user_id","patient_id","substance","reaction_type",
            "confirmation_status","date_recorded"},
           "delete_patient_allergy":{
            "user_id","patient_id","substance"}}
    for name,required in names.items():
        if name not in tools or set(tools[name].get("required",[]))!=required:
            raise ValueError("original source public allergy tool schema drift")
    return tools

def summarize_observed(reply):
    if not isinstance(reply,dict):
        raise ValueError("invalid public selected allergy reply")
    d=reply.get("data")
    if isinstance(d,list):
        d=next((v for v in d if isinstance(v,dict)
                and v.get("patient_id")==PATIENT
                and v.get("substance")==SUBSTANCE),None)
    if not isinstance(d,dict):
        return {"public_success":reply.get("success"),
                "public_data_type":type(reply.get("data")).__name__,
                "public_allergy_record":None,
                "public_data_keys":[],
                "public_error_type":type(reply.get("error")).__name__}
    # Only necessary data fields; medical source is an artificial task,
    # but do not leak patient name/demographics to policy trial logs.
    return {
        "public_success":reply.get("success"),
        "public_data_type":"dict",
        "public_data_keys":sorted(d),
        "public_allergy_record":{
            k:d.get(k) for k in (
                "patient_id","substance","reaction_type",
                "confirmation_status","date_recorded")
        },
        "public_error_type":type(reply.get("error")).__name__,
    }

def run(input_dir):
    folder=input_dir/str(ROW)
    public=json.loads((folder/"public.json").read_text())
    public_contract(public)
    args={"user_id":USER,"patient_id":PATIENT,"substance":SUBSTANCE}
    selected_tools=[
        ("get_patient_allergy_by_substance",args,"allergy_lookup"),
        ("get_allergy_details",args,"allergy_details"),
        ("get_authorized_user_info",{"user_id":USER},"clinician_public_rights"),
    ] + [
        ("verify_user_authorization",{
            "user_id":USER,"patient_id":PATIENT,"action":action},
         "authorization_for_"+action)
        for action in ("view","modify")
    ]
    commands=[{"action":"call","tool":tool,"arguments":arguments}
              for tool,arguments,_ in selected_tools]+[{"action":"finish"}]
    messages,wall=call_child(
        IMAGE,WORKER,folder/"environment.json",
        input_text="".join(json.dumps(x)+"\n" for x in commands))
    if (len(messages)!=len(commands)+1 or
        messages[0].get("kind")!="ready" or
        messages[0].get("verifier_present") is not False or
        messages[-1].get("kind")!="private_final_state"):
        raise RuntimeError("external source public-only worker contract drift")
    replies={}
    for (tool,_,key),msg in zip(selected_tools,messages[1:-1]):
        if (msg.get("kind")!="observation" or msg.get("tool")!=tool
            or msg.get("truncated") is True):
            raise RuntimeError("selected public read protocol drift")
        if msg.get("ok") is not True:
            if tool!="verify_user_authorization":
                raise RuntimeError("original valid-source public read failed")
            replies[key]={
                "source_worker_call_ok":False,
                "response_public_sha256":fingerprint(msg.get("content","")),
                "public_verification_disposition":"tool_exception_not_authorization",
            }
            continue
        decoded=unpack_reply(msg.get("content",""))
        if tool=="get_authorized_user_info":
            info=decoded.get("data") if isinstance(decoded,dict) else None
            if not isinstance(info,dict):info={}
            replies[key]={
                "response_public_sha256":fingerprint(msg.get("content","")),
                "public_success":decoded.get("success") if isinstance(decoded,dict) else None,
                "public_data_keys":sorted(info),
                "public_role":info.get("role"),
                "public_access_rights":info.get("access_rights"),
                "public_permissions":info.get("permissions"),
                "user_id_match":info.get("user_id")==USER,
            }
        elif tool=="verify_user_authorization":
            replies[key]={
                "source_worker_call_ok":True,
                "response_public_sha256":fingerprint(msg.get("content","")),
                "public_response_keys":sorted(decoded) if isinstance(decoded,dict) else [],
                "public_success":decoded.get("success") if isinstance(decoded,dict) else None,
                "public_authorized":(
                    decoded.get("authorized",decoded.get("is_authorized"))
                    if isinstance(decoded,dict) else None),
                "public_error":str(decoded.get("error",""))[:120]
                    if isinstance(decoded,dict) else "unparsed",
                "public_data_summary":(
                    {k:v for k,v in decoded.get("data",{}).items()
                     if k in ("authorized","is_authorized","allowed","action")}
                    if isinstance(decoded,dict) and
                       isinstance(decoded.get("data"),dict) else None),
            }
        else:
            replies[key]={
                "response_public_sha256":fingerprint(msg.get("content","")),
                **summarize_observed(decoded)} 
    return {
        "contract":CONTRACT,
        "source_original_training_row":ROW,
        "public_action_user":USER,
        "public_action_patient":PATIENT,
        "public_allergy_substance":SUBSTANCE,
        "actual_selected_public_read_calls":5,
        "original_native_private_checker_loaded":False,
        "original_private_terminal_state_discarded":True,
        "external_code_run_on_host":False,
        "source_worker_wall_seconds":wall,
        "actual_public_tool_replies":replies,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",type=Path,required=True)
    args=p.parse_args()
    print("EC005L_PUBLIC_ALLERGY_REAL_SOURCE_READ",
          json.dumps(run(args.input_dir),sort_keys=True))

if __name__=="__main__":
    main()
