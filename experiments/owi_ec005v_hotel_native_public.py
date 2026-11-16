#!/usr/bin/env python3
"""V: genuinely executed ORIGINAL TRAIN hotel row236 dated public-only observations.

All 159084981 original source bytes and unchanged environment class/family/public
task are checked prior to source selection; source-native third-party class
executes ONLY in existing networkless/cap-dropped/nonroot/readonly Docker.
Original verifier never mounted or called. Source-private final state discarded.
Public room IDs selected ONLY from actual original public list replies; source
user instructions determine exact dates. No booking/cancellation/mutation.
"""
from __future__ import annotations
import argparse,hashlib,json,os,tempfile
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_split import partition
from owi_ec005_realtools_intake import canonical,public_view
from owi_ec005_realtools_episode_select import write_json
from owi_ec005_realtools_goal_policy import WORKER,unpack_reply
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint
from owi_ec005u_source_eligibility import redact

CONTRACT="OWI-EC005V-ACTUAL-ORIGINAL-HOTEL-NATIVE-DATED-PUBLIC-READS/1"
SPEC="OWI-EC005V-ORIGINAL-HOTEL-DATED-CONDITIONAL-SOURCE-PUBLIC-V1"
CORPUS="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
FAMILY="fd0d8974e2af1954f04775ff85b3bc002a4c6bc14b35c5883a28555d8adaa4df"
PUBLIC_PROMPT="25d2be96389844fe56ff7490182876380bc2b0e153ee3da53598dc265b24708d"
ROW=236
ALICE_A=("2024-07-01","2024-07-04")
ALICE_B=("2024-07-04","2024-07-06")
JONATHAN=("2024-07-02","2024-07-04")
INITIAL=[
    ("list_available_rooms",{}),
    ("list_available_rooms_by_type",{"room_type":"double"}),
    ("list_available_rooms_by_type",{"room_type":"suite"}),
    ("list_bookings_by_guest",{"guest_id":"GUEST1"}),
    ("list_bookings_by_guest",{"guest_id":"GUEST2"})
]
ALLOWED={
 "list_available_rooms","list_available_rooms_by_type",
 "list_bookings_by_guest","get_room_info","get_room_amenities",
 "list_active_bookings_for_room","check_room_availability_over_date_range"
}
AVAIL_ARGS=("room_id","requested_check_in_date","requested_check_out_date")

def verified_spec(path):
    raw=path.read_bytes();p=json.loads(raw)
    source=p.get("source",{});plan=p.get("precommitted_selection",{})
    task=p.get("public_original_user_task",{})
    sci=p.get("preregistered_scientific_adjudication",{})
    if (p.get("contract")!=SPEC or
        source.get("full_raw_sha256")!=CORPUS or
        source.get("original_source_group_sha256")!=FAMILY or
        source.get("original_public_prompt_sha256")!=PUBLIC_PROMPT or
        source.get("split_seed")!=4611 or
        source.get("original_train_row")!=ROW or
        source.get("original_class_and_initial_state_unmodified") is not True or
        source.get("private_checker_never_mounted_or_executed") is not True or
        source.get("dev_and_sealed_test_tasks_not_exported") is not True or
        [tuple((x[0],x[1])) for x in plan.get("first_source_public_calls",[])]!=
           [(x[0],x[1]) for x in INITIAL] or
        plan.get("max_distinct_rooms")!=6 or
        plan.get("max_actual_native_public_read_calls")!=40 or
        plan.get("availability_tool_exact_required")!=list(AVAIL_ARGS) or
        plan.get("source_private_final_state_never_read") is not True or
        plan.get("source_private_input_bundle_outside_evidence_artifact_auto_destroyed") is not True or
        task.get("alice_replacement_segment_A",{}).get("check_in")!=ALICE_A[0] or
        task.get("alice_replacement_segment_B",{}).get("check_out_exclusive")!=ALICE_B[1] or
        task.get("jonathan_booking",{}).get("check_in")!=JONATHAN[0] or
        task.get("cannot_treat_a_pre_cancellation_conflict_due_only_to_alice_booking_as_final_skip") is not True or
        sci.get("qualifying_negative_means_original_source_availability_false_for_same_jonathan_dates_and_original_non_cancellable_booking_overlaps") is not True or
        sci.get("qualifying_same_rule_positive_and_negative_are_candidate_room_SELECT_SKIP_not_whole_task_NOOP") is not True):
        raise ValueError("exact original hotel V native public protocol/false-noop rule changed")
    return p,hashlib.sha256(raw).hexdigest()

def rows_of(x):
    if isinstance(x,list):return [z for z in x if isinstance(z,dict)]
    if isinstance(x,dict):
        for k in ("data","rooms","bookings","items","results"):
            if k in x:return rows_of(x[k])
        if all(isinstance(v,dict) for v in x.values()):return list(x.values())
        return [x]
    return []
