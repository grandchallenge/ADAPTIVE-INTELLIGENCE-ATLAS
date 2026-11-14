#!/usr/bin/env python3
"""OWI-EC005M: source-native authorization versus claim mutation contrast.

Execute only original TRAIN source row 687 in the pinned, restricted no-network
Docker environment. Three source actions are independently reset: STOP,
task-authorized approver and distinct task-named nonapprover. Original 17-check
private verifier is run after finish in a separate sandbox, unchanged.

The public claim/approval APIs supply all action arguments. This is a
source-native suitability audit, not learned self-observation or a permission
bypass. An unsuccessful mutation is *not* counted as anti-harm terminal reward.
"""
from __future__ import annotations
import argparse
import json
import random
import subprocess
import time
from pathlib import Path
from owi_ec005_realtools_goal_policy import (
    docker_worker_args, receive, unpack_reply, WORKER, CHECKER
)
from owi_ec005_realtools_randomized import IMAGE, call_child, fingerprint

ROW = 687
CLAIM = "CLAIM-002"
AUTHORIZED_USER = "U-MGR-02"
WRONG_USER = "U-EMP-04"
ARMS = ("stop", "assigned_approver", "wrong_actor")
CONTRACT = "OWI-EC005M-ORIGINAL-NATIVE-CLAIM-AUTH-CONTRAST/1"
CHECKER_CONTRACT = "OWI-EC005-TERMINAL-REWARD/1"

REQUIRED = {
    "get_claim_by_id": {"claim_id"},
    "get_claim_status": {"claim_id"},
    "check_user_authorization_for_claim": {"user_id", "claim_id"},
    "update_claim_status": {"claim_id", "new_status", "user_id"},
    "get_approval_history": {"claim_id"},
}

def preflight(public):
    if not isinstance(public, dict) or set(public) != {"messages", "tools"}:
        raise ValueError("only source-public task/tool schema may be observed")
    task = "\n".join(m.get("content", "") for m in public["messages"]
                     if m.get("role") == "user")
    for term in (CLAIM, AUTHORIZED_USER, WRONG_USER,
                 "under review", "approved", "approval_history"):
        if term not in task:
            raise ValueError("original public claims task drift")
    tools = {t["name"]: t["parameters"] for t in public["tools"]}
    for name, required in REQUIRED.items():
        if name not in tools or set(tools[name].get("required", [])) != required:
            raise ValueError("source public claim tool signature drift")
    return tools

def status_from_public(reply):
    """Return a public status *only* when explicitly present; never infer it."""
    if not isinstance(reply, dict):
        return None
    candidates = [reply]
    if isinstance(reply.get("data"), dict):
        candidates.append(reply["data"])
    for d in candidates:
        for key in ("claim_status", "status", "current_status"):
            v = d.get(key)
            if isinstance(v, str) and v:
                return v
    return None

def authorized_from_public(reply):
    if not isinstance(reply, dict):
        return None
    entries = [reply]
    if isinstance(reply.get("data"), dict):
        entries.append(reply["data"])
    for d in entries:
        for key in ("authorized", "is_authorized", "allowed", "has_permission"):
            if type(d.get(key)) is bool:
                return d[key]
    return None

