#!/usr/bin/env python3
"""OWI-EC005G2: contextual chosen-only empirical-option-value bandit.

Transparent independent baseline to the REINFORCE neural policy. Estimates
stop/direct/probe utility from ACTUALLY CHOSEN real terminal outcomes only.
No verifier source or unchosen action outcome is used for learning.
Context = a single public affordance: is a direct action well specified by
the public user request and declared tool schema? No family ID/answer key.

Prospective source-family split: train source rows 0 and 2; row 3 withheld
from ALL training and evaluated only after estimates are frozen.
This is diagnostic transfer of a pre-authored tool template, NOT new
language-agent planning, external dev/test transfer, or proof of introspection.

Exploration: independent random action permutation per context every block
of three for 3 blocks (correct conditional probabilities 1/3,1/2,1),
then epsilon-greedy (strict >=epsilon/3 support to each arm).
"""
from __future__ import annotations
import argparse
import json
import random
from collections import defaultdict
from pathlib import Path

from owi_ec005_realtools_contextual_learner import (
    TRAIN_ROWS, DIAGNOSTIC_ROW, ALL_ROWS, load_tasks, run_option
)
from owi_ec005_realtools_heterogeneous_trial import ARMS, PRICE

CONTRACT="OWI-EC005G2-CHOSEN-ONLY-CONTEXTUAL-BANDIT/1"
EXPLORE_ROUNDS=3


def context_key(task):
    context=task.get("context")
    x=context.tolist() if hasattr(context,"tolist") else None
    if x==[1.0,0.0,1.0]:
        return "direct_publicly_available"
    if x==[0.0,1.0,1.0]:
        return "public_lookup_required"
    raise ValueError("unknown or contaminated public action affordance")


class Bandit:
    def __init__(self,epsilon=0.24):
        if not 0<epsilon<1:
            raise ValueError("epsilon must have positive action support")
        self.epsilon=epsilon
        self.n=defaultdict(lambda:[0,0,0])
        self.sum=defaultdict(lambda:[0.0,0.0,0.0])
        self.history=[]
        self._permutations={}

    def choose(self,key,step,rng):
        # At each exploration-block start, permute all three arms
        # independently of their rewards; in-block selection has exact
        # conditional probability 1/(3-position), without off-policy claims.
        if step < EXPLORE_ROUNDS*len(ARMS):
            position=step%len(ARMS)
            if position==0:
                self._permutations[key]=list(range(len(ARMS)))
                rng.shuffle(self._permutations[key])
            action=self._permutations[key][position]
            propensity=1/(len(ARMS)-position)
            mode="without_replacement_exploration"
        else:
            if min(self.n[key]) < EXPLORE_ROUNDS:
                raise AssertionError("incomplete empirical option support")
            best=self.best(key)
            action=(rng.randrange(len(ARMS)) if rng.random()<self.epsilon
                    else best)
            propensity=(1-self.epsilon+self.epsilon/len(ARMS)
                        if action==best else self.epsilon/len(ARMS))
            mode="epsilon_greedy"
        return action,propensity,mode

    def update(self,key,arm,chosen_utility):
        if arm not in range(len(ARMS)) or not isinstance(chosen_utility,(int,float)):
            raise ValueError("invalid chosen scalar reward")
        self.n[key][arm]+=1
        self.sum[key][arm]+=float(chosen_utility)
        self.history.append((key,arm,float(chosen_utility)))

    def means(self,key):
        return [(self.sum[key][j]/self.n[key][j] if self.n[key][j]>0
                 else None) for j in range(len(ARMS))]

    def best(self,key):
        vals=self.means(key)
        if any(x is None for x in vals):
            raise ValueError("cannot exploit without all options observed")
        return max(range(len(ARMS)), key=lambda j:(vals[j],-j))

    def globally_best(self):
        counts=[0]*len(ARMS)
        sums=[0.0]*len(ARMS)
        for _,arm,value in self.history:
            counts[arm]+=1
            sums[arm]+=value
        if not all(counts):
            raise ValueError("global ablation unsupported")
        return max(range(len(ARMS)),key=lambda j:(sums[j]/counts[j],-j))

    def evidence(self):
        result={}
        for key in sorted(self.n):
            result[key]={
                "chosen_sample_counts":self.n[key],
                "chosen_empirical_utilities":self.means(key),
                "frozen_greedy_option":ARMS[self.best(key)],
                "unseen_counterfactual_outcomes_used":False,
            }
        return result


