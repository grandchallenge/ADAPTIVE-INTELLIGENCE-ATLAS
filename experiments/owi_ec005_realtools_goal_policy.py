#!/usr/bin/env python3
"""OWI-EC-005D source-locked, *public-only* conditional goal agent.

A deliberately simple scripted controller, NOT a learned language model.
It parses the publicly stated task, asks allowed tool calls, reads actual
observations, resolves returned IDs, and selects the next action accordingly.
Never reads the hidden environment state, verifier, reflection skills or
unchosen actions. All external code executes inside existing Docker jail.

Arms: stop; public read-only inspection; public-conditioned goal intervention.
The private checker runs ONLY after completion, in a separate container.
"""
from __future__ import annotations
import argparse
import ast
import datetime as dt
import hashlib
import json
import re
import select
import subprocess
import time
from collections import Counter
from pathlib import Path

from owi_ec005_realtools_randomized import (
    IMAGE, call_child, fingerprint, sample_arms
)

WORKER="experiments/owi_ec005_realtools_episode_worker.py"
CHECKER="experiments/owi_ec005_realtools_terminal_verifier.py"
MAX_STEPS=8

def parse_task(public):
    text = "\n".join(m["content"] for m in public["messages"]
                     if m["role"] == "user")
    first = re.search(
        r"new outbreak report for (.*?) in (.*?), submitted by the citizen "
        r"reporter (.*?), with an initial case count of (\d+)",
        text, re.IGNORECASE)
    updated = re.search(r"Update the case count to (\d+)", text, re.IGNORECASE)
    if not first or not updated:
        raise ValueError("public task unsupported by goal controller")
    return {"disease":first.group(1), "location":first.group(2),
            "reporter":first.group(3), "initial_count":int(first.group(4)),
            "target_count":int(updated.group(1))}

def unpack_reply(content):
    # EnvScaler tool interface returns Python dict reprs. literal_eval does
    # NOT execute input. Invalid/truncated replies cannot authorize mutation.
    try:
        parsed=ast.literal_eval(content)
    except (ValueError, SyntaxError, MemoryError, RecursionError):
        return {"success":False,"data":None}
    return parsed if isinstance(parsed,dict) else {"success":False,"data":None}

def identifier(items, name, key):
    if not isinstance(items,list):
        return None
    for item in items:
        if isinstance(item,dict) and item.get("name","").casefold()==name.casefold():
            return item.get(key)
    return None

