#!/usr/bin/env python3
"""Independent T original TRAIN source public-state and strict no-op gate.

Uses public-tool receipts only, not the experiment's classification code,
environment initial/final state, source class, private verifier, agent gold,
unselected counterfactual source calls or invented task masking. A source
status query about an unrelated record NEVER becomes a task-authorized no-op.
"""
from __future__ import annotations
import argparse,ast,collections,hashlib,json,math
from pathlib import Path

CONTRACT="OWI-EC005T-INDEPENDENT-NATIVE-TRAIN-PUBLIC-STATE-SUPPORT-GATE/1"
RUN="OWI-EC005T-NATIVE-SECOND-TRAIN-CANDIDATE-PUBLIC-ONLY/1"
SPEC="OWI-EC005T-ORIGINAL-NATIVE-SECOND-CANDIDATE-CURRENT-STATE-SUPPORT/1"
SHA="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
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
LOCK={
 1549:("bd3ce85082893c9a7290a2bdd14ed34945f1fd13b481e367d72e1247aea06017",
       "06b3255e155f4e0e388066d1869353529c0e6681b478668f36bce44cf8cbb65d"),
 1900:("b5ef973aea19919afbe9e5a15c5ce7c16dcdbd7c188a607353391e14868ddb1d",
       "ce1cff1989937960c321f9108b0971e039748a54758c39eca54aa564fb19bf54"),
 5:("4ef2d7157eace72aca1ea346bf7f1c5c26c9fc09bb4e7773400c2e557c212ee8",
    "17a6d595b2f53fcc1570f28fc3758d5e3beb0a1c57c7ebd06d5f639799cae5b7"),
 2000:("f32173b7fb07582f45d330c63ae31bb2328b315cc9218a385d433b52792022ac",
       "6c899b813aa7a53ec03f35f031557a59abde124a784c84d4e8695d767f8f554f"),
}
SAFE={
 1549:("get_user_by_name","get_cart_by_user_id","list_cart_items","get_product_by_name"),
 1900:("get_subscriber_by_email","list_subscriptions_for_subscriber",
       "check_subscription_exists_for_location"),
 5:("get_user_account_by_username","get_participant_by_user_account",
    "list_current_enrollments_for_participant","list_enrollments_for_participant",
    "get_clinical_trial_by_id"),
 2000:("list_folders",),
}
FIRST={1549:"get_user_by_name",1900:"get_subscriber_by_email",
       5:"get_user_account_by_username",2000:"list_folders"}

def deny(message):
    raise ValueError(message)
def good_sha(value):
    return isinstance(value,str) and len(value)==64 and all(c in "0123456789abcdef" for c in value)
def finite(value,low,high):
    return type(value) in (int,float) and math.isfinite(value) and low<=value<=high
def actual(obj):
    if obj is None:return None
    return obj["data"] if obj.get("success") is True else None
def source_items(v):
    if isinstance(v,list):return [x for x in v if isinstance(x,dict)]
    if isinstance(v,dict):
        for k in ("data","items","cart_items","subscriptions",
                  "enrollments","results","records","trials","folders"):
            if k in v:return source_items(v[k])
        if all(isinstance(z,dict) for z in v.values()):return list(v.values())
        return [v]
    return []
def source_first(obj):
    seq=source_items(actual(obj))
    return seq[0] if seq else None
def ident(obj,keys):
    if not isinstance(obj,dict):return None
    for k in keys:
        v=obj.get(k)
        if isinstance(v,(str,int)) and str(v):
            return str(v)
    return None

def verify_protocol(p):
    b=p.read_bytes();o=json.loads(b)
    source=o.get("source",{});sample=o.get("sampling",{});q=o.get("qualification",{})
    if (o.get("contract")!=SPEC or source.get("full_sha256")!=SHA or
        source.get("exact_distinct_original_family_rows")!=list(ROWS) or
        source.get("group_seed")!=4611 or source.get("partition")!="train" or
        source.get("original_private_verifier_never_mounted_or_executed") is not True or
        source.get("sealed_dev_test_task_or_tools_never_opened") is not True or
        sample.get("max_total_selected_public_tool_calls")!=35 or
        sample.get("source_initial_state_unmodified") is not True or
        sample.get("all_tools_physical_original_declared_public_read_only") is not True or
        sample.get("source_private_final_state_discarded") is not True or
        q.get("each_candidate_qualifies_only_on_actual_original_public_action_needed_and_original_public_authorized_noaction_both") is not True or
        q.get("existing_other_record_is_not_noop_for_requested_action") is not True or
        o.get("candidates",[{}])[0].get("public_target_quantities")!=TARGETS):
        deny("changed original source cohort, reward boundary or no-op criterion")
    return hashlib.sha256(b).hexdigest()

