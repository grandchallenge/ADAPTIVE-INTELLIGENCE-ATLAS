#!/usr/bin/env python3
"""EC005Q: genuinely conditional source-tool probe in a VERSIONED masked task.

The unchanged original class executes all mutations in its existing restricted
Docker worker. Author/target binding is trusted benchmark fixture setup, NOT
policy observation. For an unknown target, actor receives NO author identity,
original task statement, or status until it elects an actual source-public
list_all_users probe. Policy selects postprobe action after that real tool reply.

The original train row 710 public task is deliberately replaced for the actor
with an explicitly new *generic task interface*, never represented as natural
original-source public information structure. Original private 9-check and
separately governed corrected v1 terminal checkers run after finish in distinct
OS jails. No counterfactual or private verifier is available to the actor.
"""
from __future__ import annotations
import hashlib,json,math,subprocess,time
from pathlib import Path
from owi_ec005_realtools_goal_policy import (
    docker_worker_args,receive,unpack_reply,WORKER,CHECKER)
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint
from owi_ec005_realtools_native_professional_probe import (
    ROW,preflight,objects)
from owi_ec005_versioned_moderation_paired import (
    TARGETS,select_target,public_status,CLASS_SHA,
    REVISED_CHECKER,REVISED_CONTRACT,CHECKER_CONTRACT)

CONTRACT="OWI-EC005Q-ACTUAL-OPTIONAL-PROBE-AND-TERMINAL/1"
SPEC_SHA="63252f02eb28cef71b2af7c7ce77afdab2123dc44112598b5b56a25551cd3a7a"
CORPUS_SHA="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
STAGES=("unknown","certified","resolved")
OPTIONS=("stop","approved","rejected","probe")
POST_OPTIONS=("stop","approved","rejected")
PRICE_PER_CALL=0.002
PRICE_FOR_PROBE=0.020

