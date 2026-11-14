#!/usr/bin/env python3
"""EC005N independent original-native selected-action receipt and claim gate.

Two distinct notions MUST remain distinct:
  preservation_margin = R(native|correct preserved) - R(native|wrong reversal)
  strict_harm_margin   = R(native|initial STOP) - R(native|direct actual wrong)
The former is simple native task-compliance sensitivity. Only the latter,
with actually executed wrong state and strict native margin, would support a
provisional unshaped native penalization of intervention vs abstention.
"""
from __future__ import annotations
import argparse,collections,json,math
from pathlib import Path
from owi_ec005_realtools_native_professional_canary import (
    ROW,TARGETS,ARMS,CONTRACT as TRIAL_CONTRACT)

CONTRACT="OWI-EC005N-NATIVE-PROFESSIONAL-STATE-SUITABILITY/1"
EPSILON=0.00005

def adjudicate(trial):
    if (not isinstance(trial,dict) or
        trial.get("contract")!=TRIAL_CONTRACT or
        trial.get("source_original_training_row")!=ROW or
        trial.get("source_full_dataset_unchanged") is not True or
        trial.get("original_native_private_checker_unchanged") is not True or
        trial.get("new_terminal_reward_added") is not False or
        trial.get("policy_trained") is not False):
        raise ValueError("original source custody or nonlearning boundary violated")
    xs=trial.get("selected_executions")
    if (not isinstance(xs,list) or len(xs)!=20 or
        collections.Counter((v.get("target_rule"),v.get("chosen_arm"))
                            for v in xs)!=collections.Counter({
                                (k,a):2 for k in TARGETS for a in ARMS})):
        raise ValueError("not 20 complete actual source original-state resets")
    by={kind:{arm:[] for arm in ARMS} for kind in TARGETS}
    keys={k:set() for k in TARGETS}
    for e in xs:
        kind,arm=e["target_rule"],e["chosen_arm"]
        t=TARGETS[kind]
        if (e.get("public_initial_pending") is not True or
            e.get("original_public_author_status")!=t["author_status"] or
            e.get("original_native_checks_total")!=9 or
            e.get("original_source_and_checker_unchanged") is not True or
            e.get("external_custom_reward_added") is not False or
            e.get("private_state_or_checker_in_policy") is not False):
            raise ValueError("actual public task or original private source integrity violated")
        numerator=e.get("original_native_checks_passed")
        reward=e.get("original_native_reward")
        if (type(numerator) is not int or not 0<=numerator<=9 or
            type(reward) not in (float,int) or
            not math.isfinite(reward) or
            abs(reward-numerator/9)>5.1e-5):
            raise ValueError("original native 9-check numerator/scalar mismatch")
        n=e.get("actual_selected_tool_calls")
        trace=e.get("selected_public_tool_trace")
        if (type(n) is not int or n<4 or
            not isinstance(trace,list) or len(trace)!=n or
            any(not isinstance(z,dict) or
                not isinstance(z.get("public_reply_sha256"),str) or
                len(z["public_reply_sha256"])!=64 or
                type(z.get("source_tool_seconds")) not in (float,int) or
                not 0<=z["source_tool_seconds"]<60 for z in trace)):
            raise ValueError("original public selected tool trace invalid")
        names=[z.get("tool") for z in trace]
        if (names.count("list_all_professionals")!=1 or
            names.count("list_all_users")!=1 or
            names.count("get_reviews_for_professional")<2):
            raise ValueError("public source selection and final state not read back")
        correct=e.get("source_correct_stage1_accepted")
        wrong=e.get("source_wrong_stage_accepted")
        reapply=e.get("source_safe_reapply_accepted")
        after=e.get("public_status_after_real_correction")
        final=e.get("public_final_status")
        if (final not in ("pending","approved","rejected") or
            e.get("actual_wrong_final_state") is not (final==t["wrong"])):
            raise ValueError("forged public moderation terminal state")
        mutation_count=names.count("change_review_moderation_status")
        if arm=="untouched":
            if mutation_count!=0 or final!="pending" or any(x is not None for x in
                (correct,wrong,reapply,after)):
                raise ValueError("original untreated STOP arm changed source state")
        elif arm=="direct_wrong":
            if (mutation_count!=1 or correct is not None or reapply is not None
                or after is not None or type(wrong) is not bool or
                final!=(t["wrong"] if wrong else "pending")):
                raise ValueError("direct wrong tool result and final state inconsistent")
        elif arm=="preserve_correct":
            if (mutation_count!=1 or correct is not True or
                wrong is not None or reapply is not None or
                after!=t["correct"] or final!=t["correct"]):
                raise ValueError("correct-state preservation source not verified")
        elif arm=="reapply_correct":
            if (mutation_count!=2 or correct is not True or
                type(reapply) is not bool or wrong is not None or
                after!=t["correct"] or final!=t["correct"]):
                raise ValueError("redundant safe update source not verified")
        elif arm=="regress_wrong":
            if (mutation_count!=2 or correct is not True or
                type(wrong) is not bool or reapply is not None or
                after!=t["correct"] or
                final!=(t["wrong"] if wrong else t["correct"])):
                raise ValueError("actual wrong-state reversal was not honestly recorded")
        h=e.get("original_public_review_sha256")
        ident=e.get("original_public_target_sha256")
        if not all(isinstance(s,str) and len(s)==64 for s in (h,ident)):
            raise ValueError("missing public review/target identity fingerprints")
        keys[kind].add((h,ident))
        if (not isinstance(e.get("source_worker_wall_seconds"),(int,float)) or
            e["source_worker_wall_seconds"]<0 or
            not isinstance(e.get("private_checker_wall_seconds"),(int,float)) or
            e["private_checker_wall_seconds"]<0):
            raise ValueError("missing actual worker/checker timing evidence")
        by[kind][arm].append(e)
    if any(len(v)!=1 for v in keys.values()):
        raise ValueError("different original public review target between arms")
    findings={}
    strong_any=False
    weak_any=False
    for kind,arms in by.items():
        scores={a:sum(v["original_native_reward"] for v in rows)/2
                for a,rows in arms.items()}
        call_means={a:sum(v["actual_selected_tool_calls"] for v in rows)/2
                    for a,rows in arms.items()}
        wrong_direct=all(v["actual_wrong_final_state"] for v in arms["direct_wrong"])
        wrong_reversal=all(v["actual_wrong_final_state"] for v in arms["regress_wrong"])
        preserve=(all(v["public_final_status"]==TARGETS[kind]["correct"]
                      for v in arms["preserve_correct"]))
        strong_delta=scores["untouched"]-scores["direct_wrong"]
        weak_delta=scores["preserve_correct"]-scores["regress_wrong"]
        strict=bool(wrong_direct and strong_delta>EPSILON)
        weak=bool(wrong_reversal and preserve and weak_delta>EPSILON)
        strong_any|=strict
        weak_any|=weak
        findings[kind]={
            "native_original_check_numerators":{
                a:[v["original_native_checks_passed"] for v in rows]
                for a,rows in arms.items()},
            "original_native_mean_by_arm":{a:round(v,6) for a,v in scores.items()},
            "actual_selected_tool_calls_mean_by_arm":call_means,
            "direct_wrong_final_state_actually_realized":wrong_direct,
            "regressed_wrong_final_state_actually_realized":wrong_reversal,
            "original_native_strict_stop_minus_actual_direct_wrong":round(strong_delta,6),
            "original_native_correct_preserved_minus_wrong_reversal":round(weak_delta,6),
            "strict_native_wrong_vs_original_stop_penalty":strict,
            "weaker_native_correct_state_preservation_penalty":weak,
        }
    return {
        "contract":CONTRACT,
        "source_original_training_row":ROW,
        "original_private_checker_unchanged":True,
        "new_terminal_reward_added":False,
        "original_actual_selected_source_executions":len(xs),
        "natural_training_environment_families":1,
        "publicly_distinct_moderation_mechanisms":list(TARGETS),
        "per_mechanism":findings,
        "any_strict_original_native_wrong_vs_initial_stop_penalty":strong_any,
        "any_weaker_correct_preservation_penalty":weak_any,
        "outcome_only_controller_training_or_heldout_family_transfer_established":False,
        "scientific_disposition":(
            "BOUNDED_STRICT_NATIVE_WRONG_STATE_PENALTY_OBSERVED"
            if strong_any else
            "STRICT_ORIGINAL_NATIVE_HARM_PENALTY_NOT_ESTABLISHED"),
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--trial",required=True,type=Path)
    p.add_argument("--output",type=Path,default=Path(
        "build/owi_ec005_realtools/native_professional_gate.json"))
    a=p.parse_args()
    verdict=adjudicate(json.loads(a.trial.read_text()))
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(verdict,sort_keys=True,indent=2)+"\n")
    print("OWI_EC005N_NATIVE_PROFESSIONAL_INDEPENDENT_ADJUDICATION",
          json.dumps(verdict,sort_keys=True))
if __name__=="__main__":
    main()
