#!/usr/bin/env python3
"""OWI-EC005S public-only native observation-support discovery.

Only ORIGINAL TRAIN tasks 2151 (product-review moderation) and 2001 (tag
create-if-missing), in different original executable source environments.
No modified prompt, masked state, checker access, actor fitting or mutation.
All source third-party code executes only in restricted docker, never in host.
The original private final source state is discarded without parsing.

The actual source replies, not the private source implementation, decide
whether the original public task has BOTH action and abstention candidates.
"""
from __future__ import annotations
import argparse,hashlib,json,math,re
from collections import Counter
from pathlib import Path
from owi_ec005_realtools_goal_policy import WORKER,unpack_reply
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint
from owi_ec005_realtools_intake import canonical

CONTRACT="OWI-EC005S-ACTUAL-ORIGINAL-SOURCE-PUBLIC-SUPPORT/1"
SPEC="OWI-EC005S-ORIGINAL-PUBLIC-NATIVE-OBSERVATION-SUPPORT-V1"
RAW_SOURCE="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
CANDIDATES=(2151,2001)
READ_TOOLS={
 2151:{"list_all_products","get_reviews_for_product_by_status","get_user_by_id"},
 2001:{"list_tags"},
}
TAG_TARGETS=("tcm","herbal","acupuncture","evidence-based","safety")
REVIEW_CLASSES=("approve","reject","edit_rating_and_leave_pending","leave_unchanged")
TAG_CLASSES=("tag_already_exists_no_create","tag_missing_create_candidate")

def check_spec(spec:Path):
    raw=spec.read_bytes()
    m=json.loads(raw)
    if (m.get("contract")!=SPEC or
        m.get("source",{}).get("full_raw_sha256")!=RAW_SOURCE or
        m.get("source",{}).get("seed")!=4611 or
        m.get("source",{}).get("partition")!="train_only" or
        m.get("source",{}).get("candidates")!=list(CANDIDATES) or
        m.get("sampling",{}).get("max_total_calls")!=40 or
        m.get("sampling",{}).get("max_products")!=10 or
        m.get("sampling",{}).get("max_pending_reviews_per_product")!=12 or
        m.get("sampling",{}).get("max_distinct_author_lookups")!=20 or
        m.get("sampling",{}).get("source_original_state_unchanged") is not True or
        m.get("sampling",{}).get("original_verifier_never_mounted_or_executed") is not True or
        m.get("sampling",{}).get("all_selected_public_calls_read_only") is not True or
        m.get("interpretation",{}).get("positive_mixed_support_does_not_establish_native_reward_advantage") is not True):
        raise ValueError("source public native S preregistration or leak boundary changed")
    return hashlib.sha256(raw).hexdigest()

def public_bundle(folder,row):
    public=json.loads((folder/"public.json").read_text())
    if not isinstance(public,dict) or set(public)!={"messages","tools"}:
        raise ValueError("public task contaminated by original source-private data")
    task="\n".join(m["content"] for m in public["messages"] if m.get("role")=="user")
    if row==2151:
        phrases=["all pending reviews across all products","Home category",
                 "refill","Leave all other pending reviews unchanged",
                 "account_status is suspended"]
    else:
        phrases=["if they do not already exist","tcm","herbal","acupuncture",
                 "evidence-based","safety"]
    if not all(p.casefold() in task.casefold() for p in phrases):
        raise ValueError("original source native public conditional task drift")
    allowed={}
    for x in public["tools"]:
        if not isinstance(x,dict) or not isinstance(x.get("name"),str):
            raise ValueError("invalid original declared source public tool")
        allowed[x["name"]]=x["parameters"]
    for name in READ_TOOLS[row]:
        if name not in allowed or not isinstance(allowed[name],dict):
            raise ValueError("original source public read-only tool absent")
    return public,allowed

def rows_from_public(reply):
    """Read source-public response only; no private source-state heuristics."""
    if isinstance(reply,list):
        return [x for x in reply if isinstance(x,(dict,str))]
    if not isinstance(reply,dict):
        return []
    for key in ("data","products","reviews","users","tags","items","results","records"):
        if key in reply:
            return rows_from_public(reply[key])
    if all(isinstance(v,dict) for v in reply.values()):
        return list(reply.values())
    return [reply]

