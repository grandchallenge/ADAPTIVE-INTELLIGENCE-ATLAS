#!/usr/bin/env python3
"""Adversarial public-tool, alternate-path and abstention contract checks."""
from __future__ import annotations
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_heterogeneous_trial import Policy


def public(index):
    tasks={
        0:"User: Alice Chan (USR001). Identify and cancel only the subscription "
          "tied to the product PureView Daily Lens (monthly plan).",
        2:"For user USR002 (Lucas Viteri), reactivate: change account_status "
          "from “suspended” to “active”.",
        3:"Create a new dietary restriction entity with restriction_id DR5:\n"
          "- name: Low-Carb\n- description: Limits high-carbohydrate grains and sugars.\n"
          "- tag: low-carb\n",
    }
    schemas={
      "list_user_subscriptions":["user_id"],
      "get_product_by_id":["product_id"],
      "check_subscription_links":["subscription_id"],
      "cancel_subscription":["subscription_id"],
      "invalidate_future_payments":["subscription_id"],
      "halt_scheduled_shipments":["subscription_id"],
      "modify_subscription_details":["subscription_id","updates"],
      "check_user_account_status":["user_id"],
      "update_user_account_status":["user_id","new_status"],
      "get_dietary_restriction_by_id":["restriction_id"],
      "create_dietary_restriction":["restriction_id","name","description","tag"],
    }
    return {"messages":[{"role":"user","content":tasks[index]}],
            "tools":[{"name":name,"parameters":{"type":"object",
                     "required":need}} for name,need in schemas.items()]}


def observe(p,action,record):
    p.observe({"kind":"observation","tool":action["tool"],
               "content":str(record),"ok":True})


class TestHeterogeneousInterventions(unittest.TestCase):
    def test_stop_never_executes(self):
        for i in (0,2,3):
            p=Policy(i,public(i),"stop")
            self.assertEqual(p.next_action(),{"action":"finish"})

    def test_public_explicit_identifier_direct_no_probe(self):
        p=Policy(2,public(2),"direct")
        a=p.next_action()
        self.assertEqual(a,{"action":"call","tool":"update_user_account_status",
                            "arguments":{"user_id":"USR002","new_status":"active"}})
        self.assertEqual(p.next_action(),{"action":"finish"})
        d=Policy(3,public(3),"direct")
        create=d.next_action()
        self.assertEqual(create["tool"],"create_dietary_restriction")
        self.assertEqual(create["arguments"],{
            "restriction_id":"DR5","name":"Low-Carb",
            "description":"Limits high-carbohydrate grains and sugars.",
            "tag":"low-carb"})
        self.assertEqual(d.next_action(),{"action":"finish"})

    def test_probe_active_status_uses_abstention(self):
        p=Policy(2,public(2),"probe")
        a=p.next_action()
        self.assertEqual(a["tool"],"check_user_account_status")
        observe(p,a,{"success":True,"data":{"account_status":"active"}})
        self.assertEqual(p.next_action(),{"action":"finish"})
        p=Policy(2,public(2),"probe")
        a=p.next_action()
        observe(p,a,{"success":True,"data":{"account_status":"suspended"}})
        self.assertEqual(p.next_action()["tool"],"update_user_account_status")

    def test_probe_existing_restriction_abstains(self):
        p=Policy(3,public(3),"probe")
        a=p.next_action()
        observe(p,a,{"success":True,"data":{"restriction_id":"DR5"}})
        self.assertEqual(p.next_action(),{"action":"finish"})
        p=Policy(3,public(3),"probe")
        a=p.next_action()
        observe(p,a,{"success":False,"error":"Dietary restriction not found"})
        self.assertEqual(p.next_action()["tool"],"create_dietary_restriction")
        p=Policy(3,public(3),"probe")
        a=p.next_action()
        observe(p,a,{"success":False,"error":"Internal API unavailable"})
        self.assertEqual(p.next_action(),{"action":"finish"})

    def test_subscription_cancel_never_without_observed_product_and_valid_links(self):
        p=Policy(0,public(0),"direct")
        self.assertEqual(p.next_action(),{"action":"finish"})
        p=Policy(0,public(0),"probe")
        a=p.next_action()
        self.assertEqual(a["tool"],"list_user_subscriptions")
        observe(p,a,{"success":True,"data":[
            {"subscription_id":"SUB-A","product_id":"PROD-A","user_id":"USR001",
             "subscription_status":"active","recurrence_pattern":"monthly"}]})
        a=p.next_action()
        self.assertEqual(a["tool"],"get_product_by_id")
        observe(p,a,{"success":True,"data":{
            "product_id":"PROD-A","name":"PureView Daily Lens"}})
        a=p.next_action()
        self.assertEqual(a["tool"],"check_subscription_links")
        observe(p,a,{"success":True,"data":{
            "user_linked":True,"product_linked":False}})
        self.assertEqual(p.next_action(),{"action":"finish"})
        p=Policy(0,public(0),"probe")
        a=p.next_action()
        observe(p,a,{"success":True,"data":[
            {"subscription_id":"SUB-A","product_id":"PROD-A","user_id":"USR001",
             "subscription_status":"active","recurrence_pattern":"monthly"}]})
        a=p.next_action()
        observe(p,a,{"success":True,"data":{"name":"PureView Daily Lens"}})
        a=p.next_action()
        observe(p,a,{"success":True,"data":{
            "user_linked":True,"product_linked":True}})
        self.assertEqual(p.next_action()["tool"],"cancel_subscription")

    def test_explicit_broken_subscription_link_overrides_generic_success(self):
        self.assertFalse(Policy._valid_links({
            "success": True, "valid": True,
            "data": {"user_linked": True, "product_linked": False}}))
        self.assertFalse(Policy._valid_links({
            "links_valid": True,
            "data": {"user_linked": False, "product_linked": True}}))
        self.assertTrue(Policy._valid_links({
            "success": True, "data": {"user_linked": True, "product_linked": True}}))

    def test_refuses_untrusted_strings(self):
        p=Policy(0,public(0),"probe")
        a=p.next_action()
        observe(p,a,{"success":True,"data":"__import__('os').system('true')"})
        self.assertEqual(p.next_action(),{"action":"finish"})
        with self.assertRaises(ValueError):
            Policy(2,{"messages":[{"role":"user","content":"For user USR002 "
                         "change account_status from “suspended” to “active”."}],
                     "tools":[],"verifier":"secret"},"probe")


if __name__=="__main__":
    unittest.main()
