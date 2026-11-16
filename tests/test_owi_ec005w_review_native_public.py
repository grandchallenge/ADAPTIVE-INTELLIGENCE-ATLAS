#!/usr/bin/env python3
"""Hostile original-source W public review status fixtures (NOT empirical data)."""
from __future__ import annotations
import copy,hashlib,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005w_review_native_public import check_spec,TARGETS,METHODS
from owi_ec005w_review_native_public_gate import adjudicate,CONTRACT
from owi_ec005_realtools_randomized import fingerprint
from owi_ec005u_source_eligibility import redact

SPEC=Path(__file__).resolve().parents[1]/"governance/research/OWI_EC005W_REVIEW_TARGET_STATUS_V1.json"
PROS=[
{"professional_id":"prof_marquez","name":"Dr. Luke Marquez","specialty":"Dermatology"},
{"professional_id":"prof_ella_internal","name":"Dr. Ella Navarro","specialty":"Internal Medicine"},
{"professional_id":"prof_ella_cardio","name":"Dr. Ella Navarro","specialty":"Cardiology"},
{"professional_id":"prof_sandy","name":"Dr. Sandy Torres","specialty":"Pediatrics"}]
USERS=[
{"_id":"u_alice","username":"Alice Chan","account_status":"active"},
{"_id":"u_jules","username":"Jules Morgan","account_status":"banned"},
{"_id":"u_ria","username":"Ria Singh","account_status":"inactive"},
{"_id":"u_silas","username":"Silas Huang","account_status":"active"}]
REVIEW=[
{"view_id":"rv_alice","user_id":"u_alice","professional_id":"prof_marquez","moderation_status":"pending"},
{"view_id":"rv_jules","user_id":"u_jules","professional_id":"prof_ella_internal","moderation_status":"pending"},
{"view_id":"rv_ria","user_id":"u_ria","professional_id":"prof_ella_cardio","moderation_status":"approved"},
{"view_id":"rv_silas","user_id":"u_silas","professional_id":"prof_sandy","moderation_status":"rejected"}]
def receipt(name,args,data,*,success=True):
    raw=repr({"success":success,"data":data})
    return {
        "tool":name,"arguments":args,
        "original_declared_required_public_arguments":sorted(METHODS[name]),
        "original_raw_public_reply_sha256":hashlib.sha256(raw.encode()).hexdigest(),
        "redacted_original_public_reply":raw,
        "redacted_original_public_reply_sha256":fingerprint(raw),
        "source_tool_status":"original_public_success" if success else "original_public_failed_or_unresolved",
        "native_original_source_reply_truncated":False,
        "physical_original_tool_seconds":0.002,
        "physical_original_restricted_worker_wall_seconds":0.12,
        "native_worker_rss_kib":11000,
        "source_private_terminal_state_discarded_without_inspection":True,
        "source_original_native_verifier_never_mounted":True,
    }
