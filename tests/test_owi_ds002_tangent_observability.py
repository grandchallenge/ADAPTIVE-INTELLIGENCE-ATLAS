#!/usr/bin/env python3
"""Evaluator-only checkpoint/JVP mechanism diagnostics and access gates."""
import math
import sys
import unittest
from pathlib import Path
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments"))
from owi_ec004_core import Cfg, Core
from owi_ec005_conditional import make_batch
from owi_ds002_tangent_observability import mechanism_pair, run


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        torch.set_num_threads(1)

    def setUp(self):
        torch.manual_seed(16)
        self.core = Core(5).eval()
        self.cfg = Cfg(h=5, length=9, suffix=3, p_fault=1.)

    def test_matched_source_mechanisms_and_gated_queries(self):
        x, y, receipt = mechanism_pair(self.core, self.cfg, seed=817, n=48)
        self.assertEqual(x.shape[1], 6)
        self.assertEqual(len(x), len(y))
        self.assertTrue(bool((y == 0).any() and (y == 1).any()))
        self.assertEqual(receipt["gaussian"]["charged_jvp_queries"], 1)
        self.assertEqual(receipt["checkpoint"]["charged_jvp_queries"], 1)
        self.assertEqual(receipt["gaussian"]["charged_jvp_examples"], 48)
        self.assertEqual(receipt["checkpoint"]["charged_jvp_examples"], 48)
        self.assertTrue(bool(torch.isfinite(x).all()))

    def test_gaussian_raw_state_fault_does_not_corrupt_checkpoint(self):
        safe_cfg = Cfg(h=5, length=9, suffix=3, p_fault=0.)
        same_seed = 567
        safe = make_batch(self.core, safe_cfg,
                          torch.Generator().manual_seed(same_seed),
                          n=48, kind="gaussian")
        fault = make_batch(self.core, self.cfg,
                           torch.Generator().manual_seed(same_seed),
                           n=48, kind="gaussian")
        self.assertTrue(torch.equal(safe.x, fault.x))
        self.assertTrue(all(torch.equal(safe.checkpoints[i], fault.checkpoints[i])
                            for i in (0, 1)))
        self.assertTrue(bool((fault.fault_audit > 0).all()))

    def test_privileged_diagnostic_writes_no_policy_success_claim(self):
        output = run(seed=7, pretrain=2, train_n=32, eval_n=48)
        self.assertTrue(output["training_mechanism_labels_used"])
        self.assertTrue(output["not_outcome_only_policy_learning"])
        self.assertEqual(set(output["results"]), {
            "residual_only", "residual_plus_measured_jvp",
            "public_telemetry_plus_residual",
            "public_telemetry_residual_jvp"})
        self.assertTrue(all(math.isfinite(v["heldout_auc"])
                            for v in output["results"].values()))
        self.assertEqual(output["charged_jvp_queries"], 8)


if __name__ == "__main__":
    unittest.main()
