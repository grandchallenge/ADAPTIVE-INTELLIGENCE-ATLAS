#!/usr/bin/env python3
"""OWI-EC-005C persistent real tool worker; RUN ONLY in restricted Docker.

A private environment is loaded in the jailed child. The policy receives only
actual selected tool replies. On terminal finish, the trusted orchestrator
receives the final snapshot on a PRIVATE channel; that object must never be
forwarded to the policy, its observations, or its training features.

There is no verifier code, expected answer, or reflection skill in this worker.
"""
from __future__ import annotations
import ast
import copy
import json
import os
import resource
import sys
import time
from pathlib import Path

MAX_COMMAND_BYTES = 65536
MAX_OBSERVATION_CHARS = 8192
MAX_CALLS = 6

def send(data):
    print(json.dumps(data, sort_keys=True, ensure_ascii=False), flush=True)

def initialize(spec):
    if not isinstance(spec, dict) or set(spec) != {
        "class_code", "class_name", "initial_state", "tools"
    }:
        raise ValueError("private verifier or unexpected environment field")
    if not isinstance(spec["initial_state"], dict):
        raise ValueError("initial_state must be a mapping")
    src, name = spec["class_code"], spec["class_name"]
    if not isinstance(src, str) or not isinstance(name, str) or not name.isidentifier():
        raise ValueError("invalid source/class")
    tree = ast.parse(src)
    if not any(isinstance(c, ast.ClassDef) and c.name == name for c in tree.body):
        raise ValueError("declared class not found")
    namespace = {"__name__": "__owi_ec005_jailed_episode__"}
    # This executes external code. DO NOT run this worker outside the jail.
    exec(compile(tree, "<source_locked_external_class>", "exec"), namespace, namespace)
    cls = namespace[name]
    state = copy.deepcopy(spec["initial_state"])
    try:
        obj = cls(state)
    except TypeError:
        obj = cls()
    # Follow the upstream EnvScaler adapter's constructor/state convention.
    for key, value in state.items():
        setattr(obj, key, value)
    allowed = set()
    for t in spec["tools"]:
        if isinstance(t, dict) and t.get("type") == "function":
            item = t.get("function", {})
            if isinstance(item, dict) and isinstance(item.get("name"), str):
                allowed.add(item["name"])
    if not allowed:
        raise ValueError("no advertised tool")
    return obj, allowed

def snapshot(obj):
    return copy.deepcopy({k: v for k, v in vars(obj).items()
                          if not (k.startswith("__") and k.endswith("__"))})

def serve(spec):
    obj, allowed = initialize(spec)
    send({"kind": "ready", "max_calls": MAX_CALLS, "verifier_present": False})
    calls = 0
    for raw in sys.stdin:
        if len(raw) > MAX_COMMAND_BYTES:
            raise ValueError("command too large")
        command = json.loads(raw)
        if not isinstance(command, dict):
            raise ValueError("command object required")
        action = command.get("action")
        if action == "finish":
            if set(command) != {"action"}:
                raise ValueError("finish fields")
            # PRIVILEGED final state: only the orchestrator/verifier may read.
            send({"kind": "private_final_state", "state": snapshot(obj),
                  "tool_calls": calls,
                  "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
            return
        if action != "call" or set(command) != {"action", "tool", "arguments"}:
            raise ValueError("unsupported action")
        if calls >= MAX_CALLS:
            raise ValueError("call budget exceeded")
        name, args = command["tool"], command["arguments"]
        if name not in allowed or not isinstance(args, dict):
            raise ValueError("unknown tool or malformed arguments")
        calls += 1
        started = time.perf_counter()
        try:
            method = getattr(obj, name)
            if not callable(method):
                raise ValueError("uncallable tool")
            reply = str(method(**args))
            ok, error_name = True, None
        except Exception as exc:
            reply, ok, error_name = f"Error: {type(exc).__name__}", False, type(exc).__name__
        elapsed = time.perf_counter() - started
        send({"kind": "observation", "tool": name, "ok": ok,
              "error_type": error_name, "content": reply[:MAX_OBSERVATION_CHARS],
              "truncated": len(reply) > MAX_OBSERVATION_CHARS,
              "elapsed_seconds": elapsed})

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: worker.py /environment.json")
    os.environ.clear()  # no ambient credentials inside child
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    serve(data)

if __name__ == "__main__":
    main()
