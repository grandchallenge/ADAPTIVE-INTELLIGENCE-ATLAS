#!/usr/bin/env python3
"""OWI-EC005U: all-TRAIN-family original-public eligibility census and bounded native reads.

Original full source 2,550-task byte lock validated before partitioning.
Train only original public user messages and declared tool signatures are
surveyed (all 30 families, all TRAIN tasks); DEV/TEST prompts not exported.
Eight precommitted class-independent new TRAIN tasks receive genuine source-
native public read-only tool calls in no-network/nonroot/read-only Docker.
Never executes original code on host, mounts original private verifier, or
publishes original private source state. Original states/prompts unchanged.
Conditional words, available tools and existing unrelated records DO NOT
constitute proof of natural matched action/no-action or learned cognition.
"""
from __future__ import annotations
import argparse,hashlib,json,re,tempfile
from collections import Counter,defaultdict
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_split import partition
from owi_ec005_realtools_intake import canonical,public_view,DatasetBoundaryError
from owi_ec005_realtools_randomized import IMAGE,call_child,fingerprint
from owi_ec005_realtools_episode_select import write_json
from owi_ec005_realtools_goal_policy import WORKER,unpack_reply

CONTRACT="OWI-EC005U-SOURCE-LOCKED-TRAIN-CENSUS-PUBLIC-READS/1"
SPEC="OWI-EC005U-ORIGINAL-SOURCE-TRAIN-ELIGIBILITY-CENSUS-AND-PUBLIC-READS/1"
ORIGINAL="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
ROWS=(25,87,185,236,672,710,735,2199)
PRIOR=(0,2,3,2151,2001,1549,1900,5,2000)
WORDS=re.compile(r"\b(?:if|unless|otherwise)\b|\bwhere applicable\b",re.IGNORECASE)
PRIVATE_FIELDS=("password","secret","token","credential","private_key","api_key","auth_header",
                "authentication","oauth","client_secret","ssn","social_security","authorization")
MAX_RAW=8192

