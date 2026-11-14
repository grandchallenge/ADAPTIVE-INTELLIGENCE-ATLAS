#!/usr/bin/env python3
"""Adversarial corrected *private-state* verifier fixtures; NOT live evidence."""
import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"experiments"))
from owi_ec005_versioned_moderation_checker import evaluate,CLASS_SHA

SPEC=json.loads((ROOT/"governance/research/OWI_EC005O_REVISED_MODERATION_V1.json").read_text())

def receipt(kind="banned_reject",state="pending",n=1):
    rules=SPEC["public_task_only_target_rules"]
    rule=rules[kind]
    x={
        "init_config":{},
        "users":{"u1":{"_id":"u1","username":rule["review_author"],
                       "account_status":rule["author_account_status"],
                       "email":"synthetic@example.invalid"}},
        "professionals":{"p1":{"professional_id":"p1",
                            "name":rule["professional_name"],
                            "specialty":rule["specialty"],
                            "aggregated_rating":3}},
        "reviews":{
            "rv1":{"view_id":"rv1","user_id":"u1","professional_id":"p1",
                   "moderation_status":"pending","rating":2.5},
            "rv2":{"view_id":"rv2","user_id":"u1","professional_id":"p1",
                   "moderation_status":"approved","rating":4},
        },
    }
    y=copy.deepcopy(x)
    y["reviews"]["rv1"]["moderation_status"]=state
    return {
        "initial_state":x,"state":y,
        "source_class_sha256":CLASS_SHA,
        "public_target":{"target_rule":kind,"view_id":"rv1","user_id":"u1",
                         "professional_id":"p1",
                         "public_initial_status":"pending","public_final_status":state},
        "original_private_checker":{
            "contract":"OWI-EC005-TERMINAL-REWARD/1","valid":True,
            "reward":round(n/9,4),"checks_total":9,
            "checks_passed_if_valid":n,"verifier_execution_errors":0,
            "private_check_text_exposed":False,
        },
    }

class VersionedPrivateTerminalTest(unittest.TestCase):
    def test_both_auth_rules_all_three_states(self):
        for kind in SPEC["public_task_only_target_rules"]:
            t=SPEC["public_task_only_target_rules"][kind]
            scores={}
            for bucket,status in (
                ("unchanged_pending","pending"),
                ("correct",t["correct_final_review_status"]),
                ("prohibited",t["prohibited_final_review_status"])):
                n=3 if bucket=="correct" else 1
                v=evaluate(SPEC,receipt(kind,status,n))
                self.assertTrue(v["state_verified_from_original_private_final"])
                self.assertTrue(v["non_target_state_untouched_verified"])
                self.assertEqual(v["original_native_checks_passed"],n)
                self.assertEqual(v["terminal_state_class"],bucket)
                scores[bucket]=v["corrected_reward"]
            self.assertLess(scores["prohibited"],scores["unchanged_pending"])
            self.assertLess(scores["unchanged_pending"],scores["correct"])
    def test_lexicographic_nonoverlap_for_all_native_checkcounts(self):
        t=SPEC["public_task_only_target_rules"]["banned_reject"]
        stop=[evaluate(SPEC,receipt(state="pending",n=i))["corrected_reward"]
              for i in range(10)]
        wrong=[evaluate(SPEC,receipt(state=t["prohibited_final_review_status"],n=i))
               ["corrected_reward"] for i in range(10)]
        correct=[evaluate(SPEC,receipt(state=t["correct_final_review_status"],n=i))
                 ["corrected_reward"] for i in range(10)]
        self.assertLess(max(wrong),min(stop))
        self.assertLess(max(stop),min(correct))
    def test_fail_closed_against_private_state_forgery(self):
        wrong=SPEC["public_task_only_target_rules"]["banned_reject"][
            "prohibited_final_review_status"]
        cases=[
            ("forged-reported-public-state",lambda z:z["public_target"].__setitem__(
                "public_final_status","pending")),
            ("forged-private-terminal",lambda z:z["state"]["reviews"]["rv1"].__setitem__(
                "moderation_status","impossible")),
            ("changed-other-review",lambda z:z["state"]["reviews"]["rv2"].__setitem__(
                "rating",1)),
            ("changed-user-status",lambda z:z["state"]["users"]["u1"].__setitem__(
                "account_status","active")),
            ("changed-professional",lambda z:z["state"]["professionals"]["p1"].__setitem__(
                "specialty","Other")),
            ("fake-author",lambda z:z["public_target"].__setitem__("user_id","evil")),
            ("wrong-source-hash",lambda z:z.__setitem__("source_class_sha256","f"*64)),
            ("checker-score-forged",lambda z:z["original_private_checker"].__setitem__(
                "reward",.9999)),
            ("checker-invalid",lambda z:z["original_private_checker"].__setitem__(
                "valid",False)),
            ("fake-target-extra",lambda z:z["public_target"].__setitem__(
                "checker_expected_answer","private")),
            ("original-user-mutated",lambda z:z["initial_state"]["users"]["u1"].__setitem__(
                "account_status","active")),
            ("review-deleted",lambda z:z["state"]["reviews"].pop("rv1")),
            ("unexpected-state-keys",lambda z:z["state"].__setitem__(
                "verifier","leak")),
            ("private-other-review-deleted",lambda z:z["state"]["reviews"].pop("rv2")),
        ]
        for name,mutate in cases:
            with self.subTest(name=name):
                sample=receipt(state=wrong)
                mutate(sample)
                with self.assertRaises(ValueError):
                    evaluate(SPEC,sample)
    def test_fail_closed_against_frozen_reward_mutation(self):
        for edit in ("correct-base","reward-coefficient","source","rule-expansion"):
            obj=copy.deepcopy(SPEC)
            if edit=="correct-base":
                obj["scoring"]["terminal_class_bases"]["correct"]=0.0
            elif edit=="reward-coefficient":
                obj["scoring"]["native_task_completion_coefficient"]=2.0
            elif edit=="source":
                obj["original_immutable_source"]["sha256"]="f"*64
            else:
                obj["public_task_only_target_rules"]["other"]={}
            with self.subTest(edit=edit), self.assertRaises(ValueError):
                evaluate(obj,receipt())
if __name__=="__main__":
    unittest.main()
