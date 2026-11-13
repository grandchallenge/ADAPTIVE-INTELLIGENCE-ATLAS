#!/usr/bin/env python3
"""Adversarial source-isolation tests; no third-party environment execution."""
import hashlib
import io
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments"))
from owi_ec005_realtools_intake import (
    DatasetBoundaryError, audit_lines, public_view, private_inventory,
    canonical, remote_lines,
)


SECRET = "CANARY_SUPERVISION_SENTINEL_UNREACHABLE"


def specimen():
    return {
        "prompt": [{"role": "system", "content": "Operate tools carefully."},
                   {"role": "user", "content": "Find and repair the failing case."}],
        "extra_info": {
            "environment": {"tools": [{"name": "exec", "code": SECRET}],
                            "state": {"hidden_answer": SECRET}},
            "verifier": {"expected": SECRET},
            "rsd_skill": SECRET,
            "rsd_skills": [SECRET],
            "rsd_skill_meta": {"critique": SECRET},
        },
        "reward_model": {"style": "rule", "target": SECRET},
    }


class IntakeInvariantTests(unittest.TestCase):
    def test_private_verifier_and_skills_cannot_enter_public_view(self):
        row = specimen()
        agent = public_view(row)
        dump = canonical(agent)
        self.assertNotIn(SECRET.encode(), dump)
        for name in ("extra_info", "environment", "verifier", "rsd_skill"):
            self.assertNotIn(name, agent)
        private = private_inventory(row)
        self.assertTrue(private["has_skill_fields"])
        self.assertNotIn(SECRET, str(private))

    def test_nonexecuting_audit_and_source_hash(self):
        row = specimen()
        raw = (json.dumps(row) + "\n").encode()
        result = audit_lines(iter([raw]), source_revision="offline-fixture")
        self.assertEqual(result["raw_file_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(result["counts"]["valid_tasks"], 1)
        self.assertEqual(result["counts"]["private_skill_bearing_records"], 1)
        self.assertEqual(result["code_execution"], "none")
        self.assertEqual(result["scientific_acceptance"], "NOT_EVALUATED")
        self.assertNotIn(SECRET, json.dumps(result))

    def test_duplicate_public_task_detection(self):
        raw = (json.dumps(specimen()) + "\n").encode()
        report = audit_lines([raw, raw])
        self.assertEqual(report["counts"]["repeated_public_prompts"], 1)
        self.assertEqual(report["counts"]["valid_tasks"], 2)

    def test_reject_private_content_in_prompt_schema(self):
        row = specimen()
        row["prompt"][0]["rsd_skill"] = SECRET
        with self.assertRaises(DatasetBoundaryError):
            public_view(row)

    def test_reject_missing_verifier(self):
        row = specimen()
        del row["extra_info"]["verifier"]
        with self.assertRaises(DatasetBoundaryError):
            private_inventory(row)

    def test_source_digest_cannot_be_replaced(self):
        raw = (json.dumps(specimen()) + "\n").encode()
        with self.assertRaisesRegex(DatasetBoundaryError, "SHA256 mismatch"):
            audit_lines([raw], sha256_expected="0" * 64)

    def test_deny_oversized_untrusted_record(self):
        with self.assertRaisesRegex(DatasetBoundaryError, "oversized"):
            audit_lines([b"x" * (16 * 1024 * 1024 + 1)])

    def test_reject_malformed_json(self):
        with self.assertRaisesRegex(DatasetBoundaryError, "invalid JSONL"):
            audit_lines([b"{not-json}\n"])

    def test_reject_non_sha_remote_revision_without_network(self):
        with self.assertRaisesRegex(DatasetBoundaryError, "40-hex"):
            next(remote_lines("main"))


if __name__ == "__main__":
    unittest.main()
