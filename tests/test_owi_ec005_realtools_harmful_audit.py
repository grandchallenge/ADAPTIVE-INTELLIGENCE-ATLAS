#!/usr/bin/env python3
"""Safety and privacy contracts for source-locked subscription audit."""
import json,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_harmful_audit import find_related_records,USER
from owi_ec005_realtools_intake import DatasetBoundaryError

class AuditTests(unittest.TestCase):
    def test_only_fields_and_target_match_flags_exported(self):
        env={"initial_state":{"subscriptions":{
            "SUB-ABC":{"subscription_id":"SUB-ABC","user_id":USER,
                "product_id":"P123","subscription_status":"active",
                "customer_email":"SENSITIVE@example.com"},
            "SUB-DEF":{"subscription_id":"SUB-DEF","user_id":"OTHER",
                "product_id":"P456","subscription_status":"cancelled"}},
            "payment_records":[{"secret":"PRIVATE_AUTHORIZATION_TOKEN"}]}}
        report=find_related_records(env)
        dumped=json.dumps(report)
        self.assertEqual(report["collection_shapes"]["subscriptions"]["entries"],2)
        self.assertEqual(len(report["candidate_subscription_records"]),2)
        self.assertIn("customer_email",dumped)
        self.assertNotIn("SENSITIVE@example.com",dumped)
        self.assertNotIn("PRIVATE_AUTHORIZATION_TOKEN",dumped)
        self.assertNotIn("SUB-ABC",dumped)
        self.assertNotIn("P123",dumped)
    def test_missing_initial_state_fails(self):
        with self.assertRaises(KeyError):
            find_related_records({})
        with self.assertRaises(DatasetBoundaryError):
            find_related_records({"initial_state":[]})

if __name__=="__main__":
    unittest.main()
