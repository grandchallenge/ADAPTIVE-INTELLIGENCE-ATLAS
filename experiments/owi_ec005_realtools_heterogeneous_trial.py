#!/usr/bin/env python3
"""OWI-EC005F: three real training-family, randomized intervention trials.

Separate source-locked, public-tool-only policy from private task checker.
No learned model in this tranche: it estimates causal option/observation
costs to determine whether heterogeneity supports nontrivial later learning.
The only mechanisms chosen are STOP, PUBLIC_DIRECT, PUBLIC_PROBE_CONDITIONAL.
A family-specific transparent template derives every ID from the PUBLIC
task and actually SELECTED tool replies; no checker, class source, hidden
state, RSD skill, or unchosen result enters action selection.

Environment and terminal checker code run ONLY in distinct credential-free,
no-network, nonroot, cap-dropped, read-only Docker children.
"""
from __future__ import annotations
import argparse
import json
import random
import re
import subprocess
import time
from collections import Counter
from pathlib import Path

from owi_ec005_realtools_goal_policy import (
    docker_worker_args, receive, WORKER, CHECKER, unpack_reply
)
from owi_ec005_realtools_randomized import IMAGE, call_child, fingerprint

PRICE=0.01
MAX_STEPS=8
ARMS=("stop","direct","probe")
INDEXES=(0,2,3)


def user_text(public):
    if any(k in public for k in ("extra_info","verifier","environment",
                                 "rsd_skill","initial_state","class_code")):
        raise ValueError("private field in public action basis")
    return " ".join(m["content"] for m in public["messages"]
                    if m["role"]=="user")


def token(pattern, text):
    found=re.search(pattern,text,re.IGNORECASE)
    if not found:
        raise ValueError("required public task identifier not found")
    return found.group(1)


