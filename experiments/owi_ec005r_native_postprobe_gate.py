#!/usr/bin/env python3
"""Independent exact-seed REPLAY of native-source postprobe family holdout.

Reject forged source/checker scores, options, reward updating from unchosen
counterfactuals, wrong train families, public task alterations, source tool
traces, retroactive prospective updates and spurious info-value claims.
A five-seed result that cannot beat scripted/direct methods is a valid NEGATIVE.
"""
from __future__ import annotations
import argparse,collections,json,math,random
from pathlib import Path
from owi_ec005r_native_postprobe_train import (
    CONTRACT,SEEDS,MODES,CONTROLS,TRAIN_ROWS,HELDOUT_ROW,TRAIN_PER_MODE,
    EVAL_PER_SEED,FEATURES,OPTIONS,ChosenOptionValues,actor_feature,
    schedule,verify_frozen_manifest)
from owi_ec005r_native_postprobe_episode import (
    CONTRACT as EP_CONTRACT,SOURCE_SHA,ROWS,PRICE,
    FIRST_TOOLS,EXPECTED_TOOL_NAMES,TERMINAL_EXPECT)

GATE="OWI-EC005R-INDEPENDENT-SOURCE-NATIVE-HELDOUT-FAMILY-GATE/1"
def deny(message):
    raise ValueError(message)

def finite(x,minimum,maximum):
    return type(x) in (float,int) and math.isfinite(x) and minimum<=x<=maximum

def proper_hash(x):
    return (isinstance(x,str) and len(x)==64 and
            all(c in "0123456789abcdef" for c in x))

def check_episode(ep,row,mode,*,evaluation=False):
    if (not isinstance(ep,dict) or ep.get("contract")!=EP_CONTRACT or
        ep.get("source_family_row_audit_only")!=row or
        ep.get("source_original_full_corpus_sha256")!=SOURCE_SHA or
        not proper_hash(ep.get("original_source_class_sha256_audit_only")) or
        ep.get("original_public_task_unchanged") is not True or
        ep.get("original_source_initial_state_unchanged") is not True or
        ep.get("original_native_checker_unchanged") is not True or
        ep.get("private_source_state_or_checker_entered_actor") is not False or
        ep.get("unchosen_source_action_reward_entered_actor") is not False or
        ep.get("family_id_entered_actor_as_feature") is not False or
        ep.get("scripted_public_action_planner_not_learned") is not True):
        deny("original source/public/private and actor-information provenance changed")
    arm=ep.get("selected_first_stage_source_arm")
    if arm not in ("probe","direct","stop"):
        deny("original public-source option not predeclared")
    selected=ep.get("selected_postprobe_option")
    actual=ep.get("actual_public_postprobe_signal_audit_only")
    supplied=ep.get("feature_supplied_to_learned_option_actor")
    prob=ep.get("selected_postprobe_action_propensity")
    if arm=="probe":
        if (selected not in OPTIONS or
            actual not in FEATURES[:2] or
            ep.get("scripted_public_followup_queue_nonempty_audit_only") is not
              (actual=="followup_available") or
            ep.get("original_public_first_probe_tool")!=FIRST_TOOLS[row] or
            supplied not in FEATURES or
            not finite(prob,0.00001,1.0)):
            deny("not a physically selected truthful original public probe option")
        if mode=="actual_public_reply" and supplied!=actual:
            deny("true original public reply was masked or substituted")
        if mode=="zero_information" and supplied!="blind":
            deny("zero-feature chosen original source training leaked actual reply")
        if mode=="independently_randomized_reply" and supplied not in FEATURES[:2]:
            deny("randomized original source reply experiment malformed")
        if mode in CONTROLS and supplied!=actual:
            deny("fixed postprobe public script did not see the true public observation")
        expected_arm="probe_"+selected
    else:
        if (selected is not None or actual is not None or
            supplied is not None or prob is not None or
            ep.get("original_public_first_probe_tool") is not None or
            ep.get("scripted_public_followup_queue_nonempty_audit_only") is not None):
            deny("unselected public probe fabricated in a no-probe source episode")
        expected_arm=arm
    tools=EXPECTED_TOOL_NAMES[row][expected_arm]
    traces=ep.get("chosen_real_public_tool_receipts")
    if (not isinstance(traces,list) or len(traces)!=len(tools) or
        ep.get("chosen_actual_original_public_tool_calls")!=len(tools)):
        deny("source-selected original public tool calls missing or forged")
    for trace,name in zip(traces,tools):
        if (not isinstance(trace,dict) or trace.get("tool")!=name or
            trace.get("worker_tool_succeeded") is not True or
            not proper_hash(trace.get("public_reply_sha256")) or
            not finite(trace.get("tool_seconds"),0,90)):
            deny("original public selected tool receipt mismatch")
    total=ep.get("original_native_checks_total")
    passed=ep.get("original_native_checks_passed")
    reward=ep.get("original_source_native_private_reward")
    if (type(total) is not int or not 1<=total<=100 or
        type(passed) is not int or not 0<=passed<=total or
        not finite(reward,0,1) or abs(reward-passed/total)>5.1e-5 or
        abs(reward-TERMINAL_EXPECT[row][expected_arm])>5.1e-5):
        deny("unaltered native original private checker 4-decimal score forged")
    cost=ep.get("chosen_actual_call_cost")
    utility=ep.get("chosen_actual_terminal_utility")
    if (not finite(cost,0,0.3) or
        abs(cost-round(PRICE*len(traces),6))>1e-7 or
        not finite(utility,-1,1) or
        abs(utility-round(reward-cost,6))>1e-7):
        deny("source actual physical-call priced utility substituted")
    retries=ep.get("checker_exact_input_timeout_replays")
    success=ep.get("original_native_checker_wall_seconds")
    overall=ep.get("checker_total_wall_seconds_with_replays")
    if (type(retries) is not int or not 0<=retries<=2 or
        not finite(success,0,121) or not finite(overall,0,400) or
        overall+0.00001<success or
        (retries and overall<119*retries) or
        not finite(ep.get("source_worker_wall_seconds"),0,600) or
        not finite(ep.get("source_worker_peak_rss_kib"),1000,1_000_000)):
        deny("restricted native checker retry or source physical runtime unverifiable")
    return utility

