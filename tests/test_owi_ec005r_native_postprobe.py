#!/usr/bin/env python3
"""Hostile source-native option/heldout gate vectors; fixtures are NOT episodes."""
from __future__ import annotations
import collections,copy,json,random,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005r_native_postprobe_episode import (
    CONTRACT as EP_CONTRACT,TERMINAL_EXPECT,EXPECTED_TOOL_NAMES,
    SOURCE_SHA,PRICE,FIRST_TOOLS)
from owi_ec005r_native_postprobe_train import (
    ChosenOptionValues,SEEDS,MODES,OPTIONS,CONTROLS,
    FEATURES,TRAIN_PER_MODE,EVAL_PER_SEED,actor_feature,schedule,
    verify_frozen_manifest,baseline_script_choice)
from owi_ec005r_native_postprobe_gate import check_episode
from owi_ec005_realtools_heterogeneous_trial import Policy

def public(row):
    text={
        0:"User: Alice Chan (USR001). Identify and cancel only the subscription "
          "tied to the product PureView Daily Lens (monthly plan).",
        2:"For user USR002 (Lucas Viteri), reactivate: change account_status "
          "from “suspended” to “active”.",
        3:"Create a new dietary restriction entity with restriction_id DR5:\n"
          "- name: Low-Carb\n- description: Limits high-carbohydrate grains and sugars.\n"
          "- tag: low-carb\n",
    }[row]
    schemas={
      "list_user_subscriptions":["user_id"],
      "get_product_by_id":["product_id"],
      "check_subscription_links":["subscription_id"],
      "cancel_subscription":["subscription_id"],
      "invalidate_future_payments":["subscription_id"],
      "halt_scheduled_shipments":["subscription_id"],
      "modify_subscription_details":["subscription_id","updates"],
      "check_user_account_status":["user_id"],
      "update_user_account_status":["user_id","new_status"],
      "get_dietary_restriction_by_id":["restriction_id"],
      "create_dietary_restriction":["restriction_id","name","description","tag"],
    }
    return {"messages":[{"role":"user","content":text}],
            "tools":[{"name":name,"parameters":{
                "type":"object","required":needed}} for name,needed in schemas.items()]}

def fake_ep(row=2,arm="probe",post="continue",mode="actual_public_reply"):
    key=(arm if arm!="probe" else "probe_"+post)
    tools=EXPECTED_TOOL_NAMES[row][key]
    n={0:4,2:13,3:21}[row]
    reward=round(TERMINAL_EXPECT[row][key],4)
    passed=round(TERMINAL_EXPECT[row][key]*n)
    signal="followup_available" if arm=="probe" else None
    feature=(signal if mode=="actual_public_reply" else
             "blind" if mode=="zero_information" else
             "no_followup") if arm=="probe" else None
    return {
        "contract":EP_CONTRACT,"source_family_row_audit_only":row,
        "original_source_class_sha256_audit_only":"a"*64,
        "original_public_task_unchanged":True,
        "original_source_initial_state_unchanged":True,
        "original_native_checker_unchanged":True,
        "source_original_full_corpus_sha256":SOURCE_SHA,
        "selected_first_stage_source_arm":arm,
        "original_public_first_probe_tool":FIRST_TOOLS[row] if arm=="probe" else None,
        "actual_public_postprobe_signal_audit_only":signal,
        "scripted_public_followup_queue_nonempty_audit_only":(
            True if arm=="probe" else None),
        "feature_supplied_to_learned_option_actor":feature,
        "selected_postprobe_option":post if arm=="probe" else None,
        "selected_postprobe_action_propensity":1. if arm=="probe" else None,
        "original_source_native_private_reward":reward,
        "original_native_checks_passed":passed,
        "original_native_checks_total":n,
        "chosen_actual_call_cost":round(PRICE*len(tools),6),
        "chosen_actual_terminal_utility":round(reward-PRICE*len(tools),6),
        "chosen_actual_original_public_tool_calls":len(tools),
        "chosen_real_public_tool_receipts":[{
            "tool":k,"public_reply_sha256":"b"*64,"tool_seconds":.0005,
            "worker_tool_succeeded":True} for k in tools],
        "source_worker_wall_seconds":.4,
        "original_native_checker_wall_seconds":.02,
        "checker_total_wall_seconds_with_replays":.024,
        "checker_exact_input_timeout_replays":0,
        "source_worker_peak_rss_kib":12000,
        "private_source_state_or_checker_entered_actor":False,
        "unchosen_source_action_reward_entered_actor":False,
        "family_id_entered_actor_as_feature":False,
        "scripted_public_action_planner_not_learned":True,
    }

