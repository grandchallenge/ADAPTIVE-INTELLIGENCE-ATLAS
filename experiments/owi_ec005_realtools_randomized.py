#!/usr/bin/env python3
"""OWI-EC005C: randomized *chosen-action* real-tool/terminal-outcome replay.

Executed on a trusted GitHub Actions runner; external Python is NEVER imported
here. The policy-visible input is public.json only. The environment source and
private checklist enter disjoint no-network Docker children. The host transports
a final-state snapshot directly from child A to child B and discards it before
writing results. The agent cannot request verifier calls or inspect state.

This is an intervention and terminal-reward IPC smoke, NOT a language-agent
policy or positive causal result. The forced actions are stop, probe, retry.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import random
import subprocess
import time
from collections import Counter
from pathlib import Path

IMAGE = "python@sha256:935c3c5b12357a7e10caa9c1e6ca5692344d97cf229832ef584be2cec9fc03df"
CONTRACT = "OWI-EC005-REALTOOL-CHOSEN-OUTCOME/1"

def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                           separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def call_child(image, script, datafile, *, input_text="", timeout=30):
    source = Path(script).resolve()
    payload = Path(datafile).resolve()
    cmd = [
        "docker", "run", "-i", "--rm", "--network", "none", "--cap-drop", "ALL",
        "--security-opt", "no-new-privileges", "--read-only",
        "--user", "65534:65534", "--pids-limit", "64", "--memory", "768m",
        "--cpus", "1", "--tmpfs", "/tmp:rw,nosuid,nodev,size=32m",
        "--mount", f"type=bind,src={source},dst=/worker.py,readonly",
        "--mount", f"type=bind,src={payload},dst=/input.json,readonly",
        image, "python", "/worker.py", "/input.json"
    ]
    started = time.perf_counter()
    try:
        p = subprocess.run(cmd, input=input_text, capture_output=True,
                           text=True, timeout=timeout, check=False)
    except subprocess.TimeoutExpired as ex:
        raise RuntimeError("restricted tool/verifier child timed out") from ex
    elapsed = time.perf_counter() - started
    if p.returncode:
        # Never emit subprocess stderr: untrusted code could print secrets.
        raise RuntimeError(f"restricted child failed, exit={p.returncode}, "
                           f"stderr_sha256={hashlib.sha256(p.stderr.encode()).hexdigest()}")
    if len(p.stdout) > 4 * 1024 * 1024:
        raise RuntimeError("child output bound exceeded")
    try:
        rows = [json.loads(line) for line in p.stdout.splitlines() if line.strip()]
    except ValueError as exc:
        raise RuntimeError("invalid restricted child response framing") from exc
    return rows, elapsed

def one_episode(public, environment_path, verifier_path, worker, checker,
                image, arm, *, task_hash):
    if arm not in (0, 1, 2):
        raise ValueError("invalid arm")
    candidate = public["candidate_read_tool"]
    tools = {t["name"]: t for t in public["tools"]}
    if candidate not in tools or tools[candidate].get("parameters", {}).get("required"):
        raise ValueError("public read-only candidate schema invalid")
    calls = arm  # 0 stop, 1 probe, 2 probe + same-tool retry
    commands = [{"action": "call", "tool": candidate, "arguments": {}}
                for _ in range(calls)] + [{"action": "finish"}]
    transcript = "".join(json.dumps(action, sort_keys=True) + "\n"
                         for action in commands)
    rows, env_elapsed = call_child(image, worker, environment_path,
                                   input_text=transcript)
    if len(rows) != calls + 2 or rows[0].get("kind") != "ready":
        kinds = [(x.get("kind") if x.get("kind") in (
            "ready", "observation", "private_final_state") else "UNTRUSTED")
            for x in rows if isinstance(x, dict)]
        raise RuntimeError(f"environment IPC protocol drift: n={len(rows)}, kinds={kinds}")
    if rows[0].get("verifier_present") is not False:
        raise RuntimeError("verifier contaminated environment child")
    obs = rows[1:-1]
    if any(x.get("kind") != "observation" or x.get("tool") != candidate for x in obs):
        raise RuntimeError("unrecognized selected action observation")
    terminal = rows[-1]
    if terminal.get("kind") != "private_final_state" or not isinstance(
            terminal.get("state"), dict):
        raise RuntimeError("private final state missing")
    if terminal["tool_calls"] != calls:
        raise RuntimeError("conditional tool execution count mismatch")
    private_state = terminal["state"]
    if not isinstance(terminal.get("initial_state"), dict):
        raise RuntimeError("missing post-constructor initial state")
    private_initial = terminal["initial_state"]
    private_digest = fingerprint(private_state)
    # The terminal state is sent to an entirely separate, jailed process.
    # This is a trusted host data bridge, not an agent-facing observation.
    checker_input = json.dumps({"state": private_state,
                                "initial_state": private_initial}) + "\n"
    result, check_elapsed = call_child(
        image, checker, verifier_path, input_text=checker_input)
    if len(result) != 1 or result[0].get("contract") != "OWI-EC005-TERMINAL-REWARD/1":
        raise RuntimeError("verifier IPC contract drift")
    outcome = result[0]
    if outcome.get("valid") is not True or outcome.get("reward") is None:
        raise RuntimeError("private verifier did not produce a valid terminal score")
    if outcome.get("private_check_text_exposed") is not False:
        raise RuntimeError("private check-text leakage")
    return {
        "arm": ("stop", "probe", "probe_retry")[arm],
        "chosen_action_probability": 1/3,
        "randomized": True,
        "task_public_sha256": task_hash,
        "real_tool_calls": calls,
        "successful_tool_calls": sum(bool(x["ok"]) for x in obs),
        "observation_sha256": [fingerprint({
            "content": x["content"], "ok": x["ok"], "tool": x["tool"]})
            for x in obs],
        "actual_tool_seconds": sum(float(x["elapsed_seconds"]) for x in obs),
        "environment_container_seconds": env_elapsed,
        "private_verifier_container_seconds": check_elapsed,
        "child_peak_rss_kib": terminal["peak_rss_kib"],
        "terminal_reward": outcome["reward"],
        "terminal_checks": outcome["checks_total"],
        "terminal_checks_passed": outcome["checks_passed_if_valid"],
        "private_state_sha256_audit_only": private_digest,
        "private_target_in_policy_features": False,
        "policy_model_trained": False,
    }

def sample_arms(episodes, seed):
    if episodes < 9:
        raise ValueError("require >=9 randomized episodes for support smoke")
    rng = random.Random(seed)
    arms = [rng.randrange(3) for _ in range(episodes)]
    if set(arms) != {0, 1, 2}:
        raise ValueError("seeded random schedule lacks full arm support")
    return arms

def run(config):
    public = json.loads(Path(config.public).read_text())
    if set(public) != {"messages", "tools", "candidate_read_tool"}:
        raise ValueError("unexpected policy-visible field")
    task_hash = fingerprint(public)
    arms = sample_arms(config.episodes, config.seed)
    rows = []
    for i, arm in enumerate(arms):
        row = one_episode(public, config.environment, config.verifier,
                          config.worker, config.checker, config.image,
                          arm, task_hash=task_hash)
        row["episode"] = i
        rows.append(row)
    counts = Counter(row["arm"] for row in rows)
    arm_reward_means = {
        arm: sum(row["terminal_reward"] for row in rows
                 if row["arm"] == arm)/counts[arm] for arm in counts
    }
    # Audit only: do not make private-state hashes available to any controller.
    by_arm_states = {arm: set(row["private_state_sha256_audit_only"]
                             for row in rows if row["arm"] == arm)
                     for arm in counts}
    same_state = all(len(x) == 1 for x in by_arm_states.values()) and (
        len(set(next(iter(x)) for x in by_arm_states.values())) == 1)
    for row in rows:
        row.pop("private_state_sha256_audit_only", None)
    report = {
        "contract": CONTRACT,
        "seed": config.seed, "episodes": len(rows),
        "arms": dict(counts),
        "chosen_action_propensity": 1/3,
        "randomization": "independent seeded assignment before episode execution",
        "selected_tool": public["candidate_read_tool"],
        "public_task_sha256": task_hash,
        "arm_reward_means": arm_reward_means,
        "identical_terminal_states_across_arms": same_state,
        "complete_private_verification": True,
        "policy_optimization": "NOT_PERFORMED",
        "scientific_claim": "REAL_TOOL_RANDOMIZED_REWARD_PIPELINE_ONLY",
        "limitations": [
            "one source-locked repeated task; not 51-family transfer",
            "fixed nonadaptive actions; no language-model policy or learning",
            "read-only probe controls are not expected to improve task state",
            "no fault injection or held-out intervention mechanisms yet",
            "observed tool times and container wall time are not hardware FLOPs",
        ],
        "episodes_data": rows,
    }
    # Preserve labels/outcome only in a research-evaluator artifact, never actor inputs.
    dest = Path(config.output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return report

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--public", required=True)
    ap.add_argument("--environment", required=True)
    ap.add_argument("--verifier", required=True)
    ap.add_argument("--worker", default="experiments/owi_ec005_realtools_episode_worker.py")
    ap.add_argument("--checker", default="experiments/owi_ec005_realtools_terminal_verifier.py")
    ap.add_argument("--image", default=IMAGE)
    ap.add_argument("--episodes", type=int, default=12)
    ap.add_argument("--seed", type=int, default=12)
    ap.add_argument("--output", default="build/owi_ec005_realtools/outcome_episodes.json")
    args = ap.parse_args()
    result = run(args)
    print(json.dumps({k: v for k, v in result.items() if k != "episodes_data"},
                     sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
