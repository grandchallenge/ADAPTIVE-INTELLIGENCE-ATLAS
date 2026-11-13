#!/usr/bin/env python3
"""Native source row 2449 public allergy inputs only; no hidden-state oracle."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_allergy_probe import (
    USER,PATIENT,SUBSTANCE,public_contract,summarize_observed
)

def public():
    params={
        "verify_user_authorization":["user_id","patient_id","action"],
        "get_authorized_user_info":["user_id"],
        "get_patient_allergy_by_substance":["user_id","patient_id","substance"],
        "get_allergy_details":["user_id","patient_id","substance"],
        "update_patient_allergy":["user_id","patient_id","substance","reaction_type",
                                  "confirmation_status","date_recorded"],
        "delete_patient_allergy":["user_id","patient_id","substance"],
    }
    return {
        "messages":[{"role":"user","content":
            "As USR100, for PAT001 update existing Penicillin allergy reaction "
            "from Rash to Urticaria."}],
        "tools":[{"name":name,"parameters":{"required":cols}}
                 for name,cols in params.items()],
    }

class AllergySourceBoundary(unittest.TestCase):
    def test_declared_public_contract(self):
        self.assertEqual(len(public_contract(public())),6)
        with self.assertRaises(ValueError):
            public_contract({**public(),"verifier":"SECRET"})
        p=public()
        p["tools"][2]["parameters"]["required"]=["user_id"]
        with self.assertRaises(ValueError):
            public_contract(p)
    def test_private_patient_demographics_not_exported(self):
        r={"success":True,"data":{
            "patient_id":PATIENT,"substance":SUBSTANCE,
            "reaction_type":"Rash","confirmation_status":"Confirmed",
            "date_recorded":"2024-07-02","secret_patient_name":"SECRET",
            "date_of_birth":"SECRET"}}
        out=summarize_observed(r)
        self.assertEqual(out["public_allergy_record"]["reaction_type"],"Rash")
        self.assertNotIn("secret_patient_name",out["public_allergy_record"])
        self.assertNotIn("date_of_birth",out["public_allergy_record"])
        self.assertNotIn("SECRET",str(out))
    def test_failure_and_strange_data_not_forged(self):
        x=summarize_observed({"success":False,"data":None,"error":"denied"})
        self.assertIsNone(x["public_allergy_record"])
        with self.assertRaises(ValueError):
            summarize_observed(None)
        self.assertIsNone(summarize_observed({
            "success":True,"data":[{"patient_id":"PAT999","substance":SUBSTANCE}]
        })["public_allergy_record"])

if __name__=="__main__":
    unittest.main()
