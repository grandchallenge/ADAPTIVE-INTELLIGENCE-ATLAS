#!/usr/bin/env python3
"""OWI-EC-005T: second predeclared ORIGINAL TRAIN source-public native support cohort.

Actual unchanged original train families 1549/1900/5/2000; no state mutation,
source public task masking, private verifier or outcome learning. The source
class executes only in restricted nonroot/offline/cap-dropped/read-only Docker.
Every public record below comes from the original source's physically selected
read-only declared tool and its actual reply; unknown != absent != no-op.
"""
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path
from owi_ec005_realtools_goal_policy import WORKER, unpack_reply
from owi_ec005_realtools_intake import canonical
from owi_ec005_realtools_randomized import IMAGE, call_child, fingerprint

CONTRACT="OWI-EC005T-NATIVE-SECOND-TRAIN-CANDIDATE-PUBLIC-ONLY/1"
SPEC="OWI-EC005T-ORIGINAL-NATIVE-SECOND-CANDIDATE-CURRENT-STATE-SUPPORT/1"
RAW_SHA="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
ROWS=(1549,1900,5,2000)
TARGETS={
    "Lumina Wireless Earbuds":0,
    "Maple & Sage Candle":3,
    "Borealis Expedition Jacket":1,
    "Reverie: Short Stories":2,
    "Astra Stainless Water Bottle":5,
}
FOLDERS=("Health & Wellness","Traditional Chinese Medicine",
         "Herbal Formulas","Acupuncture","Dietary Therapy")
SAFE={
    1549:{"get_user_by_name","get_cart_by_user_id","list_cart_items",
          "get_product_by_name"},
    1900:{"get_subscriber_by_email","list_subscriptions_for_subscriber",
          "check_subscription_exists_for_location"},
    5:{"get_user_account_by_username","get_participant_by_user_account",
       "list_current_enrollments_for_participant","list_enrollments_for_participant",
       "get_clinical_trial_by_id"},
    2000:{"list_folders"},
}
FIRST={1549:("get_user_by_name",{"name":"Alice Chan"}),
       1900:("get_subscriber_by_email",{"email":"alice.chan@example.com"}),
       5:("get_user_account_by_username",{"username":"farida.youssef"}),
       2000:("list_folders",{})}

def verified_protocol(path):
    raw=path.read_bytes();obj=json.loads(raw)
    c=obj.get("source",{});s=obj.get("sampling",{})
    q=obj.get("qualification",{})
    if (obj.get("contract")!=SPEC or c.get("full_sha256")!=RAW_SHA or
        c.get("group_seed")!=4611 or c.get("partition")!="train" or
        c.get("exact_distinct_original_family_rows")!=list(ROWS) or
        c.get("original_private_verifier_never_mounted_or_executed") is not True or
        c.get("sealed_dev_test_task_or_tools_never_opened") is not True or
        s.get("max_total_selected_public_tool_calls")!=35 or
        s.get("source_initial_state_unmodified") is not True or
        s.get("original_user_task_unmodified") is not True or
        s.get("all_tools_physical_original_declared_public_read_only") is not True or
        s.get("source_private_final_state_discarded") is not True or
        q.get("each_candidate_qualifies_only_on_actual_original_public_action_needed_and_original_public_authorized_noaction_both") is not True or
        q.get("existing_other_record_is_not_noop_for_requested_action") is not True or
        obj.get("candidates",[{}])[0].get("public_target_quantities")!=TARGETS):
        raise ValueError("T source-native exact precommitted scope or safety/threshold drift")
    return hashlib.sha256(raw).hexdigest()

