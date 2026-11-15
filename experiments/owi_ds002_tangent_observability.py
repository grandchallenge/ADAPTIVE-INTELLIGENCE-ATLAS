#!/usr/bin/env python3
"""OWI-DS002 C0: *evaluator-only* tangent-information diagnostic.

Uses mechanism/fault labels only in a privileged diagnostic, never in A/B
program-selection or a deployed controller. Tests whether selected-run
checkpoint JVP observations add held-out mechanism information beyond the
already observed replay discrepancy; does NOT establish outcome-only learning.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import torch
from torch import nn
from torch.nn import functional as F

from owi_ec004_core import Cfg
from owi_ec004_train import train_base
from owi_ec005_conditional import (
    ConditionalReplay, make_batch, public_telemetry)
from owi_ds002_chosen_tangents import ChosenRunTangents


@torch.no_grad()
def paired_primal_batch(core, cfg, seed, n, kind):
    rng = torch.Generator().manual_seed(seed)
    return make_batch(core, cfg, rng, n=n, kind=kind)


def measured_features(core, cfg, seed, n, kind):
    batch = paired_primal_batch(core, cfg, seed, n, kind)
    # Every row chooses the same legitimate branch-A probe. No fault label
    # influences which operation is performed; labels are inspected AFTER.
    probe = torch.ones(n, dtype=torch.long)
    replay = ConditionalReplay(core, batch, cfg)
    residual = replay.probe(probe)[:, 0]
    cap = ChosenRunTangents(replay)
    indices = torch.arange(n, dtype=torch.long)
    direction = torch.ones((n, cfg.h)) / cfg.h ** .5
    tangent = cap.query(0, indices, direction)
    z = public_telemetry(batch)
    features = torch.column_stack((z, residual.detach(), tangent.detach()))
    receipt = cap.accounting()
    receipt["actual_replay_calls"] = replay.actual_calls
    receipt["actual_suffix_replays"] = int(replay.spent.sum())
    # This final filtering is privileged EVALUATION ONLY. An online learner
    # must not receive fault_audit or the mechanism label.
    chosen_a_fault = batch.fault_audit == 1
    return features[chosen_a_fault].detach(), receipt, batch


def mechanism_pair(core, cfg, seed, n):
    gaussian, g_rec, g_batch = measured_features(
        core, cfg, seed, n, "gaussian")
    checkpoint, c_rec, c_batch = measured_features(
        core, cfg, seed, n, "checkpoint")
    if not torch.equal(g_batch.x, c_batch.x):
        raise AssertionError("paired exogenous inputs differ")
    if not torch.equal(g_batch.fault_audit, c_batch.fault_audit):
        raise AssertionError("paired affected-branch masks differ")
    if len(gaussian) != len(checkpoint) or not len(gaussian):
        raise AssertionError("no paired branch-A fault examples")
    features = torch.cat((gaussian, checkpoint))
    labels = torch.cat((torch.zeros(len(gaussian)),
                        torch.ones(len(checkpoint))))
    return features, labels, {"gaussian": g_rec, "checkpoint": c_rec,
                              "affected_a_examples": len(gaussian)}


def auc(prob, target):
    p = prob[target > .5]
    q = prob[target < .5]
    return float(((p[:, None] > q[None, :]).float() +
                  .5 * (p[:, None] == q[None, :]).float()).mean())


def fit_diagnostic(train_x, train_y, test_x, test_y, indices, *, seed):
    # Intentional privilege: true mechanism labels provide an evaluator-only
    # upper-bound discrimination test; NEVER import into learner training.
    torch.manual_seed(seed)
    train = train_x[:, indices]
    test = test_x[:, indices]
    mean, sd = train.mean(0), train.std(0).clamp_min(1e-5)
    train = (train - mean) / sd
    test = (test - mean) / sd
    model = nn.Linear(train.shape[1], 1)
    optimizer = torch.optim.Adam(model.parameters(), lr=.03)
    for _ in range(150):
        loss = F.binary_cross_entropy_with_logits(
            model(train).squeeze(1), train_y)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        p = model(test).squeeze(1).sigmoid()
        return {"heldout_accuracy": float(((p > .5).float() == test_y).float().mean()),
                "heldout_brier": float((p - test_y).square().mean()),
                "heldout_auc": auc(p, test_y)}


def run(seed, *, pretrain=250, train_n=256, eval_n=512):
    torch.set_num_threads(1)
    begin = time.perf_counter()
    cfg = Cfg(h=12, length=9, suffix=3, p_fault=1.)
    core, accuracy = train_base(seed, cfg, pretrain)
    core.eval()
    for p in core.parameters():
        p.requires_grad_(False)
    paired = [mechanism_pair(core, cfg, seed * 811 + i + 19, train_n)
              for i in range(3)]
    x = torch.cat([r[0] for r in paired])
    y = torch.cat([r[1] for r in paired])
    x_test, y_test, test_receipts = mechanism_pair(
        core, cfg, seed * 811 + 819, eval_n)
    variants = {
        "residual_only": [4],
        "residual_plus_measured_jvp": [4, 5],
        "public_telemetry_plus_residual": [0, 1, 2, 3, 4],
        "public_telemetry_residual_jvp": [0, 1, 2, 3, 4, 5],
    }
    results = {key: fit_diagnostic(x, y, x_test, y_test, indices, seed=seed+43)
               for key, indices in variants.items()}
    receipts = [r[2] for r in paired] + [test_receipts]
    total_queries = sum(rr[arm]["charged_jvp_queries"]
                        for rr in receipts for arm in ("gaussian", "checkpoint"))
    total_examples = sum(rr[arm]["charged_jvp_examples"]
                         for rr in receipts for arm in ("gaussian", "checkpoint"))
    return {
        "research": "OWI-DS-002 C0", "seed": seed,
        "role": "PRIVILEGED_EVALUATION_ONLY_MECHANISM_LABEL_DIAGNOSTIC",
        "training_mechanism_labels_used": True,
        "not_outcome_only_policy_learning": True,
        "pretrain_accuracy": float(accuracy),
        "train_affected_branch_per_mechanism": int((y == 0).sum()),
        "test_affected_branch_per_mechanism": int((y_test == 0).sum()),
        "results": results,
        "charged_jvp_queries": total_queries,
        "charged_jvp_examples": total_examples,
        "total_elapsed_seconds": time.perf_counter() - begin,
        "warnings": [
            "labels and fault_audit are evaluator-only and are not legal learner signals",
            "train and test inputs are independently seeded but from same synthetic mechanism family",
            "discrimination under source-labelled examples does not establish online causal identification",
            "JVP compute has measured time but no physical MAC certificate",
            "no result validates differential-guided program synthesis or introspection"]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--pretrain", type=int, default=250)
    p.add_argument("--train-examples", type=int, default=256)
    p.add_argument("--eval-examples", type=int, default=512)
    p.add_argument("--output", default="")
    args = p.parse_args()
    rec = run(args.seed, pretrain=args.pretrain,
              train_n=args.train_examples, eval_n=args.eval_examples)
    data = json.dumps(rec, sort_keys=True, indent=2, allow_nan=False)
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data + "\n")
    print(data)


if __name__ == "__main__":
    main()
