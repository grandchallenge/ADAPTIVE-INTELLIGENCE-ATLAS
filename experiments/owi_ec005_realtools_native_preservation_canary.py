#!/usr/bin/env python3
"""EC005K: source-native terminal sensitivity to task-noncompliant regressions.

One ORIGINAL external task row 2301; no changed initial state, checker,
reward or privileged policy input. All alternative actions are actually
executed on independent source-class instances in a no-network read-only
Docker worker. The native terminal checker runs only after finish in a
different restricted container, never exposed to policy.

All arms first correct BOTH publicly specified schedule fields:
  1. Public read lunch available and dinner unavailable
  2. Real update lunch -> unavailable, dinner -> available
  3. Real public reads verify both corrected state fields
Then at SECOND-STAGE intervention decision:
  STOP              : preserve correct state
  REAPPLY_CORRECT   : redundant safe update, unchanged final status
  REGRESS_NONCOMPLIANT : intentionally undo correction at selected lunch OR dinner
This is an experimental *action contrast*, not a learned policy or
original-state no-probe trial. It can show if a native verifier actually
penalizes a noncompliant regression relative to abstention at this point.
"""
from __future__ import annotations
import argparse,json,random,subprocess,time
from pathlib import Path
from owi_ec005_realtools_goal_policy import (
    docker_worker_args, receive, unpack_reply, WORKER, CHECKER
)
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint
from owi_ec005_realtools_native_schedule_probe import only_public_schedule

ROW=2301
TARGET="MEAL102"
LUNCH="2024-07-14T12:00"
DINNER="2024-07-14T18:00"
ARMS=("stop","reapply_correct","regress_noncompliant")
CONTRACT="OWI-EC005K-ORIGINAL-NATIVE-POSTCORRECTION-PRESERVATION/1"

def stage2_action(arm,slot="lunch"):
    if slot not in ("lunch","dinner"):
        raise ValueError("unsupported source-public schedule target")
    correct="unavailable" if slot=="lunch" else "available"
    wrong="available" if slot=="lunch" else "unavailable"
    if arm=="stop":
        return None
    if arm=="reapply_correct":
        return correct
    if arm=="regress_noncompliant":
        return wrong
    raise ValueError("undeclared experimental intervention")

def read_target(public, tool_response,when=LUNCH):
    if when not in (LUNCH,DINNER):
        raise ValueError("unlisted public service time")
    data=only_public_schedule(public,tool_response,when)
    if (data["target_record_count"]!=1 or
        data["target_public_status"] not in ("available","unavailable")):
        raise ValueError("cannot identify original targeted public lunch schedule")
    return data["target_public_status"]

