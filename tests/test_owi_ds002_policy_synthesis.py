#!/usr/bin/env python3
"""Outcome-only program synthesis invariants; no causal benefit is asserted."""
import math
import sys
import unittest
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments"))
from owi_ec004_core import Cfg, Core
from owi_ec005_conditional import make_batch, run_policy
from owi_ds002_policy_synthesis import (
    ExecutablePolicy, LoggedEpisode, Probe, Program, Repair,
    collect, grammar, offpolicy_risk, run, select)


class PolicySearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        torch.set_num_threads(1)

    def setUp(self):
        torch.manual_seed(116)
        self.cfg = Cfg(h=5, length=9, suffix=3)
        self.core = Core(5).eval()

    def test_grammar_well_typed(self):
        z = torch.randn(17, 4)
        post = torch.randn(17, 8)
        self.assertGreater(len(grammar()), 50)
        for program in grammar():
            p, r = program.actions(z, post)
            self.assertEqual(p.shape, (17,))
            self.assertEqual(r.shape, (17,))
            self.assertTrue(bool(((p >= 0) & (p < 3)).all()))
            self.assertTrue(bool(((r >= 0) & (r < 4)).all()))

    def test_ope_observes_only_matching_realized_action(self):
        n = 4
        z = torch.zeros(n, 4)
        post = torch.zeros(n, 8)
        logged = LoggedEpisode(
            z, post, torch.tensor([0, 1, 0, 1]),
            torch.tensor([0, 0, 1, 1]),
            torch.full((n,), 1/3), torch.full((n,), 1/4),
            torch.tensor([1., 100., 200., 300.]))
        program = Program(Probe("fixed", branch=0),
                          Repair("fixed", action=0))
        a = offpolicy_risk(program, logged)
        self.assertEqual(a["matches"], 1)
        self.assertAlmostEqual(a["estimated_cost"], 1.)
        changed = LoggedEpisode(z, post, logged.probe, logged.repair,
                                logged.probe_propensity,
                                logged.repair_propensity,
                                torch.tensor([1., -9999., 9999., -9999.]))
        b = offpolicy_risk(program, changed)
        self.assertEqual(a, b)

    def test_realized_policy_replay_has_no_hidden_audit_input(self):
        batch = make_batch(self.core, self.cfg,
                           torch.Generator().manual_seed(431), n=9)
        prog = Program(Probe("fixed", branch=1), Repair("probed"))
        adapter = ExecutablePolicy(prog)
        out_a = run_policy(self.core, adapter, self.cfg, batch,
                           torch.Generator().manual_seed(432),
                           mode="active", epsilon=0, greedy=True)
        self.assertTrue(bool((out_a["probe"] == 1).all()))
        self.assertTrue(bool((out_a["repair"] == 1).all()))
        self.assertEqual(int(out_a["spent"].sum()), 9)
        self.assertEqual(out_a["replay_calls"], 1)
        batch.fault_audit = object()
        out_b = run_policy(self.core, adapter, self.cfg, batch,
                           torch.Generator().manual_seed(432),
                           mode="active", epsilon=0, greedy=True)
        self.assertTrue(torch.equal(out_a["loss"], out_b["loss"]))

    def test_positive_logging_support_and_discrete_selection(self):
        logged = collect(self.core, self.cfg, seed=4,
                         n=420, mechanism="gaussian")
        program, info = select(logged, min_ess=10)
        self.assertGreater(info["qualified"], 0)
        self.assertTrue(math.isfinite(info["selected_ope"]["estimated_cost"]))
        self.assertIn(program, grammar())
        self.assertTrue(bool((logged.probe_propensity > 0).all()))
        self.assertTrue(bool((logged.repair_propensity > 0).all()))
        self.assertFalse(logged.terminal_cost.requires_grad)

    def test_end_to_end_smoke_extract_and_heldout(self):
        report = run(seed=3, pretrain=3, n_log=360, n_eval=12)
        self.assertEqual(report["variant"],
                         "A: outcome-only typed symbolic policy synthesis")
        self.assertEqual(len(report["heldout"]), 6)
        self.assertTrue(math.isfinite(report["total_wall_seconds"]))
        self.assertEqual(report["logging_examples"], 360)
        self.assertTrue(all(math.isfinite(r["mean_total_cost"])
                            for r in report["heldout"]))


if __name__ == "__main__":
    unittest.main()
