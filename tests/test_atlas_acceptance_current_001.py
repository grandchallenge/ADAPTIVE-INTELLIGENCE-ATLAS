"""Fail-closed exact-source, role-separated ATLAS 80-chapter acceptance."""
import hashlib,json,subprocess,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'governance/editorial/v0.1.1/CHAPTER_ACCEPTANCE_EVIDENCE_080.json').read_text())
P=json.loads((R/'governance/editorial/v0.1.1/P01_PRODUCER_001.json').read_text())
def git(*args):return subprocess.check_output(['git',*args],text=True,cwd=R).strip()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class EditorialAcceptance(unittest.TestCase):
 def test_80_rows_five_accepted(self):
  self.assertEqual(len(D['chapters']),80)
  self.assertEqual(len({x['chapter_id'] for x in D['chapters']}),80)
  accepted=[x['chapter_id'] for x in D['chapters'] if x['state']=='ACCEPTED']
  self.assertEqual(accepted,[f'ATLAS-CH-{x}-001' for x in ('THESIS','MAP','OBJECTS','EVIDENCE','LINALG')])
  self.assertEqual(D['accepted_count'],5)
  self.assertEqual(sum(x['state']=='UNVERIFIED' for x in D['chapters']),75)
 def test_all_80_chapter_blobs(self):
  for row in D['chapters']:
   with self.subTest(chapter=row['chapter_id']):
    self.assertEqual(git('hash-object',row['source_path']),row['source_blob_sha1'])
 def test_source_tree_exact_in_shallow_ci(self):
  for name,expected in D['reviewed_source_tree_ids'].items():
   with self.subTest(source=name):self.assertEqual(git('rev-parse','HEAD:'+name),expected)
  self.assertEqual(D['reviewed_source_tree_ids']['sources'],D['original_reviewed_source_tree_ids']['sources'])
  self.assertEqual(D['reviewed_source_tree_ids']['figures'],D['original_reviewed_source_tree_ids']['figures'])
 def test_four_existing_acceptances_not_rewritten(self):
  for tag in ('THESIS','MAP','OBJECTS','EVIDENCE'):
   row=next(x for x in D['chapters'] if x['chapter_id']==f'ATLAS-CH-{tag}-001')
   a=row['accepted_evidence']
   q=row['current_render_revalidation']
   with self.subTest(chapter=tag):
    self.assertNotEqual(a['producer_run'],a['critic_run'])
    self.assertEqual(row['source_blob_sha1'],a['source_blob_sha1'])
    self.assertFalse(a['mathematical_certification'])
    self.assertFalse(a['public_release_authorization'])
    self.assertEqual(q['head'],D['candidate_head'])
    self.assertEqual(q['pdf_sha256'],D['current_render']['pdf_sha256'])
    self.assertEqual(q['html_sha256'],D['current_render']['html_sha256'])
    self.assertEqual(q['critic_run'],'a0430e5cf0f04b2fb2c3d0e91a814e84')
    self.assertIn('issues/430#issuecomment-',q['critic_url'])
    self.assertTrue(q['source_blob_unchanged'])
    self.assertNotEqual(a['pdf_sha256'],q['pdf_sha256'])
    if tag=='MAP':
     self.assertEqual(git('hash-object',row['documentary_packet_path']),a['documentary_blob_sha1'])
     self.assertEqual(sha(R/row['documentary_packet_path']),a['documentary_sha256'])
 def test_new_linalg_real_critic_provenance(self):
  row=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-LINALG-001')
  a=row['accepted_evidence']
  self.assertEqual(a['head'],D['candidate_head'])
  self.assertEqual(row['state'],'ACCEPTED')
  self.assertEqual(a['source_blob_sha1'],git('hash-object',row['source_path']))
  self.assertEqual(a['source_blob_sha1'],'9d74b3f4e2939cf4362a050b0851cd47f822788d')
  self.assertNotEqual(a['producer_run'],a['critic_run'])
  self.assertEqual(a['producer_run'],row['producer_run_id'])
  self.assertIn('issues/426#issuecomment-',a['producer_url'])
  self.assertIn('issues/430#issuecomment-',a['critic_url'])
  self.assertEqual(a['pdf_sha256'],D['current_render']['pdf_sha256'])
  self.assertEqual(a['html_sha256'],D['current_render']['html_sha256'])
  self.assertEqual(a['pdf_pages'],[109,123])
  self.assertEqual(a['derivation_blob_sha1'],git('hash-object','mathematics/derivations/ATLAS-CH-LINALG-001-DERIVATIONS.md'))
  self.assertEqual(a['witness_blob_sha1'],git('hash-object','mathematics/computational-witnesses/ATLAS-CW-LINALG-001.md'))
  self.assertEqual(len(row['resolved_findings']),4)
  self.assertFalse(a['mathematical_certification'])
  self.assertFalse(a['public_release_authorization'])
 def test_preserve_all_producer_and_critic_run_logs(self):
  for row in D['chapters']:
   if row['state']!='ACCEPTED':continue
   a=row['accepted_evidence']
   self.assertTrue(a.get('producer_run') and a.get('critic_run'))
   self.assertTrue(a['producer_url'].startswith('https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/'))
   self.assertTrue(a['critic_url'].startswith('https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/'))
if __name__=='__main__':unittest.main()
