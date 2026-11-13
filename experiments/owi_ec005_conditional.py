#!/usr/bin/env python3
"""OWI-EC-005: genuinely conditional recurrent intervention environment.

The policy-facing interface consists of corrupted-trajectory telemetry, its
CHOSEN probe result, and finally its CHOSEN repair's delayed task outcome.
No clean reference, fault identity, or unchosen counterfactual is computed
or passed to a policy. Privileged audit metadata remains in EnvBatch only.
"""
from __future__ import annotations

import math
import time
from dataclasses import dataclass

import torch
from torch.nn import functional as F

from owi_ec004_core import Cfg, Core, sample_data


@dataclass
class EnvBatch:
    x: torch.Tensor
    y: torch.Tensor  # withheld until the terminal outcome
    hidden: tuple[torch.Tensor, torch.Tensor]
    checkpoints: tuple[torch.Tensor, torch.Tensor]
    raw: torch.Tensor
    fault_audit: torch.Tensor  # never read by choose/run_policy


def _damage(state, kind, rng, sigma):
    if kind in ("gaussian", "persistent", "coupled", "checkpoint"):
        return state + sigma * torch.randn(state.shape, generator=rng)
    if kind == "small_noise":
        return state + 0.6 * torch.randn(state.shape, generator=rng)
    if kind == "dropout":
        return state * (torch.rand(state.shape, generator=rng) > 0.85).float()
    if kind == "signflip":
        return -state
    if kind == "roll":
        return state.roll(shifts=state.shape[1] // 2, dims=1)
    raise ValueError(kind)


@torch.no_grad()
def make_batch(core: Core, cfg: Cfg, rng: torch.Generator, *, n: int,
               kind: str = "gaussian", task: str = "majority") -> EnvBatch:
    """Build *only* the observed corrupted recurrent path (not clean replays)."""
    if cfg.suffix < 2 or cfg.length <= cfg.suffix:
        raise ValueError("require a nonempty prefix and a suffix of at least two")
    x, y = sample_data(n, cfg, rng)
    if task == "parity":
        y = ((x > 0).sum(dim=1) % 2).float()
    elif task != "majority":
        raise ValueError(task)
    if kind == "coupled":
        weights = [1 - cfg.p_fault, cfg.p_fault / 4, cfg.p_fault / 4, cfg.p_fault / 2]
    else:
        weights = [1 - cfg.p_fault, cfg.p_fault / 2, cfg.p_fault / 2, 0.0]
    fault = torch.multinomial(torch.tensor(weights), n, replacement=True, generator=rng)
    prefix = cfg.length - cfg.suffix
    hidden, checkpoints, logits = [], [], []
    for c, gru in enumerate(core.branches):
        xc = x[:, :, c:c+1]
        _, h0 = gru(xc[:, :prefix])
        check = h0.squeeze(0)
        _, h1 = gru(xc[:, prefix:prefix+1], h0)
        affected = (fault == c+1) | (fault == 3)
        if kind == "checkpoint":
            # Raw task trajectory is untouched; stored recovery checkpoint is bad.
            check = torch.where(affected[:, None],
                                _damage(check, kind, rng, cfg.sigma), check)
            state = h1.squeeze(0)
        else:
            state = torch.where(affected[:, None],
                                _damage(h1.squeeze(0), kind, rng, cfg.sigma),
                                h1.squeeze(0))
        if kind == "persistent" and cfg.suffix >= 3:
            _, mid = gru(xc[:, prefix+1:-1], state.unsqueeze(0))
            state = torch.where(affected[:, None],
                                _damage(mid.squeeze(0), kind, rng, cfg.sigma),
                                mid.squeeze(0))
            _, last = gru(xc[:, -1:], state.unsqueeze(0))
        else:
            _, last = gru(xc[:, prefix+1:], state.unsqueeze(0))
        h = last.squeeze(0)
        hidden.append(h)
        checkpoints.append(check)
        logits.append(core.heads[c](h).squeeze(1))
    return EnvBatch(x, y, tuple(hidden), tuple(checkpoints),
                    torch.stack(logits, dim=1), fault)


def public_telemetry(batch: EnvBatch) -> torch.Tensor:
    """Four permitted features; no labels, fault IDs or clean reference."""
    features = []
    for c in range(2):
        features.extend((torch.tanh(batch.raw[:, c:c+1] / 4),
                         batch.hidden[c].norm(dim=1, keepdim=True)
                         / math.sqrt(batch.hidden[c].shape[1])))
    return torch.cat(features, dim=1).detach()


def _choice(logits, rng, *, epsilon: float, greedy: bool):
    if not 0 <= epsilon <= 1:
        raise ValueError("epsilon outside [0,1]")
    probs = (1 - epsilon) * logits.softmax(dim=-1) + epsilon / logits.shape[1]
    if greedy:
        action = probs.argmax(dim=-1)
    else:
        # CPU multinomial with an independent RNG; no gradient through action.
        action = torch.multinomial(probs.detach(), 1, generator=rng).squeeze(1)
    logp = probs.gather(1, action[:, None]).clamp_min(1e-12).log().squeeze(1)
    entropy = -(probs * probs.clamp_min(1e-12).log()).sum(dim=1)
    return action, logp, entropy, probs.gather(1, action[:, None]).squeeze(1)


class ConditionalReplay:
    """Cache only requested suffixes, with actual indexed GRU execution."""

    def __init__(self, core: Core, batch: EnvBatch, cfg: Cfg):
        self.core, self.batch, self.cfg = core, batch, cfg
        self.cache = [None, None]
        self.ready = [torch.zeros(len(batch.x), dtype=torch.bool) for _ in range(2)]
        self.spent = torch.zeros(len(batch.x), dtype=torch.long)
        self.actual_calls = 0

    @torch.no_grad()
    def _ensure(self, c: int, indices: torch.Tensor):
        missing = indices[~self.ready[c][indices]]
        if missing.numel() == 0:
            return
        if self.cache[c] is None:
            self.cache[c] = torch.empty_like(self.batch.hidden[c])
        prefix = self.cfg.length - self.cfg.suffix
        x = self.batch.x[missing, prefix:, c:c+1]
        initial = self.batch.checkpoints[c][missing].unsqueeze(0)
        _, final = self.core.branches[c](x, initial)
        self.cache[c][missing] = final.squeeze(0)
        self.ready[c][missing] = True
        self.spent[missing] += 1
        self.actual_calls += 1

    def probe(self, probes: torch.Tensor) -> torch.Tensor:
        residuals = torch.zeros(len(probes), 2)
        for c in range(2):
            idx = (probes == c+1).nonzero(as_tuple=True)[0]
            self._ensure(c, idx)
            if idx.numel():
                residuals[idx, c] = ((self.cache[c][idx] -
                                      self.batch.hidden[c][idx]).square()
                                     .mean(dim=1) + 1e-8).sqrt()
        return residuals

    def repair(self, actions: torch.Tensor) -> torch.Tensor:
        final = self.batch.raw.clone()
        for c in range(2):
            idx = ((actions & (1 << c)) != 0).nonzero(as_tuple=True)[0]
            self._ensure(c, idx)
            if idx.numel():
                with torch.no_grad():
                    final[idx, c] = self.core.heads[c](self.cache[c][idx]).squeeze(1)
        return final


def dense_macs(cfg: Cfg, n: int, spent: int, *, controller: bool) -> dict:
    """Count executed dense GRU/head and controller MACs; NOT GPU profiler FLOPs."""
    gru_step = 3 * cfg.h * (cfg.h + 1)
    base = n * (2 * cfg.length * gru_step + 2 * cfg.h)
    replay = spent * (cfg.suffix * gru_step + cfg.h)
    # First MLP: 4 -> 20 -> 3; second MLP: 8 -> 20 -> 4.
    policy = n * (4 * 20 + 20 * 3 + 8 * 20 + 20 * 4) if controller else 0
    return {"base": base, "conditional_replay": replay, "controller": policy,
            "total": base + replay + policy}


def run_policy(core: Core, policy, cfg: Cfg, batch: EnvBatch,
               rng: torch.Generator, *, mode="active", epsilon=0.05,
               greedy=False, ablation="normal") -> dict:
    """Terminal reward is provided only after both decisions; no alternatives."""
    if mode not in ("active", "passive", "fixed_both"):
        raise ValueError(mode)
    if ablation not in ("normal", "zero_probe", "shuffle_probe"):
        raise ValueError(ablation)
    started = time.perf_counter()
    if mode == "fixed_both":
        probes = torch.zeros(len(batch.x), dtype=torch.long)
        repairs = torch.full_like(probes, 3)
        lp1 = lp2 = ent1 = ent2 = None
        propensity1 = propensity2 = None
    else:
        z = public_telemetry(batch)
        # Also execute the first network for passive: matched controller MACs.
        first_logits = policy.probe_actor(z)
        if mode == "active":
            probes, lp1, ent1, propensity1 = _choice(
                first_logits, rng, epsilon=epsilon, greedy=greedy)
        else:
            probes = torch.zeros(len(batch.x), dtype=torch.long)
            lp1 = ent1 = propensity1 = None
    replay = ConditionalReplay(core, batch, cfg)
    signal = replay.probe(probes)
    if mode != "fixed_both":
        if ablation == "zero_probe":
            signal.zero_()
        elif ablation == "shuffle_probe":
            signal = signal[torch.randperm(len(signal), generator=rng)]
        mask = torch.stack((probes == 1, probes == 2), dim=1).float()
        post = torch.cat((z, mask, signal), dim=1)
        repairs, lp2, ent2, propensity2 = _choice(
            policy.repair_actor(post), rng, epsilon=epsilon, greedy=greedy)
    with torch.no_grad():
        final = replay.repair(repairs)
        # Target accessed only at this terminal step.
        task_loss = F.binary_cross_entropy_with_logits(
            final, batch.y, reduction="none").mean(dim=1)
        charge = cfg.lambda_compute * replay.spent.float()
        if mode != "fixed_both":
            charge += cfg.policy_overhead
        total = task_loss + charge
    elapsed = time.perf_counter() - started
    return {"loss": total, "task_loss": task_loss, "spent": replay.spent,
            "probe": probes, "repair": repairs,
            "logp_probe": lp1, "logp_repair": lp2,
            "entropy_probe": ent1, "entropy_repair": ent2,
            "propensity_probe": propensity1, "propensity_repair": propensity2,
            "state": z if mode != "fixed_both" else None,
            "post": post if mode != "fixed_both" else None,
            "replay_calls": replay.actual_calls,
            "dense_macs": dense_macs(cfg, len(batch.x), int(replay.spent.sum()),
                                     controller=mode != "fixed_both"),
            "elapsed_seconds": elapsed}
