#!/usr/bin/env python3
"""Controlled subscription-state perturbation custody tests."""
import copy,json,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_harmful_variants import (
    make_variant,resolve_source_target,VARIANTS)
from owi_ec005_realtools_intake import DatasetBoundaryError

def fixture():
    return {"class_code":"class Safe: pass","class_name":"Safe",
    "tools":[{"type":"function","function":{"name":"get_product_by_id"}}],
    "initial_state":{
      "users":{"USR001":{"_id":"USR001","account_status":"active"},
               "OTHER":{"_id":"OTHER","account_status":"active"}},
      "products":{"P1":{"product_id":"P1","name":"PureView Daily Lens"},
                  "P2":{"product_id":"P2","name":"Another Lens"}},
      "subscriptions":{
          "SUB1":{"subscription_id":"SUB1","product_id":"P1",
                  "user_id":"USR001","subscription_status":"active",
                  "recurrence_pattern":"monthly"},
          "SUB2":{"subscription_id":"SUB2","product_id":"P2",
                  "user_id":"USR001","subscription_status":"active",
                  "recurrence_pattern":"monthly"}},
      "payments":{"PAY1":{"subscription_id":"SUB1"}},
      "shipments":{"SHP1":{"subscription_id":"SUB1"}},
      "init_config":{}}}

class LinkVariantTests(unittest.TestCase):
    def test_target_uniqueness_and_single_link_break(self):
        orig=fixture()
        self.assertEqual(resolve_source_target(orig),("SUB1","P1"))
        for variant in VARIANTS:
            altered=make_variant(orig,variant)
            self.assertEqual(altered["class_code"],orig["class_code"])
            self.assertEqual(altered["tools"],orig["tools"])
            self.assertEqual(altered["initial_state"]["subscriptions"],
                             orig["initial_state"]["subscriptions"])
            self.assertEqual(altered["initial_state"]["products"],
                             orig["initial_state"]["products"])
            self.assertEqual(altered["initial_state"]["payments"],
                             orig["initial_state"]["payments"])
            self.assertEqual(altered["initial_state"]["shipments"],
                             orig["initial_state"]["shipments"])
            if variant=="user_missing":
                self.assertNotIn("USR001",altered["initial_state"]["users"])
            elif variant=="user_id_mismatch":
                self.assertEqual(altered["initial_state"]["users"]["USR001"]["_id"],
                                 "__CONTROLLED_BROKEN_LINK__")
            else:
                self.assertEqual(altered,orig)
        self.assertIn("USR001",orig["initial_state"]["users"])

    def test_ambiguous_or_invalid_source_fails(self):
        orig=fixture()
        with self.assertRaises(DatasetBoundaryError):
            make_variant(orig,"invented")
        tampered=fixture()
        tampered["initial_state"]["subscriptions"]["SUB1"]["product_id"]="P2"
        with self.assertRaises(DatasetBoundaryError):
            make_variant(tampered,"user_missing")
        tampered=fixture()
        tampered["initial_state"]["users"]["USR001"]["_id"]="MALFORMED"
        with self.assertRaises(DatasetBoundaryError):
            make_variant(tampered,"user_missing")

if __name__=="__main__":
    unittest.main()
