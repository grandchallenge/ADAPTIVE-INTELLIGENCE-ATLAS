#!/usr/bin/env python3
"""Independent original TRAIN row710 real source-public review-status/aggregate gate.

Does not import the source runner or the original source class/checker. Replays
every actual PUBLIC selected method, preserves original exact professional
name+specialty (Ella has two named roles), checks actual user/review/status
identities and distinguishes task-authorized aggregate write suppression from
nonexistent pure leave-review-unchanged branch. Source-public text != state.
"""
from __future__ import annotations
import argparse,ast,collections,hashlib,json,math,re
from pathlib import Path

CONTRACT="OWI-EC005W-INDEPENDENT-ORIGINAL-REVIEW-SOURCE-PUBLIC-STATUS-AGGREGATE-GATE/1"
RUN="OWI-EC005W-ORIGINAL-TRAIN-REVIEW-SELECTED-NATIVE-PUBLIC-READS/1"
SPEC="OWI-EC005W-ORIGINAL-TRAIN-REVIEW-TARGET-STATUS-PUBLIC-AUDIT/1"
SOURCE="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
FAMILY="a739046b13061603e09af000ceed469840dfecba0068db2e1919454b18394b0c"
PROMPT="97bca760aa53e15f281b71771a6b63a1ba294c1ce3123f9632b114cbf12d6d36"
TARGETS=[
 ("Dr. Luke Marquez","Dermatology","Alice Chan","pending","approve","update_after_approval"),
 ("Dr. Ella Navarro","Internal Medicine","Jules Morgan","pending","reject","no_aggregate_contribution_from_rejected"),
 ("Dr. Ella Navarro","Cardiology","Ria Singh","approved","delete","update_after_approved_review_deletion"),
 ("Dr. Sandy Torres","Pediatrics","Silas Huang","rejected","edit_then_set_pending","do_not_update_until_approved"),
]
FIRST=[("list_all_professionals",{}),("list_all_users",{}),
       ("get_professional_by_name",{"name":"Dr. Ella Navarro"})]
METHODS={
 "list_all_professionals":[],
 "list_all_users":[],
 "get_professional_by_name":["name"],
 "get_reviews_for_professional":["professional_id"],
 "get_aggregated_rating_for_professional":["professional_id"],
 "get_review_by_user_and_professional":["user_id","professional_id"],
 "get_review_moderation_status":["view_id"],
}
BANNED=("password","secret","token","credential","private_key","api_key","auth_header",
        "authentication","oauth","client_secret","authorization","ssn")
def deny(message):raise ValueError(message)
def sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
                                   ensure_ascii=False).encode()).hexdigest()
def is_hash(value):
    return isinstance(value,str) and len(value)==64 and all(x in "0123456789abcdef" for x in value)
def metric(x,lo,hi):
    return type(x) in (float,int) and math.isfinite(x) and lo<=x<=hi
def check_spec(path):
    raw=path.read_bytes();obj=json.loads(raw)
    so=obj.get("source",{});pl=obj.get("prospective_selected_original_public_reads",{})
    auth=obj.get("original_task_authority",{});science=obj.get("independent_science",{})
    if (obj.get("contract")!=SPEC or so.get("full_raw_sha256")!=SOURCE or
        so.get("original_train_row")!=710 or so.get("group_seed")!=4611 or
        so.get("train_group_sha256")!=FAMILY or
        so.get("original_public_user_prompt_sha256")!=PROMPT or
        so.get("original_class_state_and_schemas_unchanged") is not True or
        so.get("original_verifier_never_executed") is not True or
        so.get("no_dev_or_sealed_test_task_exposure") is not True or
        pl.get("first_fixed_calls")!=[[x,y] for x,y in FIRST] or
        pl.get("exact_original_required_tool_arguments")!=METHODS or
        pl.get("max_original_native_selected_public_read_calls")!=27 or
        pl.get("no_intervention_no_source_write") is not True or
        pl.get("discard_source_private_terminal_state_unexamined") is not True or
        auth.get("every_one_of_four_named_reviews_requires_mutation") is not True or
        auth.get("pure_leave_named_review_unchanged_action_authorized") is not False or
        auth.get("matching_by_only_shared_professional_name_without_specialty_is_forbidden") is not True or
        science.get("cross_target_aggregate_update_skip_not_proof_of_same_instance_variable_initial_state") is not True or
        science.get("pure_review_noop_not_authorized_by_original_row710") is not False or
        [tuple((q.get("professional"),q.get("specialty"),q.get("review_author"),
                q.get("source_expected_review_before"),q.get("requested_action"),q.get("aggregate_after")))
         for q in obj.get("source_original_named_targets",[])]!=TARGETS):
        deny("independent protected original review task/branch scope changed")
    return hashlib.sha256(raw).hexdigest()

