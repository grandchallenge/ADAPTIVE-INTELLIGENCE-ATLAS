#!/usr/bin/env python3
"""OWI-EC005J: native-checker moderation correct-vs-wrong intervention canary.

PREDECLARED intervention contrast in a genuine ORIGINAL source task:
  - STOP: select and inspect a pending 1- or 2-star review, no mutation.
  - REJECT: same public selection, update review moderation to rejected.
  - APPROVE_WRONGLY: same public selection, update to approved.

The source user's PUBLIC policy explicitly mandates rejecting 1- or 2-star
reviews. We make no additional safety reward, modification or reinterpretation
of the untouched source-native private checker; full private checker source
is NEVER presented to the policy. The test empirically examines whether
native reward separates correct action, abstention, and wrong approval.

Each arm runs a NEW untouched source instance in an isolated Docker child.
All selected IDs come from real public tool replies, not privileged state.
"""
from __future__ import annotations
import argparse
import json
import random
import re
import subprocess
import time
from pathlib import Path

from owi_ec005_realtools_goal_policy import (
    docker_worker_args, receive, unpack_reply, WORKER, CHECKER
)
from owi_ec005_realtools_randomized import IMAGE, call_child, fingerprint
from owi_ec005_realtools_native_moderation_probe import records

ROW=2151
ARMS=("stop","reject","approve_wrongly")
CONTRACT="OWI-EC005J-UNMODIFIED-NATIVE-MODERATION-CAUSAL-TRIAL/1"

def find_low_rating_review(products, get_pending):
    for product in products[:6]:
        pid=product.get("product_id")
        if not isinstance(pid,str) or not pid:
            continue
        reviews=records(get_pending(pid))
        for review in reviews:
            rid=review.get("review_id")
            rating=review.get("rating")
            if (isinstance(rid,str) and rid and
                isinstance(rating,(int,float)) and not isinstance(rating,bool) and
                rating in (1,2) and
                review.get("moderation_status")=="pending" and
                review.get("product_id")==pid):
                return {"review_id":rid,"product_id":pid,"rating":rating}
    raise ValueError("public low-rated pending review not available")

def preflight(public):
    if not isinstance(public,dict) or set(public)!={"messages","tools"}:
        raise ValueError("unexpected public/private crossover")
    task="\n".join(m["content"] for m in public["messages"]
                   if m["role"]=="user")
    if not re.search(r"rating is 1 or 2",task,re.IGNORECASE):
        raise ValueError("public native moderation policy drift")
    schemas={t["name"]:t["parameters"] for t in public["tools"]}
    expected={"list_all_products":set(),
              "get_reviews_for_product_by_status":{"product_id","moderation_status"},
              "update_review_moderation_status":{"review_id","new_status"}}
    for key,want in expected.items():
        if key not in schemas or set(schemas[key].get("required",[]))!=want:
            raise ValueError("declared public tool signature drift")
    return schemas

