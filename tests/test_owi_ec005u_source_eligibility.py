#!/usr/bin/env python3
"""OWI-EC005U hostile synthetic PUBLIC-only boundary fixtures; NOT empirical source."""
from __future__ import annotations
import copy,hashlib,json,sys,tempfile,unittest,os,stat
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005u_source_eligibility import check_protocol,redact,write_selected
from owi_ec005u_source_eligibility_gate import (
  adjudicate,PREVIOUS_F_PUBLIC,ORIGINAL,ROWS,PRIOR,RUN,CONTRACT)
from owi_ec005_realtools_randomized import fingerprint
SPEC=Path(__file__).resolve().parents[1]/"governance/research/OWI_EC005U_SOURCE_ELIGIBILITY_CENSUS_V1.json"

def fixture():
    p,locked=check_protocol(SPEC)
    old=[PREVIOUS_F_PUBLIC[r][0] for r in ROWS]
    other=[hashlib.sha256(f"fake-new-group-{i}".encode()).hexdigest()
           for i in range(22)]
    groups=[{"source_original_train_family_sha256":fam,
             "original_source_train_tasks_in_family":50,
             "original_public_prompts_containing_condition_words":15,
             "public_read_tool_names_unique":2,
             "public_read_tool_occurrences":100,
             "public_condition_word_only_not_natural_state_support":True}
            for fam in old+other]
    source_id={}
    chosen=[]
    for c in p["precommitted_native_public_reads"]:
        row=c["row"]
        req={q["name"]:list(q["args_if_exact_required"]) for q in c["tool_candidates"]}
        source_id[str(row)]={
            "original_train_group_sha256":PREVIOUS_F_PUBLIC[row][0],
            "original_public_prompt_sha256":PREVIOUS_F_PUBLIC[row][1],
            "original_public_bundle_sha256":hashlib.sha256(f"bundle/{row}".encode()).hexdigest(),
            "original_source_executable_class_sha256":hashlib.sha256(
                f"class/{row}".encode()).hexdigest(),
            "original_public_read_tool_required_schema":req}
        for tool in c["tool_candidates"]:
            safe="{'success': True, 'data': []}"
            chosen.append({
                "original_train_row":row,
                "original_source_family_sha256":PREVIOUS_F_PUBLIC[row][0],
                "actual_selected_original_public_read_tool":tool["name"],
                "actual_source_public_read_arguments":tool["args_if_exact_required"],
                "declared_original_required_public_argument_names":sorted(
                    tool["args_if_exact_required"]),
                "actual_original_unredacted_public_reply_sha256":hashlib.sha256(
                    safe.encode()).hexdigest(),
                "actual_selected_original_public_reply_redacted":safe,
                "actual_selected_original_public_redacted_sha256":fingerprint(safe),
                "actual_original_source_public_tool_result":"source_public_success",
                "source_worker_reply_was_truncated":False,
                "physical_native_public_tool_seconds":.001,
                "physical_native_source_container_wall_seconds":.2,
                "native_source_worker_peak_rss_kib":12000,
                "source_native_private_verifier_never_mounted":True,
                "original_native_source_private_final_state_discarded":True})
    return {
       "contract":RUN,
       "source_original_raw_sha256_verified":ORIGINAL,
       "frozen_source_eligibility_protocol_sha256":locked,
       "source_original_dev_and_test_content_sealed":True,
       "original_native_source_initial_states_unchanged":True,
       "source_native_private_checker_never_run":True,
       "native_initial_state_source_code_executed_only_networkless_restricted_docker":True,
       "no_source_mutation_or_native_terminal_reward_or_agent_training":True,
       "source_public_credential_field_redaction_enabled":True,
       "full_original_train_census":{
         "original_total_tasks":2550,
         "independent_original_connected_families":51,
         "original_family_partition_counts":{"train":30,"dev":10,"test":11},
         "original_task_partition_counts":{"train":1500,"dev":500,"test":550},
         "all_30_original_train_family_public_only_census":groups,
         "original_train_families_with_any_conditional_language":30,
         "original_training_public_tasks_with_conditional_language":450,
         "original_previous_R_S_T_distinct_train_families":8,
         "eight_new_family_disjoint_selection_verified":True,
         "original_dev_or_sealed_test_task_public_content_exported":False,
       },
       "selected_original_train_source_identities":source_id,
       "actual_native_public_read_only_tool_receipts":chosen,
       "source_native_public_lookup_unavailable_or_incompatible":[],
       "actual_native_source_read_only_tool_count":len(chosen),
       "original_natural_same_conditional_rule_action_and_noaction_claim":"NOT_ESTABLISHED",
    }

