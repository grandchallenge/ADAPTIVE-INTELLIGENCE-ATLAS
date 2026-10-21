"""Offline hostile checks on the exact 80-row evidence; no GitHub mutations."""
import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"ci"))
from atlas_acceptance_evidence import check
class Evidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d=json.loads((ROOT/"governance/editorial/v0.1.1/CHAPTER_ACCEPTANCE_EVIDENCE_080.json").read_text())
        cls.c=json.loads((ROOT/"governance/CHAPTER_LEDGER.yaml").read_text())
        chapters=cls.d["chapters"]
        cls.queue={"work_packages":[{"issue_number":n,"chapter_ids":[r["chapter_id"] for r in chapters if r["review_issue"]==n]} for n in range(326,346)]}
        cls.tree={"tree":[{"type":"blob","path":r["source_path"],"sha":r["source_blob_sha1"]} for r in chapters]}
    def test_all_80_unaccepted(self):
        self.assertTrue(check(self.d,self.c,self.queue,self.tree))
        self.assertEqual(len(self.d["chapters"]),80)
        self.assertEqual(sum(x["state"]=="ACCEPTED" for x in self.d["chapters"]),0)
        self.assertEqual(self.d["issue_inventory"]["closed_returned"],28)
    def test_fabricated_acceptance_rejected(self):
        d=copy.deepcopy(self.d)
        d["chapters"][0]["state"]="ACCEPTED"
        with self.assertRaisesRegex(ValueError,"fabricated"):check(d,self.c,self.queue,self.tree)
    def test_stale_and_same_role_rejected(self):
        d=copy.deepcopy(self.d);d["chapters"][0]["state"]="ACCEPTED"
        d["chapters"][0]["accepted_evidence"]={"head":"0"*40,"producer_run":"same","critic_run":"same","pdf_sha256":"a","html_sha256":"b","critic_url":"https://example.org"}
        with self.assertRaisesRegex(ValueError,"stale"):check(d,self.c,self.queue,self.tree)
    def test_source_drift_rejected(self):
        d=copy.deepcopy(self.d);d["chapters"][0]["source_blob_sha1"]="0"*40
        with self.assertRaisesRegex(ValueError,"source blob"):check(d,self.c,self.queue,self.tree)
    def test_missing_chapter_rejected(self):
        d=copy.deepcopy(self.d);d["chapters"].pop()
        with self.assertRaisesRegex(ValueError,"incomplete"):check(d,self.c,self.queue,self.tree)
    def test_duplicate_assignment_rejected(self):
        q=copy.deepcopy(self.queue);q["work_packages"][0]["chapter_ids"].append(q["work_packages"][1]["chapter_ids"][0])
        with self.assertRaisesRegex(ValueError,"assignment coverage"):check(self.d,self.c,q,self.tree)
if __name__=="__main__":unittest.main()
