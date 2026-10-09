"""Replay tests for Atlas direct-editorial return recovery."""
import importlib.util
import unittest
from pathlib import Path

p=Path(__file__).resolve().parents[1]/"ci/atlas_direct_return_reconcile.py"
spec=importlib.util.spec_from_file_location("atlas_direct_return_reconcile",p)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

ASSIGN="ATLAS-EDITORIAL-P02-B"
HEAD="ff3ed0972e3637350c9140eaa85de7169fe6ca76"


def issue():
    return {
        "number":327,
        "state":"open",
        "title":"ATLAS-EDITORIAL-P02-B — agent chapter review",
        "body":"GCL-ATLAS-EDITORIAL-AGENT/1\nASSIGNMENT_ID: ATLAS-EDITORIAL-P02-B\n",
        "labels":[{"name":"gcl-pickup:direct-editorial"}],
    }


def fields():
    return [
        {"issue_field_name":"GCL Campaign","value":"ATLAS-EDITORIAL-REVIEW-001"},
        {"issue_field_name":"GCL State","single_select_option":{"name":"AVAILABLE"}},
    ]


def valid_comment(comment_id=12345):
    return {
        "id":comment_id,
        "created_at":"2026-10-09T01:00:00Z",
        "user":{"login":"reviewer42"},
        "body":(
            f"RESULT/1\nassignment_id: {ASSIGN}\n"
            "reviewer_identity: reviewer42 (independent reviewer)\n"
            f"input_head: {HEAD}\n"
            "status: partial\n\nchapter_findings:\n  Proof scope note.\n"
        ),
    }


class ReplayTests(unittest.TestCase):
    def test_replays_valid_missed_result(self):
        r=mod.reconcile(issue(),fields(),[valid_comment()])
        self.assertTrue(r["project"])
        self.assertTrue(r["replayed"])
        self.assertEqual(r["comment_id"],12345)

    def test_skips_invalid_then_accepts_later_valid(self):
        bad=valid_comment(100)
        bad["body"]=bad["body"].replace(HEAD,"main")
        good=valid_comment(200)
        r=mod.reconcile(issue(),fields(),[bad,good])
        self.assertTrue(r["project"])
        self.assertEqual(r["comment_id"],200)
        self.assertEqual(r["examined_result_comments"],2)

    def test_non_result_ignored(self):
        r=mod.reconcile(issue(),fields(),[
            {"id":1,"created_at":"2026-10-09T00:00:00Z","user":{"login":"x"},"body":"hello"}
        ])
        self.assertFalse(r["project"])
        self.assertEqual(r["examined_result_comments"],0)

    def test_closed_issue_not_replayed(self):
        i=issue();i["state"]="closed"
        r=mod.reconcile(i,fields(),[valid_comment()])
        self.assertEqual(r["reason"],"not_open_issue")

    def test_invalid_only_reports_reason(self):
        bad=valid_comment()
        bad["body"]=bad["body"].replace(ASSIGN,"ATLAS-EDITORIAL-P99")
        r=mod.reconcile(issue(),fields(),[bad])
        self.assertFalse(r["project"])
        self.assertEqual(r["rejected"][0]["reason"],"wrong_assignment")


if __name__=="__main__":
    unittest.main()
