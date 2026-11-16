#!/usr/bin/env python3
"""Independent original public-source U eligibility evidence and no-false-noop gate.

The original unmodified full-source SHA and source group split come from
separate full byte identity/partition validation. This gate independently
anchors all eight original TRAIN source public user-prompt and family IDs
against the earlier pre-U native family survey, recomputes every observed
public reply projection/status and expected method choice from the frozen
source-public schema and plan, and refuses to infer negative/clean states from
missing tools or source *language* alone. It cannot certify source-native
terminal reward, counterfactual tool outputs, or learned causal introspection.
"""
from __future__ import annotations
import argparse,ast,collections,hashlib,json,math,re
from pathlib import Path

CONTRACT="OWI-EC005U-INDEPENDENT-ORIGINAL-TRAIN-CENSUS-AND-PUBLIC-READ-GATE/1"
RUN="OWI-EC005U-SOURCE-LOCKED-TRAIN-CENSUS-PUBLIC-READS/1"
SPEC="OWI-EC005U-ORIGINAL-SOURCE-TRAIN-ELIGIBILITY-CENSUS-AND-PUBLIC-READS/1"
ORIGINAL="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
ROWS=(25,87,185,236,672,710,735,2199)
PRIOR=(0,2,3,2151,2001,1549,1900,5,2000)
PREVIOUS_F_PUBLIC={
 25:("8d797f1082a60c8b6e046e716b3ad0c810a439e178bfacb593deee3f09c3743f","0481ec3685c8559311e4145273a3a1840362f22bb82d7b982977d1492bba1e53"),
 87:("caab4d13b539cbb853496342c8fe9c0f5566127c63fe8c83c187f990fc60e7fe","74eedc400a402e4f2fb60feda4d689b4aa7e643a7d63506c75b8e0f7f12f259a"),
 185:("31e60d20e53a6d8fd3e0aa842546d2530ac9d988da81232bb5bbb090fa57978e","4d35865dd83713ad921af44f1e9e71a1db7d468fa72fa3e07b7b3c1fd65e514e"),
 236:("fd0d8974e2af1954f04775ff85b3bc002a4c6bc14b35c5883a28555d8adaa4df","25d2be96389844fe56ff7490182876380bc2b0e153ee3da53598dc265b24708d"),
 672:("fb20c5870522eef16dec83b35e3b3973d9b447f78913d580f607c802085d16f9","2d8909088e640bcadd8de8fcfe685b5f029d94a9c7c2758ddb58410cd48ef9cd"),
 710:("a739046b13061603e09af000ceed469840dfecba0068db2e1919454b18394b0c","97bca760aa53e15f281b71771a6b63a1ba294c1ce3123f9632b114cbf12d6d36"),
 735:("c33b017ebab295bd69d9b6837cf7b0b54a289ae75ac3866bd4dd13b1de28adb6","5f9448e354661afca6a0a06905565b76c02836968ae0c705aaeeb338b2337beb"),
 2199:("a9a5dadb652ba0ba5d3814323b78b1f51a099f008cd63d9ea173fd94e05f4be8","bdbf8a5ad894b7199b7a51f45d5cb1ee4b0556500bc657b188179b1ecebeaaf1")
}
BANNED=("password","secret","token","credential","private_key","api_key","auth_header",
        "social_security","authorization")
def deny(msg):raise ValueError(msg)
def okhash(x):
    return isinstance(x,str) and len(x)==64 and all(y in "0123456789abcdef" for y in x)
def finite(x,lo,hi):
    return type(x) in (float,int) and math.isfinite(x) and lo<=x<=hi
