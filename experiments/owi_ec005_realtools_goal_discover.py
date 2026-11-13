#!/usr/bin/env python3
"""Read-only *public* task-action audit for goal-directed intervention design.

No executable class source, verifier, hidden state or skill field is printed.
Complete pinned JSONL digest is verified before the public record is emitted.
Not a task solver, and not a test of policy improvement.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from owi_ec005_realtools_episode_select import choose, split_selected

def present(public):
    prompts = [{"role": m["role"], "content": m["content"][:3500]}
               for m in public["messages"] if m["role"] == "user"]
    signatures = []
    readers = []
    for tool in public["tools"]:
        name = tool["name"]
        if name.startswith(("list_", "get_", "find_", "search_")):
            readers.append({"name": name, "parameters": tool["parameters"]})
            continue
        signatures.append({"name": name, "parameters": tool["parameters"]})
    return {
        "contract": "OWI-EC005-PUBLIC-GOAL-DISCOVERY/1",
        "user_prompts": prompts[:2],
        "mutating_or_other_public_signatures": signatures[:24],
        "public_read_signatures": readers[:32],
        "candidate_read_tool": public["candidate_read_tool"],
        "private_verifier_exposed": False,
        "private_state_exposed": False,
        "mutating_action_performed": False,
        "outcome_measured": False,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--index", type=int, default=1)
    p.add_argument("--lock", type=Path,
                   default=Path("governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    args=p.parse_args()
    row=choose(json.loads(args.lock.read_text()), args.index)
    public, _, _=split_selected(row)
    print("PUBLIC_TASK_ONLY",json.dumps(present(public),ensure_ascii=False,sort_keys=True))

if __name__=="__main__":
    main()
