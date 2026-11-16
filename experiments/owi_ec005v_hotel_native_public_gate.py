#!/usr/bin/env python3
"""Independent OWI-EC005V source-public hotel date/room support gate.

Independently reconstruct original TRAIN row236 selected source tool plan,
observed candidate room identities, exact original task date windows, source
availability decisions, same-date active booking overlaps, and original Alice
booking's intended cancellation. Distinguish current-state candidate select/
skip (if genuinely observed) from terminal task abstention, learned reflection,
post-cancellation availability or original native private checker reward.
No original environment source/hidden state, checker, dev/test task required.
"""
from __future__ import annotations
import argparse,ast,collections,datetime,hashlib,json,math,re
from pathlib import Path

CONTRACT="OWI-EC005V-INDEPENDENT-ORIGINAL-HOTEL-DATED-SUPPORT-GATE/1"
SOURCE_CONTRACT="OWI-EC005V-ACTUAL-ORIGINAL-HOTEL-NATIVE-DATED-PUBLIC-READS/1"
SPEC="OWI-EC005V-ORIGINAL-HOTEL-DATED-CONDITIONAL-SOURCE-PUBLIC-V1"
CORPUS="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
FAMILY="fd0d8974e2af1954f04775ff85b3bc002a4c6bc14b35c5883a28555d8adaa4df"
TASK_SHA="25d2be96389844fe56ff7490182876380bc2b0e153ee3da53598dc265b24708d"
ALICE_A=("2024-07-01","2024-07-04")
ALICE_B=("2024-07-04","2024-07-06")
JONATHAN=("2024-07-02","2024-07-04")
FIRST=[
 ("list_available_rooms",{}),
 ("list_available_rooms_by_type",{"room_type":"double"}),
 ("list_available_rooms_by_type",{"room_type":"suite"}),
 ("list_bookings_by_guest",{"guest_id":"GUEST1"}),
 ("list_bookings_by_guest",{"guest_id":"GUEST2"})
]
METHODS={
 "list_available_rooms":[],
 "list_available_rooms_by_type":["room_type"],
 "list_bookings_by_guest":["guest_id"],
 "get_room_info":["room_id"],
 "list_active_bookings_for_room":["room_id"],
 "get_room_amenities":["room_id"],
 "check_room_availability_over_date_range":[
   "room_id","requested_check_in_date","requested_check_out_date"],
}
SENSITIVE=("password","secret","token","credential","private_key","api_key",
           "auth_header","authentication","oauth","client_secret","authorization","ssn")
def deny(msg):raise ValueError(msg)
def h(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),
                 ensure_ascii=False).encode()).hexdigest()
def ishash(x):
    return isinstance(x,str) and len(x)==64 and all(c in "0123456789abcdef" for c in x)
def metric(x,lo,hi):
    return type(x) in (float,int) and math.isfinite(x) and lo<=x<=hi
def verified_spec(p):
    raw=p.read_bytes();spec=json.loads(raw)
    ss=spec.get("source",{});task=spec.get("public_original_user_task",{})
    plan=spec.get("precommitted_selection",{})
    adj=spec.get("preregistered_scientific_adjudication",{})
    if (spec.get("contract")!=SPEC or ss.get("full_raw_sha256")!=CORPUS or
        ss.get("original_source_group_sha256")!=FAMILY or
        ss.get("original_public_prompt_sha256")!=TASK_SHA or
        ss.get("split_seed")!=4611 or ss.get("original_train_row")!=236 or
        ss.get("original_class_and_initial_state_unmodified") is not True or
        ss.get("private_checker_never_mounted_or_executed") is not True or
        ss.get("dev_and_sealed_test_tasks_not_exported") is not True or
        plan.get("first_source_public_calls")!=[[x,y] for x,y in FIRST] or
        plan.get("max_distinct_rooms")!=6 or
        plan.get("max_actual_native_public_read_calls")!=40 or
        plan.get("availability_tool_exact_required")!=METHODS["check_room_availability_over_date_range"] or
        plan.get("source_private_final_state_never_read") is not True or
        plan.get("source_private_input_bundle_outside_evidence_artifact_auto_destroyed") is not True or
        task.get("alice_replacement_segment_A",{}).get("check_in")!=ALICE_A[0] or
        task.get("alice_replacement_segment_A",{}).get("check_out_exclusive")!=ALICE_A[1] or
        task.get("alice_replacement_segment_B",{}).get("check_in")!=ALICE_B[0] or
        task.get("alice_replacement_segment_B",{}).get("check_out_exclusive")!=ALICE_B[1] or
        task.get("jonathan_booking",{}).get("check_in")!=JONATHAN[0] or
        task.get("jonathan_booking",{}).get("check_out_exclusive")!=JONATHAN[1] or
        task.get("cannot_treat_a_pre_cancellation_conflict_due_only_to_alice_booking_as_final_skip") is not True or
        adj.get("qualifying_negative_means_original_source_availability_false_for_same_jonathan_dates_and_original_non_cancellable_booking_overlaps") is not True or
        adj.get("qualifying_same_rule_positive_and_negative_are_candidate_room_SELECT_SKIP_not_whole_task_NOOP") is not True or
        adj.get("conditional_Work_Desk_evidence_requires_two_available_eligible_jonathan_doubles_one_with_desk_one_without") is not True):
        deny("frozen original hotel source task/date/temporal no-false-skip contract drift")
    return hashlib.sha256(raw).hexdigest()

