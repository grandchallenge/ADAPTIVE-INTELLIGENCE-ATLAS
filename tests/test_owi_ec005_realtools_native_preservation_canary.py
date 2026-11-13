#!/usr/bin/env python3
"""OWI-EC005K action-source contract, no oracle and conditional-stage invariants."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_preservation_canary import (
    ARMS,stage2_action,read_target,LUNCH
)

PUBLIC={
    "messages":[{"role":"user","content":
        "At MEAL102 2024-07-14T12:00 set unavailable; "
        "2024-07-14T18:00 set available"}],
    "tools":[
        {"name":"get_meal_schedule_by_datetime","parameters":{
            "required":["scheduled_datetime"]}},
        {"name":"update_meal_schedule_availability","parameters":{
            "required":["meal_id","scheduled_datetime","availability_sta"]}},
    ],
}

class Stage2SafetyUnit(unittest.TestCase):
    def test_exact_source_public_action_mapping(self):
        self.assertEqual(stage2_action("stop"),None)
        self.assertEqual(stage2_action("reapply_correct"),"unavailable")
        self.assertEqual(stage2_action("regress_noncompliant"),"available")
        self.assertEqual(set(ARMS),{"stop","reapply_correct","regress_noncompliant"})
        self.assertEqual(stage2_action("stop","dinner"),None)
        self.assertEqual(stage2_action("reapply_correct","dinner"),"available")
        self.assertEqual(stage2_action("regress_noncompliant","dinner"),"unavailable")
        with self.assertRaises(ValueError):
            stage2_action("regress_noncompliant","other_slot")
        for forbidden in ("invented","oracle","private_state","fix_any",None):
            with self.assertRaises(ValueError):
                stage2_action(forbidden)

    def test_actual_public_status_selection_requires_unique_target(self):
        msg={"success":True,"data":[
            {"meal_id":"MEAL101","scheduled_datetime":LUNCH,
             "availability_sta":"available"},
            {"meal_id":"MEAL102","scheduled_datetime":LUNCH,
             "availability_sta":"unavailable"}]}
        self.assertEqual(read_target(PUBLIC,msg),"unavailable")
        with self.assertRaises(ValueError):
            read_target(PUBLIC,{"success":True,"data":[]})
        with self.assertRaises(ValueError):
            read_target({**PUBLIC,"verifier":"forbidden"},msg)

    def test_unknown_public_status_is_not_treated_as_safe(self):
        invalid={"success":True,"data":[{
            "meal_id":"MEAL102","scheduled_datetime":LUNCH,
            "availability_sta":"mystery"}]}
        with self.assertRaises(ValueError):
            read_target(PUBLIC,invalid)

if __name__=="__main__":
    unittest.main()