def primary_record(reply):
    if not isinstance(reply,dict):
        return None
    v=reply.get("data",reply)
    if isinstance(v,dict):
        return v
    if isinstance(v,list) and len(v)==1 and isinstance(v[0],dict):
        return v[0]
    return None

def categorize_review(rating,status,category,refill):
    """Original row-2151 PUBLIC user policy, not a learned label or checker."""
    if type(rating) not in (int,float) or not math.isfinite(rating):
        return "unresolved"
    if status=="suspended" or rating in (1,2):
        return "reject"
    if status=="active" and rating in (4,5):
        if category.casefold()=="home" and refill:
            return "edit_rating_and_leave_pending"
        return "approve"
    if status in ("active","suspended","banned","inactive","closed"):
        return "leave_unchanged"
    return "unresolved"

def probe_once(folder,row,name,args,allowed):
    if name not in READ_TOOLS[row]:
        raise ValueError("write or nonwhitelisted source operation cannot be selected")
    schema=allowed.get(name)
    if not isinstance(schema,dict) or set(args)!=set(schema.get("required",[])):
        raise ValueError("public tool argument schema mismatch, no guessed source params")
    script="".join(json.dumps(c,sort_keys=True)+"\n" for c in (
        {"action":"call","tool":name,"arguments":args},{"action":"finish"}))
    results,wall=call_child(IMAGE,WORKER,folder/"environment.json",
                            input_text=script,timeout=90)
    if (len(results)!=3 or results[0].get("kind")!="ready" or
        results[0].get("verifier_present") is not False or
        results[1].get("kind")!="observation" or
        results[1].get("tool")!=name or
        results[1].get("ok") is not True or
        results[1].get("truncated") is not False or
        results[-1].get("kind")!="private_final_state" or
        results[-1].get("tool_calls")!=1):
        raise RuntimeError("original source selected public-only reply protocol failed")
    source_reply=results[1].get("content")
    if not isinstance(source_reply,str) or len(source_reply)>8192:
        raise RuntimeError("truncated or malformed original source public reply")
    # Terminal private initial/final state are deliberately not inspected.
    peak=results[-1].get("peak_rss_kib")
    results=None
    return {
        "original_source_row":row,"selected_read_only_tool":name,
        "selected_original_public_args":args,
        "raw_actual_original_public_reply":source_reply,
        "actual_public_reply_sha256":fingerprint(source_reply),
        "source_public_tool_seconds":float(results_time) if False else 0.0,
        "source_worker_container_wall_seconds":wall,
        "source_worker_peak_rss_kib":peak,
        "original_private_terminal_state_discarded":True,
        "original_native_verifier_never_executed":True,
    }

def extract_list(receipt):
    reply=unpack_reply(receipt["raw_actual_original_public_reply"])
    if reply.get("success") is not True:
        return []
    return rows_from_public(reply.get("data",reply))

def source_product_review_probe(folder,allowed,call,max_calls=40):
    inv=call(2151,"list_all_products",{})
    products=extract_list(inv)
    out=[]
    users={}
    seen_products=[]
    for product in products[:10]:
        if not isinstance(product,dict):
            continue
        pid=product.get("product_id")
        category=product.get("category")
        if not isinstance(pid,str) or not isinstance(category,str):
            continue
        if pid in seen_products:continue
        seen_products.append(pid)
        reviews=extract_list(call(2151,"get_reviews_for_product_by_status",{
            "product_id":pid,"moderation_status":"pending"}))
        for item in reviews[:12]:
            if not isinstance(item,dict):continue
            review_id=item.get("review_id")
            author=item.get("user_id")
            rating=item.get("rating")
            text=item.get("review_text","")
            mod=item.get("moderation_status")
            if (not isinstance(review_id,str) or not isinstance(author,str) or
                mod!="pending" or not isinstance(text,str) or
                (item.get("product_id") not in (None,pid))):
                raise ValueError("unrecognized pending original public review record")
            if author not in users and len(users)<20:
                rec=primary_record(unpack_reply(call(2151,"get_user_by_id",{
                    "user_id":author})["raw_actual_original_public_reply"]))
                if not isinstance(rec,dict):
                    raise ValueError("original source public reviewer not found")
                if rec.get("user_id") not in (None,author):
                    raise ValueError("original public reviewer identity disagreement")
                users[author]=rec.get("account_status")
            if author not in users:continue
            standing=users[author]
            refill=bool(re.search(r"refills?",text,re.IGNORECASE))
            outcome=categorize_review(rating,standing,category,refill)
            out.append({"source_product_id":pid,"original_source_review_id":review_id,
                        "author_source_user_id":author,"public_rating":rating,
                        "public_account_status":standing,
                        "public_product_category":category,
                        "public_review_text_contains_refill":refill,
                        "original_public_task_action_class":outcome})
    return {"candidate_row":2151,"selected_products_checked":seen_products,
            "public_reviews_classified":out,
            "natural_review_class_counts":dict(Counter(
                r["original_public_task_action_class"] for r in out)),
            "source_pending_review_count":len(out)}

