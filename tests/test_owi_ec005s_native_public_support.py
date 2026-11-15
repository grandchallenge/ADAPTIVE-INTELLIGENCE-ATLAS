#!/usr/bin/env python3
"""Hostile synthetic SOURCE-PUBLIC fixtures (not empirical native-source evidence)."""
import copy,hashlib,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005s_native_public_support import (
    CONTRACT,RAW_SOURCE,categorize_review,check_spec,public_bundle)
from owi_ec005s_native_public_support_gate import adjudicate
from owi_ec005_realtools_randomized import fingerprint
SPEC=Path(__file__).resolve().parents[1]/"governance/research/OWI_EC005S_NATIVE_PUBLIC_SUPPORT_V1.json"

def receipt(row,tool,args,reply):
    content=repr(reply)
    return {"original_source_row":row,"selected_read_only_tool":tool,
            "selected_original_public_args":args,
            "raw_actual_original_public_reply":content,
            "actual_public_reply_sha256":fingerprint(content),
            "source_public_tool_seconds":.001,
            "source_worker_container_wall_seconds":.18,
            "source_worker_peak_rss_kib":12000,
            "original_private_terminal_state_discarded":True,
            "original_native_verifier_never_executed":True}

def original_fixture():
    # SOURCE-PUBLIC synthetic text, independent of actual pinned task snapshots.
    r=[
       receipt(2151,"list_all_products",{},{"success":True,"data":[
           {"product_id":"P1","category":"Supplements"},
           {"product_id":"P2","category":"Home"}]}),
       receipt(2151,"get_reviews_for_product_by_status",{
           "product_id":"P1","moderation_status":"pending"},{
           "success":True,"data":[
               {"review_id":"R1","product_id":"P1","user_id":"U1",
                "rating":5,"review_text":"good","moderation_status":"pending"},
               {"review_id":"R2","product_id":"P1","user_id":"U2",
                "rating":1,"review_text":"bad","moderation_status":"pending"},
               {"review_id":"R3","product_id":"P1","user_id":"U3",
                "rating":3,"review_text":"okay","moderation_status":"pending"}]}),
       receipt(2151,"get_user_by_id",{"user_id":"U1"},
               {"success":True,"data":{"user_id":"U1","account_status":"active"}}),
       receipt(2151,"get_user_by_id",{"user_id":"U2"},
               {"success":True,"data":{"user_id":"U2","account_status":"suspended"}}),
       receipt(2151,"get_user_by_id",{"user_id":"U3"},
               {"success":True,"data":{"user_id":"U3","account_status":"active"}}),
       receipt(2151,"get_reviews_for_product_by_status",{
           "product_id":"P2","moderation_status":"pending"},{
           "success":True,"data":[{
               "review_id":"R4","product_id":"P2","user_id":"U1",
               "rating":5,"review_text":"Buy refills weekly","moderation_status":"pending"}]}),
       receipt(2001,"list_tags",{},{"success":True,"data":[
           {"tag_id":"T1","name":"tcm"},{"tag_id":"T2","name":"herbal"}]}),
    ]
    reviews=[
        dict(source_product_id="P1",original_source_review_id="R1",
             author_source_user_id="U1",public_rating=5,
             public_account_status="active",public_product_category="Supplements",
             public_review_text_contains_refill=False,
             original_public_task_action_class="approve"),
        dict(source_product_id="P1",original_source_review_id="R2",
             author_source_user_id="U2",public_rating=1,
             public_account_status="suspended",public_product_category="Supplements",
             public_review_text_contains_refill=False,
             original_public_task_action_class="reject"),
        dict(source_product_id="P1",original_source_review_id="R3",
             author_source_user_id="U3",public_rating=3,
             public_account_status="active",public_product_category="Supplements",
             public_review_text_contains_refill=False,
             original_public_task_action_class="leave_unchanged"),
        dict(source_product_id="P2",original_source_review_id="R4",
             author_source_user_id="U1",public_rating=5,
             public_account_status="active",public_product_category="Home",
             public_review_text_contains_refill=True,
             original_public_task_action_class="edit_rating_and_leave_pending"),
    ]
    tags=[{"tag_target_from_original_public_prompt":s,
           "public_existing_tag_record_found":s in ("tcm","herbal"),
           "original_public_task_action_class":(
               "tag_already_exists_no_create" if s in ("tcm","herbal") else
               "tag_missing_create_candidate")} for s in (
                   "tcm","herbal","acupuncture","evidence-based","safety")]
    return {
        "contract":CONTRACT,"original_whole_source_sha256":RAW_SOURCE,
        "frozen_native_public_support_spec_sha256":check_spec(SPEC),
        "original_selected_train_rows":[2151,2001],
        "original_source_classes_and_public_task_identity":{
            "2151":{"original_source_executable_class_sha256":
                    "75e5e199e65aaf2dbf374805c6eb735569b727a2796fb1fd6f8e20098650af7c",
                    "original_source_public_task_sha256":
                    "5d8bae31755d162f274a0170043e8bed595e7e0217f4fa43f84f6dbcc19e2629"},
            "2001":{"original_source_executable_class_sha256":"b"*64,
                    "original_source_public_task_sha256":"c"*64}},
        "original_dev_and_sealed_test_source_tasks_not_exposed":True,
        "third_party_source_exec_only_in_restricted_worker":True,
        "native_original_source_state_unchanged":True,
        "source_original_private_verifier_not_executed":True,
        "no_learned_policy_or_reward_claim":True,
        "actual_physical_read_only_source_tool_call_count":len(r),
        "actual_source_public_tool_receipts":r,
        "original_public_moderation":{
            "candidate_row":2151,"selected_products_checked":["P1","P2"],
            "public_reviews_classified":reviews,
            "natural_review_class_counts":{
                "approve":1,"reject":1,"leave_unchanged":1,
                "edit_rating_and_leave_pending":1},
            "source_pending_review_count":4},
        "original_public_create_if_missing":{
            "candidate_row":2001,
            "original_public_tag_rows_visible":2,
            "selected_public_tag_classifications":tags,
            "natural_tag_class_counts":{
                "tag_already_exists_no_create":2,
                "tag_missing_create_candidate":3}},
    }