def train(cfg):
    if cfg.episodes<EXPLORE_ROUNDS*len(ARMS)*len(TRAIN_ROWS):
        raise ValueError("too few episodes for complete option exploration")
    if cfg.episodes%len(TRAIN_ROWS):
        raise ValueError("training schedule must balance contexts")
    if cfg.eval_episodes<1 or cfg.eval_episodes>5:
        raise ValueError("invalid evaluation count")
    rng=random.Random(cfg.seed*701+19)
    tasks=load_tasks(cfg.input_dir,indices=TRAIN_ROWS)
    keys={i:context_key(tasks[i]) for i in TRAIN_ROWS}
    if len({keys[i] for i in TRAIN_ROWS})!=len(TRAIN_ROWS):
        raise ValueError("insufficient independent context support")
    learner=Bandit(cfg.epsilon)
    steps=defaultdict(int)
    trajectories=[]
    for t in range(cfg.episodes):
        idx=TRAIN_ROWS[(t+cfg.seed)%len(TRAIN_ROWS)]
        key=keys[idx]
        choice,pr,mode=learner.choose(key,steps[key],rng)
        steps[key]+=1
        # One selected actual real environment + separate terminal verifier.
        # Only the returned realized utility updates this estimator.
        result=run_option(tasks,idx,choice)
        util=float(result["designed_utility"])
        learner.update(key,choice,util)
        trajectories.append({
            "episode":t,
            "source_train_row":idx,
            "public_affordance_context":key,
            "chosen_arm":ARMS[choice],
            "exact_behavior_propensity":pr,
            "exploration_mode":mode,
            "realized_private_reward":result["private_terminal_reward"],
            "realized_chosen_calls":result["chosen_calls"],
            "realized_utility":util,
            "env_container_seconds":result["env_container_seconds"],
            "verifier_container_seconds":result["checker_container_seconds"],
            "actual_tool_seconds":result["actual_tool_seconds"],
            "unexecuted_options_in_training":True,
            "private_state_or_verifier_in_policy":False,
        })
    table=learner.evidence() # frozen after chosen training episodes
    # Withheld-family public task is not opened until after the final update.
    tasks=load_tasks(cfg.input_dir,indices=ALL_ROWS)
    keys={i:context_key(tasks[i]) for i in ALL_ROWS}
    if keys[DIAGNOSTIC_ROW]!=keys[2]:
        raise ValueError("withheld-context transfer class changed")
    global_choice=learner.globally_best()
    evaluations={}
    for idx in ALL_ROWS:
        key=keys[idx]
        alternatives={
            "normal":learner.best(key),
            "shuffled":learner.best(keys[0 if idx!=0 else 2]),
            "zero_context_global":global_choice,
        }
        modes={}
        for label,choice in alternatives.items():
            realized=[run_option(tasks,idx,choice)
                      for _ in range(cfg.eval_episodes)]
            modes[label]={
                "chosen_arm":ARMS[choice],
                "mean_private_reward":round(sum(r["private_terminal_reward"]
                                 for r in realized)/len(realized),6),
                "mean_designed_utility":round(sum(r["designed_utility"]
                                 for r in realized)/len(realized),6),
                "mean_chosen_calls":sum(r["chosen_calls"]
                                 for r in realized)/len(realized),
                "evaluation_episodes":len(realized),
                "sum_tool_seconds":sum(r["actual_tool_seconds"] for r in realized),
            }
        # Prospective baseline evaluator uses all options AFTER learner frozen.
        # It is not sent back to bandit update, no pseudo-counterfactual learning.
        controls={}
        for choice,arm in enumerate(ARMS):
            r=run_option(tasks,idx,choice)
            controls[arm]={"terminal_reward":r["private_terminal_reward"],
                           "designed_utility":r["designed_utility"],
                           "real_calls":r["chosen_calls"]}
        evaluations[str(idx)]={
            "partition":"train" if idx in TRAIN_ROWS
                        else "training_partition_prospective_family_holdout",
            "public_context":key,
            "normal_zero_shuffled":modes,
            "frozen_post_training_evaluator_baselines":controls,
        }
    report={
        "contract":CONTRACT,"seed":cfg.seed,
        "source_train_rows":list(TRAIN_ROWS),
        "prospective_train_partition_holdout_row":DIAGNOSTIC_ROW,
        "training_episodes":cfg.episodes,
        "exploration_blocks_per_context":EXPLORE_ROUNDS,
        "epsilon_after_exploration":cfg.epsilon,
        "minimum_post_exploration_action_support":cfg.epsilon/len(ARMS),
        "zero_support_during_forced_without_replacement_blocks":True,
        "terminal_reward_signal":"REALIZED_CHOSEN_REWARD_MINUS_ACTUAL_CHOSEN_TOOL_CALL_PRICE",
        "price_per_actual_selected_tool_call":PRICE,
        "cost_price_is_physical_FLOP_measurement":False,
        "policy_kind":"EMPIRICAL_CHOSEN_ONLY_CONTEXTUAL_BANDIT_WITH_EXPLICIT_EXPLORATION",
        "source_family_id_in_learner_features":False,
        "private_checker_in_learner":False,
        "unseen_counterfactual_outcomes_in_training":False,
        "heldout_train_partition_family_in_training":False,
        "development_family_evaluated":False,
        "sealed_test_family_evaluated":False,
        "frozen_chosen_option_estimates":table,
        "global_zero_context_option":ARMS[global_choice],
        "evaluation":evaluations,
        "scientific_outcome_only_reflective_control_established":False,
        "limitation":"publicly coded task planners, one task per train family; no unseen tool planner, no dev/test generalization, no post-probe learned adaptive decisions",
        "training_trace":trajectories,
    }
    path=Path(cfg.output)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print("REAL_CONTEXTUAL_BANDIT_EVIDENCE",json.dumps({
        k:v for k,v in report.items() if k!="training_trace"},sort_keys=True))
    return report


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",required=True)
    p.add_argument("--seed",type=int,default=11)
    p.add_argument("--episodes",type=int,default=72)
    p.add_argument("--eval-episodes",type=int,default=2)
    p.add_argument("--epsilon",type=float,default=0.24)
    p.add_argument("--output",default="build/owi_ec005_realtools/contextual_bandit.json")
    train(p.parse_args())


if __name__=="__main__":
    main()
