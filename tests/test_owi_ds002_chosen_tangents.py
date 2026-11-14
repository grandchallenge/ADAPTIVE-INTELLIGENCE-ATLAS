#!/usr/bin/env python3
"""OWI-DS-002 first-gate tests; no trained agent or synthesis win claimed."""
import sys
import unittest
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments"))
from owi_ec004_core import Cfg, Core
from owi_ec005_conditional import ConditionalReplay, make_batch
from owi_ds002_chosen_tangents import ChosenRunTangents


class Tests(unittest.TestCase):
    def setUp(self):
        torch.set_num_threads(1)
        torch.manual_seed(192)
        self.cfg = Cfg(h=5, length=9, suffix=3, batch=8)
        self.core = Core(self.cfg.h).eval()
        self.batch = make_batch(self.core, self.cfg,
                                torch.Generator().manual_seed(913), n=8)
        self.replay = ConditionalReplay(self.core, self.batch, self.cfg)
        self.cap = ChosenRunTangents(self.replay)

    def test_no_query_without_actual_selected_execution(self):
        idx = torch.tensor([0], dtype=torch.long)
        d = torch.ones(1, self.cfg.h)
        with self.assertRaises(PermissionError):
            self.cap.query(0, idx, d)
        self.assertEqual(self.cap.accounting()["charged_jvp_queries"], 0)
        self.assertEqual(self.replay.actual_calls, 0)

    def test_branch_and_example_scope_and_mixed_conditional_replay(self):
        probes = torch.tensor([1, 0, 2, 0, 1, 2, 0, 0])
        self.replay.probe(probes)
        self.assertEqual(self.replay.actual_calls, 2)
        self.assertEqual(int(self.replay.spent.sum()), 4)
        self.assertTrue(torch.equal(self.replay.ready[0].nonzero().flatten(),
                                    torch.tensor([0, 4])))
        self.assertTrue(torch.equal(self.replay.ready[1].nonzero().flatten(),
                                    torch.tensor([2, 5])))
        self.cap.query(0, torch.tensor([0, 4]), torch.ones(2, self.cfg.h))
        for branch, idx in ((0, [1]), (0, [2]), (1, [0]), (1, [7])):
            with self.assertRaises(PermissionError):
                self.cap.query(branch, torch.tensor(idx),
                               torch.ones(len(idx), self.cfg.h))
        accounting = self.cap.accounting()
        self.assertEqual(accounting["charged_jvp_queries"], 1)
        self.assertEqual(accounting["charged_jvp_examples"], 2)
        self.assertIsNone(accounting["jvp_macs"])
        self.assertEqual(int(self.replay.spent.sum()), 4)

    def test_directional_derivative_matches_independent_fd_on_selected_run(self):
        self.replay.probe(torch.tensor([1, 0, 0, 0, 1, 0, 0, 0]))
        idx = torch.tensor([0, 4])
        direction = torch.randn(2, self.cfg.h)
        tangent = self.cap.query(0, idx, direction)
        prefix = self.cfg.length - self.cfg.suffix
        suffix = self.batch.x[idx, prefix:, :1]
        initial = self.batch.checkpoints[0][idx]
        def run(z):
            with torch.no_grad():
                _, last = self.core.branches[0](suffix, z.unsqueeze(0))
                return self.core.heads[0](last.squeeze(0)).squeeze(1)
        eps = 1e-3
        fd = (run(initial + eps * direction) -
              run(initial - eps * direction)) / (2 * eps)
        self.assertTrue(torch.allclose(tangent, fd, rtol=1e-2, atol=1e-3),
                        (tangent, fd))
        self.assertFalse(tangent.requires_grad)
        self.assertEqual(self.cap.accounting()["charged_jvp_queries"], 1)

    def test_invalid_indices_directions_and_branch_rejected_without_charge(self):
        self.replay.probe(torch.ones(8, dtype=torch.long))
        cases = [
            (0, torch.tensor([-1]), torch.ones(1, 5), IndexError),
            (0, torch.tensor([8]), torch.ones(1, 5), IndexError),
            (0, torch.tensor([0, 0]), torch.ones(2, 5), ValueError),
            (0, torch.tensor([], dtype=torch.long), torch.ones(0, 5), ValueError),
            (0, torch.tensor([0]), torch.ones(1, 4), ValueError),
            (2, torch.tensor([0]), torch.ones(1, 5), ValueError),
        ]
        for branch, idx, direction, exc in cases:
            with self.assertRaises(exc):
                self.cap.query(branch, idx, direction)
        self.assertEqual(self.cap.accounting()["charged_jvp_queries"], 0)

    def test_audit_metadata_is_not_consulted_by_tangent_query(self):
        self.replay.probe(torch.ones(8, dtype=torch.long))
        idx = torch.tensor([0, 1])
        direction = torch.ones(2, self.cfg.h)
        first = self.cap.query(0, idx, direction)
        # Permission and computed tangent must not depend on fault labels.
        self.batch.fault_audit = object()
        second = self.cap.query(0, idx, direction)
        self.assertTrue(torch.equal(first, second))
        self.assertEqual(self.cap.accounting()["charged_jvp_examples"], 4)


if __name__ == "__main__":
    unittest.main()