class Policy:
    def __init__(self, index,public,arm):
        if index not in INDEXES or arm not in ARMS:
            raise ValueError("undeclared family or action")
        self.index=index
        self.arm=arm
        self.public=public
        self.prompt=user_text(public)
        self.allowed={t["name"]:t["parameters"] for t in public["tools"]}
        self.queue=[]
        self.calls=0
        self.last=None
        self.stage=0
        self.state={"candidate_products":[],"target_subscription":None,
                    "status_checked":False,"status_is_active":False,
                    "restriction_present":None,"link_checked":False,
                    "link_valid":False}
        if index==0:
            self.user=token(r"User:\s*Alice Chan\s*\((USR[0-9]+)\)",self.prompt)
            self.target_product=token(r"product\s+(.+?)\s*\(monthly plan\)",self.prompt).strip()
            if self.arm=="probe":
                self.queue=[("list_user_subscriptions",{"user_id":self.user})]
        elif index==2:
            self.user=token(r"For user\s+(USR[0-9]+)",self.prompt)
            if not re.search(r'account_status from .suspended. to .active.',self.prompt):
                raise ValueError("public change requested inconsistent with policy")
            if arm=="probe":
                self.queue=[("check_user_account_status",{"user_id":self.user})]
            if arm=="direct":
                self.queue=[("update_user_account_status",
                             {"user_id":self.user,"new_status":"active"})]
        else:
            self.rest_id=token(r"restriction_id\s+(DR[0-9]+)",self.prompt)
            self.rest_name=token(r"name:\s*(.+?)(?:\n|$)",self.prompt).strip()
            self.rest_desc=token(r"description:\s*(.+?)(?:\n|$)",self.prompt).strip()
            self.rest_tag=token(r"tag:\s*(.+?)(?:\n|$)",self.prompt).strip()
            self.create=("create_dietary_restriction",{
                "restriction_id":self.rest_id,"name":self.rest_name,
                "description":self.rest_desc,"tag":self.rest_tag})
            if arm=="probe":
                self.queue=[("get_dietary_restriction_by_id",
                             {"restriction_id":self.rest_id})]
            if arm=="direct":
                self.queue=[self.create]

    def next_action(self):
        if self.arm=="stop" or self.calls>=MAX_STEPS or not self.queue:
            return {"action":"finish"}
        name,args=self.queue.pop(0)
        schema=self.allowed.get(name)
        if not isinstance(schema,dict):
            raise ValueError("undeclared tool invoked")
        required=set(schema.get("required",[]))
        if set(args)!=required:
            # Exact required-argument discipline; optional values are omitted.
            raise ValueError(f"public parameter contract drift for {name}")
        self.last=name
        self.calls+=1
        return {"action":"call","tool":name,"arguments":args}

    def observe(self,reply):
        if reply.get("kind")!="observation" or reply.get("tool")!=self.last:
            raise RuntimeError("wrong selected tool observation")
        data=unpack_reply(reply.get("content",""))
        success=data.get("success") is True
        if self.index==0:
            if self.last=="list_user_subscriptions" and success:
                rows=data.get("data")
                if isinstance(rows,list):
                    self.state["candidate_products"]=[
                        (r["subscription_id"],r["product_id"])
                        for r in rows if isinstance(r,dict)
                        and r.get("user_id")==self.user
                        and r.get("subscription_status")=="active"
                        and r.get("recurrence_pattern")=="monthly"
                        and isinstance(r.get("subscription_id"),str)
                        and isinstance(r.get("product_id"),str)]
                    self._next_product()
            elif self.last=="get_product_by_id" and success:
                record=data.get("data")
                if isinstance(record,dict) and (
                    record.get("name") or record.get("product_name") or ""
                ).casefold()==self.target_product.casefold():
                    self.state["target_subscription"]=self.state.get("inspected_id")
                    self.queue.append(("check_subscription_links",{
                        "subscription_id":self.state["target_subscription"]}))
                else:
                    self._next_product()
            elif self.last=="check_subscription_links":
                self.state["link_checked"]=True
                # Require an explicit positive link validation. Error or
                # missing validation never authorizes a cancellation.
                if success and self._valid_links(data):
                    self.state["link_valid"]=True
                    sid=self.state["target_subscription"]
                    self.queue.extend([
                        ("cancel_subscription",{"subscription_id":sid}),
                        ("invalidate_future_payments",{"subscription_id":sid}),
                        ("halt_scheduled_shipments",{"subscription_id":sid}),
                        ("modify_subscription_details",{
                            "subscription_id":sid,"updates":{
                                "next_shipment_date":None,
                                "recurrence_pattern":"none"}})])
            elif self.last=="cancel_subscription" and not success:
                # Cancel unsuccessful: do not continue with later mutations.
                self.queue=[]
        elif self.index==2 and self.last=="check_user_account_status":
            self.state["status_checked"]=True
            if success and isinstance(data.get("data"),dict):
                status=data["data"].get("account_status")
                self.state["status_is_active"]=status=="active"
                if status=="suspended":
                    self.queue.append(("update_user_account_status",{
                        "user_id":self.user,"new_status":"active"}))
        elif self.index==3 and self.last=="get_dietary_restriction_by_id":
            # Negative lookup is evidence of absence only when the public
            # tool explicitly says "not found", not on an arbitrary failure.
            error=data.get("error")
            if success:
                self.state["restriction_present"]=True
            elif isinstance(error,str) and "not found" in error.casefold():
                self.state["restriction_present"]=False
                self.queue.append(self.create)
        # All other action results are used for reporting, not implicit
        # authorizations to take more steps.

    def _next_product(self):
        if self.state["candidate_products"]:
            sid,pid=self.state["candidate_products"].pop(0)
            self.state["inspected_id"]=sid
            self.queue.append(("get_product_by_id",{"product_id":pid}))

    @staticmethod
    def _valid_links(resp):
        obj=resp.get("data")
        # A pair of explicit link attestations overrides any contradictory
        # generic success flag. In particular, top-level valid=True can
        # NEVER authorize a cancellation when either explicit link is false.
        if isinstance(obj,dict) and ("user_linked" in obj or "product_linked" in obj):
            return obj.get("user_linked") is True and obj.get("product_linked") is True
        if resp.get("valid") is True or resp.get("links_valid") is True:
            return True
        if obj is True:
            return True
        if isinstance(obj,dict):
            return any(obj.get(k) is True for k in
                       ("valid","links_valid","is_valid","are_links_valid"))
        return False


