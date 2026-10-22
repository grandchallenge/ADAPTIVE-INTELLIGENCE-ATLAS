"""Fail-closed, shallow-CI-capable GCL Atlas editorial acceptance ledger."""
import json,subprocess,unittest,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'governance/editorial/v0.1.1/CHAPTER_ACCEPTANCE_EVIDENCE_080.json').read_text())
P=json.loads((R/'governance/editorial/v0.1.1/P01_PRODUCER_001.json').read_text())
def git(*a):return subprocess.check_output(['git',*a],cwd=R,text=True).strip()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class EditorialAcceptance(unittest.TestCase):
 def test_exactly_80_and_five_accepted(self):
  self.assertEqual(len(D['chapters']),80)
  self.assertEqual(len({r['chapter_id'] for r in D['chapters']}),80)
  accept=[x['chapter_id'] for x in D['chapters'] if x['state']=='ACCEPTED']
  self.assertEqual(accept,[f'ATLAS-CH-{x}-001' for x in ('THESIS','MAP','OBJECTS','EVIDENCE','LINALG')])
  self.assertEqual(D['accepted_count'],5)
  self.assertEqual(sum(x['state']=='UNVERIFIED' for x in D['chapters']),75)
 def test_80_exact_source_blobs(self):
  for r in D['chapters']:
   with self.subTest(id=r['chapter_id']):
    self.assertEqual(git('hash-object',r['source_path']),r['source_blob_sha1'])
 def test_exact_current_source_trees(self):
  for name,tree in D['reviewed_source_tree_ids'].items():
   with self.subTest(name=name):self.assertEqual(git('rev-parse','HEAD:'+name),tree)
  self.assertEqual(D['reviewed_source_tree_ids']['sources'],D['original_reviewed_source_tree_ids']['sources'])
  self.assertEqual(D['reviewed_source_tree_ids']['figures'],D['original_reviewed_source_tree_ids']['figures'])
 def test_prior_three_acceptances_preserved_and_new_render_rechecked(self):
  old=D['prior_render_snapshots'][0]
  for tag in ('THESIS','MAP','EVIDENCE'):
   row=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-'+tag+'-001')
   a=row['accepted_evidence'];now=row['current_render_revalidation']
   with self.subTest(tag=tag):
    self.assertEqual(row['state'],'ACCEPTED')
    self.assertEqual(a['source_blob_sha1'],row['source_blob_sha1'])
    self.assertNotEqual(a['producer_run'],a['critic_run'])
    self.assertEqual(a['pdf_sha256'],old['pdf_sha256'] if tag=='THESIS' else P['pdf_sha256'])
    self.assertEqual(a['html_sha256'],old['html_sha256'] if tag=='THESIS' else P['html_sha256'])
    self.assertEqual(now['head'],D['candidate_head'])
    self.assertEqual(now['pdf_sha256'],D['current_render']['pdf_sha256'])
    self.assertEqual(now['html_sha256'],D['current_render']['html_sha256'])
    self.assertEqual(now['critic_run'],'a0429e5cf0f04b2fb2c3d0e91a814e84')
    self.assertIn('issues/429#issuecomment-',now['critic_url'])
    self.assertTrue(now['source_blob_unchanged'])
    self.assertFalse(a['mathematical_certification'])
 def test_objects_new_acceptance_requires_distinct_critic(self):
  row=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-OBJECTS-001')
  a=row['accepted_evidence']
  self.assertEqual(a['head'],D['previous_candidate_head'])
  self.assertEqual(a['source_blob_sha1'],git('hash-object',row['source_path']))
  self.assertEqual(a['source_blob_sha1'],'bc39d74e16ba29568aeb777563c3a52d3c0ba3cc')
  self.assertNotEqual(a['producer_run'],a['critic_run'])
  self.assertIn('issues/423#issuecomment-',a['producer_url'])
  self.assertIn('issues/424#issuecomment-',a['critic_url'])
  self.assertEqual(a['pdf_sha256'],D['prior_render_snapshots'][-1]['pdf_sha256'])
  self.assertEqual(a['html_sha256'],D['prior_render_snapshots'][-1]['html_sha256'])
  self.assertEqual(a['pdf_pages'],[83,93])
  self.assertEqual(a['mathematical_display_identical_count'],23)
  self.assertEqual(a['documentary_blob_sha1'],git('hash-object','mathematics/derivations/ATLAS-CH-OBJECTS-001-DERIVATIONS.md'))
  self.assertEqual({x['id'] for x in row['resolved_findings']},{'ER-P1-06','ER-P1-07'})
  self.assertFalse(a['mathematical_certification'])
  self.assertFalse(a['public_release_authorization'])
 def test_linalg_fifth_acceptance_and_critic_exact_render(self):
  row=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-LINALG-001')
  a=row['accepted_evidence']
  self.assertEqual(row['state'],'ACCEPTED')
  self.assertEqual(a['head'],D['candidate_head'])
  self.assertEqual(a['source_blob_sha1'],git('hash-object',row['source_path']))
  self.assertNotEqual(a['producer_run'],a['critic_run'])
  self.assertEqual(a['producer_run'],'a0427e5cf0f04b2fb2c3d0e91a814e83')
  self.assertEqual(a['critic_run'],'a0429e5cf0f04b2fb2c3d0e91a814e84')
  self.assertIn('issues/427#issuecomment-',a['producer_url'])
  self.assertIn('issues/429#issuecomment-',a['critic_url'])
  self.assertEqual(a['pdf_sha256'],D['current_render']['pdf_sha256'])
  self.assertEqual(a['html_sha256'],D['current_render']['html_sha256'])
  self.assertEqual(a['pdf_pages'],[109,123])
  self.assertEqual(a['derivation_blob_sha1'],git('hash-object','mathematics/derivations/ATLAS-CH-LINALG-001-DERIVATIONS.md'))
  self.assertEqual(a['computational_witness_blob_sha1'],git('hash-object','mathematics/computational-witnesses/ATLAS-CW-LINALG-001.md'))
  self.assertEqual(a['original_figure_wolfram_blob'],git('hash-object','figures/wolfram/ATLAS-FIG-LINALG-001.wl'))
  self.assertEqual(a['original_figure_png_blob'],git('hash-object','figures/masters/ATLAS-FIG-LINALG-001.png'))
  self.assertFalse(a['mathematical_certification'])
  self.assertFalse(a['public_release_authorization'])
 def test_prior_four_new_renderer_critic(self):
  for tag in ('THESIS','MAP','OBJECTS','EVIDENCE'):
   row=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-'+tag+'-001')
   q=row['current_render_revalidation']
   self.assertEqual(q['head'],D['candidate_head'])
   self.assertEqual(q['critic_run'],'a0429e5cf0f04b2fb2c3d0e91a814e84')
   self.assertIn('issues/429#issuecomment-',q['critic_url'])
   self.assertTrue(q['source_blob_unchanged'])
   self.assertTrue(row.get('render_revalidation_history') or row['accepted_evidence']['pdf_sha256'])
 def test_all_are_editorial_not_public_or_certified(self):
  for r in D['chapters']:
   if r['state']!='ACCEPTED':continue
   a=r['accepted_evidence']
   self.assertFalse(a['mathematical_certification'])
   self.assertFalse(a['public_release_authorization'])
if __name__=='__main__':unittest.main()