def parse_public(row,folder):
    pub=json.loads((folder/"public.json").read_text())
    if not isinstance(pub,dict) or set(pub)!={"messages","tools"}:
        raise ValueError("unexpected source private data in original task public bundle")
    task="\n".join(v.get("content","") for v in pub["messages"] if v.get("role")=="user")
    anchors={
        1549:["Alice Chan","CRT-X01","Lumina Wireless Earbuds",
              "Maple & Sage Candle","Borealis Expedition Jacket",
              "Reverie: Short Stories","Astra Stainless Water Bottle"],
        1900:["alice.chan@example.com","34.0522","51.5074","37.7749",
              "only if she does not already have a subscription"],
        5:["farida.youssef","NeuroNova IV","ImmunoStar III","consent_status"],
        2000:["Health & Wellness","Traditional Chinese Medicine",
              "Herbal Formulas","Acupuncture","Dietary Therapy"],
    }[row]
    if not all(s.casefold() in task.casefold() for s in anchors):
        raise ValueError("original source user public task changed; no fabricated task")
    schemas={}
    for t in pub["tools"]:
        if (not isinstance(t,dict) or not isinstance(t.get("name"),str) or
            not isinstance(t.get("parameters"),dict)):
            raise ValueError("source public declared tool schema invalid")
        schemas[t["name"]]=t["parameters"]
    if FIRST[row][0] not in schemas:
        raise ValueError("precommitted first original source public read not declared")
    return pub,schemas,task

def public_projection(value):
    """Drop source-public credential-like fields even from synthetic benchmark replies."""
    if isinstance(value,dict):
        return {k:public_projection(v) for k,v in value.items() if
                not any(t in str(k).casefold() for t in
                        ("password","secret","token","credential","private_key","api_key"))}
    if isinstance(value,list):return [public_projection(x) for x in value]
    return value

def public_value(rec):
    if not isinstance(rec,dict) or rec.get("status")!="source_success":
        return None
    obj=unpack_reply(rec["raw_actual_original_public_reply"])
    return obj.get("data") if obj.get("success") is True else None

def items(x):
    if isinstance(x,list):return [r for r in x if isinstance(r,dict)]
    if isinstance(x,dict):
        for key in ("data","items","carts","cart_items","subscriptions",
                    "enrollments","folders","results","records","trials"):
            if key in x:return items(x[key])
        if all(isinstance(z,dict) for z in x.values()):
            return list(x.values())
        return [x]
    return []

def first(x):
    arr=items(x)
    return arr[0] if arr else None

def primitive_id(record,names):
    if not isinstance(record,dict):return None
    for n in names:
        v=record.get(n)
        if isinstance(v,(str,int)) and str(v):
            return str(v)
    return None

class NativeReader:
    def __init__(self,base,schemas):
        self.base=base
        self.schemas=schemas
        self.receipts=[]
        self.omissions=[]
    def call(self,row,tool,args):
        if len(self.receipts)>=35:
            raise RuntimeError("actual physical original source read budget exhausted")
        if tool not in SAFE[row]:
            raise ValueError("original native source mutation/tool not precommitted read-only")
        schema=self.schemas[row].get(tool)
        if not isinstance(schema,dict):
            self.omissions.append({"original_row":row,"tool":tool,
                                   "reason":"source_public_tool_not_declared"})
            return None
        required=schema.get("required",[])
        if (not isinstance(required,list) or set(args)!=set(required) or
            any(not isinstance(k,str) for k in required)):
            self.omissions.append({"original_row":row,"tool":tool,
                                   "reason":"original_source_public_schema_not_satisfied",
                                   "declared_required":required,
                                   "supplied_public_argument_names":sorted(args)})
            return None
        commands="".join(json.dumps(x,sort_keys=True)+"\n" for x in (
            {"action":"call","tool":tool,"arguments":args},
            {"action":"finish"}))
        result,wall=call_child(IMAGE,WORKER,
                  self.base/str(row)/"environment.json",
                  input_text=commands,timeout=90)
        if (len(result)!=3 or result[0].get("kind")!="ready" or
            result[0].get("verifier_present") is not False or
            result[1].get("kind")!="observation" or
            result[1].get("tool")!=tool or
            result[1].get("truncated") is not False or
            result[2].get("kind")!="private_final_state" or
            result[2].get("tool_calls")!=1):
            raise RuntimeError("actual restricted source-public IPC invalid")
        actual_reply=result[1].get("content")
        if not isinstance(actual_reply,str) or len(actual_reply)>8192:
            raise RuntimeError("oversized or wrong source actual public reply")
        ok=result[1].get("ok") is True
        native=unpack_reply(actual_reply) if ok else {"success":False}
        public_evidence=public_projection(native)
        safe_reply=repr(public_evidence)
        status="source_success" if ok and native.get("success") is True else "source_failure"
        record={
            "original_row":row,
            "selected_public_read_tool":tool,
            "actual_original_source_public_arguments":args,
            "raw_actual_original_public_reply":safe_reply,
            "sha256_actual_original_public_reply":fingerprint(safe_reply),
            "sha256_full_original_reply_audit_only":hashlib.sha256(actual_reply.encode()).hexdigest(),
            "source_public_sensitive_field_redacted":public_evidence!=native,
            "status":status,
            "physical_original_source_tool_seconds":result[1].get("elapsed_seconds"),
            "physical_source_worker_wall_seconds":wall,
            "physical_worker_peak_rss_kib":result[2].get("peak_rss_kib"),
            "source_private_final_state_discarded":True,
            "source_private_native_verifier_not_executed":True,
        }
        # Deliberately never read or serialize original private final state fields.
        result=None
        self.receipts.append(record)
        return record
    def outcome(self,row):
        return [r for r in self.receipts if r["original_row"]==row]
    def note(self,row,key):
        self.omissions.append({"original_row":row,"reason":key})

