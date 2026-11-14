#!/usr/bin/env python3
"""EC005O: evaluate source-native and separately corrected terminal checker paired.

Original TRAIN row 710 only, original state/class/checker untouched.
Corrected checker is a distinct source-private terminal evaluator, NEVER actor input.
Targets are selected from genuine public list/read tool replies, not source code
or private checker. Two target rules x five arms x two resets = 20 real
isolated episodes. Each restricted source worker has a distinct after-terminal
restricted private checker child. No controller is trained by this audit.

Strong contrast: unchanged initial STOP versus an ACTUALLY changed wrong final
state. Weaker contrast: preserve a correct state versus undo it. Neither is a
certificate of general safety or adaptive on-policy introspection.
"""
from __future__ import annotations
import argparse,hashlib,json,random,subprocess,time
from pathlib import Path
from owi_ec005_realtools_goal_policy import (
    docker_worker_args,receive,unpack_reply,WORKER,CHECKER)
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint
from owi_ec005_realtools_native_professional_probe import (
    ROW,preflight,objects)

TARGETS={
    "banned_reject":{
        "name":"Dr. Ella Navarro","specialty":"Internal Medicine",
        "user":"Jules Morgan","author_status":"banned",
        "correct":"rejected","wrong":"approved",
    },
    "eligible_approve":{
        "name":"Dr. Luke Marquez","specialty":"Dermatology",
        "user":"Alice Chan","author_status":"active",
        "correct":"approved","wrong":"rejected",
    },
}
ARMS=("untouched","direct_wrong","preserve_correct",
      "reapply_correct","regress_wrong")
CONTRACT="OWI-EC005O-PAIRED-ORIGINAL-AND-CORRECTED-TERMINAL/1"
CHECKER_CONTRACT="OWI-EC005-TERMINAL-REWARD/1"
REVISED_CHECKER="experiments/owi_ec005_versioned_moderation_checker.py"
REVISED_CONTRACT="OWI-EC005O-CORRECTED-PRIVATE-TERMINAL/1"
SPEC_CONTRACT="OWI-EC005O-REVISED-MODERATION-SOURCE-NATIVE/1"
CLASS_SHA="ddfa0ad145cc43f1ab82545912b9e80410c5793b585d31d714f92c07b626dfba"

def select_target(pros,users,fetch_reviews,kind):
    if kind not in TARGETS:
        raise ValueError("undeclared original public task")
    t=TARGETS[kind]
    people=[u for u in users if u.get("username")==t["user"] and
            u.get("account_status")==t["author_status"] and
            isinstance(u.get("_id"),str)]
    profs=[p for p in pros if p.get("name")==t["name"] and
           p.get("specialty")==t["specialty"] and
           isinstance(p.get("professional_id"),str)]
    if len(people)!=1 or len(profs)!=1:
        raise ValueError("original selected public professional/author identity changed")
    user=people[0]
    pro=profs[0]
    reviews=objects(fetch_reviews(pro["professional_id"]))
    matched=[x for x in reviews if x.get("professional_id")==pro["professional_id"]
             and x.get("user_id")==user["_id"] and
             x.get("moderation_status")=="pending" and
             isinstance(x.get("view_id"),str)]
    if len(matched)!=1:
        raise ValueError("original pending public target review cannot be uniquely bound")
    return {"view_id":matched[0]["view_id"],
            "user_id":user["_id"],
            "professional_id":pro["professional_id"],
            "public_author_status":user["account_status"],
            "initial_public_review_sha256":fingerprint(json.dumps(
                matched[0],sort_keys=True))}

def public_status(reply,view_id):
    matches=[x for x in objects(reply) if x.get("view_id")==view_id]
    if len(matches)!=1 or matches[0].get("moderation_status") not in (
        "pending","approved","rejected"):
        raise RuntimeError("actual selected public status readback missing or ambiguous")
    return matches[0]["moderation_status"]

