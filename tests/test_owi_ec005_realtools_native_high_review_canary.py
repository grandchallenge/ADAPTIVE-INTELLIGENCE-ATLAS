#!/usr/bin/env python3
"""Public high-review selection excludes inactive and Home-refill exceptions."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_high_review_canary import eligible_high

class HighReviewNativeTests(unittest.TestCase):
    def test_only_active_high_non_exception_authorized(self):
        products=[
            {"product_id":"P-HOME","category":"Home"},
            {"product_id":"P-EL","category":"Electronics"},
        ]
        result={
            "P-HOME":{"data":[{"review_id":"HOME-1","user_id":"U1",
                    "product_id":"P-HOME","rating":5,"review_text":"refills quick",
                    "moderation_status":"pending"}]},
            "P-EL":{"data":[{"review_id":"EL-2","user_id":"U2",
                    "product_id":"P-EL","rating":4,"review_text":"fine",
                    "moderation_status":"pending"}]}}
        def get_user(uid):
            return {"success":True,"data":{"user_id":uid,"account_status":"active"}}
        value=eligible_high(products,lambda pid:result[pid],get_user)
        self.assertEqual(value["review_id"],"EL-2")
        self.assertEqual(value["rating"],4)
        self.assertEqual(value["user_id"],"U2")

    def test_absent_or_inactive_author_causes_abstention(self):
        p=[{"product_id":"P","category":"Electronics"}]
        raw={"data":[{"review_id":"R1","user_id":"U1","product_id":"P",
                      "rating":5,"review_text":"good","moderation_status":"pending"}]}
        for state in ("suspended","closed","banned",None):
            with self.subTest(state=state):
                with self.assertRaises(ValueError):
                    eligible_high(p,lambda pid:raw,
                        lambda uid:{"data":{"user_id":uid,"account_status":state}})
        with self.assertRaises(ValueError):
            eligible_high(p,lambda pid:raw,
                lambda uid:{"data":{"user_id":"INTRUDER","account_status":"active"}})

if __name__=="__main__":
    unittest.main()
