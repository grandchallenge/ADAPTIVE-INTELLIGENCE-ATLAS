#!/usr/bin/env python3
"""R: ORIGINAL source-public task + physical probe + source-native terminal checker.

Unlike engineered Q, neither the source's original public task nor its initial
state is edited. Train original source class families 0,2; evaluate a third
independent family 3 only AFTER freezing the chosen-outcome policy. A scoped,
hand-authored tool-execution policy translates public requests and selected
tool replies into admissible follow-up source calls; only CONTINUE versus STOP
after the first genuine source read is learned. Its queue-nonempty feature is
explicitly scripted public interpretation, NOT learned language understanding.

Any private final source state goes only to the distinct restricted original
checker OS child after the episode. No source code/checklist/state leaks to
the decision. This is original-native reward, NOT Q/O engineered reward.
"""
from __future__ import annotations
import hashlib,json,math,subprocess,time
from pathlib import Path
from owi_ec005_realtools_heterogeneous_trial import Policy,ARMS,PRICE
from owi_ec005_realtools_goal_policy import (
    docker_worker_args,receive,WORKER,CHECKER)
from owi_ec005_realtools_randomized import IMAGE,fingerprint
from owi_ec005q_source_active_episode import private_terminal_score_with_timeout_replay

CONTRACT="OWI-EC005R-ORIGINAL-NATIVE-SOURCE-POSTPROBE/1"
SOURCE_SHA="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
ROWS=(0,2,3)
FIRST_TOOLS={
    0:"list_user_subscriptions",
    2:"check_user_account_status",
    3:"get_dietary_restriction_by_id",
}
TERMINAL_EXPECT={
    0:{"stop":0.25,"direct":0.25,
       "probe_stop":0.25,"probe_continue":0.5},
    2:{"stop":6/13,"direct":7/13,
       "probe_stop":6/13,"probe_continue":7/13},
    3:{"stop":6/21,"direct":10/21,
       "probe_stop":6/21,"probe_continue":10/21},
}
EXPECTED_TOOL_NAMES={
    0:{"stop":[],"direct":[],
       "probe_stop":["list_user_subscriptions"],
       "probe_continue":["list_user_subscriptions","get_product_by_id",
         "check_subscription_links","cancel_subscription",
         "invalidate_future_payments","halt_scheduled_shipments",
         "modify_subscription_details"]},
    2:{"stop":[],"direct":["update_user_account_status"],
       "probe_stop":["check_user_account_status"],
       "probe_continue":["check_user_account_status",
                         "update_user_account_status"]},
    3:{"stop":[],"direct":["create_dietary_restriction"],
       "probe_stop":["get_dietary_restriction_by_id"],
       "probe_continue":["get_dietary_restriction_by_id",
                         "create_dietary_restriction"]},
}

def original_public_file(folder:Path):
    public=json.loads((folder/"public.json").read_text())
    if not isinstance(public,dict) or set(public)!={"messages","tools"}:
        raise ValueError("original source public task changed or private leakage")
    return public

