#!/usr/bin/env python3
"""EC005N: public-only live discovery, original independent TRAIN source row 710.

The untrusted source class runs ONLY in original restricted Docker child;
policy receives only actual selected public tool replies. No private checker
or state is used; final state is discarded. Diagnostic publication is bounded
to synthetic public status fields (not private author/answer/checker source).
"""
from __future__ import annotations
import argparse,json,subprocess,time
from pathlib import Path
from owi_ec005_realtools_goal_policy import (
    docker_worker_args,receive,unpack_reply,WORKER)
from owi_ec005_realtools_randomized import IMAGE,fingerprint

ROW=710
CONTRACT="OWI-EC005N-ORIGINAL-PUBLIC-PROFESSIONAL-DISCOVERY/1"
REQUIRED={
    "list_all_professionals":set(),
    "list_all_users":set(),
    "get_reviews_for_professional":{"professional_id"},
    "get_review_moderation_status":{"view_id"},
    "change_review_moderation_status":{"view_id","new_status"},
}
def preflight(public):
    if not isinstance(public,dict) or set(public)!={"messages","tools"}:
        raise ValueError("only original public user task and tool signatures permitted")
    task="\n".join(m.get("content","") for m in public["messages"]
                   if m.get("role")=="user")
    for v in ("Dr. Luke Marquez","Alice Chan","Dr. Ella Navarro",
              "Jules Morgan","banned","Dr. Sandy Torres"):
        if v not in task:
            raise ValueError("original public professional task drift")
    declared={x["name"]:x["parameters"] for x in public["tools"]}
    for name,required in REQUIRED.items():
        if name not in declared or set(declared[name].get("required",[]))!=required:
            raise ValueError("source public professional tool signature drift")
    return declared

def objects(data):
    if isinstance(data,list):
        return [x for x in data if isinstance(x,dict)]
    if isinstance(data,dict):
        if "data" in data:
            return objects(data["data"])
        for key in ("professionals","users","reviews","results","items"):
            if key in data:
                return objects(data[key])
        if all(isinstance(v,dict) for v in data.values()):
            return list(data.values())
        return [data]
    return []

def public_projection(record, fields):
    return {k:record[k] for k in fields if k in record and
            isinstance(record[k],(int,float,str,bool,type(None)))}

def run(input_dir):
    folder=input_dir/str(ROW)
    public=json.loads((folder/"public.json").read_text())
    declared=preflight(public)
    proc=subprocess.Popen(docker_worker_args(
        IMAGE,WORKER,folder/"environment.json"),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,text=True,bufsize=1)
    chosen=[]
    def call(name,args):
        if name not in declared or set(args)!=set(declared[name].get("required",[])):
            raise ValueError("not a declared selected public tool call")
        proc.stdin.write(json.dumps({"action":"call","tool":name,
                                      "arguments":args})+"\n")
        proc.stdin.flush()
        m=receive(proc)
        if m.get("kind")!="observation" or m.get("tool")!=name or m.get("truncated"):
            raise RuntimeError("source public observation protocol drift")
        chosen.append({"tool":name,"sha256":fingerprint(m.get("content","")),
                       "ok":m.get("ok"),"elapsed":m.get("elapsed_seconds")})
        if m.get("ok") is not True:
            return {"public_tool_failure":True,"response_hash":chosen[-1]["sha256"]}
        return unpack_reply(m.get("content",""))
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("private source checker leaked to worker")
        pros_raw=call("list_all_professionals",{})
        users_raw=call("list_all_users",{})
        pros=objects(pros_raw)
        users=objects(users_raw)
        matches=[]
        for p in pros[:40]:
            pid=p.get("professional_id",p.get("_id"))
            name=str(p.get("name",p.get("full_name","")))
            if not isinstance(pid,str) or not any(n in name for n in (
                "Marquez","Navarro","Torres")):
                continue
            rv=call("get_reviews_for_professional",{"professional_id":pid})
            matches.append({
                "professional":public_projection(p,(
                    "professional_id","_id","name","full_name","specialty","specialization","department")),
                "public_replies_type":type(rv).__name__,
                "public_replies_keys":sorted(rv) if isinstance(rv,dict) else [],
                "public_reviews":[public_projection(x,(
                    "view_id","review_id","_id","user_id","professional_id",
                    "rating","moderation_status","status","review_text")) for x in objects(rv)[:12]],
            })
        proc.stdin.write('{"action":"finish"}\n');proc.stdin.flush()
        term=receive(proc)
        if term.get("kind")!="private_final_state":
            raise RuntimeError("source terminal bridge changed")
        proc.stdin.close()
        if proc.wait(timeout=10)!=0:
            raise RuntimeError("source process abnormal exit")
    finally:
        if proc.poll() is None:proc.kill()
        if proc.stdin and not proc.stdin.closed:proc.stdin.close()
        if proc.stdout:proc.stdout.close()
    return {
        "contract":CONTRACT,"original_train_row":ROW,
        "original_source_process_restricted":True,
        "private_checker_never_loaded":True,
        "private_final_state_discarded":True,
        "public_professionals_count":len(pros),
        "public_users_count":len(users),
        "public_user_samples":[public_projection(u,(
            "_id","user_id","username","name","full_name","account_status"))
            for u in users[:15]],
        "public_professionals_and_reviews":matches,
        "selected_public_calls":len(chosen),
        "selected_public_call_hashes":chosen,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",type=Path,required=True)
    p.add_argument("--output",type=Path,default=Path(
        "build/owi_ec005_realtools/native_professional_public.json"))
    a=p.parse_args()
    r=run(a.input_dir)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(r,sort_keys=True,indent=2)+"\n")
    print("OWI_EC005N_ORIGINAL_PUBLIC_SELECTED_PROBE",json.dumps(r,sort_keys=True))

if __name__=="__main__":
    main()