def episode(folder,arm,slot="lunch"):
    stage2=stage2_action(arm,slot)
    target_when=LUNCH if slot=="lunch" else DINNER
    correct_final="unavailable" if slot=="lunch" else "available"
    public=json.loads((folder/"public.json").read_text())
    allowed={x["name"]:x["parameters"] for x in public["tools"]}
    if (set(allowed.get("update_meal_schedule_availability",{})
                  .get("required",[]))!={"meal_id","scheduled_datetime","availability_sta"}
        or set(allowed.get("get_meal_schedule_by_datetime",{})
                  .get("required",[]))!={"scheduled_datetime"}):
        raise ValueError("original public update/read tool signature drift")
    process=subprocess.Popen(docker_worker_args(
            IMAGE,WORKER,folder/"environment.json"),
            stdin=subprocess.PIPE,stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,text=True,bufsize=1)
    started=time.perf_counter()
    receipt=[]
    terminal=None
    def selected(name,args):
        if set(args)!=set(allowed[name].get("required",[])):
            raise ValueError("unexpected actor action parameters")
        process.stdin.write(json.dumps({"action":"call","tool":name,
                                        "arguments":args})+"\n")
        process.stdin.flush()
        msg=receive(process)
        if (msg.get("kind")!="observation" or msg.get("tool")!=name or
            not msg.get("ok") or msg.get("truncated")):
            raise RuntimeError("selected real public call failed")
        receipt.append({
            "tool":name,
            "public_reply_sha256":fingerprint(msg.get("content","")),
            "actual_selected_tool_seconds":float(msg.get("elapsed_seconds",0)),
        })
        return unpack_reply(msg.get("content",""))
    def read(when=LUNCH):
        return read_target(public,selected("get_meal_schedule_by_datetime",
                                          {"scheduled_datetime":when}),when)
    def update(status,when=LUNCH):
        val=selected("update_meal_schedule_availability",{
            "meal_id":TARGET,"scheduled_datetime":when,
            "availability_sta":status})
        if val.get("success") is not True:
            raise RuntimeError("source tool failed to perform genuine selected mutation")
    try:
        ready=receive(process)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("external original class/verifier isolation drift")
        before=read(LUNCH)
        before_dinner=read(DINNER)
        if before!="available" or before_dinner!="unavailable":
            raise ValueError("source original public meal schedules changed")
        update("unavailable",LUNCH)
        update("available",DINNER)
        observed_after_correction=read(LUNCH)
        observed_dinner_after=read(DINNER)
        if observed_after_correction!="unavailable" or observed_dinner_after!="available":
            raise RuntimeError("public tools did not confirm BOTH corrected schedule states")
        if stage2 is not None:
            update(stage2,target_when)
        # Independent public readback after the last chosen intervention.
        # No internal storage-shape assumptions or privileged state features.
        public_final=read(target_when)
        expected_final=(stage2_action("regress_noncompliant",slot)
                        if arm=="regress_noncompliant" else correct_final)
        if public_final!=expected_final:
            raise RuntimeError("actual public final-state readback inconsistent")
        process.stdin.write('{"action":"finish"}\n')
        process.stdin.flush()
        terminal=receive(process)
        if terminal.get("kind")!="private_final_state":
            raise RuntimeError("private terminal transport drift")
        process.stdin.close()
        if process.wait(timeout=10):
            raise RuntimeError("jailed source class worker failure")
    finally:
        if process.poll() is None:
            process.kill()
        if process.stdin and not process.stdin.closed:
            process.stdin.close()
        if process.stdout:
            process.stdout.close()
    elapsed=time.perf_counter()-started
    if (terminal is None or
        not isinstance(terminal.get("state"),dict) or
        not isinstance(terminal.get("initial_state"),dict) or
        terminal.get("tool_calls")!=len(receipt)):
        raise RuntimeError("source selected action/terminal count mismatch")
    native,check_elapsed=call_child(IMAGE,CHECKER,folder/"verifier.json",
        input_text=json.dumps({"initial_state":terminal["initial_state"],
                               "state":terminal["state"]})+"\n")
    if (len(native)!=1 or native[0].get("contract")!=
        "OWI-EC005-TERMINAL-REWARD/1" or native[0].get("valid") is not True):
        raise RuntimeError("unmodified separate native checker invalid")
    return {
        "chosen_experimental_second_stage":arm,
        "publicly_selected_regression_slot":slot,
        "original_native_reward":float(native[0]["reward"]),
        "original_native_checks_passed":native[0]["checks_passed_if_valid"],
        "original_native_checks_total":native[0]["checks_total"],
        "public_observed_before":"available",
        "public_observed_after_first_correction":"unavailable",
        "public_observed_initial_dinner":"unavailable",
        "public_observed_after_dinner_correction":"available",
        "source_mutation_actually_occurred":True,
        "genuine_final_public_status_evaluator_only":public_final,
        "actual_selected_tool_calls":len(receipt),
        "actual_selected_tool_trace":receipt,
        "source_docker_wall_seconds":elapsed,
        "native_checker_docker_wall_seconds":check_elapsed,
        "source_worker_peak_rss_kib":terminal.get("peak_rss_kib"),
        "private_source_or_checker_in_actor":False,
        "original_native_checker_unchanged":True,
        "posthoc_reward_penalty_introduced":False,
    }

def run(root,seed=2026,repeats=2,slot="lunch"):
    if repeats not in (2,3):
        raise ValueError("repetition bound is predeclared")
    rng=random.Random(seed)
    actions=list(ARMS)*repeats
    rng.shuffle(actions)
    rows=[episode(root/str(ROW),arm,slot=slot) for arm in actions]
    groups={}
    for arm in ARMS:
        v=[x for x in rows if x["chosen_experimental_second_stage"]==arm]
        groups[arm]={
            "executed_episodes":len(v),
            "mean_unmodified_original_native_reward":round(
                sum(x["original_native_reward"] for x in v)/len(v),6),
            "mean_original_native_checks_passed":
                sum(x["original_native_checks_passed"] for x in v)/len(v),
            "mean_actual_selected_tool_calls":
                sum(x["actual_selected_tool_calls"] for x in v)/len(v),
        }
    stop=groups["stop"]["mean_unmodified_original_native_reward"]
    wrong=groups["regress_noncompliant"]["mean_unmodified_original_native_reward"]
    return {
        "contract":CONTRACT,
        "seed":seed,
        "source_row":ROW,
        "public_regression_target_slot":slot,
        "original_initial_state_unchanged":True,
        "both_first_stage_source_schedule_corrections_executed_in_all_arms":True,
        "actual_public_postrepair_observation_before_second_stage":True,
        "native_checker_original_unchanged":True,
        "external_safety_reward_added":False,
        "native_noncompliance_margin_stop_minus_regression":round(stop-wrong,6),
        "strict_native_contract_regression_penalty":stop-wrong>0.00005,
        "controlled_stage2_actions":groups,
        "selected_executions":rows,
        "outcome_only_controller_trained":False,
        "heldout_task_transfer_established":False,
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--input-dir",type=Path,required=True)
    parser.add_argument("--slot",choices=("lunch","dinner"),default="lunch")
    parser.add_argument("--output",type=Path,default=Path(
        "build/owi_ec005_realtools/native_preservation_canary.json"))
    args=parser.parse_args()
    result=run(args.input_dir,slot=args.slot)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("EC005K_ORIGINAL_NATIVE_PRESERVATION_REWARD",json.dumps({
        k:v for k,v in result.items() if k!="selected_executions"},sort_keys=True))

if __name__=="__main__":
    main()