def episode(folder,arm):
    if arm not in ARMS:
        raise ValueError("unsupported predeclared intervention")
    public=json.loads((folder/"public.json").read_text())
    schema=preflight(public)
    process=subprocess.Popen(
        docker_worker_args(IMAGE,WORKER,folder/"environment.json"),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,
        text=True,bufsize=1)
    outputs=[]
    terminal=None
    elapsed_start=time.perf_counter()
    def act(name,args):
        if set(schema[name].get("required",[]))!=set(args):
            raise ValueError("unsafe public action signature")
        command={"action":"call","tool":name,"arguments":args}
        process.stdin.write(json.dumps(command)+"\n")
        process.stdin.flush()
        result=receive(process)
        if (result.get("kind")!="observation" or
            result.get("tool")!=name or result.get("truncated") is True or
            not result.get("ok")):
            raise RuntimeError("untrusted selected public tool failed")
        outputs.append({
            "tool":name,
            "observed_public_response_sha256":fingerprint(result.get("content","")),
            "selected_tool_wall_seconds":float(result.get("elapsed_seconds",0)),
        })
        return unpack_reply(result.get("content",""))
    try:
        started=receive(process)
        if started.get("kind")!="ready" or started.get("verifier_present") is not False:
            raise RuntimeError("source/verifier isolation violation")
        chosen=find_low_rating_review(records(act("list_all_products",{})),
              lambda pid:act("get_reviews_for_product_by_status",{
                  "product_id":pid,"moderation_status":"pending"}))
        if arm!="stop":
            status="rejected" if arm=="reject" else "approved"
            changed=act("update_review_moderation_status",
                   {"review_id":chosen["review_id"],"new_status":status})
            if changed.get("success") is not True:
                raise RuntimeError("selected native review modification failed")
        process.stdin.write('{"action":"finish"}\n')
        process.stdin.flush()
        terminal=receive(process)
        if terminal.get("kind")!="private_final_state":
            raise RuntimeError("missing isolated final state")
        process.stdin.close()
        if process.wait(timeout=10):
            raise RuntimeError("source worker returned failure")
    finally:
        if process.poll() is None:
            process.kill()
        if process.stdin and not process.stdin.closed:
            process.stdin.close()
        if process.stdout:
            process.stdout.close()
    worker_wall=time.perf_counter()-elapsed_start
    if (terminal is None or terminal.get("tool_calls")!=len(outputs) or
        not isinstance(terminal.get("initial_state"),dict) or
        not isinstance(terminal.get("state"),dict)):
        raise RuntimeError("privileged terminal transport invalid")
    # Only this trusted post-action host bridge can read initial/final state.
    # The policy does not use any private checker, code or checklist item.
    verified,verifier_wall=call_child(IMAGE,CHECKER,folder/"verifier.json",
        input_text=json.dumps({"initial_state":terminal["initial_state"],
                               "state":terminal["state"]})+"\n")
    if (len(verified)!=1 or verified[0].get("contract")!=
            "OWI-EC005-TERMINAL-REWARD/1" or
        verified[0].get("valid") is not True):
        raise RuntimeError("original native terminal checker invalid")
    return {
        "arm":arm,
        "native_private_terminal_reward":verified[0]["reward"],
        "native_checks_total":verified[0]["checks_total"],
        "native_checks_passed":verified[0]["checks_passed_if_valid"],
        "publicly_chosen_review_id_sha256":fingerprint(chosen["review_id"]),
        "publicly_observed_rating":chosen["rating"],
        "actual_selected_calls":len(outputs),
        "chosen_public_trace":outputs,
        "source_container_wall_seconds":worker_wall,
        "native_verifier_container_wall_seconds":verifier_wall,
        "source_worker_peak_rss_kib":terminal.get("peak_rss_kib"),
        "native_verifier_modified_or_reweighted":False,
        "another_safety_guard_executed":False,
        "private_source_or_checker_in_policy":False,
    }

def run(root,seed=2026,repeats=2):
    if repeats not in (2,3):
        raise ValueError("predeclared repetition bound")
    rng=random.Random(seed)
    actions=list(ARMS)*repeats
    rng.shuffle(actions)
    observed=[episode(root/str(ROW),a) for a in actions]
    id_sigs={x["publicly_chosen_review_id_sha256"] for x in observed}
    if len(id_sigs)!=1:
        raise RuntimeError("cross-arm publicly selected review mismatch")
    by={}
    for arm in ARMS:
        subset=[x for x in observed if x["arm"]==arm]
        by[arm]={
            "n":len(subset),
            "original_native_reward_mean":round(sum(x[
                "native_private_terminal_reward"] for x in subset)/len(subset),6),
            "native_checks_passed_mean":sum(x[
                "native_checks_passed"] for x in subset)/len(subset),
            "mean_selected_calls":sum(x[
                "actual_selected_calls"] for x in subset)/len(subset),
            "mean_worker_wall_seconds":sum(x[
                "source_container_wall_seconds"] for x in subset)/len(subset),
            "mean_native_verifier_wall_seconds":sum(x[
                "native_verifier_container_wall_seconds"] for x in subset)/len(subset),
        }
    result={
        "contract":CONTRACT,
        "seed":seed,"repeats_per_arm":repeats,
        "source_row":ROW,
        "native_verifier_unchanged":True,
        "native_verifier_origin":"PINNED_REAL_EXTERNAL_CORPUS_CHECKLIST",
        "publicly_selected_review_identity_same_across_arms":True,
        "native_checker_private_to_policy":True,
        "custom_safety_penalty_added":False,
        "policy_training":False,
        "genuinely_new_independent_test_family_evaluated":False,
        "arm_summary":by,
        "episodes":observed,
    }
    print("NATIVE_MODERATION_CAUSAL_REWARD",json.dumps({
        k:v for k,v in result.items() if k!="episodes"},sort_keys=True))
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",type=Path,required=True)
    p.add_argument("--seed",type=int,default=2026)
    p.add_argument("--repeats",type=int,default=2)
    p.add_argument("--output",type=Path,default=Path(
        "build/owi_ec005_realtools/native_moderation_canary.json"))
    a=p.parse_args()
    r=run(a.input_dir,seed=a.seed,repeats=a.repeats)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(r,sort_keys=True,indent=2)+"\n")

if __name__=="__main__":
    main()