def fixture():
    actions=[
      receipt("list_all_professionals",{},PROS),
      receipt("list_all_users",{},USERS),
      receipt("get_professional_by_name",{"name":"Dr. Ella Navarro"},PROS[1:3])
    ]
    for pro in PROS:
        pid=pro["professional_id"]
        actions.append(receipt("get_reviews_for_professional",{"professional_id":pid},
            [rv for rv in REVIEW if rv["professional_id"]==pid]))
        actions.append(receipt("get_aggregated_rating_for_professional",{"professional_id":pid},
            {"professional_id":pid,"average_rating":4.0,"num_reviews":1}))
    for rv in REVIEW:
        actions.append(receipt("get_review_by_user_and_professional",{
            "user_id":rv["user_id"],"professional_id":rv["professional_id"]},rv))
        actions.append(receipt("get_review_moderation_status",{"view_id":rv["view_id"]},
            rv["moderation_status"]))
    target_receipts=[]
    for i,t in enumerate(TARGETS):
        name,specialty,author,before,action,agg=t
        target_receipts.append({
            "case_index":i,"professional":name,"specialty":specialty,
            "review_author":author,
            "public_professional_id":PROS[i]["professional_id"],
            "public_user_id":USERS[i]["_id"],
            "public_author_account_status":USERS[i]["account_status"],
            "task_before_review_status_expected":before,
            "task_action":action,
            "task_aggregate_rule":agg,
            "public_target_identity_status":
                "exact_original_source_public_professional_and_author_unique_identity_confirmed"})
    return {
      "contract":"OWI-EC005W-ORIGINAL-TRAIN-REVIEW-SELECTED-NATIVE-PUBLIC-READS/1",
      "original_frozen_public_protocol_file_sha256":check_spec(SPEC)[1],
      "entire_original_corpus_sha256_verified":"3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a",
      "original_train_row":710,
      "original_source_family_sha256":"a739046b13061603e09af000ceed469840dfecba0068db2e1919454b18394b0c",
      "original_public_user_task_sha256":"97bca760aa53e15f281b71771a6b63a1ba294c1ce3123f9632b114cbf12d6d36",
      "public_only_task_bundle_sha256":"a"*64,
      "original_environment_class_code_sha256":"b"*64,
      "original_declared_source_required_public_schemas":METHODS,
      "native_original_selected_read_receipts":actions,
      "native_public_tool_schema_unavailable":[],
      "selected_actual_original_public_target_identity_matches":target_receipts,
      "source_public_professional_list_count":len(PROS),
      "source_public_user_list_count":len(USERS),
      "source_public_ella_name_lookup_count":2,
      "actual_source_physical_selected_read_call_count":len(actions),
      "original_native_source_private_verifier_never_executed":True,
      "source_original_class_state_task_and_tools_unchanged":True,
      "source_private_terminal_not_exported_or_examined":True,
      "original_dev_sealed_test_task_contents_not_exposed":True,
      "source_public_credentials_redacted":True,
      "original_source_no_write_no_reward_no_policy_learning":True,
      "natural_original_review_pure_leave_unchanged_claim":
          "NOT_AUTHORIZED_BY_ORIGINAL_ROW710",
    }
