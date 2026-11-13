#!/usr/bin/env python3
"""OWI-EC005J mutation-contrast oracle-separation tests."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_moderation_canary import (
    find_low_rating_review,preflight,ARMS
)

class NativeContrastTest(unittest.TestCase):
    def test_source_public_low_rating_selection(self):
        products=[{"product_id":"A"},{"product_id":"B"}]
        queries=[]
        def respond(pid):
            queries.append(pid)
            if pid=="A":
                return {"success":True,"data":[{"review_id":"A-1","rating":5,
                    "moderation_status":"pending","product_id":"A"}]}
            return {"success":True,"data":[{
                "review_id":"B-2","rating":1,"moderation_status":"pending",
                "product_id":"B","user_id":"PUBLIC-USER"}]}
        found=find_low_rating_review(products,respond)
        self.assertEqual(found,{"review_id":"B-2","product_id":"B","rating":1})
        self.assertEqual(queries,["A","B"])

    def test_wrong_product_or_nonpending_cannot_authorize(self):
        p=[{"product_id":"A"}]
        for row in (
            {"review_id":"X","rating":1,"moderation_status":"approved","product_id":"A"},
            {"review_id":"X","rating":2,"moderation_status":"pending","product_id":"B"},
            {"review_id":"X","rating":"1","moderation_status":"pending","product_id":"A"},
            {"review_id":"X","rating":True,"moderation_status":"pending","product_id":"A"},
        ):
            with self.assertRaises(ValueError):
                find_low_rating_review(p,lambda pid,record=row:{
                    "success":True,"data":[record]})

    def test_private_payload_and_task_policy_change_denied(self):
        p={"messages":[{"role":"user","content":
            "Reject if: The rating is 1 or 2, OR author suspended."}],
            "tools":[{"name":"list_all_products","parameters":{"required":[]}},
                     {"name":"get_reviews_for_product_by_status",
                      "parameters":{"required":["product_id","moderation_status"]}},
                     {"name":"update_review_moderation_status",
                      "parameters":{"required":["review_id","new_status"]}}]}
        self.assertTrue(preflight(p))
        with self.assertRaises(ValueError):
            preflight({**p,"initial_state":{"hidden":"secret"}})
        with self.assertRaises(ValueError):
            preflight({**p,"verifier":"hidden"})
        with self.assertRaises(ValueError):
            preflight({**p,"messages":[{"role":"user","content":"approve all"}]})
        self.assertEqual(set(ARMS),{"stop","reject","approve_wrongly"})

if __name__=="__main__":
    unittest.main()
