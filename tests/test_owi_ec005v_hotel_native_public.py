#!/usr/bin/env python3
"""Hostile source-public hotel V evidence tests (synthetic, NOT empirical results).

Fixtures distinguish original Alice booking cancellation (transient false)
from other active booking blocking same Jonathan dates (valid skip), and
source-original conditional Work Desk already-present/missing differences.
No source-private checker, class, initial state or source tool called in tests.
"""
from __future__ import annotations
import copy,hashlib,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005v_hotel_native_public import verified_spec
from owi_ec005v_hotel_native_public_gate import adjudicate,CONTRACT,CORPUS,FAMILY,TASK_SHA
from owi_ec005_realtools_randomized import fingerprint
from owi_ec005u_source_eligibility import redact

SPEC=Path(__file__).resolve().parents[1]/"governance/research/OWI_EC005V_HOTEL_DATED_CONDITIONAL_V1.json"
SCHEMA={
 "list_available_rooms":[],
 "list_available_rooms_by_type":["room_type"],
 "list_bookings_by_guest":["guest_id"],
 "get_room_info":["room_id"],
 "list_active_bookings_for_room":["room_id"],
 "get_room_amenities":["room_id"],
 "check_room_availability_over_date_range":[
  "room_id","requested_check_in_date","requested_check_out_date"],
}
ORIGINAL={"booking_id":"BK1001","guest_id":"GUEST1","room_id":"RM202",
          "status":"active","check_in_date":"2024-07-01",
          "check_out_date":"2024-07-05"}
OTHER={"booking_id":"BK-OTHER","guest_id":"GUEST2","room_id":"D3",
       "status":"active","check_in_date":"2024-07-02",
       "check_out_date":"2024-07-04"}
def observation(name,args,data):
    rendered=repr({"success":True,"data":data})
    return {
      "tool":name,"arguments":args,
      "declared_required_public_arguments":sorted(SCHEMA[name]),
      "actual_original_unredacted_public_reply_sha256":hashlib.sha256(rendered.encode()).hexdigest(),
      "redacted_actual_original_source_public_reply":rendered,
      "redacted_original_source_public_reply_sha256":fingerprint(rendered),
      "source_original_read_status":"success",
      "source_original_reply_truncated":False,
      "physically_executed_native_source_tool_seconds":0.002,
      "physically_executed_restricted_source_container_wall_seconds":0.12,
      "source_worker_peak_rss_kib":17000,
      "source_private_final_state_discarded_without_inspection":True,
      "original_private_verifier_not_mounted_or_called":True,
    }