class PublicReplay:
    def __init__(self,trial):
        self.events={row:[] for row in ROWS}
        self.omissions=trial.get("public_schema_or_source_evidence_omissions",[])
        schemas=trial.get("selected_source_public_read_schema_required")
        if (not isinstance(schemas,dict) or set(schemas)!={str(r) for r in ROWS}):
            deny("declared original public source read schemas missing")
        self.schemas=schemas
        if not isinstance(self.omissions,list) or len(self.omissions)>30:
            deny("unbounded source-schema omitted calls")
        for r in self.omissions:
            if (not isinstance(r,dict) or r.get("original_row") not in ROWS or
                r.get("reason") not in (
                    "source_public_tool_not_declared",
                    "original_source_public_schema_not_satisfied",
                    "source_user_id_not_observed",
                    "original_requested_cart_not_authoritatively_identified",
                    "original_source_subscriber_id_not_observed",
                    "conditional_create_public_check_required_schema_unknown",
                    "original_public_user_account_not_observed",
                    "original_public_participant_lookup_schema_unknown",
                    "original_public_participant_id_link_mismatch",
                    "original_source_participant_id_not_observed")):
                deny("injected source failure/omission status")
        receipts=trial.get("source_public_selected_read_receipts")
        if (not isinstance(receipts,list) or not 4<=len(receipts)<=35 or
            trial.get("original_source_public_only_read_calls_physically_executed")!=len(receipts)):
            deny("missing actual physical original source public tool calls")
        last=-1
        for e in receipts:
            row=e.get("original_row")
            if row not in ROWS or ROWS.index(row)<last:
                deny("unprecommitted source family or changed source tool order")
            last=ROWS.index(row)
            tool=e.get("selected_public_read_tool")
            args=e.get("actual_original_source_public_arguments")
            if tool not in SAFE[row] or not isinstance(args,dict):
                deny("source-original write action or invented tool/arguments")
            required=schemas[str(row)].get(tool)
            if not isinstance(required,list) or set(args)!=set(required):
                deny("actual original selected public call violates original source declared required params")
            data=e.get("raw_actual_original_public_reply")
            if (not isinstance(data,str) or not data or len(data)>8192 or
                any(t in data.casefold() for t in ("hashed_password","password_hash","access_token","private_key"))):
                deny("source public reply missing, oversized or credential exposed")
            hashvalue=hashlib.sha256(json.dumps(data,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
            if (e.get("sha256_actual_original_public_reply")!=hashvalue or
                not good_sha(e.get("sha256_full_original_reply_audit_only")) or
                type(e.get("source_public_sensitive_field_redacted")) is not bool or
                e.get("source_private_final_state_discarded") is not True or
                e.get("source_private_native_verifier_not_executed") is not True or
                not finite(e.get("physical_original_source_tool_seconds"),0,60) or
                not finite(e.get("physical_source_worker_wall_seconds"),0,90) or
                not finite(e.get("physical_worker_peak_rss_kib"),1000,1000000)):
                deny("unsupported physical source tool receipt, private leak or forged projection digest")
            try:
                parsed=ast.literal_eval(data)
            except (SyntaxError,ValueError,TypeError,MemoryError,RecursionError) as ex:
                raise ValueError("actual original source public projection cannot be re-parsed") from ex
            if not isinstance(parsed,dict) or parsed.get("success") not in (True,False):
                deny("source public success/record framing invalid")
            expected_status=("source_success" if parsed.get("success") is True else "source_failure")
            if e.get("status")!=expected_status:
                deny("source-original successful public read claimed failed or vice versa")
            # The full raw tool response is only hashed by host. Credentials
            # are deleted from stored projections before logging/artifacts.
            self.events[row].append((tool,args,parsed,e))
        for row in ROWS:
            if not self.events[row] or self.events[row][0][0]!=FIRST[row]:
                deny("precommitted genuine first original source public read not physically selected")
        self.checked=0
    def next(self,row,tool,expected_args=None):
        events=self.events[row]
        i=self._counts.get(row,0) if hasattr(self,"_counts") else 0
        if i>=len(events):
            return None
        e=events[i]
        if e[0]!=tool:
            deny("source original read order deviates from public-only plan")
        if expected_args is not None and e[1]!=expected_args:
            deny("actual selected public args not derived from previous real original public result")
        if not hasattr(self,"_counts"):self._counts={}
        self._counts[row]=i+1
        self.checked+=1
        return e[2]
    def more(self,row):
        return (self._counts.get(row,0) if hasattr(self,"_counts") else 0)<len(self.events[row])
    def assert_consumed(self):
        if self.checked!=sum(map(len,self.events.values())):
            deny("unaccounted extra fabricated source original public tool receipt")

def cart_gate(p):
    a=p.next(1549,"get_user_by_name",{"name":"Alice Chan"})
    user=source_first(a)
    if user is None:
        return {"source_user_observed":False,"cart_original_task_binding_verified":False,
                "original_requested_cart_cases":[],"genuine_mixed_support":False}
    uid=ident(user,("_id","user_id","id"))
    if user.get("name")!="Alice Chan" or not uid:
        deny("source-user first selected public lookup mismatched original task")
    cart=p.next(1549,"get_cart_by_user_id",{"user_id":uid})
    cart_state=source_first(cart)
    found_id=ident(cart_state,("cart_id","_id","id"))
    exact_link=found_id=="CRT-X01"
    if p.more(1549) and p.events[1549][p._counts.get(1549,0)][0]=="list_cart_items":
        listing=p.next(1549,"list_cart_items",{"user_id":uid})
    else:listing=None
    cart_items=source_items(actual(listing))
    products={}
    for name in TARGETS:
        if not p.more(1549):break
        product=p.next(1549,"get_product_by_name",{"name":name})
        product_obj=source_first(product)
        if product_obj and product_obj.get("name")==name:
            products[name]=ident(product_obj,("product_id","_id","id"))
    statuses=[]
    for name,wanted in TARGETS.items():
        pid=products.get(name)
        if not exact_link or actual(listing) is None or not pid:
            state="unresolved_source_cart_user_identity_or_product"
            cur=None
        else:
            relevant=[r for r in cart_items if
                      str(r.get("product_id",r.get("item_id","")))==pid]
            if len(relevant)>1:deny("duplicate source cart product linkage")
            if relevant:
                q=relevant[0].get("quantity")
                if type(q) is not int or q<0:cur=None
                else:cur=q
            else:cur=0
            state=("already_satisfied_no_cart_write" if cur==wanted else
                   "requested_cart_quantity_mutation") if cur is not None else "unresolved_actual_quantity"
        statuses.append({"public_target_product_name":name,"requested_quantity":wanted,
                         "observed_original_public_current_quantity":cur,
                         "original_public_rule_action_class":state})
    counter=collections.Counter(x["original_public_rule_action_class"] for x in statuses)
    return {"source_user_observed":True,
            "cart_original_task_public_user_id":uid,
            "original_get_cart_by_user_id_returned_cart_id":found_id,
            "cart_original_task_binding_verified":exact_link,
            "actual_original_public_cart_items_returned":len(cart_items),
            "original_requested_cart_cases":statuses,
            "original_public_conditional_cart_counts":dict(counter),
            "genuine_mixed_support":bool(
                counter["already_satisfied_no_cart_write"] and
                counter["requested_cart_quantity_mutation"]) and exact_link}

def geo_gate(p):
    e=p.next(1900,"get_subscriber_by_email")
    args=p.events[1900][0][1]
    if set(args) not in ({"email"},{"email_address"}) or list(args.values())!=["alice.chan@example.com"]:
        deny("original public subscriber specified email changed")
    who=source_first(e)
    sid=ident(who,("subscriber_id","_id","id"))
    if not sid:return {"original_public_subscriber_observed":False,"genuine_mixed_support":False}
    sub=p.next(1900,"list_subscriptions_for_subscriber",{"subscriber_id":sid}) if p.more(1900) else None
    subs=source_items(actual(sub))
    for item in subs:
        if item.get("subscriber_id")!=sid:
            deny("foreign subscriber public subscription contaminates original user")
    listed=[{"subscription_id":r.get("subscription_id"),
             "active_status":r.get("active_status"),
             "latitude":r.get("latitude"),"longitude":r.get("longitude")} for r in subs]
    sf=None
    if p.more(1900):
        rec=p.next(1900,"check_subscription_exists_for_location")
        current_args=p.events[1900][p._counts[1900]-1][1]
        if (any(current_args.get(k)!=37.7749 for k in ("lat","latitude") if k in current_args) or
            any(current_args.get(k)!=-122.4194 for k in ("lon","lng","longitude") if k in current_args) or
            ("subscriber_id" in current_args and current_args["subscriber_id"]!=sid)):
            deny("condition check did not probe original requested SF coordinates/subscriber")
        sf=actual(rec)
        if type(sf) not in (bool,type(None)):
            deny("original location check returned ambiguous or nonboolean source reply")
    cond=("create_if_missing_source_candidate" if sf is False else
          "already_exists_no_create" if sf is True else "unresolved")
    return {"original_public_subscriber_observed":True,
            "original_source_subscriber_id":sid,
            "original_original_subscriber_public_rows":listed,
            "original_conditional_create_target":"San Francisco",
            "original_requested_sf_location_exists":sf,
            "original_sf_create_conditional_class":cond,
            "original_mutation_required_existing_LA_London_not_noops":True,
            "genuine_mixed_support":False,
            "reason":"only_one_original_public_conditional_create_target_has_an_actual_source_state"}

def trial_gate(p):
    a=p.next(5,"get_user_account_by_username",{"username":"farida.youssef"})
    acct=source_first(a)
    if not acct:
        return {"original_source_trial_participant_observed":False,"genuine_mixed_support":False}
    aid=ident(acct,("account_id","user_account_id","user_id","_id","id"))
    pid=ident(acct,("participant_id",))
    if acct.get("username")!="farida.youssef" or not pid:
        deny("original participant source account ID is not source-public grounded")
    participant=None
    if p.more(5) and p.events[5][p._counts.get(5,0)][0]=="get_participant_by_user_account":
        x=p.next(5,"get_participant_by_user_account")
        args=p.events[5][p._counts[5]-1][1]
        if any(v not in (aid,"farida.youssef") for v in args.values()):
            deny("source participant lookup uses nonpublic foreign account")
        participant=source_first(x)
        if participant:
            alternate=ident(participant,("participant_id","_id","id"))
            if alternate and alternate!=pid:
                deny("conflicting original-public participant identity")
    current=p.next(5,"list_current_enrollments_for_participant",{"participant_id":pid}) if p.more(5) else None
    all_enrollments=p.next(5,"list_enrollments_for_participant",{"participant_id":pid}) if p.more(5) else None
    active=source_items(actual(current));all_rows=source_items(actual(all_enrollments))
    for r in active+all_rows:
        if r.get("participant_id")!=pid:
            deny("foreign participant contamination in source-public trial records")
    seen={}
    for r in active[:5]:
        if not p.more(5):break
        e=p.next(5,"get_clinical_trial_by_id",{"trial_id":r.get("trial_id")})
        obj=source_first(e)
        if obj and obj.get("trial_id")==r.get("trial_id"):
            seen[r["trial_id"]]=obj
    decisions=[]
    for e in active[:5]:
        tid=e.get("trial_id");trial=seen.get(tid)
        status=trial.get("status") if trial else None
        enrollment=e.get("enrollment_status")
        cls=("withdraw_required" if enrollment=="enrolled" and status=="suspended"
             else "leave_active_non_suspended_trial_enrollment_unchanged"
                  if enrollment=="enrolled" and status in ("active","completed")
             else "unresolved_source_trial_status")
        decisions.append({"original_public_trial_id":tid,
                          "original_public_trial_name":trial.get("name") if trial else None,
                          "public_enrollment_status":enrollment,"public_trial_status":status,
                          "original_source_conditional_withdraw_class":cls})
    counters=collections.Counter(d["original_source_conditional_withdraw_class"] for d in decisions)
    prior_withdrawn_ctc3=sum(
        x.get("trial_id")=="CT-C3" and x.get("enrollment_status")=="withdrawn"
        for x in all_rows)
    consent=participant.get("consent_status") if participant else None
    return {"original_source_trial_participant_observed":True,
            "original_public_participant_id":pid,
            "original_source_current_enrollment_count":len(active),
            "original_source_all_enrollment_count":len(all_rows),
            "original_source_conditional_withdraw_cases":decisions,
            "original_source_withdraw_policy_status_counts":dict(counters),
            "source_public_prior_withdrawn_ctc3_found":prior_withdrawn_ctc3,
            "source_public_consent_status":consent,
            "requested_public_consent_valid_status_already_satisfied":(
                consent=="valid" if isinstance(consent,str) else None),
            "genuine_mixed_support":bool(
                counters["withdraw_required"] and
                counters["leave_active_non_suspended_trial_enrollment_unchanged"])}

def bookmark_gate(p):
    e=p.next(2000,"list_folders",{})
    folder_records=source_items(actual(e))
    found={r.get("name","").casefold() for r in folder_records if isinstance(r.get("name"),str)}
    target=[{"original_public_requested_folder":name,
             "already_present_in_selected_original_public_list":name.casefold() in found}
            for name in FOLDERS]
    count=sum(x["already_present_in_selected_original_public_list"] for x in target)
    return {"original_public_existing_folder_records":len(folder_records),
            "original_requested_folder_public_existence_statuses":target,
            "already_present_original_requested_folders":count,
            "missing_original_requested_folders":len(target)-count,
            "genuine_mixed_support":False,
            "reason":"create-hierarchy instruction does_not_authorize_noop_without_independent_public_conditional_semantics"}

def adjudicate(trial,*,task_spec):
    spec_hash=verify_protocol(task_spec)
    if (not isinstance(trial,dict) or trial.get("contract")!=RUN or
        trial.get("original_source_full_sha256")!=SHA or
        trial.get("frozen_original_source_current_state_protocol_sha256")!=spec_hash or
        trial.get("original_source_train_rows")!=list(ROWS) or
        trial.get("original_private_source_and_native_verifier_not_exported") is not True or
        trial.get("original_source_initial_state_and_user_task_unmodified") is not True or
        trial.get("no_original_source_private_checker_executed") is not True or
        trial.get("no_actual_terminal_reward_or_policy_training") is not True or
        trial.get("sealed_dev_and_test_families_unopened") is not True):
        deny("original source native data/actor/verifier boundary changed")
    identities=trial.get("original_public_and_class_hashes")
    if not isinstance(identities,dict) or set(identities)!={str(x) for x in ROWS}:
        deny("not original four source groups")
    for row in ROWS:
        h=identities[str(row)]
        if (h.get("original_executable_class_sha256")!=LOCK[row][0] or
            h.get("public_task_sha256")!=LOCK[row][1]):
            deny("independently source-locked original class/public prompt identity drift")
    p=PublicReplay(trial)
    results={
        "1549":cart_gate(p),
        "1900":geo_gate(p),
        "5":trial_gate(p),
        "2000":bookmark_gate(p),
    }
    p.assert_consumed()
    positive={row:r["genuine_mixed_support"] for row,r in results.items()}
    return {
        "contract":CONTRACT,
        "frozen_source_original_protocol_sha256":spec_hash,
        "source_whole_unchanged_original_sha256":SHA,
        "original_source_original_train_family_rows":list(ROWS),
        "original_source_read_only_actual_calls":p.checked,
        "source_original_tool_statuses":dict(collections.Counter(
            r["status"] for r in trial["source_public_selected_read_receipts"])),
        "original_source_public_only_missing_evidence_omissions":p.omissions,
        "independently_reconstructed_source_public_candidate_states":results,
        "qualifying_naturally_mixed_source_public_action_noaction_by_family":positive,
        "qualifying_original_mixed_condition_family_count":sum(positive.values()),
        "predecessor_S_row_2001_class_also_used_by_T_row_2000":(
            LOCK[2000][0]=="f32173b7fb07582f45d330c63ae31bb2328b315cc9218a385d433b52792022ac"),
        "new_independent_executable_train_families_relative_to_S":[1549,1900,5],
        "original_private_checker_or_hidden_source_state_not_used":True,
        "source_development_and_sealed_test_families_not_opened":True,
        "native_original_source_mutation_not_executed":True,
        "source_public_private_credentials_redacted":True,
        "no_causal_policy_learning_or_original_native_terminal_reward":True,
        "scientific_disposition":(
            "NATURAL_ORIGINAL_NATIVE_ACTION_NOACTION_SUPPORT_FOUND_FOR_SCOPED_CONDITIONAL_FAMILY"
            if any(positive.values()) else
            "FOUR_FAMILY_ORIGINAL_NATIVE_SOURCE_PUBLIC_SUPPORT_NOT_YET_QUALIFIED"),
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--trial",type=Path,required=True)
    p.add_argument("--task-spec",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    result=adjudicate(json.loads(a.trial.read_text()),task_spec=a.task_spec)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("OWI_EC005T_INDEPENDENT_ORIGINAL_NATIVE_PUBLIC_CONDITIONAL_GATE",
          json.dumps(result,sort_keys=True))
if __name__=="__main__":
    main()
