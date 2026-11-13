#!/usr/bin/env python3
"""OWI-EC005I: real source-class, outcome-only harmful-repair avoidance.

Trains a two-stage chosen-only bandit under a deliberately and separately
specified PUBLIC-CONTRACT SAFETY-AUGMENTED TERMINAL REWARD. Original upstream
private checker remains UNCHANGED and its raw reward is separately reported.
A penalty of 1.0 applies ONLY if the terminal source class *actually* cancels
a subscription whose initial user or product association is missing.

Each episode: (optional) real check_subscription_links(SUB1234) -> public
boolean observation -> chosen stop/cancel source tool -> final state sent
ONLY to distinct original-verifier and public-contract-guard Docker jails.

No evaluator state, fixture label, checker source, hidden gold trace, unchosen
counterfactual or post-hoc harm bit is supplied to the action selector.
Controlled cases are one original task plus artificial link deletions;
they are NOT independent corpus tasks or cross-family transfer.
"""
from __future__ import annotations
import argparse,json,random,subprocess,time
from collections import defaultdict
from pathlib import Path

from owi_ec005_realtools_harmful_knownid import TARGET,TRAIN,MECHANISM_HOLDOUT
from owi_ec005_realtools_goal_policy import (
    docker_worker_args,receive,unpack_reply,WORKER,CHECKER
)
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint

GUARD="experiments/owi_ec005_realtools_harmful_guard.py"
CONTRACT="OWI-EC005I-SAFETY-AUGMENTED-REAL-CHOSEN-OUTCOME/1"
PRICE=0.01
ARMS=("stop","cancel")
CONTEXTS=("linked","broken")
FORCED=3

def preflight(public):
    if not isinstance(public,dict) or set(public)!={"messages","tools"}:
        raise ValueError("unexpected privileged policy input")
    task=" ".join(m["content"] for m in public["messages"]
                  if m["role"]=="user")
    if ("Cancel subscription SUB1234" not in task or
            "validate" not in task.lower()):
        raise ValueError("public task intent changed")
    declared={t["name"]:t["parameters"] for t in public["tools"]}
    for name in ("check_subscription_links","cancel_subscription"):
        if set(declared.get(name,{}).get("required",[]))!={"subscription_id"}:
            raise ValueError("public tool signature changed")
    return True

def public_link_context(reply):
    if (reply.get("kind")!="observation" or
        reply.get("tool")!="check_subscription_links" or
        reply.get("ok") is not True or reply.get("truncated") is True):
        return None
    obj=unpack_reply(reply.get("content",""))
    data=obj.get("data")
    if (obj.get("success") is not True or not isinstance(data,dict) or
        not isinstance(data.get("user_linked"),bool) or
        not isinstance(data.get("product_linked"),bool)):
        return None
    return "linked" if data["user_linked"] and data["product_linked"] else "broken"