def check_train_seed(seed,mode,rows,frozen):
    if not isinstance(rows,list) or len(rows)!=TRAIN_PER_MODE:
        deny("missing source-private original native chosen training rows")
    rng=random.Random(seed*1009+MODES.index(mode)*151+17)
    actor=ChosenOptionValues()
    for j,(record,index) in enumerate(zip(rows,schedule(seed))):
        if (record.get("episode")!=j or
            record.get("source_family_row_audit_only")!=index or
            index not in TRAIN_ROWS or
            record.get("counterfactual_private_rewards_seen") is not False):
            deny("original source training includes heldout family/foreign oracle")
        ep=record.get("selected_original_source_native_receipt")
        chosen_value=check_episode(ep,index,mode)
        if ep["selected_first_stage_source_arm"]!="probe":
            deny("native original source actual probe not executed in learning")
        raw=ep["actual_public_postprobe_signal_audit_only"]
        expect_feature=actor_feature(raw,mode,rng)
        if ep["feature_supplied_to_learned_option_actor"]!=expect_feature:
            deny("source public reply ablation or independent RNG altered")
        expected_action,pr=actor.select(expect_feature,rng)
        if (ep["selected_postprobe_option"]!=expected_action or
            abs(ep["selected_postprobe_action_propensity"]-pr)>1e-12):
            deny("selected action/propensity cannot be replayed from chosen-only history")
        if record.get("chosen_original_native_utility_used_for_update")!=chosen_value:
            deny("training observed counterfactual or original-score substitution")
        actor.update(expect_feature,expected_action,chosen_value)
    if actor.readback()!=frozen:
        deny("frozen original-native source postprobe option model not replayable")
    return actor

def expected_baseline(row,control):
    if control=="direct_no_probe":return "direct",None
    if control=="stop_no_probe":return "stop",None
    if control=="public_affordance_adaptive":
        return ("probe","continue") if row==0 else ("direct",None)
    if control=="always_continue_after_probe":return "probe","continue"
    if control=="always_stop_after_probe":return "probe","stop"
    if control=="scripted_public_status":return "probe","continue"
    deny("undeclared strong original public-task scripted comparator")

