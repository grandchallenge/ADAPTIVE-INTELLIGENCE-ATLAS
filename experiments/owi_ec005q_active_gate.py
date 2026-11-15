#!/usr/bin/env python3
"""OWI-EC005Q independent original-source and chosen-only causal replay gate.

Reviews real selected tool receipts, exactly reconstructs seed RNG, action
propensities, optional actual probe, stage1 conditional choice and updates from
single realized delayed terminal scalar. Does NOT certify source-independent
generalization or that a constructed masked task is unchanged native benchmark.
"""
from __future__ import annotations
import argparse,collections,json,math,random
from pathlib import Path
from owi_ec005q_active_train import (
    CONTRACT,MODES,BASELINES,SEEDS,TRAIN_EPISODES,STAGES,RULES,
    TwoStageActor,schedule,baseline_choices,eval_baseline_after)
from owi_ec005q_source_active_episode import (
    CONTRACT as EP_CONTRACT,OPTIONS,POST_OPTIONS,
    PRICE_PER_CALL,PRICE_FOR_PROBE,SPEC_SHA,CORPUS_SHA,CLASS_SHA)
from owi_ec005_versioned_moderation_paired import TARGETS

GATE="OWI-EC005Q-INDEPENDENT-REAL-SOURCE-ACTIVE-OBSERVATION-GATE/1"
VALID_FEATURES=("unknown","certified_active","certified_banned","already_resolved")
NORMAL_POST=("active","banned")

def deny(reason):
    raise ValueError(reason)

def finite(x,low,high):
    return type(x) in (float,int) and math.isfinite(x) and low<=x<=high

