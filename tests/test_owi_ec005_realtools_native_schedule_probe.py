#!/usr/bin/env python3
"""EC005K original public schedule parsing / privacy invariants."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_schedule_probe import (
    only_public_schedule,SCHEDULES
)
PUBLIC={
    "messages":[{"role":"user","content":
        "MEAL102: set schedule 2024-07-14T12:00 to unavailable and 2024-07-14T18:00 to available"}],
    "tools":[
        {"name":"get_meal_schedule_by_datetime","parameters":{
            "required":["scheduled_datetime"]}},
        {"name":"update_meal_schedule_availability","parameters":{
            "required":["meal_id","scheduled_datetime","availability_sta"]}},
    ],
}
class ScheduleProbeTests(unittest.TestCase):
    def test_public_target_selection(self):
        reply={"success":True,"data":[
            {"meal_id":"MEAL101","scheduled_datetime":"2024-07-14T18:00",
             "availability_status":"unavailable"},
            {"meal_id":"MEAL102","scheduled_datetime":"2024-07-14T18:00",
             "availability_status":"available"},
        ]}
        result=only_public_schedule(PUBLIC,reply,"2024-07-14T18:00")
        self.assertEqual(result["target_record_count"],1)
        self.assertEqual(result["target_public_status"],"available")
        self.assertEqual(result["public_schedule_count"],2)

    def test_wrong_datetime_ambiguous_or_private_leak_fails(self):
        with self.assertRaises(ValueError):
            only_public_schedule({**PUBLIC,"verifier":"HIDDEN"},{
                "success":True,"data":[]},SCHEDULES[0][1])
        with self.assertRaises(ValueError):
            only_public_schedule(PUBLIC,{"success":False,"data":[]},SCHEDULES[0][1])
        repeated={"meal_id":"MEAL102","scheduled_datetime":SCHEDULES[0][1]}
        with self.assertRaises(ValueError):
            only_public_schedule(PUBLIC,{"success":True,"data":[repeated,repeated]},
                                  SCHEDULES[0][1])

    def test_unknown_schedule_is_explicit_not_assumed(self):
        x=only_public_schedule(PUBLIC,{"success":True,"data":[]},SCHEDULES[0][1])
        self.assertEqual(x["target_record_count"],0)
        self.assertIsNone(x["target_public_status"])

if __name__=="__main__":
    unittest.main()
