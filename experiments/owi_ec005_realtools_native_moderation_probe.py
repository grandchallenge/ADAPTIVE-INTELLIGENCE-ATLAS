#!/usr/bin/env python3
"""Read-only native moderation-task discovery through actual selected tools.

The third-party class executes solely inside the source-locked no-network
Docker worker. No private checker, hidden state, or source code is exposed to
this read-only policy. Only tool-success/record-schema and bounded public
review status/rating summaries are logged; final private state is discarded.
"""
from __future__ import annotations
import argparse
import json
import subprocess
from pathlib import Path

from owi_ec005_realtools_goal_policy import (
    docker_worker_args, receive, unpack_reply, WORKER
)
from owi_ec005_realtools_randomized import IMAGE, fingerprint

SOURCE_ROW=2151

def records(parsed):
    data=parsed.get("data") if isinstance(parsed,dict) else None
    if isinstance(data,list):
        return [x for x in data if isinstance(x,dict)]
    if isinstance(data,dict):
        return [x for x in data.values() if isinstance(x,dict)]
    return []

def inspect(directory):
    public=json.loads((directory/"public.json").read_text())
    if set(public)!={"messages","tools"}:
        raise ValueError("public-only policy boundary")
    required={"list_all_products","get_reviews_for_product_by_status"}
    declared={x["name"]:x["parameters"] for x in public["tools"]}
    if not required.issubset(declared) or declared["list_all_products"].get("required") != []:
        raise ValueError("public tool scope changed")
    proc=subprocess.Popen(
        docker_worker_args(IMAGE,WORKER,directory/"environment.json"),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,
        text=True,bufsize=1)
    calls=[]
    def read(name,args):
        if name not in declared or set(args)!=set(declared[name].get("required",[])):
            raise ValueError("invalid public selected tool arguments")
        cmd={"action":"call","tool":name,"arguments":args}
        proc.stdin.write(json.dumps(cmd)+"\n")
        proc.stdin.flush()
        obs=receive(proc)
        if obs.get("kind")!="observation" or obs.get("tool")!=name:
            raise RuntimeError("selected public tool observation mismatch")
        calls.append({"name":name,"hash":fingerprint(obs.get("content","")),
                      "ok":obs.get("ok"),"truncated":obs.get("truncated",False)})
        if obs.get("truncated"):
            raise RuntimeError("truncated public tool observation")
        return unpack_reply(obs.get("content",""))
    try:
        start=receive(proc)
        if start.get("kind")!="ready" or start.get("verifier_present") is not False:
            raise RuntimeError("external worker privacy failure")
        products_result=read("list_all_products",{})
        products=records(products_result)
        observations=[]
        for p in products[:4]:
            pid=p.get("product_id")
            if not isinstance(pid,str):
                continue
            out=read("get_reviews_for_product_by_status",
                     {"product_id":pid,"moderation_status":"pending"})
            reviews=records(out)
            observations.append({
                "product_id_public_read":pid,
                "product_category_public_read":p.get("category"),
                "product_fields":sorted(p.keys()),
                "pending_review_count":len(reviews),
                "pending_review_samples":[{
                    "review_id_public_read":v.get("review_id"),
                    "review_field_names":sorted(v),
                    "user_id_public_read":v.get("user_id"),
                    "rating_public_read":v.get("rating"),
                    "status_public_read":v.get("moderation_status"),
                    "review_text_has_refill":(
                        "refill" in str(v.get("review_text","")).lower()),
                } for v in reviews[:4]],
            })
        author_statuses=[]
        author_ids=[]
        for product in observations:
            for candidate in product["pending_review_samples"]:
                uid=candidate.get("user_id_public_read")
                if isinstance(uid,str) and uid not in author_ids:
                    author_ids.append(uid)
        for uid in author_ids[:3]:
            result=read("get_user_by_id",{"user_id":uid})
            record=result.get("data")
            if not isinstance(record,dict):
                record={}
            author_statuses.append({
                "publicly_retrieved_user_id":uid,
                "user_id_matched":record.get("user_id")==uid or
                                  record.get("_id")==uid,
                "public_account_status":record.get("account_status"),
                "public_user_field_names":sorted(record),
            })
        proc.stdin.write('{"action":"finish"}\n')
        proc.stdin.flush()
        final=receive(proc)
        if final.get("kind")!="private_final_state":
            raise RuntimeError("worker private final-state IPC changed")
        proc.stdin.close()
        if proc.wait(timeout=10)!=0:
            raise RuntimeError("worker abnormal exit")
    finally:
        if proc.poll() is None:proc.kill()
        if proc.stdin and not proc.stdin.closed:proc.stdin.close()
        if proc.stdout:proc.stdout.close()
    return {
        "contract":"OWI-EC005J-MODERATION-PUBLIC-ONLY-PROBE/1",
        "source_row":SOURCE_ROW,
        "products_seen":len(products),
        "public_selected_tool_calls":len(calls),
        "public_records":observations,
        "public_author_statuses":author_statuses,
        "selected_tool_audit":calls,
        "private_final_state_discarded":True,
        "native_verifier_never_loaded":True,
        "source_code_not_executed_on_host":True,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",required=True,type=Path)
    a=p.parse_args()
    report=inspect(a.input_dir/str(SOURCE_ROW))
    print("NATIVE_MODERATION_SELECTED_PUBLIC_PROBE",
          json.dumps(report,sort_keys=True))

if __name__=="__main__":
    main()
