#!/usr/bin/env python3
"""OWI-EC-005C terminal private checker; RUN ONLY in isolated Docker.

Follows the published EnvScaler check_func contract: each checklist entry
provides executable Python source defining check_func(final_state), where the
initial_state is an injected global. Only a terminal aggregate scalar result
exits the verifier process. No check_item, expected answer, source or state is
returned to the agent or optimizer. Verifier execution failure is *invalid*,
not silently converted to a valid zero-reward example.
"""
from __future__ import annotations
from copy import deepcopy
import hashlib
import json
import os
import sys
from pathlib import Path

MAX_STATE_BYTES = 4 * 1024 * 1024
MAX_CHECKS = 40
MAX_CODE_CHARS = 120000

def run_verifier(private, state):
    if not isinstance(private, dict) or set(private) != {"verifier", "initial_state"}:
        raise ValueError("invalid private verification bundle")
    if not isinstance(private["initial_state"], dict) or not isinstance(state, dict):
        raise ValueError("expected JSON state objects")
    verifier = private["verifier"]
    if not isinstance(verifier, dict) or verifier.get("kind") != "checklist_func":
        raise ValueError("unsupported verifier kind")
    checklist = verifier.get("checklist")
    if not isinstance(checklist, list) or not 0 < len(checklist) <= MAX_CHECKS:
        raise ValueError("missing/oversized checklist")
    passed, error_types = 0, []
    for item in checklist:
        if not isinstance(item, dict) or not isinstance(item.get("check_func"), str):
            raise ValueError("unrecognized check shape")
        source = item["check_func"]
        if len(source) > MAX_CODE_CHARS:
            raise ValueError("oversized checker")
        namespace = {"initial_state": deepcopy(private["initial_state"])}
        try:
            # Intentionally executed ONLY in verifier's own restricted OS jail.
            exec(source, namespace)
            check = namespace.get("check_func")
            if not callable(check):
                raise TypeError("check_func missing")
            result = check(deepcopy(state))
            if not isinstance(result, bool):
                raise TypeError("check_func did not return bool")
            passed += int(result)
        except Exception as exc:
            error_types.append(type(exc).__name__)
    if error_types:
        # Never pass a broken verifier as a genuine task reward.
        return {"contract": "OWI-EC005-TERMINAL-REWARD/1",
                "valid": False, "reward": None,
                "checks_total": len(checklist),
                "checks_passed_if_valid": None,
                "verifier_execution_errors": len(error_types),
                "error_type_histogram": {t: error_types.count(t)
                                          for t in sorted(set(error_types))},
                "private_check_text_exposed": False}
    return {"contract": "OWI-EC005-TERMINAL-REWARD/1",
            "valid": True, "reward": round(passed / len(checklist), 4),
            "checks_total": len(checklist),
            "checks_passed_if_valid": passed,
            "verifier_execution_errors": 0,
            "private_check_text_exposed": False}

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: verifier.py /private-verifier.json")
    os.environ.clear()
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    raw = sys.stdin.buffer.readline(MAX_STATE_BYTES + 1)
    if len(raw) > MAX_STATE_BYTES or not raw:
        raise SystemExit("invalid state message length")
    state = json.loads(raw)
    if not isinstance(state, dict) or set(state) != {"state"}:
        raise SystemExit("private final state message required")
    result = run_verifier(data, state["state"])
    print(json.dumps(result, sort_keys=True), flush=True)

if __name__ == "__main__":
    main()