def trial(public,environment,verifier,index,arm):
    p=Policy(index,public,arm)
    proc=subprocess.Popen(
        docker_worker_args(IMAGE,WORKER,environment),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,text=True,bufsize=1)
    started=time.perf_counter()
    observations=[]
    terminal=None
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("worker/verifier isolation contract violation")
        while True:
            command=p.next_action()
            proc.stdin.write(json.dumps(command,sort_keys=True)+"\n")
            proc.stdin.flush()
            reply=receive(proc)
            if command["action"]=="finish":
                if reply.get("kind")!="private_final_state":
                    raise RuntimeError("terminal state absent")
                terminal=reply
                break
            p.observe(reply)
            observations.append({
                "tool":command["tool"],"observation_sha256":fingerprint(
                    reply.get("content","")),
                "tool_seconds":float(reply.get("elapsed_seconds",0)),
                "worker_exception_free":bool(reply.get("ok"))})
        proc.stdin.close()
        if proc.wait(timeout=10):
            raise RuntimeError("restricted environment failed")
    finally:
        if proc.poll() is None:
            proc.kill()
        if proc.stdin and not proc.stdin.closed:
            proc.stdin.close()
        if proc.stdout:
            proc.stdout.close()
    env_elapsed=time.perf_counter()-started
    if terminal is None or terminal.get("tool_calls")!=len(observations):
        raise RuntimeError("tool-count integrity mismatch")
    if not all(isinstance(terminal.get(k),dict)
               for k in ("initial_state","state")):
        raise RuntimeError("private terminal JSON contract drift")
    # The only checker access is from this trusted bridge at the end;
    # the selected-action policy never receives or inspects checker source.
    envelope=json.dumps({"initial_state":terminal["initial_state"],
                         "state":terminal["state"]})+"\n"
    checked,checker_elapsed=call_child(
        IMAGE,CHECKER,verifier,input_text=envelope)
    if len(checked)!=1 or checked[0].get("contract")!=(
            "OWI-EC005-TERMINAL-REWARD/1"):
        raise RuntimeError("private checker IPC contract drift")
    outcome=checked[0]
    if outcome.get("valid") is not True:
        raise RuntimeError("invalid terminal checker (not a zero reward)")
    return {
        "family_train_row":index,"arm":arm,"assigned_propensity":1/3,
        "private_terminal_reward":outcome["reward"],
        "checks_passed":outcome["checks_passed_if_valid"],
        "checks_total":outcome["checks_total"],
        "chosen_calls":len(observations),
        "chosen_tool_trace":observations,
        "designed_call_cost":PRICE*len(observations),
        "designed_utility":round(outcome["reward"]-PRICE*len(observations),6),
        "actual_tool_seconds":sum(x["tool_seconds"] for x in observations),
        "env_container_seconds":env_elapsed,
        "checker_container_seconds":checker_elapsed,
        "publicly_resolved_target":bool(p.state.get("target_subscription")),
        "private_fields_in_policy":False,
        "unchosen_counterfactual_tools_executed":False,
    }


def run(cfg):
    rng=random.Random(cfg.seed)
    if cfg.repeats<2 or cfg.repeats>6:
        raise ValueError("bounded matched repeats 2..6")
    results=[]
    for index in INDEXES:
        folder=Path(cfg.input_dir)/str(index)
        public=json.loads((folder/"public.json").read_text())
        actions=list(ARMS)*cfg.repeats
        rng.shuffle(actions)
        for i,arm in enumerate(actions):
            result=trial(public,folder/"environment.json",
                         folder/"verifier.json",index,arm)
            result["repetition_index"]=i
            results.append(result)
    groups={}
    for i in INDEXES:
        groups[str(i)]={}
        for arm in ARMS:
            sample=[x for x in results if x["family_train_row"]==i
                    and x["arm"]==arm]
            groups[str(i)][arm]={
                "episodes":len(sample),
                "mean_reward":round(sum(x["private_terminal_reward"]
                                         for x in sample)/len(sample),5),
                "mean_utility":round(sum(x["designed_utility"]
                                          for x in sample)/len(sample),5),
                "mean_calls":sum(x["chosen_calls"] for x in sample)/len(sample),
                "mean_actual_tool_seconds":sum(x["actual_tool_seconds"]
                                               for x in sample)/len(sample),
            }
    report={
        "contract":"OWI-EC005F-MULTI-FAMILY-ACTUAL-INTERVENTION/1",
        "seed":cfg.seed,
        "independent_training_family_count":len(INDEXES),
        "independent_task_count":len(INDEXES),
        "episodes":len(results),
        "arm_first_stage_propensity":1/3,
        "randomized_blocking":"equal within each family, shuffled by seed",
        "private_verifier_invoked_only_at_terminal":True,
        "heldout_development_family_evaluated":False,
        "heldout_test_family_evaluated":False,
        "outcome_only_policy_learning":"NOT_PERFORMED",
        "scientific_introspection_claim":"NOT_ESTABLISHED",
        "design_call_price":PRICE,
        "family_results":groups,
        "episodes_data":results,
    }
    dest=Path(cfg.output)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(report,sort_keys=True,indent=2)+"\n")
    print("HETEROGENEOUS_TERMINAL_EVIDENCE",json.dumps({
        k:v for k,v in report.items() if k!="episodes_data"},sort_keys=True))
    return report


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",required=True)
    ap.add_argument("--seed",type=int,default=2026)
    ap.add_argument("--repeats",type=int,default=3)
    ap.add_argument("--output",default="build/owi_ec005_realtools/heterogeneous_outcomes.json")
    cfg=ap.parse_args()
    run(cfg)
if __name__=="__main__":
    main()