def rows(data):
    if isinstance(data,list):return [x for x in data if isinstance(x,dict)]
    if isinstance(data,dict):
        for key in ("data","users","professionals","reviews","results","items"):
            if key in data:return rows(data[key])
        return [data]
    return []
def exact(items,name,key,extra=None,specialty=None):
    matching=[x for x in items if isinstance(x.get(key),str) and
        x[key].casefold()==name.casefold() and
        (extra is None or (isinstance(x.get(extra),str) and x[extra].casefold()==specialty.casefold()))]
    return matching[0] if len(matching)==1 else None
def review_before(review):
    if not isinstance(review,dict):return None
    for key in ("moderation_status","status","review_status"):
        if isinstance(review.get(key),str):
            return review[key]
    return None

class SourceGate:
    def __init__(self,report):
        original=report.get("native_original_selected_read_receipts")
        schemas=report.get("original_declared_source_required_public_schemas")
        if (not isinstance(original,list) or not 3<=len(original)<=27 or
            len(original)!=report.get("actual_source_physical_selected_read_call_count") or
            not isinstance(schemas,dict) or set(schemas)!=set(METHODS) or
            any(not isinstance(schemas[x],list) or set(schemas[x])!=set(METHODS[x]) for x in METHODS)):
            deny("source-native original read count or declared PUBLIC method schemas changed")
        if report.get("native_public_tool_schema_unavailable")!=[]:
            deny("original required read method unavailable; no guessed status allowed")
        self.calls=[]
        for r in original:
            name=r.get("tool");args=r.get("arguments")
            if (name not in METHODS or not isinstance(args,dict) or
                set(args)!=set(METHODS[name]) or
                r.get("original_declared_required_public_arguments")!=sorted(METHODS[name])):
                deny("illegal/forged selected original review method or required args")
            payload=r.get("redacted_original_public_reply")
            if payload is not None:
                if (not isinstance(payload,str) or len(payload)>8192 or
                    any(re.search(r"(?i)['\"]?"+x+r"[a-z_]*['\"]?\s*:",payload) for x in BANNED) or
                    re.search(r"(?i)(?:oauth[_ -]?token|bearer\s+\S+|sk-[a-z0-9])",payload)):
                    deny("original public source projection malformed or leaks auth")
            if (not is_hash(r.get("original_raw_public_reply_sha256")) or
                (sha(payload) if payload is not None else None)!=r.get("redacted_original_public_reply_sha256") or
                r.get("source_private_terminal_state_discarded_without_inspection") is not True or
                r.get("source_original_native_verifier_never_mounted") is not True or
                r.get("native_original_source_reply_truncated") is not False or
                not metric(r.get("physical_original_tool_seconds"),0,60) or
                not metric(r.get("physical_original_restricted_worker_wall_seconds"),0,90) or
                not metric(r.get("native_worker_rss_kib"),1000,1000000)):
                deny("real original source physical public receipt custody or private trust failure")
            parsed=None
            if payload is not None:
                try:parsed=ast.literal_eval(payload)
                except (ValueError,SyntaxError,RecursionError,MemoryError,TypeError) as exc:
                    raise ValueError("source public review reply cannot be safely parsed") from exc
                if not isinstance(parsed,dict) or type(parsed.get("success")) is not bool:
                    deny("source public original reply must contain real success bool")
            status=("original_public_success" if parsed is not None and parsed["success"] is True
                    else "original_public_failed_or_unresolved")
            if r.get("source_tool_status")!=status:
                deny("fake source public success/failed status")
            self.calls.append((name,args,parsed))
        self.cursor=0
    def take(self,name,args):
        if self.cursor>=len(self.calls):deny("missing selected actual original source tool reply")
        n,a,out=self.calls[self.cursor]
        if n!=name or a!=args:deny("selected original source public tool/args/order mismatch")
        self.cursor+=1
        return out.get("data") if isinstance(out,dict) and out.get("success") is True else None
    def done(self):
        if self.cursor!=len(self.calls):deny("unaccounted extra original source tool readings")

