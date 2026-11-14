#!/usr/bin/env python3
"""OWI-EC005P unit and hostile vectors; never pretend fixtures are source runs."""
from __future__ import annotations
import copy,random,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005p_real_source_policy import (
    public_context,public_correct_status,OPTIONS)
from owi_ec005p_chosen_outcome_train import (
    OnPolicyBandit,feature_for,utility,limited_receipt,
    sample_train_schedule,TRAIN_EPISODES,MODES,SEEDS)
from owi_ec005p_chosen_outcome_gate import (
    check_terminal,check_training_episode,check_evaluation,expected_class)

def trace(n):
    names=["list_all_professionals","list_all_users",
           "get_reviews_for_professional","get_reviews_for_professional"]
    if n==5:
        names+=["get_reviews_for_professional"]
    elif n==6:
        names+=["change_review_moderation_status","get_reviews_for_professional"]
    elif n in (7,8):
        names+=["change_review_moderation_status",
                "get_reviews_for_professional"]
        if n==8:names.append("change_review_moderation_status")
        names.append("get_reviews_for_professional")
    return [{"tool":name,"public_reply_sha256":"a"*64,
             "source_tool_seconds":.00001} for name in names]

def trainrow(action="rejected",rule="banned_reject"):
    n=3 if action=="rejected" else 1
    base=1 if action=="rejected" else 0 if action=="stop" else -1
    reward=round(base+.1*n/9,6)
    calls=5 if action=="stop" else 6
    utility=round(reward-.002*calls,6)
    return {
        "episode_index":0,
        "train_rule_audit_only":rule,
        "feature_actually_supplied_to_policy":"banned:pending",
        "source_selected_action":action,
        "source_selected_propensity":1.0,
        "chosen_actual_corrected_terminal_reward":reward,
        "chosen_actual_original_native_reward_audit_only":round(n/9,4),
        "chosen_actual_utility":utility,
        "assigned_scalar_to_policy_update":utility,
        "assigned_scalar_origin_episode":0,
        "actual_source_tool_calls":calls,
        "source_worker_wall_seconds":1.,
        "original_native_checker_wall_seconds":.05,
        "versioned_private_checker_wall_seconds":.05,
        "peak_source_worker_rss_kib":20000,
        "real_source_selected_public_receipts":trace(calls),
        "private_state_or_checker_in_actor":False,
        "unchosen_counterfactual_outcome_in_update":False,
    }
def evalrow(action="rejected",rule="banned_reject",model="public_rule_correct"):
    n=3 if action=="rejected" else 1
    base=1 if action=="rejected" else 0 if action=="stop" else -1
    reward=round(base+.1*n/9,6)
    calls=5 if action=="stop" else 6
    return {
        "evaluation_stage":"initial_pending",
        "source_public_rule_audit_only":rule,
        "model":model,
        "selected_option":action,
        "policy_feature":"banned:pending",
        "real_corrected_reward":reward,
        "real_original_native_reward":round(n/9,4),
        "real_terminal_class":"correct" if action=="rejected" else
            "unchanged_pending" if action=="stop" else "prohibited",
        "realized_utility":round(reward-.002*calls,6),
        "real_public_tool_calls":calls,
        "actual_worker_wall_seconds":1.0,
        "actual_original_checker_wall_seconds":.05,
        "actual_corrected_checker_wall_seconds":.05,
        "worker_peak_rss_kib":20000,
        "actual_public_selected_call_hashes":trace(calls),
        "learned_policy_updated_during_evaluation":False,
    }

