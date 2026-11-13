#!/usr/bin/env python3
"""OWI-EC005J: second original native-checker intervention contrast.

Choose a DIFFERENT existing pending review from only genuine selected public
replies: 4- or 5-star review, ACTIVE author, not Home/refill exception.
Public rule requires APPROVE. Compare stop, approve and prohibited reject
in fresh no-network external source environments, unchanged original checker.
No native-reward augmentation or custom guard.
"""
from __future__ import annotations
import argparse,json,random,subprocess,time
from pathlib import Path
from owi_ec005_realtools_native_moderation_probe import records
from owi_ec005_realtools_native_moderation_canary import preflight
from owi_ec005_realtools_goal_policy import (
    docker_worker_args,receive,unpack_reply,WORKER,CHECKER)
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint

ROW=2151
ARMS=("stop","approve","reject_wrongly")
CONTRACT="OWI-EC005J-UNMODIFIED-NATIVE-HIGH-RATING-MODERATION/1"

def eligible_high(products,fetch_pending,fetch_user):
    for product in products[:6]:
        pid=product.get("product_id")
        cat=product.get("category")
        if not isinstance(pid,str):
            continue
        for review in records(fetch_pending(pid)):
            uid=review.get("user_id")
            rid=review.get("review_id")
            score=review.get("rating")
            refill="refill" in str(review.get("review_text","")).lower()
            if (not isinstance(score,(float,int)) or
                isinstance(score,bool) or score not in (4,5) or
                not isinstance(uid,str) or not isinstance(rid,str) or
                review.get("moderation_status")!="pending" or
                review.get("product_id")!=pid or
                (cat=="Home" and refill)):
                continue
            user=fetch_user(uid)
            info=user.get("data") if isinstance(user,dict) else None
            if isinstance(info,dict) and info.get("user_id")==uid and (
                info.get("account_status")=="active"):
                return {"review_id":rid,"user_id":uid,"rating":score,
                        "product_id":pid,"category":cat}
    raise ValueError("no authorized high-rated review found through public tools")

def episode(folder,arm):
    if arm not in ARMS:raise ValueError("invalid arm")
    public=json.loads((folder/"public.json").read_text())
    declared=preflight(public)
    if set(declared.get("get_user_by_id",{}).get("required",[]))!={"user_id"}:
        raise ValueError("public user auth tool signature drift")
    start=time.perf_counter()
    proc=subprocess.Popen(docker_worker_args(IMAGE,WORKER,folder/"environment.json"),
              stdin=subprocess.PIPE,stdout=subprocess.PIPE,
              stderr=subprocess.DEVNULL,text=True,bufsize=1)
    calls=[]
    final=None
    def call(name,args):
        if set(declared[name].get("required",[]))!=set(args):
            raise ValueError("public action signature mismatch")
        proc.stdin.write(json.dumps({"action":"call","tool":name,
                                     "arguments":args})+"\n")
        proc.stdin.flush()
        obs=receive(proc)
        if (obs.get("kind")!="observation" or obs.get("tool")!=name or
            not obs.get("ok") or obs.get("truncated")):
            raise RuntimeError("failed selected public tool observation")
        calls.append({"name":name,"public_result_sha256":fingerprint(
                          obs.get("content","")),"tool_seconds":float(
                          obs.get("elapsed_seconds",0))})
        return unpack_reply(obs.get("content",""))
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("private checker leaked to source worker")
        products=records(call("list_all_products",{}))
        target=eligible_high(products,
             lambda pid:call("get_reviews_for_product_by_status",{
                 "product_id":pid,"moderation_status":"pending"}),
             lambda uid:call("get_user_by_id",{"user_id":uid}))
        if arm!="stop":
            dest="approved" if arm=="approve" else "rejected"
            result=call("update_review_moderation_status",{
                "review_id":target["review_id"],"new_status":dest})
            if result.get("success") is not True:
                raise RuntimeError("source mutation unsuccessful")
        proc.stdin.write('{"action":"finish"}\n');proc.stdin.flush()
        final=receive(proc)
        if final.get("kind")!="private_final_state":
            raise RuntimeError("private terminal state missing")
        proc.stdin.close()
        if proc.wait(timeout=10):raise RuntimeError("worker failed")
    finally:
        if proc.poll() is None:proc.kill()
        if proc.stdin and not proc.stdin.closed:proc.stdin.close()
        if proc.stdout:proc.stdout.close()
    elapsed=time.perf_counter()-start
    if final.get("tool_calls")!=len(calls):
        raise RuntimeError("selected source tool count mismatch")
    checked,checker_sec=call_child(IMAGE,CHECKER,folder/"verifier.json",
            input_text=json.dumps({"initial_state":final["initial_state"],
                                   "state":final["state"]})+"\n")
    if (len(checked)!=1 or checked[0].get("contract")!=
        "OWI-EC005-TERMINAL-REWARD/1" or checked[0].get("valid") is not True):
        raise RuntimeError("original checker unusable")
    return {
        "arm":arm,
        "original_native_reward":checked[0]["reward"],
        "original_native_checks_passed":checked[0]["checks_passed_if_valid"],
        "original_native_checks_total":checked[0]["checks_total"],
        "publicly_chosen_review_sha256":fingerprint(target["review_id"]),
        "publicly_observed_review_rating":target["rating"],
        "publicly_observed_active_author":True,
        "actual_selected_calls":len(calls),
        "selected_tool_receipts":calls,
        "worker_wall_seconds":elapsed,
        "private_checker_wall_seconds":checker_sec,
        "external_worker_peak_rss_kib":final.get("peak_rss_kib"),
        "private_state_or_check_in_policy":False,
        "additional_safety_guard_or_reward_shaping":False,
    }

def run(directory,seed=2026,repeats=2):
    if repeats not in (2,3):raise ValueError("invalid repeat scope")
    rng=random.Random(seed+320)
    sequence=list(ARMS)*repeats
    rng.shuffle(sequence)
    result=[episode(directory/str(ROW),a) for a in sequence]
    if len({x["publicly_chosen_review_sha256"] for x in result})!=1:
        raise RuntimeError("review target inconsistent between arms")
    score={}
    for a in ARMS:
        sub=[x for x in result if x["arm"]==a]
        score[a]={
            "episodes":len(sub),
            "mean_native_original_reward":round(sum(x["original_native_reward"]
                                                for x in sub)/len(sub),6),
            "mean_native_original_checks_passed":sum(x[
                "original_native_checks_passed"] for x in sub)/len(sub),
            "mean_actual_selected_calls":sum(x["actual_selected_calls"]
                                                for x in sub)/len(sub),
        }
    return {"contract":CONTRACT,
            "seed":seed,"source_row":ROW,
            "original_native_verifier_untouched":True,
            "separate_safety_guard":False,
            "same_genuine_public_review_across_arms":True,
            "chosen_policy_training":False,
            "arm_summary":score,"selected_episodes":result}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",type=Path,required=True)
    p.add_argument("--output",type=Path,default=Path(
        "build/owi_ec005_realtools/native_high_review_canary.json"))
    a=p.parse_args()
    result=run(a.input_dir)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("NATIVE_HIGH_RATING_CORRECT_VS_WRONG_REWARD",json.dumps({
        k:v for k,v in result.items() if k!="selected_episodes"},sort_keys=True))

if __name__=="__main__":
    main()
