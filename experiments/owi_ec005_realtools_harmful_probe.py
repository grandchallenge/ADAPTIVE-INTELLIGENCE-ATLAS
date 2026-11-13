#!/usr/bin/env python3
"""Live PUBLIC-only association checks in controlled source-locked variants.

Runs untrusted external tool class ONLY inside existing restricted Docker.
Never mounts the private verifier and explicitly discards final private state.
The actor's target and product are discovered via actual selected public tools,
not the private fixture manifest.
"""
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
from owi_ec005_realtools_heterogeneous_trial import Policy
from owi_ec005_realtools_goal_policy import (
    docker_worker_args,receive,WORKER,unpack_reply)
from owi_ec005_realtools_randomized import IMAGE
from owi_ec005_realtools_harmful_variants import VARIANTS

def inspect_variant(folder):
    public=json.loads((folder/"public.json").read_text())
    p=Policy(0,public,"probe")
    proc=subprocess.Popen(docker_worker_args(IMAGE,WORKER,
                           folder/"environment.json"),
                          stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                          stderr=subprocess.DEVNULL,text=True,bufsize=1)
    declared=[]
    check=None
    try:
        ready=receive(proc)
        if ready.get("kind")!="ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("worker privacy invariant")
        while len(declared)<3:
            command=p.next_action()
            if command["action"]!="call":
                break
            proc.stdin.write(json.dumps(command)+"\n");proc.stdin.flush()
            reply=receive(proc)
            if reply.get("kind")!="observation":
                raise RuntimeError("missing actual public observation")
            p.observe(reply)
            declared.append(command["tool"])
            if command["tool"]=="check_subscription_links":
                dat=unpack_reply(reply.get("content",""))
                data=dat.get("data")
                check={"success":dat.get("success") is True,
                       "user_linked":data.get("user_linked")
                           if isinstance(data,dict) else None,
                       "product_linked":data.get("product_linked")
                           if isinstance(data,dict) else None,
                       "policy_authorizes_cancel":p.state["link_valid"]}
        proc.stdin.write('{"action":"finish"}\n');proc.stdin.flush()
        private=receive(proc)
        if private.get("kind")!="private_final_state":
            raise RuntimeError("no private terminal transport")
        proc.stdin.close()
        if proc.wait(timeout=10):
            raise RuntimeError("worker failure")
    finally:
        if proc.poll() is None:proc.kill()
        if proc.stdin and not proc.stdin.closed:proc.stdin.close()
        if proc.stdout:proc.stdout.close()
    return {"observed_tool_sequence":declared,
            "public_check":check,
            "public_target_resolved":bool(p.state["target_subscription"]),
            "private_terminal_state_discarded":True,
            "private_verifier_never_loaded":True}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",required=True,type=Path)
    a=p.parse_args()
    for variant in VARIANTS:
        got=inspect_variant(a.input_dir/variant)
        print("REAL_SUBSCRIPTION_LINK_PUBLIC_REPLAY",json.dumps({
            "variant_host_only_for_experimental_audit":variant,
            **got},sort_keys=True))

if __name__=="__main__":
    main()