def verify_spec(path):
    data=path.read_bytes();p=json.loads(data)
    source=p.get("source",{});sm=p.get("sampling",{});e=p.get("evidence",{})
    if (p.get("contract")!=SPEC or
        source.get("full_bytes_sha256")!=ORIGINAL or
        source.get("grouping_seed")!=4611 or
        [source.get("expected_train_connected_classes"),
         source.get("expected_dev_connected_classes"),
         source.get("expected_sealed_test_connected_classes")]!=[30,10,11] or
        source.get("sealed_dev_and_test_content_never_exported") is not True or
        source.get("source_private_verifier_never_executed") is not True or
        p.get("precommitted_distinct_source_train_candidate_rows")!=list(ROWS) or
        p.get("census",{}).get("families_seen_before_U")!=list(PRIOR) or
        sm.get("max_physical_selected_source_read_calls")!=24 or
        sm.get("no_original_source_write_tools") is not True or
        sm.get("source_native_private_checker_not_mounted") is not True or
        sm.get("redact_public_credentials_before_artifact_or_logs") is not True or
        e.get("full_mixed_action_no_action_requires_same_original_task_rule_and_two_actual_opposing_source_public_states") is not True or
        e.get("mere_possible_conditional_branch_not_actual_mixed_support") is not True):
        deny("frozen U original-source eligibility cohort or scientific boundary changed")
    candidates=p.get("precommitted_native_public_reads",[])
    if not isinstance(candidates,list) or [x.get("row") for x in candidates]!=list(ROWS):
        deny("U selected source rows or order changed")
    for c in candidates:
        if (not isinstance(c.get("tool_candidates"),list) or
            not 1<=len(c["tool_candidates"])<=3 or
            not isinstance(c.get("public_task_anchors"),list) or
            len(c["public_task_anchors"])<2):
            deny("U native source public plan malformed")
        for tool in c["tool_candidates"]:
            if (not isinstance(tool.get("name"),str) or
                not tool["name"].startswith(("get_","list_","find_","check_")) or
                not isinstance(tool.get("args_if_exact_required"),dict)):
                deny("source-native unsafe tool")
    return p,hashlib.sha256(data).hexdigest()

def one_reply(r):
    raw=r.get("actual_selected_original_public_reply_redacted")
    status=r.get("actual_original_source_public_tool_result")
    if status not in ("source_public_success","source_failed_or_unparseable",
                      "source_response_truncated"):
        deny("invented actual source public read result status")
    if raw is None:
        if status=="source_public_success":deny("source success without verifiable public content")
        if r.get("actual_selected_original_public_redacted_sha256") is not None:
            deny("source redacted evidence missing but hash supplied")
        return None
    if not isinstance(raw,str) or len(raw)>100000 or any(
        re.search(r"""(?i)['"]?"""+word+r"""[a-z_]*['"]?\s*:""",raw) for word in BANNED):
        deny("source-public original tool projection invalid or sensitive")
    checksum=hashlib.sha256(json.dumps(raw,sort_keys=True,separators=(",",":"),
                                ensure_ascii=False).encode()).hexdigest()
    if r.get("actual_selected_original_public_redacted_sha256")!=checksum:
        deny("original public source reply hash changed")
    try:x=ast.literal_eval(raw)
    except (SyntaxError,ValueError,TypeError,RecursionError,MemoryError) as exc:
        raise ValueError("source public selected response cannot be safely parsed") from exc
    if not isinstance(x,dict) or type(x.get("success")) is not bool:
        deny("invalid projected original native source reply mapping")
    if (x["success"] is True)!=(status=="source_public_success"):
        deny("reported actual source public success does not match source payload")
    return x

def records(x):
    if isinstance(x,list):return [v for v in x if isinstance(v,dict)]
    if isinstance(x,dict):
        for k in ("data","items","records","rooms","users","contacts","professionals",
                  "equipment","locations","sessions","bookings","results","challenges",
                  "categories"):
            if k in x:return records(x[k])
        if all(isinstance(v,dict) for v in x.values()):return list(x.values())
        return [x]
    return []