def read_cart(reader):
    row=1549
    rec=reader.call(row,*FIRST[row])
    who=first(public_value(rec))
    uid=primitive_id(who,("user_id","_id","id"))
    if not uid:
        reader.note(row,"source_user_id_not_observed")
        return
    cart=reader.call(row,"get_cart_by_user_id",{"user_id":uid})
    c=first(public_value(cart))
    cid=primitive_id(c,("cart_id","_id","id"))
    if cid!="CRT-X01":
        reader.note(row,"original_requested_cart_not_authoritatively_identified")
    # CRT-X01 is from the unchanged ORIGINAL public user task. Read it,
    # but never certify it as that user's cart absent independent public linkage.
    reader.call(row,"list_cart_items",{"cart_id":"CRT-X01"})
    for name in TARGETS:
        reader.call(row,"get_product_by_name",{"name":name})

def read_subscriber(reader):
    row=1900
    # Alias 'email_address' comes from the original public *declared schema*,
    # not hidden state. Our first canary revealed that schema name.
    declared=reader.schemas[row].get("get_subscriber_by_email",{}).get("required",[])
    email_args=({"email_address":"alice.chan@example.com"}
                if declared==["email_address"] else FIRST[row][1])
    rec=reader.call(row,"get_subscriber_by_email",email_args)
    who=first(public_value(rec))
    subscriber=primitive_id(who,("subscriber_id","_id","id"))
    if not subscriber:
        reader.note(row,"original_source_subscriber_id_not_observed")
        return
    reader.call(row,"list_subscriptions_for_subscriber",{"subscriber_id":subscriber})
    source_schema=reader.schemas[row].get("check_subscription_exists_for_location",{})
    needed=source_schema.get("required",[])
    aliases={"subscriber_id":subscriber,
             "latitude":37.7749,"longitude":-122.4194,
             "lat":37.7749,"lon":-122.4194,
             "lng":-122.4194}
    if isinstance(needed,list) and set(needed)<=set(aliases):
        args={k:aliases[k] for k in needed}
        # Without subscriber scope, duplicate status does not authorize
        # a user-specific no-op claim. It may still be diagnostic evidence.
        reader.call(row,"check_subscription_exists_for_location",args)
    else:reader.note(row,"conditional_create_public_check_required_schema_unknown")

