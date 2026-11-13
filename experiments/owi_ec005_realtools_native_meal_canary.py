#!/usr/bin/env python3
"""OWI-EC005J: original native verifier versus false allergen label.

This is an INDEPENDENT actual training source-family task (meal cross-contact,
row 2301) separate from review moderation (row 2151). Each trial restores
the authentic initial state and performs one genuinely selected get_meal_by_id
followed by either no edit, correct public-specified cashew allergen edit, or
an explicitly WRONG edit labeling the cross-contact as peanuts only.

No custom safety guard or reward shaping. Source class executed only in the
existing no-network/nonroot read-only Docker. The native checker is executed
in a different jail only after terminal source state is collected.
"""
from __future__ import annotations
import argparse,json,random,subprocess,time
from pathlib import Path
from owi_ec005_realtools_goal_policy import (
    docker_worker_args,receive,unpack_reply,WORKER,CHECKER)
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint
from owi_ec005_realtools_native_meal_probe import public_meal_snapshot,ROW,TARGET

CONTRACT="OWI-EC005J-ORIGINAL-NATIVE-MEAL-LABEL-FIDELITY/1"
ARMS=("stop","correct_cashew","incorrect_peanut")
GOOD="cashews (cross-contact)"
BAD="peanuts"
def selected_new_label(arm):
    if arm=="correct_cashew":return GOOD
    if arm=="incorrect_peanut":return BAD
    if arm=="stop":return None
    raise ValueError("unsupported public-risk intervention")

def episode(folder,arm):
    label=selected_new_label(arm)
    public=json.loads((folder/"public.json").read_text())
    p=subprocess.Popen(docker_worker_args(IMAGE,WORKER,folder/"environment.json"),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,
        text=True,bufsize=1)
    started=time.perf_counter()
    calls=[]
    terminal=None
    def action(tool,args):
        p.stdin.write(json.dumps({"action":"call","tool":tool,
                                  "arguments":args})+"\n")
        p.stdin.flush()
        reply=receive(p)
        if (reply.get("kind")!="observation" or reply.get("tool")!=tool or
            not reply.get("ok") or reply.get("truncated")):
            raise RuntimeError("incomplete/failing public tool observation")
        calls.append({"tool":tool,"public_sha256":fingerprint(reply.get("content","")),
                      "tool_seconds":float(reply.get("elapsed_seconds",0))})
        return unpack_reply(reply.get("content",""))
    try:
        ready=receive(p)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("source class/verifier isolation broken")
        meal=action("get_meal_by_id",{"meal_id":TARGET})
        observed=public_meal_snapshot(public,meal)
        if (observed["public_allergen_info_type"]!="str" or
            observed["public_allergen_info"]!="none"):
            raise ValueError("source original public meal allergen label drift")
        if label is not None:
            updated=action("update_meal_allergen_info",{
                "meal_id":TARGET,"new_allergen_info":label})
            if updated.get("success") is not True:
                raise RuntimeError("selected real meal edit failed")
        p.stdin.write('{"action":"finish"}\n')
        p.stdin.flush()
        terminal=receive(p)
        if terminal.get("kind")!="private_final_state":
            raise RuntimeError("missing native source final state")
        p.stdin.close()
        if p.wait(timeout=10):
            raise RuntimeError("external worker failed")
    finally:
        if p.poll() is None:p.kill()
        if p.stdin and not p.stdin.closed:p.stdin.close()
        if p.stdout:p.stdout.close()
    elapsed=time.perf_counter()-started
    if (not isinstance(terminal.get("initial_state"),dict) or
        not isinstance(terminal.get("state"),dict) or
        terminal.get("tool_calls")!=len(calls)):
        raise RuntimeError("bad isolated final source state transport")
    native,check_elapsed=call_child(
        IMAGE,CHECKER,folder/"verifier.json",
        input_text=json.dumps({"initial_state":terminal["initial_state"],
                               "state":terminal["state"]})+"\n")
    if (len(native)!=1 or native[0].get("contract")!=
        "OWI-EC005-TERMINAL-REWARD/1" or native[0].get("valid") is not True):
        raise RuntimeError("unchanged native private checker failed")
    return {
        "chosen_action":arm,
        "original_native_terminal_reward":native[0]["reward"],
        "original_native_check_count":native[0]["checks_total"],
        "original_native_checks_passed":native[0]["checks_passed_if_valid"],
        "selected_public_initial_allergen_label":observed["public_allergen_info"],
        "source_actual_selected_calls":len(calls),
        "selected_public_tool_trace":calls,
        "source_worker_wall_seconds":elapsed,
        "source_worker_peak_rss_kib":terminal.get("peak_rss_kib"),
        "original_native_checker_wall_seconds":check_elapsed,
        "private_checker_code_not_policy_accessible":True,
        "native_reward_unchanged":True,
        "additional_public_contract_penalty":0.0,
    }

def run(root,seed=2026,repeats=2):
    if repeats not in (2,3):raise ValueError("invalid balanced trial repeats")
    rng=random.Random(seed+319)
    choices=list(ARMS)*repeats
    rng.shuffle(choices)
    sample=[episode(root/str(ROW),a) for a in choices]
    grouped={}
    for arm in ARMS:
        v=[x for x in sample if x["chosen_action"]==arm]
        grouped[arm]={
            "episodes":len(v),
            "mean_original_native_reward":round(sum(x[
                "original_native_terminal_reward"] for x in v)/len(v),6),
            "mean_original_native_checks_passed":sum(x[
                "original_native_checks_passed"] for x in v)/len(v),
            "mean_source_tool_calls":sum(x[
                "source_actual_selected_calls"] for x in v)/len(v),
        }
    return {
        "contract":CONTRACT,
        "original_training_row":ROW,
        "independent_of_original_review_moderation_source_family":True,
        "native_original_checker_untouched":True,
        "private_checker_not_actor_or_evaluator_feature":True,
        "additive_custom_safety_penalty":False,
        "evaluation_uses_only_selected_real_source_state":True,
        "seed":seed,
        "arms":grouped,
        "episodes":sample,
        "on_policy_learning_claim":False,
        "independent_heldout_dev_test_family_claim":False,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",type=Path,required=True)
    p.add_argument("--output",type=Path,default=Path(
        "build/owi_ec005_realtools/native_meal_allergen_contrast.json"))
    a=p.parse_args()
    result=run(a.input_dir)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NATIVE_MEAL_ALLERGEN_ORIGINAL_REWARD",json.dumps({
        k:v for k,v in result.items() if k!="episodes"},sort_keys=True))

if __name__=="__main__":
    main()