class NativeOriginalTrainFamilyEligibility(unittest.TestCase):
    def test_source_preregistration_fixed_and_full_census(self):
        data,sha=check_protocol(SPEC)
        self.assertEqual(len(sha),64)
        self.assertEqual(data["precommitted_distinct_source_train_candidate_rows"],list(ROWS))
        self.assertEqual(len(data["precommitted_native_public_reads"]),8)
        self.assertEqual(data["census"]["families_seen_before_U"],list(PRIOR))
    def test_original_source_worker_bind_files_readable_to_uid_65534(self):
        # The actual Docker child runs nonroot, and umask 077 alone creates
        # unreadable 0600 files even if the host can inspect them.
        old=os.umask(0o077)
        try:
            with tempfile.TemporaryDirectory() as temp:
                payload={25:({"messages":[{"role":"user","content":"Public synthetic fixture"}],
                              "tools":[]},{"class_code":"class Test: pass",
                              "class_name":"Test","initial_state":{},"tools":[]},{},
                              {"environment_id_sha256":"a"*64})}
                write_selected(payload,Path(temp)/"source")
                for name in ("public.json","environment.json"):
                    f=Path(temp)/"source"/"25"/name
                    self.assertEqual(stat.S_IMODE(f.stat().st_mode),0o444)
        finally:os.umask(old)
    def test_public_tool_sensitive_fields_redacted_recursively(self):
        source={"success":True,"data":[{
            "name":"Alice Chan","hashed_password":"synthetic",
            "api_key":"mock","nested":{"access_token":"x","status":"active"},
            "arr":[{"secret_key":"x","room_id":"R1"}]}]}
        projection=redact(source)
        s=repr(projection)
        for v in ("hashed_password","api_key","access_token","secret_key"):
            self.assertNotIn(v,s)
        self.assertIn("room_id",s)
    def test_independent_census_gate_for_synthetic_fixture(self):
        got=adjudicate(fixture(),protocol_path=SPEC)
        self.assertEqual(got["contract"],CONTRACT)
        self.assertEqual(got["original_connected_training_environment_families_censused"],30)
        self.assertEqual(got["original_training_tasks_public_prompt_checked"],1500)
        self.assertEqual(got["new_predeclared_original_training_families_compared_with_R_S_T"],8)
        self.assertFalse(got["natural_same_original_conditional_action_vs_noaction_support_established"])
        self.assertFalse(got["positive_information_value_or_learned_causal_repair_established"])
    def test_unsafe_changes_to_protocol_rejected(self):
        original=json.loads(SPEC.read_text())
        mutants=[
         ("wrong_family",lambda d:d.__setitem__(
             "precommitted_distinct_source_train_candidate_rows",[2199]+list(ROWS)[1:])),
         ("sealed_exposed",lambda d:d["source"].__setitem__(
             "sealed_dev_and_test_content_never_exported",False)),
         ("native_verifier",lambda d:d["sampling"].__setitem__(
             "source_native_private_checker_not_mounted",False)),
         ("new_state",lambda d:d["sampling"].__setitem__(
             "source_original_class_and_initial_state_unmodified",False)),
         ("no_op_hype",lambda d:d["evidence"].__setitem__(
             "mere_possible_conditional_branch_not_actual_mixed_support",False)),
         ("new_cost",lambda d:d["sampling"].__setitem__(
             "max_physical_selected_source_read_calls",240)),
        ]
        for tag,fn in mutants:
            with self.subTest(tag=tag),tempfile.TemporaryDirectory() as temp:
                x=copy.deepcopy(original);fn(x)
                dest=Path(temp)/"mutant.json";dest.write_text(json.dumps(x))
                with self.assertRaises(ValueError):check_protocol(dest)
    def test_malicious_or_false_success_source_receipt_rejected(self):
        mutant_cases=[
          ("source_bytes",lambda x:x.__setitem__("source_original_raw_sha256_verified","a"*64)),
          ("train_dev_leak",lambda x:x.__setitem__(
              "source_original_dev_and_test_content_sealed",False)),
          ("native_checker",lambda x:x.__setitem__(
              "source_native_private_checker_never_run",False)),
          ("fake_class",lambda x:x["selected_original_train_source_identities"]["25"].__setitem__(
              "original_train_group_sha256","b"*64)),
          ("forged_prompt",lambda x:x["selected_original_train_source_identities"]["87"].__setitem__(
              "original_public_prompt_sha256","a"*64)),
          ("wrong_read",lambda x:x["actual_native_public_read_only_tool_receipts"][0].__setitem__(
              "actual_selected_original_public_read_tool","delete_room")),
          ("fake_success",lambda x:x["actual_native_public_read_only_tool_receipts"][0].__setitem__(
              "actual_original_source_public_tool_result","source_failed_or_unparseable")),
          ("source_reply_forged",lambda x:x["actual_native_public_read_only_tool_receipts"][0].__setitem__(
              "actual_selected_original_public_reply_redacted","{'success':True,'data':[1]}")),
          ("secret_projection",lambda x:x["actual_native_public_read_only_tool_receipts"][0].__setitem__(
              "actual_selected_original_public_reply_redacted","{'success':True,'data':{'hashed_password':'mock'}}")),
          ("invented_noop",lambda x:x.__setitem__(
              "original_natural_same_conditional_rule_action_and_noaction_claim","PROVED")),
          ("bad_elapsed",lambda x:x["actual_native_public_read_only_tool_receipts"][0].__setitem__(
              "physical_native_source_container_wall_seconds",-1)),
          ("no_source_worker_privacy",lambda x:x["actual_native_public_read_only_tool_receipts"][0].__setitem__(
              "original_native_source_private_final_state_discarded",False)),
          ("extra_unaccounted_tool",lambda x:x["actual_native_public_read_only_tool_receipts"].append(
              copy.deepcopy(x["actual_native_public_read_only_tool_receipts"][0]))),
          ("missing_family",lambda x:x["full_original_train_census"][
              "all_30_original_train_family_public_only_census"].pop()),
        ]
        for tag,fn in mutant_cases:
            with self.subTest(tag=tag):
                data=fixture();fn(data)
                with self.assertRaises(ValueError):adjudicate(data,protocol_path=SPEC)

if __name__=="__main__":
    unittest.main()