def source_native_episode(folder:Path,index:int,arm:str,select_after_probe=None):
    if index not in ROWS or arm not in ARMS:
        raise ValueError("not preregistered original source family/arm")
    if (arm=="probe")!=(select_after_probe is not None):
        raise ValueError("only selected live probe may invoke postprobe actor")
    public=original_public_file(folder)
    scripted=Policy(index,public,arm)  # public task, public selected replies only
    original_source=json.loads((folder/"environment.json").read_text())
    class_code=original_source.get("class_code")
    if not isinstance(class_code,str) or len(class_code)<100:
        raise ValueError("trusted audit source class missing")
    class_sha=hashlib.sha256(class_code.encode()).hexdigest()
    del original_source,class_code
    proc=subprocess.Popen(
        docker_worker_args(IMAGE,WORKER,folder/"environment.json"),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,text=True,bufsize=1)
    start=time.perf_counter()
    traces=[]
    terminal=None
    actual_public_signal=None
    supplied_actor_signal=None
    second_action=None
    second_propensity=None
    semantic_queue_from_public=False
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("source worker contains forbidden original native verifier")
        while True:
            command=scripted.next_action()
            proc.stdin.write(json.dumps(command,sort_keys=True)+"\n")
            proc.stdin.flush()
            reply=receive(proc)
            if command["action"]=="finish":
                if reply.get("kind")!="private_final_state":
                    raise RuntimeError("actual original source terminal state missing")
                terminal=reply
                break
            if (reply.get("kind")!="observation" or
                reply.get("tool")!=command["tool"] or
                reply.get("truncated") or reply.get("ok") is not True):
                raise RuntimeError("original selected source tool failed or changed contract")
            scripted.observe(reply)
            traces.append({
                "tool":command["tool"],
                "public_reply_sha256":fingerprint(reply.get("content","")),
                "tool_seconds":float(reply.get("elapsed_seconds",0)),
                "worker_tool_succeeded":True})
            if arm=="probe" and len(traces)==1:
                if command["tool"]!=FIRST_TOOLS[index]:
                    raise RuntimeError("not the actual original family public first probe")
                # This semantic feature is computed by the PREAUTHORED
                # public response planner, not the actor, which is limited
                # to one learned binary option choice. It may leak how to
                # interpret a task while not leaking any source private state.
                semantic_queue_from_public=bool(scripted.queue)
                actual_public_signal=("followup_available" if
                                      semantic_queue_from_public else "no_followup")
                result=select_after_probe(actual_public_signal)
                if (not isinstance(result,(list,tuple)) or len(result)!=3 or
                    result[0] not in ("stop","continue") or
                    not isinstance(result[1],(float,int)) or
                    not math.isfinite(result[1]) or not 0<result[1]<=1 or
                    result[2] not in ("followup_available","no_followup","blind")):
                    raise ValueError("postprobe learned action/propensity/feature invalid")
                second_action,second_propensity,supplied_actor_signal=result
                if second_action=="stop":
                    scripted.queue=[]
        proc.stdin.close()
        if proc.wait(timeout=15):
            raise RuntimeError("original restricted source child nonzero")
    finally:
        if proc.poll() is None:
            proc.kill()
        if proc.stdin and not proc.stdin.closed:proc.stdin.close()
        if proc.stdout:proc.stdout.close()
    worker_elapsed=time.perf_counter()-start
    if terminal is None or terminal.get("tool_calls")!=len(traces):
        raise RuntimeError("actual selected tool count or source-final bridge mismatch")
    if (not isinstance(terminal.get("initial_state"),dict) or
        not isinstance(terminal.get("state"),dict)):
        raise RuntimeError("source-native terminal initial/final state missing")
    expected_arm=(arm if arm!="probe" else "probe_"+second_action)
    if [x["tool"] for x in traces]!=EXPECTED_TOOL_NAMES[index][expected_arm]:
        raise RuntimeError("unexpected original source-public selected action sequence")
    private_input=json.dumps({
        "initial_state":terminal["initial_state"],
        "state":terminal["state"]})+"\n"
    checked,checker_seconds,retries,checker_total=private_terminal_score_with_timeout_replay(
        CHECKER,folder/"verifier.json",private_input)
    if len(checked)!=1 or checked[0].get("contract")!=(
            "OWI-EC005-TERMINAL-REWARD/1") or (
            checked[0].get("valid") is not True):
        raise RuntimeError("source-native private checklist invalid, never valid zero")
    native=checked[0]
    total=native.get("checks_total")
    passed=native.get("checks_passed_if_valid")
    reward=native.get("reward")
    if (type(total) is not int or type(passed) is not int or
        total<=0 or not 0<=passed<=total or
        type(reward) not in (float,int) or not math.isfinite(reward) or
        abs(reward-passed/total)>0.000051 or
        abs(reward-TERMINAL_EXPECT[index][expected_arm])>0.000051):
        raise RuntimeError("original-native independent checklist count/score changed")
    utility=round(reward-PRICE*len(traces),6)
    return {
        "contract":CONTRACT,"source_family_row_audit_only":index,
        "original_source_class_sha256_audit_only":class_sha,
        "original_public_task_unchanged":True,
        "original_source_initial_state_unchanged":True,
        "original_native_checker_unchanged":True,
        "source_original_full_corpus_sha256":SOURCE_SHA,
        "selected_first_stage_source_arm":arm,
        "original_public_first_probe_tool":FIRST_TOOLS[index] if arm=="probe" else None,
        "actual_public_postprobe_signal_audit_only":actual_public_signal,
        "scripted_public_followup_queue_nonempty_audit_only":semantic_queue_from_public if arm=="probe" else None,
        "feature_supplied_to_learned_option_actor":supplied_actor_signal,
        "selected_postprobe_option":second_action,
        "selected_postprobe_action_propensity":second_propensity,
        "original_source_native_private_reward":reward,
        "original_native_checks_passed":passed,
        "original_native_checks_total":total,
        "chosen_actual_call_cost":round(PRICE*len(traces),6),
        "chosen_actual_terminal_utility":utility,
        "chosen_actual_original_public_tool_calls":len(traces),
        "chosen_real_public_tool_receipts":traces,
        "source_worker_wall_seconds":worker_elapsed,
        "original_native_checker_wall_seconds":checker_seconds,
        "checker_total_wall_seconds_with_replays":checker_total,
        "checker_exact_input_timeout_replays":retries,
        "source_worker_peak_rss_kib":terminal.get("peak_rss_kib"),
        "private_source_state_or_checker_entered_actor":False,
        "unchosen_source_action_reward_entered_actor":False,
        "family_id_entered_actor_as_feature":False,
        "scripted_public_action_planner_not_learned":True,
    }
