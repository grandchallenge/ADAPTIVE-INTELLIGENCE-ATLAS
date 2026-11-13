#!/usr/bin/env python3
"""Invariant, leakage, and sampled-gradient smoke tests for OWI-EC-005."""
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments"))
import torch

from owi_ec004_core import Cfg, Core
from owi_ec005_conditional import make_batch, run_policy, public_telemetry
from owi_ec005_actor_critic import fit, Controller, evaluate


class Forced:
    def __init__(self, probe, repair):
        self.p, self.r = probe, repair

    def probe_actor(self, x):
        logits = torch.full((len(x), 3), -50.0)
        logits[:, self.p] = 50
        return logits

    def repair_actor(self, x):
        logits = torch.full((len(x), 4), -50.0)
        logits[:, self.r] = 50
        return logits


class Tests(unittest.TestCase):
    def setUp(self):
        torch.set_num_threads(1)
        torch.manual_seed(22)
        self.cfg = Cfg(h=5, batch=8, length=9, suffix=3)
        self.core = Core(self.cfg.h).eval()
        self.batch = make_batch(self.core, self.cfg,
                                torch.Generator().manual_seed(300), n=8)

    def run_forced(self, probe, repair):
        observed = []
        hooks = []
        for c, gru in enumerate(self.core.branches):
            hooks.append(gru.register_forward_pre_hook(
                lambda module, inp, c=c: observed.append((c, inp[0].shape[0]))))
        try:
            out = run_policy(
                self.core, Forced(probe, repair), self.cfg, self.batch,
                torch.Generator().manual_seed(101), mode="active",
                greedy=True, epsilon=0)
        finally:
            for hook in hooks:
                hook.remove()
        return out, observed

    def test_no_probe_no_repair_runs_zero_suffixes(self):
        out, observed = self.run_forced(0, 0)
        self.assertEqual(observed, [])
        self.assertEqual(out["replay_calls"], 0)
        self.assertEqual(int(out["spent"].sum()), 0)
        self.assertTrue((out["probe"] == 0).all())
        self.assertTrue((out["repair"] == 0).all())

    def test_probe_repair_reuses_only_chosen_cache(self):
        out, observed = self.run_forced(1, 1)
        self.assertEqual(observed, [(0, 8)])
        self.assertEqual(out["replay_calls"], 1)
        self.assertEqual(int(out["spent"].sum()), 8)
        self.assertTrue((out["spent"] == 1).all())

    def test_no_probe_both_repair_executes_both(self):
        out, observed = self.run_forced(0, 3)
        self.assertEqual(observed, [(0, 8), (1, 8)])
        self.assertEqual(int(out["spent"].sum()), 16)
        self.assertEqual(out["replay_calls"], 2)

    def test_probe_a_and_repair_both_does_not_replay_a_twice(self):
        out, observed = self.run_forced(1, 3)
        self.assertEqual(observed, [(0, 8), (1, 8)])
        self.assertEqual(int(out["spent"].sum()), 16)

    def test_fault_metadata_cannot_affect_policy_actions(self):
        original = self.batch.fault_audit
        out_a, _ = self.run_forced(1, 2)
        self.batch.fault_audit = torch.full_like(original, 999)
        out_b, _ = self.run_forced(1, 2)
        self.assertTrue(torch.equal(out_a["repair"], out_b["repair"]))
        self.assertTrue(torch.allclose(out_a["loss"], out_b["loss"]))
        self.assertEqual(public_telemetry(self.batch).shape, (8, 4))
        self.assertFalse(public_telemetry(self.batch).requires_grad)

    def test_all_support_propensities_positive_and_outcome_gradient(self):
        policy = Controller()
        with torch.no_grad():
            policy.probe_actor[-1].bias[:] = torch.tensor([15.0, -5.0, -10.0])
        out = run_policy(
            self.core, policy, self.cfg, self.batch,
            torch.Generator().manual_seed(123), mode="active",
            greedy=False, epsilon=0.05)
        self.assertGreaterEqual(float(out["propensity_probe"].min()), 0.05 / 3 - 1e-7)
        self.assertGreaterEqual(float(out["propensity_repair"].min()), 0.05 / 4 - 1e-7)
        objective = (out["loss"].detach() *
                     (out["logp_probe"] + out["logp_repair"])).mean()
        objective.backward()
        self.assertTrue(any(p.grad is not None and torch.isfinite(p.grad).all()
                            for p in policy.parameters()))

    def test_conditional_macs_match_executed_samples(self):
        out, _ = self.run_forced(1, 3)
        expected = 8 * 2 * (self.cfg.suffix * 3 * 5 * 6 + 5)
        self.assertEqual(out["dense_macs"]["conditional_replay"], expected)
        self.assertTrue(math.isfinite(float(out["elapsed_seconds"])))

    def test_heldout_mechanisms_and_task_shift_finite(self):
        for kind in ("persistent", "coupled", "checkpoint", "roll"):
            result = evaluate(self.core, None, self.cfg, seed=55,
                              mode="fixed_both", kind=kind, length=9, n=16)
            self.assertTrue(math.isfinite(result["objective"]))
        parity = evaluate(self.core, None, self.cfg, seed=55,
                          mode="fixed_both", kind="gaussian", length=9,
                          n=16, task="parity")
        self.assertTrue(math.isfinite(parity["objective"]))

    def test_small_actor_critic_iteration_both_modes(self):
        for mode in ("active", "passive"):
            model, rows = fit(self.core, self.cfg, 1, mode, 3, batch_size=8)
            self.assertEqual(rows[-1]["step"], 3)
            self.assertTrue(math.isfinite(rows[-1]["outcome_only_cost"]))
            self.assertIsNotNone(model)


if __name__ == "__main__":
    unittest.main()
