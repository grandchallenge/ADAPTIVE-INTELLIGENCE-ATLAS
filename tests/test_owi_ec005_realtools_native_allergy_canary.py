#!/usr/bin/env python3
"""Real clinical-source action scope; deletion cannot be mislabelled harmless."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_allergy_canary import (
    intervention,read_present,public_deleted,ARMS
)

class NativeAllergyActionUnit(unittest.TestCase):
    def test_four_public_predeclared_actions(self):
        self.assertEqual(set(ARMS),{
            "stop","correct","delete_wrong","correct_then_delete"})
        self.assertEqual(intervention("stop"),{"update_first":False,"delete":False})
        self.assertEqual(intervention("correct"),{"update_first":True,"delete":False})
        self.assertEqual(intervention("delete_wrong"),{"update_first":False,"delete":True})
        self.assertEqual(intervention("correct_then_delete"),{
            "update_first":True,"delete":True})
        for forbidden in ("oracle","modify_private","delete_other_patient",None):
            with self.assertRaises(ValueError):
                intervention(forbidden)

    def test_only_genuine_public_correct_patient_allergy_authorizes(self):
        record={"success":True,"data":{
            "patient_id":"PAT001","substance":"Penicillin",
            "reaction_type":"Rash","confirmation_status":"Confirmed",
            "date_recorded":"2015-06-21"}}
        self.assertEqual(read_present(record)["date_recorded"],"2015-06-21")
        for bad in (
            {"success":True,"data":{**record["data"],"patient_id":"PAT002"}},
            {"success":True,"data":{**record["data"],"substance":"Amoxicillin"}},
            {"success":True,"data":{**record["data"],"confirmation_status":"Unconfirmed"}},
            {"success":False,"data":None},
            {"success":True,"data":{}},
        ):
            with self.subTest(record=bad):
                with self.assertRaises(ValueError):
                    read_present(bad)

    def test_absence_not_forged_when_record_still_exists(self):
        self.assertTrue(public_deleted({"success":False,"data":None}))
        self.assertFalse(public_deleted({"success":True,"data":{
            "patient_id":"PAT001","substance":"Penicillin"}}))
        self.assertFalse(public_deleted({"success":False,"data":{
            "patient_id":"PAT001","substance":"Penicillin"}}))
        self.assertFalse(public_deleted({"success":True,"data":None}))
        with self.assertRaises(ValueError):
            public_deleted(None)

if __name__=="__main__":
    unittest.main()
