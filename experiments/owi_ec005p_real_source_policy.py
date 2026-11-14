#!/usr/bin/env python3
"""OWI-EC005P: on-policy original-source real episode with v1 terminal score.

The choice callback receives ONLY status fields from actual selected original
public read-tool replies, never task-kind/answer/original private state/checker.
This is option selection (STOP / APPROVE / REJECT), not language planning.
Source class, unchanged original checker and O-v1 corrected terminal checker
run in three separate nonroot/network-disabled jailed children. No outcome
from an unchosen option is evaluated at training time.
"""
from __future__ import annotations
import hashlib,json,subprocess,time
from pathlib import Path
from owi_ec005_realtools_goal_policy import (
    docker_worker_args,receive,unpack_reply,WORKER,CHECKER)
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint
from owi_ec005_realtools_native_professional_probe import (
    preflight,objects)
from owi_ec005_versioned_moderation_paired import (
    CLASS_SHA,REVISED_CHECKER,REVISED_CONTRACT,CHECKER_CONTRACT,
    select_target,public_status)

CONTRACT="OWI-EC005P-SOURCE-CHOSEN-ONLY-V1-TERMINAL/1"
OPTIONS=("stop","approved","rejected")
TRAIN_ROW=710
RULES=("banned_reject","eligible_approve")
SOURCE_SHA="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
SPEC_SHA="63252f02eb28cef71b2af7c7ce77afdab2123dc44112598b5b56a25551cd3a7a"

def public_context(author_status,review_status):
    if author_status not in ("banned","active") or review_status not in (
            "pending","approved","rejected"):
        raise ValueError("unknown actual source-public author/review status")
    return author_status+":"+review_status

def public_correct_status(author_status):
    """A fully scripted PUBLIC RULE baseline; never called by learned policy."""
    if author_status=="banned":return "rejected"
    if author_status=="active":return "approved"
    raise ValueError("unsupported known public contract")