def source_id(x,key):
    return x.get(key) if isinstance(x,dict) and isinstance(x.get(key),str) else None

class NativePublicReader:
    def __init__(self,envfile,methods):
        self.envfile=envfile;self.methods=methods;self.calls=[];self.unavailable=[]
    def read(self,tool,args):
        if tool not in ALLOWED or len(self.calls)>=40:raise ValueError("unapproved public method/read cap")
        schema=self.methods.get(tool)
        if schema is None:
            self.unavailable.append({"tool":tool,"args":args,"reason":"original_public_method_not_declared"})
            return None
        required=schema.get("required")
        if not isinstance(required,list) or set(required)!=set(args):
            self.unavailable.append({"tool":tool,"args":args,"reason":"original_public_required_schema_mismatch",
                                     "original_required":required})
            return None
        commands="".join(json.dumps(c,sort_keys=True)+"\n" for c in
                         ({"action":"call","tool":tool,"arguments":args},
                          {"action":"finish"}))
        response,wall=call_child(IMAGE,WORKER,self.envfile,
                                 input_text=commands,timeout=90)
        if (len(response)!=3 or response[0].get("kind")!="ready" or
            response[0].get("verifier_present") is not False or
            response[1].get("kind")!="observation" or
            response[1].get("tool")!=tool or
            response[2].get("kind")!="private_final_state" or
            response[2].get("tool_calls")!=1):
            raise RuntimeError("original source read-only IPC/trust contract violated")
        raw=response[1].get("content")
        if not isinstance(raw,str) or len(raw)>8192:
            raise RuntimeError("original source reply not bounded")
        output_ok=response[1].get("ok") is True and response[1].get("truncated") is False
        unparsed=unpack_reply(raw) if output_ok else {"success":False}
        projected=redact(unparsed)
        raw_projected=repr(projected)
        status="success" if unparsed.get("success") is True and output_ok else "unresolved_source_failure"
        self.calls.append({
           "tool":tool,"arguments":args,
           "declared_required_public_arguments":sorted(required),
           "actual_original_unredacted_public_reply_sha256":hashlib.sha256(raw.encode()).hexdigest(),
           "redacted_actual_original_source_public_reply":raw_projected,
           "redacted_original_source_public_reply_sha256":fingerprint(raw_projected),
           "source_original_read_status":status,
           "source_original_reply_truncated":response[1].get("truncated"),
           "physically_executed_native_source_tool_seconds":response[1].get("elapsed_seconds"),
           "physically_executed_restricted_source_container_wall_seconds":wall,
           "source_worker_peak_rss_kib":response[2].get("peak_rss_kib"),
           "source_private_final_state_discarded_without_inspection":True,
           "original_private_verifier_not_mounted_or_called":True,
        })
        response=None
        if status!="success":return None
        return projected.get("data")

def selected_rooms(available_doubles,available_suites,alice_bookings,jonathan_bookings):
    rooms=[]
    for group,limit in ((available_doubles,2),(available_suites,2),
                        ([x for x in alice_bookings if x.get("status")=="active"],1),
                        ([x for x in jonathan_bookings if x.get("status")=="active"],1)):
        count=0
        for x in group:
            if count>=limit:break
            rid=source_id(x,"room_id")
            if rid and rid not in rooms:
                rooms.append(rid);count+=1
    if len(rooms)>6:raise ValueError("original source public room sample cap violated")
    return rooms

def prepare_original():
    lock=json.loads(Path("governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json").read_text())
    if lock.get("sha256")!=CORPUS:raise ValueError("full source lock changed")
    all_rows=audit_source(lock)
    p=partition(all_rows,seed=4611)
    original={x["row_index"]:x for x in p["partitions"]["train"]}
    if (ROW not in original or original[ROW]["environment_id_sha256"]!=FAMILY
        or original[ROW]["public_prompt_sha256"]!=PUBLIC_PROMPT):
        raise ValueError("hotel original train partition/public prompt mismatch")
    obj=all_rows[ROW];public=public_view(obj)
    task="\n".join(v["content"] for v in public["messages"] if v["role"]=="user")
    for anchor in ("GUEST1","GUEST2","2024-07-01","2024-07-04","2024-07-06",
                   "Mountain View","Work Desk","Do not alter any other existing bookings"):
        if anchor.casefold() not in task.casefold():
            raise ValueError("original source user hotel booking instruction changed")
    env=obj["extra_info"]["environment"]
    methods={}
    for t in env["tools"]:
        f=t.get("function",{}) if isinstance(t,dict) else {}
        if not isinstance(f.get("name"),str) or not isinstance(f.get("parameters"),dict):
            raise ValueError("original hotel source tool public declaration invalid")
        methods[f["name"]]=f["parameters"]
    if not ALLOWED.issubset(methods):
        raise ValueError("source-original hotel read-only interface changed")
    if set(methods["check_room_availability_over_date_range"].get("required",[]))!=set(AVAIL_ARGS):
        raise ValueError("original date-availability exact public schema changed")
    source_env={k:env[k] for k in ("class_code","class_name","initial_state","tools")}
    return public,methods,source_env