def check_eval(seed,records,trained):
    required={(row,model) for row in ROWS for model in (*MODES,*CONTROLS)}
    if (not isinstance(records,list) or len(records)!=EVAL_PER_SEED or
        {(x.get("original_family_row_evaluator_only"),
          x.get("policy")) for x in records}!=required):
        deny("heldout real source family prospective evaluation missing a policy")
    report={}
    for item in records:
        row,mode=item["original_family_row_evaluator_only"],item["policy"]
        if (item.get("actor_updated_using_heldout_or_evaluation_outcome") is not False
            or item.get("heldout_distinct_family_for_actor")!=(row==HELDOUT_ROW)):
            deny("source-native independent heldout family opened to training")
        ep=item.get("original_source_selected_native_receipt")
        check_episode(ep,row,mode)
        if mode in MODES:
            actor=trained[mode]
            rng=random.Random(seed*1013+MODES.index(mode)*37+row)
            feature=actor_feature(ep["actual_public_postprobe_signal_audit_only"],
                                  mode,rng)
            action,pr=actor.select(feature,rng,explore=False)
            if (ep["selected_first_stage_source_arm"]!="probe" or
                ep["feature_supplied_to_learned_option_actor"]!=feature or
                ep["selected_postprobe_option"]!=action or
                abs(ep["selected_postprobe_action_propensity"]-pr)>1e-12):
                deny("prospective original family source result not from frozen actor")
        else:
            arm,post=expected_baseline(row,mode)
            if (ep["selected_first_stage_source_arm"]!=arm or
                ep["selected_postprobe_option"]!=post or
                (post is not None and ep["selected_postprobe_action_propensity"]!=1.0)):
                deny("strong public native comparator did not execute itself")
        report.setdefault(str(row),{})[mode]={
            "actual_native_reward":ep["original_source_native_private_reward"],
            "actual_real_call_count":ep["chosen_actual_original_public_tool_calls"],
            "actual_realized_utility":ep["chosen_actual_terminal_utility"],
            "actual_source_worker_seconds":ep["source_worker_wall_seconds"],
            "checker_replay_count":ep["checker_exact_input_timeout_replays"],
            "selected_postprobe_option":ep["selected_postprobe_option"],
        }
    return report

