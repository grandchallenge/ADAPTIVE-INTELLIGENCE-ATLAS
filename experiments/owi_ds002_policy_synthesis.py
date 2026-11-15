#!/usr/bin/env python3
"""OWI-DS-002 A-baseline: typed, discrete, outcome-only policy-program search.

This is a real conditional probe/repair policy synthesis baseline on the
OWI-EC-005 recurrent environment, NOT a differentiable-synthesis result.
Candidate evaluation uses only chosen, realized, logged action outcomes.
The policy's *actual* selected actions are evaluated on fresh trajectories.
No hidden fault labels or unchosen action outcomes enter selection.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import math
from pathlib import Path
import time

import torch

from owi_ec004_core import Cfg, Core
from owi_ec004_train import train_base
from owi_ec005_conditional import make_batch, run_policy


@dataclass(frozen=True)
class Probe:
    rule: str
    branch: int = 0
    feature: int = 0
    threshold: float = 0.0

    def apply(self, state: torch.Tensor) -> torch.Tensor:
        n = len(state)
        if self.rule == "fixed":
            return torch.full((n,), self.branch, dtype=torch.long)
        if self.rule == "weak_logit":
            if self.feature not in (0, 2) or self.branch not in (1, 2):
                raise ValueError("invalid typed probe expression")
            return torch.where(state[:, self.feature].abs() < self.threshold,
                               self.branch, 0).long()
        if self.rule == "large_norm":
            if self.feature not in (1, 3) or self.branch not in (1, 2):
                raise ValueError("invalid typed probe expression")
            return torch.where(state[:, self.feature] > self.threshold,
                               self.branch, 0).long()
        raise ValueError("unknown probe rule")


@dataclass(frozen=True)
class Repair:
    rule: str
    action: int = 0
    threshold: float = 0.0

    def apply(self, post: torch.Tensor) -> torch.Tensor:
        n = len(post)
        if self.rule == "fixed":
            return torch.full((n,), self.action, dtype=torch.long)
        if self.rule == "probed":
            # post[4:6] are observed chosen-probe masks, not oracle labels.
            return (post[:, 4] > .5).long() + 2 * (post[:, 5] > .5).long()
        if self.rule == "gap":
            a = (post[:, 4] > .5) & (post[:, 6] > self.threshold)
            b = (post[:, 5] > .5) & (post[:, 7] > self.threshold)
            return a.long() + 2 * b.long()
        if self.rule == "weak":
            # Conditional policy can choose a repair without a prior probe.
            return torch.where(post[:, 0].abs() < post[:, 2].abs(), 1, 2).long()
        raise ValueError("unknown repair rule")


@dataclass(frozen=True)
class Program:
    probe: Probe
    repair: Repair

    def actions(self, state: torch.Tensor, post: torch.Tensor):
        return self.probe.apply(state), self.repair.apply(post)

    def complexity(self) -> int:
        return (1 if self.probe.rule == "fixed" else 3) + (
            1 if self.repair.rule == "fixed" else 3)


def grammar() -> list[Program]:
    probes = [Probe("fixed", branch=a) for a in range(3)]
    for rule, features, thresholds in (
        ("weak_logit", (0, 2), (.1, .25, .5, .8)),
        ("large_norm", (1, 3), (.1, .25, .5, .8)),
    ):
        for f in features:
            for t in thresholds:
                probes.append(Probe(rule, branch=1 + f // 2, feature=f,
                                    threshold=t))
    repairs = [Repair("fixed", action=a) for a in range(4)]
    repairs += [Repair("probed"), Repair("weak")]
    repairs += [Repair("gap", threshold=t) for t in (.025, .075, .2, .5, 1.0)]
    return [Program(p, r) for p in probes for r in repairs]


class UniformLogging:
    def probe_actor(self, x):
        return x.new_zeros((len(x), 3))

    def repair_actor(self, x):
        return x.new_zeros((len(x), 4))


class ExecutablePolicy:
    """Adapter that executes a *discrete extracted program* via run_policy."""
    def __init__(self, program: Program):
        self.program = program

    def probe_actor(self, state):
        choice = self.program.probe.apply(state)
        logits = state.new_full((len(state), 3), -40.)
        logits.scatter_(1, choice[:, None], 40.)
        return logits

    def repair_actor(self, post):
        choice = self.program.repair.apply(post)
        logits = post.new_full((len(post), 4), -40.)
        logits.scatter_(1, choice[:, None], 40.)
        return logits


@dataclass(frozen=True)
class LoggedEpisode:
    state: torch.Tensor
    post: torch.Tensor
    probe: torch.Tensor
    repair: torch.Tensor
    probe_propensity: torch.Tensor
    repair_propensity: torch.Tensor
    terminal_cost: torch.Tensor

    def __post_init__(self):
        n = len(self.probe)
        if (self.state.shape != (n, 4) or self.post.shape != (n, 8) or
            any(v.shape != (n,) for v in
                (self.repair, self.probe_propensity,
                 self.repair_propensity, self.terminal_cost))):
            raise ValueError("invalid logged trajectory shape")
        if (not bool((self.probe_propensity > 0).all()) or
            not bool((self.repair_propensity > 0).all())):
            raise ValueError("logged behavior lacks positive support")


def collect(core: Core, cfg: Cfg, seed: int, *, n: int,
            mechanism: str) -> LoggedEpisode:
    batch = make_batch(core, cfg,
                       torch.Generator().manual_seed(seed * 9871 + 17),
                       n=n, kind=mechanism)
    with torch.no_grad():
        out = run_policy(core, UniformLogging(), cfg, batch,
                         torch.Generator().manual_seed(seed * 9871 + 18),
                         mode="active", epsilon=1., greedy=False)
    return LoggedEpisode(
        out["state"].detach(), out["post"].detach(),
        out["probe"].detach(), out["repair"].detach(),
        out["propensity_probe"].detach(),
        out["propensity_repair"].detach(), out["loss"].detach())


def offpolicy_risk(program: Program, logged: LoggedEpisode) -> dict:
    """Self-normalized sequential IPS; *only* the matching chosen path.

    The resulting estimator requires correct logged propensities, coverage,
    consistency and independent episodes. It is a noisy model-selection
    estimator, NOT an estimate of unseen per-example counterfactual outcomes.
    """
    p, r = program.actions(logged.state, logged.post)
    match = (p == logged.probe) & (r == logged.repair)
    weights = match.float() / (logged.probe_propensity *
                               logged.repair_propensity)
    total = float(weights.sum())
    hits = int(match.sum())
    if total <= 0:
        return {"estimated_cost": float("inf"), "effective_n": 0.,
                "matches": 0, "standard_error": float("inf")}
    estimate = float((weights * logged.terminal_cost).sum() / total)
    effective_n = total ** 2 / float((weights * weights).sum())
    residual = logged.terminal_cost - estimate
    # Conservative descriptive SE; it is NOT a guaranteed confidence bound
    # after adaptive candidate selection.
    stderr = math.sqrt(float((weights.square() * residual.square()).sum())) / total
    return {"estimated_cost": estimate, "effective_n": effective_n,
            "matches": hits, "standard_error": stderr}


def select(logged: LoggedEpisode, *, min_ess: float = 20.,
           complexity_penalty: float = .001):
    if min_ess <= 0:
        raise ValueError("min_ess must be positive")
    candidates = grammar()
    qualified = []
    for program in candidates:
        stats = offpolicy_risk(program, logged)
        if stats["effective_n"] < min_ess:
            continue
        # Risk-averse selection within a *fixed*, preregistered grammar.
        criterion = (stats["estimated_cost"] + 1.96 * stats["standard_error"]
                     + complexity_penalty * program.complexity())
        qualified.append((criterion, program, stats))
    if not qualified:
        raise RuntimeError("insufficient logged coverage for all candidates")
    qualified.sort(key=lambda x: (x[0], x[1].complexity(), repr(x[1])))
    _, best, risk = qualified[0]
    return best, {"grammar_size": len(candidates),
                  "qualified": len(qualified),
                  "selection_estimator": "self-normalized sequential IPS",
                  "selected_ope": risk}


@torch.no_grad()
def evaluate(core, cfg, program, *, seed: int, mechanism: str,
             length: int, n: int, task: str = "majority") -> dict:
    shifted = Cfg(h=cfg.h, length=length, suffix=cfg.suffix,
                  p_fault=cfg.p_fault, sigma=cfg.sigma,
                  lambda_compute=cfg.lambda_compute,
                  policy_overhead=cfg.policy_overhead)
    batch = make_batch(core, shifted,
                       torch.Generator().manual_seed(seed * 8701 + 59),
                       n=n, kind=mechanism, task=task)
    start = time.perf_counter()
    out = run_policy(core, ExecutablePolicy(program), shifted, batch,
                     torch.Generator().manual_seed(seed * 8701 + 60),
                     mode="active", epsilon=0., greedy=True)
    return {"mechanism": mechanism, "task": task, "length": length,
            "examples": n, "mean_total_cost": float(out["loss"].mean()),
            "mean_task_bce": float(out["task_loss"].mean()),
            "mean_compute_charge": float((out["loss"] - out["task_loss"]).mean()),
            "actual_suffix_replays": int(out["spent"].sum()),
            "actual_replay_calls": int(out["replay_calls"]),
            "dense_mac_proxy": out["dense_macs"],
            "execution_seconds": time.perf_counter() - start}


def run(seed: int, *, pretrain: int = 250, n_log: int = 4096,
        n_eval: int = 512) -> dict:
    torch.set_num_threads(1)
    cfg = Cfg(h=12, length=9, suffix=3)
    start = time.perf_counter()
    core, pretrain_accuracy = train_base(seed, cfg, pretrain)
    core.eval()
    for p in core.parameters():
        p.requires_grad_(False)
    # Environment cohorts and action propensities are independent of tested
    # program structure. All logging is under ONE known behavior policy.
    # Training uses these realized terminal outcomes only.
    logs = [collect(core, cfg, seed * 31 + i, n=n_log // 3,
                    mechanism=k) for i, k in
            enumerate(("gaussian", "dropout", "signflip"))]
    logged = LoggedEpisode(
        *(torch.cat([getattr(item, f) for item in logs], dim=0)
          for f in LoggedEpisode.__dataclass_fields__))
    program, diagnostics = select(logged)
    heldout = [evaluate(core, cfg, program, seed=seed * 101 + i,
                        mechanism=k, length=9, n=n_eval)
               for i, k in enumerate(("persistent", "coupled",
                                      "checkpoint", "roll"))]
    heldout.append(evaluate(core, cfg, program, seed=seed * 101 + 11,
                            mechanism="gaussian", length=13, n=n_eval))
    heldout.append(evaluate(core, cfg, program, seed=seed * 101 + 12,
                            mechanism="gaussian", length=9, n=n_eval,
                            task="parity"))
    return {"research": "OWI-DS-002",
            "variant": "A: outcome-only typed symbolic policy synthesis",
            "claim": "baseline only; no differential advantage established",
            "seed": seed, "pretrain_steps": pretrain,
            "pretrain_accuracy": float(pretrain_accuracy),
            "logging_examples": len(logged.probe),
            "selection": diagnostics,
            "extracted_program": {"probe": asdict(program.probe),
                                  "repair": asdict(program.repair)},
            "heldout": heldout,
            "total_wall_seconds": time.perf_counter() - start,
            "compute_warning": "wall and dense MAC proxy only; not a matched "
                               "synthesis-compute comparison or formal proof"}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--pretrain", type=int, default=250)
    p.add_argument("--logging-examples", type=int, default=4096)
    p.add_argument("--eval-examples", type=int, default=512)
    p.add_argument("--output", default="")
    args = p.parse_args()
    row = run(args.seed, pretrain=args.pretrain, n_log=args.logging_examples,
              n_eval=args.eval_examples)
    payload = json.dumps(row, sort_keys=True, indent=2, allow_nan=False)
    if args.output:
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(payload + "\n", encoding="utf8")
    print(payload)


if __name__ == "__main__":
    main()
