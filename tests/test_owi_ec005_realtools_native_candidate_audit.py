#!/usr/bin/env python3
"""OWI-EC005J source-family scope and no-private-oracle audit tests."""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_candidate_audit import public_candidates
from owi_ec005_realtools_intake import DatasetBoundaryError

class NativeCandidateBoundary(unittest.TestCase):
    def test_rejects_nonpredeclared_and_duplicate_family(self):
        for indices in ((),(2151,2151),(8,),(2151,8),(2151,2301,2449,687,710,2151)):
            with self.subTest(indices=indices):
                with self.assertRaises(DatasetBoundaryError):
                    public_candidates([],indices=indices)

    def test_export_public_schema_not_hidden_checker_or_state(self):
        public={"messages":[{"role":"user","content":"Moderate pending reviews based on authorized policy"}],
                "tools":[{"name":"update_review_moderation_status",
                          "parameters":{"required":["review_id","status"],
                                        "properties":{"review_id":{"type":"string"},
                                                      "status":{"type":"string"}}}}]}
        env={"class_code":"class Secret: SECRET_CHECKER_SOURCE","initial_state":{
            "users":{"SECRET_PRIVATE_USER_ID":{"password":"SECRET_PRIVATE_VALUE"}},
            "reviews":{"REV-1":{"review_id":"SENSITIVE"}}}}
        private={"verifier":{"checklist":[{"check_func":"SECRET_CHECKER_SOURCE"}]}}
        with patch("owi_ec005_realtools_native_candidate_audit.build",
                   return_value=[(2151,"GROUP-SHA",public,env,private)]):
            result=public_candidates([{}],indices=(2151,))
        self.assertEqual(len(result),1)
        x=result[0]
        self.assertEqual(x["original_private_checker_count"],1)
        self.assertEqual(x["row"],2151)
        self.assertFalse(x["original_checker_source_exported"])
        dumped=json.dumps(x)
        for token in ("SECRET_CHECKER_SOURCE","SECRET_PRIVATE_USER_ID",
                      "SECRET_PRIVATE_VALUE","SENSITIVE"):
            self.assertNotIn(token,dumped)
        self.assertIn("Moderate pending reviews",dumped)

    def test_drift_rejected(self):
        public={"messages":[{"role":"user","content":"Moderate user"}],
                "tools":[{"name":"review","parameters":{"required":"not-an-array"}}]}
        env={"class_code":"class Hidden: pass","initial_state":{}}
        private={"verifier":{"checklist":[{"check_func":"checker"}]}}
        with patch("owi_ec005_realtools_native_candidate_audit.build",
                   return_value=[(2151,"H",public,env,private)]):
            with self.assertRaises(DatasetBoundaryError):
                public_candidates([],indices=(2151,))
if __name__=="__main__":
    unittest.main()
