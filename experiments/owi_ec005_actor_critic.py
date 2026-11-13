#!/usr/bin/env python3
"""OWI-EC-005 frozen-GRU, outcome-only sequential actor-critic experiment.

The controller receives no fault ID, no clean target for introspection, and no
unchosen intervention outcomes. It receives a terminal scalar task+compute loss
after its two selected decisions. Behavior probabilities retain epsilon support.
"""
from __future__ import annotations

import argparse
import json
import math
import resource
import statistics
import time
from pathlib import Path

import torch
from torch import nn

from owi_ec004_core import Cfg, Core
from owi_ec004_train import train_base
from owi_ec005_conditional import make_batch, run_policy
from owi_ec005_identify import identify_probe_value
from owi_ec005_privileged import privileged_oracle


class Controller(nn.Module):
    def __init__(self):
        super().__init__()
        self.probe_actor = nn.Sequential(nn.Linear(4, 20), nn.Tanh(),
                                         nn.Linear(20, 3))
        self.repair_actor = nn.Sequential(nn.Linear(8, 20), nn.Tanh(),
                                          nn.Linear(20, 4))
        self.probe_value = nn.Sequential(nn.Linear(4, 20), nn.Tanh(),
                                         nn.Linear(20, 1))
        self.repair_value = nn.Sequential(nn.Linear(8, 20), nn.Tanh(),
                                          nn.Linear(20, 1))


