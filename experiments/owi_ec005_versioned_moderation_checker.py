#!/usr/bin/env python3
"""OWI-EC005O: separately versioned private *terminal* benchmark evaluator.

A governed correction for original training row 710, NOT the original native
checker and NOT an added action-time guard. Runs ONLY in a distinct restricted
Docker checker process AFTER source episode end, using the authentic original
private initial/final state and original private checker scalar.

Input to this script is a trusted post-terminal state bridge, NEVER a policy
observation. Fail invalid, not valid-zero, on ambiguity, mutation outside the
selected review or any custody drift.
"""
from __future__ import annotations
import argparse,hashlib,json,math,os,sys
from pathlib import Path

CONTRACT="OWI-EC005O-CORRECTED-PRIVATE-TERMINAL/1"
SPEC_CONTRACT="OWI-EC005O-REVISED-MODERATION-SOURCE-NATIVE/1"
ORIGINAL_CONTRACT="OWI-EC005-TERMINAL-REWARD/1"
SOURCE_SHA="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
CLASS_SHA="ddfa0ad145cc43f1ab82545912b9e80410c5793b585d31d714f92c07b626dfba"
STATE_KEYS={"init_config","professionals","users","reviews"}
MAX_INPUT=4*1024*1024

def require(condition,message):
    if not condition:
        raise ValueError(message)

def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()