def source_tag_probe(folder,allowed,call):
    receipt=call(2001,"list_tags",{})
    rows=extract_list(receipt)
    tags=set()
    for rec in rows:
        if isinstance(rec,str):tags.add(rec.casefold().strip())
        elif isinstance(rec,dict):
            name=rec.get("name",rec.get("tag_name"))
            if isinstance(name,str):tags.add(name.casefold().strip())
    result=[{"tag_target_from_original_public_prompt":name,
             "public_existing_tag_record_found":name.casefold() in tags,
             "original_public_task_action_class":(
                "tag_already_exists_no_create" if name.casefold() in tags else
                "tag_missing_create_candidate")} for name in TAG_TARGETS]
    return {"candidate_row":2001,"original_public_tag_rows_visible":len(rows),
            "selected_public_tag_classifications":result,
            "natural_tag_class_counts":dict(Counter(
                x["original_public_task_action_class"] for x in result))}

def run(base,spec):
    task_sha=check_spec(spec)
    original={}
    allowed={}
    identities={}
    for row in CANDIDATES:
        folder=base/str(row)
        original[row],allowed[row]=public_bundle(folder,row)
        env=json.loads((folder/"environment.json").read_text())
        code=env.get("class_code")
        if not isinstance(code,str):
            raise ValueError("source class identity unavailable to privileged audit")
        identities[str(row)]={
            "original_source_public_task_sha256":hashlib.sha256(canonical(original[row])).hexdigest(),
            "original_source_executable_class_sha256":hashlib.sha256(code.encode()).hexdigest()}
        del env,code
    if len({x["original_source_executable_class_sha256"]
             for x in identities.values()})!=len(CANDIDATES):
        raise ValueError("original source independent classes not established")
    receipts=[]
    def call(row,name,args):
        if len(receipts)>=40:
            raise RuntimeError("source native read-only selected public call budget exhausted")
        r=probe_once(base/str(row),row,name,args,allowed[row])
        receipts.append(r)
        return r
    review=source_product_review_probe(base/str(2151),allowed[2151],call)
    tag=source_tag_probe(base/str(2001),allowed[2001],call)
    return {
        "contract":CONTRACT,
        "original_whole_source_sha256":RAW_SOURCE,
        "frozen_native_public_support_spec_sha256":task_sha,
        "original_selected_train_rows":list(CANDIDATES),
        "original_source_classes_and_public_task_identity":identities,
        "original_dev_and_sealed_test_source_tasks_not_exposed":True,
        "third_party_source_exec_only_in_restricted_worker":True,
        "native_original_source_state_unchanged":True,
        "source_original_private_verifier_not_executed":True,
        "no_learned_policy_or_reward_claim":True,
        "actual_physical_read_only_source_tool_call_count":len(receipts),
        "actual_source_public_tool_receipts":receipts,
        "original_public_moderation":review,
        "original_public_create_if_missing":tag,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input-dir",required=True,type=Path)
    p.add_argument("--task-spec",required=True,type=Path)
    p.add_argument("--output",required=True,type=Path)
    a=p.parse_args()
    v=run(a.input_dir,a.task_spec)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(v,sort_keys=True,indent=2)+"\n")
    print("OWI_EC005S_NATIVE_SOURCE_PUBLIC_SUPPORT",json.dumps({
        k:v[k] for k in ("actual_physical_read_only_source_tool_call_count",
                        "original_public_moderation","original_public_create_if_missing")},
        sort_keys=True))
if __name__=="__main__":
    main()
