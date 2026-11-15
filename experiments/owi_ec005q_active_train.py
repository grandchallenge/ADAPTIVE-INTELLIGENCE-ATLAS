#!/usr/bin/env python3
"""OWI-EC005Q: 5-seed genuine source-conditional probe/repair option learner.

New benchmark-specific GENERIC task masks target identity; original source
class, initial records and native private checker stay unchanged. The actor's
optional list_all_users probe is actually executed only on chosen PROBE paths.
Two tabular chosen-outcome action-value stages train on the SAME delayed
realized terminal scalar, with independent randomized, zero-signal ablations.

This establishes at most within-one-original-source synthetic-masked-task
active information value; NOT an independently held-out source-family result.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,math,random,time
from pathlib import Path
from owi_ec005q_source_active_episode import (
    CONTRACT as EP_CONTRACT,source_episode,STAGES,OPTIONS,POST_OPTIONS,
    PRICE_PER_CALL,PRICE_FOR_PROBE,SPEC_SHA)
from owi_ec005_versioned_moderation_paired import TARGETS

CONTRACT="OWI-EC005Q-FIVE-SEED-CHOSEN-ONLY-ACTIVE-PROBE/1"
SEEDS=(11,23,37,41,53)
MODES=("true","zero_probe_signal","randomized_probe_signal")
BASELINES=("scripted_adaptive","always_probe_correct","always_stop",
           "always_approve","always_reject")
TRAIN_EPISODES=96
UNKNOWN_FORCED_PROBES=12
MIN_SUPPORT=2
EPSILON=0.18
REWARD_SCALAR_NAME="actual_selected_versioned_utility"
TASK_SPEC_CONTRACT="OWI-EC005Q-MASKED-PARTIAL-OBSERVATION-SOURCE-BENCHMARK/1"

def check_frozen_task_manifest(path):
    """Validate the exact byte-identity and declared scope of Q's NEW task."""
    raw=path.read_bytes()
    manifest=json.loads(raw)
    if (manifest.get("contract")!=TASK_SPEC_CONTRACT or
        manifest.get("status")!="PREREGISTERED_CANDIDATE_NOT_ORIGINAL_NATIVE_DATASET" or
        manifest.get("source",{}).get("source_row")!=710 or
        manifest.get("source",{}).get("full_dataset_sha256")!=
          "3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a" or
        manifest.get("source",{}).get("source_class_sha256")!=
          "ddfa0ad145cc43f1ab82545912b9e80410c5793b585d31d714f92c07b626dfba" or
        manifest.get("separate_corrected_terminal_spec",{}).get("sha256")!=SPEC_SHA or
        manifest.get("training",{}).get("seeds")!=list(SEEDS) or
        manifest.get("training",{}).get("modes")!=list(MODES) or
        manifest.get("training",{}).get("source_episodes_per_mode_per_seed")!=TRAIN_EPISODES or
        manifest.get("training",{}).get("forced_support",{}).get("uncertain_first_probe_visits")!=UNKNOWN_FORCED_PROBES or
        manifest.get("training",{}).get("epsilon")!=EPSILON or
        manifest.get("evaluation",{}).get("regimes")!=list(STAGES) or
        manifest.get("evaluation",{}).get("policies")!=list((*MODES,*BASELINES)) or
        manifest.get("evaluation",{}).get("source_episodes_per_seed")!=48):
        raise ValueError("frozen versioned Q public-task/probe-reward manifest drift")
    return hashlib.sha256(raw).hexdigest()
RULES=("banned_reject","eligible_approve")
SCHEDULE_PHASES=("unknown","certified","resolved")

class ValueTable:
    """Tabular estimates from chosen terminal scalars only; unbiased prior."""
    def __init__(self,options):
        self.options=tuple(options)
        self.count=collections.defaultdict(lambda:[0]*len(self.options))
        self.totals=collections.defaultdict(lambda:[0.]*len(self.options))
        self.updates=0
    def best(self,key):
        count=self.count[key]
        vals=[self.totals[key][i]/count[i] if count[i] else -math.inf
              for i in range(len(self.options))]
        if all(not math.isfinite(x) for x in vals):return self.options[0]
        return self.options[max(range(len(self.options)),
                                key=lambda i:(vals[i],-i))]
    def choose(self,key,rng,*,force=None,explore=True):
        if not isinstance(key,str) or not key:
            raise ValueError("actor feature must be nonempty actual public field")
        if force is not None:
            if force not in self.options:
                raise ValueError("forced exploration beyond original source actions")
            return force,1.0
        if not explore:
            return self.best(key),1.0
        counts=self.count[key]
        unvisited=[i for i,n in enumerate(counts) if n<MIN_SUPPORT]
        if unvisited:
            k=rng.choice(unvisited)
            return self.options[k],1/len(unvisited)
        opt=self.best(key)
        if rng.random()<EPSILON:
            selected=self.options[rng.randrange(len(self.options))]
        else:
            selected=opt
        pr=(1-EPSILON+EPSILON/len(self.options) if selected==opt
            else EPSILON/len(self.options))
        return selected,pr
    def update(self,key,action,selected_scalar):
        if action not in self.options or type(selected_scalar) not in (int,float):
            raise ValueError("invalid chosen source option or terminal reward")
        if not math.isfinite(selected_scalar) or not -2.0<=selected_scalar<=2.0:
            raise ValueError("invalid chosen source scalar")
        k=self.options.index(action)
        self.count[key][k]+=1
        self.totals[key][k]+=selected_scalar
        self.updates+=1
    def readable(self):
        return {k:{"chosen_counts":dict(zip(self.options,self.count[k])),
                   "chosen_means":{
                       a:(round(self.totals[k][i]/self.count[k][i],6)
                          if self.count[k][i] else None)
                       for i,a in enumerate(self.options)},
                   "greedy":self.best(k)}
                for k in sorted(self.count)}

