"""Exact-source, role-separated chapter acceptance ledger; no public certification."""
import hashlib,json,subprocess,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'governance/editorial/v0.1.1/CHAPTER_ACCEPTANCE_EVIDENCE_080.json').read_text())
P=json.loads((R/'governance/editorial/v0.1.1/P01_PRODUCER_001.json').read_text())
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True).strip()
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
class EditorialAcceptance(unittest.TestCase):
    def test_exactly_80_three_accepted(self):
        self.assertEqual(len(D['chapters']),80)
        self.assertEqual(len({r['chapter_id'] for r in D['chapters']}),80)
        accepted=[r['chapter_id'] for r in D['chapters'] if r['state']=='ACCEPTED']
        self.assertEqual(accepted,['ATLAS-CH-THESIS-001','ATLAS-CH-MAP-001','ATLAS-CH-EVIDENCE-001'])
        self.assertEqual(D['accepted_count'],len(accepted))
    def test_all_80_source_blobs(self):
        for row in D['chapters']:
            with self.subTest(chapter=row['chapter_id']):
                self.assertEqual(git('hash-object',row['source_path']),row['source_blob_sha1'])
    def test_legacy_map_evidence_receipts_not_rewritten(self):
        for tag in ('MAP','EVIDENCE'):
            cid=f'ATLAS-CH-{tag}-001'
            row=next(r for r in D['chapters'] if r['chapter_id']==cid)
            p=next(x for x in P['rows'] if x['chapter_id']==cid)
            a=row['accepted_evidence']; q=row['current_render_revalidation']
            with self.subTest(chapter=cid):
                self.assertEqual(row['state'],'ACCEPTED')
                self.assertEqual(a['source_blob_sha1'],p['source_blob_sha1'])
                self.assertEqual(a['head'],D['legacy_candidate_head'])
                self.assertEqual(a['pdf_sha256'],P['pdf_sha256'])
                self.assertEqual(a['html_sha256'],P['html_sha256'])
                self.assertNotEqual(a['producer_run'],a['critic_run'])
                self.assertEqual(q['head'],D['candidate_head'])
                self.assertEqual(q['pdf_sha256'],D['current_render']['pdf_sha256'])
                self.assertEqual(q['html_sha256'],D['current_render']['html_sha256'])
                self.assertEqual(q['critic_run'],D['current_render']['revalidation_critic_run'])
                self.assertIn('issues/421#issuecomment-',q['critic_url'])
                self.assertTrue(q['source_blob_unchanged'])
                self.assertFalse(a['mathematical_certification'])
                if tag=='MAP':
                    self.assertEqual(git('hash-object',row['documentary_packet_path']),a['documentary_blob_sha1'])
                    self.assertEqual(sha(R/row['documentary_packet_path']),a['documentary_sha256'])
    def test_thesis_actual_producer_critic_acceptance(self):
        row=next(r for r in D['chapters'] if r['chapter_id']=='ATLAS-CH-THESIS-001')
        a=row['accepted_evidence']
        self.assertEqual(a['head'],D['candidate_head'])
        self.assertEqual(a['source_blob_sha1'],row['source_blob_sha1'])
        self.assertEqual(a['source_blob_sha1'],'7c8fed7b3146ab906482486393cc7382a0b8aee3')
        self.assertNotEqual(a['producer_run'],a['critic_run'])
        self.assertEqual(a['producer_run'],row['producer_run_id'])
        self.assertIn('issues/420#issuecomment-',a['producer_url'])
        self.assertIn('issues/421#issuecomment-',a['critic_url'])
        self.assertEqual(a['pdf_sha256'],D['current_render']['pdf_sha256'])
        self.assertEqual(a['html_sha256'],D['current_render']['html_sha256'])
        self.assertEqual(a['pdf_pages'],[69,76])
        self.assertEqual(a['source_locks_checked'],4)
        self.assertEqual(a['documentary_blob_sha1'],git('hash-object','mathematics/derivations/ATLAS-CH-THESIS-001-DERIVATIONS.md'))
        self.assertEqual({e['status'] for e in row['resolved_findings']},{'RESOLVED'})
        self.assertEqual({e['id'] for e in row['resolved_findings']},{'ER-P1-01','ER-P1-02'})
        self.assertFalse(a['mathematical_certification'])
        self.assertFalse(a['public_release_authorization'])
    def test_exact_current_source_trees_shallow_ci(self):
        for name,tree in D['reviewed_source_tree_ids'].items():
            with self.subTest(name=name):
                self.assertEqual(git('rev-parse','HEAD:'+name),tree)
        self.assertNotEqual(D['original_reviewed_source_tree_ids']['manuscript'],
                            D['reviewed_source_tree_ids']['manuscript'])
        self.assertEqual(D['original_reviewed_source_tree_ids']['sources'],
                         D['reviewed_source_tree_ids']['sources'])
        self.assertEqual(D['original_reviewed_source_tree_ids']['figures'],
                         D['reviewed_source_tree_ids']['figures'])
    def test_repair_required_not_inflated(self):
        objects=next(x for x in D['chapters'] if x['chapter_id']=='ATLAS-CH-OBJECTS-001')
        self.assertEqual(objects['state'],'UNVERIFIED')
        self.assertIn('fragmentation',objects['unresolved'])
        self.assertEqual(len([x for x in D['chapters'] if x['state']=='UNVERIFIED']),77)
if __name__=='__main__':unittest.main()