def episode(folder,kind,arm,revised_spec):
    if kind not in TARGETS or arm not in ARMS:
        raise ValueError("undeclared selected intervention")
    t=TARGETS[kind]
    environment=json.loads((folder/"environment.json").read_text())
    if (not isinstance(environment,dict) or
        hashlib.sha256(environment["class_code"].encode()).hexdigest()!=CLASS_SHA):
        raise ValueError("original source class not the pinned family SHA256")
    public=json.loads((folder/"public.json").read_text())
    declared=preflight(public)
    began=time.perf_counter()
    proc=subprocess.Popen(
        docker_worker_args(IMAGE,WORKER,folder/"environment.json"),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,text=True,bufsize=1)
    trace=[]
    final=None
    def call(name,args):
        if name not in declared or set(args)!=set(declared[name].get("required",[])):
            raise ValueError("not an actual public tool invocation")
        proc.stdin.write(json.dumps({"action":"call","tool":name,
                                      "arguments":args})+"\n")
        proc.stdin.flush()
        m=receive(proc)
        if (m.get("kind")!="observation" or m.get("tool")!=name or
            m.get("ok") is not True or m.get("truncated")):
            raise RuntimeError("original source selected public tool protocol failed")
        trace.append({"tool":name,
                      "public_reply_sha256":fingerprint(m.get("content","")),
                      "source_tool_seconds":float(m.get("elapsed_seconds",0))})
        return unpack_reply(m.get("content",""))
    def status(target):
        return public_status(call("get_reviews_for_professional",{
            "professional_id":target["professional_id"]}),target["view_id"])
    def change(target,destination):
        reply=call("change_review_moderation_status",{
            "view_id":target["view_id"],"new_status":destination})
        if not isinstance(reply,dict):
            raise RuntimeError("original public moderation response not a dictionary")
        return reply.get("success") is True

    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("original source checker crossed worker boundary")
        pros=objects(call("list_all_professionals",{}))
        users=objects(call("list_all_users",{}))
        target=select_target(pros,users,
            lambda pid:call("get_reviews_for_professional",{
                "professional_id":pid}),kind)
        first=status(target)
        if first!="pending":
            raise ValueError("original selected review not pending")
        correct_result=None
        wrong_result=None
        reapply_result=None
        status_after_correct=None
        if arm in ("preserve_correct","reapply_correct","regress_wrong"):
            correct_result=change(target,t["correct"])
            status_after_correct=status(target)
            if correct_result is not True or status_after_correct!=t["correct"]:
                raise RuntimeError("source could not achieve real required correct stage1")
            if arm=="reapply_correct":
                reapply_result=change(target,t["correct"])
            if arm=="regress_wrong":
                wrong_result=change(target,t["wrong"])
        elif arm=="direct_wrong":
            wrong_result=change(target,t["wrong"])
        observed_end=status(target)
        proc.stdin.write('{"action":"finish"}\n')
        proc.stdin.flush()
        final=receive(proc)
        if final.get("kind")!="private_final_state":
            raise RuntimeError("original source final-state bridge missing")
        proc.stdin.close()
        if proc.wait(timeout=10)!=0:
            raise RuntimeError("original source restricted worker exit failed")
    finally:
        if proc.poll() is None:proc.kill()
        if proc.stdin and not proc.stdin.closed:proc.stdin.close()
        if proc.stdout:proc.stdout.close()
    elapsed=time.perf_counter()-began
    if (final is None or final.get("tool_calls")!=len(trace)
        or not isinstance(final.get("initial_state"),dict)
        or not isinstance(final.get("state"),dict)):
        raise RuntimeError("selected source provenance/tool counts mismatch")
    scored,checker_elapsed=call_child(
        IMAGE,CHECKER,folder/"verifier.json",
        input_text=json.dumps({"initial_state":final["initial_state"],
                               "state":final["state"]})+"\n")
    if (len(scored)!=1 or scored[0].get("contract")!=CHECKER_CONTRACT
        or scored[0].get("valid") is not True
        or scored[0].get("checks_total")!=9):
        raise RuntimeError("original native private checker contract failed")
    n=scored[0]["checks_passed_if_valid"]
    reward=scored[0]["reward"]
    if (type(n) is not int or not 0<=n<=9 or
        type(reward) not in (int,float) or
        abs(reward-n/9)>5.1e-5):
        raise RuntimeError("original native 9-item checker numerator/value drift")
    # This is the TRUSTED host-only post-terminal state bridge. The source
    # checker is already finished; its full result goes ONLY to a second
    # independent restricted Docker checker, never to the action selector.
    # The revised evaluator derives the real terminal status directly from
    # the source's private final snapshot; 'public_final_status' is cross-
    # checked against that state, not trusted as a scoring oracle.
    corrected_rows,corrected_seconds=call_child(
        IMAGE,REVISED_CHECKER,revised_spec,
        input_text=json.dumps({
            "initial_state":final["initial_state"],
            "state":final["state"],
            "source_class_sha256":CLASS_SHA,
            "public_target":{
                "target_rule":kind,"view_id":target["view_id"],
                "user_id":target["user_id"],
                "professional_id":target["professional_id"],
                "public_initial_status":first,
                "public_final_status":observed_end,
            },
            "original_private_checker":scored[0],
        })+"\n")
    if (len(corrected_rows)!=1 or
        corrected_rows[0].get("contract")!=REVISED_CONTRACT or
        corrected_rows[0].get("valid") is not True or
        corrected_rows[0].get("state_verified_from_original_private_final") is not True or
        corrected_rows[0].get("original_native_reward_unchanged")!=reward or
        corrected_rows[0].get("original_native_checks_passed")!=n):
        raise RuntimeError("separate versioned terminal evaluator did not validate original state")
    corrected=corrected_rows[0]
    return {
        "original_native_and_corrected_private_checkers_separate":True,
        "versioned_corrected_terminal_contract":REVISED_CONTRACT,
        "versioned_corrected_reward":corrected["corrected_reward"],
        "versioned_terminal_state_class":corrected["terminal_state_class"],
        "original_private_state_source_sha256":corrected["private_original_state_sha256_audit_only"],
        "private_terminal_state_sha256":corrected["private_final_state_sha256_audit_only"],
        "corrected_private_target_digest":corrected["private_target_review_sha256"],
        "corrected_private_non_target_untouched":corrected["non_target_state_untouched_verified"],
        "corrected_private_author_professional_verified":corrected["user_and_professional_identity_verified_from_original_private"],
        "corrected_verifier_container_seconds":corrected_seconds,
        "target_rule":kind,"chosen_arm":arm,
        "public_initial_pending":first=="pending",
        "original_public_review_sha256":target["initial_public_review_sha256"],
        "original_public_author_status":target["public_author_status"],
        "original_public_target_sha256":fingerprint(target["view_id"]),
        "source_correct_stage1_accepted":correct_result,
        "public_status_after_real_correction":status_after_correct,
        "source_wrong_stage_accepted":wrong_result,
        "source_safe_reapply_accepted":reapply_result,
        "public_final_status":observed_end,
        "actual_wrong_final_state":observed_end==t["wrong"],
        "original_native_checks_total":9,
        "original_native_checks_passed":n,
        "original_native_reward":reward,
        "actual_selected_tool_calls":len(trace),
        "selected_public_tool_trace":trace,
        "source_worker_wall_seconds":elapsed,
        "private_checker_wall_seconds":checker_elapsed,
        "source_worker_peak_rss_kib":final.get("peak_rss_kib"),
        "original_source_and_checker_unchanged":True,
        "external_custom_reward_added":False,
        "private_state_or_checker_in_policy":False,
    }