def sha(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def check_protocol(path):
    b=path.read_bytes();d=json.loads(b)
    src=d.get("source",{});sm=d.get("sampling",{});e=d.get("evidence",{})
    candidates=d.get("precommitted_native_public_reads",[])
    if (d.get("contract")!=SPEC or src.get("full_bytes_sha256")!=ORIGINAL or
        src.get("grouping_seed")!=4611 or src.get("expected_total_tasks")!=2550 or
        src.get("expected_train_connected_classes")!=30 or
        src.get("expected_dev_connected_classes")!=10 or
        src.get("expected_sealed_test_connected_classes")!=11 or
        src.get("source_private_verifier_never_executed") is not True or
        src.get("sealed_dev_and_test_content_never_exported") is not True or
        d.get("precommitted_distinct_source_train_candidate_rows")!=list(ROWS) or
        [c.get("row") for c in candidates]!=list(ROWS) or
        d.get("census",{}).get("families_seen_before_U")!=list(PRIOR) or
        sm.get("max_physical_selected_source_read_calls")!=24 or
        sm.get("max_public_reply_chars_per_call")!=MAX_RAW or
        sm.get("source_original_class_and_initial_state_unmodified") is not True or
        sm.get("no_original_source_write_tools") is not True or
        sm.get("redact_public_credentials_before_artifact_or_logs") is not True or
        sm.get("source_native_private_checker_not_mounted") is not True or
        e.get("full_mixed_action_no_action_requires_same_original_task_rule_and_two_actual_opposing_source_public_states") is not True or
        e.get("public_prompt_word_if_is_not_observed_noop") is not True or
        e.get("mere_possible_conditional_branch_not_actual_mixed_support") is not True):
        raise ValueError("precommitted original source/native public-only U protocol boundary drift")
    for c in candidates:
        if (not isinstance(c.get("public_task_anchors"),list) or
            not 2<=len(c["public_task_anchors"])<=4 or
            not isinstance(c.get("tool_candidates"),list) or
            not 1<=len(c["tool_candidates"])<=3):
            raise ValueError("unbounded source-public candidate or anchors")
        for x in c["tool_candidates"]:
            name=x.get("name")
            if (not isinstance(name,str) or not name.startswith(("get_","list_","find_","check_")) or
                not isinstance(x.get("args_if_exact_required"),dict)):
                raise ValueError("source-public candidate cannot execute unsafe operation")
    return d,hashlib.sha256(b).hexdigest()

def redact(value):
    if isinstance(value,dict):
        return {str(k):redact(v) for k,v in value.items()
                if not any(word in str(k).casefold() for word in PRIVATE_FIELDS)}
    if isinstance(value,list):return [redact(x) for x in value]
    if isinstance(value,str) and re.search(
        r"(?i)(?:oauth[_ -]?token|bearer\s+\S+|sk-[a-z0-9]|eyj[a-z0-9_-]{15,})",value):
        # Some original source *public* text fields contain mock credential
        # strings even when the key itself looks harmless.
        return "[SOURCE_PUBLIC_CREDENTIAL_REDACTED]"
    return value

def inventory(rows, protocol):
    split=partition(rows,seed=4611)
    groups=defaultdict(list)
    for item in split["partitions"]["train"]:
        groups[item["environment_id_sha256"]].append(item)
    if (split["raw_task_count"]!=2550 or
        split["partition_group_counts"]!={"train":30,"dev":10,"test":11} or
        len(groups)!=30):
        raise DatasetBoundaryError("original full-train grouped partition count drift")
    records=[]
    for family,group in sorted(groups.items()):
        terms=0
        read_names=Counter()
        for item in group:
            r=rows[item["row_index"]]
            prompt="\n".join(m["content"] for m in public_view(r)["messages"]
                             if m["role"]=="user")
            if WORDS.search(prompt):terms+=1
            for t in r["extra_info"]["environment"]["tools"]:
                fn=t.get("function",{}) if isinstance(t,dict) else {}
                name=fn.get("name")
                if not isinstance(name,str):raise DatasetBoundaryError("source original declared tool schema missing")
                if name.startswith(("get_","list_","find_","check_")):read_names[name]+=1
        records.append({
            "source_original_train_family_sha256":family,
            "original_source_train_tasks_in_family":len(group),
            "original_public_prompts_containing_condition_words":terms,
            "public_read_tool_names_unique":len(read_names),
            "public_read_tool_occurrences":sum(read_names.values()),
            "public_condition_word_only_not_natural_state_support":True,
        })
    train_idx={x["row_index"]:x for x in split["partitions"]["train"]}
    prior_families={train_idx[i]["environment_id_sha256"] for i in PRIOR}
    chosen=protocol["precommitted_native_public_reads"]
    if len(prior_families)!=8: # S/T row2001/2000 share one class; R 0/2/3
        raise DatasetBoundaryError("known existing R/S/T family count drift")
    chosen_fams=set()
    selected={}
    for c in chosen:
        i=c["row"]
        if i not in train_idx:raise DatasetBoundaryError("predeclared new U row is not original TRAIN")
        item=train_idx[i]
        fam=item["environment_id_sha256"]
        if fam in chosen_fams or fam in prior_families:
            raise DatasetBoundaryError("U selected duplicate or previously studied R/S/T original class")
        chosen_fams.add(fam)
        r=rows[i]
        task=public_view(r)
        prompt=" ".join(m["content"] for m in task["messages"] if m["role"]=="user")
        if not all(s.casefold() in prompt.casefold() for s in c["public_task_anchors"]):
            raise DatasetBoundaryError("U precommitted original PUBLIC task anchor differs")
        env=r["extra_info"]["environment"]
        methods={}
        original_tools=[]
        for t in env["tools"]:
            f=t.get("function",{}) if isinstance(t,dict) else {}
            name=f.get("name")
            if not isinstance(name,str) or not isinstance(f.get("parameters"),dict):
                raise DatasetBoundaryError("original source declared public method invalid")
            methods[name]=f["parameters"]
            original_tools.append({"name":name,"parameters":f["parameters"]})
        for tool in c["tool_candidates"]:
            if tool["name"] not in methods:
                # A previously listed public tool must remain declared,
                # but an unavailable desired tool does not prove absence.
                pass
        task["tools"]=original_tools
        full_env={k:env[k] for k in ("class_code","class_name","initial_state","tools")}
        selected[i]=(task,full_env,methods,item)
    if len(chosen_fams)!=8 or len(chosen_fams & prior_families):
        raise DatasetBoundaryError("new original source family independence failure")
    results={
        "original_total_tasks":split["raw_task_count"],
        "independent_original_connected_families":split["independent_connected_environment_families"],
        "original_family_partition_counts":split["partition_group_counts"],
        "original_task_partition_counts":split["partition_task_counts"],
        "all_30_original_train_family_public_only_census":records,
        "original_train_families_with_any_conditional_language":sum(
            r["original_public_prompts_containing_condition_words"]>0 for r in records),
        "original_training_public_tasks_with_conditional_language":sum(
            r["original_public_prompts_containing_condition_words"] for r in records),
        "original_previous_R_S_T_distinct_train_families":len(prior_families),
        "eight_new_family_disjoint_selection_verified":True,
        "original_dev_or_sealed_test_task_public_content_exported":False,
    }
    return selected,results

def write_selected(selected,root):
    for row,(public,env,methods,item) in selected.items():
        dest=root/str(row);dest.mkdir(parents=True,exist_ok=True)
        # The trusted host source selector's 0444 file mode is essential:
        # Docker's source child runs as UID 65534 and receives a *file*
        # bind mount at /input.json. A private temp workspace + umask 077
        # alone creates 0600 payload files and causes worker exit=1.
        write_json(dest/"public.json",public)
        write_json(dest/"environment.json",env)

def original_native_read(root,selected,protocol):
    all_calls=[]
    inability=[]
    for c in protocol["precommitted_native_public_reads"]:
        row=c["row"]
        task,env,methods,item=selected[row]
        for q in c["tool_candidates"]:
            name,args=q["name"],q["args_if_exact_required"]
            declared=methods.get(name)
            if declared is None:
                inability.append({"row":row,"tool":name,"reason":"original_source_public_tool_not_declared"})
                continue
            needed=declared.get("required",[])
            if not isinstance(needed,list) or set(args)!=set(needed):
                inability.append({"row":row,"tool":name,
                     "reason":"original_declared_required_public_arguments_not_matched",
                     "actual_required":needed,"precommitted_argument_names":sorted(args)})
                continue
            if len(all_calls)>=24:raise RuntimeError("U physical source read budget exceeded")
            commands="".join(json.dumps(x,sort_keys=True)+"\n" for x in (
                {"action":"call","tool":name,"arguments":args},
                {"action":"finish"}))
            output,wall=call_child(IMAGE,WORKER,root/str(row)/"environment.json",
                                   input_text=commands,timeout=90)
            if (len(output)!=3 or output[0].get("kind")!="ready" or
                output[0].get("verifier_present") is not False or
                output[1].get("kind")!="observation" or
                output[1].get("tool")!=name or
                output[2].get("kind")!="private_final_state" or
                output[2].get("tool_calls")!=1):
                raise RuntimeError("native source restricted public worker contract violation")
            raw=output[1].get("content")
            if not isinstance(raw,str) or len(raw)>MAX_RAW:
                raise RuntimeError("native source public original tool response invalid")
            native=unpack_reply(raw) if output[1].get("ok") is True and not output[1].get("truncated") else None
            parsed=redact(native) if isinstance(native,dict) else None
            safe=repr(parsed) if parsed is not None else None
            status=("source_public_success" if isinstance(native,dict) and
                    native.get("success") is True else
                    "source_response_truncated" if output[1].get("truncated") else
                    "source_failed_or_unparseable")
            record={
                "original_train_row":row,
                "original_source_family_sha256":item["environment_id_sha256"],
                "actual_selected_original_public_read_tool":name,
                "actual_source_public_read_arguments":args,
                "declared_original_required_public_argument_names":sorted(needed),
                "actual_original_unredacted_public_reply_sha256":hashlib.sha256(raw.encode()).hexdigest(),
                "actual_selected_original_public_reply_redacted":safe,
                "actual_selected_original_public_redacted_sha256":fingerprint(safe) if safe is not None else None,
                "actual_original_source_public_tool_result":status,
                "source_worker_reply_was_truncated":output[1].get("truncated") is True,
                "physical_native_public_tool_seconds":output[1].get("elapsed_seconds"),
                "physical_native_source_container_wall_seconds":wall,
                "native_source_worker_peak_rss_kib":output[2].get("peak_rss_kib"),
                "source_native_private_verifier_never_mounted":True,
                "original_native_source_private_final_state_discarded":True
            }
            # The source terminal is privileged and deliberately NOT read or
            # serialized. No raw unredacted original public tool value persisted.
            output=None
            all_calls.append(record)
    return all_calls,inability

def run(spec,lock,out_dir):
    protocol,locked_hash=check_protocol(spec)
    source=json.loads(lock.read_text())
    if (source.get("sha256")!=ORIGINAL or
        source.get("revision")!=protocol["source"]["revision"]):
        raise DatasetBoundaryError("original source full-byte identity changed")
    rows=audit_source(source)
    chosen,census=inventory(rows,protocol)
    # Private class/state only in an auto-discarding outside-artifact temporary
    # directory. A failure MUST NOT cause private worker bundles to be uploaded.
    import os
    with tempfile.TemporaryDirectory(prefix="owi_ec005u_private_",
          dir=os.environ.get("RUNNER_TEMP") or None) as temp:
        bundles=Path(temp)/"only_docker_worker"
        write_selected(chosen,bundles)
        # All original source-private class/state is confined to that tree.
        receipts,unavailable=original_native_read(bundles,chosen,protocol)
    del rows
    identities={
      str(i):{
        "original_train_group_sha256":p["environment_id_sha256"],
        "original_public_prompt_sha256":p["public_prompt_sha256"],
        "original_public_bundle_sha256":sha(public),
        "original_source_executable_class_sha256":hashlib.sha256(env["class_code"].encode()).hexdigest(),
        "original_public_read_tool_required_schema":{
            q["name"]:m.get(q["name"],{}).get("required",None)
            for q in next(c["tool_candidates"] for c in
                          protocol["precommitted_native_public_reads"] if c["row"]==i)}
       }
      for i,(public,env,m,p) in chosen.items()
    }
    report={
       "contract":CONTRACT,
       "source_original_raw_sha256_verified":ORIGINAL,
       "frozen_source_eligibility_protocol_sha256":locked_hash,
       "source_original_dev_and_test_content_sealed":True,
       "original_native_source_initial_states_unchanged":True,
       "source_native_private_checker_never_run":True,
       "native_initial_state_source_code_executed_only_networkless_restricted_docker":True,
       "no_source_mutation_or_native_terminal_reward_or_agent_training":True,
       "source_public_credential_field_redaction_enabled":True,
       "full_original_train_census":census,
       "selected_original_train_source_identities":identities,
       "actual_native_public_read_only_tool_receipts":receipts,
       "source_native_public_lookup_unavailable_or_incompatible":unavailable,
       "actual_native_source_read_only_tool_count":len(receipts),
       "original_natural_same_conditional_rule_action_and_noaction_claim":"NOT_ESTABLISHED",
    }
    # Source-private Docker input bundles were destroyed on exit, including
    # exceptions, before any public evidence artifact is written.
    return report

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--task-spec",type=Path,required=True)
    p.add_argument("--source-lock",type=Path,default=Path(
        "governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json"))
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    a.output.parent.mkdir(parents=True,exist_ok=True)
    result=run(a.task_spec,a.source_lock,a.output.parent)
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("OWI_EC005U_30_TRAIN_FAMILY_CENSUS",json.dumps({
        k:v for k,v in result["full_original_train_census"].items()
        if k!="all_30_original_train_family_public_only_census"},sort_keys=True))
    print("OWI_EC005U_NATIVE_PUBLIC_ELIGIBILITY_READS",json.dumps({
        "actual_native_source_read_only_tool_count":result["actual_native_source_read_only_tool_count"],
        "selected_original_train_rows":list(result["selected_original_train_source_identities"]),
        "per_family_observed_status":[{"row":r["original_train_row"],
            "tool":r["actual_selected_original_public_read_tool"],
            "status":r["actual_original_source_public_tool_result"],
            "public_reply_redacted_excerpt":(r["actual_selected_original_public_reply_redacted"] or "")[:350]}
              for r in result["actual_native_public_read_only_tool_receipts"]],
        "unavailable":result["source_native_public_lookup_unavailable_or_incompatible"],
        "original_same_rule_mixed_support":"NOT_ESTABLISHED"},sort_keys=True))
if __name__=="__main__":
    main()
