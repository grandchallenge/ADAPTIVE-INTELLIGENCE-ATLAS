"""Fail-closed exact-source, role-separated ATLAS 80-chapter acceptance."""
import hashlib,json,subprocess,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'governance/editorial/v0.1.1/CHAPTER_ACCEPTANCE_EVIDENCE_080.json').read_text())
P=json.loads((R/'governance/editorial/v0.1.1/P01_PRODUCER_001.json').read_text())
def git(*args):return subprocess.check_output(['git',*args],text=True,cwd=R).strip()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class EditorialAcceptance(unittest.TestCase):
 def test_80_rows_eight_accepted(self):
  self.assertEqual(len(D['chapters']),80)
  self.assertEqual(len({x['chapter_id'] for x in D['chapters']}),80)
  accepted=[x['chapter_id'] for x in D['chapters'] if x['state']=='ACCEPTED']
  self.assertEqual(accepted,[f'ATLAS-CH-{x}-001' for x in ('THESIS','MAP','OBJECTS','EVIDENCE','LINALG','NONNORMAL','KRYLOV','INFO')])
  self.assertEqual(D['accepted_count'],8)
  self.assertEqual(sum(x['state']=='UNVERIFIED' for x in D['chapters']),72)
 def test_all_80_chapter_blobs(self):
  pending=D.get('pending_producer')
  for row in D['chapters']:
   with self.subTest(chapter=row['chapter_id']):
    current=git('hash-object',row['source_path'])
    if pending and row['chapter_id']==pending['chapter_id']:
     self.assertEqual(row['state'],'UNVERIFIED')
     self.assertIsNone(row['accepted_evidence'])
     self.assertEqual(row['source_path'],pending['source_path'])
     self.assertNotEqual(row['source_blob_sha1'],pending['proposed_source_blob_sha1'])
     self.assertEqual(current,pending['proposed_source_blob_sha1'])
    else:
     self.assertEqual(current,row['source_blob_sha1'])
 def test_source_tree_exact_in_shallow_ci(self):
  pending=D.get('pending_producer')
  if pending:
   self.assertEqual(pending['chapter_id'],'ATLAS-CH-GEOM-001')
   self.assertEqual(pending['issue'],443)
   self.assertEqual(pending['pull_request'],445)
   self.assertEqual(pending['state'],'PRODUCED_PENDING_CRITIC')
   self.assertEqual(pending['acceptance_count_change'],0)
   self.assertEqual(D['accepted_count'],8)
   self.assertNotEqual(D['reviewed_source_tree_ids']['manuscript'],pending['proposed_manuscript_tree_sha1'])
  for name,expected in D['reviewed_source_tree_ids'].items():
   actual=git('rev-parse','HEAD:'+name)
   with self.subTest(source=name):
    if pending and name=='manuscript':
     self.assertEqual(actual,pending['proposed_manuscript_tree_sha1'])
    else:
     self.assertEqual(actual,expected)
  self.assertEqual(D['reviewed_source_tree_ids']['sources'],D['original_reviewed_source_tree_ids']['sources'])
  self.assertEqual(D['reviewed_source_tree_ids']['figures'],D['original_reviewed_source_tree_ids']['figures'])
 def test_seven_existing_acceptances_not_rewritten(self):
  for tag in ('THESIS','MAP','OBJECTS','EVIDENCE','LINALG','NONNORMAL','KRYLOV'):
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
    self.assertEqual(q['critic_run'],'a0439e5cf0f04b2fb2c3d0e91a814e90')
    self.assertIn('issues/439#issuecomment-',q['critic_url'])
    self.assertTrue(q['source_blob_unchanged'])
    self.assertNotEqual(a['pdf_sha256'],q['pdf_sha256'])
    if tag=='MAP':
     self.assertEqual(git('hash-object',row['documentary_packet_path']),a['documentary_blob_sha1'])
     self.assertEqual(sha(R/row['documentary_packet_path']),a['documentary_sha256'])
 def test_new_linalg_real_critic_provenance(self):
  row=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-LINALG-001')
  a=row['accepted_evidence']
  self.assertEqual(a['head'],'8e4ebce996f116f4fcabd9a73b3901845bea813c')
  self.assertEqual(row['state'],'ACCEPTED')
  self.assertEqual(a['source_blob_sha1'],git('hash-object',row['source_path']))
  self.assertEqual(a['source_blob_sha1'],'9d74b3f4e2939cf4362a050b0851cd47f822788d')
  self.assertNotEqual(a['producer_run'],a['critic_run'])
  self.assertEqual(a['producer_run'],row['producer_run_id'])
  self.assertIn('issues/426#issuecomment-',a['producer_url'])
  self.assertIn('issues/430#issuecomment-',a['critic_url'])
  self.assertEqual(a['pdf_sha256'],next(x['pdf_sha256'] for x in D['prior_render_snapshots'] if x['head']==a['head']))
  self.assertEqual(a['html_sha256'],next(x['html_sha256'] for x in D['prior_render_snapshots'] if x['head']==a['head']))
  self.assertEqual(a['pdf_pages'],[109,123])
  self.assertEqual(a['derivation_blob_sha1'],git('hash-object','mathematics/derivations/ATLAS-CH-LINALG-001-DERIVATIONS.md'))
  self.assertEqual(a['witness_blob_sha1'],git('hash-object','mathematics/computational-witnesses/ATLAS-CW-LINALG-001.md'))
  self.assertEqual(len(row['resolved_findings']),4)
  self.assertFalse(a['mathematical_certification'])
  self.assertFalse(a['public_release_authorization'])
 def test_nonnormal_mathematical_critic_provenance(self):
  row=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-NONNORMAL-001')
  a=row['accepted_evidence']
  self.assertEqual(row['state'],'ACCEPTED')
  self.assertEqual(a['head'],'8f163c07a095aac6e3e07d1157981745970ae79b')
  self.assertEqual(a['source_blob_sha1'],git('hash-object',row['source_path']))
  self.assertEqual(a['source_blob_sha1'],'c25d2fe874eae5933c55b43919bda3cab8733345')
  self.assertNotEqual(a['producer_run'],a['critic_run'])
  self.assertEqual(a['producer_run'],row['producer_run_id'])
  self.assertIn('issues/432#issuecomment-',a['producer_url'])
  self.assertIn('issues/433#issuecomment-',a['critic_url'])
  self.assertEqual(a['pdf_sha256'],next(x['pdf_sha256'] for x in D['prior_render_snapshots'] if x['head']==a['head']))
  self.assertEqual(a['html_sha256'],next(x['html_sha256'] for x in D['prior_render_snapshots'] if x['head']==a['head']))
  self.assertEqual(a['pdf_pages'],[125,136])
  self.assertEqual(a['derivation_blob_sha1'],git('hash-object','mathematics/derivations/ATLAS-CH-NONNORMAL-001-DERIVATIONS.md'))
  self.assertEqual(a['witness_blob_sha1'],git('hash-object','mathematics/computational-witnesses/ATLAS-CW-NONNORMAL-001.md'))
  self.assertEqual(a['source_lock_entries_checked'],4)
  self.assertEqual(a['figure_physical_page'],130)
  self.assertGreaterEqual(a['figure_effective_dpi'],200)
  self.assertEqual({x['status'] for x in row['resolved_findings']},{'RESOLVED'})
  self.assertFalse(a['mathematical_certification'])
  self.assertFalse(a['public_release_authorization'])
 def test_krylov_math_critic_and_source_replay(self):
  row=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-KRYLOV-001')
  a=row['accepted_evidence']
  self.assertEqual(row['state'],'ACCEPTED')
  self.assertEqual(a['head'],D['previous_candidate_head'])
  self.assertEqual(a['source_blob_sha1'],git('hash-object',row['source_path']))
  self.assertEqual(a['source_blob_sha1'],'405fbe3f462998b3950b232309d811763108f3c7')
  self.assertNotEqual(a['producer_run'],a['critic_run'])
  self.assertEqual(a['producer_run'],row['producer_run_id'])
  self.assertIn('issues/435#issuecomment-',a['producer_url'])
  self.assertIn('issues/436#issuecomment-',a['critic_url'])
  self.assertEqual(a['pdf_sha256'],next(x['pdf_sha256'] for x in D['prior_render_snapshots'] if x['head']==a['head']))
  self.assertEqual(a['html_sha256'],next(x['html_sha256'] for x in D['prior_render_snapshots'] if x['head']==a['head']))
  self.assertEqual(a['pdf_pages'],[137,148])
  self.assertEqual(a['derivation_blob_sha1'],git('hash-object','mathematics/derivations/ATLAS-CH-KRYLOV-001-DERIVATIONS.md'))
  self.assertEqual(a['witness_blob_sha1'],git('hash-object','mathematics/computational-witnesses/ATLAS-CW-KRYLOV-001.md'))
  self.assertEqual(a['historical_pinned_git_source_locks_checked'],3)
  self.assertEqual(len(row['resolved_findings']),4)
  self.assertTrue(all(v['status']=='RESOLVED' for v in row['resolved_findings']))
  self.assertFalse(a['mathematical_certification'])
  self.assertFalse(a['public_release_authorization'])
 def test_info_mathematical_critic_and_unit_provenance(self):
  row=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-INFO-001')
  a=row['accepted_evidence']
  self.assertEqual(row['state'],'ACCEPTED')
  self.assertEqual(a['head'],D['candidate_head'])
  self.assertEqual(a['source_blob_sha1'],git('hash-object',row['source_path']))
  self.assertEqual(a['source_blob_sha1'],'4caaa28f0e5924f94d08d6ac95f2be6a824525d1')
  self.assertNotEqual(a['producer_run'],a['critic_run'])
  self.assertEqual(a['producer_run'],row['producer_run_id'])
  self.assertIn('issues/438#issuecomment-',a['producer_url'])
  self.assertIn('issues/439#issuecomment-',a['critic_url'])
  self.assertEqual(a['pdf_sha256'],D['current_render']['pdf_sha256'])
  self.assertEqual(a['html_sha256'],D['current_render']['html_sha256'])
  self.assertEqual(a['pdf_pages'],[149,162])
  self.assertEqual(a['specification_blob_sha1'],git('hash-object','manuscript/specifications/ATLAS-CH-INFO-001.md'))
  self.assertEqual(a['derivation_blob_sha1'],git('hash-object','mathematics/derivations/ATLAS-CH-INFO-001-DERIVATIONS.md'))
  self.assertEqual(a['witness_blob_sha1'],git('hash-object','mathematics/computational-witnesses/ATLAS-CW-INFO-001.md'))
  self.assertEqual(a['bibliographic_source_entries_checked'],3)
  self.assertEqual(len(row['resolved_findings']),6)
  self.assertTrue(all(v['status']=='RESOLVED' for v in row['resolved_findings']))
  self.assertEqual(a['witness_mutual_information_bits'],'0.1887218755408671')
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
