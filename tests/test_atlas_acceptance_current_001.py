"""Fail-closed chapter acceptance and role provenance (candidate-only)."""
import hashlib,json,subprocess,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'governance/editorial/v0.1.1/CHAPTER_ACCEPTANCE_EVIDENCE_080.json').read_text())
P=json.loads((R/'governance/editorial/v0.1.1/P01_PRODUCER_001.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True).strip()
class EditorialAcceptance(unittest.TestCase):
    def test_exactly_80_and_two_accepted(self):
        self.assertEqual(len(D['chapters']),80)
        self.assertEqual(len({r['chapter_id'] for r in D['chapters']}),80)
        self.assertEqual(sum(r['state']=='ACCEPTED' for r in D['chapters']),D['accepted_count'])
        self.assertEqual(D['accepted_count'],2)
        self.assertEqual([x['chapter_id'] for x in D['chapters'] if x['state']=='ACCEPTED'],['ATLAS-CH-MAP-001','ATLAS-CH-EVIDENCE-001'])
    def test_source_hashes_exact(self):
        for row in D['chapters']:
            with self.subTest(chapter=row['chapter_id']):
                self.assertEqual(git('hash-object',row['source_path']),row['source_blob_sha1'])
    def test_accepted_source_producer_critic_renderer(self):
        accepted=[r for r in D['chapters'] if r['state']=='ACCEPTED']
        self.assertEqual(len(accepted),2)
        for r in accepted:
            p=next(x for x in P['rows'] if x['chapter_id']==r['chapter_id'])
            a=r['accepted_evidence']
            with self.subTest(chapter=r['chapter_id']):
                self.assertEqual(a['head'],D['candidate_head'])
                self.assertEqual(a['source_blob_sha1'],p['source_blob_sha1'])
                self.assertNotEqual(a['producer_run'],a['critic_run'])
                self.assertEqual(a['pdf_sha256'],P['pdf_sha256'])
                self.assertEqual(a['html_sha256'],P['html_sha256'])
                self.assertEqual(a['pdf_pages'],p['pdf_pages'])
                self.assertTrue(a['producer_url'].startswith('https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/'))
                self.assertTrue(a['critic_url'].startswith('https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/'))
                self.assertFalse(a['mathematical_certification'])
                self.assertFalse(a['public_release_authorization'])
                self.assertFalse(p['findings'])
                if r['chapter_id']=='ATLAS-CH-EVIDENCE-001':
                    self.assertEqual(a['producer_run'],p['producer_run_id'])
                    self.assertIn('issues/414#issuecomment-',a['critic_url'])
                else:
                    self.assertEqual(a['chapter_producer_run'],p['producer_run_id'])
                    self.assertIn('issues/418#issuecomment-',a['critic_url'])
                    doc=R/r['documentary_packet_path']
                    self.assertEqual(git('hash-object',str(doc)),a['documentary_blob_sha1'])
                    self.assertEqual(sha(doc),a['documentary_sha256'])
                    self.assertEqual(a['documentary_blob_sha1'],'f7ea7a6912465ab2160e6f84645913e7eef2df2a')
                    self.assertNotEqual(a['producer_run'],a['chapter_producer_run'])
    def test_map_critic_signoff_is_not_old_revise(self):
        r=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-MAP-001')
        a=r['accepted_evidence']
        self.assertEqual(a['prior_critic_revise_run'],'a0414e5cf0f04b2fb2c3d0e91a814e76')
        self.assertEqual(a['critic_run'],'a0418e5cf0f04b2fb2c3d0e91a814e78')
        self.assertEqual(r['resolved_findings'][0]['disposition'],'RESOLVED')
    def test_no_source_change_since_real_render(self):
        for folder,reviewed_tree in D['reviewed_source_tree_ids'].items():
            with self.subTest(source_tree=folder):
                self.assertEqual(git('rev-parse','HEAD:'+folder),reviewed_tree)
    def test_repair_required_not_inflated(self):
        for tag in ('THESIS','OBJECTS'):
            x=next(r for r in D['chapters'] if r['chapter_id']==f'ATLAS-CH-{tag}-001')
            self.assertEqual(x['state'],'UNVERIFIED')
            self.assertTrue(x['unresolved'])
if __name__=='__main__':unittest.main()