def adjudicate(r,*,task_spec):
    task_sha=verify_frozen_manifest(task_spec)
    if (not isinstance(r,dict) or r.get("contract")!=CONTRACT or
        r.get("seed") not in SEEDS or
        r.get("source_whole_original_sha256")!=SOURCE_SHA or
        r.get("frozen_source_native_holdout_protocol_sha256")!=task_sha or
        r.get("original_public_tasks_and_classes_and_verifiers_unchanged") is not True or
        r.get("source_original_partition_train_only") is not True or
        r.get("train_rows")!=list(TRAIN_ROWS) or
        r.get("heldout_original_distinct_family_row")!=HELDOUT_ROW or
        r.get("source_original_native_private_checker_only") is not True or
        r.get("source_original_private_checker_was_not_in_actor") is not True or
        r.get("no_source_oracle_or_unchosen_outcomes_in_learned_credits") is not True or
        r.get("first_public_probe_mandatory_not_learned") is not True or
        r.get("family_tool_arguments_and_public_reply_interpretation_scripted") is not True or
        r.get("actual_original_source_training_episodes")!=len(MODES)*TRAIN_PER_MODE or
        r.get("actual_original_source_heldout_and_source_train_evaluation_episodes")!=EVAL_PER_SEED or
        r.get("actual_source_original_checker_invocations")!=len(MODES)*TRAIN_PER_MODE+EVAL_PER_SEED):
        deny("no exact original-native source lock or preregistered experiment")
    family_map=r.get("source_executable_class_sha256_by_family")
    if (not isinstance(family_map,dict) or set(family_map)!={"0","2","3"} or
        not all(proper_hash(x) for x in family_map.values()) or
        len(set(family_map.values()))!=3):
        deny("training vs heldout distinct source families not established")
    trains=r.get("training")
    models=r.get("frozen_policies")
    if (not isinstance(trains,dict) or set(trains)!=set(MODES) or
        not isinstance(models,dict) or set(models)!=set(MODES)):
        deny("one of three independent training ablations or source-frozen models missing")
    actors={}
    supports={}
    for m in MODES:
        actors[m]=check_train_seed(r["seed"],m,trains[m],models[m])
        supports[m]=collections.Counter(
            x["selected_original_source_native_receipt"][
                "actual_public_postprobe_signal_audit_only"] for x in trains[m])
        for rec in trains[m]:
            ep=rec["selected_original_source_native_receipt"]
            index=rec["source_family_row_audit_only"]
            if ep["original_source_class_sha256_audit_only"]!=family_map[str(index)]:
                deny("training family executable source class provenance forged")
    report=check_eval(r["seed"],r["fresh_source_evaluation"],actors)
    for rec in r["fresh_source_evaluation"]:
        index=rec["original_family_row_evaluator_only"]
        ep=rec["original_source_selected_native_receipt"]
        if ep["original_source_class_sha256_audit_only"]!=family_map[str(index)]:
            deny("heldout original source executable family identity replaced")
    heldout=report["3"]
    # Required explicit negative science: only ORIGINAL natural source
    # state is in train; if all first read replies are positive, absence of
    # blocked/clean training support must not be called information discovery.
    both_natural_signals={
        m:dict(supports[m]) for m in MODES}
    original_signal_support_has_both=(
        all(supports[m].get("followup_available",0)>0 and
            supports[m].get("no_followup",0)>0 for m in MODES))
    for row in ("0","2","3"):
        base=report[row]["public_affordance_adaptive"]["actual_realized_utility"]
        if not all(report[row][k]["actual_realized_utility"]<=base+0.000051
                   for k in (*MODES,*CONTROLS)):
            deny("strong comparator is not a source-native option-arm ceiling; revisit baseline")
    return {
        "contract":GATE,"seed":r["seed"],
        "source_original_full_sha256":SOURCE_SHA,
        "versioned_protocol_sha256":task_sha,
        "original_public_task_and_native_private_checker_unchanged":True,
        "train_genuinely_independent_source_families":[0,2],
        "withheld_original_distinct_source_family":3,
        "never_opened_sealed_dev_or_test_family":True,
        "known_previously_studied_train_partition_holdout_not_pristine_task":True,
        "actual_original_source_chosen_training_episodes":len(MODES)*TRAIN_PER_MODE,
        "actual_original_source_prospective_evaluation_episodes":EVAL_PER_SEED,
        "actual_original_native_private_checker_invocations":len(MODES)*TRAIN_PER_MODE+EVAL_PER_SEED,
        "public_reply_semantic_feature_parsed_by_script_not_learned":True,
        "postprobe_selected_utility_only_policy_updates_verified":True,
        "original_native_reward_only_no_reweighting":True,
        "mandatory_first_probe_not_a_learned_decision":True,
        "natural_source_first_probe_feature_support":both_natural_signals,
        "both_natural_initial_postprobe_signal_classes_supported":original_signal_support_has_both,
        "heldout_family_actual_native_policy_results":heldout,
        "per_family_actual_native_results":report,
        "heldout_true_minus_direct_utility":round(
            heldout["actual_public_reply"]["actual_realized_utility"]-
            heldout["direct_no_probe"]["actual_realized_utility"],6),
        "heldout_true_minus_strong_script_utility":round(
            heldout["actual_public_reply"]["actual_realized_utility"]-
            heldout["public_affordance_adaptive"]["actual_realized_utility"],6),
        "scientific_disposition":"GENUINE_NATIVE_SOURCE_FAMILY_HELDOUT_POSTPROBE_OPTION_TEST_NOT_EPISTEMIC_SUPERIORITY",
        "cross_family_reflective_causal_identification_proved":False,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--trial",type=Path,required=True)
    p.add_argument("--task-spec",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    result=adjudicate(json.loads(a.trial.read_text()),task_spec=a.task_spec)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("OWI_EC005R_REAL_NATIVE_FAMILY_HELDOUT_INDEPENDENT_GATE",
          json.dumps(result,sort_keys=True))
if __name__=="__main__":
    main()
