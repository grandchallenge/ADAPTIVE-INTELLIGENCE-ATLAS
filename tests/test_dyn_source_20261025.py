from fractions import Fraction as F
from pathlib import Path
import math, unittest
R=Path(__file__).resolve().parents[1]
S=(R/'manuscript/parts/02-mathematical-substrate/ATLAS-CH-DYN-001.md').read_text()
D=(R/'mathematics/derivations/ATLAS-CH-DYN-001-DERIVATIONS.md').read_text()
class DynWitness(unittest.TestCase):
 def test_euler_counterexample(self):
  assert F(1)-F(3,2)*2==-2
  for n in range(1,7): self.assertGreater(2**n,math.exp(-3*n))
 def test_stability_boundary(self):
  self.assertTrue(all(abs(1-2*h)<1 for h in [F(1,4),F(1,2),F(3,4)]))
  self.assertEqual(abs(1-F(2)),1)
 def test_source_and_derivation(self):
  for x in ['0<h', 'e^{-3n}', '(-2)^n']:self.assertIn(x,S)
  for x in ['D11a. Exact scalar Euler stability defect','e^{-3n}']:self.assertIn(x,D)
if __name__=='__main__':unittest.main()