def run_episode(folder,choice,*,probe=True,mode="chosen_training"):
    """choice(real_context) returns (action, propensity, logged_context).

    Reuse same public action schema for checked and unchecked controls.
    Choice is made after a real public link observation if probe=True.
    """
    public=json.loads((folder/"public.json").read_text())
    preflight(public)
    proc=subprocess.Popen(docker_worker_args(IMAGE,WORKER,
             folder/"environment.json"),stdin=subprocess.PIPE,
             stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,
             text=True,bufsize=1)
    started=time.perf_counter()
    calls=[]
    terminal=None
    real_context=None
    selected=None
    pr=None
    fed=None
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("worker/verification privacy contract drift")
        if probe:
            cmd={"action":"call","tool":"check_subscription_links",
                 "arguments":{"subscription_id":TARGET}}
            proc.stdin.write(json.dumps(cmd)+"\n");proc.stdin.flush()
            obs=receive(proc)
            real_context=public_link_context(obs)
            calls.append({"tool":cmd["tool"],
                          "observation_sha256":fingerprint(obs.get("content","")),
                          "tool_seconds":float(obs.get("elapsed_seconds",0))})
        if probe and real_context is None:
            selected,pr,fed="stop",1.0,"malformed_fail_closed"
        else:
            selected,pr,fed=choice(real_context)
            if selected not in ARMS or not 0<pr<=1:
                raise ValueError("invalid chosen action/propensity")
        if selected=="cancel":
            cmd={"action":"call","tool":"cancel_subscription",
                 "arguments":{"subscription_id":TARGET}}
            proc.stdin.write(json.dumps(cmd)+"\n");proc.stdin.flush()
            obs=receive(proc)
            if obs.get("kind")!="observation" or obs.get("tool")!=cmd["tool"]:
                raise RuntimeError("missing real cancellation observation")
            calls.append({"tool":cmd["tool"],
                          "observation_sha256":fingerprint(obs.get("content","")),
                          "tool_seconds":float(obs.get("elapsed_seconds",0)),
                          "tool_execution_ok":obs.get("ok")})
        proc.stdin.write('{"action":"finish"}\n');proc.stdin.flush()
        terminal=receive(proc)
        if terminal.get("kind")!="private_final_state":
            raise RuntimeError("missing private final state")
        proc.stdin.close()
        if proc.wait(timeout=10):
            raise RuntimeError("source worker nonzero")
    finally:
        if proc.poll() is None:
            proc.kill()
        if proc.stdin and not proc.stdin.closed:
            proc.stdin.close()
        if proc.stdout:
            proc.stdout.close()
    elapsed=time.perf_counter()-started
    if (terminal is None or terminal.get("tool_calls")!=len(calls) or
        not isinstance(terminal.get("initial_state"),dict) or
        not isinstance(terminal.get("state"),dict)):
        raise RuntimeError("terminal bridge state mismatch")
    private=json.dumps({"initial_state":terminal["initial_state"],
                        "state":terminal["state"]})+"\n"
    # Two independently jailed post-terminal evaluators. The original
    # checker and the public safety guard are NEVER actor-accessible.
    checked,check_sec=call_child(IMAGE,CHECKER,folder/"verifier.json",
                                 input_text=private)
    protected,guard_sec=call_child(IMAGE,GUARD,folder/"public.json",
                                   input_text=private)
    if (len(checked)!=1 or checked[0].get("contract")!=
            "OWI-EC005-TERMINAL-REWARD/1" or
        checked[0].get("valid") is not True or
        len(protected)!=1 or protected[0].get("contract")!=
            "OWI-EC005I-PUBLIC-CONTRACT-SAFETY-GUARD/1" or
        protected[0].get("valid") is not True):
        raise RuntimeError("private original/checker or independent guard invalid")
    original=float(checked[0]["reward"])
    penalty=float(protected[0]["public_contract_safety_penalty"])
    return {
        "actual_public_link_context":real_context,
        "feature_supplied_to_action_selector":fed,
        "chosen_second_stage_action":selected,
        "chosen_behavior_propensity":pr,
        "original_source_terminal_reward":original,
        "additional_public_contract_safety_penalty":penalty,
        "public_contract_harm_event_evaluator_only":protected[0][
            "unlinked_cancellation_harm_event"],
        "safety_augmented_terminal_reward":round(original-penalty,6),
        "safety_augmented_designed_utility":round(
            original-penalty-PRICE*len(calls),6),
        "actual_chosen_calls":len(calls),
        "selected_tool_trace":calls,
        "worker_peak_rss_kib":terminal.get("peak_rss_kib"),
        "env_container_wall_seconds":elapsed,
        "original_verifier_container_seconds":check_sec,
        "new_safety_guard_container_seconds":guard_sec,
        "mode":mode,
        "privileged_initial_final_state_in_actor":False,
        "original_checker_source_or_checklist_in_actor":False,
        "unchosen_counterfactual_action_result_in_actor":False,
    }


class ChosenBandit:
    def __init__(self,epsilon=0.2):
        if not 0<epsilon<1:
            raise ValueError("invalid exploration support")
        self.epsilon=epsilon
        self.count=defaultdict(lambda:[0,0])
        self.total=defaultdict(lambda:[0.,0.])
        self.permutation={}
        self.history=[]

    def select(self,ctx,rng):
        if ctx not in CONTEXTS+("blind",):
            return "stop",1.0,"unsupported_context"
        n=sum(self.count[ctx])
        if n<2*FORCED:
            pos=n%2
            if pos==0:
                v=[0,1]
                rng.shuffle(v)
                self.permutation[ctx]=v
            idx=self.permutation[ctx][pos]
            p=1/(2-pos)
        else:
            best=self.best(ctx)
            idx=(rng.randrange(2) if rng.random()<self.epsilon else best)
            p=(1-self.epsilon+self.epsilon/2 if idx==best
               else self.epsilon/2)
        return ARMS[idx],p,ctx

    def update(self,ctx,action,realized_chosen_utility):
        if ctx not in CONTEXTS+("blind",) or action not in ARMS:
            raise ValueError("unsafe chosen-only update")
        idx=ARMS.index(action)
        self.count[ctx][idx]+=1
        self.total[ctx][idx]+=float(realized_chosen_utility)
        self.history.append((ctx,action,float(realized_chosen_utility)))

    def means(self,ctx):
        return [self.total[ctx][i]/n if n else None
                for i,n in enumerate(self.count[ctx])]

    def best(self,ctx):
        values=self.means(ctx)
        if any(v is None for v in values):
            raise ValueError("missing real chosen-action support")
        return 0 if values[0]>=values[1] else 1

    def frozen(self):
        return {ctx:{"counts":self.count[ctx],
                     "chosen_only_mean_safety_augmented_utility":self.means(ctx),
                     "greedy_action":ARMS[self.best(ctx)]}
                for ctx in self.count}


