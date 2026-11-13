#!/usr/bin/env python3
"""OWI-EC005G: actual chosen-outcome-only contextual three-option learner.

Three options: stop, public-direct, public-probe-and-conditionally-act.
A task-specific transparent tool planner from EC005F still executes actions.
ONLY the initial option decision is learned; the learner does not invent tool
arguments or learn within-episode repairs. Distinguish that from active
introspection in every interpretation.

Training: source-pinned *real* tool environment + distinct terminal checker,
REINFORCE over only the chosen option's scalar terminal utility. Neither
private checker, hidden environment state, gold solutions nor unchosen
counterfactual action outcomes are available to features/optimizer.

Predeclared group separation: train rows 0,2; one other training family
row 3 is a prospective *training-partition holdout* for diagnosis, not a
sealed test-set or genuine language-agent out-of-domain generalization.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from collections import defaultdict
from pathlib import Path

import torch
from torch import nn

from owi_ec005_realtools_heterogeneous_trial import Policy, trial, ARMS, PRICE
from owi_ec005_realtools_randomized import fingerprint

TRAIN_ROWS = (0, 2)
DIAGNOSTIC_ROW = 3
ALL_ROWS = TRAIN_ROWS + (DIAGNOSTIC_ROW,)
FEATURE_DIM = 3
CONTRACT = "OWI-EC005G-REAL-CONTEXTUAL-CHOSEN-OUTCOME/1"


def public_features(public, planner_index):
    """No family ID or string token IDs are features. Only public feasibility.

    The existing public tool planner may form a direct action if the public
    prompt supplies the *required* target identifier. This is a programmatic
    affordance, not a privileged reward label or task-checker field.
    """
    if set(public) != {"messages", "tools"}:
        raise ValueError("unexpected/public-private field contamination")
    direct = Policy(planner_index, public, "direct").next_action()
    probe = Policy(planner_index, public, "probe").next_action()
    if probe["action"] != "call":
        raise ValueError("probe is not supported on this public task")
    enabled = float(direct["action"] == "call")
    return torch.tensor([enabled, 1.0 - enabled, 1.0], dtype=torch.float32)


class ContextualActor(nn.Module):
    def __init__(self):
        super().__init__()
        self.logits = nn.Linear(FEATURE_DIM, len(ARMS))
        # Unbiased initial prior, rather than a seeded preference for any arm.
        nn.init.zeros_(self.logits.weight)
        nn.init.zeros_(self.logits.bias)

    def forward(self, context):
        return self.logits(context)


def sample_option(actor, context, rng, *, epsilon=0.24, greedy=False):
    if not 0 <= epsilon < 1:
        raise ValueError("invalid exploration support")
    weights=torch.softmax(actor(context), dim=0)
    policy=(1-epsilon)*weights + epsilon/len(ARMS)
    probabilities=policy.detach().tolist()
    if greedy:
        action=max(range(len(ARMS)),key=lambda k:probabilities[k])
    else:
        roll=rng.random()
        total=0.0
        action=len(ARMS)-1
        for k,pr in enumerate(probabilities):
            total+=pr
            if roll < total:
                action=k
                break
    chosen=policy[action]
    entropy=-(policy*torch.log(policy)).sum()
    return action, float(chosen.detach()), torch.log(chosen), entropy


def choose_ablation_context(original, kind, other):
    if kind=="normal":
        return original
    if kind=="zero":
        return torch.tensor([0.0, 0.0, 1.0])
    if kind=="shuffled":
        return other
    raise ValueError("unknown ablation")


def load_tasks(input_dir,indices=ALL_ROWS):
    tasks={}
    for i in indices:
        folder=Path(input_dir)/str(i)
        public=json.loads((folder/"public.json").read_text())
        # Family preparation and lock verification are in the CI before this
        # module runs. No checker data is read to derive any feature.
        context=public_features(public,i)
        tasks[i]={"public":public,"context":context,
                  "environment":folder/"environment.json",
                  "verifier":folder/"verifier.json"}
    if 0 in tasks and float(tasks[0]["context"][0])!=0:
        raise ValueError("subscription unexpectedly has a direct target ID")
    if any(float(tasks[i]["context"][0])!=1 for i in (2,3) if i in tasks):
        raise ValueError("direct option unexpectedly unavailable")
    return tasks


def run_option(tasks,index,choice):
    item=tasks[index]
    return trial(item["public"],item["environment"],item["verifier"],
                 index,ARMS[choice])


def evaluate(actor,tasks,*,seed,episodes=2,include_diagnostic=True):
    """Greedy replays of only the selected action; baselines evaluator-only."""
    rng=random.Random(seed+100_003)
    records={}
    for i in ALL_ROWS if include_diagnostic else TRAIN_ROWS:
        chosen_records={}
        original=tasks[i]["context"]
        shuffled=tasks[0 if i!=0 else 2]["context"]
        for mode in ("normal","zero","shuffled"):
            x=choose_ablation_context(original,mode,shuffled)
            choice,probability,_,_=sample_option(
                actor,x,rng,epsilon=0,greedy=True)
            samples=[run_option(tasks,i,choice) for _ in range(episodes)]
            chosen_records[mode]={
                "chosen_arm":ARMS[choice],
                "greedy_probability":probability,
                "mean_reward":round(sum(s["private_terminal_reward"]
                                        for s in samples)/episodes,6),
                "mean_utility":round(sum(s["designed_utility"]
                                         for s in samples)/episodes,6),
                "mean_calls":sum(s["chosen_calls"] for s in samples)/episodes,
                "total_actual_tool_seconds":sum(s["actual_tool_seconds"]
                                                for s in samples),
                "evaluation_episodes":episodes,
            }
        # Fixed-policy comparisons are deliberately AFTER training. No
        # unchosen result is available at policy selection or update time.
        baselines={}
        for arm in ARMS:
            sample=run_option(tasks,i,ARMS.index(arm))
            baselines[arm]={
                "reward":sample["private_terminal_reward"],
                "utility":sample["designed_utility"],
                "calls":sample["chosen_calls"],
            }
        records[str(i)]={
            "group":"train" if i in TRAIN_ROWS else "train_partition_heldout_family",
            "normal_zero_shuffled":chosen_records,
            "post_training_evaluator_only_fixed_baselines":baselines,
        }
    return records


def train(cfg):
    if cfg.episodes<24 or cfg.episodes%len(TRAIN_ROWS):
        raise ValueError("require balanced real training episodes >=24")
    if cfg.eval_episodes<1 or cfg.eval_episodes>5:
        raise ValueError("bounded evaluation episodes 1..5")
    if not 0<cfg.epsilon<1:
        raise ValueError("exploration must give every arm positive support")
    torch.manual_seed(cfg.seed)
    torch.set_num_threads(1)
    actor=ContextualActor()
    before=torch.cat([x.detach().flatten() for x in actor.parameters()])
    opt=torch.optim.Adam(actor.parameters(),lr=cfg.lr)
    rng=random.Random(cfg.seed*4051+47)
    tasks=load_tasks(cfg.input_dir,indices=TRAIN_ROWS)
    baseline=defaultdict(lambda:None)
    trajectories=[]
    for n in range(cfg.episodes):
        index=TRAIN_ROWS[(n+cfg.seed)%len(TRAIN_ROWS)]
        context=tasks[index]["context"]
        choice,propensity,logp,entropy=sample_option(
            actor,context,rng,epsilon=cfg.epsilon)
        # IMPORTANT: exactly one chosen option executed. No unchosen action,
        # checker run, synthetic data or privileged reference enters update.
        outcome=run_option(tasks,index,choice)
        utility=outcome["designed_utility"]
        reference=baseline[index]
        advantage=0.0 if reference is None else utility-reference
        loss=-(advantage*logp) - cfg.entropy_weight*entropy
        opt.zero_grad(set_to_none=True)
        loss.backward()
        nn.utils.clip_grad_norm_(actor.parameters(),5.0)
        opt.step()
        baseline[index]=(utility if reference is None else
                         0.85*reference+0.15*utility)
        trajectories.append({
            "episode":n,"train_row":index,
            "context_features":context.tolist(),
            "selected_option":ARMS[choice],
            "selected_propensity":propensity,
            "realized_private_terminal_reward":outcome["private_terminal_reward"],
            "realized_tool_calls":outcome["chosen_calls"],
            "realized_utility":utility,
            "moving_baseline_before_update":reference,
            "actual_tool_seconds":outcome["actual_tool_seconds"],
            "env_container_seconds":outcome["env_container_seconds"],
            "checker_container_seconds":outcome["checker_container_seconds"],
            "private_fields_in_actor":False,
            "unchosen_arm_evaluated_during_learning":False,
        })
    final=torch.cat([p.detach().flatten() for p in actor.parameters()])
    delta=float((final-before).abs().sum())
    if delta <=1e-7:
        raise RuntimeError("no neural outcome-only update occurred")
    weights_sha=hashlib.sha256(json.dumps(final.tolist(),
                       separators=(",",":")).encode()).hexdigest()
    actor.eval()
    # First access to withheld family public context occurs after optimizer freeze.
    evaluation_tasks=load_tasks(cfg.input_dir,indices=ALL_ROWS)
    results=evaluate(actor,evaluation_tasks,seed=cfg.seed,episodes=cfg.eval_episodes)
    report={
        "contract":CONTRACT,
        "source_train_rows":list(TRAIN_ROWS),
        "prospective_train_partition_holdout_row":DIAGNOSTIC_ROW,
        "heldout_family_used_for_training":False,
        "development_family_used":False,
        "sealed_test_family_used":False,
        "seed":cfg.seed,
        "training_episodes":cfg.episodes,
        "epsilon":cfg.epsilon,
        "minimum_behavior_support":cfg.epsilon/len(ARMS),
        "cost_price":PRICE,
        "cost_units":"designed per-selected-tool-call price, not hardware FLOPs",
        "actor_type":"three-action contextual linear neural bandit",
        "actor_context":"publicly derivable option feasibility only; no family ID",
        "actor_parameter_l1_delta":delta,
        "actor_weights_sha256":weights_sha,
        "training_signal":"REALIZED_CHOSEN_TERMINAL_SCALAR_MINUS_ACTUAL_CHOSEN_TOOL_PRICE",
        "unnchosen_counterfactual_training":"NEVER",
        "control_scope":"FIRST_STAGE_OPTION_ONLY; tool planner is scripted",
        "contextual_generalization":"NOT_ESTABLISHED_WITHOUT_HOLDOUT_ADVANTAGE",
        "per_family_results":results,
        "training_trace":trajectories,
    }
    path=Path(cfg.output)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print("CONTEXTUAL_REAL_OUTCOME_REPLAY",json.dumps({
        k:v for k,v in report.items() if k!="training_trace"},sort_keys=True))
    return report


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",required=True)
    ap.add_argument("--seed",type=int,default=11)
    ap.add_argument("--episodes",type=int,default=96)
    ap.add_argument("--eval-episodes",type=int,default=2)
    ap.add_argument("--epsilon",type=float,default=0.24)
    ap.add_argument("--entropy-weight",type=float,default=0.002)
    ap.add_argument("--lr",type=float,default=0.08)
    ap.add_argument("--output",default="build/owi_ec005_realtools/contextual.json")
    train(ap.parse_args())


if __name__=="__main__":
    main()