def check_receipt(e,stage,rule,mode):
    if (not isinstance(e,dict) or e.get("contract")!=EP_CONTRACT or
        e.get("original_source_train_row")!=710 or
        e.get("original_full_corpus_sha256")!=CORPUS_SHA or
        e.get("original_class_sha256")!=CLASS_SHA or
        e.get("separate_corrected_v1_spec_sha256")!=SPEC_SHA or
        e.get("public_versioned_task_is_not_original_source_public_task") is not True or
        e.get("task_kind_evaluator_audit_only")!=rule or
        e.get("versioned_public_stage")!=stage or
        e.get("source_original_initial_pending") is not True or
        e.get("privileged_task_identity_or_source_state_in_actor") is not False or
        e.get("unselected_counterfactual_terminal_outcome_in_actor") is not False or
        e.get("original_source_code_or_original_or_corrected_checker_in_actor") is not False):
        deny("not same original source + separate masked task trust boundary")
    standing=TARGETS[rule]["author_status"]
    correct=TARGETS[rule]["correct"]
    if e.get("source_trusted_original_author_standing_evaluator_only")!=standing:
        deny("real source selected author standing did not match task-public rule")
    expected_feature=("unknown" if stage=="unknown" else
                      "certified_"+standing if stage=="certified" else
                      "already_resolved")
    if e.get("versioned_public_initial_feature")!=expected_feature or (
        e.get("fixture_precorrected_source_review_only")!=(stage=="resolved")):
        deny("source-normalized public observation/fixture scope mismatch")
    initial=e.get("initial_selected_action")
    if initial not in OPTIONS or not finite(e.get("initial_selected_action_propensity"),0.00001,1):
        deny("unsupported original-source on-policy choice/propensity")
    probed=initial=="probe"
    if e.get("physical_optional_probe_executed") is not probed:
        deny("reported optional observation did not correspond to chosen source call")
    if probed:
        if (e.get("actual_selected_original_public_probe_status_evaluator_only")!=standing
            or e.get("postprobe_selected_action") not in POST_OPTIONS or
            not finite(e.get("postprobe_selected_propensity"),0.00001,1)):
            deny("postprobe original source status or chosen repair missing")
        supplied=e.get("policy_supplied_postprobe_signal")
        if mode=="true" and supplied!=standing:
            deny("true actual source probe signal was changed")
        if mode=="zero_probe_signal" and supplied!="blind":
            deny("masked probe reply ablation leaked real source user status")
        if mode=="randomized_probe_signal" and supplied not in NORMAL_POST:
            deny("randomized versioned probe signal invalid")
        if e.get("randomized_probe_reply_ablation")!=(mode=="randomized_probe_signal"):
            deny("mixed true and randomized source probe receipt")
        effective=e["postprobe_selected_action"]
    else:
        if any(e.get(key) is not None for key in (
            "actual_selected_original_public_probe_status_evaluator_only",
            "policy_supplied_postprobe_signal","postprobe_selected_action",
            "postprobe_selected_propensity")) or
            e.get("randomized_probe_reply_ablation") is not False:
            deny("fabricated unchosen optional probe or postprobe observation")
        effective=initial
    if e.get("effective_selected_terminal_action")!=effective:
        deny("real original public action differs from audited policy")
    expected_final=(correct if stage=="resolved" and effective=="stop" else
                    "pending" if effective=="stop" else effective)
    if e.get("source_public_final_review_status")!=expected_final:
        deny("selected public source final readback differs from actual action")
    state_class=("correct" if expected_final==correct else
                 "unchanged_pending" if expected_final=="pending" else "prohibited")
    expected_native_checks=(3 if rule=="banned_reject" else 2) if (
        state_class=="correct") else 1
    n=e.get("original_native_checks_passed_audit_only")
    native=e.get("original_native_checker_reward_audit_only")
    if (n!=expected_native_checks or not finite(native,0,1) or
        abs(native-n/9)>5.1e-5):
        deny("unchanged original-native 9-condition negative-control discrepancy")
    base={"correct":1,"unchanged_pending":0,"prohibited":-1}[state_class]
    expected_reward=round(base+.1*n/9,6)
    if (e.get("corrected_private_terminal_class_audit_only")!=state_class or
        not finite(e.get("actual_selected_versioned_terminal_reward"),-1.1,1.2)
        or abs(e["actual_selected_versioned_terminal_reward"]-expected_reward)>1e-7):
        deny("not real original-source private terminal corrected v1 outcome")
    phases=[("trusted_fixture","list_all_professionals"),
            ("trusted_fixture","list_all_users"),
            ("trusted_fixture","get_reviews_for_professional")]
    if stage=="resolved":
        phases.extend([
            ("trusted_evaluation_fixture","change_review_moderation_status"),
            ("trusted_evaluation_fixture","get_reviews_for_professional")])
    if probed:phases.append(("selected_optional_probe","list_all_users"))
    if effective!="stop":
        phases.append(("selected_policy_action","change_review_moderation_status"))
    phases.append(("selected_final_public_readback","get_reviews_for_professional"))
    actual=e.get("original_source_actual_public_tool_trace")
    if (not isinstance(actual,list) or len(actual)!=len(phases) or
        e.get("original_source_actual_calls")!=len(phases) or
        not 4<=len(actual)<=8):
        deny("source actual selected public fixture/probe/mutation call count drift")
    for got,(phase,tool) in zip(actual,phases):
        if (not isinstance(got,dict) or got.get("phase")!=phase or
            got.get("tool")!=tool or
            not isinstance(got.get("real_public_reply_sha256"),str) or
            len(got["real_public_reply_sha256"])!=64 or
            not all(x in "0123456789abcdef" for x in
                    got["real_public_reply_sha256"]) or
            not finite(got.get("actual_tool_seconds"),0,30)):
            deny("original-source chosen physical public selected-call evidence forged")
    expected_utility=round(expected_reward-PRICE_PER_CALL*len(actual)-
        (PRICE_FOR_PROBE if probed else 0.),6)
    if (not finite(e.get("actual_selected_versioned_utility"),-2,2) or
        abs(e["actual_selected_versioned_utility"]-expected_utility)>1e-7):
        deny("realized actual source tool costs or active probe price wrong")
    for k in ("source_worker_wall_seconds","original_native_checker_wall_seconds",
              "separate_corrected_checker_wall_seconds"):
        if not finite(e.get(k),0,120):
            deny("missing physical source/checker runtime measurements")
    if not finite(e.get("source_worker_peak_rss_kib"),1000,1_000_000):
        deny("missing original source OS worker peak RSS")
    return e["actual_selected_versioned_utility"]

