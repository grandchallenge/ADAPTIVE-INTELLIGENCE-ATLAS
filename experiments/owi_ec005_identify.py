#!/usr/bin/env python3
"""Randomized on-policy probe-intervention identification for OWI-EC-005.

The first intervention is sampled from a logged mixture propensity. The
second action follows the *frozen* controller conditional on the observed
probe. Only realized terminal losses are used; no unchosen probes or
alternate repair outcomes are evaluated. This estimates the value of
forcing a FIRST probe action under the given downstream repair policy.
"""
import math
import statistics

import torch

from owi_ec004_core import Cfg
from owi_ec005_conditional import make_batch, run_policy


@torch.no_grad()
def identify_probe_value(core, policy, cfg: Cfg, seed: int, *,
                         kind="gaussian", batches=6, n=256, epsilon=0.2):
    if batches < 2 or n < 2:
        raise ValueError("require repeated independent samples")
    if not 0 < epsilon <= 1:
        raise ValueError("randomization must give every probe positive support")
    env_rng = torch.Generator().manual_seed(seed * 1000 + 6192)
    action_rng = torch.Generator().manual_seed(seed * 1000 + 6193)
    # A time-invariant policy is essential: unlike online training, this
    # evaluates one frozen controller and its assigned propensities.
    policy.eval()
    core.eval()
    samples = [[], [], []]
    counts = [0, 0, 0]
    weights = [[], [], []]
    for _ in range(batches):
        batch = make_batch(core, cfg, env_rng, n=n, kind=kind)
        result = run_policy(core, policy, cfg, batch, action_rng,
                            mode="active", epsilon=epsilon, greedy=False)
        p = result["probe"]
        propensity = result["propensity_probe"]
        outcomes = result["loss"]
        for a in range(3):
            indicator = (p == a).float()
            inverse = indicator / propensity
            scores = inverse * outcomes
            samples[a].extend(scores.tolist())
            weights[a].extend(inverse.tolist())
            counts[a] += int(indicator.sum())
    estimates = [statistics.mean(samples[a]) for a in range(3)]
    total = batches * n

    def effect(first, second):
        paired = [a - b for a, b in zip(samples[first], samples[second])]
        return {"estimate": statistics.mean(paired),
                "standard_error": statistics.stdev(paired) / math.sqrt(total)}

    ess = []
    for a in range(3):
        w = weights[a]
        ess.append((sum(w) ** 2 / sum(v * v for v in w))
                   if sum(v * v for v in w) > 0 else 0)
    return {
        "experiment": "randomized first probe, frozen downstream controller",
        "estimand": "E[L(do(probe=0), downstream policy)] - E[L(do(probe=a), downstream policy)]",
        "epsilon": epsilon,
        "n": total,
        "arm_counts": counts,
        "arm_effective_sample_sizes": ess,
        "inverse_propensity_loss": {
            "no_probe": estimates[0], "probe_A": estimates[1],
            "probe_B": estimates[2]},
        "benefit_probe_A": effect(0, 1),
        "benefit_probe_B": effect(0, 2),
        "identification_assumptions": [
            "known positive logged first-stage mixture propensities",
            "frozen controller during evaluation",
            "randomized intervention, no hidden action-dependent outcome censoring",
            "consistency and no interference between independent examples",
            "second-stage action follows the frozen policy conditioned on chosen probe",
        ],
        "not_estimated": [
            "per-example unobserved counterfactuals",
            "optimal probe-and-repair dynamic regime",
            "effect of choosing an alternative repair at the second stage",
            "any hardware energy or wall-clock causal effect",
        ],
    }