class NativeHeldoutFalseProofTests(unittest.TestCase):
    def test_unchanged_original_public_affordance_and_strong_script(self):
        self.assertEqual(baseline_script_choice(0,public(0)),"probe")
        self.assertEqual(baseline_script_choice(2,public(2)),"direct")
        self.assertEqual(baseline_script_choice(3,public(3)),"direct")
        self.assertEqual(Policy(0,public(0),"probe").next_action()["tool"],
                         FIRST_TOOLS[0])
    def test_preregistered_balanced_training_and_exact_source_manifest(self):
        p=Path(__file__).resolve().parents[1]/(
            "governance/research/OWI_EC005R_NATIVE_POSTPROBE_HOLDOUT_V1.json")
        self.assertEqual(len(verify_frozen_manifest(p)),64)
        self.assertEqual(EVAL_PER_SEED,27)
        self.assertEqual(len(CONTROLS),6)
        for seed in SEEDS:
            s=schedule(seed)
            self.assertEqual(len(s),TRAIN_PER_MODE)
            self.assertEqual(collections.Counter(s),{0:24,2:24})
            self.assertNotIn(3,s)
        x=json.loads(p.read_text())
        for field,edited in [
            ("heldout",lambda z:z["source"].__setitem__(
                "heldout_distinct_train_partition_family",2)),
            ("source",lambda z:z["source"].__setitem__("full_sha256","0"*64)),
            ("strong_script",lambda z:z["evaluation"].__setitem__(
                "fixed_controls",["always_stop_after_probe"])),
            ("seed",lambda z:z["training"].__setitem__("seeds",[1])),
            ("new_mask",lambda z:z["source"].__setitem__(
                "independent_train_rows",[0,2,3])),
        ]:
            with self.subTest(field=field),tempfile.TemporaryDirectory() as t:
                mutant=copy.deepcopy(x);edited(mutant)
                q=Path(t)/"mutant.json";q.write_text(json.dumps(mutant))
                with self.assertRaises(ValueError):
                    verify_frozen_manifest(q)
    def test_postprobe_actor_only_uses_selected_native_scalar(self):
        a=ChosenOptionValues()
        rng=random.Random(11)
        for i in range(4):
            opt,p=a.select("followup_available",rng)
            self.assertGreater(p,0)
            self.assertIn(opt,OPTIONS)
            a.update("followup_available",opt,
                     .48 if opt=="continue" else .24)
        self.assertEqual(a.best("followup_available"),"continue")
        self.assertEqual(a.updates,4)
        self.assertEqual(a.count["followup_available"],[2,2])
        self.assertEqual(actor_feature("followup_available",
                  "zero_information",rng),"blind")
        self.assertEqual(actor_feature("followup_available",
                  "actual_public_reply",rng),"followup_available")
        with self.assertRaises(ValueError):
            a.update("private_source_family_id","continue",.5)
        with self.assertRaises(ValueError):
            a.update("followup_available","stop",float("nan"))
    def test_all_original_native_source_score_and_trace_vectors(self):
        for row in (0,2,3):
            for arm in ("probe","direct","stop"):
                for after in ("continue","stop") if arm=="probe" else (None,):
                    for mode in MODES if arm=="probe" else ("actual_public_reply",):
                        with self.subTest(row=row,arm=arm,after=after,mode=mode):
                            obj=fake_ep(row,arm,after,mode)
                            self.assertEqual(check_episode(obj,row,mode),
                                             obj["chosen_actual_terminal_utility"])
    def test_reject_malformed_native_private_reward_and_fake_source_observation(self):
        ep=fake_ep()
        hostile=[
            ("new_score",lambda x:x.__setitem__(
                "original_source_native_private_reward",-.2)),
            ("fabricated_checker",lambda x:x.__setitem__(
                "original_native_checks_passed",1)),
            ("private_leak",lambda x:x.__setitem__(
                "private_source_state_or_checker_entered_actor",True)),
            ("counterfactual_leak",lambda x:x.__setitem__(
                "unchosen_source_action_reward_entered_actor",True)),
            ("family_id_feature",lambda x:x.__setitem__(
                "family_id_entered_actor_as_feature",True)),
            ("public_task_modified",lambda x:x.__setitem__(
                "original_public_task_unchanged",False)),
            ("missing_actual_probe",lambda x:x["chosen_real_public_tool_receipts"].pop(0)),
            ("wrong_original_tool",lambda x:x["chosen_real_public_tool_receipts"][0].__setitem__(
                "tool","secret_checker")),
            ("free_added_cost",lambda x:x.__setitem__("chosen_actual_call_cost",0)),
            ("fake_native_reward",lambda x:x.__setitem__(
                "chosen_actual_terminal_utility",.9)),
            ("unbounded_native_checker_retry",lambda x:x.__setitem__(
                "checker_exact_input_timeout_replays",4)),
            ("free_native_checker_retry",lambda x:x.__setitem__(
                "checker_exact_input_timeout_replays",1)),
            ("wrong_original_public_task_source",lambda x:x.__setitem__(
                "source_original_full_corpus_sha256","0"*64)),
        ]
        for name,mutator in hostile:
            obj=copy.deepcopy(ep);mutator(obj)
            with self.subTest(name=name),self.assertRaises(ValueError):
                check_episode(obj,2,"actual_public_reply")
        masked=copy.deepcopy(ep)
        masked["feature_supplied_to_learned_option_actor"]="followup_available"
        with self.assertRaises(ValueError):
            check_episode(masked,2,"zero_information")

if __name__=="__main__":
    unittest.main()