def run(spec_path):
    spec,source_spec_hash=verified_spec(spec_path)
    public,methods,env=prepare_original()
    import os
    with tempfile.TemporaryDirectory(prefix="owi_ec005v_private_",dir=os.environ.get("RUNNER_TEMP") or None) as temp:
        envfile=Path(temp)/"environment.json"
        # The file is 0444 for Docker UID 65534 bind mount, while temp
        # parent is private, outside any uploaded artifact path.
        write_json(envfile,env)
        reader=NativePublicReader(envfile,methods)
        initial={}
        for name,args in INITIAL:
            initial[name+":"+json.dumps(args,sort_keys=True)]=reader.read(name,args)
        db=rows_of(initial['list_available_rooms_by_type:{"room_type": "double"}'])
        sb=rows_of(initial['list_available_rooms_by_type:{"room_type": "suite"}'])
        alice=rows_of(initial['list_bookings_by_guest:{"guest_id": "GUEST1"}'])
        jon=rows_of(initial['list_bookings_by_guest:{"guest_id": "GUEST2"}'])
        rooms=selected_rooms(db,sb,alice,jon)
        for rid in rooms:
            info=reader.read("get_room_info",{"room_id":rid})
            reader.read("list_active_bookings_for_room",{"room_id":rid})
            rtype=info.get("room_type") if isinstance(info,dict) and info.get("room_id")==rid else None
            if rtype=="double":
                reader.read("get_room_amenities",{"room_id":rid})
                for start,end in (ALICE_A,JONATHAN):
                    reader.read("check_room_availability_over_date_range",{
                      "room_id":rid,"requested_check_in_date":start,
                      "requested_check_out_date":end})
            elif rtype=="suite":
                reader.read("check_room_availability_over_date_range",{
                    "room_id":rid,"requested_check_in_date":ALICE_B[0],
                    "requested_check_out_date":ALICE_B[1]})
        report={
            "contract":CONTRACT,
            "frozen_original_source_v_protocol_sha256":source_spec_hash,
            "original_corpus_full_2550_task_sha256":CORPUS,
            "original_train_row":ROW,
            "original_train_family_sha256":FAMILY,
            "original_train_public_prompt_sha256":PUBLIC_PROMPT,
            "original_train_public_bundle_sha256":hashlib.sha256(canonical(public)).hexdigest(),
            "original_train_class_code_sha256":hashlib.sha256(env["class_code"].encode()).hexdigest(),
            "original_public_tool_required_schemas":{key:methods[key].get("required") for key in sorted(ALLOWED)},
            "selected_original_source_public_rooms":rooms,
            "selected_original_native_public_read_receipts":reader.calls,
            "unavailable_declared_original_source_public_reads":reader.unavailable,
            "actual_selected_original_source_read_calls":len(reader.calls),
            "original_source_class_task_initial_state_unchanged":True,
            "original_native_private_checker_never_mounted_or_executed":True,
            "source_private_final_state_never_parsed_or_exported":True,
            "original_source_dev_test_tasks_sealed":True,
            "no_source_mutation_nor_native_reward_nor_policy_training":True,
            "source_public_credential_like_fields_redacted":True,
            "natural_same_task_select_skip_support_claim":"NOT_ADJUDICATED_BY_RUNNER",
        }
    return report

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--task-spec",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    result=run(a.task_spec)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("OWI_EC005V_ACTUAL_ORIGINAL_SOURCE_PUBLIC_READS",json.dumps({
        "source_row":ROW,"actual_physical_read_count":result["actual_selected_original_source_read_calls"],
        "native_public_read_status_counts":{
           k:sum(r["source_original_read_status"]==k for r in result["selected_original_native_public_read_receipts"])
           for k in {"success","unresolved_source_failure"}},
        "selected_original_room_ids":result["selected_original_source_public_rooms"],
        "selected_read_summaries":[{"tool":r["tool"],"args":r["arguments"],
          "status":r["source_original_read_status"],
          "redacted_public_response_excerpt":r["redacted_actual_original_source_public_reply"][:850]}
          for r in result["selected_original_native_public_read_receipts"]],
        "unavailable":result["unavailable_declared_original_source_public_reads"]
    },sort_keys=True))
if __name__=="__main__":
    main()
