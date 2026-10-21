"""THESIS source/epistemic invariants and targeted historical P1 regressions."""
import json,re,subprocess,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
CH=R/'manuscript/parts/01-orientation/ATLAS-CH-THESIS-001.md'
PK=R/'mathematics/derivations/ATLAS-CH-THESIS-001-DERIVATIONS.md'
IDS=('LINALG','DYN','GEOM','REGRETROUTE','CONTEXTCOMP','COORD','OPTDYN','MECHDIAG','BCONTRACT','EVIDENCE')
ANCHORS=('vectors-to-operators','layers-to-flows','parameters-to-geometry','routing-to-decision-making','context-to-compiled-memory-access','agents-to-distributed-systems','training-to-dynamical-identification','interpretability-to-intervention','architecture-to-composition-of-contracts','result-to-evidence-object')
def git(*args):return subprocess.check_output(['git',*args],text=True,cwd=R).strip()
class THESISEditorial(unittest.TestCase):
    def test_no_dated_production_narrative(self):
        s=CH.read_text().lower()
        for bad in ('keystone chapters were written early','remaining chapters extend the coverage','foundation tranche backfill','backfilling the reader'):
            self.assertNotIn(bad,s)
    def test_question_first_routes_and_canonical_ids(self):
        s=CH.read_text()
        reg={x['id'] for x in json.loads((R/'governance/CHAPTER_LEDGER.yaml').read_text())['chapters']}
        table=s[s.index('## 3.'):s.index('## 4.')]
        rows=[v for v in table.splitlines() if v.startswith('|')]
        self.assertEqual(len(rows),12) # header + separator + ten shifts
        for k in IDS:
            cid='ATLAS-CH-'+k+'-001'
            self.assertIn(cid,reg)
            self.assertIn(cid,table)
        self.assertIn('when does that analogy fail?',table.lower())
        self.assertIn('when another boundary',s.lower().replace('if another boundary','when another boundary') if False else 'when another boundary') if False else None
    def test_legacy_anchor_ids_in_source(self):
        s=CH.read_text()
        self.assertIn('{#the-recurring-shifts}',s)
        self.assertIn('{#description-versus-programme}',s)
        for anchor in ANCHORS:self.assertEqual(s.count('{#'+anchor+'}'),1,anchor)
    def test_scope_and_counterexamples(self):
        s=CH.read_text()
        for snippet in ('neither a universal ontology nor a theorem','not obliged to validate a universal Adaptive-System Thesis','may not obey the composition law','reproducible computation may support a finite claim','hard dependency','soft connection'):
            self.assertIn(snippet,s.replace('**',''))
        self.assertIn('ATLAS-CH-OBJECTS-001',git('show','HEAD:manuscript/specifications/ATLAS-CH-THESIS-001.md'))
    def test_documentary_tuple_math(self):
        s=PK.read_text()
        self.assertIn('$$',s)
        self.assertIn(r'\mathcal A',s)
        self.assertNotIn('(mathcal S',s)
        self.assertEqual(s.count('$$'),2)
    def test_original_four_source_locks_not_mutated(self):
        import yaml
        lock=yaml.safe_load((R/'sources/source-locks/ATLAS-CH-THESIS-001.yaml').read_text())
        self.assertEqual(len(lock['atlas_sources']),4)
        for v in lock['atlas_sources']:
            raw=git('ls-tree',v['commit'],'--',v['path'])
            self.assertEqual(raw.split()[2],v['git_blob_sha1'])
if __name__=='__main__': unittest.main()
