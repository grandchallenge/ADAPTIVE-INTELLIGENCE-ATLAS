#!/usr/bin/env python3
"""OWI-EC005P: five-seed actual chosen-only online contextual-option learning.

Features = ONLY source-selected public account/review status, no task ID,
private checker, source class state, target status or correct-answer label.
Three available options: STOP, APPROVE, REJECT. The scripted original public
target binding and tool execution are not learned; only option value is learned.

Training is online: execute exactly ONE sampled real action in a FRESH original
source reset, then update the empirical bandit with ONLY its terminal scalar.
True, zero-feature and miscredited-prior-chosen-outcome modes are trained
INDEPENDENTLY. Evaluation runs fresh original-source episodes AFTER freeze:
scripted public-rule-correct is an explicitly stronger fixed-policy benchmark;
heldout post-correction scenario is evaluator-scripted, not heldout source family.
"""
from __future__ import annotations
import argparse,collections,json,math,random,time
from pathlib import Path
from owi_ec005p_real_source_policy import (
    CONTRACT as SOURCE_CONTRACT,source_episode,OPTIONS,RULES,
    public_correct_status,SPEC_SHA)

CONTRACT="OWI-EC005P-CHOSEN-ONLY-SOURCE-LOCKED-BANDIT/1"
SEEDS=(11,23,37,41,53)
MODES=("true","zero_information","shuffled_chosen_outcome_credit")
TRAIN_EPISODES=60
EPSILON=0.18
PRICE_PER_ACTUAL_TOOL_CALL=0.002
MIN_FORCED_PER_ACTION=2
EVAL_BASELINES=("always_stop","always_approve","always_reject","public_rule_correct")
STAGES=("initial_pending","heldout_postcorrect")
ACTION_TO_STATUS={"always_stop":"stop","always_approve":"approved",
                  "always_reject":"rejected"}

def feature_for(raw,mode):
    if raw not in ("active:pending","banned:pending",
                   "active:approved","banned:rejected"):
        raise ValueError("unsupported original public context")
    if mode=="zero_information":
        return "blind"
    if mode in ("true","shuffled_chosen_outcome_credit"):
        return raw
    raise ValueError("unknown ablation")

class OnPolicyBandit:
    """A trained option-value table; no environment/oracle/reward source inside."""
    def __init__(self):
        self.counts=collections.defaultdict(lambda:[0]*len(OPTIONS))
        self.sums=collections.defaultdict(lambda:[0.0]*len(OPTIONS))
        self.next_forced={}
        self.learned_updates=0

    def best(self,feature):
        n=self.counts[feature]
        vals=[self.sums[feature][i]/n[i] if n[i] else -math.inf
              for i in range(len(OPTIONS))]
        if all(not math.isfinite(x) for x in vals):
            return 0
        return max(range(len(OPTIONS)),key=lambda k:(vals[k],-k))

    def sample(self,feature,rng,*,explore=True):
        count=self.counts[feature]
        if explore and min(count)<MIN_FORCED_PER_ACTION:
            # Uniform among underrepresented actions: no preferred label
            choices=[j for j,n in enumerate(count) if n<MIN_FORCED_PER_ACTION]
            a=rng.choice(choices)
            return OPTIONS[a],1/len(choices),feature
        best=self.best(feature)
        if not explore:
            return OPTIONS[best],1.0,feature
        if rng.random()<EPSILON:
            a=rng.randrange(len(OPTIONS))
        else:
            a=best
        probability=(1-EPSILON+EPSILON/len(OPTIONS)
                     if a==best else EPSILON/len(OPTIONS))
        return OPTIONS[a],probability,feature

    def update(self,feature,selected,chosen_scalar):
        if selected not in OPTIONS or type(chosen_scalar) not in (float,int):
            raise ValueError("not a chosen scalar outcome")
        if not math.isfinite(chosen_scalar) or not -2<=chosen_scalar<=2:
            raise ValueError("invalid terminal value")
        idx=OPTIONS.index(selected)
        self.counts[feature][idx]+=1
        self.sums[feature][idx]+=chosen_scalar
        self.learned_updates+=1

    def readable(self):
        return {k:{"n_by_option":dict(zip(OPTIONS,self.counts[k])),
                   "mean_utility_by_option":{
                       a:(round(self.sums[k][i]/self.counts[k][i],6)
                          if self.counts[k][i] else None)
                       for i,a in enumerate(OPTIONS)},
                   "greedy":OPTIONS[self.best(k)]}
                for k in sorted(self.counts)}