def check_train_mode(seed,mode,rows,expected_frozen):
    if not isinstance(rows,list) or len(rows)!=TRAIN_EPISODES:
        deny("missing original source real training episodes")
    rng=random.Random(seed*1009+MODES.index(mode)*151+17)
    actor=TwoStageActor()
    scenarios=schedule(seed)
    seen_probe=0
    for i,(record,(stage,rule)) in enumerate(zip(rows,scenarios)):
        if (record.get("episode_index")!=i or
            record.get("stage_audit_only")!=stage or
            record.get("target_rule_audit_only")!=rule or
            record.get("all_unchosen_outcomes_unobserved") is not True):
            deny("precommitted chosen original-source randomized scenario drift")
        ep=record.get("source_selected_actual_episode")
        scalar=check_receipt(ep,stage,rule,mode)
        if (record.get("chosen_only_scalar_for_both_actor_stages")!=scalar):
            deny("selected source score substituted with counterfactual or oracle")
        first,pr=actor.initial_choice(
            ep["versioned_public_initial_feature"],rng)
        if (first!=ep["initial_selected_action"] or
            abs(pr-ep["initial_selected_action_propensity"])>1e-12):
            deny("source policy first action not from actual seeded history")
        if first=="probe":
            seen_probe+=1
            if mode=="randomized_probe_signal":
                expected_signal=rng.choice(("banned","active"))
            elif mode=="zero_probe_signal":
                expected_signal="blind"
            else:
                expected_signal=TARGETS[rule]["author_status"]
            if ep["policy_supplied_postprobe_signal"]!=expected_signal:
                deny("postprobe actor signal not derived from actual chosen evidence/ablation RNG")
            post,postpr=actor.post_choice(expected_signal,rng)
            if (post!=ep["postprobe_selected_action"] or
                abs(postpr-ep["postprobe_selected_propensity"])>1e-12):
                deny("postprobe selected action not from chosen-only seeded learner")
        actor.update_from_chosen_only(ep)
    if actor.readable()!=expected_frozen:
        deny("frozen model posttraining state differs from exact chosen-only episode replay")
    if actor.unknown_seen!=32 or actor.readable()["forced_unknown_probe_count"]!=24:
        deny("intended forced original source information support absent")
    if seen_probe<24:
        deny("source-physical selected probe was never explored sufficiently")
    return seen_probe

