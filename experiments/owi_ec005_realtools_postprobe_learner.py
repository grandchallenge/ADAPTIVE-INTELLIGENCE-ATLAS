#!/usr/bin/env python3
"""OWI-EC005H: genuine post-probe, chosen-only, two-action real-tool learner.

The learner does NOT receive scenario names or hidden states. It first pays
for a REAL selected check_user_account_status tool call in the pinned external
class, then acts on the actually observed account_status. The learner chooses
whether to update (one real mutation) or stop (no mutation). The two options
are trained only from a scalar, independent, POST-TERMINAL source-locked
private checker outcome and the actual chosen call count.

The synthetic environment variants are explicit single-field initial-state
interventions, not authentic unseen upstream dataset records. No training on
closed-state variant: it's an unsupported-mechanism abstention diagnostic.
This demonstrates bounded post-probe option learning, not a learned semantic
tool planner, spontaneous self-introspection, or an overall task-compute gain.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import random
import re
import subprocess
import time
from collections import defaultdict
from pathlib import Path

from owi_ec005_realtools_heterogeneous_trial import PRICE, user_text, trial as no_probe_trial
from owi_ec005_realtools_goal_policy import (
    docker_worker_args, receive, WORKER, CHECKER, unpack_reply
)
from owi_ec005_realtools_randomized import IMAGE, call_child, fingerprint

CONTRACT="OWI-EC005H-REAL-POSTPROBE-CHOSEN-OUTCOME/1"
STATUS=("suspended","active")
UNKNOWN="closed"
ACTIONS=("stop","update")
FORCED_ROUNDS=4
USER_ID="USR002"

def public_preflight(public):
    if not isinstance(public,dict) or set(public)!={"messages","tools"}:
        raise ValueError("policy public-only boundary")
    prompt=user_text(public)
    if not re.search(r"For user\s+USR002\b",prompt):
        raise ValueError("public task target drift")
    if not re.search(r'account_status from .suspended. to .active.',prompt):
        raise ValueError("public task intent drift")
    tools={t["name"]:t["parameters"] for t in public["tools"]}
    if (set(tools.get("check_user_account_status",{}).get("required",[]))
            !={"user_id"} or
        set(tools.get("update_user_account_status",{}).get("required",[]))
            !={"user_id","new_status"}):
        raise ValueError("public advertised tool contract drift")
    return True

def read_observed_status(reply):
    if (reply.get("kind")!="observation" or
            reply.get("tool")!="check_user_account_status" or
            reply.get("ok") is not True or reply.get("truncated") is True):
        return None
    parsed=unpack_reply(reply.get("content",""))
    data=parsed.get("data")
    if (parsed.get("success") is not True or not isinstance(data,dict) or
            data.get("_id")!=USER_ID):
        return None
    state=data.get("account_status")
    return state if state in STATUS+(UNKNOWN,) else None

def episode(folder,decision,*,mode="learned"):
    """Execute only one selected intervention after one actual public probe.

    decision(status) receives only the real public observation; hidden
    scenario status never passed. A separate checker runs on terminal state.
    """
    public=json.loads((folder/"public.json").read_text())
    public_preflight(public)
    proc=subprocess.Popen(
        docker_worker_args(IMAGE,WORKER,folder/"environment.json"),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,text=True,bufsize=1)
    tools=[]
    terminal=None
    observed=None
    chosen=None
    chosen_pr=None
    started=time.perf_counter()
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("jail privilege/ready mismatch")
        probe={"action":"call","tool":"check_user_account_status",
               "arguments":{"user_id":USER_ID}}
        proc.stdin.write(json.dumps(probe)+"\n")
        proc.stdin.flush()
        reply=receive(proc)
        observed=read_observed_status(reply)
        tools.append({
            "name":probe["tool"],
            "observation_sha256":fingerprint(reply.get("content","")),
            "elapsed_seconds":float(reply.get("elapsed_seconds",0)),
            "public_probe_valid":observed is not None,
        })
        if observed is None:
            # Unsupported/invalid probe: fail closed without mutation.
            chosen,chosen_pr="stop",1.0
        else:
            chosen,chosen_pr=decision(observed)
            if chosen not in ACTIONS or not 0<chosen_pr<=1:
                raise ValueError("invalid chosen action/propensity")
            # For unseen/unsupported account states, no mutation may be
            # authorized until a separately trained/approved mechanism exists.
            if observed not in STATUS and chosen!="stop":
                raise ValueError("unsupported status modification denied")
        if chosen=="update":
            update={"action":"call","tool":"update_user_account_status",
                    "arguments":{"user_id":USER_ID,"new_status":"active"}}
            proc.stdin.write(json.dumps(update)+"\n")
            proc.stdin.flush()
            reply2=receive(proc)
            if reply2.get("kind")!="observation" or reply2.get("tool")!=update["tool"]:
                raise RuntimeError("real update result missing")
            tools.append({
                "name":update["tool"],
                "observation_sha256":fingerprint(reply2.get("content","")),
                "elapsed_seconds":float(reply2.get("elapsed_seconds",0)),
                "public_probe_valid":None,
            })
        proc.stdin.write('{"action":"finish"}\n')
        proc.stdin.flush()
        terminal=receive(proc)
        if terminal.get("kind")!="private_final_state":
            raise RuntimeError("terminal state did not arrive privately")
        proc.stdin.close()
        if proc.wait(timeout=10)!=0:
            raise RuntimeError("tool worker exit failure")
    finally:
        if proc.poll() is None:
            proc.kill()
        if proc.stdin and not proc.stdin.closed:
            proc.stdin.close()
        if proc.stdout:
            proc.stdout.close()
    elapsed=time.perf_counter()-started
    if (terminal is None or terminal.get("tool_calls")!=len(tools) or
            not all(isinstance(terminal.get(k),dict)
                    for k in ("initial_state","state"))):
        raise RuntimeError("malformed privileged terminal envelope")
    # Trust boundary: private state is passed directly to the checker AFTER
    # action selection and is not inspected/recorded by the actor.
    checked,verify_time=call_child(IMAGE,CHECKER,folder/"verifier.json",
          input_text=json.dumps({"initial_state":terminal["initial_state"],
                                 "state":terminal["state"]})+"\n")
    if (len(checked)!=1 or
        checked[0].get("contract")!="OWI-EC005-TERMINAL-REWARD/1" or
        checked[0].get("valid") is not True):
        raise RuntimeError("independent terminal checker invalid")
    score=float(checked[0]["reward"])
    return {
        "observed_public_status":observed,
        "selected_second_stage_action":chosen,
        "chosen_action_propensity":chosen_pr,
        "private_terminal_reward":score,
        "private_checker_count":checked[0]["checks_total"],
        "private_checks_passed":checked[0]["checks_passed_if_valid"],
        "actual_selected_calls":len(tools),
        "designed_utility":round(score-PRICE*len(tools),6),
        "tool_name_sequence":[t["name"] for t in tools],
        "hashed_selected_observations":[t["observation_sha256"] for t in tools],
        "actual_tool_seconds":sum(t["elapsed_seconds"] for t in tools),
        "env_container_wall_seconds":elapsed,
        "checker_container_wall_seconds":verify_time,
        "peak_worker_rss_kib":terminal.get("peak_rss_kib"),
        "third_party_code_in_jail":True,
        "private_state_or_check_in_actor":False,
        "unchosen_action_executed_for_training":False,
        "execution_mode":mode,
    }


class PostProbeBandit:
    def __init__(self,epsilon=0.2):
        if not 0<epsilon<1:
            raise ValueError("epsilon missing")
        self.epsilon=epsilon
        self.count=defaultdict(lambda:[0,0])
        self.total=defaultdict(lambda:[0.,0.])
        self.history=[]
        self.permutations={}

    def choice(self,observed,rng):
        if observed not in STATUS:
            return "stop",1., "unsupported_fail_closed"
        n=sum(self.count[observed])
        if n<2*FORCED_ROUNDS:
            p=n%2
            if p==0:
                perm=[0,1]
                rng.shuffle(perm)
                self.permutations[observed]=perm
            choice=self.permutations[observed][p]
            probability=1/(2-p)
            mode="context_specific_without_replacement"
        else:
            best=self.best(observed)
            choice=(rng.randrange(2) if rng.random()<self.epsilon else best)
            probability=(1-self.epsilon+self.epsilon/2
                         if choice==best else self.epsilon/2)
            mode="epsilon_greedy"
        return ACTIONS[choice],probability,mode

    def update(self,observed,action,utility):
        if observed not in STATUS or action not in ACTIONS:
            raise ValueError("invalid chosen observation/action update")
        ix=ACTIONS.index(action)
        self.count[observed][ix]+=1
        self.total[observed][ix]+=float(utility)
        self.history.append((observed,action,float(utility)))

    def means(self,observed):
        return [self.total[observed][i]/n if n else None
                for i,n in enumerate(self.count[observed])]

    def best(self,observed):
        means=self.means(observed)
        if any(v is None for v in means):
            raise ValueError("missing selected option support")
        return 0 if means[0]>=means[1] else 1

    def pooled_best(self):
        sums=[0.,0.]
        counts=[0,0]
        for _,action,utility in self.history:
            i=ACTIONS.index(action)
            sums[i]+=utility
            counts[i]+=1
        if not all(counts):
            raise ValueError("pooled baseline lacks selected support")
        return 0 if sums[0]/counts[0]>=sums[1]/counts[1] else 1

    def evidence(self):
        return {status:{
            "chosen_counts":self.count[status],
            "chosen_empirical_designed_utility":self.means(status),
            "frozen_action":ACTIONS[self.best(status)],
        } for status in STATUS}


def train(cfg):
    if cfg.episodes<4*FORCED_ROUNDS or cfg.episodes%2:
        raise ValueError("balanced and supported training episode count")
    if cfg.eval_episodes<1 or cfg.eval_episodes>5:
        raise ValueError("evaluation count 1..5 required")
    root=Path(cfg.input_dir)
    manifest=json.loads((root/"variant_manifest.json").read_text())
    if (manifest.get("contract")!="OWI-EC005H-CONTROLLED-SOURCE-CLASS-VARIANTS/1"
        or manifest.get("train_variants")!=list(STATUS)
        or manifest.get("holdout_mechanism_variant")!=UNKNOWN):
        raise ValueError("controlled variant provenance drift")
    rng=random.Random(10007*cfg.seed+23)
    bandit=PostProbeBandit(cfg.epsilon)
    scenario_schedule=list(STATUS)*(cfg.episodes//2)
    rng.shuffle(scenario_schedule)
    trace=[]
    for t,scenario in enumerate(scenario_schedule):
        selected={}
        def choose(status):
            action,pr,phase=bandit.choice(status,rng)
            selected["phase"]=phase
            return action,pr
        result=episode(root/scenario,choose,mode="chosen_only_training")
        if result["observed_public_status"]!=scenario:
            # Host integrity check only, not a learner feature.
            raise RuntimeError("source class public observation scenario mismatch")
        bandit.update(result["observed_public_status"],
                      result["selected_second_stage_action"],
                      result["designed_utility"])
        trace.append({
            "episode":t,
            "host_control_scenario":scenario,
            "actual_public_observation":result["observed_public_status"],
            "chosen_action":result["selected_second_stage_action"],
            "chosen_propensity":result["chosen_action_propensity"],
            "exploration_phase":selected["phase"],
            "realized_terminal_private_reward":result["private_terminal_reward"],
            "realized_tool_calls":result["actual_selected_calls"],
            "realized_designed_utility":result["designed_utility"],
            "actual_tool_seconds":result["actual_tool_seconds"],
            "env_container_seconds":result["env_container_wall_seconds"],
            "checker_container_seconds":result["checker_container_wall_seconds"],
            "private_state_or_check_in_actor":False,
            "unexecuted_action_result_observed":False,
        })
    frozen=bandit.evidence()
    pooled=ACTIONS[bandit.pooled_best()]
    results={}
    for scenario in STATUS+(UNKNOWN,):
        modes={}
        for label in ("normal","flipped_observation","zero_feedback_pooled",
                      "always_mutate","always_abstain","public_rule"):
            if label=="normal":
                action=(frozen[scenario]["frozen_action"] if scenario in STATUS
                        else "stop")
            elif label=="flipped_observation":
                flipped=(STATUS[1-STATUS.index(scenario)]
                         if scenario in STATUS else UNKNOWN)
                action=(frozen[flipped]["frozen_action"] if flipped in STATUS
                        else "stop")
            elif label=="zero_feedback_pooled":
                action=pooled if scenario in STATUS else "stop"
            elif label=="always_mutate":
                action="update" if scenario in STATUS else "stop"
            elif label=="always_abstain":
                action="stop"
            else:
                action="update" if scenario=="suspended" else "stop"
            samples=[episode(root/scenario,lambda obs,a=action:(a,1.),
                             mode="posttraining_evaluation")
                     for _ in range(cfg.eval_episodes)]
            modes[label]={
                "selected_second_stage_action":action,
                "mean_terminal_reward":round(sum(x["private_terminal_reward"]
                                              for x in samples)/len(samples),6),
                "mean_designed_utility":round(sum(x["designed_utility"]
                                              for x in samples)/len(samples),6),
                "mean_actual_tool_calls":sum(x["actual_selected_calls"]
                                              for x in samples)/len(samples),
                "mean_env_container_wall_seconds":sum(x["env_container_wall_seconds"]
                                              for x in samples)/len(samples),
                "mean_checker_container_wall_seconds":sum(x["checker_container_wall_seconds"]
                                              for x in samples)/len(samples),
                "peak_worker_rss_kib":max(x["peak_worker_rss_kib"] for x in samples),
                "episodes":len(samples),
            }
        # Stronger option-stage comparator: update WITHOUT paying for the
        # information-gathering call. These live fixed controls run strictly
        # AFTER freezing. They are NOT counterfactual training labels.
        public=json.loads((root/scenario/"public.json").read_text())
        no_probe={}
        for arm in ("direct","stop"):
            baselines=[no_probe_trial(
                public,root/scenario/"environment.json",
                root/scenario/"verifier.json",2,arm)
                for _ in range(cfg.eval_episodes)]
            no_probe[arm]={
                "mean_terminal_reward":round(sum(x["private_terminal_reward"]
                                      for x in baselines)/len(baselines),6),
                "mean_designed_utility":round(sum(x["designed_utility"]
                                      for x in baselines)/len(baselines),6),
                "mean_actual_tool_calls":sum(x["chosen_calls"]
                                      for x in baselines)/len(baselines),
                "mean_env_container_wall_seconds":sum(x["env_container_seconds"]
                                      for x in baselines)/len(baselines),
                "mean_checker_container_wall_seconds":sum(x["checker_container_seconds"]
                                      for x in baselines)/len(baselines),
                "evaluation_episodes":len(baselines),
            }
        results[scenario]={"one_probe_then_decide":modes,
                           "posttraining_no_probe_fixed_controls":no_probe}
    report={
        "contract":CONTRACT,
        "seed":cfg.seed,
        "source_status":"PINNED_REAL_CLASS_AND_ORIGINAL_PRIVATE_CHECKER; INITIAL_STATE_CONTROLLED",
        "variant_manifest":manifest,
        "training_statuses":list(STATUS),
        "withheld_status":UNKNOWN,
        "training_episodes":cfg.episodes,
        "epsilon":cfg.epsilon,
        "training_chooses_only_after_actual_selected_public_probe":True,
        "learner_inputs":["actual_public_probe_response_status"],
        "learner_training_signal":"CHOSEN_REAL_TERMINAL_SCALAR_MINUS_CHOSEN_TOOL_PRICE",
        "unseen_counterfactual_actions_in_training":False,
        "private_initial_final_state_never_in_actor":True,
        "context_specific_forced_support":FORCED_ROUNDS,
        "epsilon_after_forced_support":cfg.epsilon,
        "minimum_postforced_option_support":cfg.epsilon/2,
        "without_replacement_exploration_has_conditional_zero_support":True,
        "frozen_chosen_value_estimates":frozen,
        "pooled_zero_feedback_action":pooled,
        "evaluation":results,
        "heldout_original_dev_or_test_family_evaluated":False,
        "heldout_intervention_mechanism_generalization_proven":False,
        "claim":"BOUNDED_POSTPROBE_OUTCOME_ONLY_LEARNING; NOT_GENERAL_REFLECTIVE_CONTROL",
        "designed_call_price":PRICE,
        "designed_call_price_is_physical_compute":False,
        "strongest_no_probe_fixed_policy_evaluated":True,
        "training_has_no_access_to_evaluation_fixed_policy_results":True,
        "training_trace":trace,
    }
    path=Path(cfg.output)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,sort_keys=True,indent=2)+"\n")
    print("REAL_POSTPROBE_SELECTED_OUTCOME",json.dumps({
        k:v for k,v in report.items() if k not in ("training_trace","variant_manifest")},
        sort_keys=True))
    return report

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",required=True)
    ap.add_argument("--seed",type=int,default=11)
    ap.add_argument("--episodes",type=int,default=40)
    ap.add_argument("--eval-episodes",type=int,default=2)
    ap.add_argument("--epsilon",type=float,default=.2)
    ap.add_argument("--output",default="build/owi_ec005_realtools/postprobe_outcome.json")
    train(ap.parse_args())

if __name__=="__main__":
    main()
