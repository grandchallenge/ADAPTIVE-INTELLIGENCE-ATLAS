#!/usr/bin/env python3
"""Restricted-container CHILD worker for a real third-party tool environment.

THIS FILE IS ONLY SAFE TO RUN INSIDE AN EPHEMERAL OS CONTAINER with:
  --network none --cap-drop ALL --security-opt no-new-privileges
  --read-only --user 65534:65534 --pids-limit 64 --memory 768m
It executes third-party class_code. The calling workflow must supply only
the environment (no verifier, RSD skills, credentials, or host volumes).
"""
from __future__ import annotations

import ast
import hashlib
import inspect
import json
import os
import resource
import sys
import time
from pathlib import Path


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                       default=lambda obj: type(obj).__name__).encode()).hexdigest()


def choose_read_only_zero_arg_tool(tools, instance):
    eligible = []
    for spec in tools:
        if not isinstance(spec, dict):
            continue
        fn = spec.get("function")
        if not isinstance(fn, dict):
            continue
        name = fn.get("name")
        params = fn.get("parameters", {})
        if not isinstance(name, str) or not name.isidentifier():
            continue
        if not name.startswith(("list_", "get_", "find_", "search_")):
            continue
        if not isinstance(params, dict) or params.get("required", []):
            continue
        attr = getattr(instance, name, None)
        if not callable(attr):
            continue
        try:
            sig = inspect.signature(attr)
        except (ValueError, TypeError):
            continue
        if any(p.default is inspect.Parameter.empty and
               p.kind not in (inspect.Parameter.VAR_POSITIONAL,
                              inspect.Parameter.VAR_KEYWORD)
               for p in sig.parameters.values()):
            continue
        eligible.append((name, attr))
    return eligible


def run_environment(payload):
    if set(payload) != {"class_code", "class_name", "initial_state", "tools"}:
        raise ValueError("hidden/private field or unexpected payload")
    source = payload["class_code"]
    name = payload["class_name"]
    if not isinstance(source, str) or not isinstance(name, str) or not name.isidentifier():
        raise ValueError("invalid class source/identifier")
    tree = ast.parse(source)
    if not any(isinstance(node, ast.ClassDef) and node.name == name
               for node in tree.body):
        raise ValueError("declared class is not defined")
    # Everything below executes UNTRUSTED class source and must be jailed.
    namespace = {"__name__": "__owi_ec005_realtool_sandbox__"}
    exec(compile(tree, "<untrusted-tool-environment>", "exec"), namespace, namespace)
    klass = namespace[name]
    if not isinstance(klass, type):
        raise ValueError("class was not instantiated")
    sig = inspect.signature(klass)
    required = [p for p in sig.parameters.values()
                if p.default is inspect.Parameter.empty and
                p.kind not in (inspect.Parameter.VAR_POSITIONAL,
                               inspect.Parameter.VAR_KEYWORD)]
    if len(required) == 0:
        obj = klass()
    elif len(required) == 1:
        obj = klass(payload["initial_state"])
    else:
        raise ValueError("constructor has unsupported required arguments")
    candidates = choose_read_only_zero_arg_tool(payload["tools"], obj)
    if not candidates:
        raise ValueError("no declared read-only zero-argument tool")
    # Invoke only the FIRST compatible real tool; do not ask a verifier.
    errors = []
    for method_name, fn in candidates[:6]:
        started = time.monotonic()
        try:
            result = fn()
        except Exception as exc:
            errors.append(type(exc).__name__)
            continue
        return {
            "record_type": "OWI-EC005-REALTOOL-CONDITIONAL-SMOKE/1",
            "actual_python_tool_invoked": True,
            "method": method_name,
            "result_type": type(result).__name__,
            "result_sha256": digest(result),
            "elapsed_seconds": time.monotonic() - started,
            "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "attempted_earlier_tools": len(errors),
            "verifier_evaluated": False,
            "outcome_only_policy_trained": False,
        }
    raise RuntimeError("candidate tools failed in isolated sandbox: " +
                       ",".join(errors))


def main():
    if len(sys.argv) != 2:
        raise SystemExit("expected exactly one environment input path")
    # Erase inheritable environment variables (including injected tokens).
    os.environ.clear()
    path = Path(sys.argv[1])
    payload = json.loads(path.read_text())
    print(json.dumps(run_environment(payload), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