def utility(episode):
    if episode.get("contract")!=SOURCE_CONTRACT:
        raise ValueError("not a source-private chosen-only receipt")
    reward=episode["actual_selected_terminal_reward"]
    n=episode["actual_tool_calls"]
    if type(reward) not in (int,float) or not math.isfinite(reward) or (
            type(n) is not int) or not 0<=n<=8:
        raise ValueError("invalid original-source actual cost/reward")
    return round(reward-PRICE_PER_ACTUAL_TOOL_CALL*n,6)

def limited_receipt(episode):
    """Audit-only public receipt plus scalar, no source-private values."""
    allowed={
        "contract","source_original_train_row","source_full_sha256",
        "source_class_sha256","corrected_spec_sha256",
        "source_public_task_rule_audit_only","public_observed_context_only",
        "actual_policy_supplied_context","policy_selected_option",
        "actual_selected_propensity","original_source_public_initial_status",
        "actual_public_status_at_decision","actual_public_final_status",
        "evaluation_only_scripted_precorrection",
        "original_native_checker_reward_audit_only",
        "original_native_check_count_audit_only",
        "actual_selected_terminal_reward",
        "private_terminal_class_evaluator_only","actual_tool_calls",
        "actual_public_source_tool_trace","actual_source_worker_wall_seconds",
        "source_worker_peak_rss_kib","original_native_checker_wall_seconds",
        "versioned_checker_wall_seconds",
        "private_source_state_or_original_checker_in_policy",
        "unchosen_action_outcome_in_policy",
    }
    if set(episode)!=allowed:
        raise ValueError("unexpected private fields in chosen-only source receipt")
    return episode

def sample_train_schedule(seed):
    # All contexts have equal support, independent precommitted schedule.
    tasks=[RULES[(n+seed)%len(RULES)] for n in range(TRAIN_EPISODES)]
    return tasks

def train_mode(folder,spec,seed,mode):
    rng=random.Random(seed*1009+MODES.index(mode)*151+17)
    tasks=sample_train_schedule(seed)
    actor=OnPolicyBandit()
    trajectories=[]
    historical=[]
    for n,rule in enumerate(tasks):
        chosen={}
        def select(raw):
            key=feature_for(raw,mode)
            action,propensity,supplied=actor.sample(key,rng)
            chosen.update({"feature":key,"option":action,
                           "propensity":propensity})
            return action,propensity,supplied
        ep=limited_receipt(source_episode(folder/"710",rule,select,spec))
        if (ep["evaluation_only_scripted_precorrection"] is not False or
            ep["actual_policy_supplied_context"]!=chosen["feature"] or
            ep["policy_selected_option"]!=chosen["option"] or
            ep["actual_selected_propensity"]!=chosen["propensity"]):
            raise ValueError("on-policy selected action/feature receipt mismatch")
        value=utility(ep)
        if mode=="shuffled_chosen_outcome_credit" and historical:
            # A deliberately BROKEN online chosen-outcome credit-assignment
            # control: update this context/action with a prior episode's
            # independently chosen scalar, never an unchosen counterfactual.
            # Exact origin logged to make reward contamination auditable.
            idx=rng.randrange(len(historical))
            assigned=historical[idx][1]
            assigned_from=historical[idx][0]
        else:
            assigned=value
            assigned_from=n
        actor.update(chosen["feature"],chosen["option"],assigned)
        historical.append((n,value))
        trajectories.append({
            "episode_index":n,"train_rule_audit_only":rule,
            "feature_actually_supplied_to_policy":chosen["feature"],
            "source_selected_action":chosen["option"],
            "source_selected_propensity":chosen["propensity"],
            "chosen_actual_corrected_terminal_reward":ep["actual_selected_terminal_reward"],
            "chosen_actual_original_native_reward_audit_only":
                ep["original_native_checker_reward_audit_only"],
            "chosen_actual_utility":value,
            "assigned_scalar_to_policy_update":assigned,
            "assigned_scalar_origin_episode":assigned_from,
            "actual_source_tool_calls":ep["actual_tool_calls"],
            "source_worker_wall_seconds":ep["actual_source_worker_wall_seconds"],
            "original_native_checker_wall_seconds":
                ep["original_native_checker_wall_seconds"],
            "versioned_private_checker_wall_seconds":ep["versioned_checker_wall_seconds"],
            "peak_source_worker_rss_kib":ep["source_worker_peak_rss_kib"],
            "real_source_selected_public_receipts":
                ep["actual_public_source_tool_trace"],
            "private_state_or_checker_in_actor":False,
            "unchosen_counterfactual_outcome_in_update":False,
        })
    return actor,trajectories

