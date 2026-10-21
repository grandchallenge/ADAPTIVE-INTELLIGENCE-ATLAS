"""Fail-closed chapter acceptance and role provenance (candidate-only)."""
import hashlib,json,subprocess,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'governance/editorial/v0.1.1/CHAPTER_ACCEPTANCE_EVIDENCE_080.json').read_text())
P=json.loads((R/'governance/editorial/v0.1.1/P01_PRODUCER_001.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True).strip()
class EditorialAcceptance(unittest.TestCase):
    def test_exactly_80_and_one_accepted(self):
        self.assertEqual(len(D['chapters']),80)
        self.assertEqual(len({r['chapter_id'] for r in D['chapters']}),80)
        self.assertEqual(sum(r['state']=='ACCEPTED' for r in D['chapters']),D['accepted_count'])
        self.assertEqual(D['accepted_count'],1)
        self.assertEqual([x['chapter_id'] for x in D['chapters'] if x['state']=='ACCEPTED'],['ATLAS-CH-EVIDENCE-001'])
    def test_source_hashes_exact(self):
        for row in D['chapters']:
            with self.subTest(chapter=row['chapter_id']):
                self.assertEqual(git('hash-object',row['source_path']),row['source_blob_sha1'])
    def test_accepted_source_producer_critic_renderer(self):
        r=next(x for x in D['chapters'] if x['state']=='ACCEPTED')
        p=next(x for x in P['rows'] if x['chapter_id']==r['chapter_id'])
        a=r['accepted_evidence']
        self.assertEqual(a['head'],D['candidate_head'])
        self.assertEqual(a['source_blob_sha1'],p['source_blob_sha1'])
        self.assertNotEqual(a['producer_run'],a['critic_run'])
        self.assertEqual(a['producer_run'],p['producer_run_id'])
        self.assertEqual(a['pdf_sha256'],P['pdf_sha256'])
        self.assertEqual(a['html_sha256'],P['html_sha256'])
        self.assertEqual(a['pdf_pages'],p['pdf_pages'])
        self.assertTrue(a['producer_url'].startswith('https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/412#issuecomment-'))
        self.assertTrue(a['critic_url'].startswith('https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/414#issuecomment-'))
        self.assertFalse(a['mathematical_certification'])
        self.assertFalse(a['public_release_authorization'])
        self.assertFalse(p['findings'])
    def test_no_source_change_since_real_render(self):
        self.assertFalse(git('diff','--name-only',D['candidate_head'],'HEAD','--','manuscript/','sources/','figures/'),
                         'Renderer unchanged proof invalid')
    def test_repair_required_not_inflated(self):
        for tag in ('MAP','THESIS','OBJECTS'):
            x=next(r for r in D['chapters'] if r['chapter_id']==f'ATLAS-CH-{tag}-001')
            self.assertEqual(x['state'],'UNVERIFIED')
            self.assertTrue(x['unresolved'])
if __name__=='__main__':unittest.main()
