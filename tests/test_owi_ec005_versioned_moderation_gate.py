#!/usr/bin/env python3
"""Exact receipt gate synthetic hostile vectors; not empirical source evidence."""
import copy,hashlib,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"experiments"))
sys.path.insert(0,str(ROOT/"tests"))
from test_owi_ec005_realtools_native_professional_gate import scenario
from owi_ec005_versioned_moderation_gate import adjudicate
from owi_ec005_versioned_moderation_paired import (
    CONTRACT,REVISED_CONTRACT,CLASS_SHA,TARGETS)
from owi_ec005_versioned_moderation_checker import CONTRACT as CHECKER_CONTRACT

SPEC=json.loads((ROOT/"governance/research/OWI_EC005O_REVISED_MODERATION_V1.json").read_text())
def paired():
    r=scenario()
    r["contract"]=CONTRACT
    r["source_class_sha256"]=CLASS_SHA
    r["original_native_and_corrected_checkers_separate"]=True
    r["versioned_corrected_contract"]=REVISED_CONTRACT
    r["frozen_benchmark_spec_sha256"]=hashlib.sha256((
        json.dumps(SPEC,sort_keys=True,indent=2)+"\n").encode()).hexdigest()
    for x in r["selected_executions"]:
        t=TARGETS[x["target_rule"]]
        state_class=("correct" if x["public_final_status"]==t["correct"] else
                     "prohibited" if x["public_final_status"]==t["wrong"] else
                     "unchanged_pending")
        x.update({
            "original_native_and_corrected_private_checkers_separate":True,
            "versioned_corrected_terminal_contract":CHECKER_CONTRACT,
            "versioned_corrected_reward":round({
                "correct":1.0,"unchanged_pending":0.0,"prohibited":-1.0}[state_class]+
                .1*x["original_native_checks_passed"]/9,6),
            "versioned_terminal_state_class":state_class,
            "original_private_state_source_sha256":"1"*64,
            "private_terminal_state_sha256":"2"*64,
            "corrected_private_target_digest":"3"*64,
            "corrected_private_non_target_untouched":True,
            "corrected_private_author_professional_verified":True,
            "corrected_verifier_container_seconds":.01,
        })
    return r

class PairedEvidenceGate(unittest.TestCase):
    def test_synthetic_positive_ordering_separate_not_source_proof(self):
        r=adjudicate(paired(),SPEC)
        self.assertEqual(r["actual_original_source_episodes"],20)
        self.assertEqual(r["separate_original_private_checker_runs"],20)
        self.assertEqual(r["separate_versioned_corrected_private_checker_runs"],20)
        self.assertTrue(r["original_native_no_harm_penalty_negative_control_reproduced"])
        self.assertTrue(r["corrected_wrong_below_stop_for_both_public_task_rules"])
        self.assertFalse(r["five_seed_outcome_only_learning_and_heldout_transfer_established"])
    def test_independent_gate_denies_forged_evidence(self):
        edits=[
            ("old-source",lambda x:x.__setitem__("source_class_sha256","a"*64)),
            ("old-scorer",lambda x:x["selected_executions"][0].__setitem__(
                "original_native_reward",.9)),
            ("wrong-review",lambda x:x["selected_executions"][1].__setitem__(
                "original_public_target_sha256","a"*64)),
            ("forged-revised-score",lambda x:x["selected_executions"][0].__setitem__(
                "versioned_corrected_reward",-1.0)),
            ("forged-class",lambda x:x["selected_executions"][0].__setitem__(
                "versioned_terminal_state_class","prohibited")),
            ("missing-private-checker",lambda x:x["selected_executions"][0].__setitem__(
                "original_native_and_corrected_private_checkers_separate",False)),
            ("missing-source-private-readback",lambda x:x["selected_executions"][0].__setitem__(
                "corrected_private_non_target_untouched",False)),
            ("mismatched-original-start-state",lambda x:x["selected_executions"][0].__setitem__(
                "original_private_state_source_sha256","f"*64)),
            ("missing-episode",lambda x:x["selected_executions"].pop()),
            ("positive-original-negative-control",lambda x:x["selected_executions"][0].__setitem__(
                "original_native_checks_passed",9)),
            ("not-frozen-spec",lambda x:x.__setitem__(
                "frozen_benchmark_spec_sha256","f"*64)),
        ]
        for name,edit in edits:
            with self.subTest(name=name):
                d=paired();edit(d)
                with self.assertRaises(ValueError):
                    adjudicate(d,SPEC)
    def test_real_frozen_bytes_not_reserialized_keys(self):
        # Regression for an actual source replay failure: JavaScript-style
        # repository JSON key order differs from Python sorted JSON reemit.
        raw=(ROOT/"governance/research/OWI_EC005O_REVISED_MODERATION_V1.json").read_bytes()
        report=paired()
        report["frozen_benchmark_spec_sha256"]=hashlib.sha256(raw).hexdigest()
        self.assertEqual(
            adjudicate(report,SPEC,spec_bytes=raw)["actual_original_source_episodes"],20)
        with self.assertRaises(ValueError):
            adjudicate(report,SPEC,spec_bytes=raw+b" ")
        with self.assertRaises(ValueError):
            adjudicate(report,SPEC,spec_bytes=b'{"contract":"tampered"}')

    def test_reject_revised_scoring_spec_change(self):
        d=copy.deepcopy(SPEC)
        d["scoring"]["native_task_completion_coefficient"]=1.0
        with self.assertRaises(ValueError):
            adjudicate(paired(),d)
if __name__=="__main__":
    unittest.main()