def source_episode(folder:Path,kind:str,stage:str,initial_decision,
                   conditional_decision,revised_spec:Path,
                   *,probe_mode="true",rng=None):
    if kind not in TARGETS or stage not in STAGES:
        raise ValueError("outside preregistered original TRAIN row/rule/stage")
    if probe_mode not in ("true","zero_probe_signal","randomized_probe_signal"):
        raise ValueError("not an approved versioned observation ablation")
    if probe_mode=="randomized_probe_signal" and rng is None:
        raise ValueError("independent randomized probe reply requires seeded RNG")
    if hashlib.sha256(revised_spec.read_bytes()).hexdigest()!=SPEC_SHA:
        raise ValueError("separately versioned corrected terminal spec changed")
    env=json.loads((folder/"environment.json").read_text())
    if (not isinstance(env,dict) or
        hashlib.sha256(env.get("class_code","").encode()).hexdigest()!=CLASS_SHA):
        raise ValueError("underlying original source class not pinned")
    public=json.loads((folder/"public.json").read_text())
    declared=preflight(public)
    started=time.perf_counter()
    proc=subprocess.Popen(
        docker_worker_args(IMAGE,WORKER,folder/"environment.json"),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,
        text=True,bufsize=1)
    trace=[]
    final=None
    def call(name,args,phase):
        if name not in declared or set(args)!=set(declared[name].get("required",[])):
            raise ValueError("unrecognized source public action or arguments")
        proc.stdin.write(json.dumps({"action":"call","tool":name,
                                      "arguments":args})+"\n")
        proc.stdin.flush()
        msg=receive(proc)
        if (msg.get("kind")!="observation" or msg.get("tool")!=name or
            msg.get("ok") is not True or msg.get("truncated")):
            raise RuntimeError("actual source public tool response invalid")
        trace.append({
            "phase":phase,"tool":name,
            "real_public_reply_sha256":fingerprint(msg.get("content","")),
            "actual_tool_seconds":float(msg.get("elapsed_seconds",0))})
        return unpack_reply(msg.get("content",""))
    def query_status(target,phase):
        return public_status(call("get_reviews_for_professional",{
            "professional_id":target["professional_id"]},phase),
            target["view_id"])
    def mutate(target,status,phase):
        resp=call("change_review_moderation_status",{
            "view_id":target["view_id"],"new_status":status},phase)
        if not isinstance(resp,dict) or resp.get("success") is not True:
            raise RuntimeError("actual original public selected mutation refused")
    def target_status_from_public_reply(users,target):
        records=[u for u in objects(users) if u.get("_id")==target["user_id"]]
        if len(records)!=1 or records[0].get("account_status") not in ("banned","active"):
            raise RuntimeError("actual source-public selected author status unknown")
        return records[0]["account_status"]
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("original private checker crossed source worker boundary")
        # Benchmark fixture is trusted infrastructure, not the actor:
        # physically call selected original source-public discovery APIs.
        profs=objects(call("list_all_professionals",{},"trusted_fixture"))
        initial_users_raw=call("list_all_users",{},"trusted_fixture")
        initial_users=objects(initial_users_raw)
        target=select_target(
            profs,initial_users,lambda pid:call(
                "get_reviews_for_professional",{
                    "professional_id":pid},"trusted_fixture"),kind)
        original_public_status="pending"
        public_author=target_status_from_public_reply(initial_users_raw,target)
        if public_author!=TARGETS[kind]["author_status"]:
            raise RuntimeError("original source author standing changed")
        correct=("rejected" if public_author=="banned" else "approved")
        scripted_fixture_correction=False
        if stage=="resolved":
            # Explicitly source-executed setup, never an agent action/repair.
            mutate(target,correct,"trusted_evaluation_fixture")
            observed=query_status(target,"trusted_evaluation_fixture")
            if observed!=correct:
                raise RuntimeError("source-original resolved condition not established")
            scripted_fixture_correction=True
        if stage=="unknown":
            start_feature="unknown"
        elif stage=="certified":
            # Source-authentic original public status cached in a VERSIONED
            # synthetic task observation; no extra policy probe necessary.
            start_feature="certified_"+public_author
        else:
            start_feature="already_resolved"
        first=initial_decision(start_feature)
        if (not isinstance(first,tuple) or len(first)!=2 or
            first[0] not in OPTIONS or type(first[1]) not in (float,int) or
            not math.isfinite(first[1]) or not 0<first[1]<=1):
            raise RuntimeError("initial source actor not a valid on-policy decision")
        initial_action,initial_propensity=first
        effective_action=initial_action
        actual_probe_status=None
        supplied_probe_status=None
        post_action=None
        post_propensity=None
        probe_signal_randomized=False
        if initial_action=="probe":
            # Only here does the actor actually purchase the live source-public
            # observation; the fixture's earlier private target selection is
            # explicitly NOT a free learned observation.
            observed=call("list_all_users",{},"selected_optional_probe")
            actual_probe_status=target_status_from_public_reply(observed,target)
            if probe_mode=="true":
                supplied_probe_status=actual_probe_status
            elif probe_mode=="zero_probe_signal":
                supplied_probe_status="blind"
            else:
                # Explicitly independent binary observation corruption.
                # Never claim that this altered supplied reply is the
                # original unmodified source's tool response.
                supplied_probe_status=rng.choice(("banned","active"))
                probe_signal_randomized=True
            p=conditional_decision(supplied_probe_status)
            if (not isinstance(p,tuple) or len(p)!=2 or
                p[0] not in POST_OPTIONS or type(p[1]) not in (float,int) or
                not math.isfinite(p[1]) or not 0<p[1]<=1):
                raise RuntimeError("conditional postprobe policy decision invalid")
            post_action,post_propensity=p
            effective_action=post_action
        if effective_action!="stop":
            mutate(target,effective_action,"selected_policy_action")
        final_status=query_status(target,"selected_final_public_readback")
        proc.stdin.write('{"action":"finish"}\n')
        proc.stdin.flush()
        final=receive(proc)
        if final.get("kind")!="private_final_state":
            raise RuntimeError("original worker missing trusted terminal state")
        proc.stdin.close()
        if proc.wait(timeout=10)!=0:
            raise RuntimeError("restricted original source worker failed")
    finally:
        if proc.poll() is None:proc.kill()
        if proc.stdin and not proc.stdin.closed:proc.stdin.close()
        if proc.stdout:proc.stdout.close()
    wall=time.perf_counter()-started
    if (final is None or final.get("tool_calls")!=len(trace) or
        not 4<=len(trace)<=8 or
        not isinstance(final.get("initial_state"),dict) or
        not isinstance(final.get("state"),dict)):
        raise RuntimeError("private final source-state bridge/actual call count mismatch")
    orig,old_sec=call_child(IMAGE,CHECKER,folder/"verifier.json",
        input_text=json.dumps({"initial_state":final["initial_state"],
                               "state":final["state"]})+"\n")
    if (len(orig)!=1 or orig[0].get("contract")!=CHECKER_CONTRACT or
        orig[0].get("valid") is not True or orig[0].get("checks_total")!=9):
        raise RuntimeError("unaltered original native private checker invalid")
    original=orig[0]
    n=original["checks_passed_if_valid"]
    if (type(n) is not int or not 0<=n<=9 or
        abs(original["reward"]-n/9)>5.1e-5):
        raise RuntimeError("unaltered native checker numerator mismatch")
    corrected,new_sec=call_child(IMAGE,REVISED_CHECKER,revised_spec,
        input_text=json.dumps({
            "initial_state":final["initial_state"],
            "state":final["state"],"source_class_sha256":CLASS_SHA,
            "public_target":{
                "target_rule":kind,"view_id":target["view_id"],
                "user_id":target["user_id"],
                "professional_id":target["professional_id"],
                "public_initial_status":original_public_status,
                "public_final_status":final_status},
            "original_private_checker":original,
        })+"\n")
    if (len(corrected)!=1 or
        corrected[0].get("contract")!=REVISED_CONTRACT or
        corrected[0].get("valid") is not True or
        corrected[0].get("original_native_checks_passed")!=n or
        corrected[0].get("original_native_reward_unchanged")!=original["reward"] or
        corrected[0].get("state_verified_from_original_private_final") is not True or
        corrected[0].get("non_target_state_untouched_verified") is not True):
        raise RuntimeError("separate corrected terminal source-private verifier invalid")
    new=corrected[0]
    utility=round(new["corrected_reward"]-
                  PRICE_PER_CALL*len(trace)-
                  (PRICE_FOR_PROBE if initial_action=="probe" else 0.),6)
    return {
        "contract":CONTRACT,"original_source_train_row":ROW,
        "original_full_corpus_sha256":CORPUS_SHA,
        "original_class_sha256":CLASS_SHA,
        "separate_corrected_v1_spec_sha256":SPEC_SHA,
        "public_versioned_task_is_not_original_source_public_task":True,
        "task_kind_evaluator_audit_only":kind,
        "source_trusted_original_author_standing_evaluator_only":public_author,
        "versioned_public_stage":stage,
        "versioned_public_initial_feature":start_feature,
        "source_original_initial_pending":True,
        "fixture_precorrected_source_review_only":scripted_fixture_correction,
        "initial_selected_action":initial_action,
        "initial_selected_action_propensity":float(initial_propensity),
        "physical_optional_probe_executed":initial_action=="probe",
        "actual_selected_original_public_probe_status_evaluator_only":
            actual_probe_status,
        "policy_supplied_postprobe_signal":supplied_probe_status,
        "postprobe_selected_action":post_action,
        "postprobe_selected_propensity":(
            float(post_propensity) if post_propensity is not None else None),
        "randomized_probe_reply_ablation":probe_signal_randomized,
        "effective_selected_terminal_action":effective_action,
        "source_public_final_review_status":final_status,
        "original_native_checker_reward_audit_only":original["reward"],
        "original_native_checks_passed_audit_only":n,
        "corrected_private_terminal_class_audit_only":new["terminal_state_class"],
        "actual_selected_versioned_terminal_reward":new["corrected_reward"],
        "actual_selected_versioned_utility":utility,
        "original_source_actual_calls":len(trace),
        "original_source_actual_public_tool_trace":trace,
        "source_worker_wall_seconds":wall,
        "original_native_checker_wall_seconds":old_sec,
        "separate_corrected_checker_wall_seconds":new_sec,
        "source_worker_peak_rss_kib":final.get("peak_rss_kib"),
        "privileged_task_identity_or_source_state_in_actor":False,
        "unselected_counterfactual_terminal_outcome_in_actor":False,
        "original_source_code_or_original_or_corrected_checker_in_actor":False,
    }
