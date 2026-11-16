#!/usr/bin/env python3
"""Original source TRAIN row710 named review/status/aggregate audit; public read-only.

Prelocked full original 2550-task source, unchanged original class/initial
state/USER task. External source class executes ONLY restricted pinned Docker.
Original native PRIVATE verifier not mounted; final source state discarded.
Four named professional+specialty and review author targets are exactly
original PUBLIC instructions, not invented external review/noop controls.
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

CONTRACT="OWI-EC005W-ORIGINAL-TRAIN-REVIEW-SELECTED-NATIVE-PUBLIC-READS/1"
SPEC="OWI-EC005W-ORIGINAL-TRAIN-REVIEW-TARGET-STATUS-PUBLIC-AUDIT/1"
SOURCE="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
FAMILY="a739046b13061603e09af000ceed469840dfecba0068db2e1919454b18394b0c"
PROMPT="97bca760aa53e15f281b71771a6b63a1ba294c1ce3123f9632b114cbf12d6d36"
ROW=710
TARGETS=[
 ("Dr. Luke Marquez","Dermatology","Alice Chan","pending","approve","update_after_approval"),
 ("Dr. Ella Navarro","Internal Medicine","Jules Morgan","pending","reject","no_aggregate_contribution_from_rejected"),
 ("Dr. Ella Navarro","Cardiology","Ria Singh","approved","delete","update_after_approved_review_deletion"),
 ("Dr. Sandy Torres","Pediatrics","Silas Huang","rejected","edit_then_set_pending","do_not_update_until_approved"),
]
FIRST=[
 ("list_all_professionals",{}),
 ("list_all_users",{}),
 ("get_professional_by_name",{"name":"Dr. Ella Navarro"}),
]
METHODS={
 "list_all_professionals":[],
 "list_all_users":[],
 "get_professional_by_name":["name"],
 "get_reviews_for_professional":["professional_id"],
 "get_aggregated_rating_for_professional":["professional_id"],
 "get_review_by_user_and_professional":["user_id","professional_id"],
 "get_review_moderation_status":["view_id"]
}

def check_spec(path):
    raw=path.read_bytes()
    p=json.loads(raw);src=p.get("source",{});plan=p.get("prospective_selected_original_public_reads",{})
    auth=p.get("original_task_authority",{});science=p.get("independent_science",{})
    if (p.get("contract")!=SPEC or src.get("full_raw_sha256")!=SOURCE or
        src.get("original_train_row")!=ROW or src.get("group_seed")!=4611 or
        src.get("train_group_sha256")!=FAMILY or src.get("original_public_user_prompt_sha256")!=PROMPT or
        src.get("original_class_state_and_schemas_unchanged") is not True or
        src.get("original_user_task_unchanged") is not True or
        src.get("original_verifier_never_executed") is not True or
        src.get("no_dev_or_sealed_test_task_exposure") is not True or
        [tuple((x[0],x[1])) for x in plan.get("first_fixed_calls",[])]!=FIRST or
        plan.get("max_original_native_selected_public_read_calls")!=27 or
        plan.get("exact_original_required_tool_arguments")!=METHODS or
        plan.get("no_intervention_no_source_write") is not True or
        plan.get("discard_source_private_terminal_state_unexamined") is not True or
        plan.get("stage_source_private_worker_in_auto_cleaned_RUNNER_TEMP_outside_public_artifact") is not True or
        auth.get("every_one_of_four_named_reviews_requires_mutation") is not True or
        auth.get("pure_leave_named_review_unchanged_action_authorized") is not False or
        auth.get("unknown_or_nonexistent_exact_specialty_user_review_is_not_noop") is not True or
        science.get("pure_review_noop_not_authorized_by_original_row710") is not False or
        science.get("cross_target_aggregate_update_skip_not_proof_of_same_instance_variable_initial_state") is not True or
        [tuple((q.get("professional"),q.get("specialty"),q.get("review_author"),
                 q.get("source_expected_review_before"),q.get("requested_action"),q.get("aggregate_after")))
          for q in p.get("source_original_named_targets",[])]!=TARGETS):
        raise ValueError("original source task/qualification or read-only frozen W protocol drift")
    return p,hashlib.sha256(raw).hexdigest()

def records(data):
    if isinstance(data,list):return [v for v in data if isinstance(v,dict)]
    if isinstance(data,dict):
        for k in ("data","items","users","professionals","reviews","results"):
            if k in data:return records(data[k])
        return [data]
    return []

def unique_by(items,key,value,*,extra_key=None,extra_val=None):
    match=[x for x in items if isinstance(x,dict) and
           isinstance(x.get(key),str) and x[key].casefold()==value.casefold() and
           (extra_key is None or (isinstance(x.get(extra_key),str) and
            x[extra_key].casefold()==extra_val.casefold()))]
    return match[0] if len(match)==1 else None

class Native:
    def __init__(self,envfile,schemas):
        self.envfile=envfile;self.schemas=schemas;self.receipts=[];self.omissions=[]
    def read(self,tool,args):
        if tool not in METHODS or len(self.receipts)>=27:
            raise ValueError("W source selected public method/call count violates prereg")
        actual=self.schemas.get(tool)
        if not isinstance(actual,dict):
            self.omissions.append({"tool":tool,"args":args,"reason":"source_public_method_missing"})
            return None
        req=actual.get("required")
        if not isinstance(req,list) or set(req)!=set(args) or set(req)!=set(METHODS[tool]):
            self.omissions.append({"tool":tool,"args":args,"reason":"source_original_required_public_argument_schema_mismatch",
                                   "original_declared_required":req})
            return None
        command="".join(json.dumps(y,sort_keys=True)+"\n" for y in (
            {"action":"call","tool":tool,"arguments":args},{"action":"finish"}))
        out,wall=call_child(IMAGE,WORKER,self.envfile,input_text=command,timeout=90)
        if (len(out)!=3 or out[0].get("kind")!="ready" or
            out[0].get("verifier_present") is not False or
            out[1].get("kind")!="observation" or out[1].get("tool")!=tool or
            out[2].get("kind")!="private_final_state" or out[2].get("tool_calls")!=1):
            raise RuntimeError("restricted original public source worker IPC trust failure")
        raw=out[1].get("content")
        if not isinstance(raw,str) or len(raw)>8192:
            raise RuntimeError("original read-only tool public reply unbounded")
        parsed=unpack_reply(raw) if out[1].get("ok") is True and out[1].get("truncated") is False else None
        if parsed is not None and not isinstance(parsed,dict):
            raise RuntimeError("original public read response not a mapping")
        clean=redact(parsed) if parsed is not None else None
        representation=repr(clean) if clean is not None else None
        status="original_public_success" if isinstance(parsed,dict) and parsed.get("success") is True else "original_public_failed_or_unresolved"
        receipt={
          "tool":tool,"arguments":args,
          "original_declared_required_public_arguments":sorted(req),
          "original_raw_public_reply_sha256":hashlib.sha256(raw.encode()).hexdigest(),
          "redacted_original_public_reply":representation,
          "redacted_original_public_reply_sha256":fingerprint(representation) if representation is not None else None,
          "source_tool_status":status,
          "native_original_source_reply_truncated":out[1].get("truncated"),
          "physical_original_tool_seconds":out[1].get("elapsed_seconds"),
          "physical_original_restricted_worker_wall_seconds":wall,
          "native_worker_rss_kib":out[2].get("peak_rss_kib"),
          "source_private_terminal_state_discarded_without_inspection":True,
          "source_original_native_verifier_never_mounted":True,
        }
        # Original private terminal state is never parsed or written to artifact.
        out=None
        self.receipts.append(receipt)
        return clean.get("data") if status=="original_public_success" else None

def source_training_original():
    lock=json.loads(Path("governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json").read_text())
    if lock.get("sha256")!=SOURCE:raise ValueError("whole original source digest mismatch")
    rows=audit_source(lock)
    p=partition(rows,seed=4611)
    train={x["row_index"]:x for x in p["partitions"]["train"]}
    if ROW not in train or train[ROW]["environment_id_sha256"]!=FAMILY or train[ROW]["public_prompt_sha256"]!=PROMPT:
        raise ValueError("W original TRAIN source family or public prompt mismatch")
    obj=rows[ROW]
    public=public_view(obj)
    user_task="\n".join(x["content"] for x in public["messages"] if x["role"]=="user")
    for value in ("Dr. Luke Marquez","Dr. Ella Navarro","Dr. Sandy Torres",
        "Alice Chan","Jules Morgan","Ria Singh","Silas Huang",
        "Do not update aggregated rating unless and until the review is approved"):
        if value.casefold() not in user_task.casefold():
            raise ValueError("original public user moderation instruction not anchored")
    env=obj["extra_info"]["environment"]
    schemas={}
    for t in env["tools"]:
        fn=t.get("function",{}) if isinstance(t,dict) else {}
        if not isinstance(fn.get("name"),str) or not isinstance(fn.get("parameters"),dict):
            raise ValueError("original declared source public tools malformed")
        schemas[fn["name"]]=fn["parameters"]
    if not set(METHODS).issubset(schemas):
        raise ValueError("original source public professional/review interface unavailable")
    for key,required in METHODS.items():
        if set(schemas[key].get("required",[]))!=set(required):
            raise ValueError("original source public read method required args differ")
    private_env={k:env[k] for k in ("class_code","class_name","initial_state","tools")}
    return public,schemas,private_env

def run(spec_path):
    spec,byte_sha=check_spec(spec_path)
    public,schemas,environment=source_training_original()
    with tempfile.TemporaryDirectory(prefix="owi_ec005w_private_",dir=os.environ.get("RUNNER_TEMP") or None) as temp:
        envfile=Path(temp)/"environment.json"
        write_json(envfile,environment)  # 0444 for nonroot Docker bind input
        native=Native(envfile,schemas)
        first=[]
        for tool,args in FIRST:first.append(native.read(tool,args))
        professions=records(first[0]);users=records(first[1])
        # THIRD original public reply is an independent Ella source crosscheck;
        # it is NOT used to substitute a professional whose specialty does not match.
        ella=records(first[2])
        targets=[]
        pro_ids=[]
        for i,original in enumerate(TARGETS):
            name,specialty,author,before,action,aggregate=original
            pro=unique_by(professions,"name",name,extra_key="specialty",extra_val=specialty)
            user=unique_by(users,"username",author)
            pro_id=pro.get("professional_id") if isinstance(pro,dict) else None
            user_id=user.get("_id") if isinstance(user,dict) else None
            if (not isinstance(pro_id,str) or not isinstance(user_id,str)):
                state="original_source_public_professional_or_author_unique_identity_unresolved"
            else:state="exact_original_source_public_professional_and_author_unique_identity_confirmed"
            targets.append({"case_index":i,"professional":name,"specialty":specialty,
                            "review_author":author,"public_professional_id":pro_id,
                            "public_user_id":user_id,"public_author_account_status":user.get("account_status") if isinstance(user,dict) else None,
                            "task_before_review_status_expected":before,"task_action":action,
                            "task_aggregate_rule":aggregate,
                            "public_target_identity_status":state})
            if pro_id and pro_id not in pro_ids:pro_ids.append(pro_id)
        # Original public professional ID may be shared *name* with different
        # specialty; no professional ID is chosen without both exact labels.
        for pid in pro_ids:
            native.read("get_reviews_for_professional",{"professional_id":pid})
            native.read("get_aggregated_rating_for_professional",{"professional_id":pid})
        for target in targets:
            if not target["public_professional_id"] or not target["public_user_id"]:
                continue
            review=native.read("get_review_by_user_and_professional",{
                "user_id":target["public_user_id"],
                "professional_id":target["public_professional_id"]})
            if isinstance(review,dict):
                view_id=review.get("view_id")
                if isinstance(view_id,str):
                    native.read("get_review_moderation_status",{"view_id":view_id})
        report={
          "contract":CONTRACT,
          "original_frozen_public_protocol_file_sha256":byte_sha,
          "entire_original_corpus_sha256_verified":SOURCE,
          "original_train_row":ROW,"original_source_family_sha256":FAMILY,
          "original_public_user_task_sha256":PROMPT,
          "public_only_task_bundle_sha256":hashlib.sha256(canonical(public)).hexdigest(),
          "original_environment_class_code_sha256":hashlib.sha256(environment["class_code"].encode()).hexdigest(),
          "original_declared_source_required_public_schemas":{x:schemas[x]["required"] for x in METHODS},
          "native_original_selected_read_receipts":native.receipts,
          "native_public_tool_schema_unavailable":native.omissions,
          "selected_actual_original_public_target_identity_matches":targets,
          "source_public_professional_list_count":len(professions),
          "source_public_user_list_count":len(users),
          "source_public_ella_name_lookup_count":len(ella),
          "actual_source_physical_selected_read_call_count":len(native.receipts),
          "original_native_source_private_verifier_never_executed":True,
          "source_original_class_state_task_and_tools_unchanged":True,
          "source_private_terminal_not_exported_or_examined":True,
          "original_dev_sealed_test_task_contents_not_exposed":True,
          "source_public_credentials_redacted":True,
          "original_source_no_write_no_reward_no_policy_learning":True,
          "natural_original_review_pure_leave_unchanged_claim":"NOT_AUTHORIZED_BY_ORIGINAL_ROW710",
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
    print("OWI_EC005W_SOURCE_NATIVE_ORIGINAL_PUBLIC_REVIEW_READS",json.dumps({
       "original_train_row":ROW,
       "source_native_public_read_tool_calls":result["actual_source_physical_selected_read_call_count"],
       "status_counts":{k:sum(r["source_tool_status"]==k for r in result["native_original_selected_read_receipts"])
              for k in ("original_public_success","original_public_failed_or_unresolved")},
       "target_identity_cases":result["selected_actual_original_public_target_identity_matches"],
       "source_original_professional_count":result["source_public_professional_list_count"],
       "source_original_user_count":result["source_public_user_list_count"],
       "ella_public_name_lookup_count":result["source_public_ella_name_lookup_count"],
       "original_selected_tool_receipts":[{"tool":r["tool"],"args":r["arguments"],
           "status":r["source_tool_status"],
           "public_redacted_excerpt":(r["redacted_original_public_reply"] or "")[:750]}
            for r in result["native_original_selected_read_receipts"]],
       "unavailable":result["native_public_tool_schema_unavailable"],
       "pure_original_review_noop":"NOT_AUTHORIZED_BY_ORIGINAL_ROW710"
    },sort_keys=True))
if __name__=="__main__":main()