def source_rows(data):
    if isinstance(data,list):return [x for x in data if isinstance(x,dict)]
    if isinstance(data,dict):
        for key in ("data","bookings","rooms","results","items"):
            if key in data:return source_rows(data[key])
        if all(isinstance(x,dict) for x in data.values()):
            return list(data.values())
        return [data]
    return []
def source_id(row):
    return row.get("room_id") if isinstance(row,dict) and isinstance(row.get("room_id"),str) else None
def chosen(doubles,suites,alice,jonathan):
    seen=[]
    for group,max_count in ((doubles,2),(suites,2),
                     ([x for x in alice if x.get("status")=="active"],1),
                     ([x for x in jonathan if x.get("status")=="active"],1)):
        added=0
        for row in group:
            if added>=max_count:break
            rid=source_id(row)
            if rid and rid not in seen:
                seen.append(rid);added+=1
    if len(seen)>6:deny("source original public selected room cap drift")
    return seen
def overlap(a,b,c,d):
    try:
        a,b,c,d=(datetime.date.fromisoformat(x) for x in (a,b,c,d))
    except (ValueError,TypeError):return False
    return a<b and c<d and max(a,c)<min(b,d)

class Gate:
    def __init__(self,report):
        self.report=report
        receipts=report.get("selected_original_native_public_read_receipts")
        if (not isinstance(receipts,list) or not 5<=len(receipts)<=40 or
            report.get("actual_selected_original_source_read_calls")!=len(receipts)):
            deny("actual original source public read receipt count missing/forged")
        methods=report.get("original_public_tool_required_schemas")
        if (not isinstance(methods,dict) or set(methods)!=set(METHODS) or
            any(set(methods[k])!=set(v) for k,v in METHODS.items())):
            deny("original source task's declared method required tool arguments changed")
        self.calls=[]
        for receipt in receipts:
            name=receipt.get("tool");args=receipt.get("arguments")
            if name not in METHODS or not isinstance(args,dict) or set(args)!=set(METHODS[name]):
                deny("actual original source read includes illegal/mutating method or fabricated params")
            if receipt.get("declared_required_public_arguments")!=sorted(METHODS[name]):
                deny("native selected public argument schema not exact original")
            raw=receipt.get("redacted_actual_original_source_public_reply")
            if (not isinstance(raw,str) or not raw or len(raw)>8192 or
                any(re.search(r"(?i)['\"]?"+word+r"[a-z_]*['\"]?\s*:",raw)
                    for word in SENSITIVE) or
                re.search(r"(?i)(?:oauth[_ -]?token|bearer\s+\S+|sk-[a-z0-9])",raw)):
                deny("missing/leaked original source PUBLIC tool reply")
            if (not ishash(receipt.get("actual_original_unredacted_public_reply_sha256")) or
                receipt.get("redacted_original_source_public_reply_sha256")!=h(raw) or
                receipt.get("source_private_final_state_discarded_without_inspection") is not True or
                receipt.get("original_private_verifier_not_mounted_or_called") is not True or
                receipt.get("source_original_reply_truncated") is not False or
                not metric(receipt.get("physically_executed_native_source_tool_seconds"),0,60) or
                not metric(receipt.get("physically_executed_restricted_source_container_wall_seconds"),0,90) or
                not metric(receipt.get("source_worker_peak_rss_kib"),1000,1000000)):
                deny("source original receipt physical/read-only/private leak/digest inconsistency")
            try:parsed=ast.literal_eval(raw)
            except (ValueError,SyntaxError,RecursionError,MemoryError,TypeError) as exc:
                raise ValueError("source public original tool data unparseable") from exc
            if not isinstance(parsed,dict) or type(parsed.get("success")) is not bool:
                deny("source original public reply success/schema invalid")
            status="success" if parsed["success"] is True else "unresolved_source_failure"
            if receipt.get("source_original_read_status")!=status:
                deny("source call false success/failure status")
            self.calls.append((name,args,parsed))
        self.at=0
    def take(self,tool,args):
        if self.at>=len(self.calls):
            deny("actual native original selected public read missing")
        name,a,parsed=self.calls[self.at]
        if name!=tool or a!=args:deny("actual selected source public tool/arguments order or identity changed")
        self.at+=1
        return parsed.get("data") if parsed["success"] is True else None
    def done(self):
        if self.at!=len(self.calls):deny("extra original source tool receipt not justified by original public task")