def baseline_action(kind,raw):
    if kind=="public_rule_correct":
        status=raw.split(":")[0]
        return public_correct_status(status)
    return ACTION_TO_STATUS[kind]

def evaluate(folder,spec,seed,trained):
    evaluations=[]
    for stage in STAGES:
        for rule in RULES:
            for mode,actor in trained.items():
                # All models FROZEN. No evaluation outcome enters learning.
                def select(raw,actor=actor,mode=mode):
                    key=feature_for(raw,mode)
                    return actor.sample(key,random.Random(0),explore=False)
                ep=limited_receipt(source_episode(folder/"710",rule,select,spec,
                    postcorrect=(stage=="heldout_postcorrect")))
                evaluations.append({
                    "evaluation_stage":stage,
                    "source_public_rule_audit_only":rule,"model":mode,
                    "selected_option":ep["policy_selected_option"],
                    "policy_feature":ep["actual_policy_supplied_context"],
                    "real_corrected_reward":ep["actual_selected_terminal_reward"],
                    "real_original_native_reward":ep["original_native_checker_reward_audit_only"],
                    "real_terminal_class":ep["private_terminal_class_evaluator_only"],
                    "realized_utility":utility(ep),
                    "real_public_tool_calls":ep["actual_tool_calls"],
                    "actual_worker_wall_seconds":ep["actual_source_worker_wall_seconds"],
                    "actual_original_checker_wall_seconds":
                        ep["original_native_checker_wall_seconds"],
                    "actual_corrected_checker_wall_seconds":
                        ep["versioned_checker_wall_seconds"],
                    "worker_peak_rss_kib":ep["source_worker_peak_rss_kib"],
                    "actual_public_selected_call_hashes":
                        ep["actual_public_source_tool_trace"],
                    "learned_policy_updated_during_evaluation":False,
                })
            for kind in EVAL_BASELINES:
                def select(raw,kind=kind):
                    return baseline_action(kind,raw),1.0,feature_for(raw,"true")
                ep=limited_receipt(source_episode(folder/"710",rule,select,spec,
                    postcorrect=(stage=="heldout_postcorrect")))
                evaluations.append({
                    "evaluation_stage":stage,
                    "source_public_rule_audit_only":rule,"model":kind,
                    "selected_option":ep["policy_selected_option"],
                    "policy_feature":ep["actual_policy_supplied_context"],
                    "real_corrected_reward":ep["actual_selected_terminal_reward"],
                    "real_original_native_reward":ep["original_native_checker_reward_audit_only"],
                    "real_terminal_class":ep["private_terminal_class_evaluator_only"],
                    "realized_utility":utility(ep),
                    "real_public_tool_calls":ep["actual_tool_calls"],
                    "actual_worker_wall_seconds":ep["actual_source_worker_wall_seconds"],
                    "actual_original_checker_wall_seconds":
                        ep["original_native_checker_wall_seconds"],
                    "actual_corrected_checker_wall_seconds":
                        ep["versioned_checker_wall_seconds"],
                    "worker_peak_rss_kib":ep["source_worker_peak_rss_kib"],
                    "actual_public_selected_call_hashes":
                        ep["actual_public_source_tool_trace"],
                    "learned_policy_updated_during_evaluation":False,
                })
    if len(evaluations)!=len(STAGES)*len(RULES)*(
            len(MODES)+len(EVAL_BASELINES)):
        raise AssertionError("frozen post-training evaluation incomplete")
    return evaluations

