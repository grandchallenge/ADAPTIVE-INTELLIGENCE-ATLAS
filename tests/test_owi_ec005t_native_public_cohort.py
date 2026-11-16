#!/usr/bin/env python3
"""Original-source T protocol and independent gate hostile fixtures.

These tiny synthetic public-reply fixtures prove rejection contracts; they
are NOT physical evidence or results from the original third-party source.
"""
from __future__ import annotations
import copy,hashlib,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005t_native_public_cohort import verified_protocol,public_projection
from owi_ec005t_native_public_cohort_gate import (
    adjudicate,LOCK,SHA,TARGETS,ROWS,RUN,SAFE,
    CONTRACT,trial_gate,PublicReplay)
from owi_ec005_realtools_randomized import fingerprint

ROOT=Path(__file__).resolve().parents[1]
SPEC=ROOT/"governance/research/OWI_EC005T_NATIVE_SECOND_COHORT_V1.json"
def receipt(row,tool,args,reply):
    safe=repr(reply)
    return {
        "original_row":row,"selected_public_read_tool":tool,
        "actual_original_source_public_arguments":args,
        "raw_actual_original_public_reply":safe,
        "sha256_actual_original_public_reply":fingerprint(safe),
        "sha256_full_original_reply_audit_only":hashlib.sha256(safe.encode()).hexdigest(),
        "source_public_sensitive_field_redacted":False,
        "status":"source_success" if reply.get("success") else "source_failure",
        "physical_original_source_tool_seconds":0.001,
        "physical_source_worker_wall_seconds":0.15,
        "physical_worker_peak_rss_kib":15000,
        "source_private_final_state_discarded":True,
        "source_private_native_verifier_not_executed":True,
    }
def fake():
    recs=[
        receipt(1549,"get_user_by_name",{"name":"Alice Chan"},
                {"success":False,"data":None}),
        receipt(1900,"get_subscriber_by_email",
                {"email_address":"alice.chan@example.com"},
                {"success":False,"data":None}),
        receipt(5,"get_user_account_by_username",
                {"username":"farida.youssef"},{"success":False,"data":None}),
        receipt(2000,"list_folders",{},{"success":True,"data":[]}),
    ]
    return {
        "contract":RUN,"original_source_full_sha256":SHA,
        "frozen_original_source_current_state_protocol_sha256":verified_protocol(SPEC),
        "original_source_train_rows":list(ROWS),
        "original_public_and_class_hashes":{
            str(k):{"original_executable_class_sha256":LOCK[k][0],
                    "public_task_sha256":LOCK[k][1]} for k in ROWS},
        "selected_source_public_read_schema_required":{
            "1549":{"get_user_by_name":["name"]},
            "1900":{"get_subscriber_by_email":["email_address"]},
            "5":{"get_user_account_by_username":["username"]},
            "2000":{"list_folders":[]}},
        "original_private_source_and_native_verifier_not_exported":True,
        "original_source_initial_state_and_user_task_unmodified":True,
        "original_source_public_only_read_calls_physically_executed":len(recs),
        "source_public_selected_read_receipts":recs,
        "public_schema_or_source_evidence_omissions":[],
        "no_original_source_private_checker_executed":True,
        "no_actual_terminal_reward_or_policy_training":True,
        "sealed_dev_and_test_families_unopened":True,
    }