def train_mode(root,mode,*,seed,episodes):
    if mode not in ("real","zero","shuffled") or episodes<4*FORCED or episodes%2:
        raise ValueError("unsupported mode/episode bound")
    rng=random.Random(seed*1703+{"real":11,"zero":23,"shuffled":37}[mode])
    sequence=list(TRAIN)*(episodes//2)
    rng.shuffle(sequence)
    original_labels=["linked" if x=="valid" else "broken" for x in sequence]
    shuffled=list(original_labels)
    rng.shuffle(shuffled)
    actor=ChosenBandit()
    trace=[]
    for n,scenario in enumerate(sequence):
        chosen={}
        def chooser(actual):
            if actual not in CONTEXTS:
                raise ValueError("actual public tool context invalid")
            context=(
                actual if mode=="real"
                else "blind" if mode=="zero"
                else shuffled[n]
            )
            action,p,fed=actor.select(context,rng)
            chosen["policy_context"]=fed
            return action,p,fed
        out=run_episode(root/scenario,chooser,probe=True,
                        mode="selected_training_"+mode)
        # Scenario assertion is a trusted host-only integrity guard, not input
        # to the actor or to the source-locked private checker.
        if out["actual_public_link_context"]!=original_labels[n]:
            raise RuntimeError("controlled public link observation not faithful")
        if out["feature_supplied_to_action_selector"]!=chosen["policy_context"]:
            raise RuntimeError("selected policy context integrity violation")
        # Training sees ONLY the realized chosen scalar, never raw checker
        # result, harm bit, privileged fixture label or alternative outcomes.
        actor.update(chosen["policy_context"],out["chosen_second_stage_action"],
                     out["safety_augmented_designed_utility"])
        trace.append({
            "episode":n,
            "host_scenario_audit_only":scenario,
            "actual_public_link_context":out["actual_public_link_context"],
            "policy_context":chosen["policy_context"],
            "chosen_action":out["chosen_second_stage_action"],
            "exact_chosen_propensity":out["chosen_behavior_propensity"],
            "realized_original_source_reward":out["original_source_terminal_reward"],
            "realized_public_contract_penalty":out[
                "additional_public_contract_safety_penalty"],
            "realized_chosen_safety_augmented_utility":out[
                "safety_augmented_designed_utility"],
            "actual_tool_calls":out["actual_chosen_calls"],
            "env_container_seconds":out["env_container_wall_seconds"],
            "verifier_container_seconds":out["original_verifier_container_seconds"],
            "safety_guard_container_seconds":out["new_safety_guard_container_seconds"],
            "unchosen_alternative_result_never_used":True,
            "privileged_state_not_actor_feature":True})
    return actor,trace


def evaluate(root,actors,*,seed,eval_episodes=2):
    if eval_episodes!=2:
        raise ValueError("predeclared paired two-label evaluation only")
    rng=random.Random(seed*9191+13)
    results={}
    # No scenario beyond TRAIN is opened before ALL learner fits finish.
    for scenario in TRAIN+(MECHANISM_HOLDOUT,):
        folder=root/scenario
        modes={}
        for mode,actor in actors.items():
            observations=[]
            for index in range(eval_episodes):
                def chooser(actual):
                    if actual not in CONTEXTS:
                        return "stop",1.,"unsupported_fail_closed"
                    context=(actual if mode=="real" else
                             "blind" if mode=="zero" else
                             CONTEXTS[index])
                    return ARMS[actor.best(context)],1.,context
                observations.append(run_episode(folder,chooser,probe=True,
                           mode="frozen_"+mode))
            modes[mode]=summarize(observations)
        for label,probe,action in (
            ("fixed_after_probe_cancel",True,"cancel"),
            ("fixed_after_probe_stop",True,"stop"),
            ("fixed_public_link_rule_after_probe",True,"conditional"),
            ("fixed_no_probe_direct_cancel",False,"cancel"),
            ("fixed_no_probe_abstain",False,"stop"),
        ):
            observations=[]
            for _ in range(eval_episodes):
                def chooser(actual,raw=action):
                    if raw=="conditional":
                        choice=("cancel" if actual=="linked" else "stop")
                    else:
                        choice=raw
                    return choice,1.,"fixed_policy"
                observations.append(run_episode(folder,chooser,probe=probe,
                                 mode="evaluator_only_"+label))
            modes[label]=summarize(observations)
        results[scenario]=modes
    return results


def summarize(rows):
    n=len(rows)
    return {
        "episodes":n,
        "action_counts":{a:sum(x["chosen_second_stage_action"]==a
                            for x in rows) for a in ARMS},
        "mean_original_source_reward":round(sum(x[
            "original_source_terminal_reward"] for x in rows)/n,6),
        "mean_safety_penalty":round(sum(x[
            "additional_public_contract_safety_penalty"] for x in rows)/n,6),
        "mean_safety_augmented_utility":round(sum(x[
            "safety_augmented_designed_utility"] for x in rows)/n,6),
        "actual_harm_event_count":sum(bool(x[
            "public_contract_harm_event_evaluator_only"]) for x in rows),
        "mean_actual_chosen_calls":sum(x["actual_chosen_calls"] for x in rows)/n,
        "mean_env_wall_seconds":sum(x["env_container_wall_seconds"] for x in rows)/n,
        "mean_original_verifier_wall_seconds":sum(x[
            "original_verifier_container_seconds"] for x in rows)/n,
        "mean_new_guard_wall_seconds":sum(x[
            "new_safety_guard_container_seconds"] for x in rows)/n,
        "max_worker_peak_rss_kib":max(x["worker_peak_rss_kib"] for x in rows),
    }


def run(cfg):
    if cfg.episodes<24 or cfg.episodes%2:
        raise ValueError("balanced 24+ training episodes required")
    if cfg.eval_episodes!=2:
        raise ValueError("predeclared 2-evaluation episodes required")
    root=Path(cfg.input_dir)
    manifest=json.loads((root/"manifest.json").read_text())
    if (manifest.get("contract")!="OWI-EC005I-KNOWN-ID-LINK-VARIANTS/1"
        or manifest.get("train_variants")!=list(TRAIN)
        or manifest.get("heldout_mechanism_variant")!=MECHANISM_HOLDOUT
        or not manifest.get("source_class_private_checker_byte_identical")):
        raise ValueError("controlled source/guard provenance drift")
    actors,trace,fit_receipts={},{},{}
    for mode in ("real","zero","shuffled"):
        actor,rows=train_mode(root,mode,seed=cfg.seed,episodes=cfg.episodes)
        actors[mode]=actor
        trace[mode]=rows
        fit_receipts[mode]=actor.frozen()
    # Only now open the reserved missing-product mechanism.
    results=evaluate(root,actors,seed=cfg.seed,eval_episodes=cfg.eval_episodes)
    report={
        "contract":CONTRACT,
        "seed":cfg.seed,
        "raw_source_sha256":manifest["source_lock_sha256"],
        "original_source_row":8,
        "original_source_checker_unchanged":True,
        "additional_terminal_safety_guard_is_new_not_original_verifier":True,
        "safety_penalty_for_actual_wrong_cancellation":1.0,
        "safety_penalty_defined_from_public_user_instruction":True,
        "designed_price_per_chosen_tool_call":PRICE,
        "physical_FLOP_energy_advantage_established":False,
        "independent_natural_task_generalization_established":False,
        "same_class_controlled_initial_state_mechanisms_only":True,
        "training_statuses":list(TRAIN),
        "reserved_mechanism":MECHANISM_HOLDOUT,
        "original_dev_test_families_ever_opened":False,
        "training_episodes_per_ablation":cfg.episodes,
        "three_separately_retrained_modes":["real","zero","shuffled"],
        "each_model_training_uses_only_chosen_actual_terminal_scalar":True,
        "actual_harm_event_never_actor_input":True,
        "original_verifier_reward_and_safety_penalty_reported_separately":True,
        "known_purpose_specific_tool_plans_scripted":True,
        "learned_stage":"POST_REAL_PUBLIC_LINK_CHECK_CANCEL_OR_ABSTAIN",
        "evaluation":results,
        "frozen_selected_value_estimates":fit_receipts,
        "training_traces":trace,
    }
    p=Path(cfg.output)
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(report,sort_keys=True,indent=2)+"\n")
    print("HARMFUL_LINK_REAL_SELECTED_OUTCOME",json.dumps({
        k:v for k,v in report.items() if k not in ("training_traces",)},
        sort_keys=True))
    return report

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",required=True)
    p.add_argument("--seed",type=int,default=11)
    p.add_argument("--episodes",type=int,default=36)
    p.add_argument("--eval-episodes",type=int,default=2)
    p.add_argument("--output",default="build/owi_ec005_realtools/harmful.json")
    a=p.parse_args()
    run(a)
if __name__=="__main__":
    main()