def source_episode(folder:Path,rule:str,choose,revised_spec:Path,
                   *,postcorrect=False):
    if rule not in RULES:
        raise ValueError("only frozen source-public target rules admitted")
    if hashlib.sha256(revised_spec.read_bytes()).hexdigest()!=SPEC_SHA:
        raise ValueError("corrected benchmark frozen file byte identity changed")
    env=json.loads((folder/"environment.json").read_text())
    if (not isinstance(env,dict) or
        hashlib.sha256(env.get("class_code","").encode()).hexdigest()!=CLASS_SHA):
        raise ValueError("original source family/class code changed")
    public=json.loads((folder/"public.json").read_text())
    declared=preflight(public)
    began=time.perf_counter()
    proc=subprocess.Popen(docker_worker_args(
        IMAGE,WORKER,folder/"environment.json"),stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,bufsize=1)
    trace=[]
    final=None
    def call(tool,args):
        if tool not in declared or set(args)!=set(declared[tool].get("required",[])):
            raise ValueError("not original public declared tool call")
        proc.stdin.write(json.dumps({
            "action":"call","tool":tool,"arguments":args})+"\n")
        proc.stdin.flush()
        msg=receive(proc)
        if (msg.get("kind")!="observation" or msg.get("tool")!=tool or
            msg.get("ok") is not True or msg.get("truncated")):
            raise RuntimeError("selected original source public observation invalid")
        trace.append({"tool":tool,
                     "public_reply_sha256":fingerprint(msg.get("content","")),
                     "source_tool_seconds":float(msg.get("elapsed_seconds",0))})
        return unpack_reply(msg.get("content",""))
    def status(target):
        resp=call("get_reviews_for_professional",{
            "professional_id":target["professional_id"]})
        return public_status(resp,target["view_id"])
    def mutate(target,dest):
        x=call("change_review_moderation_status",{
            "view_id":target["view_id"],"new_status":dest})
        if not isinstance(x,dict) or x.get("success") is not True:
            raise RuntimeError("selected original source legitimate tool mutation refused")
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("original source worker leaked private verifier")
        professionals=objects(call("list_all_professionals",{}))
        users=objects(call("list_all_users",{}))
        selected=select_target(professionals,users,lambda pid:
            call("get_reviews_for_professional",{"professional_id":pid}),rule)
        original_status=status(selected)
        if original_status!="pending":
            raise ValueError("original source target not in pending state")
        observed_author=selected["public_author_status"]
        if postcorrect:
            # EVALUATION-ONLY initial stage, authored from public user task;
            # NEVER used in on-policy training; not a hidden-state oracle.
            mutate(selected,public_correct_status(observed_author))
            present=status(selected)
            if present!=public_correct_status(observed_author):
                raise RuntimeError("scripted heldout setup not actually corrected")
        else:
            present=original_status
        # THIS is the sole policy decision: only genuinely selected PUBLIC
        # author/review observations, no task name, target IDs or checker.
        context=public_context(observed_author,present)
        choice,propensity=choose(context)
        if choice not in OPTIONS or type(propensity) not in (int,float) or not (
            0<propensity<=1):
            raise ValueError("controller chose unrecognized action/propensity")
        if choice!="stop":
            mutate(selected,choice)
        final_public_status=status(selected)
        proc.stdin.write('{"action":"finish"}\n');proc.stdin.flush()
        final=receive(proc)
        if final.get("kind")!="private_final_state":
            raise RuntimeError("private source-state bridge missing")
        proc.stdin.close()
        if proc.wait(timeout=10)!=0:
            raise RuntimeError("restricted original source worker exited nonzero")
    finally:
        if proc.poll() is None:proc.kill()
        if proc.stdin and not proc.stdin.closed:proc.stdin.close()
        if proc.stdout:proc.stdout.close()
    worker_seconds=time.perf_counter()-began
    if (final is None or final.get("tool_calls")!=len(trace)
        or len(trace)>8 or not isinstance(final.get("initial_state"),dict)
        or not isinstance(final.get("state"),dict)):
        raise RuntimeError("source terminal actual tool call/state receipt drift")
    original,old_sec=call_child(
        IMAGE,CHECKER,folder/"verifier.json",
        input_text=json.dumps({
            "initial_state":final["initial_state"],"state":final["state"]})+"\n")
    if len(original)!=1 or original[0].get("contract")!=CHECKER_CONTRACT or (
            original[0].get("valid") is not True) or (
            original[0].get("checks_total")!=9):
        raise RuntimeError("unchanged original private terminal checker failed")
    native=original[0]
    if type(native.get("checks_passed_if_valid")) is not int or (
        abs(native["reward"]-native["checks_passed_if_valid"]/9)>5.1e-5):
        raise RuntimeError("original native checklist numerator mismatch")
    corrected,new_sec=call_child(
        IMAGE,REVISED_CHECKER,revised_spec,input_text=json.dumps({
            "initial_state":final["initial_state"],"state":final["state"],
            "source_class_sha256":CLASS_SHA,
            "public_target":{
                "target_rule":rule,"view_id":selected["view_id"],
                "user_id":selected["user_id"],
                "professional_id":selected["professional_id"],
                "public_initial_status":original_status,
                "public_final_status":final_public_status,
            },
            "original_private_checker":native,
        })+"\n")
    if (len(corrected)!=1 or corrected[0].get("contract")!=REVISED_CONTRACT
        or corrected[0].get("valid") is not True or
        corrected[0].get("state_verified_from_original_private_final") is not True or
        corrected[0].get("original_native_checks_passed")!=
            native["checks_passed_if_valid"] or
        corrected[0].get("original_native_reward_unchanged")!=native["reward"] or
        corrected[0].get("non_target_state_untouched_verified") is not True):
        raise RuntimeError("versioned independent private final-state verdict invalid")
    result=corrected[0]
    return {
        "contract":CONTRACT,
        "source_original_train_row":TRAIN_ROW,
        "source_full_sha256":SOURCE_SHA,
        "source_class_sha256":CLASS_SHA,
        "corrected_spec_sha256":SPEC_SHA,
        "source_public_task_rule_audit_only":rule,
        "public_observed_context_only":context,
        "policy_selected_option":choice,
        "actual_selected_propensity":propensity,
        "original_source_public_initial_status":original_status,
        "actual_public_status_at_decision":present,
        "actual_public_final_status":final_public_status,
        "evaluation_only_scripted_precorrection":bool(postcorrect),
        "original_native_checker_reward_audit_only":native["reward"],
        "original_native_check_count_audit_only":native["checks_passed_if_valid"],
        "actual_selected_terminal_reward":result["corrected_reward"],
        "private_terminal_class_evaluator_only":result["terminal_state_class"],
        "actual_tool_calls":len(trace),
        "actual_public_source_tool_trace":trace,
        "actual_source_worker_wall_seconds":worker_seconds,
        "source_worker_peak_rss_kib":final.get("peak_rss_kib"),
        "original_native_checker_wall_seconds":old_sec,
        "versioned_checker_wall_seconds":new_sec,
        "private_source_state_or_original_checker_in_policy":False,
        "unchosen_action_outcome_in_policy":False,
    }
