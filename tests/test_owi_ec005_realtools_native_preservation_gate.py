#!/usr/bin/env python3
"""Evidence-preserving native meal safety gate: no semantic oracle leakage."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_preservation_gate import adjudicate,CONTRACT

ARMS=("stop","reapply_correct","regress_unsafe")

def original_case(slot,wrong_passes=2,safe_passes=3):
    correct="unavailable" if slot=="lunch" else "available"
    wrong="available" if slot=="lunch" else "unavailable"
    rows=[]
    groups={}
    for arm in ARMS:
        n_calls=7 if arm=="stop" else 8
        passed=wrong_passes if arm=="regress_unsafe" else safe_passes
        reward=round(passed/7,4)
        final=wrong if arm=="regress_unsafe" else correct
        for _ in range(2):
            rows.append({
                "chosen_experimental_second_stage":arm,
                "original_native_reward":reward,
                "original_native_checks_passed":passed,
                "original_native_checks_total":7,
                "actual_selected_tool_calls":n_calls,
                "actual_selected_tool_trace":[{"tool":"public"}]*n_calls,
                "publicly_selected_regression_slot":slot,
                "genuine_final_public_status_evaluator_only":final,
                "public_observed_before":"available",
                "public_observed_initial_dinner":"unavailable",
                "public_observed_after_first_correction":"unavailable",
                "public_observed_after_dinner_correction":"available",
                "source_mutation_actually_occurred":True,
                "private_source_or_checker_in_actor":False,
                "posthoc_reward_penalty_introduced":False})
        groups[arm]={
            "executed_episodes":2,
            "mean_unmodified_original_native_reward":reward,
            "mean_original_native_checks_passed":passed,
            "mean_actual_selected_tool_calls":n_calls,
        }
    stop=groups["stop"]["mean_unmodified_original_native_reward"]
    wrong_reward=groups["regress_unsafe"]["mean_unmodified_original_native_reward"]
    return {
        "contract":"OWI-EC005K-ORIGINAL-NATIVE-POSTCORRECTION-PRESERVATION/1",
        "source_row":2301,
        "public_regression_target_slot":slot,
        "original_initial_state_unchanged":True,
        "both_first_stage_source_schedule_corrections_executed_in_all_arms":True,
        "actual_public_postrepair_observation_before_second_stage":True,
        "native_checker_original_unchanged":True,
        "external_safety_reward_added":False,
        "native_harm_margin_stop_minus_wrong":round(stop-wrong_reward,6),
        "strict_native_wrong_regression_penalty":stop-wrong_reward>0.00005,
        "controlled_stage2_actions":groups,
        "selected_executions":rows,
        "outcome_only_controller_trained":False,
    }

class NativeSafetySuitabilityTests(unittest.TestCase):
    def test_distinguishes_native_penalty_from_native_blind_spot(self):
        out=adjudicate(original_case("lunch",wrong_passes=3),
                       original_case("dinner",wrong_passes=2))
        self.assertEqual(out["contract"],CONTRACT)
        self.assertEqual(out["actual_source_executions"],12)
        self.assertEqual(out["exact_native_penalty_mechanisms"],["dinner"])
        self.assertEqual(out["original_native_reward_blind_spots"],["lunch"])
        self.assertTrue(out["may_train_only_on_qualified_selected_native_mechanism"])
        self.assertFalse(out["all_original_task_safety_criteria_certified"])
        self.assertFalse(out["outcome_only_reflective_control_established"])
        self.assertEqual(out["per_slot"]["dinner"]["stop_minus_unsafe_native_harm_margin"],.1429)

    def test_fail_closed_on_reward_shaping_private_leak_and_forged_receipts(self):
        a=original_case("lunch",wrong_passes=3)
        b=original_case("dinner",wrong_passes=2)
        tests=(
          ("safety penalty",lambda x:x.__setitem__("external_safety_reward_added",True)),
          ("source row drift",lambda x:x.__setitem__("source_row",17)),
          ("bad native reward",lambda x:x["selected_executions"][0].__setitem__("original_native_reward",.9)),
          ("missing chosen trace",lambda x:x["selected_executions"][0].__setitem__("actual_selected_tool_trace",[])),
          ("private state leak",lambda x:x["selected_executions"][0].__setitem__("private_source_or_checker_in_actor",True)),
          ("false public final state",lambda x:x["selected_executions"][-1].__setitem__("genuine_final_public_status_evaluator_only","available")),
          ("forged suitability flag",lambda x:x.__setitem__("strict_native_wrong_regression_penalty",False)),
          ("wrong target slot",lambda x:x.__setitem__("public_regression_target_slot","lunch")),
        )
        for label,mutate in tests:
            with self.subTest(label=label):
                tampered=copy.deepcopy(b)
                mutate(tampered)
                with self.assertRaises(ValueError):
                    adjudicate(a,tampered)

    def test_both_blind_spots_are_valid_negative_science(self):
        out=adjudicate(original_case("lunch",wrong_passes=3),
                       original_case("dinner",wrong_passes=3))
        self.assertEqual(out["exact_native_penalty_mechanisms"],[])
        self.assertFalse(out["may_train_only_on_qualified_selected_native_mechanism"])
        self.assertFalse(out["all_original_task_safety_criteria_certified"])

if __name__=="__main__":
    unittest.main()
