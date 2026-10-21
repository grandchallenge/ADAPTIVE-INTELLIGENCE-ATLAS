"""Source-level invariants for the six-section OBJECTS chapter correction."""
import json,re,subprocess,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'manuscript/parts/01-orientation/ATLAS-CH-OBJECTS-001.md'
DOC=ROOT/'mathematics/derivations/ATLAS-CH-OBJECTS-001-DERIVATIONS.md'
LEGACY=('the-same-tensor-can-be-four-different-things','noun-verb-motion-handshake','state',
'operator','first-category-error-array-equals-role','flow-and-dynamics',
'second-category-error-one-step-equals-dynamics','flow-like-is-weaker-than-flow',
'interface','third-category-error-matching-shape-equals-composability',
'interfaces-are-not-interiors','state-dependent-operators','operator-valued-state',
'evidence-is-another-object-class','why-this-vocabulary-matters','the-four-questions',
'operator-1','flow','interface-1','handoff-to-linear-algebra',
'handoff-to-information')
def raw():return SRC.read_text()
class ObjectRoles(unittest.TestCase):
 def test_consolidated_sections_and_preserved_legacy_links(self):
  s=raw()
  self.assertEqual(len(re.findall(r'(?m)^## [1-9]+\. ',s)),6)
  self.assertEqual(len(re.findall(r'(?m)^### ',s)),2)
  for anchor in LEGACY:
   with self.subTest(anchor=anchor):self.assertEqual(s.count('{#'+anchor+'}'),1)
 def test_correct_global_semiflow_local_flow(self):
  s=raw()
  for part in ('continuous global autonomous flow','jointly continuous',
               'open time-state domain','continuous semiflow','local flow',
               'do not imply continuity or differentiability','Neither a local flow nor a semiflow'):
   self.assertIn(part,s)
  self.assertIn('\\Phi_{t+s}',s)
 def test_three_distinct_worked_role_errors(self):
  s=raw()
  self.assertEqual(s.count('First category error:'),0)
  for statement in ('covariance matrix','x_k+h f(x_k)','same object',
       'not defined at the zero vector','G(F(x))=1','original magnitude is','contract can omit'):
   self.assertIn(statement,s)
 def test_four_questions_have_separate_roles(self):
  s=raw()
  for name in ('State','Operator','Flow','Interface'):
   self.assertRegex(s,r'\| (?:\[\]\{#[^}]+\} )?'+name+r' \|')
  self.assertIn('ATLAS-CH-OBJECTS-001',s)
 def test_rendered_canonical_unchanged_math_gates(self):
  tex=(ROOT/'manuscript/latex/atlas-v0.1.1-rc.2.tex').read_text()
  import hashlib
  self.assertEqual(len(set(re.findall(r'\\label\{([^}]+)\}',tex))),2971)
  self.assertEqual(tex.count(r'\includegraphics'),18)
 def test_documentary_math_paired_and_scoped(self):
  s=DOC.read_text()
  self.assertEqual(len(re.findall(r'(?m)^\$\$$',s)),8)
  self.assertIn('\\Phi_{t+s}',s)
  self.assertIn('\\mathcal X',s)
  self.assertNotIn('Phi_t:mathcal',s)
  self.assertIn('not a universal ontology',s)
if __name__=='__main__':unittest.main()
