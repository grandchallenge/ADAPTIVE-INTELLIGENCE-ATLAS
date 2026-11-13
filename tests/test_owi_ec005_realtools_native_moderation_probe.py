#!/usr/bin/env python3
"""Native public moderation discovery tests without executing source code."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_moderation_probe import records

class PublicReviewRecordsTests(unittest.TestCase):
    def test_list_and_mapping_public_data_only(self):
        p={"success":True,"data":[{"review_id":"R1"},None,{"review_id":"R2"}]}
        self.assertEqual([x["review_id"] for x in records(p)],["R1","R2"])
        self.assertEqual(records({"success":True,"data":{
            "R1":{"review_id":"R1"},"bad":"X"}}),[{"review_id":"R1"}])
    def test_invalid_reply_does_not_forge_records(self):
        for v in ({},{"success":False,"data":None},{"success":True,"data":"secret"},
                  {"data":[1,2,None]},None):
            self.assertEqual(records(v),[])
if __name__=="__main__":
    unittest.main()
