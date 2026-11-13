#!/usr/bin/env python3
"""Unit and nonleakage tests for public-observation conditioned goal policy."""
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_goal_policy import GoalPolicy, parse_task, unpack_reply

PROMPT=("Create and process a new outbreak report for Tarvio Gastroenteritis in "
        "Old Market, submitted by the citizen reporter Miguel Torres, with an "
        "initial case count of 6. Update the case count to 12.")
TOOLS=["get_location_by_name","list_reporters_by_type","list_reports_by_disease",
       "create_outbreak_report","validate_reporter_credentials",
       "update_case_count","verify_outbreak_report","escalate_outbreak_report"]

def public():
    return {"messages":[{"role":"user","content":PROMPT}],
            "tools":[{"name":name,"parameters":{}} for name in TOOLS],
            "candidate_read_tool":"get_location_by_name"}

def observe(policy, action, data):
    policy.observe({"kind":"observation","tool":action["tool"],
                    "content":str(data),"ok":True})

class PolicyTests(unittest.TestCase):
    def test_task_parses_only_public_intent(self):
        g=parse_task(public())
        self.assertEqual(g["disease"],"Tarvio Gastroenteritis")
        self.assertEqual(g["location"],"Old Market")
        self.assertEqual(g["reporter"],"Miguel Torres")
        self.assertEqual(g["target_count"],12)

    def test_readonly_control_never_mutates(self):
        p=GoalPolicy(public(),1)
        for tool in ("get_location_by_name","list_reporters_by_type",
                     "list_reports_by_disease"):
            a=p.next_action();self.assertEqual(a["tool"],tool)
            observe(p,a,{"success":True,"data":[]})
        self.assertEqual(p.next_action(),{"action":"finish"})

    def test_goal_uses_only_observed_ids_and_actual_new_report_id(self):
        p=GoalPolicy(public(),2)
        a=p.next_action()
        observe(p,a,{"success":True,"data":[{"name":"Old Market","location_id":"L_FROM_TOOL"}]})
        a=p.next_action()
        observe(p,a,{"success":True,"data":[{"name":"Miguel Torres","reporter_id":"R_FROM_TOOL"}]})
        a=p.next_action()
        observe(p,a,{"success":True,"data":[{
            "report_id":"PREVIOUS","location_id":"L_FROM_TOOL",
            "disease_name":"Tarvio Gastroenteritis","date_reported":"2024-04-17"}]})
        a=p.next_action()
        self.assertEqual(a["tool"],"create_outbreak_report")
        self.assertEqual(a["arguments"]["location_id"],"L_FROM_TOOL")
        self.assertEqual(a["arguments"]["reporter_id"],"R_FROM_TOOL")
        self.assertEqual(a["arguments"]["date_reported"],"2024-04-18")
        observe(p,a,{"success":True,"data":{"report_id":"NEW_FROM_TOOL"}})
        a=p.next_action()
        self.assertEqual(a["tool"],"validate_reporter_credentials")
        observe(p,a,{"success":True,"data":{"reporter_id":"R_FROM_TOOL"}})
        a=p.next_action()
        self.assertEqual(a["tool"],"update_case_count")
        self.assertEqual(a["arguments"]["report_id"],"NEW_FROM_TOOL")
        self.assertEqual(a["arguments"]["case_count"],12)
        observe(p,a,{"success":True,"data":{}})
        a=p.next_action();self.assertEqual(a["tool"],"verify_outbreak_report")
        observe(p,a,{"success":False,"error":"not ready"})
        self.assertEqual(p.next_action(),{"action":"finish"})

    def test_no_reporter_identifier_prevents_mutation(self):
        p=GoalPolicy(public(),2)
        a=p.next_action()
        observe(p,a,{"success":True,"data":[{"name":"Old Market","location_id":"L1"}]})
        a=p.next_action()
        observe(p,a,{"success":True,"data":[{"name":"Another Person","reporter_id":"R1"}]})
        a=p.next_action()
        observe(p,a,{"success":True,"data":[]})
        self.assertEqual(p.next_action(),{"action":"finish"})

    def test_does_not_execute_untrusted_tool_output(self):
        self.assertFalse(unpack_reply("__import__('os').system('true')")["success"])

if __name__=="__main__":
    unittest.main()