class OriginalReviewSourceAdversarial(unittest.TestCase):
    def test_original_review_preregistration(self):
        sp,digest=check_spec(SPEC)
        self.assertEqual(len(digest),64)
        self.assertEqual(len(sp["source_original_named_targets"]),4)
        self.assertFalse(sp["original_task_authority"]["pure_leave_named_review_unchanged_action_authorized"])
    def test_hypothetical_full_fixture_can_support_distinct_aggregate_actions_not_review_noop(self):
        result=adjudicate(fixture(),spec_path=SPEC)
        self.assertEqual(result["contract"],CONTRACT)
        self.assertEqual(result["actual_source_exact_linked_review_preconditions_confirmed"],4)
        self.assertTrue(result["cross_action_original_source_aggregate_update_versus_no_update_directive_observed"])
        self.assertEqual(result["source_actual_task_cases_with_approved_set_aggregate_update_instruction"],[0,2])
        self.assertEqual(result["source_actual_task_cases_with_explicit_pending_aggregate_no_update"],[3])
        self.assertFalse(result["actual_source_natural_same_review_rule_action_and_pure_noop_pair_proved"])
        self.assertFalse(result["single_same_review_decision_naturally_variable_original_source_state_proved"])
        self.assertEqual(result["original_task_authorized_pure_review_noop_targets"],0)
    def test_public_source_credential_redacted(self):
        r={"success":True,"data":{"auth_token":"mock","_id":"u_alice",
                                   "authentication_info":"OAuth_Token:fake"}}
        val=redact(r)
        self.assertEqual(val["data"],{"_id":"u_alice"})
    def test_mismatching_source_before_status_never_promotes_aggregate_contrast(self):
        x=fixture()
        # Consistent returned review status but different from original target
        for r in x["native_original_selected_read_receipts"]:
            if r["tool"]=="get_review_by_user_and_professional" and r["arguments"]["user_id"]=="u_silas":
                original=ast_data(r)
                original["data"]["moderation_status"]="approved"
                change_data(r,original)
            if r["tool"]=="get_review_moderation_status" and r["arguments"]["view_id"]=="rv_silas":
                change_data(r,{"success":True,"data":"approved"})
        got=adjudicate(x,spec_path=SPEC)
        self.assertFalse(got["cross_action_original_source_aggregate_update_versus_no_update_directive_observed"])
        self.assertFalse(got["actual_source_natural_same_review_rule_action_and_pure_noop_pair_proved"])
    def test_hostile_source_counterfeits_rejected(self):
        mutations=[
         ("source",lambda x:x.__setitem__("entire_original_corpus_sha256_verified","f"*64)),
         ("verifier",lambda x:x.__setitem__("original_native_source_private_verifier_never_executed",False)),
         ("fabricated_pure_review_noop",lambda x:x.__setitem__("natural_original_review_pure_leave_unchanged_claim","SUPPORTED")),
         ("wrong_ella_specialty_id",lambda x:x["selected_actual_original_public_target_identity_matches"][1].__setitem__("public_professional_id","prof_ella_cardio")),
         ("original_source_task_change",lambda x:x.__setitem__("original_public_user_task_sha256","f"*64)),
         ("source_credential",lambda x:x["native_original_selected_read_receipts"][0].__setitem__("redacted_original_public_reply","{'success': True,'data': {'OAuth_Token':'x'}}")),
         ("forged_source_reply",lambda x:x["native_original_selected_read_receipts"][0].__setitem__("redacted_original_public_reply","{'success':True,'data':[]}")),
         ("source_other_method",lambda x:x["native_original_selected_read_receipts"][0].__setitem__("tool","delete_review")),
         ("mismatch_native_status",lambda x:x["native_original_selected_read_receipts"][0].__setitem__("source_tool_status","original_public_failed_or_unresolved")),
         ("missing_call",lambda x:x["native_original_selected_read_receipts"].pop()),
         ("extra_call",lambda x:x["native_original_selected_read_receipts"].append(copy.deepcopy(x["native_original_selected_read_receipts"][0]))),
         ("truncated_public",lambda x:x["native_original_selected_read_receipts"][0].__setitem__("native_original_source_reply_truncated",True)),
         ("private_final_leak",lambda x:x["native_original_selected_read_receipts"][0].__setitem__("source_private_terminal_state_discarded_without_inspection",False)),
         ("tool_telemetry",lambda x:x["native_original_selected_read_receipts"][0].__setitem__("physical_original_tool_seconds",-1)),
        ]
        for tag,change in mutations:
            with self.subTest(tag=tag):
                x=fixture();change(x)
                with self.assertRaises(ValueError):adjudicate(x,spec_path=SPEC)
    def test_unsafe_protocol_mutations_rejected(self):
        original=json.loads(SPEC.read_text())
        changes=[
          ("lookups",lambda x:x["prospective_selected_original_public_reads"].__setitem__(
            "max_original_native_selected_public_read_calls",300)),
          ("source",lambda x:x["source"].__setitem__("full_raw_sha256","0"*64)),
          ("review_noop",lambda x:x["original_task_authority"].__setitem__(
            "pure_leave_named_review_unchanged_action_authorized",True)),
          ("specialty_relaxed",lambda x:x["original_task_authority"].__setitem__(
            "matching_by_only_shared_professional_name_without_specialty_is_forbidden",False)),
          ("original_name_changed",lambda x:x["source_original_named_targets"][1].__setitem__(
            "professional","Dr. Everybody")),
          ("native_verifier",lambda x:x["source"].__setitem__("original_verifier_never_executed",False))
        ]
        for tag,change in changes:
            with self.subTest(tag=tag),tempfile.TemporaryDirectory() as tmp:
                x=copy.deepcopy(original);change(x)
                p=Path(tmp)/"malicious.json";p.write_text(json.dumps(x))
                with self.assertRaises(ValueError):check_spec(p)
def ast_data(r):
    import ast
    return ast.literal_eval(r["redacted_original_public_reply"])
def change_data(r,payload):
    raw=repr(payload)
    r["redacted_original_public_reply"]=raw
    r["redacted_original_public_reply_sha256"]=fingerprint(raw)
if __name__=="__main__":unittest.main()