def fixture(*,include_other=True,second_desk_missing=True):
    doubles=[
      {"room_id":"D1","room_type":"double","status":"available",
       "amenities":["WiFi","TV","Work Desk","Mountain View"]},
      {"room_id":"D2","room_type":"double","status":"available",
       "amenities":["WiFi","TV"] if second_desk_missing else ["WiFi","TV","Work Desk"]}]
    rooms=[*doubles,{"room_id":"RM202","room_type":"double","status":"reserved",
                     "amenities":["WiFi","TV"]}]
    guest2=[OTHER] if include_other else []
    if include_other:rooms.append({"room_id":"D3","room_type":"double",
                                   "status":"reserved","amenities":["WiFi","TV"]})
    actions=[
      observation("list_available_rooms",{},doubles),
      observation("list_available_rooms_by_type",{"room_type":"double"},doubles),
      observation("list_available_rooms_by_type",{"room_type":"suite"},[]),
      observation("list_bookings_by_guest",{"guest_id":"GUEST1"},[ORIGINAL]),
      observation("list_bookings_by_guest",{"guest_id":"GUEST2"},guest2),
    ]
    for room in rooms:
        rid=room["room_id"]
        bookings=([ORIGINAL] if rid=="RM202" else
                  [OTHER] if rid=="D3" else [])
        actions.append(observation("get_room_info",{"room_id":rid},room))
        actions.append(observation("list_active_bookings_for_room",{"room_id":rid},bookings))
        actions.append(observation("get_room_amenities",{"room_id":rid},room["amenities"]))
        for datea,dateb in (("2024-07-01","2024-07-04"),
                            ("2024-07-02","2024-07-04")):
            available=rid in ("D1","D2")
            actions.append(observation("check_room_availability_over_date_range",{
                "room_id":rid,"requested_check_in_date":datea,
                "requested_check_out_date":dateb},{"available":available,
                  "reason":"active booking overlaps" if not available else ""}))
    return {
        "contract":"OWI-EC005V-ACTUAL-ORIGINAL-HOTEL-NATIVE-DATED-PUBLIC-READS/1",
        "frozen_original_source_v_protocol_sha256":verified_spec(SPEC)[1],
        "original_corpus_full_2550_task_sha256":CORPUS,
        "original_train_row":236,"original_train_family_sha256":FAMILY,
        "original_train_public_prompt_sha256":TASK_SHA,
        "original_train_public_bundle_sha256":"a"*64,
        "original_train_class_code_sha256":"b"*64,
        "original_public_tool_required_schemas":SCHEMA,
        "selected_original_source_public_rooms":["D1","D2","RM202"]+(["D3"] if include_other else []),
        "selected_original_native_public_read_receipts":actions,
        "unavailable_declared_original_source_public_reads":[],
        "actual_selected_original_source_read_calls":len(actions),
        "original_source_class_task_initial_state_unchanged":True,
        "original_native_private_checker_never_mounted_or_executed":True,
        "source_private_final_state_never_parsed_or_exported":True,
        "original_source_dev_test_tasks_sealed":True,
        "no_source_mutation_nor_native_reward_nor_policy_training":True,
        "source_public_credential_like_fields_redacted":True,
        "natural_same_task_select_skip_support_claim":"NOT_ADJUDICATED_BY_RUNNER",
    }
