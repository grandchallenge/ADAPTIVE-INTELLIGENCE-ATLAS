#!/usr/bin/env python3
"""OWI-DS002 B: outcome-only neural guidance, typed extraction and paired A/B."""
import math
import sys
import unittest
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments"))
from owi_ec004_core import Cfg, Core
from owi_ds002_policy_synthesis import collect, grammar
from owi_ds002_neural_guided import Guide, fit_guide, project_to_typed_program, run


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        torch.set_num_threads(1)

    def setUp(self):
        torch.manual_seed(17)
        self.core = Core(5).eval()
        self.cfg = Cfg(h=5, length=9, suffix=3)

    def test_guide_training_only_from_chosen_logged_actions(self):
        log = collect(self.core, self.cfg, seed=82, n=240,
                      mechanism="gaussian")
        model, curve, seconds = fit_guide(log, 82, steps=4)
        self.assertEqual(curve[-1]["step"], 4)
        self.assertTrue(math.isfinite(seconds))
        self.assertTrue(all(math.isfinite(row["training_objective"])
                            for row in curve))
        p, r = model.distributions(log)
        self.assertEqual(p.shape, (240, 3))
        self.assertEqual(r.shape, (240, 4))
        self.assertTrue(torch.allclose(p.sum(1), torch.ones(240), atol=1e-5))
        self.assertTrue(torch.allclose(r.sum(1), torch.ones(240), atol=1e-5))

    def test_discrete_projection_uses_existing_program_grammar(self):
        log = collect(self.core, self.cfg, seed=29, n=240,
                      mechanism="dropout")
        model = Guide().eval()
        prog, detail = project_to_typed_program(model, log)
        self.assertIn(prog, grammar())
        self.assertEqual(detail["programs_considered"], len(grammar()))
        self.assertTrue(math.isfinite(detail["projection_score"]))

    def test_real_training_and_paired_fresh_evaluation(self):
        output = run(2, pretrain=3, steps=4, n_log=360, n_eval=12)
        self.assertEqual(output["logging_examples"], 360)
        self.assertEqual(len(output["paired"]), 6)
        self.assertTrue(all(math.isfinite(row["b_minus_a_mean_cost"])
                            for row in output["paired"]))
        self.assertTrue(all(row["a"]["examples"] == row["b"]["examples"] == 12
                            for row in output["paired"]))
        self.assertIn("NOT environment", output["limits"][0])


if __name__ == "__main__":
    unittest.main()