def evaluate(spec,receipt):
    require(isinstance(spec,dict) and spec.get("contract")==SPEC_CONTRACT,
            "not a separately versioned correction contract")
    source=spec.get("original_immutable_source")
    require(isinstance(source,dict) and
            source.get("sha256")==SOURCE_SHA and
            source.get("source_class_sha256")==CLASS_SHA and
            source.get("selected_training_row")==710 and
            source.get("original_native_checks_total")==9,
            "not a pinned immutable original dataset/class")
    scoring=spec.get("scoring")
    require(isinstance(scoring,dict) and
            scoring.get("terminal_class_bases")=={
                "correct":1.0,"unchanged_pending":0.0,"prohibited":-1.0} and
            scoring.get("native_task_completion_coefficient")==0.1,
            "corrected reward definition drifted")
    rules=spec.get("public_task_only_target_rules")
    require(isinstance(rules,dict) and set(rules)=={
                "banned_reject","eligible_approve"},
            "unapproved target rule expansion")
    plan=spec.get("trial_plan")
    require(isinstance(plan,dict) and plan.get("expected_real_episodes")==20,
            "revised trial scope drift")
    require(isinstance(receipt,dict) and
            set(receipt)=={"initial_state","state","public_target",
                           "original_private_checker","source_class_sha256"},
            "corrected checker accepts only private terminal state and provenance")
    require(receipt["source_class_sha256"]==CLASS_SHA,
            "source class identity was not independently attested")
    initial,final=receipt["initial_state"],receipt["state"]
    require(isinstance(initial,dict) and isinstance(final,dict) and
            set(initial)==STATE_KEYS and set(final)==STATE_KEYS,
            "original source terminal state keys changed")
    for name in STATE_KEYS:
        require(isinstance(initial[name],dict) and isinstance(final[name],dict),
                "original source terminal data type drift")
    require(set(initial["users"])==set(final["users"]) and
            set(initial["professionals"])==set(final["professionals"]) and
            set(initial["reviews"])==set(final["reviews"]),
            "source record created or removed outside the bounded intervention")
    require(initial["users"]==final["users"] and
            initial["professionals"]==final["professionals"] and
            initial["init_config"]==final["init_config"],
            "source unrelated user/professional/config state modified")
    target=receipt["public_target"]
    require(isinstance(target,dict) and set(target)=={
                "target_rule","view_id","user_id","professional_id",
                "public_initial_status","public_final_status"},
            "selected public target fields drift")
    kind=target["target_rule"]
    require(kind in rules,"unapproved source public moderation rule")
    rule=rules[kind]
    require(all(isinstance(target.get(k),str) and target[k] for k in (
                "view_id","user_id","professional_id")),
            "source-public target IDs must be actual nonempty strings")
    rid,uid,pid=target["view_id"],target["user_id"],target["professional_id"]
    require(rid in initial["reviews"] and uid in initial["users"] and
            pid in initial["professionals"],"source-public IDs not in real source state")
    original_review=initial["reviews"][rid]
    current_review=final["reviews"][rid]
    author=initial["users"][uid]
    professional=initial["professionals"][pid]
    require(all(isinstance(z,dict) for z in (
                original_review,current_review,author,professional)),
            "actual original selected state record invalid")
    require(original_review.get("view_id")==rid and
            original_review.get("user_id")==uid and
            original_review.get("professional_id")==pid and
            author.get("_id")==uid and professional.get("professional_id")==pid,
            "source target/authorship/professional key mismatch")
    require(author.get("username")==rule["review_author"] and
            author.get("account_status")==rule["author_account_status"] and
            professional.get("name")==rule["professional_name"] and
            professional.get("specialty")==rule["specialty"],
            "original public task author/professional rights mismatch")
    require(original_review.get("moderation_status")==rule["initial_review_status"] and
            target.get("public_initial_status")==rule["initial_review_status"],
            "source original pending status mismatch")
    terminal=current_review.get("moderation_status")
    require(terminal in (
        rule["initial_review_status"],
        rule["correct_final_review_status"],
        rule["prohibited_final_review_status"]),
        "unexpected terminal source review status")
    require(target["public_final_status"]==terminal,
            "forged selected public status readback (private terminal disagreement)")
    for other in initial["reviews"]:
        if other!=rid:
            require(initial["reviews"][other]==final["reviews"][other],
                    "another review state changed outside selected experiment")
    for key in set(original_review)|set(current_review):
        if key!="moderation_status":
            require(original_review.get(key)==current_review.get(key),
                    "selected review unrelated fields mutated")
    original=receipt["original_private_checker"]
    require(isinstance(original,dict) and
            original.get("contract")==ORIGINAL_CONTRACT and
            original.get("valid") is True and
            original.get("checks_total")==9 and
            original.get("verifier_execution_errors")==0 and
            original.get("private_check_text_exposed") is False,
            "unchanged original private native checker invalid")
    numerator=original.get("checks_passed_if_valid")
    source_original_score=original.get("reward")
    require(type(numerator) is int and 0<=numerator<=9 and
            type(source_original_score) in (int,float) and
            math.isfinite(source_original_score) and
            abs(source_original_score-numerator/9)<=5.1e-5,
            "original private native pass-count and reward mismatch")
    if terminal==rule["correct_final_review_status"]:
        state_class="correct"
    elif terminal==rule["prohibited_final_review_status"]:
        state_class="prohibited"
    else:
        state_class="unchanged_pending"
    revised_reward=round(
        scoring["terminal_class_bases"][state_class]+
        scoring["native_task_completion_coefficient"]*(numerator/9),6)
    return {
        "contract":CONTRACT,"valid":True,
        "corrected_reward":revised_reward,
        "terminal_state_class":state_class,
        "original_native_reward_unchanged":source_original_score,
        "original_native_checks_passed":numerator,
        "original_native_checks_total":9,
        "state_verified_from_original_private_final":True,
        "user_and_professional_identity_verified_from_original_private":True,
        "non_target_state_untouched_verified":True,
        "private_target_review_sha256":hashlib.sha256(canonical({
            "view_id":rid,"professional_id":pid,"user_id":uid})).hexdigest(),
        "private_original_state_sha256_audit_only":hashlib.sha256(canonical(initial)).hexdigest(),
        "private_final_state_sha256_audit_only":hashlib.sha256(canonical(final)).hexdigest(),
        "original_private_check_text_exposed":False,
        "changed_original_checker_or_source":False,
        "versioned_new_checker_not_attributed_to_original":True,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("private_spec")
    args=p.parse_args()
    os.environ.clear()
    spec=json.loads(Path(args.private_spec).read_text(encoding="utf-8"))
    data=sys.stdin.buffer.readline(MAX_INPUT+1)
    require(0<len(data)<=MAX_INPUT,"missing or oversized private state bridge")
    receipt=json.loads(data)
    print(json.dumps(evaluate(spec,receipt),sort_keys=True),flush=True)
if __name__=="__main__":
    main()
