#!/usr/bin/env python3
"""Q false-proof atlas: synthetic hostile fixtures; not native-source evidence."""
from __future__ import annotations
import collections,copy,json,random,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005q_active_train import (
    TwoStageActor,ValueTable,OPTIONS,POST_OPTIONS,MODES,RULES,
    TRAIN_EPISODES,UNKNOWN_FORCED_PROBES,schedule,
    baseline_choices,eval_baseline_after,check_frozen_task_manifest)
from owi_ec005q_source_active_episode import (
    CONTRACT as EP_CONTRACT,PRICE_PER_CALL,PRICE_FOR_PROBE)
from owi_ec005q_active_gate import check_receipt

TARGET={"banned_reject":("banned","rejected",3),
        "eligible_approve":("active","approved",2)}

def synthetic_receipt(rule,stage,first,post=None,mode="true"):
    standing,correct,passed_correct=TARGET[rule]
    probed=first=="probe"
    if probed and post is None:post="stop"
    effective=post if probed else first
    final=(correct if stage=="resolved" and effective=="stop" else
           "pending" if effective=="stop" else effective)
    bucket=("correct" if final==correct else "unchanged_pending"
            if final=="pending" else "prohibited")
    n=passed_correct if bucket=="correct" else 1
    base={"correct":1,"unchanged_pending":0,"prohibited":-1}[bucket]
    reward=round(base+0.1*n/9,6)
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
    feature=("unknown" if stage=="unknown" else
             "certified_"+standing if stage=="certified" else
             "already_resolved")
    supplied=(standing if mode=="true" else
              "blind" if mode=="zero_probe_signal" else "active")
    return {
        "contract":EP_CONTRACT,"original_source_train_row":710,
        "original_full_corpus_sha256":
            "3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a",
        "original_class_sha256":
            "ddfa0ad145cc43f1ab82545912b9e80410c5793b585d31d714f92c07b626dfba",
        "separate_corrected_v1_spec_sha256":
            "63252f02eb28cef71b2af7c7ce77afdab2123dc44112598b5b56a25551cd3a7a",
        "public_versioned_task_is_not_original_source_public_task":True,
        "task_kind_evaluator_audit_only":rule,
        "source_trusted_original_author_standing_evaluator_only":standing,
        "versioned_public_stage":stage,
        "versioned_public_initial_feature":feature,
        "source_original_initial_pending":True,
        "fixture_precorrected_source_review_only":stage=="resolved",
        "initial_selected_action":first,
        "initial_selected_action_propensity":1.0,
        "physical_optional_probe_executed":probed,
        "actual_selected_original_public_probe_status_evaluator_only":
            standing if probed else None,
        "policy_supplied_postprobe_signal":supplied if probed else None,
        "postprobe_selected_action":post if probed else None,
        "postprobe_selected_propensity":1.0 if probed else None,
        "randomized_probe_reply_ablation":
            probed and mode=="randomized_probe_signal",
        "effective_selected_terminal_action":effective,
        "source_public_final_review_status":final,
        "original_native_checker_reward_audit_only":round(n/9,4),
        "original_native_checks_passed_audit_only":n,
        "corrected_private_terminal_class_audit_only":bucket,
        "actual_selected_versioned_terminal_reward":reward,
        "actual_selected_versioned_utility":round(
            reward-PRICE_PER_CALL*len(phases)-
            (PRICE_FOR_PROBE if probed else 0.),6),
        "original_source_actual_calls":len(phases),
        "original_source_actual_public_tool_trace":[
            {"phase":p,"tool":t,"real_public_reply_sha256":"a"*64,
             "actual_tool_seconds":.001} for p,t in phases],
        "source_worker_wall_seconds":.3,
        "original_native_checker_wall_seconds":.02,
        "separate_corrected_checker_wall_seconds":.02,
        "source_worker_peak_rss_kib":20000,
        "original_checker_exact_input_timeout_replays":0,
        "corrected_checker_exact_input_timeout_replays":0,
        "original_checker_total_wall_seconds_with_retries":.023,
        "corrected_checker_total_wall_seconds_with_retries":.023,
        "privileged_task_identity_or_source_state_in_actor":False,
        "unselected_counterfactual_terminal_outcome_in_actor":False,
        "original_source_code_or_original_or_corrected_checker_in_actor":False,
    }

