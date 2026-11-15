#!/usr/bin/env python3
"""OWI-EC005S independent PUBLIC-only source-receipt replay gate.

Recompute each reported conditional category from actually selected source
public replies, rather than accepting a host-supplied action/gold label.
No source private initial/final state, class source, native private verifier,
unselected results or synthetic controlled state variants are admitted.
"""
from __future__ import annotations
import argparse,ast,collections,hashlib,json,math,re
from pathlib import Path
from owi_ec005s_native_public_support import (
    CONTRACT,SPEC,RAW_SOURCE,CANDIDATES,TAG_TARGETS,
    REVIEW_CLASSES,TAG_CLASSES,check_spec)
from owi_ec005_realtools_randomized import fingerprint

GATE="OWI-EC005S-INDEPENDENT-ORIGINAL-PUBLIC-NATURAL-SUPPORT-GATE/1"

def deny(why):
    raise ValueError(why)
def finite(x,low,high):
    return type(x) in (float,int) and math.isfinite(x) and low<=x<=high
def sha(x):
    return (isinstance(x,str) and len(x)==64 and
            all(t in "0123456789abcdef" for t in x))
def parse_public(s):
    try:v=ast.literal_eval(s)
    except (TypeError,SyntaxError,ValueError,RecursionError,MemoryError) as exc:
        raise ValueError("not an actual parseable source public tool reply") from exc
    if not isinstance(v,dict):
        deny("original public source reply is not a mapping")
    return v
def source_objects(v):
    if isinstance(v,list):return [x for x in v if isinstance(x,(dict,str))]
    if not isinstance(v,dict):return []
    for key in ("data","products","reviews","users","tags","items","results","records"):
        if key in v:return source_objects(v[key])
    if all(isinstance(x,dict) for x in v.values()):
        return list(v.values())
    return [v]

def list_public(receipt):
    obj=parse_public(receipt["raw_actual_original_public_reply"])
    if obj.get("success") is not True:
        deny("unsuccessful original-source public lookup cannot prove absence")
    return source_objects(obj.get("data",obj))

def public_item(receipt):
    obj=parse_public(receipt["raw_actual_original_public_reply"])
    if obj.get("success") is not True:
        deny("original-source public individual record lookup unsuccessful")
    val=obj.get("data",obj)
    if isinstance(val,dict):return val
    if isinstance(val,list) and len(val)==1 and isinstance(val[0],dict):
        return val[0]
    deny("invalid original-public object record; cannot infer status")

def classify(rating,standing,category,has_refill):
    if type(rating) not in (float,int) or not math.isfinite(rating):
        return "unresolved"
    if standing=="suspended" or rating in (1,2):
        return "reject"
    if standing=="active" and rating in (4,5):
        if isinstance(category,str) and category.casefold()=="home" and has_refill:
            return "edit_rating_and_leave_pending"
        return "approve"
    if standing in ("active","suspended","banned","inactive","closed"):
        return "leave_unchanged"
    return "unresolved"