def fit(core, cfg, seed, mode, steps, *, batch_size=192, log=None):
    torch.manual_seed(seed + (500 if mode == "active" else 900))
    controller = Controller()
    optimizer = torch.optim.Adam(controller.parameters(), lr=0.0015)
    # Separate exogenous and policy RNGs: decisions cannot change the next
    # environment draw, and evaluation cohorts remain paired across policies.
    env_rng = torch.Generator().manual_seed(seed * 1000 + 511)
    actor_rng = torch.Generator().manual_seed(seed * 1000 + 512)
    records = []
    sampled_trajectories = []  # logged chosen actions only, never audit labels
    core.eval()
    for p in core.parameters():
        p.requires_grad_(False)
    for step in range(steps):
        # Never expose the privileged fault_audit field to the optimizer.
        batch = make_batch(core, cfg, env_rng, n=batch_size)
        epsilon = 0.35 if step < steps // 3 else (0.15 if step < 2 * steps // 3 else 0.05)
        out = run_policy(core, controller, cfg, batch, actor_rng,
                         mode=mode, epsilon=epsilon, greedy=False)
        target = out["loss"].detach()
        v_repair = controller.repair_value(out["post"]).squeeze(1)
        advantage_repair = target - v_repair.detach()
        actor_loss = (advantage_repair * out["logp_repair"]).mean()
        critic_loss = (v_repair - target).square().mean()
        ent = out["entropy_repair"].mean()
        if mode == "active":
            v_probe = controller.probe_value(out["state"]).squeeze(1)
            actor_loss = actor_loss + ((target - v_probe.detach()) *
                                       out["logp_probe"]).mean()
            critic_loss = critic_loss + (v_probe - target).square().mean()
            ent = ent + out["entropy_probe"].mean()
        entropy_weight = 0.012 if step < 2 * steps // 3 else 0.004
        loss = actor_loss + 0.5 * critic_loss - entropy_weight * ent
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        nn.utils.clip_grad_norm_(controller.parameters(), 3.0)
        optimizer.step()
        if (step + 1) % max(1, steps // 20) == 0:
            for j in range(min(8, batch_size)):
                sampled_trajectories.append({
                    "step": step + 1, "position": j,
                    "probe": int(out["probe"][j]),
                    "repair": int(out["repair"][j]),
                    "probe_propensity": (None if mode == "passive" else
                                          float(out["propensity_probe"][j].detach())),
                    "repair_propensity": float(out["propensity_repair"][j].detach()),
                    "realized_terminal_loss": float(target[j]),
                    "realized_replays": int(out["spent"][j]),
                    "delayed_outcome_after_decisions": 2,
                })
        if (step + 1) % max(1, steps // 10) == 0:
            row = {
                "step": step + 1,
                "outcome_only_cost": float(target.mean()),
                "probe_rate": float((out["probe"] != 0).float().mean()),
                "repair_rate": float((out["repair"] != 0).float().mean()),
                "abstain_both_rate": float(((out["probe"] == 0) &
                                           (out["repair"] == 0)).float().mean()),
                "behavior_probe_propensity": (None if mode == "passive"
                    else float(out["propensity_probe"].detach().mean())), 
                "behavior_repair_propensity": float(out["propensity_repair"].detach().mean()),
                "behavior_epsilon": epsilon,
            }
            records.append(row)
            if log:
                log({f"{mode}/{k}": v for k, v in row.items() if v is not None},
                    step=step + 1)
    return controller, records, sampled_trajectories


@torch.no_grad()
def evaluate(core, controller, cfg, *, seed, mode, kind, length, n,
             task="majority", ablation="normal"):
    eval_cfg = Cfg(h=cfg.h, suffix=cfg.suffix, length=length,
                   p_fault=cfg.p_fault, sigma=cfg.sigma,
                   lambda_compute=cfg.lambda_compute,
                   policy_overhead=cfg.policy_overhead)
    # Independently pinned environmental samples, identical across policies.
    env_rng = torch.Generator().manual_seed(seed * 100000 +
                                            1234 + 17 * length +
                                            {"gaussian": 1, "dropout": 2,
                                             "signflip": 3, "roll": 4,
                                             "small_noise": 5, "persistent": 6,
                                             "coupled": 7, "checkpoint": 8}[kind] +
                                            (300 if task == "parity" else 0))
    action_rng = torch.Generator().manual_seed(seed * 100000 + 808)
    core.eval()
    if controller is not None:
        controller.eval()
    batch = make_batch(core, eval_cfg, env_rng, n=n, kind=kind, task=task)
    out = run_policy(core, controller, eval_cfg, batch, action_rng,
                     mode=mode, epsilon=0, greedy=True, ablation=ablation)
    # Audit labels below are NEVER consulted by policy/train gradients.
    fault = batch.fault_audit
    clean = fault == 0
    return {
        "n_examples": n,
        "objective": float(out["loss"].mean()),
        "task_loss": float(out["task_loss"].mean()),
        "compute_charge": float((out["loss"] - out["task_loss"]).mean()),
        "probe_rate": float((out["probe"] != 0).float().mean()),
        "repair_rate": float((out["repair"] != 0).float().mean()),
        "abstain_both_rate": float(((out["probe"] == 0) &
                                    (out["repair"] == 0)).float().mean()),
        "clean_no_probe_rate": float((out["probe"][clean] == 0).float().mean())
                                    if clean.any() else None,
        "clean_no_repair_rate": float((out["repair"][clean] == 0).float().mean())
                                    if clean.any() else None,
        "replay_per_example": float(out["spent"].float().mean()),
        "realized_gru_replay_calls": out["replay_calls"],
        "executed_dense_macs": out["dense_macs"],
        "elapsed_seconds_batch": out["elapsed_seconds"],
        "peak_process_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "chosen_repair_propensity_mean":
            None if mode == "fixed_both" else float(out["propensity_repair"].mean()),
        "note": "MACs count executed dense multiplies, not hardware FLOP counters; "
                "RSS is process high-water mark; timing includes Python dispatch",
    }


def prepare_core(seed, cfg, steps, folder):
    path = folder / f"seed{seed}_core.pt"
    if path.exists():
        data = torch.load(path, map_location="cpu", weights_only=True)
        if data.get("steps") != steps:
            raise ValueError("cached core pretraining step count mismatch")
        core = Core(cfg.h)
        core.load_state_dict(data["core"])
        return core, data["accuracy"]
    core, accuracy = train_base(seed, cfg, steps)
    torch.save({"core": core.state_dict(), "accuracy": accuracy, "steps": steps}, path)
    return core, accuracy


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--stage", choices=["train", "evaluate", "all"], default="all")
    ap.add_argument("--mode", choices=["active", "passive", "both"], default="both")
    ap.add_argument("--pretrain", type=int, default=250)
    ap.add_argument("--steps", type=int, default=1200)
    ap.add_argument("--batch", type=int, default=192)
    ap.add_argument("--eval", type=int, default=2048)
    ap.add_argument("--folder", default="build/owi_ec005")
    ap.add_argument("--wandb-project", default="")
    args = ap.parse_args()
    torch.set_num_threads(1)
    cfg = Cfg(batch=args.batch, pretrain=args.pretrain)
    folder = Path(args.folder)
    folder.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    core, accuracy = prepare_core(args.seed, cfg, args.pretrain, folder)
    wb = None
    if args.wandb_project:
        import wandb  # optional dependency; never required for reproducible CI
        wb = wandb.init(project=args.wandb_project,
                        name=f"owi-ec005-{args.seed}", config=vars(args))
    modes = ["active", "passive"] if args.mode == "both" else [args.mode]
    if args.stage in ("train", "all"):
        for mode in modes:
            controller, curve, trace = fit(core, cfg, args.seed, mode, args.steps,
                                    batch_size=args.batch,
                                    log=(wb.log if wb else None))
            torch.save({"controller": controller.state_dict(), "curve": curve,
                        "chosen_behavior_trace": trace,
                        "seed": args.seed, "mode": mode, "steps": args.steps},
                       folder / f"seed{args.seed}_{mode}.pt")
    if args.stage in ("evaluate", "all"):
        results = {}
        trace_evidence = {}
        for mode in [*modes, "fixed_both"]:
            controller = None
            if mode != "fixed_both":
                data = torch.load(folder / f"seed{args.seed}_{mode}.pt",
                                  map_location="cpu", weights_only=True)
                controller = Controller()
                controller.load_state_dict(data["controller"])
                trace_evidence[mode] = data["chosen_behavior_trace"]
            results[mode] = {}
            for kind in ("gaussian", "dropout", "signflip", "roll", "small_noise",
                         "persistent", "coupled", "checkpoint"):
                results[mode][kind] = evaluate(
                    core, controller, cfg, seed=args.seed, mode=mode,
                    kind=kind, length=9, n=args.eval)
            # Shift length and task semantics, without retraining the task core.
            results[mode]["length13"] = evaluate(
                core, controller, cfg, seed=args.seed, mode=mode, kind="gaussian",
                length=13, n=args.eval)
            results[mode]["parity"] = evaluate(
                core, controller, cfg, seed=args.seed, mode=mode, kind="gaussian",
                length=9, n=args.eval, task="parity")
            if mode == "active":
                for ablation in ("zero_probe", "shuffle_probe"):
                    results[mode][ablation] = evaluate(
                        core, controller, cfg, seed=args.seed, mode=mode,
                        kind="gaussian", length=9, n=args.eval,
                        ablation=ablation)
        if "active" in results:
            actor = Controller()
            saved = torch.load(folder / f"seed{args.seed}_active.pt",
                               map_location="cpu", weights_only=True)
            actor.load_state_dict(saved["controller"])
            results["active"]["randomized_probe_identification"] = identify_probe_value(
                core, actor, cfg, args.seed, batches=6, n=min(args.eval, 256))
        results["privileged_oracle"] = privileged_oracle(
            core, cfg, args.seed, kind="gaussian", length=9, n=args.eval)
        record = {
            "research": "OWI-EC-005", "seed": args.seed,
            "core_clean_accuracy": accuracy,
            "training_observation": "only chosen sequential interventions and terminal loss",
            "counterfactual_training": False,
            "probe_behavior_support_floor": 0.05 / 3,
            "repair_behavior_support_floor": 0.05 / 4,
            "off_policy_correction": "none (updates use current mixture behavior policy)",
            "controller_core_joint_training": False,
            "results": results, "chosen_behavior_trace": trace_evidence,
            "elapsed_seconds": time.monotonic() - started,
        }
        dest = folder / f"seed{args.seed}_results.json"
        dest.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
        print("EC005_RESULT", str(dest), "gaussian",
              {k: round(v["gaussian"]["objective"], 6)
               for k, v in results.items() if "gaussian" in v}, flush=True)
    if wb:
        wb.finish()


if __name__ == "__main__":
    main()
