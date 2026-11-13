#!/usr/bin/env python3
"""OWI-EC005G contextual gate invariants, leakage and chosen-only gradient."""
from __future__ import annotations

import math
import random
import sys
import unittest
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_contextual_learner import (
    ContextualActor, public_features, sample_option, choose_ablation_context,
    TRAIN_ROWS, DIAGNOSTIC_ROW
)
from test_owi_ec005_realtools_heterogeneous_trial import public


class ContextualTests(unittest.TestCase):
    def test_no_family_identity_feature_and_direct_feasibility(self):
        x0=public_features(public(0),0)
        x2=public_features(public(2),2)
        x3=public_features(public(3),3)
        self.assertEqual(x0.tolist(),[0.,1.,1.])
        self.assertEqual(x2.tolist(),[1.,0.,1.])
        self.assertEqual(x3.tolist(),x2.tolist())
        self.assertEqual(TRAIN_ROWS,(0,2))
        self.assertNotIn(DIAGNOSTIC_ROW, TRAIN_ROWS)

    def test_rejects_private_feature_payload(self):
        contaminated={**public(2),"verifier":{"kind":"checklist_func"}}
        with self.assertRaises(ValueError):
            public_features(contaminated,2)
        contaminated={**public(2),"initial_state":{"hidden":True}}
        with self.assertRaises(ValueError):
            public_features(contaminated,2)

    def test_valid_randomized_three_way_support(self):
        actor=ContextualActor()
        x=public_features(public(0),0)
        rng=random.Random(881)
        chosen=set()
        for _ in range(150):
            action,prob,logp,entropy=sample_option(
                actor,x,rng,epsilon=0.24)
            self.assertGreaterEqual(prob,0.08-1e-6)
            self.assertLessEqual(prob,0.84+1e-6)
            self.assertAlmostEqual(math.exp(float(logp.detach())),prob,places=5)
            self.assertGreater(float(entropy),0)
            chosen.add(action)
        self.assertEqual(chosen,{0,1,2})

    def test_training_gradient_realized_chosen_scalar_only(self):
        actor=ContextualActor()
        optim=torch.optim.Adam(actor.parameters(),lr=.08)
        x=public_features(public(0),0)
        first=torch.cat([p.detach().flatten() for p in actor.parameters()])
        action,p,logp,entropy=sample_option(
            actor,x,random.Random(4),epsilon=.24)
        chosen_terminal_utility=0.43
        past_selected_baseline=0.30
        loss=-(chosen_terminal_utility-past_selected_baseline)*logp-.002*entropy
        optim.zero_grad(set_to_none=True)
        loss.backward()
        self.assertTrue(any(p.grad is not None and
                            float(p.grad.abs().sum())>0 for p in actor.parameters()))
        optim.step()
        after=torch.cat([p.detach().flatten() for p in actor.parameters()])
        self.assertGreater(float((after-first).abs().sum()),0.)

    def test_shuffled_and_zero_differ_from_context(self):
        original=public_features(public(0),0)
        other=public_features(public(2),2)
        self.assertEqual(choose_ablation_context(original,"normal",other).tolist(),
                         original.tolist())
        self.assertEqual(choose_ablation_context(original,"shuffled",other).tolist(),
                         other.tolist())
        self.assertEqual(choose_ablation_context(original,"zero",other).tolist(),
                         [0.,0.,1.])
        with self.assertRaises(ValueError):
            choose_ablation_context(original,"oracle",other)


if __name__=="__main__":
    unittest.main()
