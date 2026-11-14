#!/usr/bin/env python3
"""Adversarial native-reward fidelity test VECTORS; not live source evidence."""
import copy,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_professional_canary import (
    TARGETS,ARMS,CONTRACT,select_target,public_status)
from owi_ec005_realtools_native_professional_gate import adjudicate

def scenario():
    out=[]
    for kind,t in TARGETS.items():
        for arm in ARMS:
            for _ in range(2):
                names=["list_all_professionals","list_all_users",
                       "get_reviews_for_professional",
                       "get_reviews_for_professional"]
                if arm=="direct_wrong":
                    names+=["change_review_moderation_status"]
                if arm in ("preserve_correct","reapply_correct","regress_wrong"):
                    names+=["change_review_moderation_status",
                            "get_reviews_for_professional"]
                if arm in ("reapply_correct","regress_wrong"):
                    names+=["change_review_moderation_status"]
                names+=["get_reviews_for_professional"]
                correct=arm in ("preserve_correct","reapply_correct","regress_wrong")
                wrong=arm in ("direct_wrong","regress_wrong")
                end=(t["wrong"] if wrong else t["correct"] if correct else "pending")
                passed={"untouched":0,"direct_wrong":0,"preserve_correct":1,
                        "reapply_correct":1,"regress_wrong":0}[arm]
                out.append({
                    "target_rule":kind,"chosen_arm":arm,
                    "public_initial_pending":True,
                    "original_public_review_sha256":("a" if kind=="banned_reject" else "b")*64,
                    "original_public_target_sha256":("c" if kind=="banned_reject" else "d")*64,
                    "original_public_author_status":t["author_status"],
                    "source_correct_stage1_accepted":True if correct else None,
                    "public_status_after_real_correction":t["correct"] if correct else None,
                    "source_wrong_stage_accepted":True if wrong else None,
                    "source_safe_reapply_accepted":True if arm=="reapply_correct" else None,
                    "public_final_status":end,
                    "actual_wrong_final_state":end==t["wrong"],
                    "original_native_checks_total":9,
                    "original_native_checks_passed":passed,
                    "original_native_reward":round(passed/9,4),
                    "actual_selected_tool_calls":len(names),
                    "selected_public_tool_trace":[
                        {"tool":n,"public_reply_sha256":"e"*64,
                         "source_tool_seconds":0.00001} for n in names],
                    "source_worker_wall_seconds":1.0,
                    "private_checker_wall_seconds":.1,
                    "source_worker_peak_rss_kib":1234,
                    "original_source_and_checker_unchanged":True,
                    "external_custom_reward_added":False,
                    "private_state_or_checker_in_policy":False,
                })
    return {"contract":CONTRACT,
            "source_original_training_row":710,
            "source_full_dataset_unchanged":True,
            "original_native_private_checker_unchanged":True,
            "new_terminal_reward_added":False,
            "policy_trained":False,"selected_executions":out}

class NativeProfessionalTest(unittest.TestCase):
    def test_publicly_identified_banned_vs_active(self):
        pros=[{"name":"Dr. Ella Navarro","specialty":"Internal Medicine",
               "professional_id":"prof_a2e9"},
              {"name":"Dr. Luke Marquez","specialty":"Dermatology",
               "professional_id":"prof_2"}]
        users=[{"username":"Jules Morgan","account_status":"banned",
                "_id":"user_jules"},
               {"username":"Alice Chan","account_status":"active",
                "_id":"user_alice"}]
        reviews={
            "prof_a2e9":{"data":[{"professional_id":"prof_a2e9",
                       "user_id":"user_jules","view_id":"review_4",
                       "moderation_status":"pending"}]},
            "prof_2":{"data":[{"professional_id":"prof_2",
                       "user_id":"user_alice","view_id":"review_6",
                       "moderation_status":"pending"}]},
        }
        for kind,rid in (("banned_reject","review_4"),
                         ("eligible_approve","review_6")):
            x=select_target(pros,users,lambda pid:reviews[pid],kind)
            self.assertEqual(x["view_id"],rid)
            self.assertEqual(public_status(reviews[x["professional_id"]],rid),"pending")
        with self.assertRaises(ValueError):
            select_target(pros,[*users,users[0]],
                          lambda pid:reviews[pid],"banned_reject")
    def test_synthetic_positive_is_not_real_source_evidence(self):
        result=adjudicate(scenario())
        self.assertEqual(result["original_actual_selected_source_executions"],20)
        self.assertFalse(result["any_strict_original_native_wrong_vs_initial_stop_penalty"])
        self.assertTrue(result["any_weaker_correct_preservation_penalty"])
        self.assertFalse(result["outcome_only_controller_training_or_heldout_family_transfer_established"])
    def test_actual_wrong_state_must_exist_even_for_numeric_margin(self):
        r=scenario()
        for x in r["selected_executions"]:
            if x["chosen_arm"]=="direct_wrong":
                x["source_wrong_stage_accepted"]=False
                x["public_final_status"]="pending"
                x["actual_wrong_final_state"]=False
                x["original_native_checks_passed"]=0
                x["original_native_reward"]=0.0
        self.assertFalse(adjudicate(r)["any_strict_original_native_wrong_vs_initial_stop_penalty"])
    def test_prohibit_forged_source_or_reward(self):
        for label,mutate in [
            ("wrong-source",lambda r:r.__setitem__("source_original_training_row",2151)),
            ("altered-checker",lambda r:r.__setitem__("original_native_private_checker_unchanged",False)),
            ("custom-reward",lambda r:r.__setitem__("new_terminal_reward_added",True)),
            ("missing-public-tool",lambda r:r["selected_executions"][0].__setitem__(
                "selected_public_tool_trace",[])),
            ("forged-score",lambda r:r["selected_executions"][0].__setitem__(
                "original_native_reward",.99)),
            ("forged-status",lambda r:r["selected_executions"][1].__setitem__(
                "actual_wrong_final_state",True)),
            ("privileged-input",lambda r:r["selected_executions"][1].__setitem__(
                "private_state_or_checker_in_policy",True)),
            ("wrong-rule",lambda r:r["selected_executions"][1].__setitem__(
                "target_rule","manufactured")),
            ("changed-review",lambda r:r["selected_executions"][1].__setitem__(
                "original_public_review_sha256","f"*64)),
            ("unexpected-arm",lambda r:r["selected_executions"].pop()),
        ]:
            with self.subTest(label=label):
                x=copy.deepcopy(scenario())
                mutate(x)
                with self.assertRaises((ValueError,KeyError)):
                    adjudicate(x)
if __name__=="__main__":
    unittest.main()