class NativePublicOnlyFalseProofTests(unittest.TestCase):
    def test_source_original_public_conditional_policy_and_abstention(self):
        cases=[(5,"active","Supplements",False,"approve"),
               (4,"active","Home",True,"edit_rating_and_leave_pending"),
               (2,"active","Home",True,"reject"),
               (5,"suspended","Supplements",False,"reject"),
               (3,"active","Supplements",False,"leave_unchanged"),
               (5,"unknown","Home",False,"unresolved")]
        for a,b,c,d,out in cases:
            self.assertEqual(categorize_review(a,b,c,d),out)
    def test_preregistered_spec_has_read_only_observation_budget(self):
        self.assertEqual(len(check_spec(SPEC)),64)
        original=json.loads(SPEC.read_text())
        for k,modify in [
            ("private_checker",lambda x:x["sampling"].__setitem__(
                "original_verifier_never_mounted_or_executed",False)),
            ("learned_state",lambda x:x["sampling"].__setitem__(
                "source_original_state_unchanged",False)),
            ("different_dataset",lambda x:x["source"].__setitem__(
                "full_raw_sha256","a"*64)),
            ("more_tools",lambda x:x["sampling"].__setitem__("max_total_calls",400)),
            ("several_invalid_families",lambda x:x["source"].__setitem__(
                "candidates",[2001,2151,710])),
        ]:
            x=copy.deepcopy(original);modify(x)
            with self.subTest(k=k),tempfile.TemporaryDirectory() as d:
                f=Path(d)/"mutant.json"
                f.write_text(json.dumps(x))
                with self.assertRaises(ValueError):check_spec(f)
    def test_independent_real_public_gate_replays_synthetic_fixture(self):
        x=original_fixture()
        z=adjudicate(x,spec=SPEC)
        self.assertTrue(z["qualifying_natural_mixed_observation_cohort_found"])
        self.assertTrue(z["original_source_moderation_policy_all_three_required_classes_observed"])
        self.assertTrue(z["native_create_if_missing_original_both_classes_observed"])
        self.assertEqual(z["original_source_public_selected_tool_calls_verified"],7)
        self.assertTrue(z["no_learned_policy_or_private_terminal_reward_evidence"])
    def test_reject_forged_native_source_public_receipts(self):
        original=original_fixture()
        mutations=[
            ("modified_original_source",lambda x:x.__setitem__(
                "original_whole_source_sha256","0"*64)),
            ("private_state_exposed",lambda x:x.__setitem__(
                "source_original_private_verifier_not_executed",False)),
            ("selected_read_mutation",lambda x:x["actual_source_public_tool_receipts"][0].__setitem__(
                "selected_read_only_tool","delete_review")),
            ("forged_reply_hash",lambda x:x["actual_source_public_tool_receipts"][0].__setitem__(
                "actual_public_reply_sha256","0"*64)),
            ("forged_account_status",lambda x:x["original_public_moderation"][
                "public_reviews_classified"][0].__setitem__(
                    "public_account_status","suspended")),
            ("forged_moderation_class",lambda x:x["original_public_moderation"][
                "public_reviews_classified"][0].__setitem__(
                    "original_public_task_action_class","reject")),
            ("forged_tag_exists",lambda x:x["original_public_create_if_missing"][
                "selected_public_tag_classifications"][0].__setitem__(
                    "public_existing_tag_record_found",False)),
            ("source_reply_failed",lambda x:x["actual_source_public_tool_receipts"][0].__setitem__(
                "raw_actual_original_public_reply","{'success':False,'data':[]}")),
            ("unmetered_added_tool",lambda x:x["actual_source_public_tool_receipts"].append(
                copy.deepcopy(x["actual_source_public_tool_receipts"][0]))),
            ("no_real_read",lambda x:x["actual_source_public_tool_receipts"].pop(0)),
            ("fake_worker_rss",lambda x:x["actual_source_public_tool_receipts"][0].__setitem__(
                "source_worker_peak_rss_kib",0)),
            ("wrong_original_class",lambda x:x[
                "original_source_classes_and_public_task_identity"]["2151"].__setitem__(
                    "original_source_executable_class_sha256","0"*64)),
        ]
        for tag,mutate in mutations:
            x=copy.deepcopy(original);mutate(x)
            with self.subTest(tag=tag),self.assertRaises(ValueError):
                adjudicate(x,spec=SPEC)

if __name__=="__main__":
    unittest.main()
