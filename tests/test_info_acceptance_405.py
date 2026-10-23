"""Exact information-theory witness and source-boundary checks (stdlib only)."""
import math,unittest
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[1]
S=(R/'manuscript/parts/02-mathematical-substrate/ATLAS-CH-INFO-001.md').read_text()
D=(R/'mathematics/derivations/ATLAS-CH-INFO-001-DERIVATIONS.md').read_text()
SPEC=(R/'manuscript/specifications/ATLAS-CH-INFO-001.md').read_text()
W=(R/'mathematics/computational-witnesses/ATLAS-CW-INFO-001.md').read_text()
def H(p):return -sum(float(x)*math.log2(float(x)) for x in p if x>0)
class InformationExact(unittest.TestCase):
 def test_joint_mutual_info(self):
  P=[[F(3,8),F(1,8)],[F(1,8),F(3,8)]]
  self.assertEqual([sum(row) for row in P],[F(1,2)]*2)
  self.assertEqual([sum(P[i][j] for i in range(2)) for j in range(2)],[F(1,2)]*2)
  mi=sum(float(v)*math.log2(4*float(v)) for row in P for v in row)
  self.assertAlmostEqual(mi,math.log(27/16)/math.log(16),places=13)
  self.assertAlmostEqual(mi,0.1887218755408671,places=13)
  self.assertAlmostEqual(H([x for row in P for x in row]),2-mi,places=13)
  self.assertIn('0.1887218755408671',W)
 def test_units_and_cross_entropy(self):
  p=[F(3,4),F(1,4)];q=[F(1,2),F(1,2)]
  x=-sum(float(a)*math.log2(float(b)) for a,b in zip(p,q))
  kl=sum(float(a)*math.log2(float(a/b)) for a,b in zip(p,q))
  self.assertAlmostEqual(x,H(p)+kl,places=13)
  self.assertIn(r'\log_2\frac{p(x)}{q(x)}',S)
  self.assertIn(r'\log_2\frac{p(x)}{q(x)}',D)
  self.assertIn(r'division by \(\ln 2\)',S)
  self.assertNotIn(r'division by \(1/\ln 2\)',S)
 def test_kl_absolute_continuity_and_tower(self):
  self.assertTrue(F(1,2)>0 and F(0)==0)
  self.assertIn(r'P\not\ll Q',S)
  self.assertIn(r'\mathbb E[\mathbb E[X\mid Y]]',S)
  P=[[F(3,8),F(1,8)],[F(1,8),F(3,8)]]
  self.assertEqual(sum(i*P[i][j] for i in range(2) for j in range(2)),
                   sum(sum(i*P[i][j] for i in range(2)) for j in range(2)))
 def test_hoeffding_bernoulli(self):
  self.assertLess(2*math.exp(-8),.001)
  for text in (S,D):
   self.assertIn('independent',text)
   self.assertIn(r'2e^{-8}',text)
 def test_bernoulli_sufficiency_scope(self):
  p=F(2,5)
  prob=lambda x:math.prod(float(p if v else 1-p) for v in x)
  self.assertAlmostEqual(prob([1,1,0,0]),prob([0,1,0,1]))
  self.assertIn('conditional distribution',S)
  self.assertIn(r'T=\sum_i X_i',S)
  self.assertIn(r'0<p<1',S)
 def test_print_and_source_bounds(self):
  for x in (S,D,SPEC):
   self.assertEqual(x.count(r'\['),x.count(r'\]'))
   self.assertFalse(any(ord(c)<32 and c not in '\n\t' for c in x))
  for key in ('CoverThomas2006','WainwrightJordan2008','Vershynin2018'):
   self.assertIn(key,S)
  tex=(R/'manuscript/latex/atlas-v0.1.1-rc.2.tex').read_text()
  self.assertEqual(len({v.split('}',1)[0] for v in tex.split(chr(92)+'label{')[1:]}),2971)
  self.assertEqual(tex.count(r'\includegraphics'),18)
if __name__=='__main__':unittest.main()