def adjudicate(report,*,spec):
    digest=check_spec(spec)
    if (not isinstance(report,dict) or report.get("contract")!=CONTRACT or
        report.get("original_whole_source_sha256")!=RAW_SOURCE or
        report.get("frozen_native_public_support_spec_sha256")!=digest or
        report.get("original_selected_train_rows")!=list(CANDIDATES) or
        report.get("original_dev_and_sealed_test_source_tasks_not_exposed") is not True or
        report.get("third_party_source_exec_only_in_restricted_worker") is not True or
        report.get("native_original_source_state_unchanged") is not True or
        report.get("source_original_private_verifier_not_executed") is not True or
        report.get("no_learned_policy_or_reward_claim") is not True):
        deny("original source public-only privacy/partition/protocol provenance drift")
    family=report.get("original_source_classes_and_public_task_identity")
    if (not isinstance(family,dict) or set(family)!={"2151","2001"} or
        any(set(x)!={"original_source_public_task_sha256",
                     "original_source_executable_class_sha256"}
            for x in family.values()) or
        any(not all(sha(v) for v in x.values()) for x in family.values()) or
        family["2151"]["original_source_executable_class_sha256"]==
        family["2001"]["original_source_executable_class_sha256"]):
        deny("distinct original executable TRAIN family identities invalid")
    # The source class and row 2151 public prompt were independently recorded
    # by the preexisting EC005J source-native candidate audit.
    if family["2151"]["original_source_executable_class_sha256"]!=(
        "75e5e199e65aaf2dbf374805c6eb735569b727a2796fb1fd6f8e20098650af7c"):
        deny("original native product-review source class changed")
    if family["2151"]["original_source_public_task_sha256"]!=(
        "5d8bae31755d162f274a0170043e8bed595e7e0217f4fa43f84f6dbcc19e2629"):
        deny("original native product-review user task changed")
    receipts=report.get("actual_source_public_tool_receipts")
    if (not isinstance(receipts,list) or
        len(receipts)!=report.get("actual_physical_read_only_source_tool_call_count") or
        not 2<=len(receipts)<=40):
        deny("actual physical original source read-only call count absent")
    allowed={2151:{"list_all_products","get_reviews_for_product_by_status",
                    "get_user_by_id"},2001:{"list_tags"}}
    for rec in receipts:
        if (not isinstance(rec,dict) or
            rec.get("original_source_row") not in (2151,2001) or
            rec.get("selected_read_only_tool") not in allowed[rec["original_source_row"]] or
            not isinstance(rec.get("selected_original_public_args"),dict) or
            not isinstance(rec.get("raw_actual_original_public_reply"),str) or
            len(rec["raw_actual_original_public_reply"])>8192 or
            rec.get("actual_public_reply_sha256")!=fingerprint(
                rec["raw_actual_original_public_reply"]) or
            rec.get("original_private_terminal_state_discarded") is not True or
            rec.get("original_native_verifier_never_executed") is not True or
            not finite(rec.get("source_public_tool_seconds"),0,40) or
            not finite(rec.get("source_worker_container_wall_seconds"),0,90) or
            not finite(rec.get("source_worker_peak_rss_kib"),1000,1000000)):
            deny("source physical original public tool receipt illegal, leaked or forged")
    p=0
    def next_receipt(row,tool,arguments):
        nonlocal p
        if p>=len(receipts):deny("original source selected public call missing")
        x=receipts[p];p+=1
        if (x["original_source_row"]!=row or
            x["selected_read_only_tool"]!=tool or
            x["selected_original_public_args"]!=arguments):
            deny("original source actual selected tool order/arguments substituted")
        return x
    products=list_public(next_receipt(2151,"list_all_products",{}))
    expected=[]
    user_lookup={}
    product_ids=[]
    for product in products[:10]:
        if not isinstance(product,dict):continue
        pid,cat=product.get("product_id"),product.get("category")
        if not isinstance(pid,str) or not isinstance(cat,str):continue
        if pid in product_ids:continue
        product_ids.append(pid)
        reviews=list_public(next_receipt(2151,"get_reviews_for_product_by_status",
                        {"product_id":pid,"moderation_status":"pending"}))
        for rev in reviews[:12]:
            if not isinstance(rev,dict):continue
            rid,author=rev.get("review_id"),rev.get("user_id")
            rating,body=rev.get("rating"),rev.get("review_text","")
            if (not isinstance(rid,str) or not isinstance(author,str) or
                rev.get("moderation_status")!="pending" or
                not isinstance(body,str) or rev.get("product_id") not in (None,pid)):
                deny("original native pending review record invalid")
            if author not in user_lookup and len(user_lookup)<20:
                account=public_item(next_receipt(2151,"get_user_by_id",
                                                 {"user_id":author}))
                if account.get("user_id") not in (None,author):
                    deny("source-public reviewer identity missing")
                user_lookup[author]=account.get("account_status")
            if author not in user_lookup:continue
            status=user_lookup[author]
            refill=bool(re.search(r"refills?",body,re.IGNORECASE))
            expected.append({
                "source_product_id":pid,"original_source_review_id":rid,
                "author_source_user_id":author,"public_rating":rating,
                "public_account_status":status,"public_product_category":cat,
                "public_review_text_contains_refill":refill,
                "original_public_task_action_class":classify(rating,status,cat,refill)})
    observed_reviews=report.get("original_public_moderation",{})
    if (observed_reviews.get("candidate_row")!=2151 or
        observed_reviews.get("selected_products_checked")!=product_ids or
        observed_reviews.get("public_reviews_classified")!=expected or
        observed_reviews.get("source_pending_review_count")!=len(expected) or
        observed_reviews.get("natural_review_class_counts")!=dict(collections.Counter(
            x["original_public_task_action_class"] for x in expected))):
        deny("native review source public action/abstention classes not independently reconstructible")
    tags=list_public(next_receipt(2001,"list_tags",{}))
    found=set()
    for item in tags:
        if isinstance(item,str):found.add(item.casefold().strip())
        elif isinstance(item,dict):
            name=item.get("name",item.get("tag_name"))
            if isinstance(name,str):found.add(name.casefold().strip())
    expect_tags=[{
       "tag_target_from_original_public_prompt":name,
       "public_existing_tag_record_found":name.casefold() in found,
       "original_public_task_action_class":(
           "tag_already_exists_no_create" if name.casefold() in found else
           "tag_missing_create_candidate")} for name in TAG_TARGETS]
    observed_tags=report.get("original_public_create_if_missing",{})
    if (observed_tags.get("candidate_row")!=2001 or
        observed_tags.get("original_public_tag_rows_visible")!=len(tags) or
        observed_tags.get("selected_public_tag_classifications")!=expect_tags or
        observed_tags.get("natural_tag_class_counts")!=dict(collections.Counter(
            x["original_public_task_action_class"] for x in expect_tags))):
        deny("native bookmark create-if-missing source-public status forged")
    if p!=len(receipts):
        deny("unaccounted actual original source public tool calls appended")
    review_counts=collections.Counter(x["original_public_task_action_class"] for x in expected)
    tag_counts=collections.Counter(x["original_public_task_action_class"] for x in expect_tags)
    review_support=all(review_counts[c] for c in ("approve","reject","leave_unchanged"))
    tag_support=all(tag_counts[c] for c in ("tag_already_exists_no_create",
                                          "tag_missing_create_candidate"))
    return {
        "contract":GATE,"original_whole_source_sha256":RAW_SOURCE,
        "preregistered_public_only_spec_sha256":digest,
        "source_original_executable_train_families":[2151,2001],
        "distinct_source_executable_class_sha256":{
            k:v["original_source_executable_class_sha256"] for k,v in family.items()},
        "original_source_public_selected_tool_calls_verified":len(receipts),
        "native_original_pending_reviews_observed":len(expected),
        "native_public_original_review_policy_action_counts":dict(review_counts),
        "original_source_moderation_policy_all_three_required_classes_observed":bool(review_support),
        "native_public_tag_targets_checked":len(expect_tags),
        "native_public_tag_exists_and_missing_counts":dict(tag_counts),
        "native_create_if_missing_original_both_classes_observed":bool(tag_support),
        "qualifying_natural_mixed_observation_cohort_found":bool(review_support or tag_support),
        "original_dev_test_task_content_or_source_private_verifier_not_exported":True,
        "no_source_mutation_or_synthetic_masking":True,
        "no_learned_policy_or_private_terminal_reward_evidence":True,
        "future_independent_family_holdout_not_yet_precommitted":True,
        "scientific_disposition":(
            "ORIGINAL_SOURCE_PUBLIC_NATURAL_MIXED_OBSERVATION_CANDIDATES_FOUND"
            if review_support or tag_support else
            "BOUNDED_TWO_FAMILY_NATIVE_SOURCE_SUPPORT_COHORT_NOT_QUALIFIED"),
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--trial",type=Path,required=True)
    p.add_argument("--task-spec",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    result=adjudicate(json.loads(a.trial.read_text()),spec=a.task_spec)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("OWI_EC005S_INDEPENDENT_NATIVE_PUBLIC_SUPPORT",
          json.dumps(result,sort_keys=True))
if __name__=="__main__":
    main()
