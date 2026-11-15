#!/usr/bin/env python3
"""OWI-DS-002 B: neural-guided search projected to the SAME typed grammar.

The guide learns from the *same* logged, chosen-action outcomes as the
symbolic A baseline. A differentiable sequential importance-weighted risk
fits a conditional action guide; an offline projection extracts a discrete
policy program. No unchosen repair outcome, fault ID, checkpoint oracle,
or tangent observation enters B. This is NOT derivative-guided synthesis.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from pathlib import Path
import time

import torch
from torch import nn

from owi_ec004_core import Cfg
from owi_ec004_train import train_base
from owi_ds002_policy_synthesis import (
    LoggedEpisode, collect, evaluate, grammar, select)


class Guide(nn.Module):
    def __init__(self, hidden=24):
        super().__init__()
        self.probe = nn.Sequential(nn.Linear(4, hidden), nn.Tanh(),
                                   nn.Linear(hidden, 3))
        self.repair = nn.Sequential(nn.Linear(8, hidden), nn.Tanh(),
                                    nn.Linear(hidden, 4))

    def distributions(self, log: LoggedEpisode):
        return self.probe(log.state).softmax(-1), self.repair(log.post).softmax(-1)


def fit_guide(log: LoggedEpisode, seed: int, *, steps=300, lr=.004):
    if steps <= 0:
        raise ValueError("positive steps required")
    torch.manual_seed(seed * 177 + 73)
    model = Guide()
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.001)
    observed = log.terminal_cost.detach()
    # Baseline is a scalar; the expectation of policy importance weights is
    # one under a correctly logged full-support behavior policy.
    centered = observed - observed.mean()
    trace = []
    began = time.perf_counter()
    for step in range(steps):
        p, r = model.distributions(log)
        chosen_p = p.gather(1, log.probe[:, None]).squeeze(1)
        chosen_r = r.gather(1, log.repair[:, None]).squeeze(1)
        weight = ((chosen_p * chosen_r) /
                  (log.probe_propensity * log.repair_propensity))
        # Sequential IPS: this is differentiation through a *policy model*,
        # not a derivative observation of the environment.
        risk = (weight * centered).mean()
        # Penalize overly concentrated off-policy weights and preserve
        # support during early policy search; no privileged risk used.
        variance = (weight - 1).square().mean()
        kl_probe = (p * (p.clamp_min(1e-12).log() +
                         torch.log(p.new_tensor(3.)))).sum(-1).mean()
        kl_repair = (r * (r.clamp_min(1e-12).log() +
                          torch.log(r.new_tensor(4.)))).sum(-1).mean()
        objective = risk + .002 * variance + .001 * (kl_probe + kl_repair)
        opt.zero_grad(set_to_none=True)
        objective.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 2.)
        opt.step()
        if (step + 1) % max(1, steps // 10) == 0:
            trace.append({"step": step + 1,
                          "centered_ips_objective": float(risk.detach()),
                          "weight_second_moment": float(weight.square().mean().detach()),
                          "training_objective": float(objective.detach())})
    return model.eval(), trace, time.perf_counter() - began


@torch.no_grad()
def project_to_typed_program(model: Guide, log: LoggedEpisode):
    """Project guide to a discrete two-stage program without new outcomes.

    Probe matching is observable for every training example. The repair
    projection term uses a first-stage inverse-propensity correction because
    only the *chosen* post-probe state exists. The learned guide itself
    sees no unexecuted probe poststate.
    """
    p, r = model.distributions(log)
    logp = p.clamp_min(1e-12).log()
    logr = r.clamp_min(1e-12).log()
    qualified = []
    for program in grammar():
        pp, rr = program.actions(log.state, log.post)
        probe_loss = -logp.gather(1, pp[:, None]).mean()
        chosen = pp == log.probe
        weighted = chosen.float() / log.probe_propensity
        repair_loss = -(weighted * logr.gather(1, rr[:, None]).squeeze(1)).mean()
        score = float(probe_loss + repair_loss +
                      .004 * program.complexity())
        qualified.append((score, program))
    qualified.sort(key=lambda row: (row[0], row[1].complexity(), repr(row[1])))
    return qualified[0][1], {"programs_considered": len(qualified),
                             "projection_score": qualified[0][0],
                             "method": "inverse-propensity-corrected neural-to-typed-program projection"}


def run(seed, *, pretrain=250, steps=300, n_log=4095, n_eval=512):
    torch.set_num_threads(1)
    started = time.perf_counter()
    cfg = Cfg(h=12, length=9, suffix=3)
    core, accuracy = train_base(seed, cfg, pretrain)
    core.eval()
    for p in core.parameters():
        p.requires_grad_(False)
    logs = [collect(core, cfg, seed * 31 + i, n=n_log // 3,
                    mechanism=k) for i, k in
            enumerate(("gaussian", "dropout", "signflip"))]
    logged = LoggedEpisode(
        *(torch.cat([getattr(item, f) for item in logs])
          for f in LoggedEpisode.__dataclass_fields__))
    # A is recomputed only from the same observational data; fixed candidate
    # comparison occurs on independent evaluation cohorts below.
    a_start = time.perf_counter()
    baseline, a_diag = select(logged)
    a_select_seconds = time.perf_counter() - a_start
    guide, curve, b_train_seconds = fit_guide(logged, seed, steps=steps)
    b_start = time.perf_counter()
    guided, b_diag = project_to_typed_program(guide, logged)
    b_project_seconds = time.perf_counter() - b_start
    conditions = [(k, 9, "majority") for k in
                  ("persistent", "coupled", "checkpoint", "roll")]
    conditions += [("gaussian", 13, "majority"),
                   ("gaussian", 9, "parity")]
    paired = []
    for i, (k, length, task) in enumerate(conditions):
        env_seed = seed * 101 + (i if i < 4 else (11 if i == 4 else 12))
        a = evaluate(core, cfg, baseline, seed=env_seed, mechanism=k,
                     length=length, n=n_eval, task=task)
        b = evaluate(core, cfg, guided, seed=env_seed, mechanism=k,
                     length=length, n=n_eval, task=task)
        paired.append({"condition": k if i < 4 else ("length13" if i == 4 else "parity"),
                       "a": a, "b": b,
                       "b_minus_a_mean_cost": b["mean_total_cost"]-a["mean_total_cost"]})
    return {"research": "OWI-DS-002", "variant": "B neural-guided typed program search",
            "seed": seed, "pretrain_steps": pretrain, "guide_steps": steps,
            "pretrain_accuracy": float(accuracy), "logging_examples": len(logged.probe),
            "a_program": {"probe": asdict(baseline.probe), "repair": asdict(baseline.repair)},
            "b_program": {"probe": asdict(guided.probe), "repair": asdict(guided.repair)},
            "a_selection": a_diag, "b_projection": b_diag,
            "guide_curve": curve, "a_select_seconds": a_select_seconds,
            "b_training_seconds": b_train_seconds,
            "b_projection_seconds": b_project_seconds,
            "paired": paired, "total_wall_seconds": time.perf_counter() - started,
            "limits": [
                "neural guide differentiates chosen-action IPS objective, NOT environment",
                "not a differential-synthesis C or reflective D test",
                "A and B do not yet have equal total search compute",
                "both use one small fixed typed grammar and synthetic recurrent core",
                "BCE is not verified general program correctness",
                "no privileged unchosen outcomes accessed by training"]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--pretrain", type=int, default=250)
    p.add_argument("--steps", type=int, default=300)
    p.add_argument("--logging-examples", type=int, default=4095)
    p.add_argument("--eval-examples", type=int, default=512)
    p.add_argument("--output", default="")
    p.add_argument("--wandb-project", default="")
    args = p.parse_args()
    result = run(args.seed, pretrain=args.pretrain, steps=args.steps,
                 n_log=args.logging_examples, n_eval=args.eval_examples)
    if args.wandb_project:
        import wandb
        with wandb.init(project=args.wandb_project, config=vars(args),
                        name=f"owi-ds002-neural-guided-{args.seed}"):
            wandb.log({f"paired/{case['condition']}/b_minus_a":
                       case["b_minus_a_mean_cost"] for case in result["paired"]})
            for row in result["guide_curve"]:
                wandb.log({"guide/centered_ips": row["centered_ips_objective"],
                           "guide/weight_second_moment": row["weight_second_moment"]},
                          step=row["step"])
    payload = json.dumps(result, indent=2, sort_keys=True, allow_nan=False)
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload + "\n", encoding="utf8")
    print(payload)


if __name__ == "__main__":
    main()