def adjudicate(report,*,spec_path):
    digest=check_spec(spec_path)
    if (not isinstance(report,dict) or report.get("contract")!=RUN or
        report.get("original_frozen_public_protocol_file_sha256")!=digest or
        report.get("entire_original_corpus_sha256_verified")!=SOURCE or
        report.get("original_train_row")!=710 or
        report.get("original_source_family_sha256")!=FAMILY or
        report.get("original_public_user_task_sha256")!=PROMPT or
        not is_hash(report.get("public_only_task_bundle_sha256")) or
        not is_hash(report.get("original_environment_class_code_sha256")) or
        report.get("original_native_source_private_verifier_never_executed") is not True or
        report.get("source_original_class_state_task_and_tools_unchanged") is not True or
        report.get("source_private_terminal_not_exported_or_examined") is not True or
        report.get("original_dev_sealed_test_task_contents_not_exposed") is not True or
        report.get("source_public_credentials_redacted") is not True or
        report.get("original_source_no_write_no_reward_no_policy_learning") is not True or
        report.get("natural_original_review_pure_leave_unchanged_claim")!="NOT_AUTHORIZED_BY_ORIGINAL_ROW710"):
        deny("original source family/task, read-only or no-false-review-noop state contradicted")
    gate=SourceGate(report)
    initial=[gate.take(*method) for method in FIRST]
    professionals=rows(initial[0]);users=rows(initial[1]);ella_public=rows(initial[2])
    if (len(professionals)!=report.get("source_public_professional_list_count") or
        len(users)!=report.get("source_public_user_list_count") or
        len(ella_public)!=report.get("source_public_ella_name_lookup_count")):
        deny("actual original source first public lists don't match source receipt count")
    all_targets=[]
    prof_ids=[]
    for index,(name,specialty,author,before,action,aggregate) in enumerate(TARGETS):
        professional=exact(professionals,name,"name",extra="specialty",specialty=specialty)
        user=exact(users,author,"username")
        prof_id=professional.get("professional_id") if isinstance(professional,dict) else None
        user_id=user.get("_id") if isinstance(user,dict) else None
        match=(isinstance(prof_id,str) and isinstance(user_id,str))
        own=report["selected_actual_original_public_target_identity_matches"][index]
        if (own.get("professional")!=name or own.get("specialty")!=specialty or
            own.get("review_author")!=author or own.get("public_professional_id")!=prof_id or
            own.get("public_user_id")!=user_id or
            own.get("task_action")!=action or own.get("task_before_review_status_expected")!=before or
            own.get("task_aggregate_rule")!=aggregate or
            own.get("public_author_account_status")!=(user.get("account_status") if isinstance(user,dict) else None) or
            own.get("public_target_identity_status")!=(
                "exact_original_source_public_professional_and_author_unique_identity_confirmed"
                if match else "original_source_public_professional_or_author_unique_identity_unresolved")):
            deny("original task named exact specialty/author PUBLIC identity changed, possibly confused Ella")
        all_targets.append({
            "task_case":index,"original_task_professional":name,
            "original_task_specialty":specialty,
            "original_task_review_author":author,
            "original_task_expected_review_status":before,
            "original_task_requested_review_mutation":action,
            "original_task_aggregate_instruction":aggregate,
            "actually_public_unique_professional_and_author_identified":bool(match),
            "original_public_professional_id":prof_id,
            "original_public_author_id":user_id,
            "original_public_author_account_status":user.get("account_status") if isinstance(user,dict) else None,
            "actual_review_public_status":None,
            "actual_review_public_unique_id":None,
            "source_selected_review_current_state_matches_task_preconditions":False,
            "actually_public_original_review_linkage_verified":False,
            "source_task_authorized_review_leave_unchanged":False,
        })
        if isinstance(prof_id,str) and prof_id not in prof_ids:prof_ids.append(prof_id)
    if not isinstance(report.get("selected_actual_original_public_target_identity_matches"),list) or len(
            report["selected_actual_original_public_target_identity_matches"])!=4:
        deny("original source 4 target receipt count changed")
    summaries={}
    for pid in prof_ids:
        rr=gate.take("get_reviews_for_professional",{"professional_id":pid})
        avg=gate.take("get_aggregated_rating_for_professional",{"professional_id":pid})
        summaries[pid]={"public_review_count":len(rows(rr)),
                        "current_original_public_aggregate":avg}
    for index,target in enumerate(all_targets):
        pid=target["original_public_professional_id"];uid=target["original_public_author_id"]
        if not isinstance(pid,str) or not isinstance(uid,str):continue
        review=gate.take("get_review_by_user_and_professional",{
            "user_id":uid,"professional_id":pid})
        if isinstance(review,dict):
            actual_id=review.get("view_id")
            if isinstance(actual_id,str):
                # Trust actual source returned review ID, not guessed private ID.
                source_status=gate.take("get_review_moderation_status",{"view_id":actual_id})
                if not isinstance(source_status,str) or source_status not in (
                    "pending","approved","rejected"):
                    source_status=None
            else:source_status=None
            direct_status=review_before(review)
            if (isinstance(direct_status,str) and
                isinstance(source_status,str) and direct_status!=source_status):
                deny("two original public tool replies disagree on same review status")
            current_status=source_status or direct_status
            target["actual_review_public_status"]=current_status
            target["actual_review_public_unique_id"]=actual_id if isinstance(actual_id,str) else None
            same_user=review.get("user_id") in (uid,None)
            same_pro=review.get("professional_id") in (pid,None)
            target["actually_public_original_review_linkage_verified"]=(
                same_user and same_pro and (isinstance(actual_id,str) or
                isinstance(current_status,str)))
            target["source_selected_review_current_state_matches_task_preconditions"]=(
                target["actually_public_original_review_linkage_verified"] and
                current_status==target["original_task_expected_review_status"])
    gate.done()
    verified=[x for x in all_targets if x["source_selected_review_current_state_matches_task_preconditions"]]
    verified_aggregate_update=[x["task_case"] for x in verified if
         x["original_task_aggregate_instruction"] in (
          "update_after_approval","update_after_approved_review_deletion")]
    verified_aggregate_no_update=[x["task_case"] for x in verified if
         x["original_task_aggregate_instruction"]=="do_not_update_until_approved" and
         x["actual_review_public_status"]=="rejected"]
    # Original task's aggregate decisions for named actions differ; this
    # does NOT imply same initial-state conditional across identical targets.
    cross_action_aggregate_contrast=bool(verified_aggregate_update and verified_aggregate_no_update)
    return {
      "contract":CONTRACT,
      "source_full_original_pinned_sha256":SOURCE,
      "frozen_original_public_w_protocol_sha256":digest,
      "original_source_connected_train_family_sha256":FAMILY,
      "original_native_physically_selected_public_calls_independently_replayed":gate.cursor,
      "original_source_native_public_read_status_counts":dict(collections.Counter(
           x["source_tool_status"] for x in report["native_original_selected_read_receipts"])),
      "original_four_requested_named_moderation_targets":all_targets,
      "public_professional_review_and_aggregate_inventory":summaries,
      "actual_source_exact_linked_review_preconditions_confirmed":len(verified),
      "source_actual_task_cases_with_approved_set_aggregate_update_instruction":verified_aggregate_update,
      "source_actual_task_cases_with_explicit_pending_aggregate_no_update":verified_aggregate_no_update,
      "cross_action_original_source_aggregate_update_versus_no_update_directive_observed":cross_action_aggregate_contrast,
      "original_task_authorized_pure_review_noop_targets":0,
      "actual_source_natural_same_review_rule_action_and_pure_noop_pair_proved":False,
      "single_same_review_decision_naturally_variable_original_source_state_proved":False,
      "no_original_native_reward_or_learned_reflection_ever_evaluated":True,
      "original_private_checker_never_used":True,
      "original_dev_and_sealed_test_task_content_unseen":True,
      "scientific_disposition":("ORIGINAL_TARGETED_AGGREGATE_WRITE_SUPPRESSION_PUBLIC_CONTRAST_OBSERVED__PURE_REVIEW_NOOP_NOT_AUTHORIZED"
             if cross_action_aggregate_contrast else
             "ORIGINAL_REVIEW_CURRENT_STATE_SOURCE_PUBLIC_AUDIT__NO_QUALIFIED_PURE_REVIEW_NOOP"),
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--trial",type=Path,required=True)
    ap.add_argument("--task-spec",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    g=adjudicate(json.loads(a.trial.read_text()),spec_path=a.task_spec)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(g,sort_keys=True,indent=2)+"\n")
    print("OWI_EC005W_INDEPENDENT_ORIGINAL_SOURCE_MODERATION_GATE",json.dumps(g,sort_keys=True))
if __name__=="__main__":main()
