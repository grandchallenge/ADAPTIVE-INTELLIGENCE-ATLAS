#!/usr/bin/env python3
"""No-private-data public-scope regression tests for original row 710."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_professional_probe import (
    preflight,objects,public_projection,REQUIRED)
def public():
    return {"messages":[{"role":"user","content":
          "Dr. Luke Marquez Alice Chan Dr. Ella Navarro Jules Morgan "
          "banned Dr. Sandy Torres"}],
          "tools":[{"name":k,"parameters":{"required":list(v)}}
                   for k,v in REQUIRED.items()]}

class PublicProfessionalBoundaries(unittest.TestCase):
    def test_source_only_preflight(self):
        self.assertEqual(set(preflight(public())),set(REQUIRED))
        for forged in ({**public(),"verifier":{"secret":"wrong"}},
                       {**public(),"tools":[]},
                       {"messages":[],"tools":public()["tools"]}):
            with self.assertRaises(ValueError):
                preflight(forged)
    def test_nested_read_response_and_no_secret_projection(self):
        r={"success":True,"data":{"reviews":[{"view_id":"RW1",
           "moderation_status":"pending","private_solution":"SECRET",
           "rating":1,"secret":{"patient":"NONE"}}]}}
        xs=objects(r)
        self.assertEqual(xs[0]["view_id"],"RW1")
        p=public_projection(xs[0],("view_id","rating","private_solution"))
        self.assertNotIn("secret",p)
        self.assertEqual(objects({"data":None}),[])
    def test_reject_unrecognized_read_schema(self):
        self.assertEqual(objects(None),[])
        self.assertEqual(objects({"data":[{"rating":3}]}),[{"rating":3}])
if __name__=="__main__":
    unittest.main()