def run(folder,spec,seed):
    if seed not in SEEDS:
        raise ValueError("only predeclared 5 independent training seeds")
    if not isinstance(folder,Path) or not spec.is_file():
        raise ValueError("source task/spec files required")
    if spec.read_bytes() and __import__("hashlib").sha256(spec.read_bytes()
            ).hexdigest()!=SPEC_SHA:
        raise ValueError("frozen source-corrected benchmark spec hash drift")
    begin=time.perf_counter()
    policies,training={},{}
    for mode in MODES:
        policies[mode],training[mode]=train_mode(folder,spec,seed,mode)
    total_train=sum(len(x) for x in training.values())
    if total_train!=len(MODES)*TRAIN_EPISODES:
        raise AssertionError("not 180 chosen-only actual original source training episodes")
    frozen={mode:p.readable() for mode,p in policies.items()}
    before={mode:p.learned_updates for mode,p in policies.items()}
    evaluation=evaluate(folder,spec,seed,policies)
    if before!={mode:p.learned_updates for mode,p in policies.items()}:
        raise RuntimeError("outcome labels leaked from evaluation into learned policies")
    return {
        "contract":CONTRACT,"seed":seed,
        "original_source_train_row":710,
        "original_source_and_original_native_checker_unchanged":True,
        "frozen_corrected_spec_sha256":SPEC_SHA,
        "new_versioned_reward_not_original_native":True,
        "experimental_modes":list(MODES),
        "separate_independently_retrained_policy_per_mode":True,
        "chosen_outcome_only_online_updates":True,
        "train_episodes_per_mode":TRAIN_EPISODES,
        "actual_original_source_train_episodes":total_train,
        "actual_original_source_evaluation_episodes":len(evaluation),
        "baseline_actions_evaluator_only":list(EVAL_BASELINES),
        "heldout_postcorrection_stage_not_source_family_holdout":True,
        "policy_architecture":"EMPIRICAL_TABULAR_3_ACTION_ONLINE_CONTEXTUAL_BANDIT",
        "policy_learns_next_option_only_not_tool_planning":True,
        "model_training_compute_note":"60 scalar-value table updates per mode; no neural FLOPs or language model",
        "fixed_price_per_actual_tool_call":PRICE_PER_ACTUAL_TOOL_CALL,
        "actual_run_wall_seconds":time.perf_counter()-begin,
        "training":training,"frozen_learned_option_tables":frozen,
        "prospective_actual_source_evaluation":evaluation,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",type=Path,required=True)
    p.add_argument("--revised-spec",type=Path,default=Path(
        "governance/research/OWI_EC005O_REVISED_MODERATION_V1.json"))
    p.add_argument("--seed",type=int,required=True,choices=SEEDS)
    p.add_argument("--output-dir",type=Path,default=Path(
        "build/owi_ec005p"))
    a=p.parse_args()
    out=run(a.input_dir,a.revised_spec,a.seed)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    path=a.output_dir/f"source_chosen_outcome_seed_{a.seed}.json"
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    summ={
        "contract":CONTRACT,"seed":a.seed,
        "actual_original_source_train_episodes":
            out["actual_original_source_train_episodes"],
        "actual_original_source_evaluation_episodes":
            out["actual_original_source_evaluation_episodes"],
        "frozen_learned_option_tables":out["frozen_learned_option_tables"],
        "prospective_evaluation":[{k:v for k,v in x.items()
            if k not in ("actual_public_selected_call_hashes",)}
            for x in out["prospective_actual_source_evaluation"]],
    }
    print("OWI_EC005P_SOURCE_CHOSEN_ONLY_FIVE_SEED",json.dumps(summ,sort_keys=True))
if __name__=="__main__":
    main()