class NativeSecondCohortFalseProofTests(unittest.TestCase):
    def test_frozen_exact_source_and_original_training_cohort(self):
        self.assertEqual(len(verified_protocol(SPEC)),64)
        source=json.loads(SPEC.read_text())
        for key,change in [
            ("wrong_original_task",lambda x:x["source"].__setitem__(
                "exact_distinct_original_family_rows",[5,2000,1549,1900])),
            ("source_digest",lambda x:x["source"].__setitem__("full_sha256","0"*64)),
            ("source_private_checker",lambda x:x["source"].__setitem__(
                "original_private_verifier_never_mounted_or_executed",False)),
            ("weakened_noop",lambda x:x["qualification"].__setitem__(
                "existing_other_record_is_not_noop_for_requested_action",False)),
            ("new_budget",lambda x:x["sampling"].__setitem__(
                "max_total_selected_public_tool_calls",350)),
            ("invented_target",lambda x:x["candidates"][0].__setitem__(
                "public_target_quantities",{"Lumina Wireless Earbuds":0})),
        ]:
            new=copy.deepcopy(source);change(new)
            with self.subTest(key=key),tempfile.TemporaryDirectory() as d:
                path=Path(d)/"mutant.json"
                path.write_text(json.dumps(new))
                with self.assertRaises(ValueError):verified_protocol(path)
    def test_public_projection_scrubs_even_original_source_exposed_credentials(self):
        source={"success":True,"data":{
            "participant_id":"P1","hashed_password":"fakehash",
            "api_key":"synthetic", "username":"farida.youssef",
            "nested":[{"refresh_token":"abc","consent_status":"valid"}]}}
        safe=public_projection(source)
        self.assertEqual(safe["data"]["participant_id"],"P1")
        self.assertNotIn("hashed_password",safe["data"])
        self.assertNotIn("api_key",safe["data"])
        self.assertEqual(safe["data"]["nested"],[{"consent_status":"valid"}])
    def test_negative_fixture_not_misreported_as_original_positive_evidence(self):
        result=adjudicate(fake(),task_spec=SPEC)
        self.assertEqual(result["contract"],CONTRACT)
        self.assertEqual(result["original_source_read_only_actual_calls"],4)
        self.assertEqual(result["qualifying_original_mixed_condition_family_count"],0)
        self.assertTrue(result["no_causal_policy_learning_or_original_native_terminal_reward"])
    def test_source_private_or_replay_forgery_rejected(self):
        mutants=[
          ("wrong_source_bytes",lambda x:x.__setitem__(
              "original_source_full_sha256","0"*64)),
          ("foreign_original_class",lambda x:x[
              "original_public_and_class_hashes"]["5"].__setitem__(
                  "original_executable_class_sha256","b"*64)),
          ("dev_test_leak",lambda x:x.__setitem__(
              "sealed_dev_and_test_families_unopened",False)),
          ("source_native_checker_leak",lambda x:x.__setitem__(
              "no_original_source_private_checker_executed",False)),
          ("chosen_source_read_write",lambda x:x["source_public_selected_read_receipts"][0].__setitem__(
              "selected_public_read_tool","delete_cart")),
          ("forged_source_reply",lambda x:x["source_public_selected_read_receipts"][0].__setitem__(
              "raw_actual_original_public_reply","{'success':True,'data':[]}")),
          ("source_failed_as_success",lambda x:x["source_public_selected_read_receipts"][0].__setitem__(
              "status","source_success")),
          ("wrong_source_real_args",lambda x:x["source_public_selected_read_receipts"][0].__setitem__(
              "actual_original_source_public_arguments",{"name":"Other"})),
          ("wrong_public_first_tool",lambda x:x["source_public_selected_read_receipts"][0].__setitem__(
              "selected_public_read_tool","get_cart_by_user_id")),
          ("unmetered_original_call",lambda x:x["source_public_selected_read_receipts"].append(
              copy.deepcopy(x["source_public_selected_read_receipts"][0]))),
          ("forged_source_wall",lambda x:x["source_public_selected_read_receipts"][0].__setitem__(
              "physical_source_worker_wall_seconds",-5)),
          ("exposed_password",lambda x:x["source_public_selected_read_receipts"][0].__setitem__(
              "raw_actual_original_public_reply","{'hashed_password':'private'}")),
          ("not_original_schema",lambda x:x[
              "selected_source_public_read_schema_required"]["1549"].__setitem__(
              "get_user_by_name",["user_id"])),
        ]
        for name,edit in mutants:
            with self.subTest(name=name):
                data=fake();edit(data)
                with self.assertRaises(ValueError):adjudicate(data,task_spec=SPEC)
    def test_synthetic_trial_has_mixed_suspended_and_active_public_lookups(self):
        base=fake()
        recs=base["source_public_selected_read_receipts"]
        r5=[
          receipt(5,"get_user_account_by_username",{"username":"farida.youssef"},
                  {"success":True,"data":{
                      "username":"farida.youssef","participant_id":"PID1"}}),
          receipt(5,"list_current_enrollments_for_participant",
                  {"participant_id":"PID1"},
                  {"success":True,"data":[
                      {"participant_id":"PID1","enrollment_status":"enrolled","trial_id":"T1"},
                      {"participant_id":"PID1","enrollment_status":"enrolled","trial_id":"T2"}]}),
          receipt(5,"list_enrollments_for_participant",
                  {"participant_id":"PID1"},{"success":True,"data":[]}),
          receipt(5,"get_clinical_trial_by_id",{"trial_id":"T1"},
                  {"success":True,"data":{"trial_id":"T1","name":"Suspended",
                                        "status":"suspended"}}),
          receipt(5,"get_clinical_trial_by_id",{"trial_id":"T2"},
                  {"success":True,"data":{"trial_id":"T2","name":"Active",
                                        "status":"active"}}),
        ]
        base["source_public_selected_read_receipts"]=recs[:2]+r5+recs[3:]
        base["original_source_public_only_read_calls_physically_executed"]=len(
            base["source_public_selected_read_receipts"])
        base["selected_source_public_read_schema_required"]["5"].update({
            "list_current_enrollments_for_participant":["participant_id"],
            "list_enrollments_for_participant":["participant_id"],
            "get_clinical_trial_by_id":["trial_id"]})
        # Mark synthetic fixture has two real public branch conditions;
        # a test proves classification mechanism only, NOT empirical support.
        got=adjudicate(base,task_spec=SPEC)
        status=got["independently_reconstructed_source_public_candidate_states"]["5"]
        self.assertTrue(status["genuine_mixed_support"])
        self.assertEqual(status["original_source_withdraw_policy_status_counts"],
            {"withdraw_required":1,"leave_active_non_suspended_trial_enrollment_unchanged":1})

if __name__=="__main__":
    unittest.main()