class ChosenOutcomeTests(unittest.TestCase):
    def test_only_actual_source_public_features(self):
        self.assertEqual(public_context("active","pending"),"active:pending")
        self.assertEqual(public_correct_status("banned"),"rejected")
        self.assertEqual(public_correct_status("active"),"approved")
        for x in ("inactive","unknown"):
            with self.assertRaises(ValueError):
                public_context(x,"pending")
        self.assertEqual(feature_for("banned:pending","zero_information"),"blind")
        self.assertEqual(feature_for("active:pending","true"),"active:pending")
        for bad in ("other","task_710","oracle_correct"):
            with self.assertRaises(ValueError):
                feature_for(bad,"true")
    def test_empirical_agent_chosen_only_rewards_and_forced_exploration(self):
        rng=random.Random(11)
        a=OnPolicyBandit()
        selected=[]
        for _ in range(6):
            action,p,key=a.sample("banned:pending",rng)
            self.assertGreater(p,0)
            self.assertLessEqual(p,1)
            self.assertIn(action,OPTIONS)
            a.update(key,action,1.0 if action=="rejected" else -1.)
            selected.append(action)
        self.assertEqual(set(selected),set(OPTIONS))
        self.assertTrue(all(v==2 for v in a.counts["banned:pending"]))
        self.assertEqual(a.best("banned:pending"),OPTIONS.index("rejected"))
        with self.assertRaises(ValueError):
            a.update("banned:pending","approved",float("nan"))
    def test_five_seed_frozen_balanced_source_schedule(self):
        self.assertEqual(len(SEEDS),5)
        self.assertEqual(len(MODES),3)
        for seed in SEEDS:
            tasks=sample_train_schedule(seed)
            self.assertEqual(len(tasks),TRAIN_EPISODES)
            self.assertEqual(tasks.count("banned_reject"),TRAIN_EPISODES//2)
            self.assertEqual(tasks.count("eligible_approve"),TRAIN_EPISODES//2)
    def test_native_original_and_repaired_score_strict_not_confused(self):
        self.assertEqual(expected_class("banned_reject","rejected",
                                        "initial_pending"),"correct")
        self.assertEqual(expected_class("banned_reject","approved",
                                        "initial_pending"),"prohibited")
        self.assertEqual(expected_class("banned_reject","stop",
                                        "heldout_postcorrect"),"correct")
        self.assertEqual(check_terminal("banned_reject","approved",
                                        "initial_pending",-.988889,.1111),"prohibited")
        for wrong in (0.011111,1.033333):
            with self.assertRaises(ValueError):
                check_terminal("banned_reject","approved","initial_pending",
                               wrong,.1111)
    def test_private_payload_and_traces_not_accepted_in_policy_receipt(self):
        r=trainrow()
        self.assertGreaterEqual(check_training_episode("true",r,0,{}),0)
        for field,val in [
            ("private_state_or_checker_in_actor",True),
            ("unchosen_counterfactual_outcome_in_update",True),
            ("chosen_actual_corrected_terminal_reward",3.0),
            ("source_selected_propensity",0.0),
            ("actual_source_tool_calls",4),
            ("real_source_selected_public_receipts",[]),
            ("assigned_scalar_to_policy_update",1.333),
            ("peak_source_worker_rss_kib",0),
        ]:
            x=copy.deepcopy(r)
            x[field]=val
            with self.subTest(field=field),self.assertRaises(ValueError):
                check_training_episode("true",x,0,{})
        x=copy.deepcopy(r)
        x["feature_actually_supplied_to_policy"]="banned:pending"
        with self.assertRaises(ValueError):
            check_training_episode("zero_information",x,0,{})
        x=copy.deepcopy(r)
        x["assigned_scalar_origin_episode"]=0
        x["episode_index"]=1
        with self.assertRaises(ValueError):
            check_training_episode("shuffled_chosen_outcome_credit",x,1,{0:-1.})
    def test_prospective_source_baseline_requires_actual_correct_action(self):
        r=evalrow()
        check_evaluation(r)
        for field,val in [
            ("realized_utility",999),
            ("real_terminal_class","prohibited"),
            ("selected_option","approved"),
            ("real_public_tool_calls",8),
            ("policy_feature","blind"),
            ("learned_policy_updated_during_evaluation",True),
        ]:
            x=copy.deepcopy(r);x[field]=val
            with self.subTest(field=field),self.assertRaises(ValueError):
                check_evaluation(x)

if __name__=="__main__":
    unittest.main()
