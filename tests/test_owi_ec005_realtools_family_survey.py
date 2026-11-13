#!/usr/bin/env python3
"""Adversarial tests for public-only, held-out environment family survey."""
import hashlib
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_family_survey import audit_source,public_family_survey
from owi_ec005_realtools_intake import DatasetBoundaryError,REPO,FILE
from owi_ec005_realtools_split import partition
from owi_ec005_realtools_family_prepare import build


def fixture():
    rows=[]
    for i in range(8):
        row={"prompt":[{"role":"system","content":"Fixture system."},
                       {"role":"user","content":"Private target? Use public tool "+str(i)}],
             "extra_info":{"environment":{
                 "env_id":"fixture-env-"+str(i),
                 "class_code":"class Fixture"+str(i)+":\n    pass\n",
                 "tools":[{"type":"function","function":{"name":"list_records",
                         "parameters":{"type":"object"}}}],
                 "initial_state":{"secret":"DO_NOT_SHOW_"+str(i)}},
                 "verifier":{"kind":"checklist_func",
                     "checklist":[{"check_func":"SECRET_CHECK_"+str(i)}]},
                 "rsd_skill":"SECRET_SKILL_"+str(i)}}
        rows.append(row)
    return rows


class TestPublicHeterogeneousSurvey(unittest.TestCase):
    def test_no_test_prompts_exported_and_all_three_splits_are_present(self):
        rows=fixture()
        report=public_family_survey(rows,example_limit=1)
        self.assertEqual(report["train_families"],4)
        self.assertEqual(report["dev_families"],1)
        self.assertEqual(report["sealed_test_families"],3)
        self.assertFalse(report["test_prompts_or_tools_exposed"])
        self.assertTrue(report["test_public_prompt_fingerprints_hashed_for_deduplication"])
        self.assertEqual(set(g["partition"] for g in report["families"]),
                         {"train","dev"})
        exported=json.dumps(report)
        self.assertNotIn("SECRET_CHECK_",exported)
        self.assertNotIn("DO_NOT_SHOW_",exported)
        self.assertNotIn("SECRET_SKILL_",exported)
        train_dev_indices={g["representatives"][0]["row_index"]
                           for g in report["families"]}
        for i in set(range(8))-train_dev_indices:
            self.assertNotIn("Use public tool "+str(i),exported)

    def test_full_source_byte_lock_fail_closed(self):
        rows=fixture()
        lines=[(json.dumps(x,sort_keys=True)+"\n").encode() for x in rows]
        raw=b"".join(lines)
        lock={"repository":REPO,"filename":FILE,
              "revision":"offline",
              "sha256":hashlib.sha256(raw).hexdigest(),
              "size_bytes":len(raw),"observed_tasks":len(rows)}
        self.assertEqual(len(audit_source(lock,lines=lines)),len(rows))
        with self.assertRaises(DatasetBoundaryError):
            audit_source({**lock,"sha256":"0"*64},lines=lines)
        with self.assertRaises(DatasetBoundaryError):
            audit_source({**lock,"observed_tasks":9},lines=lines)

    def test_private_bundle_rejected_on_heldout_and_separate_on_train(self):
        rows=fixture()
        for i,row in enumerate(rows):
            row["extra_info"]["environment"]["class_name"]="Fixture"+str(i)
        p=partition(rows,seed=4611)
        index=p["partitions"]["train"][0]["row_index"]
        hidden=p["partitions"]["test"][0]["row_index"]
        selected=build(rows,[index])
        self.assertEqual(len(selected),1)
        idx,fam,public,environment,private=selected[0]
        self.assertEqual(idx,index)
        self.assertEqual(set(environment),{
            "class_code","class_name","initial_state","tools"})
        self.assertEqual(set(private),{"verifier"})
        self.assertNotIn("SECRET_CHECK",json.dumps(public))
        self.assertNotIn("DO_NOT_SHOW",json.dumps(public))
        self.assertNotIn("SECRET_SKILL",json.dumps(public))
        with self.assertRaises(DatasetBoundaryError):
            build(rows,[hidden])
        with self.assertRaises(DatasetBoundaryError):
            build(rows,[index,index])

    def test_example_bounds(self):
        with self.assertRaises(DatasetBoundaryError):
            public_family_survey(fixture(),example_limit=4)


if __name__=="__main__":
    unittest.main()