def booking_is_alice_to_cancel(booking):
    return (booking.get("guest_id")=="GUEST1" and
            booking.get("status")=="active" and
            booking.get("check_in_date")=="2024-07-01" and
            booking.get("check_out_date")=="2024-07-05" and
            isinstance(booking.get("booking_id"),str))
def amenities_list(data):
    if isinstance(data,list) and all(isinstance(x,str) for x in data):
        return data
    if isinstance(data,dict) and isinstance(data.get("amenities"),list) and all(
            isinstance(x,str) for x in data["amenities"]):
        return data["amenities"]
    return None
def available_flag(data):
    if isinstance(data,dict) and type(data.get("available")) is bool:
        return data["available"]
    return None

def adjudicate(report,*,spec_path):
    digest=verified_spec(spec_path)
    if (not isinstance(report,dict) or report.get("contract")!=SOURCE_CONTRACT or
        report.get("frozen_original_source_v_protocol_sha256")!=digest or
        report.get("original_corpus_full_2550_task_sha256")!=CORPUS or
        report.get("original_train_row")!=236 or
        report.get("original_train_family_sha256")!=FAMILY or
        report.get("original_train_public_prompt_sha256")!=TASK_SHA or
        not ishash(report.get("original_train_public_bundle_sha256")) or
        not ishash(report.get("original_train_class_code_sha256")) or
        report.get("original_source_class_task_initial_state_unchanged") is not True or
        report.get("original_native_private_checker_never_mounted_or_executed") is not True or
        report.get("source_private_final_state_never_parsed_or_exported") is not True or
        report.get("original_source_dev_test_tasks_sealed") is not True or
        report.get("no_source_mutation_nor_native_reward_nor_policy_training") is not True or
        report.get("source_public_credential_like_fields_redacted") is not True or
        report.get("natural_same_task_select_skip_support_claim")!="NOT_ADJUDICATED_BY_RUNNER"):
        deny("source original provenance/task/secret-free public science boundary changed")
    omitted=report.get("unavailable_declared_original_source_public_reads")
    if not isinstance(omitted,list) or omitted:deny("source original required public tools missing; fail closed rather than synthesize negative availability")
    gate=Gate(report)
    original={}
    for name,args in FIRST:
        original[(name,tuple(sorted(args.items())))]=gate.take(name,args)
    doubles=source_rows(original[("list_available_rooms_by_type",(("room_type","double"),))])
    suites=source_rows(original[("list_available_rooms_by_type",(("room_type","suite"),))])
    guest1=source_rows(original[("list_bookings_by_guest",(("guest_id","GUEST1"),))])
    guest2=source_rows(original[("list_bookings_by_guest",(("guest_id","GUEST2"),))])
    observed=chosen(doubles,suites,guest1,guest2)
    if report.get("selected_original_source_public_rooms")!=observed:
        deny("room candidates not determined by actually observed original public source IDs")
    to_cancel={x["booking_id"] for x in guest1 if booking_is_alice_to_cancel(x)}
    if len(to_cancel)>1:deny("original source Alice original booking cancellation ambiguously identifies multiple records")
    state={}
    checks=[]
    desk={}
    for rid in observed:
        room=gate.take("get_room_info",{"room_id":rid})
        book=gate.take("list_active_bookings_for_room",{"room_id":rid})
        if room is not None and (not isinstance(room,dict) or room.get("room_id")!=rid):
            deny("room public lookup returned mismatched identity/type")
        booklist=source_rows(book)
        if any(x.get("room_id") not in (None,rid) for x in booklist):
            deny("source public active booking fetched for foreign room")
        kind=room.get("room_type") if isinstance(room,dict) else None
        if kind not in ("single","double","suite",None):
            deny("unrecognized original room type")
        state[rid]={"room_type":kind,"source_room_status":room.get("status") if isinstance(room,dict) else None,
                    "active_booking_ids_public":[x.get("booking_id") for x in booklist],
                    "source_amenities":None}
        if kind=="double":
            amen=amenities_list(gate.take("get_room_amenities",{"room_id":rid}))
            state[rid]["source_amenities"]=amen
            for segment,(start,end) in (("Alice A",ALICE_A),("Jonathan",JONATHAN)):
                raw=gate.take("check_room_availability_over_date_range",{
                    "room_id":rid,"requested_check_in_date":start,
                    "requested_check_out_date":end})
                availability=available_flag(raw)
                other_overlap=any(
                    x.get("status")=="active" and
                    x.get("booking_id") not in to_cancel and
                    overlap(x.get("check_in_date"),x.get("check_out_date"),start,end)
                    for x in booklist)
                cancelled_overlap=any(
                    x.get("status")=="active" and
                    x.get("booking_id") in to_cancel and
                    overlap(x.get("check_in_date"),x.get("check_out_date"),start,end)
                    for x in booklist)
                checks.append({"source_room_id":rid,"original_task_segment":segment,
                    "original_task_check_in":start,"original_task_check_out_exclusive":end,
                    "original_source_native_date_available":availability,
                    "original_source_non_cancellable_active_booking_overlap":other_overlap,
                    "original_source_alice_original_to_cancel_overlap":cancelled_overlap,
                    "original_source_public_reason":raw.get("reason") if isinstance(raw,dict) and isinstance(raw.get("reason"),str) else None})
        elif kind=="suite":
            raw=gate.take("check_room_availability_over_date_range",{
                    "room_id":rid,"requested_check_in_date":ALICE_B[0],
                    "requested_check_out_date":ALICE_B[1]})
            checks.append({"source_room_id":rid,"original_task_segment":"Alice B",
                "original_task_check_in":ALICE_B[0],
                "original_task_check_out_exclusive":ALICE_B[1],
                "original_source_native_date_available":available_flag(raw),
                "original_source_non_cancellable_active_booking_overlap":any(
                    x.get("status")=="active" and x.get("booking_id") not in to_cancel and
                    overlap(x.get("check_in_date"),x.get("check_out_date"),*ALICE_B) for x in booklist),
                "original_source_alice_original_to_cancel_overlap":any(
                    x.get("status")=="active" and x.get("booking_id") in to_cancel and
                    overlap(x.get("check_in_date"),x.get("check_out_date"),*ALICE_B) for x in booklist),
                "original_source_public_reason":raw.get("reason") if isinstance(raw,dict) and isinstance(raw.get("reason"),str) else None})
    gate.done()
    jon=[]
    for c in checks:
        if c["original_task_segment"]!="Jonathan":continue
        rid=c["source_room_id"]
        am=state[rid]["source_amenities"]
        has_requirements=(all(x in am for x in ("WiFi","TV"))
                          if isinstance(am,list) else None)
        has_desk=("Work Desk" in am if isinstance(am,list) else None)
        is_positive=(c["original_source_native_date_available"] is True and
                     has_requirements is True)
        # Original task must CANCEL Alice's booking. A negative pre-cancel
        # availability on that *same booking* cannot justify final skip.
        is_negative=(c["original_source_native_date_available"] is False and
                     c["original_source_non_cancellable_active_booking_overlap"] is True)
        jon.append({"original_source_room_id":rid,
                    "source_date_available_pre_cancellation":c["original_source_native_date_available"],
                    "public_amenities_include_WiFi_TV":has_requirements,
                    "public_amenities_include_Work_Desk":has_desk,
                    "public_amenities_include_Mountain_View":("Mountain View" in am if isinstance(am,list) else None),
                    "same_original_Jonathan_conditional_eligible_now":is_positive,
                    "same_original_Jonathan_conditional_ineligible_due_to_non_cancellable_booking":is_negative,
                    "original_booking_to_cancel_overlaps":c["original_source_alice_original_to_cancel_overlap"],
                    "other_unchangeable_active_booking_overlaps":c["original_source_non_cancellable_active_booking_overlap"]})
    positive=[x["original_source_room_id"] for x in jon if x["same_original_Jonathan_conditional_eligible_now"]]
    negative=[x["original_source_room_id"] for x in jon if x["same_original_Jonathan_conditional_ineligible_due_to_non_cancellable_booking"]]
    desk_present=[x["original_source_room_id"] for x in jon if
                  x["same_original_Jonathan_conditional_eligible_now"] and x["public_amenities_include_Work_Desk"] is True]
    desk_missing=[x["original_source_room_id"] for x in jon if
                  x["same_original_Jonathan_conditional_eligible_now"] and x["public_amenities_include_Work_Desk"] is False]
    support=any(a!=b for a in positive for b in negative)
    desk_support=bool(desk_present and desk_missing)
    # Independent joint-capacity diagnostic: both Alice A and Jonathan
    # request a double over overlapping dates, and a single double cannot
    # host both even when each independent prebooking availability read is
    # true. This does NOT modify the frozen select/skip qualification rule.
    alice_a_current_positive=[
        x["source_room_id"] for x in checks
        if x["original_task_segment"]=="Alice A" and
           x["original_source_native_date_available"] is True]
    separate_current_double_pair=any(
        a!=j for a in alice_a_current_positive for j in positive)
    # No currently available suite in the observed original public source
    # candidate sample is not a proof no other suite could ever be booked.
    observed_suite=[rid for rid in observed if state[rid]["room_type"]=="suite"]
    status=("ACTUAL_ORIGINAL_HOTEL_NATIVE_JONATHAN_ROOM_SELECT_SKIP_CONTRAST_SUPPORTED"
           if support else "SCOPED_SOURCE_PUBLIC_HOTEL_DATED_SELECT_SKIP_NOT_QUALIFIED")
    return {
      "contract":CONTRACT,
      "frozen_v_original_source_protocol_sha256":digest,
      "verified_original_full_source_sha256":CORPUS,
      "original_train_family":FAMILY,
      "actual_selected_original_source_public_calls_verified":gate.at,
      "actual_selected_original_source_public_result_status_counts":dict(collections.Counter(
          r["source_original_read_status"] for r in report["selected_original_native_public_read_receipts"])),
      "original_source_public_candidate_rooms":observed,
      "original_alice_original_bookings_identified_for_future_cancellation":sorted(to_cancel),
      "original_room_info_and_current_active_bookings":state,
      "source_native_date_specific_availability_cases":checks,
      "original_jonathan_double_room_source_public_conditional_cases":jon,
      "original_same_rule_select_room_positive_eligible_candidates":positive,
      "alice_segment_A_individually_currently_available_double_rooms":alice_a_current_positive,
      "current_state_distinct_double_rooms_for_overlapping_Alice_A_and_Jonathan_proven":separate_current_double_pair,
      "alice_A_and_Jonathan_requested_dates_overlap":overlap(*ALICE_A,*JONATHAN),
      "source_current_suite_room_candidate_count":len(observed_suite),
      "all_three_original_bookings_jointly_feasible_proven_by_selected_reads":False,
      "original_same_rule_skip_room_non_cancellable_conflict_candidates":negative,
      "original_source_conditional_Work_Desk_already_present_candidates":desk_present,
      "original_source_conditional_Work_Desk_missing_add_candidates":desk_missing,
      "natural_same_original_jonathan_date_availability_SELECT_SKIP_pair_supported":support,
      "natural_same_original_Work_Desk_add_skip_pair_supported":desk_support,
      "original_entire_hotel_task_NO_ACTION_authorized_or_proved":False,
      "pre_cancellation_unavailability_may_change_after_original_alice_booking_cancellation":True,
      "original_private_source_or_native_checker_never_used":True,
      "original_dev_and_sealed_test_task_content_not_accessed":True,
      "no_original_source_mutation_training_or_terminal_reward":True,
      "scientific_disposition":status,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--trial",type=Path,required=True)
    p.add_argument("--task-spec",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    result=adjudicate(json.loads(a.trial.read_text()),spec_path=a.task_spec)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("OWI_EC005V_INDEPENDENT_ORIGINAL_HOTEL_DATED_SOURCE_GATE",json.dumps(result,sort_keys=True))
if __name__=="__main__":
    main()
