#!/usr/bin/env python3
"""Five-seed ORIGINAL-native source family 0/2 => heldout family 3 transfer.

Learner operates AFTER ONE MANDATORY genuinely selected original source public
probe. It learns only binary CONTINUE/STOP. The source-public action planner
that parses domain tools and builds follow-up actions is preauthored and NOT
trained; the feature (follow-up queue nonempty) is itself computed by this
planner. Outcome-only selection cannot be claimed as learned introspection.

Never open heldout family's public task/tool schema until after model freeze;
however its procedure was independently studied in predecessor EC005F/G,
so this is parameter-update holdout, not pristine blinded novel task intake.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,math,random,time
from pathlib import Path
from owi_ec005r_native_postprobe_episode import (
    CONTRACT as EP_CONTRACT,SOURCE_SHA,ROWS,PRICE,
    source_native_episode,original_public_file)
from owi_ec005_realtools_heterogeneous_trial import Policy

CONTRACT="OWI-EC005R-ORIGINAL-NATIVE-POSTPROBE-HOLDOUT-FIVE-SEED/1"
SPEC_CONTRACT="OWI-EC005R-SOURCE-NATIVE-POSTPROBE-FAMILY-HOLDOUT/1"
SEEDS=(11,23,37,41,53)
MODES=("actual_public_reply","zero_information","independently_randomized_reply")
CONTROLS=("always_continue_after_probe","always_stop_after_probe",
          "scripted_public_status","direct_no_probe","stop_no_probe",
          "public_affordance_adaptive")
TRAIN_ROWS=(0,2)
HELDOUT_ROW=3
TRAIN_PER_MODE=48
EVAL_PER_SEED=27
EPSILON=0.20
SUPPORT=2
OPTIONS=("stop","continue")
FEATURES=("followup_available","no_followup","blind")

def verify_frozen_manifest(path):
    raw=path.read_bytes()
    s=json.loads(raw)
    if (s.get("contract")!=SPEC_CONTRACT or
        s.get("source",{}).get("full_sha256")!=SOURCE_SHA or
        s.get("source",{}).get("independent_train_rows")!=list(TRAIN_ROWS) or
        s.get("source",{}).get("heldout_distinct_train_partition_family")!=HELDOUT_ROW or
        s.get("training",{}).get("seeds")!=list(SEEDS) or
        s.get("training",{}).get("modes")!=list(MODES) or
        s.get("training",{}).get("per_mode_per_seed_source_episodes")!=TRAIN_PER_MODE or
        s.get("training",{}).get("per_training_source_family_per_mode")!=TRAIN_PER_MODE//2 or
        s.get("evaluation",{}).get("frozen_models")!=list(MODES) or
        s.get("evaluation",{}).get("fixed_controls")!=list(CONTROLS) or
        s.get("evaluation",{}).get("real_source_eval_episodes_per_seed")!=EVAL_PER_SEED or
        s.get("accounting",{}).get("per_seed_original_source_episodes")!=
            TRAIN_PER_MODE*len(MODES)+EVAL_PER_SEED or
        s.get("accounting",{}).get("price_per_selected_tool_call")!=PRICE):
        raise ValueError("source-native R contract, heldout cohort or strong baseline drift")
    return hashlib.sha256(raw).hexdigest()

class ChosenOptionValues:
    def __init__(self):
        self.count=collections.defaultdict(lambda:[0,0])
        self.total=collections.defaultdict(lambda:[0.0,0.0])
        self.updates=0
    def best(self,key):
        if key not in FEATURES:raise ValueError("not a source selected public feature")
        ns=self.count[key]
        values=[self.total[key][i]/ns[i] if ns[i] else -math.inf
                for i in (0,1)]
        return OPTIONS[max((0,1),key=lambda i:(values[i],-i))]
    def select(self,key,rng,*,explore=True):
        if key not in FEATURES:raise ValueError("not original public derived feature")
        if not explore:return self.best(key),1.0
        under=[i for i,n in enumerate(self.count[key]) if n<SUPPORT]
        if under:
            i=rng.choice(under)
            return OPTIONS[i],1/len(under)
        best=self.best(key)
        if rng.random()<EPSILON:
            i=rng.randrange(2)
        else:
            i=OPTIONS.index(best)
        propensity=(1-EPSILON+EPSILON/2 if OPTIONS[i]==best else EPSILON/2)
        return OPTIONS[i],propensity
    def update(self,feature,chosen,realized):
        if feature not in FEATURES or chosen not in OPTIONS or (
            type(realized) not in (int,float)) or not math.isfinite(realized) or (
            not -1<=realized<=1):
            raise ValueError("not a supported real chosen source native scalar")
        i=OPTIONS.index(chosen)
        self.count[feature][i]+=1
        self.total[feature][i]+=realized
        self.updates+=1
    def readback(self):
        return {k:{"counts":dict(zip(OPTIONS,self.count[k])),
                   "means":{a:(round(self.total[k][i]/self.count[k][i],6)
                        if self.count[k][i] else None)
                        for i,a in enumerate(OPTIONS)},
                   "greedy":self.best(k)}
                for k in sorted(self.count)}

def schedule(seed):
    if seed not in SEEDS:raise ValueError("nonpreregistered independent seed")
    out=list(TRAIN_ROWS)*(TRAIN_PER_MODE//2)
    random.Random(seed*17+31).shuffle(out)
    assert len(out)==TRAIN_PER_MODE
    return out

def actor_feature(real,mode,rng):
    if real not in FEATURES[:-1] or mode not in MODES:
        raise ValueError("unselected or false public observation")
    if mode=="actual_public_reply":return real
    if mode=="zero_information":return "blind"
    # An explicitly artificial independent coin toss, not source-origin data.
    return rng.choice(FEATURES[:-1])

def train_mode(folder,seed,mode):
    rng=random.Random(seed*1009+MODES.index(mode)*151+17)
    actor=ChosenOptionValues()
    log=[]
    for idx,row in enumerate(schedule(seed)):
        def chooser(real):
            key=actor_feature(real,mode,rng)
            action,p=actor.select(key,rng,explore=True)
            return action,p,key
        ep=source_native_episode(folder/str(row),row,"probe",chooser)
        actor.update(ep["feature_supplied_to_learned_option_actor"],
                     ep["selected_postprobe_option"],
                     ep["chosen_actual_terminal_utility"])
        log.append({
            "episode":idx,"source_family_row_audit_only":row,
            "selected_original_source_native_receipt":ep,
            "chosen_original_native_utility_used_for_update":
                ep["chosen_actual_terminal_utility"],
            "counterfactual_private_rewards_seen":False,
        })
    return actor,log

def baseline_script_choice(row,task):
    # This public direct-action feasibility is computed by the SAME
    # original existing family-aware domain planner. It is a strong
    # transparent comparator, not a privileged source/checker oracle.
    direct=Policy(row,task,"direct").next_action()
    if direct["action"]=="call":
        return "direct"
    probe=Policy(row,task,"probe").next_action()
    if probe["action"]!="call":
        raise ValueError("unsupported original source public feasible options")
    return "probe"

def evaluate(folder,seed,trained):
    result=[]
    for row in ROWS:
        # The independent original holdout public.json is first read here,
        # after ALL mode training and source outcome updates are complete.
        public=original_public_file(folder/str(row))
        for policy in (*MODES,*CONTROLS):
            if policy in MODES:
                actor=trained[policy]
                rng=random.Random(seed*1013+MODES.index(policy)*37+row)
                def chooser(real,actor=actor,mode=policy,rng=rng):
                    key=actor_feature(real,mode,rng)
                    choice,pr=actor.select(key,rng,explore=False)
                    return choice,pr,key
                arm="probe"
                ep=source_native_episode(folder/str(row),row,arm,chooser)
            elif policy=="direct_no_probe":
                ep=source_native_episode(folder/str(row),row,"direct")
            elif policy=="stop_no_probe":
                ep=source_native_episode(folder/str(row),row,"stop")
            elif policy=="public_affordance_adaptive":
                arm=baseline_script_choice(row,public)
                if arm=="probe":
                    ep=source_native_episode(folder/str(row),row,arm,
                        lambda real:("continue" if real=="followup_available"
                                     else "stop",1.0,real))
                else:
                    ep=source_native_episode(folder/str(row),row,arm)
            else:
                if policy=="always_continue_after_probe":
                    choose=lambda real:("continue",1.0,real)
                elif policy=="always_stop_after_probe":
                    choose=lambda real:("stop",1.0,real)
                elif policy=="scripted_public_status":
                    choose=lambda real:("continue" if real=="followup_available"
                                         else "stop",1.0,real)
                else:raise ValueError("missing declared original source baseline")
                ep=source_native_episode(folder/str(row),row,"probe",choose)
            result.append({
                "original_family_row_evaluator_only":row,
                "policy":policy,"original_source_selected_native_receipt":ep,
                "actor_updated_using_heldout_or_evaluation_outcome":False,
                "heldout_distinct_family_for_actor":row==HELDOUT_ROW,
            })
    if len(result)!=EVAL_PER_SEED:raise AssertionError("evaluation cohort mismatch")
    return result

def run(folder,seed,spec):
    digest=verify_frozen_manifest(spec)
    actor,training={},{}
    began=time.perf_counter()
    for mode in MODES:
        actor[mode],training[mode]=train_mode(folder,seed,mode)
    frozen={mode:actor[mode].readback() for mode in MODES}
    test=evaluate(folder,seed,actor)
    if frozen!={mode:actor[mode].readback() for mode in MODES}:
        raise RuntimeError("actual source heldout/evaluation mutated frozen actor")
    unique={}
    for mode,rows in training.items():
        for x in rows:
            ep=x["selected_original_source_native_receipt"]
            unique.setdefault(str(x["source_family_row_audit_only"]),
                              ep["original_source_class_sha256_audit_only"])
    for x in test:
        ep=x["original_source_selected_native_receipt"]
        unique.setdefault(str(x["original_family_row_evaluator_only"]),
                          ep["original_source_class_sha256_audit_only"])
    if set(unique)!={"0","2","3"} or len(set(unique.values()))!=3:
        raise RuntimeError("independent original source TRAIN families not disjoint")
    return {
        "contract":CONTRACT,"seed":seed,
        "source_whole_original_sha256":SOURCE_SHA,
        "frozen_source_native_holdout_protocol_sha256":digest,
        "original_public_tasks_and_classes_and_verifiers_unchanged":True,
        "source_original_partition_train_only":True,
        "train_rows":[0,2],
        "heldout_original_distinct_family_row":HELDOUT_ROW,
        "source_executable_class_sha256_by_family":unique,
        "source_original_native_private_checker_only":True,
        "source_original_private_checker_was_not_in_actor":True,
        "no_source_oracle_or_unchosen_outcomes_in_learned_credits":True,
        "first_public_probe_mandatory_not_learned":True,
        "family_tool_arguments_and_public_reply_interpretation_scripted":True,
        "actual_original_source_training_episodes":TRAIN_PER_MODE*len(MODES),
        "actual_original_source_heldout_and_source_train_evaluation_episodes":len(test),
        "actual_source_original_checker_invocations":TRAIN_PER_MODE*len(MODES)+len(test),
        "actual_source_and_checker_wall_seconds":time.perf_counter()-began,
        "training":training,"frozen_policies":frozen,
        "fresh_source_evaluation":test,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",type=Path,required=True)
    p.add_argument("--seed",type=int,required=True,choices=SEEDS)
    p.add_argument("--task-spec",type=Path,required=True)
    p.add_argument("--output-dir",type=Path,default=Path("build/owi_ec005r"))
    a=p.parse_args()
    r=run(a.input_dir,a.seed,a.task_spec)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    path=a.output_dir/f"source_native_postprobe_seed_{a.seed}.json"
    path.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n")
    print("OWI_EC005R_NATIVE_FAMILY_HELDOUT_CHOSEN_ONLY_TRAINING",
          json.dumps({"seed":r["seed"],"train":r["actual_original_source_training_episodes"],
                      "fresh_eval":len(r["fresh_source_evaluation"]),
                      "frozen":r["frozen_policies"]},sort_keys=True))
if __name__=="__main__":
    main()