class OriginalHotelAdversarialTests(unittest.TestCase):
    def test_original_source_freeze_exact_and_temporal_boundary(self):
        p,d=verified_spec(SPEC)
        self.assertEqual(len(d),64)
        self.assertEqual(p["source"]["original_train_row"],236)
        self.assertTrue(p["public_original_user_task"][
            "cannot_treat_a_pre_cancellation_conflict_due_only_to_alice_booking_as_final_skip"])
    def test_synthetic_external_booking_select_skip_distinct_from_alice_cancel(self):
        g=adjudicate(fixture(),spec_path=SPEC)
        self.assertEqual(g["contract"],CONTRACT)
        self.assertTrue(g["natural_same_original_jonathan_date_availability_SELECT_SKIP_pair_supported"])
        self.assertTrue(g["natural_same_original_Work_Desk_add_skip_pair_supported"])
        self.assertEqual(g["original_same_rule_skip_room_non_cancellable_conflict_candidates"],["D3"])
        self.assertEqual(g["original_same_rule_select_room_positive_eligible_candidates"],["D1","D2"])
        self.assertEqual(g["original_alice_original_bookings_identified_for_future_cancellation"],["BK1001"])
        self.assertFalse(g["original_entire_hotel_task_NO_ACTION_authorized_or_proved"])
    def test_original_alice_cancel_only_false_does_not_qualify(self):
        g=adjudicate(fixture(include_other=False),spec_path=SPEC)
        self.assertFalse(g["natural_same_original_jonathan_date_availability_SELECT_SKIP_pair_supported"])
        self.assertEqual(g["original_same_rule_skip_room_non_cancellable_conflict_candidates"],[])
        self.assertTrue(g["natural_same_original_Work_Desk_add_skip_pair_supported"])
    def test_same_desk_status_both_does_not_make_conditional_WorkDesk_support(self):
        g=adjudicate(fixture(second_desk_missing=False),spec_path=SPEC)
        self.assertFalse(g["natural_same_original_Work_Desk_add_skip_pair_supported"])
    def test_source_public_credential_redaction(self):
        data={"success":True,"data":{"authentication_info":"OAuth_Token:fake",
                                      "room_id":"D1","amenities":["WiFi","TV"]}}
        v=redact(data)
        self.assertNotIn("authentication_info",str(v))
        self.assertEqual(v["data"]["room_id"],"D1")
    def test_mutated_frozen_original_source_contract_rejected(self):
        original=json.loads(SPEC.read_text())
        mutations=[
          ("read_cap",lambda x:x["precommitted_selection"].__setitem__(
              "max_actual_native_public_read_calls",400)),
          ("original_date",lambda x:x["public_original_user_task"][
              "alice_replacement_segment_A"].__setitem__("check_in","2024-07-02")),
          ("source_byte_lock",lambda x:x["source"].__setitem__(
              "full_raw_sha256","0"*64)),
          ("checker",lambda x:x["source"].__setitem__(
              "private_checker_never_mounted_or_executed",False)),
          ("state_mutation",lambda x:x["source"].__setitem__(
              "original_class_and_initial_state_unmodified",False)),
          ("fake_cancel_skip",lambda x:x["public_original_user_task"].__setitem__(
              "cannot_treat_a_pre_cancellation_conflict_due_only_to_alice_booking_as_final_skip",False)),
          ("relaxed_non_cancel",lambda x:x["preregistered_scientific_adjudication"].__setitem__(
              "qualifying_negative_means_original_source_availability_false_for_same_jonathan_dates_and_original_non_cancellable_booking_overlaps",False)),
        ]
        for label,patch in mutations:
            with self.subTest(label=label),tempfile.TemporaryDirectory() as tmp:
                data=copy.deepcopy(original);patch(data)
                path=Path(tmp)/"changed.json";path.write_text(json.dumps(data))
                with self.assertRaises(ValueError):verified_spec(path)
    def test_original_source_trust_and_fake_availability_rejected(self):
        mutations=[
          ("private_verifier",lambda x:x.__setitem__(
              "original_native_private_checker_never_mounted_or_executed",False)),
          ("source_state_mutated",lambda x:x.__setitem__(
              "original_source_class_task_initial_state_unchanged",False)),
          ("wrong_family",lambda x:x.__setitem__(
              "original_train_family_sha256","f"*64)),
          ("invented_native_reward",lambda x:x.__setitem__(
              "natural_same_task_select_skip_support_claim","POSITIVE")),
          ("chosen_wrong_room",lambda x:x["selected_original_source_public_rooms"].append("BAD")),
          ("extra_source_mutation",lambda x:x["selected_original_native_public_read_receipts"][0].__setitem__(
              "tool","cancel_booking")),
          ("wrong_exact_source_dates",lambda x:x[
              "selected_original_native_public_read_receipts"][-1]["arguments"].__setitem__(
              "requested_check_out_date","2024-07-05")),
          ("reply_hash_forgery",lambda x:x[
              "selected_original_native_public_read_receipts"][-1].__setitem__(
              "redacted_actual_original_source_public_reply","{'success':True,'data':{'available':True}}")),
          ("fake_public_token",lambda x:x[
              "selected_original_native_public_read_receipts"][-1].__setitem__(
              "redacted_actual_original_source_public_reply","{'success':True,'data':{'authentication_info':'OAuth_Token:mock'}}")),
          ("illegal_original_noop",lambda x:x.__setitem__(
              "source_private_final_state_never_parsed_or_exported",False)),
          ("forged_wall_clock",lambda x:x[
              "selected_original_native_public_read_receipts"][-1].__setitem__(
              "physically_executed_restricted_source_container_wall_seconds",-1)),
        ]
        for label,patch in mutations:
            with self.subTest(label=label):
                x=fixture();patch(x)
                with self.assertRaises(ValueError):adjudicate(x,spec_path=SPEC)
if __name__=="__main__":
    unittest.main()
