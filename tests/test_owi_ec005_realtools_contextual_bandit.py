#!/usr/bin/env python3
"""Contract tests for contextual chosen-only estimator and strict propensities."""
from __future__ import annotations
import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_contextual_bandit import (
    Bandit, EXPLORE_ROUNDS, context_key
)
from owi_ec005_realtools_contextual_learner import public_features
from test_owi_ec005_realtools_heterogeneous_trial import public


class BanditTests(unittest.TestCase):
    def test_independent_contextual_exploration_and_exact_propensities(self):
        b=Bandit(epsilon=0.24)
        rng=random.Random(778)
        contexts=["public_lookup_required","direct_publicly_available"]
        order={c:[] for c in contexts}
        for step in range(EXPLORE_ROUNDS*3):
            for key in contexts:
                arm,pr,mode=b.choose(key,step,rng)
                order[key].append(arm)
                self.assertEqual(mode,"without_replacement_exploration")
                self.assertEqual(pr,1/(3-step%3))
                b.update(key,arm,float(arm))
        for key in contexts:
            self.assertEqual(b.n[key],[EXPLORE_ROUNDS]*3)
            for j in range(EXPLORE_ROUNDS):
                self.assertEqual(set(order[key][3*j:3*j+3]),{0,1,2})

    def test_only_chosen_terminal_scalar_enters_estimates(self):
        b=Bandit()
        key="direct_publicly_available"
        for arm,utility in ((0,.4615),(1,.5285),(2,.5185)):
            b.update(key,arm,utility)
        self.assertEqual(b.best(key),1)
        self.assertEqual(b.means(key),[.4615,.5285,.5185])
        self.assertEqual(len(b.history),3)
        self.assertFalse(any(isinstance(v,dict) for v in b.history))

    def test_observation_needed_context_picks_probe_and_shuffled_does_not(self):
        b=Bandit()
        for j,utility in enumerate((.25,.25,.43)):
            b.update("public_lookup_required",j,utility)
        for j,utility in enumerate((.4615,.5285,.5185)):
            b.update("direct_publicly_available",j,utility)
        self.assertEqual(b.best("public_lookup_required"),2)
        self.assertEqual(b.best("direct_publicly_available"),1)
        self.assertNotEqual(b.best("public_lookup_required"),
                            b.best("direct_publicly_available"))
        self.assertEqual(context_key({"context":public_features(public(0),0)}),
                         "public_lookup_required")
        self.assertEqual(context_key({"context":public_features(public(2),2)}),
                         "direct_publicly_available")
        self.assertEqual(context_key({"context":public_features(public(3),3)}),
                         "direct_publicly_available")

    def test_epsilon_support_exploitation_and_true_chosen_probability(self):
        b=Bandit(epsilon=.24)
        key="public_lookup_required"
        for arm,utility in ((0,.25),(1,.25),(2,.43)):
            for _ in range(EXPLORE_ROUNDS):
                b.update(key,arm,utility)
        rng=random.Random(13)
        seen=set()
        for t in range(200):
            action,prob,phase=b.choose(key,100+t,rng)
            self.assertEqual(phase,"epsilon_greedy")
            self.assertGreaterEqual(prob,.08-1e-10)
            self.assertAlmostEqual(prob,.84 if action==2 else .08)
            seen.add(action)
        self.assertEqual(seen,{0,1,2})

    def test_unsafe_context_and_unsupported_exploitation(self):
        b=Bandit()
        with self.assertRaises(ValueError):
            b.best("new_context_no_observations")
        with self.assertRaises(ValueError):
            context_key({"context":[1.0,0.0,1.0]})
        with self.assertRaises(ValueError):
            Bandit(epsilon=0)


if __name__=="__main__":
    unittest.main()
