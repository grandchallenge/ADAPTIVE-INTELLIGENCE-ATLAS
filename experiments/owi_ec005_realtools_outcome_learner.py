#!/usr/bin/env python3
"""OWI-EC-005E: chosen-outcome-only learned *option gates* for real tools.

The three learned decisions are whether to start public inspection, whether
to create after inspection, and whether to proceed after recovering the ID.
All tool arguments/continuation procedures are still the transparent, public-
only scripted GoalPolicy. This learns intervention gates, NOT language/tool
planning or general introspection. No checker/fault/skill information enters
the actor. Each training update uses just this episode's actually realized
terminal scalar reward and exact selected tool-call count.

The executable environment and private verifier are separate restricted
no-network Docker children (see goal_policy.py). Never import class_code here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import subprocess
import time
from pathlib import Path

import torch
from torch import nn

from owi_ec005_realtools_goal_policy import (
    GoalPolicy, WORKER, CHECKER, docker_worker_args, receive, one_episode as fixed_episode
)
from owi_ec005_realtools_randomized import IMAGE, call_child, fingerprint

GATES={0:0, 3:1, 5:2}
FEATURE_DIM=11
CONTRACT="OWI-EC005E-REALTOOL-OUTCOME-ONLY-GATES/1"


class Actor(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers=nn.Sequential(
            nn.Linear(FEATURE_DIM,16), nn.Tanh(),
            nn.Linear(16,1),
        )

    def forward(self, state):
        return self.layers(state).flatten()[0]


def features(policy, stage, *, ablation="normal"):
    if stage not in (0,1,2):
        raise ValueError("invalid policy stage")
    state=policy.state  # created exclusively from selected public tool replies
    public_values=[
        float(bool(state.get("location_id"))),
        float(bool(state.get("reporter_id"))),
        float(bool(state.get("prior"))),
        float(bool(state.get("created"))),
        float(bool(state.get("report_id"))),
        float(policy.actions)/8,
        0.0,  # reserved public tool-error statistic; no privileged value
        1.0,
    ]
    if ablation=="zero_feedback":
        # Do not falsify the public planner's actual observations: ablate
        # the neural gate's observation features only, not tool arguments.
        public_values[:5]=[0.0]*5
    elif ablation!="normal":
        raise ValueError("unsupported neural-gate feature ablation")
    x=[float(stage==k) for k in range(3)]+public_values
    assert len(x)==FEATURE_DIM
    return torch.tensor(x,dtype=torch.float32)


def choose(model, x, *, epsilon, greedy, rng):
    """Epsilon-supported stochastic Bernoulli with exact behavior propensity."""
    logit=model(x)
    p=torch.sigmoid(logit)
    mixed=(1-epsilon)*p+epsilon*0.5
    q=float(mixed.detach().item())
    action=int(q>=0.5) if greedy else int(rng.random()<q)
    logp=torch.log(mixed if action else (1-mixed))
    entropy=-(mixed*torch.log(mixed)+(1-mixed)*torch.log(1-mixed))
    return action, q if action else 1-q, logp, entropy


def learned_episode(public, environment, verifier, model, rng, *,
                    epsilon=0.2, greedy=False, ablation="normal",
                    compute_charge=0.01):
    """One truly conditional selected trajectory; checker only after finish."""
    policy=GoalPolicy(public,2)
    started=time.perf_counter()
    proc=subprocess.Popen(
        docker_worker_args(IMAGE,WORKER,environment),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,
        text=True,bufsize=1)
    chosen=[]
    observations=[]
    terminal=None
    logps=[]
    entropies=[]
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("restricted tool-worker privilege mismatch")
        while True:
            if policy.actions in GATES:
                stage=GATES[policy.actions]
                input_vec=features(policy,stage,ablation=ablation)
                action,propensity,logp,entropy=choose(
                    model,input_vec,epsilon=epsilon,greedy=greedy,rng=rng)
                chosen.append({"stage":stage,"proceed":bool(action),
                               "chosen_propensity":propensity,
                               "observed_features_sha256":fingerprint(
                                   [round(float(v),5) for v in input_vec.tolist()])})
                logps.append(logp)
                entropies.append(entropy)
                if action==0:
                    command={"action":"finish"}
                else:
                    command=policy.next_action()
            else:
                command=policy.next_action()
            proc.stdin.write(json.dumps(command,sort_keys=True)+"\n")
            proc.stdin.flush()
            reply=receive(proc)
            if command["action"]=="finish":
                if reply.get("kind")!="private_final_state":
                    raise RuntimeError("worker omitted private terminal state")
                terminal=reply
                break
            if reply.get("kind")!="observation" or reply.get("tool")!=command["tool"]:
                raise RuntimeError("selected observation mismatch")
            policy.observe(reply)
            observations.append({
                "tool":command["tool"],
                "ok":bool(reply["ok"]),
                "result_sha256":fingerprint(reply.get("content","")),
                "elapsed_seconds":float(reply["elapsed_seconds"]),
            })
        proc.stdin.close()
        if proc.wait(timeout=10):
            raise RuntimeError("tool child failed")
    finally:
        if proc.poll() is None:
            proc.kill()
        if proc.stdin and not proc.stdin.closed:
            proc.stdin.close()
        if proc.stdout:
            proc.stdout.close()
    env_elapsed=time.perf_counter()-started
    if terminal is None or terminal.get("tool_calls")!=len(observations):
        raise RuntimeError("invalid terminal call count")
    if not all(isinstance(terminal.get(k),dict)
               for k in ("initial_state","state")):
        raise RuntimeError("invalid terminal envelope")
    checker_input=json.dumps({
        "initial_state":terminal["initial_state"],
        "state":terminal["state"],
    })+"\n"
    outcome,ver_elapsed=call_child(IMAGE,CHECKER,verifier,input_text=checker_input)
    if len(outcome)!=1 or outcome[0].get("contract")!="OWI-EC005-TERMINAL-REWARD/1":
        raise RuntimeError("private checker contract mismatch")
    if outcome[0].get("valid") is not True:
        raise RuntimeError("invalid private evaluator is NOT negative reward")
    score=float(outcome[0]["reward"])
    cost=float(compute_charge)*len(observations)
    total=score-cost
    row={
        "reward":score,"utility":total,"charged_call_cost":cost,
        "real_calls":len(observations),
        "environment_container_seconds":env_elapsed,
        "private_verifier_container_seconds":ver_elapsed,
        "actual_tool_seconds":sum(o["elapsed_seconds"] for o in observations),
        "chosen_gate_actions":chosen,
        "chosen_tool_observation_hashes":[o["result_sha256"] for o in observations],
        "selected_tool_names":[o["tool"] for o in observations],
        "private_check_count":outcome[0]["checks_total"],
        "goal_report_id_from_selected_observation":bool(policy.state["report_id"]),
        "private_state_or_check_in_actor":False,
        "counterfactual_outcomes_used":False,
    }
    return row,logps,entropies


def fixed_baselines(public,environment,verifier,price):
    rows={}
    for arm,name in ((0,"stop"),(1,"read_only"),(2,"scripted_goal")):
        r=fixed_episode(public,environment,verifier,arm)
        rows[name]={
            "reward":r["reward"],
            "utility":round(r["reward"]-price*r["calls"],6),
            "calls":r["calls"],
            "tool_seconds":r["tool_seconds"],
            "environment_container_seconds":r["environment_container_seconds"],
            "verifier_container_seconds":r["verifier_container_seconds"],
        }
    return rows


def run(config):
    public=json.loads(Path(config.public).read_text())
    if set(public)!={"messages","tools","candidate_read_tool"}:
        raise ValueError("unexpected public policy payload")
    if config.episodes<8:
        raise ValueError("training episodes too few")
    if not 0<config.epsilon<1 or not 0<config.call_price<0.1:
        raise ValueError("invalid cost/behavior support")
    torch.set_num_threads(1)
    torch.manual_seed(config.seed)
    rng=random.Random(config.seed*2003+71)
    model=Actor()
    initial_weights=torch.cat([p.detach().flatten() for p in model.parameters()]).clone()
    optimizer=torch.optim.Adam(model.parameters(),lr=config.lr)
    ema=None
    curve=[]
    for t in range(config.episodes):
        eps=config.epsilon
        model.train()
        row,logps,entropies=learned_episode(
            public,config.environment,config.verifier,model,rng,
            epsilon=eps,greedy=False,compute_charge=config.call_price)
        # The only learner reward is the scalar returned at terminal finish.
        reward=row["utility"]
        baseline=reward if ema is None else ema
        advantage=reward-baseline
        if not logps:
            raise AssertionError("missing chosen gate decisions")
        policy_loss=-advantage*torch.stack(logps).sum()
        entropy_bonus=torch.stack(entropies).sum()
        loss=policy_loss-config.entropy_weight*entropy_bonus
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(),5.0)
        optimizer.step()
        ema=reward if ema is None else (0.92*ema+0.08*reward)
        curve.append({
            "episode":t,"chosen_gate_actions":row["chosen_gate_actions"],
            "real_calls":row["real_calls"],
            "realized_terminal_reward":row["reward"],
            "realized_utility":reward,
            "behavior_epsilon":eps,
            "moving_baseline_before_update":baseline,
            "environment_container_seconds":row["environment_container_seconds"],
            "private_verifier_container_seconds":row["private_verifier_container_seconds"],
            "private_state_or_check_in_actor":False,
        })
    model.eval()
    final_weights=torch.cat([p.detach().flatten() for p in model.parameters()])
    delta=float((final_weights-initial_weights).abs().sum())
    if delta<=1e-8:
        raise RuntimeError("no genuine controller learning/update")
    checksum=hashlib.sha256(final_weights.numpy().tobytes()).hexdigest()
    # Held-out *episodes*, same task and same environment family: NOT transfer.
    evaluation={}
    for condition,abl in (("learned_normal","normal"),
                          ("learned_zero_gate_feedback","zero_feedback")):
        rows=[]
        for j in range(config.eval_episodes):
            row,_,_=learned_episode(public,config.environment,config.verifier,
                                   model,rng,epsilon=0,greedy=True,
                                   ablation=abl,compute_charge=config.call_price)
            rows.append(row)
        evaluation[condition]={
            "episodes":len(rows),
            "mean_reward":sum(r["reward"] for r in rows)/len(rows),
            "mean_utility":sum(r["utility"] for r in rows)/len(rows),
            "mean_calls":sum(r["real_calls"] for r in rows)/len(rows),
            "chosen_gate_actions":rows[0]["chosen_gate_actions"],
            "mean_container_seconds":sum(r["environment_container_seconds"]
                                          for r in rows)/len(rows),
        }
    baselines=fixed_baselines(public,config.environment,config.verifier,
                             config.call_price)
    report={
        "contract":CONTRACT,
        "seed":config.seed,
        "pinned_public_task_sha256":fingerprint(public),
        "policy_type":"LEARNED_BERNOULLI_OPTION_GATES_OVER_FIXED_PUBLIC_TOOL_PLANNER",
        "training_signal":"ONLY_REALIZED_CHOSEN_TERMINAL_SCALAR_REWARD_AND_TOOL_COUNT",
        "counterfactual_actions_trained":False,
        "training_episodes":config.episodes,
        "evaluation_episodes_per_ablation":config.eval_episodes,
        "behavior_epsilon":config.epsilon,
        "minimum_bernoulli_action_support":config.epsilon/2,
        "objective_call_price":config.call_price,
        "objective_price_type":"design-weighted call count, NOT hardware compute",
        "model_weight_l1_delta":delta,
        "model_parameter_sha256":checksum,
        "training_curve":curve,
        "evaluations":evaluation,
        "fixed_baselines":baselines,
        "generalization":"NOT_TESTED_SINGLE_SOURCE_TASK",
        "held_out_fault_mechanisms":"NOT_TESTED",
        "zero_gate_feedback_ablation":"neural decision features only; scripted tool planner still uses actual public replies",
        "private_verifier_not_accessible_to_learner":True,
        "scientific_acceptance":"NOT_ESTABLISHED",
    }
    dst=Path(config.output)
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print("REAL_OUTCOME_ONLY_LEARNER",json.dumps({
        k:v for k,v in report.items() if k!="training_curve"},sort_keys=True))
    return report


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--public",required=True)
    ap.add_argument("--environment",required=True)
    ap.add_argument("--verifier",required=True)
    ap.add_argument("--seed",type=int,default=11)
    ap.add_argument("--episodes",type=int,default=72)
    ap.add_argument("--eval-episodes",type=int,default=4)
    ap.add_argument("--epsilon",type=float,default=0.20)
    ap.add_argument("--call-price",type=float,default=0.01)
    ap.add_argument("--lr",type=float,default=0.024)
    ap.add_argument("--entropy-weight",type=float,default=0.002)
    ap.add_argument("--output",default="build/owi_ec005_realtools/learned_gates.json")
    args=ap.parse_args()
    run(args)


if __name__=="__main__":
    main()
