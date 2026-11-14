#!/usr/bin/env python3
"""Independent source-locked chosen-only training/evaluation evidence gate.

Rejects forged outcomes, fabricated selection propensity, altered source,
nonphysical public traces, incorrect original/native v1 score, ablation leakage,
retrospective evaluation updates and overclaims. A scientific NEGATIVE result
passes if real original-source evidence is complete and honestly recorded.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,math
from pathlib import Path
from owi_ec005p_chosen_outcome_train import (
    CONTRACT,SEEDS,MODES,RULES,OPTIONS,STAGES,EVAL_BASELINES,
    TRAIN_EPISODES,PRICE_PER_ACTUAL_TOOL_CALL)
from owi_ec005p_real_source_policy import SPEC_SHA,SOURCE_SHA,CLASS_SHA

CONTRACT_GATE="OWI-EC005P-INDEPENDENT-CHOSEN-OUTCOME-RESEARCH-GATE/1"
CORRECT_ACTION={"banned_reject":"rejected","eligible_approve":"approved"}
BASE={"correct":1.0,"unchanged_pending":0.0,"prohibited":-1.0}

def deny(message):
    raise ValueError(message)

def check_hash(s):
    return isinstance(s,str) and len(s)==64 and all(c in "0123456789abcdef" for c in s)

def expected_class(rule,action,stage):
    if rule not in RULES or action not in OPTIONS or stage not in STAGES:
        deny("undeclared source public task/action/mechanism")
    if action=="stop":
        return "unchanged_pending" if stage=="initial_pending" else "correct"
    return "correct" if action==CORRECT_ACTION[rule] else "prohibited"

def check_terminal(rule,action,stage,reward,native):
    if any(type(v) not in (int,float) or not math.isfinite(v)
           for v in (reward,native)):
        deny("invalid actual source-native terminal outcome scalar")
    num=round(9*native)
    if not 0<=num<=9 or abs(native-num/9)>5.1e-5:
        deny("forged unchanged original native scalar")
    class_name=expected_class(rule,action,stage)
    expected=round(BASE[class_name]+0.1*num/9,6)
    if abs(reward-expected)>1e-7:
        deny("original private terminal outcome and frozen v1 formula mismatch")
    return class_name

def check_trace(rows,calls):
    if (type(calls) is not int or not 3<=calls<=8 or
        not isinstance(rows,list) or len(rows)!=calls):
        deny("selected actual public tool call receipt count mismatch")
    names=[v.get("tool") for v in rows if isinstance(v,dict)]
    if (len(names)!=calls or names.count("list_all_professionals")!=1 or
        names.count("list_all_users")!=1 or
        names.count("get_reviews_for_professional")<2):
        deny("actual original source public discovery/final read missing")
    for v in rows:
        if (not check_hash(v.get("public_reply_sha256")) or
            type(v.get("source_tool_seconds")) not in (float,int) or
            not 0<=v["source_tool_seconds"]<60):
            deny("selected public source receipts forged or invalid")

def check_training_episode(mode,row,i,previous):
    if (row.get("episode_index")!=i or
        row.get("train_rule_audit_only") not in RULES or
        row.get("source_selected_action") not in OPTIONS or
        row.get("private_state_or_checker_in_actor") is not False or
        row.get("unchosen_counterfactual_outcome_in_update") is not False or
        row.get("actual_source_tool_calls") is None):
        deny("training private leakage, task or action provenance drift")
    feat=row.get("feature_actually_supplied_to_policy")
    if mode=="zero_information":
        if feat!="blind":deny("zero-information feature ablation contaminated")
    elif feat not in ("active:pending","banned:pending"):
        deny("learned actual source-public normal feature not valid")
    expected=("banned:pending" if
              row["train_rule_audit_only"]=="banned_reject" else "active:pending")
    if mode!="zero_information" and feat!=expected:
        deny("source-public identity feature mismatched actual original rule")
    propensity=row.get("source_selected_propensity")
    if type(propensity) not in (int,float) or not 0<propensity<=1:
        deny("chosen on-policy behavior propensity not recorded")
    reward=row.get("chosen_actual_corrected_terminal_reward")
    native=row.get("chosen_actual_original_native_reward_audit_only")
    check_terminal(row["train_rule_audit_only"],row["source_selected_action"],
                   "initial_pending",reward,native)
    calls=row["actual_source_tool_calls"]
    expected_calls=5 if row["source_selected_action"]=="stop" else 6
    if calls!=expected_calls:
        deny("original source initial-stage intervention call count drift")
    check_trace(row.get("real_source_selected_public_receipts"),calls)
    actual_utility=row.get("chosen_actual_utility")
    if (type(actual_utility) not in (int,float) or
        abs(actual_utility-round(reward-PRICE_PER_ACTUAL_TOOL_CALL*calls,6))>1e-7):
        deny("actual chosen only scalar utility or real source cost forged")
    assigned=row.get("assigned_scalar_to_policy_update")
    origin=row.get("assigned_scalar_origin_episode")
    if type(origin) is not int or not 0<=origin<=i:
        deny("shuffled scalar credit origin missing or from the future")
    if mode=="shuffled_chosen_outcome_credit" and i>0:
        if origin>=i or abs(assigned-previous[origin])>1e-7:
            deny("shuffled credit did not derive from a PRIOR actual chosen scalar")
    elif origin!=i or abs(assigned-actual_utility)>1e-7:
        deny("true chosen-only reward was misassigned")
    for k in ("source_worker_wall_seconds","original_native_checker_wall_seconds",
              "versioned_private_checker_wall_seconds"):
        v=row.get(k)
        if type(v) not in (int,float) or not math.isfinite(v) or not 0<=v<120:
            deny("missing actually measured original/paired checker wall time")
    rss=row.get("peak_source_worker_rss_kib")
    if type(rss) is not int or not 1000<=rss<=1_000_000:
        deny("source-reported worker peak RSS implausible")
    return actual_utility

def check_evaluation(row):
    if (row.get("evaluation_stage") not in STAGES or
        row.get("source_public_rule_audit_only") not in RULES or
        row.get("model") not in (*MODES,*EVAL_BASELINES) or
        row.get("selected_option") not in OPTIONS or
        row.get("learned_policy_updated_during_evaluation") is not False):
        deny("undeclared or contaminated prospective actual source evaluation")
    rule,action,stage=(row["source_public_rule_audit_only"],
                       row["selected_option"],row["evaluation_stage"])
    expected=check_terminal(rule,action,stage,
                            row.get("real_corrected_reward"),
                            row.get("real_original_native_reward"))
    if row.get("real_terminal_class")!=expected:
        deny("versioned original-private terminal class does not match public rule")
    if row["model"]=="zero_information":
        if row.get("policy_feature")!="blind":
            deny("evaluation zero-feature ablation leaked public user status")
    elif row.get("policy_feature")!=(
            ("banned" if rule=="banned_reject" else "active")+":"+(
                "pending" if stage=="initial_pending" else
                CORRECT_ACTION[rule])):
        deny("evaluation actual public feature identity mismatch")
    if row["model"] in EVAL_BASELINES:
        baseline={"always_stop":"stop","always_approve":"approved",
                  "always_reject":"rejected"}
        expected_action=(CORRECT_ACTION[rule] if
                         row["model"]=="public_rule_correct" else
                         baseline[row["model"]])
        if action!=expected_action:
            deny("predeclared fixed-policy baseline did not execute")
    calls=row.get("real_public_tool_calls")
    expected_calls=(5 if action=="stop" else 6)+(
        2 if stage=="heldout_postcorrect" else 0)
    if calls!=expected_calls:
        deny("actual source evaluation call budget mismatched action/stage")
    check_trace(row.get("actual_public_selected_call_hashes"),calls)
    if (type(row.get("realized_utility")) not in (int,float) or
        abs(row["realized_utility"]-round(
            row["real_corrected_reward"]-PRICE_PER_ACTUAL_TOOL_CALL*calls,6))>1e-7):
        deny("prospective evaluation realized utility modified")
    for k in ("actual_worker_wall_seconds",
              "actual_original_checker_wall_seconds",
              "actual_corrected_checker_wall_seconds"):
        v=row.get(k)
        if type(v) not in (int,float) or not math.isfinite(v) or not 0<=v<120:
            deny("missing physical source or checker elapsed evidence")

def adjudicate(r):
    if (not isinstance(r,dict) or r.get("contract")!=CONTRACT or
        r.get("seed") not in SEEDS or
        r.get("original_source_train_row")!=710 or
        r.get("original_source_and_original_native_checker_unchanged") is not True or
        r.get("frozen_corrected_spec_sha256")!=SPEC_SHA or
        r.get("new_versioned_reward_not_original_native") is not True or
        r.get("experimental_modes")!=list(MODES) or
        r.get("separate_independently_retrained_policy_per_mode") is not True or
        r.get("chosen_outcome_only_online_updates") is not True or
        r.get("train_episodes_per_mode")!=TRAIN_EPISODES or
        r.get("actual_original_source_train_episodes")!=TRAIN_EPISODES*len(MODES) or
        r.get("baseline_actions_evaluator_only")!=list(EVAL_BASELINES) or
        r.get("heldout_postcorrection_stage_not_source_family_holdout") is not True or
        r.get("policy_learns_next_option_only_not_tool_planning") is not True or
        r.get("fixed_price_per_actual_tool_call")!=PRICE_PER_ACTUAL_TOOL_CALL):
        deny("source-locked model/benchmark identity or honest scope flags drift")
    trains=r.get("training")
    frozen=r.get("frozen_learned_option_tables")
    if (not isinstance(trains,dict) or set(trains)!=set(MODES) or
        not isinstance(frozen,dict) or set(frozen)!=set(MODES)):
        deny("one of separately retrained information ablations unavailable")
    for mode,rows in trains.items():
        if not isinstance(rows,list) or len(rows)!=TRAIN_EPISODES:
            deny("actual on-policy source training episodes missing")
        counts=collections.Counter(x.get("train_rule_audit_only") for x in rows)
        if any(counts[t]!=TRAIN_EPISODES//len(RULES) for t in RULES):
            deny("not balanced original source target training visits")
        historical={}
        for i,rec in enumerate(rows):
            v=check_training_episode(mode,rec,i,historical)
            historical[i]=v
        tables=frozen[mode]
        observed=collections.defaultdict(lambda:collections.Counter())
        sums=collections.defaultdict(lambda:collections.defaultdict(float))
        for x in rows:
            key=x["feature_actually_supplied_to_policy"]
            option=x["source_selected_action"]
            observed[key][option]+=1
            sums[key][option]+=x["assigned_scalar_to_policy_update"]
        if set(tables)!=set(observed):
            deny("frozen learned model features differ from actual chosen training")
        for k,t in tables.items():
            for a in OPTIONS:
                if t["n_by_option"][a]!=observed[k][a]:
                    deny("frozen model count was forged or retroactively updated")
                val=t["mean_utility_by_option"][a]
                expected=(round(sums[k][a]/observed[k][a],6)
                          if observed[k][a] else None)
                if val!=expected:
                    deny("frozen model value table altered after actual chosen updates")
            greedy=max(range(len(OPTIONS)),
                       key=lambda i:((sums[k][OPTIONS[i]]/observed[k][OPTIONS[i]]
                        if observed[k][OPTIONS[i]] else -math.inf),-i))
            if t["greedy"]!=OPTIONS[greedy]:
                deny("frozen learned policy selection inconsistent with chosen outcomes")
    evals=r.get("prospective_actual_source_evaluation")
    wanted={(stage,rule,model) for stage in STAGES for rule in RULES
            for model in (*MODES,*EVAL_BASELINES)}
    if (not isinstance(evals,list) or len(evals)!=len(wanted) or
        {(v.get("evaluation_stage"),v.get("source_public_rule_audit_only"),
          v.get("model")) for v in evals}!=wanted or
        r.get("actual_original_source_evaluation_episodes")!=len(wanted)):
        deny("prospective source evaluation incomplete or duplicate")
    for rec in evals:
        check_evaluation(rec)
        model=rec["model"]
        if model in MODES:
            key=rec["policy_feature"]
            actor=frozen[model]
            expected=actor[key]["greedy"] if key in actor else "stop"
            if rec["selected_option"]!=expected:
                deny("post-training learned option differed from frozen source-learned policy")
    summaries={}
    for stage in STAGES:
        subset=[x for x in evals if x["evaluation_stage"]==stage]
        row={}
        for m in (*MODES,*EVAL_BASELINES):
            mine=[x for x in subset if x["model"]==m]
            row[m]={
                "actual_real_source_cases":len(mine),
                "mean_original_native_reward":round(
                    sum(x["real_original_native_reward"] for x in mine)/len(mine),6),
                "mean_corrected_reward":round(
                    sum(x["real_corrected_reward"] for x in mine)/len(mine),6),
                "mean_realized_utility":round(
                    sum(x["realized_utility"] for x in mine)/len(mine),6),
                "mean_actual_source_tool_calls":round(
                    sum(x["real_public_tool_calls"] for x in mine)/len(mine),3),
                "correct_terminal_count":sum(
                    x["real_terminal_class"]=="correct" for x in mine),
            }
        summaries[stage]=row
    return {
        "contract":CONTRACT_GATE,"seed":r["seed"],
        "original_source_train_row":710,
        "original_source_class_sha256":CLASS_SHA,
        "original_full_source_sha256":SOURCE_SHA,
        "frozen_new_corrected_reward_spec_sha256":SPEC_SHA,
        "source_episodes_train":TRAIN_EPISODES*len(MODES),
        "source_episodes_eval":len(evals),
        "total_source_ep_and_two_separate_private_checks":TRAIN_EPISODES*len(MODES)+len(evals),
        "original_native_checker_untouched":True,
        "new_terminal_reward_not_original_native":True,
        "selected_outcome_only_online_policy_training_established":True,
        "learned_tool_planning_or_runtime_reflection_established":False,
        "independent_original_source_families":1,
        "heldout_different_independent_family_established":False,
        "task_public_procedure_script_is_strong_fixed_baseline":True,
        "shuffled_credit_is_prior_actual_chosen_scalar_not_unselected_counterfactual":True,
        "per_stage_prospective_actual_source":summaries,
        "policy_selection_vs_public_rule_correct_initial_delta_utility":round(
            summaries["initial_pending"]["true"]["mean_realized_utility"]-
            summaries["initial_pending"]["public_rule_correct"]["mean_realized_utility"],6),
        "reflective_causal_identification_proved":False,
        "scientific_disposition":"BOUNDED_REAL_CHOSEN_ONLY_OPTION_LEARNING_NOT_REFLECTIVE_CONTROL",
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--trial",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    result=adjudicate(json.loads(a.trial.read_text()))
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("OWI_EC005P_INDEPENDENT_REAL_SOURCE_RESEARCH_GATE",
          json.dumps(result,sort_keys=True))
if __name__=="__main__":
    main()