def adjudicate(result,*,protocol_path):
    p,ph=verify_spec(protocol_path)
    if (not isinstance(result,dict) or result.get("contract")!=RUN or
        result.get("source_original_raw_sha256_verified")!=ORIGINAL or
        result.get("frozen_source_eligibility_protocol_sha256")!=ph or
        result.get("source_original_dev_and_test_content_sealed") is not True or
        result.get("original_native_source_initial_states_unchanged") is not True or
        result.get("source_native_private_checker_never_run") is not True or
        result.get("native_initial_state_source_code_executed_only_networkless_restricted_docker") is not True or
        result.get("no_source_mutation_or_native_terminal_reward_or_agent_training") is not True or
        result.get("source_public_credential_field_redaction_enabled") is not True or
        result.get("original_natural_same_conditional_rule_action_and_noaction_claim")!="NOT_ESTABLISHED"):
        deny("source-private/native-checker/public-only status claims or preregistration invalid")
    census=result.get("full_original_train_census")
    if not isinstance(census,dict):deny("all 30 original source train census missing")
    if (census.get("original_total_tasks")!=2550 or
        census.get("independent_original_connected_families")!=51 or
        census.get("original_family_partition_counts")!={"train":30,"dev":10,"test":11} or
        census.get("original_task_partition_counts")!={"train":1500,"dev":500,"test":550} or
        census.get("original_previous_R_S_T_distinct_train_families")!=8 or
        census.get("eight_new_family_disjoint_selection_verified") is not True or
        census.get("original_dev_or_sealed_test_task_public_content_exported") is not False):
        deny("source original partition/family counts or sealed task boundary incorrect")
    groups=census.get("all_30_original_train_family_public_only_census")
    if not isinstance(groups,list) or len(groups)!=30:
        deny("not all 30 original TRAIN classes surveyed")
    ids=set();cond=0
    for row in groups:
        fam=row.get("source_original_train_family_sha256")
        if not okhash(fam) or fam in ids:deny("train family id duplicated or unverified")
        ids.add(fam)
        n=row.get("original_source_train_tasks_in_family")
        k=row.get("original_public_prompts_containing_condition_words")
        if (not isinstance(n,int) or n!=50 or
            not isinstance(k,int) or not 0<=k<=n or
            row.get("public_condition_word_only_not_natural_state_support") is not True or
            not isinstance(row.get("public_read_tool_names_unique"),int) or
            row["public_read_tool_names_unique"]<1):
            deny("source train conditional public-only statistics wrong/overclaimed")
        cond+=k
    if (census.get("original_training_public_tasks_with_conditional_language")!=cond or
        census.get("original_train_families_with_any_conditional_language")!=sum(
            x["original_public_prompts_containing_condition_words"]>0 for x in groups)):
        deny("original-source condition language statistics not reproducible")
    selected=result.get("selected_original_train_source_identities")
    if not isinstance(selected,dict) or set(selected)!={str(x) for x in ROWS}:
        deny("not eight original precommitted independently grouped source train tasks")
    classes=set();families=set()
    for row in ROWS:
        entry=selected[str(row)]
        want=PREVIOUS_F_PUBLIC[row]
        if (entry.get("original_train_group_sha256")!=want[0] or
            entry.get("original_public_prompt_sha256")!=want[1] or
            entry["original_train_group_sha256"] not in ids or
            not okhash(entry.get("original_source_executable_class_sha256")) or
            not okhash(entry.get("original_public_bundle_sha256"))):
            deny("external pre-U original source TRAIN family or public-task fingerprint mismatch")
        classes.add(entry["original_source_executable_class_sha256"])
        families.add(entry["original_train_group_sha256"])
    if len(classes)!=8 or len(families)!=8:deny("U source-native executable family separation false")
    seen=result.get("actual_native_public_read_only_tool_receipts")
    skipped=result.get("source_native_public_lookup_unavailable_or_incompatible")
    if (not isinstance(seen,list) or not 1<=len(seen)<=24 or
        result.get("actual_native_source_read_only_tool_count")!=len(seen) or
        not isinstance(skipped,list)):
        deny("source physical selected read evidence count invalid")
    status_by_row={str(row):[] for row in ROWS}
    count_by_row={str(row):0 for row in ROWS}
    ptr=0;skip=0
    for c in p["precommitted_native_public_reads"]:
        row=c["row"]
        entry=selected[str(row)]
        methods=entry.get("original_public_read_tool_required_schema")
        if not isinstance(methods,dict):
            deny("source-original public schema per source family missing")
        if set(methods)!={q["name"] for q in c["tool_candidates"]}:
            deny("source-public read candidates not same as preregistration")
        for q in c["tool_candidates"]:
            name,args=q["name"],q["args_if_exact_required"]
            required=methods[name]
            if not isinstance(required,list) or set(required)!=set(args):
                if skip>=len(skipped):deny("missing native original schema mismatch omission")
                o=skipped[skip];skip+=1
                if (o.get("row")!=row or o.get("tool")!=name or
                    o.get("reason") not in (
                      "original_source_public_tool_not_declared",
                      "original_declared_required_public_arguments_not_matched")):
                    deny("source-public unavailable call substituted after observing state")
                if o["reason"]=="original_source_public_tool_not_declared":
                    if required is not None:deny("source-declared tool falsely omitted")
                elif (o.get("actual_required")!=required or
                      o.get("precommitted_argument_names")!=sorted(args)):
                    deny("original source-public required arguments mismatch forged")
                continue
            if ptr>=len(seen):deny("missing originally preselected physically executed source tool")
            r=seen[ptr];ptr+=1
            if (r.get("original_train_row")!=row or
                r.get("original_source_family_sha256")!=entry["original_train_group_sha256"] or
                r.get("actual_selected_original_public_read_tool")!=name or
                r.get("actual_source_public_read_arguments")!=args or
                r.get("declared_original_required_public_argument_names")!=sorted(required) or
                not okhash(r.get("actual_original_unredacted_public_reply_sha256")) or
                r.get("source_native_private_verifier_never_mounted") is not True or
                r.get("original_native_source_private_final_state_discarded") is not True or
                not finite(r.get("physical_native_public_tool_seconds"),0,60) or
                not finite(r.get("physical_native_source_container_wall_seconds"),0,90) or
                not finite(r.get("native_source_worker_peak_rss_kib"),1000,1000000)):
                deny("actual original source tool/identity or timing/privacy receipt forged")
            obs=one_reply(r)
            if obs is not None and isinstance(obs.get("data"),(list,dict)):
                n=len(records(obs["data"]))
            else:n=0
            if n>200:deny("original source public support record bounded export exceeded")
            status_by_row[str(row)].append({
                "selected_public_tool":name,
                "actual_original_source_reply_status":r["actual_original_source_public_tool_result"],
                "visible_source_data_object_count_bounded":n,
                "source_original_public_result_schema_known":obs is not None,
            })
            count_by_row[str(row)]+=1
    if ptr!=len(seen) or skip!=len(skipped):
        deny("unaccounted tool receipt or unsupported public schema omission")
    # This is an *eligibility* study. A native no-action branch is NOT proven
    # by a list existing, by a free slot, by conditional text, or by an unqueried
    # counterfactual. Return strictly positive known statuses only.
    return {
        "contract":CONTRACT,
        "frozen_original_u_public_source_protocol_sha256":ph,
        "full_original_source_unchanged_sha256":ORIGINAL,
        "original_connected_training_environment_families_censused":30,
        "original_training_tasks_public_prompt_checked":1500,
        "original_training_family_conditional_language_counts":{
            "families_with_any_conditional_language":
                census["original_train_families_with_any_conditional_language"],
            "training_tasks_with_any_conditional_language":
                census["original_training_public_tasks_with_conditional_language"],
        },
        "new_predeclared_original_training_families_compared_with_R_S_T":8,
        "previous_R_S_T_source_families":8,
        "total_distinct_original_training_families_explicitly_public_probed_R_through_U":16,
        "actual_original_source_public_read_only_calls_independently_replayed":len(seen),
        "actual_original_source_public_read_counts_by_train_row":count_by_row,
        "original_source_public_read_results_by_train_row":status_by_row,
        "actual_native_source_read_tool_status_counts":dict(collections.Counter(
            r["actual_original_source_public_tool_result"] for r in seen)),
        "source_native_public_methods_unavailable_or_required_schema_mismatch":len(skipped),
        "original_task_state_linkage_certified_from_only_read_tool_census":False,
        "natural_same_original_conditional_action_vs_noaction_support_established":False,
        "positive_information_value_or_learned_causal_repair_established":False,
        "original_native_private_checker_never_executed":True,
        "source_original_dev_test_task_info_never_exported":True,
        "original_source_class_initial_state_unchanged":True,
        "scientific_disposition":"THIRTY_TRAIN_FAMILY_PUBLIC_CENSUS_AND_EIGHT_NEW_NATIVE_SOURCE_READS__STRICT_SAME_RULE_MIXED_NOOP_SUPPORT_UNDECIDED",
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--trial",type=Path,required=True)
    ap.add_argument("--task-spec",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    result=adjudicate(json.loads(a.trial.read_text()),protocol_path=a.task_spec)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("OWI_EC005U_INDEPENDENT_TRAIN_SOURCE_PUBLIC_ELIGIBILITY_GATE",
          json.dumps(result,sort_keys=True))
if __name__=="__main__":
    main()