class TwoStageActor:
    def __init__(self):
        self.initial=ValueTable(OPTIONS)
        self.post=ValueTable(POST_OPTIONS)
        self.unknown_seen=0
    def initial_choice(self,feature,rng,*,explore=True):
        if feature not in ("unknown","certified_active",
                           "certified_banned","already_resolved"):
            raise ValueError("initial policy feature not source-public verified")
        forced=None
        if explore and feature=="unknown":
            self.unknown_seen+=1
            # Precommitted independent-of-hidden-status exploration schedule.
            # Do NOT call this a learned information policy.
            if self.unknown_seen<=UNKNOWN_FORCED_PROBES:
                forced="probe"
        return self.initial.choose(feature,rng,force=forced,explore=explore)
    def post_choice(self,status,rng,*,explore=True):
        if status not in ("active","banned","blind"):
            raise ValueError("postprobe status is not an allowed source/ablation reply")
        return self.post.choose(status,rng,explore=explore)
    def update_from_chosen_only(self,episode):
        if episode.get("contract")!=EP_CONTRACT:
            raise ValueError("not a real selected original source episode")
        feature=episode["versioned_public_initial_feature"]
        initial=episode["initial_selected_action"]
        scalar=episode[REWARD_SCALAR_NAME]
        self.initial.update(feature,initial,scalar)
        if initial=="probe":
            self.post.update(episode["policy_supplied_postprobe_signal"],
                             episode["postprobe_selected_action"],scalar)
    def readable(self):
        return {"initial":self.initial.readable(),
                "postprobe":self.post.readable(),
                "stage0_updates":self.initial.updates,
                "postprobe_updates":self.post.updates,
                "forced_unknown_probe_count":min(
                    self.unknown_seen,UNKNOWN_FORCED_PROBES)}

def schedule(seed):
    if seed not in SEEDS:
        raise ValueError("not a preregistered independent seed")
    seq=list(SCHEDULE_PHASES)*32
    random.Random(seed*17+31).shuffle(seq)
    count=collections.Counter()
    out=[]
    for stage in seq:
        rule=RULES[count[stage]%2]
        out.append((stage,rule))
        count[stage]+=1
    if len(out)!=TRAIN_EPISODES or any(count[x]!=32 for x in STAGES):
        raise RuntimeError("source training scenario balancing failed")
    return out

def training_mode(folder,spec,seed,mode):
    if mode not in MODES:
        raise ValueError("undeclared observation ablation")
    rng=random.Random(seed*1009+MODES.index(mode)*151+17)
    actor=TwoStageActor()
    trajectories=[]
    for i,(stage,rule) in enumerate(schedule(seed)):
        def initial(feature):
            return actor.initial_choice(feature,rng)
        def after(signal):
            return actor.post_choice(signal,rng)
        episode=source_episode(folder/"710",rule,stage,initial,after,spec,
                               probe_mode=mode,rng=rng)
        # Only THIS chosen episode's scalar drives both option updates.
        actor.update_from_chosen_only(episode)
        trajectories.append({"episode_index":i,"stage_audit_only":stage,
                             "target_rule_audit_only":rule,
                             "source_selected_actual_episode":episode,
                             "chosen_only_scalar_for_both_actor_stages":
                                 episode[REWARD_SCALAR_NAME],
                             "all_unchosen_outcomes_unobserved":True})
    return actor,trajectories

def baseline_choices(policy,feature):
    if policy=="scripted_adaptive":
        if feature=="unknown":return "probe",1.0
        if feature=="already_resolved":return "stop",1.0
        if feature=="certified_active":return "approved",1.0
        if feature=="certified_banned":return "rejected",1.0
    if policy=="always_probe_correct":return "probe",1.0
    if policy=="always_stop":return "stop",1.0
    if policy=="always_approve":return "approved",1.0
    if policy=="always_reject":return "rejected",1.0
    raise ValueError("fixed strong scripted policy outside task-public scope")

def eval_baseline_after(policy,feature,signal):
    if policy not in ("scripted_adaptive","always_probe_correct"):
        raise ValueError("nonprobe fixed action cannot condition")
    if feature=="already_resolved":return "stop",1.0
    if signal=="active":return "approved",1.0
    if signal=="banned":return "rejected",1.0
    raise ValueError("original selected source probe signal missing")

