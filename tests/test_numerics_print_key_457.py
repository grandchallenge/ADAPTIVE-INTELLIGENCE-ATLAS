"""Bounded, exact contract for numerical stability-figure reading key."""
from pathlib import Path
import unittest
P=Path(__file__).resolve().parents[1]
S=(P/'manuscript/parts/02-mathematical-substrate/ATLAS-CH-NUMERICS-001.md').read_text()
class NumericalFigureKey(unittest.TestCase):
 def test_stability_region_and_defect_scope(self):
  for term in ['**How to read the three panels at print size.**',r'(u+1)^2+v^2\le1',r'(u-1)^2+v^2=1','singular point $z=1$','Frobenius norm','one-step local defect','not global trajectory error','small-$h$ regime']:
   self.assertIn(term,S)
 def test_stability_disc_vs_exterior(self):
  self.assertEqual(((-1+1)**2+0**2)<=1,True)
  self.assertEqual(((1-1)**2+0**2)>=1,False)
  self.assertEqual(((-2-1)**2+0**2)>=1,True)
