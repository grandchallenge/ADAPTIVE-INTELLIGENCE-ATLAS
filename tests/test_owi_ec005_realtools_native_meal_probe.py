#!/usr/bin/env python3
"""OWI-EC005J public allergen task source/target identity assertions."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_meal_probe import public_meal_snapshot

def task():
    return {"messages":[{"role":"user","content":
       "MEAL102 cashews (cross-contact) risk; update its allergen_info"}],
       "tools":[
           {"name":"get_meal_by_id","parameters":{"required":["meal_id"]}},
           {"name":"update_meal_allergen_info","parameters":{
               "required":["meal_id","new_allergen_info"],
               "properties":{"new_allergen_info":{"type":"string"}}}},
       ]}
class MealPublicTests(unittest.TestCase):
    def test_genuine_public_info_and_declared_schema(self):
        p=public_meal_snapshot(task(),{"success":True,"data":{
            "meal_id":"MEAL102","allergen_info":"none",
            "dietary_properties":["nut-free","vegetarian"]}})
        self.assertEqual(p["public_allergen_info_type"],"str")
        self.assertEqual(p["public_allergen_info"],"none")
        self.assertEqual(p["public_meal_id"],"MEAL102")
    def test_mismatched_id_failed_reply_and_private_payload_rejected(self):
        with self.assertRaises(ValueError):
            public_meal_snapshot(task(),{"success":True,"data":{
                "meal_id":"OTHER","allergen_info":"none"}})
        with self.assertRaises(ValueError):
            public_meal_snapshot(task(),{"success":False,"data":None})
        with self.assertRaises(ValueError):
            public_meal_snapshot({**task(),"verifier":{"private":True}},
                      {"success":True,"data":{"meal_id":"MEAL102"}})
        t=task()
        t["messages"]=[{"role":"user","content":"no safety checks"}]
        with self.assertRaises(ValueError):
            public_meal_snapshot(t,{"success":True,"data":{"meal_id":"MEAL102"}})
if __name__=="__main__":
    unittest.main()