def evaluation(folder,spec,seed,trained):
    # Independent evaluation RNG; no mutation of frozen learned tables.
    result=[]
    for stage in STAGES:
        for rule in RULES:
            for mode in (*MODES,*BASELINES):
                if mode in MODES:
                    actor=trained[mode]
                    rng=random.Random(seed*1013+MODES.index(mode)*37+
                        STAGES.index(stage)*11+RULES.index(rule))
                    def initial(feature,actor=actor,rng=rng):
                        return actor.initial_choice(feature,rng,explore=False)
                    def after(signal,actor=actor,rng=rng):
                        return actor.post_choice(signal,rng,explore=False)
                    probe_mode=mode
                else:
                    cached={"initial":None}
                    def initial(feature,policy=mode,cached=cached):
                        cached["initial"]=feature
                        return baseline_choices(policy,feature)
                    def after(signal,policy=mode,cached=cached):
                        return eval_baseline_after(policy,cached["initial"],signal)
                    probe_mode="true"
                    rng=None
                ep=source_episode(folder/"710",rule,stage,initial,after,spec,
                                  probe_mode=probe_mode,rng=rng)
                result.append({"evaluation_stage":stage,
                               "target_rule_audit_only":rule,
                               "frozen_model_or_fixed_baseline":mode,
                               "source_selected_actual_episode":ep,
                               "learner_updated_on_evaluation":False})
    expected=len(STAGES)*len(RULES)*(len(MODES)+len(BASELINES))
    if len(result)!=expected:raise AssertionError("missing source evaluation cases")
    return result

def run(folder,spec,seed,task_spec):
    if seed not in SEEDS:raise ValueError("only five preregistered seeds")
    if not spec.exists():raise ValueError("frozen O-v1 versioned private scorer missing")
    task_spec_sha=check_frozen_task_manifest(task_spec)
    started=time.perf_counter()
    actor,training={},{}
    for mode in MODES:
        actor[mode],training[mode]=training_mode(folder,spec,seed,mode)
    frozen={mode:a.readable() for mode,a in actor.items()}
    evaluation_rows=evaluation(folder,spec,seed,actor)
    if frozen!={mode:a.readable() for mode,a in actor.items()}:
        raise ValueError("prospective evaluation contaminated frozen learned policies")
    total=len(MODES)*TRAIN_EPISODES+len(evaluation_rows)
    return {
        "contract":CONTRACT,"seed":seed,
        "original_corpus_and_checker_unmodified":True,
        "generic_source_public_task_is_versioned_and_intentionally_masked":True,
        "new_versioned_terminal_reward_not_original_native":True,
        "corrected_spec_sha256":SPEC_SHA,
        "frozen_versioned_masked_task_spec_sha256":task_spec_sha,
        "source_original_train_row":710,
        "one_original_independent_natural_training_family":True,
        "five_independent_seed_runs_required":True,
        "chosen_only_delayed_scalar_for_both_policy_stages":True,
        "scripted_target_discovery_not_learned":True,
        "no_unselected_counterfactual_actions_in_training":True,
        "per_mode_real_source_training_episodes":TRAIN_EPISODES,
        "total_actual_original_source_training_episodes":len(MODES)*TRAIN_EPISODES,
        "total_actual_original_source_evaluation_episodes":len(evaluation_rows),
        "total_actual_original_source_episodes":total,
        "original_private_checker_invocations":total,
        "versioned_corrected_private_checker_invocations":total,
        "probe_actual_tool_call_cost":PRICE_PER_CALL,
        "optional_probe_additional_design_price":PRICE_FOR_PROBE,
        "actual_original_source_wall_seconds":time.perf_counter()-started,
        "training":training,"frozen_learned_models":frozen,
        "fresh_prospective_evaluation":evaluation_rows,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",type=Path,required=True)
    p.add_argument("--revised-spec",type=Path,required=True)
    p.add_argument("--task-spec",type=Path,required=True)
    p.add_argument("--seed",type=int,choices=SEEDS,required=True)
    p.add_argument("--output-dir",type=Path,default=Path("build/owi_ec005q"))
    a=p.parse_args()
    out=run(a.input_dir,a.revised_spec,a.seed,a.task_spec)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    target=a.output_dir/f"active_source_seed_{a.seed}.json"
    target.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    from collections import Counter
    summary={
        "contract":out["contract"],"seed":a.seed,
        "actual_original_source_episodes":out["total_actual_original_source_episodes"],
        "actual_optional_probes":sum(
            e["source_selected_actual_episode"]["physical_optional_probe_executed"]
            for rows in out["training"].values() for e in rows),
        "frozen_greedy_actions":{
            k:{"initial":v["initial"],"postprobe":v["postprobe"]}
            for k,v in out["frozen_learned_models"].items()},
    }
    print("OWI_EC005Q_GENUINE_SOURCE_OPTIONAL_PROBE_TRAINING",
          json.dumps(summary,sort_keys=True))
if __name__=="__main__":
    main()
