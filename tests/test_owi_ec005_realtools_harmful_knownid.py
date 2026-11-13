#!/usr/bin/env python3
"""Controlled known-ID association variant invariants."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_harmful_knownid import (
    TARGET,VARIANTS,target_fields,make_variant)
from owi_ec005_realtools_intake import DatasetBoundaryError

def fixture():
    return {"class_code":"class App: pass","class_name":"App","tools":[],
     "initial_state":{
        "users":{"U1":{"_id":"U1","account_status":"active"},
                 "U2":{"_id":"U2","account_status":"active"}},
        "products":{"P1":{"product_id":"P1","name":"A"},
                    "P2":{"product_id":"P2","name":"B"}},
        "subscriptions":{
             "SUB1234":{"subscription_id":"SUB1234","user_id":"U1",
                         "product_id":"P1","subscription_status":"active"},
             "SUB2468":{"subscription_id":"SUB2468","user_id":"U2",
                         "product_id":"P2","subscription_status":"active"}},
        "payments":{"PAY":{"subscription_id":"SUB1234"}},
        "shipments":{"SHIP":{"subscription_id":"SUB1234"}}}}

class KnownIDTest(unittest.TestCase):
    def test_exact_link_removal_and_unaltered_other_records(self):
        orig=fixture()
        self.assertEqual(target_fields(orig),("U1","P1"))
        for name in VARIANTS:
            alt=make_variant(orig,name)
            for field in ("class_code","class_name","tools"):
                self.assertEqual(alt[field],orig[field])
            for field in ("subscriptions","payments","shipments"):
                self.assertEqual(alt["initial_state"][field],
                                 orig["initial_state"][field])
            self.assertIn("U2",alt["initial_state"]["users"])
            self.assertIn("P2",alt["initial_state"]["products"])
            if name=="missing_user":
                self.assertNotIn("U1",alt["initial_state"]["users"])
                self.assertIn("P1",alt["initial_state"]["products"])
            if name=="missing_product":
                self.assertNotIn("P1",alt["initial_state"]["products"])
                self.assertIn("U1",alt["initial_state"]["users"])
            if name=="valid":
                self.assertEqual(alt,orig)
        self.assertIn("U1",orig["initial_state"]["users"])
        self.assertIn("P1",orig["initial_state"]["products"])
    def test_unsupported_or_drift_fails_closed(self):
        with self.assertRaises(DatasetBoundaryError):
            make_variant(fixture(),"unknown")
        original=fixture()
        original["initial_state"]["subscriptions"]["SUB1234"]["subscription_status"]="cancelled"
        with self.assertRaises(DatasetBoundaryError):
            target_fields(original)
        other=fixture()
        del other["initial_state"]["users"]["U1"]
        with self.assertRaises(DatasetBoundaryError):
            make_variant(other,"missing_product")

if __name__=="__main__":
    unittest.main()