def check_eval(seed,rows,trained):
    needed={(stage,rule,mode) for stage in STAGES for rule in RULES
            for mode in (*MODES,*BASELINES)}
    if (not isinstance(rows,list) or len(rows)!=len(needed) or
        {(x.get("evaluation_stage"),x.get("target_rule_audit_only"),
          x.get("frozen_model_or_fixed_baseline")) for x in rows}!=needed):
        deny("fresh source evaluation missing frozen model/fixed baseline")
    summary={}
    for r in rows:
        stage,rule,mode=(r["evaluation_stage"],r["target_rule_audit_only"],
                         r["frozen_model_or_fixed_baseline"])
        if r.get("learner_updated_on_evaluation") is not False:
            deny("future evaluation outcomes entered learned training update")
        ep=r.get("source_selected_actual_episode")
        scalar=check_receipt(ep,stage,rule,
            mode if mode in MODES else "true")
        feature=ep["versioned_public_initial_feature"]
        if mode in MODES:
            actor=trained[mode]
            # Rehydrate frozen stage tables from source-replayed read-only model.
            rng=random.Random(seed*1013+MODES.index(mode)*37+
                STAGES.index(stage)*11+RULES.index(rule))
            initial,pr=actor.initial_choice(feature,rng,explore=False)
            if initial=="probe":
                if mode=="randomized_probe_signal":
                    supplied=rng.choice(("banned","active"))
                elif mode=="zero_probe_signal":
                    supplied="blind"
                else:
                    supplied=TARGETS[rule]["author_status"]
                if ep["policy_supplied_postprobe_signal"]!=supplied:
                    deny("prospective probe corruption not reproducible from frozen seed")
                post,postpr=actor.post_choice(supplied,rng,explore=False)
            else:post,postpr=None,None
        else:
            initial,pr=baseline_choices(mode,feature)
            if initial=="probe":
                post,postpr=eval_baseline_after(
                    mode,feature,TARGETS[rule]["author_status"])
            else:post,postpr=None,None
        if (initial!=ep["initial_selected_action"] or
            abs(pr-ep["initial_selected_action_propensity"])>1e-12 or
            post!=ep["postprobe_selected_action"] or
            (postpr is None)!=(ep["postprobe_selected_propensity"] is None) or
            (postpr is not None and abs(
                postpr-ep["postprobe_selected_propensity"])>1e-12)):
            deny("actual source evaluation action differs from frozen/predeclared policy")
        s=summary.setdefault(stage,{}).setdefault(mode,{
            "correct":0,"source_cases":0,"probe_count":0,"utility_sum":0.,
            "reward_sum":0.,"calls_sum":0,"worker_seconds_sum":0.})
        s["source_cases"]+=1
        s["correct"]+=int(ep["corrected_private_terminal_class_audit_only"]=="correct")
        s["probe_count"]+=int(ep["physical_optional_probe_executed"])
        s["utility_sum"]+=scalar
        s["reward_sum"]+=ep["actual_selected_versioned_terminal_reward"]
        s["calls_sum"]+=ep["original_source_actual_calls"]
        s["worker_seconds_sum"]+=ep["source_worker_wall_seconds"]
    for stage,policies in summary.items():
        for name,s in policies.items():
            if s["source_cases"]!=2:deny("not two public task-rule evaluation cases")
            n=s.pop("source_cases")
            s["mean_realized_utility"]=round(s.pop("utility_sum")/n,6)
            s["mean_corrected_reward"]=round(s.pop("reward_sum")/n,6)
            s["mean_source_tool_calls"]=round(s.pop("calls_sum")/n,3)
            s["mean_physical_worker_seconds"]=round(s.pop("worker_seconds_sum")/n,6)
    return summary