class GoalPolicy:
    """The policy receives only public task and actually selected responses."""
    def __init__(self, public, arm):
        self.goal=parse_task(public)
        self.arm=arm
        self.actions=0
        self.state={"location_id":None,"reporter_id":None,
                    "prior": [],"report_id":None,"created":False,
                    "date_reported":None,
                    "verified":False}
        self.allowed={x["name"] for x in public["tools"]}
        needed={"get_location_by_name","list_reporters_by_type",
                "list_reports_by_disease","create_outbreak_report",
                "validate_reporter_credentials","update_case_count",
                "verify_outbreak_report","escalate_outbreak_report"}
        if not needed.issubset(self.allowed):
            raise ValueError("public tool declarations changed")
        self.last_action=None

    def next_action(self):
        i=self.actions
        g=self.goal
        if self.arm==0 or (self.arm==1 and i>=3) or i>=MAX_STEPS:
            return {"action":"finish"}
        if i==0:
            tool,args="get_location_by_name",{"name":g["location"]}
        elif i==1:
            tool,args="list_reporters_by_type",{"reporter_type":"citizen"}
        elif i==2:
            tool,args="list_reports_by_disease",{"disease_name":g["disease"]}
        elif self.arm!=2:
            return {"action":"finish"}
        elif not self.state["location_id"] or not self.state["reporter_id"]:
            return {"action":"finish"}
        elif i==3:
            dates=[]
            for item in self.state["prior"]:
                if (isinstance(item,dict) and
                    item.get("location_id")==self.state["location_id"] and
                    item.get("disease_name","").casefold()==g["disease"].casefold()):
                    try:
                        dates.append(dt.date.fromisoformat(item["date_reported"]))
                    except (ValueError, KeyError, TypeError):
                        pass
            if not dates:
                # If public observations do not establish chronological context,
                # decline to invent a dated record.
                return {"action":"finish"}
            proposed=(max(dates)+dt.timedelta(days=1)).isoformat()
            self.state["date_reported"]=proposed
            tool,args="create_outbreak_report",{
                "disease_name":g["disease"], "location_id":self.state["location_id"],
                "date_reported":proposed,"reporter_id":self.state["reporter_id"],
                "case_count":g["initial_count"]}
        elif not self.state["created"]:
            return {"action":"finish"}
        elif i==4:
            # The real create API returns only a message, NOT an identifier.
            # Resolve the new ID through an actual, declared read tool.
            tool,args="list_reports_by_disease",{"disease_name":g["disease"]}
        elif not self.state["report_id"]:
            return {"action":"finish"}
        elif i==5:
            tool,args="validate_reporter_credentials",{
                "reporter_id":self.state["reporter_id"]}
        elif i==6:
            tool,args="update_case_count",{
                "report_id":self.state["report_id"],
                "case_count":g["target_count"]}
        elif i==7:
            tool,args="verify_outbreak_report",{
                "report_id":self.state["report_id"]}
        else:
            return {"action":"finish"}
        self.last_action=tool
        self.actions+=1
        return {"action":"call","tool":tool,"arguments":args}

    def observe(self, reply):
        if reply.get("kind")!="observation" or reply.get("tool")!=self.last_action:
            raise ValueError("invalid policy-visible observation")
        parsed=unpack_reply(reply.get("content",""))
        if not parsed.get("success"):
            # Preserve failed tool response; do not fabricate missing success.
            if self.last_action=="verify_outbreak_report":
                self.state["verified"]=False
            return
        data=parsed.get("data")
        if self.last_action=="get_location_by_name":
            self.state["location_id"]=identifier(
                data,self.goal["location"],"location_id")
        elif self.last_action=="list_reporters_by_type":
            self.state["reporter_id"]=identifier(
                data,self.goal["reporter"],"reporter_id")
        elif self.last_action=="list_reports_by_disease":
            if self.actions<=3:
                self.state["prior"]=data if isinstance(data,list) else []
            else:
                # Choose only a UNIQUE report matching the just-created public
                # specification. Refuse ambiguous matches rather than guess.
                candidates=[item for item in (data if isinstance(data,list) else [])
                            if isinstance(item,dict)
                            and item.get("location_id")==self.state["location_id"]
                            and item.get("reporter_id")==self.state["reporter_id"]
                            and item.get("date_reported")==self.state["date_reported"]
                            and item.get("case_count")==self.goal["initial_count"]]
                if len(candidates)==1:
                    self.state["report_id"]=candidates[0].get("report_id")
        elif self.last_action=="create_outbreak_report":
            self.state["created"]=True
            if isinstance(data,dict):
                self.state["report_id"]=data.get("report_id")
            if not self.state["report_id"] and isinstance(parsed.get("report_id"),str):
                self.state["report_id"]=parsed["report_id"]
        elif self.last_action=="verify_outbreak_report":
            self.state["verified"]=True

def docker_worker_args(image, script, payload):
    return [
        "docker","run","-i","--rm","--network","none",
        "--cap-drop","ALL","--security-opt","no-new-privileges",
        "--read-only","--user","65534:65534","--pids-limit","64",
        "--memory","768m","--cpus","1",
        "--tmpfs","/tmp:rw,nosuid,nodev,size=32m",
        "--mount",f"type=bind,src={Path(script).resolve()},dst=/worker.py,readonly",
        "--mount",f"type=bind,src={Path(payload).resolve()},dst=/input.json,readonly",
        image,"python","/worker.py","/input.json"
    ]

def receive(proc, *, timeout=20):
    ready,_,_=select.select([proc.stdout],[],[],timeout)
    if not ready:
        raise TimeoutError("no timely child reply")
    line=proc.stdout.readline()
    if not line or len(line)>4*1024*1024:
        raise RuntimeError("empty/oversized child reply")
    try: return json.loads(line)
    except ValueError as exc: raise RuntimeError("invalid child reply") from exc