def read_trial(reader):
    row=5
    rec=reader.call(row,*FIRST[row])
    who=first(public_value(rec))
    account_id=primitive_id(who,("account_id","user_account_id","user_id","_id","id"))
    pid=primitive_id(who,("participant_id",))
    if not account_id and not pid:
        reader.note(row,"original_public_user_account_not_observed")
        return
    if account_id:
        required=reader.schemas[row].get("get_participant_by_user_account",{}).get("required",[])
        known={"user_account_id":account_id,"account_id":account_id}
        if isinstance(required,list) and set(required)<=set(known):
            participant=reader.call(row,"get_participant_by_user_account",
                                    {k:known[k] for k in required})
            p=first(public_value(participant))
            next_pid=primitive_id(p,("participant_id","_id","id"))
            if next_pid and pid and next_pid!=pid:
                reader.note(row,"original_public_participant_id_link_mismatch")
            elif next_pid:pid=next_pid
    if not pid:
        reader.note(row,"original_source_participant_id_not_observed")
        return
    current=reader.call(row,"list_current_enrollments_for_participant",
                        {"participant_id":pid})
    reader.call(row,"list_enrollments_for_participant",{"participant_id":pid})
    seen=set()
    for enrollment in items(public_value(current))[:5]:
        trial_id=primitive_id(enrollment,("trial_id","clinical_trial_id"))
        if trial_id and trial_id not in seen:
            seen.add(trial_id)
            reader.call(row,"get_clinical_trial_by_id",{"trial_id":trial_id})

def read_bookmarks(reader):
    reader.call(2000,*FIRST[2000])

def run(input_dir,spec):
    proto=verified_protocol(spec)
    identities={}
    schema={}
    for row in ROWS:
        folder=input_dir/str(row)
        public,schemas,_=parse_public(row,folder)
        env=json.loads((folder/"environment.json").read_text())
        cls=env.get("class_code")
        if not isinstance(cls,str) or len(cls)<100:
            raise ValueError("bad source class identity in separate privileged audit")
        identities[str(row)]={
            "public_task_sha256":hashlib.sha256(canonical(public)).hexdigest(),
            "original_executable_class_sha256":hashlib.sha256(cls.encode()).hexdigest()}
        schema[row]=schemas
        del env,cls
    if len({v["original_executable_class_sha256"]
            for v in identities.values()})!=len(ROWS):
        raise ValueError("not four independent original training executable source families")
    reader=NativeReader(input_dir,schema)
    read_cart(reader)
    read_subscriber(reader)
    read_trial(reader)
    read_bookmarks(reader)
    # Do not conditionally substitute a different task if this cohort is negative.
    return {
        "contract":CONTRACT,
        "original_source_full_sha256":RAW_SHA,
        "frozen_original_source_current_state_protocol_sha256":proto,
        "original_source_train_rows":list(ROWS),
        "original_public_and_class_hashes":identities,
        "original_private_source_and_native_verifier_not_exported":True,
        "original_source_initial_state_and_user_task_unmodified":True,
        "original_source_public_only_read_calls_physically_executed":len(reader.receipts),
        "source_public_selected_read_receipts":reader.receipts,
        "public_schema_or_source_evidence_omissions":reader.omissions,
        "no_original_source_private_checker_executed":True,
        "no_actual_terminal_reward_or_policy_training":True,
        "sealed_dev_and_test_families_unopened":True,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",required=True,type=Path)
    p.add_argument("--task-spec",required=True,type=Path)
    p.add_argument("--output",required=True,type=Path)
    a=p.parse_args()
    v=run(a.input_dir,a.task_spec)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
    print("OWI_EC005T_ACTUAL_SOURCE_PUBLIC_ONLY_RECEIPTS",
          json.dumps({"rows":v["original_source_train_rows"],
                      "original_native_read_calls":v["original_source_public_only_read_calls_physically_executed"],
                      "selected_reads":[
                          {"row":r["original_row"],"tool":r["selected_public_read_tool"],
                           "status":r["status"],"public_reply":r["raw_actual_original_public_reply"][:1400]}
                          for r in v["source_public_selected_read_receipts"]],
                      "omissions":v["public_schema_or_source_evidence_omissions"]},
                     sort_keys=True))
if __name__=="__main__":
    main()
