"""Pure admission tests for Atlas operational RETURNED projection."""
import copy
import importlib.util
import unittest
from pathlib import Path

p=Path(__file__).resolve().parents[1]/"ci/atlas_direct_return_projector.py"
spec=importlib.util.spec_from_file_location("atlas_direct_return_projector",p)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

ASSIGN="ATLAS-EDITORIAL-P02-B"
HEAD="ff3ed0972e3637350c9140eaa85de7169fe6ca76"

def fixture():
    return {
       "action":"created",
       "repository":{"full_name":"grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS"},
       "issue":{"number":327,"state":"open","title":"ATLAS-EDITORIAL-P02-B — agent chapter review",
                "body":"GCL-ATLAS-EDITORIAL-AGENT/1\nASSIGNMENT_ID: ATLAS-EDITORIAL-P02-B\n",
                "labels":[{"name":"gcl-pickup:direct-editorial"}]},
       "comment":{"id":12345,"user":{"login":"reviewer42"},
                  "body":f"RESULT/1\nassignment_id: {ASSIGN}\nreviewer_identity: reviewer42 (independent reviewer)\ninput_head: {HEAD}\nstatus: partial\n\nchapter_findings:\n  Proof scope note.\n"}
       },[
         {"issue_field_name":"GCL Campaign","value":"ATLAS-EDITORIAL-REVIEW-001"},
         {"issue_field_name":"GCL State","single_select_option":{"name":"AVAILABLE"}},
       ]
class ProjectionTests(unittest.TestCase):
    def test_partial(self):
        e,f=fixture()
        r=mod.evaluate(e,f)
        self.assertTrue(r["project"])
        self.assertEqual(r["state_to_write"],"RETURNED")
        self.assertFalse(r["editorial_accepted"])
        self.assertFalse(r["independent_review_approved"])
    def test_complete_still_not_accepted(self):
        e,f=fixture();e["comment"]["body"]=e["comment"]["body"].replace("status: partial","status: completed")
        r=mod.evaluate(e,f)
        self.assertEqual(r["self_reported_status"],"completed")
        self.assertFalse(r["editorial_accepted"])
    def test_spoofed_identity(self):
        e,f=fixture();e["comment"]["user"]["login"]="another-user"
        self.assertEqual(mod.evaluate(e,f)["reason"],"authenticated_actor_mismatch")
    def test_agent_review_same_authenticated_login(self):
        e,f=fixture()
        e["comment"]["body"] = e["comment"]["body"].replace(
            "reviewer_identity: reviewer42 (independent reviewer)",
            "github_actor: reviewer42\nreviewer_identity: atlas-math-reviewer\nagent_role: MATH_CHECK\nagent_run_id: independent-pass-02",
        )
        result=mod.evaluate(e,f)
        self.assertTrue(result["project"])
        self.assertEqual(result["authenticated_actor"],"reviewer42")
        self.assertEqual(result["agent_role"],"MATH_CHECK")
        self.assertEqual(result["agent_run_id"],"independent-pass-02")
        self.assertFalse(result["independent_review_approved"])

    def test_explicit_transport_actor_mismatch(self):
        e,f=fixture()
        e["comment"]["body"]=e["comment"]["body"].replace(
            "reviewer_identity: reviewer42 (independent reviewer)",
            "github_actor: otheruser\nreviewer_identity: atlas-reviewer",
        )
        self.assertEqual(mod.evaluate(e,f)["reason"],"authenticated_actor_mismatch")

    def test_wrong_assignment(self):
        e,f=fixture();e["comment"]["body"]=e["comment"]["body"].replace(ASSIGN,"ATLAS-EDITORIAL-P99")
        self.assertEqual(mod.evaluate(e,f)["reason"],"wrong_assignment")
    def test_other_campaign(self):
        e,f=fixture();f[0]["value"]="ERDOS-RECON"
        self.assertEqual(mod.evaluate(e,f)["reason"],"not_atlas_campaign")
    def test_unlabeled_issue(self):
        e,f=fixture();e["issue"]["labels"]=[]
        self.assertEqual(mod.evaluate(e,f)["reason"],"not_direct_editorial")
    def test_not_result(self):
        e,f=fixture();e["comment"]["body"]="please review"
        self.assertEqual(mod.evaluate(e,f)["reason"],"not_result")
    def test_invalid_head(self):
        e,f=fixture();e["comment"]["body"]=e["comment"]["body"].replace(HEAD,"main")
        self.assertEqual(mod.evaluate(e,f)["reason"],"invalid_source_head")
    def test_duplicate_is_idempotent(self):
        e,f=fixture();f[1]["single_select_option"]["name"]="RETURNED"
        self.assertEqual(mod.evaluate(e,f)["reason"],"already_returned")
    def test_blocked_state_not_overridden(self):
        e,f=fixture();f[1]["single_select_option"]["name"]="BLOCKED"
        self.assertEqual(mod.evaluate(e,f)["reason"],"state_not_available")
    def test_not_pr(self):
        e,f=fixture();e["issue"]["pull_request"]={}
        self.assertEqual(mod.evaluate(e,f)["reason"],"not_open_issue")
    def test_title_fallback_for_figures(self):
        e,f=fixture()
        e["issue"]["title"]="EDITORIAL-FIGURE-002 — graphical audit"
        e["issue"]["body"]="Parent #314 figure review"
        e["comment"]["body"]=e["comment"]["body"].replace(ASSIGN,"EDITORIAL-FIGURE-002")
        self.assertTrue(mod.evaluate(e,f)["project"])
    def test_malformed_status(self):
        e,f=fixture();e["comment"]["body"]=e["comment"]["body"].replace("status: partial","status: certified")
        self.assertEqual(mod.evaluate(e,f)["reason"],"invalid_result_status")

if __name__=="__main__":
    unittest.main()
