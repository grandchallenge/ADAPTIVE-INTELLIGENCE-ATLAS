#!/usr/bin/env python3
"""Public tool-response discovery for three predeclared training families.

The caller mounts only environment source/state/tools in restricted Docker.
Private verifier bundle is never mounted or read here. Terminal worker state
is discarded without logging; only actual selected tool observation is printed.
This is a diagnostic, not any success/reward claim.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from owi_ec005_realtools_randomized import IMAGE,call_child

PROBES={
    0:("list_user_subscriptions",{"user_id":"USR001"},"USR001"),
    2:("check_user_account_status",{"user_id":"USR002"},"USR002"),
    3:("get_dietary_restriction_by_id",{"restriction_id":"DR5"},"DR5"),
}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",type=Path,required=True)
    args=p.parse_args()
    for idx,(tool,kwargs,needle) in PROBES.items():
        task=args.input_dir/str(idx)
        public=json.loads((task/"public.json").read_text())
        declared={f["name"] for f in public["tools"]}
        if tool not in declared:
            raise ValueError("undeclared public probe")
        prompt=" ".join(m["content"] for m in public["messages"]
                        if m["role"]=="user")
        if needle not in prompt:
            raise ValueError("public task does not authorize probe target")
        cmds=[{"action":"call","tool":tool,"arguments":kwargs},
              {"action":"finish"}]
        rows,_=call_child(IMAGE,"experiments/owi_ec005_realtools_episode_worker.py",
                           task/"environment.json",
                           input_text="".join(json.dumps(c)+"\n" for c in cmds))
        if (len(rows)!=3 or rows[0].get("kind")!="ready" or
            rows[1].get("kind")!="observation" or
            rows[2].get("kind")!="private_final_state"):
            raise RuntimeError("tool IPC mismatch")
        print("HETERO_PUBLIC_OBSERVATION",json.dumps({
            "row_index":idx,"tool":tool,"arguments":kwargs,
            "ok":rows[1]["ok"],
            "content":rows[1]["content"][:4500],
            "truncated":rows[1]["truncated"],
            "private_terminal_state_discarded":True,
            "private_checker_never_mounted":True,
        },sort_keys=True,ensure_ascii=False))
if __name__=="__main__":
    main()
