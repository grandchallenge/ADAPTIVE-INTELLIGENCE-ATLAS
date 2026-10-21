"""Adversarial replay: no new Atlas RETURNED projection without valid global grant."""
import copy,json,unittest
from pathlib import Path
from test_atlas_direct_return_projector import fixture,mod,HEAD
R="grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS";RUN="1"*32
def setup():
    e,f=fixture();e["issue"]["number"]=407
    e["comment"]["created_at"]="2026-10-21T08:30:00Z"
    e["comment"]["body"]=e["comment"]["body"].replace("status: partial",f"agent_run_id: {RUN}\nstatus: partial")
    req={"id":1,"created_at":"2026-10-21T08:00:00Z","user":{"login":"reviewer42"},
        "body":f"EDITORIAL-START/1\nrepository: {R}\nissue: 407\nrun_id: {RUN}\nsource_head: {HEAD}\n"}
    dec={"request_id":1,"outcome":"GRANTED","op":"START","repo":R,"issue":407,"run":RUN,
         "worker":"reviewer42","source_head":HEAD,"expires_at":"2026-10-21T12:00:00+00:00",
         "reason":"CAPACITY_ADMITTED"}
    bot={"id":2,"created_at":"2026-10-21T08:01:00Z","user":{"login":"github-actions[bot]"},
         "body":"GCL-EDITORIAL-DECISION/1\n"+json.dumps(dec)}
    return e,f,[req,bot]
def checked(e,f,h):return mod.evaluate(e,f,grant_history=h,require_grant=True)
class Tests(unittest.TestCase):
    def test_positive_but_not_approved(self):
        e,f,h=setup();d=checked(e,f,h)
        self.assertTrue(d["project"]);self.assertFalse(d["editorial_accepted"])
    def test_no_grant(self):
        e,f,h=setup()
        self.assertEqual(checked(e,f,[])["reason"],"grant_no_authenticated_grant")
    def test_expired(self):
        e,f,h=setup();e["comment"]["created_at"]="2026-10-21T13:00:00Z"
        self.assertEqual(checked(e,f,h)["reason"],"grant_no_active_grant_at_return")
    def test_changed_head(self):
        e,f,h=setup();e["comment"]["body"]=e["comment"]["body"].replace(HEAD,"f"*40)
        self.assertEqual(checked(e,f,h)["reason"],"grant_source_head_drift")
    def test_spoofed_bot(self):
        e,f,h=setup();h[1]["user"]["login"]="forger"
        self.assertEqual(checked(e,f,h)["reason"],"grant_no_authenticated_grant")
    def test_malformed_history(self):
        e,f,h=setup();h.append(h[0])
        self.assertEqual(checked(e,f,h)["reason"],"grant_grant_history_invalid_fail_closed")
    def test_end_invalidates_grant(self):
        e,f,h=setup()
        req={"id":3,"created_at":"2026-10-21T08:10:00Z","user":{"login":"reviewer42"},
             "body":f"EDITORIAL-END/1\nrepository: {R}\nissue: 407\nrun_id: {RUN}\n"}
        dec={"request_id":3,"outcome":"ENDED","op":"END","repo":R,"issue":407,"run":RUN,
             "worker":"reviewer42","source_head":None,"expires_at":"2026-10-21T12:00:00+00:00",
             "reason":"RELEASED"}
        h.extend([req,{"id":4,"created_at":"2026-10-21T08:11:00Z",
             "user":{"login":"github-actions[bot]"},"body":"GCL-EDITORIAL-DECISION/1\n"+json.dumps(dec)}])
        self.assertEqual(checked(e,f,h)["reason"],"grant_grant_ended_before_result")
    def test_legacy_not_rejected(self):
        e,f,h=setup();e["comment"]["created_at"]="2026-10-11T08:00:00Z"
        self.assertTrue(checked(e,f,[])["project"])
    def test_workflows_gate_both_paths(self):
        root=Path(__file__).resolve().parents[1]
        for n in ("atlas-direct-editorial-returns.yml","atlas-direct-editorial-return-replay.yml"):
            s=(root/".github/workflows"/n).read_text()
            self.assertIn("issues/1096/comments",s);self.assertIn("--grant-history",s)
if __name__=="__main__":unittest.main()