def run(directory,revised_spec,seed=14011,repeats=2):
    frozen=json.loads(revised_spec.read_text())
    if frozen.get("contract")!=SPEC_CONTRACT:
        raise ValueError("not frozen versioned corrected specification")
    if repeats!=2:
        raise ValueError("only predeclared two independent resets per arm")
    schedule=[(kind,arm) for kind in TARGETS for arm in ARMS for _ in range(repeats)]
    random.Random(seed).shuffle(schedule)
    trials=[episode(directory/str(ROW),kind,arm,revised_spec) for kind,arm in schedule]
    if len(trials)!=20:
        raise RuntimeError("missing reset source episodes")
    for kind in TARGETS:
        hashes={e["original_public_review_sha256"]
                for e in trials if e["target_rule"]==kind}
        if len(hashes)!=1:
            raise ValueError("not same publicly selected original review per arm")
    return {
        "contract":CONTRACT,"source_original_training_row":ROW,
        "source_full_dataset_unchanged":True,
        "original_native_private_checker_unchanged":True,
        "new_terminal_reward_added":False,
        "policy_trained":False,
        "original_native_and_corrected_checkers_separate":True,
        "versioned_corrected_contract":REVISED_CONTRACT,
        "source_class_sha256":CLASS_SHA,
        "frozen_benchmark_spec_sha256":hashlib.sha256(revised_spec.read_bytes()).hexdigest(),
        "seed":seed,"selected_executions":trials,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",required=True,type=Path)
    p.add_argument("--output",type=Path,default=Path(
        "build/owi_ec005_realtools/versioned_moderation_paired.json"))
    p.add_argument("--revised-spec",required=True,type=Path)
    a=p.parse_args()
    out=run(a.input_dir,a.revised_spec)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("OWI_EC005O_PAIRED_ORIGINAL_AND_VERSIONED_PRIVATE_TERMINAL",json.dumps({
        "contract":out["contract"],"source_train_row":ROW,
        "actual_episodes":len(out["selected_executions"]),
        "unchanged_native_checker":True,"source_full_dataset_unchanged":True,
        "corrected_checker_separate_and_postterminal":True,
    },sort_keys=True))

if __name__=="__main__":
    main()
