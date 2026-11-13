#!/usr/bin/env python3
"""Outcome-only learned option-gate and information-boundary invariants."""
from __future__ import annotations
import math
import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
import torch
from owi_ec005_realtools_outcome_learner import (
    Actor, GoalPolicy, features, choose, FEATURE_DIM
)
from test_owi_ec005_realtools_goal import public


class TestOutcomeOnlyGates(unittest.TestCase):
    def test_actor_uses_only_public_derived_policy_state(self):
        p=GoalPolicy(public(),2)
        p.state["location_id"]="OBSERVED_LOCATION"
        p.state["reporter_id"]="OBSERVED_REPORTER"
        p.state["prior"]=[{"report_id":"OBSERVED_PRIOR"}]
        x=features(p,1)
        self.assertEqual(len(x),FEATURE_DIM)
        self.assertEqual(x[:3].tolist(),[0.,1.,0.])
        self.assertEqual(x[3:6].tolist(),[1.,1.,1.])
        # Test the neural gate ablation only; the underlying planner retains
        # actual public observations to avoid substituting fabricated IDs.
        z=features(p,1,ablation="zero_feedback")
        self.assertEqual(z[:3].tolist(),x[:3].tolist())
        self.assertEqual(z[3:8].tolist(),[0.]*5)
        self.assertEqual(p.state["reporter_id"],"OBSERVED_REPORTER")
        self.assertFalse(any("verifier" in k for k in p.state))
        with self.assertRaises(ValueError):
            features(p,1,ablation="privileged_oracle")

    def test_epsilon_exploration_has_two_sided_support_and_true_log_prob(self):
        torch.manual_seed(13)
        rng=random.Random(111)
        a=Actor()
        p=GoalPolicy(public(),2)
        x=features(p,0)
        seen=set()
        for _ in range(100):
            action,pr,logp,h=choose(a,x,epsilon=.20,greedy=False,rng=rng)
            self.assertGreaterEqual(pr,.10-1e-7)
            self.assertLessEqual(pr,.90+1e-7)
            self.assertAlmostEqual(math.exp(float(logp.detach())),pr,places=5)
            self.assertGreater(float(h),0)
            seen.add(action)
        self.assertEqual(seen,{0,1})

    def test_terminal_only_reinforce_updates_learnable_parameters(self):
        torch.manual_seed(4)
        a=Actor()
        optim=torch.optim.Adam(a.parameters(),lr=.02)
        p=GoalPolicy(public(),2)
        x=features(p,0)
        first=torch.cat([w.detach().flatten() for w in a.parameters()])
        action,pr,logp,entropy=choose(a,x,epsilon=.20,greedy=False,
                                      rng=random.Random(42))
        # The training method consumes ONLY a realized terminal scalar and
        # the charge for selected calls; no unchosen outcomes are supplied.
        realized_terminal_reward=.3846
        realized_selected_calls=8
        terminal_utility=realized_terminal_reward-.01*realized_selected_calls
        loss=-(terminal_utility-.1538)*logp-.002*entropy
        optim.zero_grad(set_to_none=True)
        loss.backward()
        self.assertTrue(any(w.grad is not None and
                            float(w.grad.abs().sum())>0 for w in a.parameters()))
        optim.step()
        after=torch.cat([w.detach().flatten() for w in a.parameters()])
        self.assertGreater(float((after-first).abs().sum()),0)

    def test_stages_are_strict_and_no_hidden_fields(self):
        a=Actor()
        p=GoalPolicy(public(),2)
        for stage in range(3):
            self.assertEqual(a(features(p,stage)).numel(),1)
        with self.assertRaises(ValueError):
            features(p,3)
        self.assertEqual(set(p.state),{
            "location_id","reporter_id","prior","report_id","created",
            "date_reported","verified"
        })


if __name__=="__main__":
    unittest.main()
