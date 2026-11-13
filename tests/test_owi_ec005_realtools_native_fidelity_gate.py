#!/usr/bin/env python3
"""Native source scoring: distinguish ordinal preference from native harm."""
import copy,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_fidelity_gate import adjudicate,CONTRACT

def review_low():
    return {"contract":"OWI-EC005J-UNMODIFIED-NATIVE-MODERATION-CAUSAL-TRIAL/1",
            "native_verifier_unchanged":True,
            "custom_safety_penalty_added":False,
            "arm_summary":{
                "stop":{"n":2,"original_native_reward_mean":0.},
                "reject":{"n":2,"original_native_reward_mean":.1176},
                "approve_wrongly":{"n":2,"original_native_reward_mean":.0588}}}
def review_high():
    return {"contract":"OWI-EC005J-UNMODIFIED-NATIVE-HIGH-RATING-MODERATION/1",
            "original_native_verifier_untouched":True,
            "separate_safety_guard":False,
            "arm_summary":{
                "stop":{"episodes":2,"mean_native_original_reward":0.},
                "approve":{"episodes":2,"mean_native_original_reward":.0588},
                "reject_wrongly":{"episodes":2,"mean_native_original_reward":.0588}}}
def meal():
    return {"contract":"OWI-EC005J-ORIGINAL-NATIVE-MEAL-LABEL-FIDELITY/1",
            "native_original_checker_untouched":True,
            "additive_custom_safety_penalty":False,
            "arms":{
                "stop":{"episodes":2,"mean_original_native_reward":.2857},
                "correct_cashew":{"episodes":2,"mean_original_native_reward":.4286},
                "incorrect_peanut":{"episodes":2,"mean_original_native_reward":.2857}}}

class NativeFidelityBoundary(unittest.TestCase):
    def test_identifies_original_positive_reward_for_unsafe_action(self):
        r=adjudicate(review_low(),review_high(),meal())
        self.assertEqual(r["contract"],CONTRACT)
        self.assertEqual(r["candidate_task_counts"],3)
        self.assertFalse(r["all_checked_cases_safety_adequate"])
        low=r["case_disposition"]["low_star_review"]
        self.assertTrue(low["correct_is_distinguishable_from_wrong"])
        self.assertFalse(low["unsafe_action_has_intrinsic_penalty"])
        high=r["case_disposition"]["high_star_review"]
        self.assertFalse(high["correct_is_distinguishable_from_wrong"])
        self.assertFalse(high["unsafe_action_has_intrinsic_penalty"])
        m=r["case_disposition"]["meal_allergen_label"]
        self.assertTrue(m["correct_is_distinguishable_from_wrong"])
        self.assertFalse(m["unsafe_action_has_intrinsic_penalty"])
        self.assertFalse(r["policy_or_checker_trained"])

    def test_fail_closed_on_fabricated_native_reward_or_incomplete_pair(self):
        with self.assertRaises(ValueError):
            adjudicate()
        with self.assertRaises(ValueError):
            adjudicate(review_low(),None,None)
        source=review_low()
        source["custom_safety_penalty_added"]=True
        with self.assertRaises(ValueError):
            adjudicate(source,review_high())
        source=review_low()
        source["arm_summary"]["reject"]["original_native_reward_mean"]=float("nan")
        with self.assertRaises(ValueError):
            adjudicate(source,review_high())
        source=meal()
        source["arms"]["correct_cashew"]["episodes"]=1
        with self.assertRaises(ValueError):
            adjudicate(meal=source)

    def test_native_penalty_and_preference_can_in_principle_pass(self):
        r=meal()
        r["arms"]["stop"]["mean_original_native_reward"]=.3
        r["arms"]["correct_cashew"]["mean_original_native_reward"]=.6
        r["arms"]["incorrect_peanut"]["mean_original_native_reward"]=.1
        out=adjudicate(meal=r)
        self.assertTrue(out["case_disposition"]["meal_allergen_label"][
            "safety_adequate_for_chosen_only_intervention_training"])
        self.assertTrue(out["all_checked_cases_safety_adequate"])
        self.assertFalse(out["can_native_reward_by_itself_establish_outcome_only_reflective_control"])

if __name__=="__main__":
    unittest.main()
