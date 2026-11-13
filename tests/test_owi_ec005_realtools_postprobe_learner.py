#!/usr/bin/env python3
"""Adversarial post-probe source control and chosen-scalar bandit invariants."""
from __future__ import annotations
import random,sys,unittest,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_postprobe_variants import with_status
from owi_ec005_realtools_postprobe_learner import (
    read_observed_status, PostProbeBandit, public_preflight, STATUS, UNKNOWN,
    FORCED_ROUNDS
)
from owi_ec005_realtools_intake import DatasetBoundaryError
from test_owi_ec005_realtools_heterogeneous_trial import public

def fixture():
    return {"class_code":"class Fake: pass","class_name":"Fake",
            "initial_state":{"users":{"USR002":{"_id":"USR002",
                       "account_status":"suspended","preferenc":[]},
                      "USR999":{"_id":"USR999",
                       "account_status":"closed"}},
                       "sleep_logs":[{"_id":"unchanged"}],
                       "init_config":{"enabled":True}},
            "tools":[{"type":"function","function":{"name":"check_user_account_status"}}]}

class PostProbeTests(unittest.TestCase):
    def test_only_one_controlled_field_changes(self):
        original=fixture()
        for variant in ("suspended","active","closed"):
            new=with_status(original,variant)
            self.assertEqual(original["initial_state"]["users"]["USR002"]["account_status"],
                             "suspended")
            self.assertEqual(new["initial_state"]["users"]["USR002"]["account_status"],
                             variant)
            self.assertEqual(original["class_code"],new["class_code"])
            self.assertEqual(original["tools"],new["tools"])
            self.assertEqual(original["initial_state"]["sleep_logs"],new["initial_state"]["sleep_logs"])
            self.assertEqual(original["initial_state"]["users"]["USR999"],
                             new["initial_state"]["users"]["USR999"])
        with self.assertRaises(DatasetBoundaryError):
            with_status(original,"compromised")
        wrong=fixture()
        wrong["initial_state"]["users"]["USR002"]["_id"]="other"
        with self.assertRaises(DatasetBoundaryError):
            with_status(wrong,"active")

    def test_public_probe_reply_only_exposes_explicit_target(self):
        for status in STATUS+(UNKNOWN,):
            r={"kind":"observation","tool":"check_user_account_status",
               "ok":True,"truncated":False,
               "content":str({"success":True,"data":{
                   "_id":"USR002","account_status":status}})}
            self.assertEqual(read_observed_status(r),status)
            r["content"]=str({"success":True,"data":{
                "_id":"OTHER","account_status":status}})
            self.assertIsNone(read_observed_status(r))
        self.assertIsNone(read_observed_status({
            "kind":"observation","tool":"check_user_account_status",
            "ok":True,"truncated":True,"content":"malformed"}))
        self.assertIsNone(read_observed_status({
            "kind":"observation","tool":"evil_source_tool",
            "ok":True,"content":"__import__('os').system('true')"}))

    def test_full_public_task_accepted_but_privileged_fields_refused(self):
        p=public(2)
        self.assertTrue(public_preflight(p))
        with self.assertRaises(ValueError):
            public_preflight({**p,"verifier":"SECRET_CHECKER"})
        with self.assertRaises(ValueError):
            public_preflight({**p,"initial_state":{"account_status":"active"}})

    def test_two_context_forced_exploration_and_exact_propensity(self):
        b=PostProbeBandit()
        rng=random.Random(9)
        for k in STATUS:
            seq=[]
            for t in range(2*FORCED_ROUNDS):
                action,prob,phase=b.choice(k,rng)
                self.assertEqual(phase,"context_specific_without_replacement")
                self.assertEqual(prob,.5 if t%2==0 else 1.)
                b.update(k,action,float(ACTIONS_INDEX[action]))
                seq.append(action)
            for n in range(FORCED_ROUNDS):
                self.assertEqual(set(seq[2*n:2*n+2]),{"stop","update"})
        self.assertEqual(b.count["suspended"],[FORCED_ROUNDS]*2)
        self.assertEqual(b.count["active"],[FORCED_ROUNDS]*2)
        self.assertEqual(b.choice("closed",rng),("stop",1.,"unsupported_fail_closed"))

    def test_learner_identifies_realized_choice_and_context_flip(self):
        b=PostProbeBandit()
        for status,stop,update in [("suspended",.38,.45),("active",.45,.44)]:
            for _ in range(4):
                b.update(status,"stop",stop)
                b.update(status,"update",update)
        self.assertEqual(b.evidence()["suspended"]["frozen_action"],"update")
        self.assertEqual(b.evidence()["active"]["frozen_action"],"stop")
        self.assertNotEqual(b.evidence()["suspended"]["frozen_action"],
                            b.evidence()["active"]["frozen_action"])
        self.assertIn(b.pooled_best(),(0,1))
        rng=random.Random(23)
        seen=set()
        for _ in range(100):
            act,p,phase=b.choice("suspended",rng)
            self.assertEqual(phase,"epsilon_greedy")
            self.assertIn(act,("stop","update"))
            self.assertAlmostEqual(p,.9 if act=="update" else .1)
            seen.add(act)
        self.assertEqual(seen,{"stop","update"})

ACTIONS_INDEX={"stop":0,"update":1}
if __name__=="__main__":
    unittest.main()