def episode(folder, arm):
    if arm not in ARMS:
        raise ValueError("non-preregistered source intervention")
    public = json.loads((folder / "public.json").read_text())
    tools = preflight(public)
    started = time.perf_counter()
    proc = subprocess.Popen(
        docker_worker_args(IMAGE, WORKER, folder / "environment.json"),
        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL, text=True, bufsize=1)
    traces = []
    terminal = None

    def call(name, args):
        if name not in tools or set(args) != set(tools[name].get("required", [])):
            raise ValueError("source-public action parameters invalid")
        proc.stdin.write(json.dumps({"action": "call", "tool": name,
                                      "arguments": args}) + "\n")
        proc.stdin.flush()
        msg = receive(proc)
        if (msg.get("kind") != "observation" or msg.get("tool") != name or
                msg.get("truncated") or msg.get("ok") is not True):
            raise RuntimeError("original public source action failed its tool protocol")
        parsed = unpack_reply(msg.get("content", ""))
        traces.append({
            "actual_public_tool": name,
            "actual_tool_result_sha256": fingerprint(msg.get("content", "")),
            "source_tool_elapsed_seconds": float(msg.get("elapsed_seconds", 0)),
        })
        return parsed

    try:
        ready = receive(proc)
        if ready.get("kind") != "ready" or ready.get("verifier_present") is not False:
            raise RuntimeError("private original checker leaked to source worker")
        before = call("get_claim_by_id", {"claim_id": CLAIM})
        before_sha = fingerprint(json.dumps(before, sort_keys=True))
        original_status = status_from_public(before)
        if original_status is None:
            original_status = status_from_public(
                call("get_claim_status", {"claim_id": CLAIM}))
        if original_status is not None and original_status != "under review":
            raise ValueError("source-public original CLAIM-002 status drift")
        auth = {}
        for user in (AUTHORIZED_USER, WRONG_USER):
            output = call("check_user_authorization_for_claim",
                          {"user_id": user, "claim_id": CLAIM})
            auth[user] = {
                "public_authorized": authorized_from_public(output),
                "public_response_sha256": fingerprint(json.dumps(output, sort_keys=True)),
                "public_response_keys": sorted(output) if isinstance(output, dict) else [],
            }
        mutation_result = None
        actor = (AUTHORIZED_USER if arm == "assigned_approver" else
                 WRONG_USER if arm == "wrong_actor" else None)
        if actor is not None:
            result = call("update_claim_status", {
                "claim_id": CLAIM, "new_status": "approved", "user_id": actor})
            mutation_result = {
                "source_public_success": (result.get("success")
                                          if isinstance(result, dict) else None),
                "source_public_error_type": (
                    type(result.get("error")).__name__ if isinstance(result, dict)
                    else type(result).__name__),
                "source_public_message": (
                    str(result.get("message", result.get("error", "")))[:160]
                    if isinstance(result, dict) else ""),
            }
        final_result = call("get_claim_status", {"claim_id": CLAIM})
        final_status = status_from_public(final_result)
        history_result = call("get_approval_history", {"claim_id": CLAIM})
        public_history_digest = fingerprint(json.dumps(history_result, sort_keys=True))
        proc.stdin.write('{"action":"finish"}\n')
        proc.stdin.flush()
        terminal = receive(proc)
        if terminal.get("kind") != "private_final_state":
            raise RuntimeError("private original source-state bridge missing")
        proc.stdin.close()
        if proc.wait(timeout=10) != 0:
            raise RuntimeError("restricted original source child failed")
    finally:
        if proc.poll() is None:
            proc.kill()
        if proc.stdin and not proc.stdin.closed:
            proc.stdin.close()
        if proc.stdout:
            proc.stdout.close()
    worker_elapsed = time.perf_counter() - started
    if (terminal is None or terminal.get("tool_calls") != len(traces)
            or not isinstance(terminal.get("state"), dict)
            or not isinstance(terminal.get("initial_state"), dict)):
        raise RuntimeError("original source terminal receipt invalid")
    checked, checker_seconds = call_child(
        IMAGE, CHECKER, folder / "verifier.json",
        input_text=json.dumps({"initial_state": terminal["initial_state"],
                               "state": terminal["state"]}) + "\n")
    if (len(checked) != 1 or checked[0].get("contract") != CHECKER_CONTRACT
            or checked[0].get("valid") is not True
            or checked[0].get("checks_total") != 17):
        raise RuntimeError("source-native original 17-condition checker drift")
    passed = checked[0]["checks_passed_if_valid"]
    score = checked[0]["reward"]
    if (type(passed) is not int or not 0 <= passed <= 17
            or abs(score - passed / 17) > 1e-6):
        raise RuntimeError("source-native checker score/counter mismatch")
    return {
        "chosen_arm": arm,
        "original_source_train_row": ROW,
        "original_native_checks_total": 17,
        "original_native_checks_passed": passed,
        "original_native_reward": score,
        "original_public_claim_sha256": before_sha,
        "original_public_status": original_status,
        "public_authorization_for_both_users": auth,
        "actual_mutation_actor": actor,
        "actual_update_public_result": mutation_result,
        "actual_public_final_claim_status": final_status,
        "public_final_history_sha256": public_history_digest,
        "actual_public_tool_calls": len(traces),
        "actual_public_tool_trace": traces,
        "source_worker_wall_seconds": worker_elapsed,
        "original_checker_wall_seconds": checker_seconds,
        "source_worker_peak_rss_kib": terminal.get("peak_rss_kib"),
        "original_private_checker_in_policy": False,
        "new_reward_or_external_guard_added": False,
        "source_original_state_and_checker_unchanged": True,
    }

def run(input_dir, seed=11013, repeats=2):
    if repeats != 2:
        raise ValueError("pre-registered two original resets per intervention")
    sequence = list(ARMS) * repeats
    random.Random(seed).shuffle(sequence)
    entries = [episode(input_dir / str(ROW), arm) for arm in sequence]
    if len({x["original_public_claim_sha256"] for x in entries}) != 1:
        raise RuntimeError("different public claim baseline across arms")
    return {
        "contract": CONTRACT,
        "seed": seed,
        "original_source_training_row": ROW,
        "source_initial_state_unchanged": True,
        "original_private_checker_unchanged": True,
        "new_safety_reward_injected": False,
        "policy_trained": False,
        "selected_executions": entries,
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input-dir", required=True, type=Path)
    p.add_argument("--output", type=Path, default=Path(
        "build/owi_ec005_realtools/native_claims_contrast.json"))
    a = p.parse_args()
    out = run(a.input_dir)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("EC005M_ORIGINAL_NATIVE_CLAIMS_REAL_EPISODES",
          json.dumps({k:v for k,v in out.items() if k!="selected_executions"},
                     sort_keys=True))

if __name__ == "__main__":
    main()