def one_episode(public, environment, verifier, arm, image=IMAGE):
    policy=GoalPolicy(public,arm)
    start=time.perf_counter()
    proc=subprocess.Popen(
        docker_worker_args(image,WORKER,environment),
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,
        text=True,bufsize=1)
    observations=[]
    terminal=None
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("worker readiness/privilege mismatch")
        while True:
            action=policy.next_action()
            proc.stdin.write(json.dumps(action,sort_keys=True)+"\n")
            proc.stdin.flush()
            reply=receive(proc)
            if action["action"]=="finish":
                if reply.get("kind")!="private_final_state":
                    raise RuntimeError("missing private terminal state")
                terminal=reply
                break
            policy.observe(reply)
            observations.append({
                "tool":reply["tool"],"ok":reply["ok"],
                "result_sha256":fingerprint(reply.get("content","")),
                "selected_seconds":reply["elapsed_seconds"]})
        proc.stdin.close()
        if proc.wait(timeout=10):
            raise RuntimeError("worker exited nonzero")
    finally:
        if proc.poll() is None: proc.kill()
        if proc.stdin and not proc.stdin.closed: proc.stdin.close()
        if proc.stdout: proc.stdout.close()
    env_seconds=time.perf_counter()-start
    if terminal is None or terminal.get("tool_calls")!=len(observations):
        raise RuntimeError("untrusted state/call-count mismatch")
    for field in ("initial_state","state"):
        if not isinstance(terminal.get(field),dict):
            raise RuntimeError("invalid terminal state type")
    bundle=json.dumps({"initial_state":terminal["initial_state"],
                       "state":terminal["state"]})+"\n"
    # Verification happens ONLY after final action. It is not an observation.
    # Restrict the bridge to the private checker, never the GoalPolicy.
    result,verify_seconds=call_child(image,CHECKER,verifier,input_text=bundle)
    if len(result)!=1 or result[0].get("contract")!="OWI-EC005-TERMINAL-REWARD/1":
        raise RuntimeError("verifier response mismatch")
    r=result[0]
    if r.get("valid") is not True:
        raise RuntimeError("invalid checker result: not a training sample")
    return {
        "arm":["stop","read_only","goal"][arm],
        "propensity":1/3,
        "reward":r["reward"],
        "checks_total":r["checks_total"],
        "checks_passed":r["checks_passed_if_valid"],
        "calls":len(observations),
        "tool_seconds":sum(o["selected_seconds"] for o in observations),
        "environment_container_seconds":env_seconds,
        "verifier_container_seconds":verify_seconds,
        "observations":observations,
        "goal_created_report":policy.state["created"] if arm==2 else False,
        "goal_report_id_learned_from_selected_reply":bool(policy.state["report_id"]) if arm==2 else False,
        "private_state_or_verifier_in_policy":False,
        "policy_kind":"PUBLIC_ONLY_DETERMINISTIC_SCRIPT_NOT_LEARNED",
    }

def run(cfg):
    public=json.loads(Path(cfg.public).read_text())
    if set(public)!={"messages","tools","candidate_read_tool"}:
        raise RuntimeError("unexpected public policy interface")
    assignment=sample_arms(cfg.episodes,cfg.seed)
    rows=[]
    for i,a in enumerate(assignment):
        r=one_episode(public,cfg.environment,cfg.verifier,a)
        r["episode"]=i
        rows.append(r)
    groups=Counter(r["arm"] for r in rows)
    scores={a:round(sum(r["reward"] for r in rows if r["arm"]==a)/groups[a],4)
            for a in groups}
    mean_calls={a:sum(r["calls"] for r in rows if r["arm"]==a)/groups[a]
                for a in groups}
    result={
        "contract":"OWI-EC005D-REALTOOL-PUBLIC-CONDITIONAL-GOAL/1",
        "source_task_public_sha256":fingerprint(public),
        "episodes":len(rows),"seed":cfg.seed,"arm_counts":dict(groups),
        "assigned_propensity":1/3,
        "arm_mean_reward":scores,
        "arm_mean_calls":mean_calls,
        "goal_minus_stop":round(scores["goal"]-scores["stop"],4),
        "goal_better_than_stop":scores["goal"]>scores["stop"],
        "verifier_outcomes_valid":True,
        "training":"NOT_PERFORMED",
        "positive_policy_learning_claim":False,
        "limitation":"single source-pinned task, scripted actions; no LM outcome-only optimization",
        "episodes_data":rows,
    }
    dst=Path(cfg.output);dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--public",required=True)
    p.add_argument("--environment",required=True)
    p.add_argument("--verifier",required=True)
    p.add_argument("--seed",type=int,default=12)
    p.add_argument("--episodes",type=int,default=12)
    p.add_argument("--output",default="build/owi_ec005_realtools/goal_outcomes.json")
    cfg=p.parse_args()
    result=run(cfg)
    print("PUBLIC_GOAL_TERMINAL_RESULT",json.dumps({
        k:v for k,v in result.items() if k!="episodes_data"},sort_keys=True))
if __name__=="__main__":
    main()
