#!/usr/bin/env python3
"""Evaluation-only omniscient repair lower bound for OWI-EC-005.

Never import/call this code from fit(), actor losses or action selection.
It deliberately computes every unchosen replay and repair outcome, making
it privileged. All such compute is excluded from deployed controller cost.
"""
from __future__ import annotations

import torch
from torch.nn import functional as F

from owi_ec004_core import Cfg
from owi_ec005_conditional import ConditionalReplay, make_batch


@torch.no_grad()
def privileged_oracle(core, cfg: Cfg, seed: int, *, kind="gaussian",
                      length=9, n=512, task="majority"):
    # Identical environment cohort seed to actor_critic.evaluate.
    mechanism = {"gaussian": 1, "dropout": 2, "signflip": 3, "roll": 4,
                 "small_noise": 5, "persistent": 6,
                 "coupled": 7, "checkpoint": 8}[kind]
    rng = torch.Generator().manual_seed(
        seed * 100000 + 1234 + 17 * length + mechanism +
        (300 if task == "parity" else 0))
    audit_cfg = Cfg(h=cfg.h, suffix=cfg.suffix, length=length,
                    p_fault=cfg.p_fault, sigma=cfg.sigma,
                    lambda_compute=cfg.lambda_compute,
                    policy_overhead=cfg.policy_overhead)
    batch = make_batch(core, audit_cfg, rng, n=n, kind=kind, task=task)
    source = ConditionalReplay(core, batch, audit_cfg)
    all_idx = torch.arange(n)
    source._ensure(0, all_idx)
    source._ensure(1, all_idx)
    clean = [core.heads[c](source.cache[c]).squeeze(1) for c in range(2)]
    scores = []
    for r in range(4):
        logits = batch.raw.clone()
        for c in range(2):
            if r & (1 << c):
                logits[:, c] = clean[c]
        loss = F.binary_cross_entropy_with_logits(
            logits, batch.y, reduction="none").mean(dim=1)
        cost = audit_cfg.lambda_compute * ((r & 1 != 0) + (r & 2 != 0))
        scores.append(loss + cost)
    loss_by_action = torch.stack(scores, dim=1)
    oracle_loss, oracle_action = loss_by_action.min(dim=1)
    return {
        "n_examples": n,
        "fixed_none": float(scores[0].mean()),
        "fixed_both": float(scores[3].mean()),
        "omniscient_repair_lower_bound": float(oracle_loss.mean()),
        "oracle_action_rates": {
            str(a): float((oracle_action == a).float().mean()) for a in range(4)},
        "privilege": "All four unchosen repair outcomes and both replays "
                     "computed solely in isolated evaluator; prohibited in training",
        "not_a_deployed_compute_measurement": True,
    }
