#!/usr/bin/env python3
"""Adversarial tests for selected-action real-tool and private reward separation."""
from __future__ import annotations
import io
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments"))
from owi_ec005_realtools_episode_worker import serve
from owi_ec005_realtools_terminal_verifier import run_verifier
from owi_ec005_realtools_episode_select import split_selected
from owi_ec005_realtools_randomized import sample_arms

SENTINEL = "PRIVATE_VERIFIER_TARGET_MUST_NEVER_ENTER_POLICY"

def specimen():
    code = (
        "class Fixture:\n"
        "    def __init__(self, initial_state):\n"
        "        self.records = list(initial_state['records'])\n"
        "        self.initialized = True\n"
        "    def list_records(self):\n"
        "        return list(self.records)\n"
        "    def update_record(self, index, value):\n"
        "        self.records[index] = value\n"
        "        return 'updated'\n"
    )
    tools = [
        {"type": "function", "function": {
            "name": "list_records",
            "parameters": {"type": "object", "required": [], "properties": {}}}},
        {"type": "function", "function": {
            "name": "update_record",
            "parameters": {"type": "object", "required": ["index", "value"],
                           "properties": {"index": {"type": "integer"},
                                          "value": {"type": "integer"}}}}}
    ]
    checker = ("def check_func(final_state):\n"
               "    return (final_state['records'][0] == 4 and "
               "initial_state['records'][0] == 1 and "
               "initial_state['initialized'])\n")
    return {
        "prompt": [{"role": "system", "content": "Use the tools."},
                   {"role": "user", "content": "Update the first record."}],
        "extra_info": {
            "environment": {
                "class_code": code, "class_name": "Fixture",
                "initial_state": {"records": [1, 2]}, "tools": tools},
            "verifier": {
                "kind": "checklist_func",
                "checklist": [{"check_item": SENTINEL, "check_func": checker}],
            },
            "rsd_skill": SENTINEL,
        },
    }

def simulate(payload, actions):
    private, public = [], []
    stdin = io.StringIO("".join(json.dumps(a) + "\n" for a in actions))
    stdout = io.StringIO()
    with patch.object(sys, "stdin", stdin), patch.object(sys, "stdout", stdout):
        serve(payload)
    messages = [json.loads(s) for s in stdout.getvalue().splitlines()]
    return messages

class Tests(unittest.TestCase):
    def test_source_selector_keeps_private_checker_out_of_policy(self):
        row = specimen()
        public, environment, private = split_selected(row)
        self.assertEqual(public["candidate_read_tool"], "list_records")
        self.assertEqual(set(environment), {
            "class_code", "class_name", "initial_state", "tools"})
        self.assertEqual(set(private), {"verifier"})
        self.assertNotIn(SENTINEL, json.dumps(public))
        self.assertNotIn(SENTINEL, json.dumps(environment))
        self.assertIn(SENTINEL, json.dumps(private))

    def test_repeated_stateful_calls_and_terminal_snapshot(self):
        _, env, private = split_selected(specimen())
        rows = simulate(env, [
            {"action": "call", "tool": "list_records", "arguments": {}},
            {"action": "call", "tool": "update_record", "arguments": {
                "index": 0, "value": 4}},
            {"action": "finish"},
        ])
        self.assertEqual(len(rows), 4)
        self.assertEqual([r["kind"] for r in rows],
                         ["ready", "observation", "observation", "private_final_state"])
        self.assertTrue(rows[1]["ok"])
        self.assertEqual(rows[-1]["tool_calls"], 2)
        self.assertEqual(rows[-1]["state"]["records"], [4, 2])
        self.assertEqual(rows[-1]["initial_state"]["records"], [1, 2])
        self.assertTrue(rows[-1]["initial_state"]["initialized"])
        self.assertNotIn(SENTINEL, json.dumps(rows))
        outcome = run_verifier(private, {"initial_state": rows[-1]["initial_state"],
                                         "state": rows[-1]["state"]})
        self.assertTrue(outcome["valid"])
        self.assertEqual(outcome["reward"], 1.0)
        self.assertEqual(outcome["checks_passed_if_valid"], 1)
        self.assertNotIn(SENTINEL, json.dumps(outcome))

    def test_stop_yields_real_private_zero_reward(self):
        _, env, private = split_selected(specimen())
        rows = simulate(env, [{"action": "finish"}])
        outcome = run_verifier(private, {"initial_state": rows[-1]["initial_state"],
                                         "state": rows[-1]["state"]})
        self.assertEqual(rows[-1]["tool_calls"], 0)
        self.assertTrue(outcome["valid"])
        self.assertEqual(outcome["reward"], 0.0)

    def test_broken_checker_is_not_valid_negative_training_example(self):
        row = specimen()
        row["extra_info"]["verifier"]["checklist"][0]["check_func"] = (
            "def check_func(final_state):\n    raise KeyError('missing')\n")
        _, env, private = split_selected(row)
        rows = simulate(env, [{"action": "finish"}])
        outcome = run_verifier(private, {"initial_state": rows[-1]["initial_state"],
                                         "state": rows[-1]["state"]})
        self.assertFalse(outcome["valid"])
        self.assertIsNone(outcome["reward"])
        self.assertEqual(outcome["verifier_execution_errors"], 1)

    def test_randomized_action_support_and_reproducibility(self):
        first = sample_arms(12, seed=12)
        self.assertEqual(first, sample_arms(12, seed=12))
        self.assertEqual(set(first), {0, 1, 2})
        self.assertEqual(len(first), 12)

    def test_reject_undeclared_tool_execution(self):
        _, env, _ = split_selected(specimen())
        with self.assertRaises(ValueError):
            simulate(env, [{"action": "call", "tool": "open_socket",
                            "arguments": {}}, {"action": "finish"}])

if __name__ == "__main__":
    unittest.main()