def adjudicate(data):
    if (not isinstance(data,dict) or data.get("contract")!=CONTRACT or
        data.get("seed") not in SEEDS or
        data.get("original_corpus_and_checker_unmodified") is not True or
        data.get("generic_source_public_task_is_versioned_and_intentionally_masked") is not True or
        data.get("new_versioned_terminal_reward_not_original_native") is not True or
        data.get("corrected_spec_sha256")!=SPEC_SHA or
        data.get("source_original_train_row")!=710 or
        data.get("one_original_independent_natural_training_family") is not True or
        data.get("chosen_only_delayed_scalar_for_both_policy_stages") is not True or
        data.get("scripted_target_discovery_not_learned") is not True or
        data.get("no_unselected_counterfactual_actions_in_training") is not True or
        data.get("per_mode_real_source_training_episodes")!=TRAIN_EPISODES or
        data.get("total_actual_original_source_training_episodes")!=3*TRAIN_EPISODES or
        data.get("total_actual_original_source_evaluation_episodes")!=48 or
        data.get("total_actual_original_source_episodes")!=3*TRAIN_EPISODES+48 or
        data.get("original_private_checker_invocations")!=3*TRAIN_EPISODES+48 or
        data.get("versioned_corrected_private_checker_invocations")!=3*TRAIN_EPISODES+48 or
        data.get("probe_actual_tool_call_cost")!=PRICE_PER_CALL or
        data.get("optional_probe_additional_design_price")!=PRICE_FOR_PROBE):
        deny("benchmark/genuine source chosen-only experiment admission contract drift")
    train=data.get("training")
    frozen=data.get("frozen_learned_models")
    if (not isinstance(train,dict) or set(train)!=set(MODES) or
        not isinstance(frozen,dict) or set(frozen)!=set(MODES)):
        deny("three independent source-trained intervention ablations incomplete")
    actors={}
    probes={}
    for mode in MODES:
        # Replaying an actual source on-policy chosen action sequence exactly
        # reconstructs frozen actor values, independent of arbitrary labels.
        probes[mode]=check_train_mode(data["seed"],mode,train[mode],frozen[mode])
        # Reconstitute model ONLY from observed chosen terminal scalars.
        actor=TwoStageActor()
        for rec in train[mode]:
            ep=rec["source_selected_actual_episode"]
            actor.update_from_chosen_only(ep)
        if actor.initial.readable()!=frozen[mode]["initial"] or (
            actor.post.readable()!=frozen[mode]["postprobe"]):
            deny("posttraining option table not recoverable from chosen outcomes")
        actors[mode]=actor
    stage_summaries=check_eval(
        data["seed"],data["fresh_prospective_evaluation"],actors)
    uncertain=stage_summaries["unknown"]
    certified=stage_summaries["certified"]
    resolved=stage_summaries["resolved"]
    return {
        "contract":GATE,"seed":data["seed"],
        "original_full_source_sha256":CORPUS_SHA,
        "original_source_class_sha256":CLASS_SHA,
        "new_masked_task_public_wrapper_not_original_native":True,
        "separately_versioned_terminal_v1_spec_sha256":SPEC_SHA,
        "source_train_independent_families":1,
        "actual_original_source_train_episodes":3*TRAIN_EPISODES,
        "actual_original_source_eval_episodes":48,
        "actual_original_source_and_each_checker_runs":3*TRAIN_EPISODES+48,
        "actual_chosen_optional_probes_by_mode":probes,
        "two_stage_online_selected_terminal_scalar_updates_replayed":True,
        "original_native_checker_unmodified":True,
        "source_tool_probes_physically_conditional_and_verified":True,
        "five_seed_bounded_empirical_training_not_lang_model":True,
        "strong_scripted_adaptive_baseline_included":True,
        "scripted_unknown_probe_and_conditional_rule_baseline":True,
        "independent_heldout_original_family_established":False,
        "actual_computation_cost_physical_wall_RSS_recorded_but_FLOPs_not_measured":True,
        "stage_metrics":stage_summaries,
        "unknown_true_minus_adaptive_mean_utility":round(
            uncertain["true"]["mean_realized_utility"]-
            uncertain["scripted_adaptive"]["mean_realized_utility"],6),
        "certified_true_minus_adaptive_mean_utility":round(
            certified["true"]["mean_realized_utility"]-
            certified["scripted_adaptive"]["mean_realized_utility"],6),
        "resolved_true_minus_adaptive_mean_utility":round(
            resolved["true"]["mean_realized_utility"]-
            resolved["scripted_adaptive"]["mean_realized_utility"],6),
        "reflective_self_observation_and_heldout_family_generalization_proved":False,
        "scientific_disposition":"VERSIONED_SOURCE_BACKED_ACTIVE_OBSERVATION_BOUNDED_NOT_GENUINE_FAMILY_TRANSFER",
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--trial",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    result=adjudicate(json.loads(a.trial.read_text()))
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("OWI_EC005Q_REAL_OPTIONAL_SOURCE_PROBE_INDEPENDENT_EVIDENCE_GATE",
          json.dumps(result,sort_keys=True))
if __name__=="__main__":
    main()