class ActiveProbeFalseProofTests(unittest.TestCase):
    def test_exact_masked_task_spec_and_mutant_rejection(self):
        path=Path(__file__).resolve().parents[1]/(
            "governance/research/OWI_EC005Q_ACTIVE_OBSERVATION_V1.json")
        self.assertEqual(len(check_frozen_task_manifest(path)),64)
        original=json.loads(path.read_text())
        for label,change in [
            ("source_edit",lambda d:d["source"].__setitem__(
                "source_class_sha256","f"*64)),
            ("scorer_switch",lambda d:d["separate_corrected_terminal_spec"].__setitem__(
                "sha256","f"*64)),
            ("disable_zero_ablation",lambda d:d["training"].__setitem__(
                "modes",["true"])),
            ("disable_probe_force",lambda d:d["training"]["forced_support"].__setitem__(
                "uncertain_first_probe_visits",0)),
            ("hide_strong_script",lambda d:d["evaluation"].__setitem__(
                "policies",["true"])),
        ]:
            with self.subTest(label=label):
                modified=copy.deepcopy(original);change(modified)
                with tempfile.TemporaryDirectory() as folder:
                    p=Path(folder)/"mutant.json"
                    p.write_text(json.dumps(modified))
                    with self.assertRaises(ValueError):
                        check_frozen_task_manifest(p)
    def test_balanced_original_train_task_rule_schedule(self):
        self.assertEqual(len(MODES),3)
        for seed in (11,23,37,41,53):
            s=schedule(seed)
            self.assertEqual(len(s),TRAIN_EPISODES)
            c=collections.Counter(s)
            for stage in ("unknown","certified","resolved"):
                for rule in RULES:
                    self.assertEqual(c[stage,rule],16)
            first_forced=[r for st,r in s if st=="unknown"][:UNKNOWN_FORCED_PROBES]
            self.assertEqual(first_forced.count("banned_reject"),UNKNOWN_FORCED_PROBES//2)
            self.assertEqual(first_forced.count("eligible_approve"),UNKNOWN_FORCED_PROBES//2)
    def test_learned_context_action_after_actual_chosen_scalar(self):
        a=TwoStageActor()
        rng=random.Random(4)
        for n in range(UNKNOWN_FORCED_PROBES):
            action,propensity=a.initial_choice("unknown",rng)
            self.assertEqual(action,"probe")
            self.assertEqual(propensity,1.)
            chosen=a.post_choice("banned",rng)
            self.assertIn(chosen[0],POST_OPTIONS)
            self.assertGreater(chosen[1],0)
            ep=synthetic_receipt("banned_reject","unknown","probe",chosen[0])
            a.update_from_chosen_only(ep)
        self.assertEqual(a.initial.count["unknown"][OPTIONS.index("probe")],24)
        self.assertEqual(a.unknown_seen,24)
        with self.assertRaises(ValueError):
            a.initial_choice("private_target_name",rng)
        with self.assertRaises(ValueError):
            a.post_choice("source_private_checker",rng)
    def test_physically_selected_probe_and_terminal_numerator(self):
        for stage in ("unknown","certified","resolved"):
            for rule in RULES:
                for first in OPTIONS:
                    for post in ("stop","approved","rejected") if first=="probe" else (None,):
                        for mode in MODES:
                            with self.subTest(stage=stage,rule=rule,first=first,
                                              post=post,mode=mode):
                                e=synthetic_receipt(rule,stage,first,post,mode)
                                expected=check_receipt(e,stage,rule,mode)
                                self.assertEqual(expected,
                                                 e["actual_selected_versioned_utility"])
    def test_reject_false_probe_and_privileged_leak(self):
        src=synthetic_receipt("banned_reject","unknown","probe","rejected")
        hostile=[
            ("fake_unexecuted_probe",lambda z:z.__setitem__(
                "physical_optional_probe_executed",False)),
            ("fake_public_source_probe_response",lambda z:z.__setitem__(
                "actual_selected_original_public_probe_status_evaluator_only","active")),
            ("wrong_probe_signal",lambda z:z.__setitem__(
                "policy_supplied_postprobe_signal","active")),
            ("modified_original_reward",lambda z:z.__setitem__(
                "original_native_checker_reward_audit_only",.9999)),
            ("score_reweight",lambda z:z.__setitem__(
                "actual_selected_versioned_terminal_reward",.2)),
            ("leaked_task",lambda z:z.__setitem__(
                "privileged_task_identity_or_source_state_in_actor",True)),
            ("probe_no_source_call",lambda z:z["original_source_actual_public_tool_trace"].pop(3)),
            ("changed_checker_spec",lambda z:z.__setitem__(
                "separate_corrected_v1_spec_sha256","f"*64)),
            ("faked_final_wrong",lambda z:z.__setitem__(
                "source_public_final_review_status","approved")),
            ("missing_RSS",lambda z:z.__setitem__(
                "source_worker_peak_rss_kib",0)),
            ("corrected_score_from_unselected",lambda z:z.__setitem__(
                "unselected_counterfactual_terminal_outcome_in_actor",True)),
            ("wrong_provenance",lambda z:z.__setitem__(
                "public_versioned_task_is_not_original_source_public_task",False)),
            ("fabricated_free_probe",lambda z:z.__setitem__(
                "actual_selected_versioned_utility",1.033333)),
            ("fabricated_free_timeout_replay",lambda z:z.__setitem__(
                "corrected_checker_exact_input_timeout_replays",1)),
            ("unbounded_timeout_replay",lambda z:z.__setitem__(
                "original_checker_exact_input_timeout_replays",5)),
            ("checker_total_wall_negative",lambda z:z.__setitem__(
                "corrected_checker_total_wall_seconds_with_retries",-.1)),
        ]
        for name,mutate in hostile:
            with self.subTest(name=name):
                x=copy.deepcopy(src)
                mutate(x)
                with self.assertRaises(ValueError):
                    check_receipt(x,"unknown","banned_reject","true")
    def test_strong_public_adaptive_baseline_and_stop(self):
        self.assertEqual(baseline_choices("scripted_adaptive","unknown"),("probe",1.))
        self.assertEqual(baseline_choices("scripted_adaptive","certified_active"),
                         ("approved",1.))
        self.assertEqual(baseline_choices("scripted_adaptive","certified_banned"),
                         ("rejected",1.))
        self.assertEqual(baseline_choices("scripted_adaptive","already_resolved"),
                         ("stop",1.))
        self.assertEqual(eval_baseline_after(
            "scripted_adaptive","unknown","banned"),("rejected",1.))
        self.assertEqual(eval_baseline_after(
            "always_probe_correct","already_resolved","active"),("stop",1.))
        with self.assertRaises(ValueError):
            eval_baseline_after("scripted_adaptive","unknown","invented")
if __name__=="__main__":
    unittest.main()
