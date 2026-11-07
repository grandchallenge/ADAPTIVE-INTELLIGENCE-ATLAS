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
 def test_hopf_frequency_scope_448(self):
  spec=(R/'manuscript/specifications/ATLAS-CH-DYN-001.md').read_text()
  self.assertIn(r'$\omega\ne 0$',S)
  self.assertIn(r'$\omega\ne 0$',spec)
  self.assertIn('every point on that circle is stationary',S)
  self.assertIn('the circle consists of equilibria',spec)
  self.assertIn(r'\omega\neq0',D)
  self.assertEqual(F(1)*F(1)-F(1)**3,0)
  self.assertEqual(F(0)*F(1),0)
  self.assertEqual(F(2)*F(1),2)
 def test_linearization_remainder_critic(self):
  spec=(R/'manuscript/specifications/ATLAS-CH-DYN-001.md').read_text()
  self.assertIn(r'o(\|\delta\|)',spec)
  self.assertIn('locally Lipschitz Jacobian',spec)
  self.assertIn(r'f(x)=|x|^{3/2}',spec)
  # Counterexample: f(x)=|x|^(3/2) is differentiable at zero,
  # but f(x)/x^2=1/sqrt(x) diverges for x down to zero.
  from fractions import Fraction as Q
  ratios=[(Q(1,n*n)**Q(3,2))/(Q(1,n*n)**2) for n in (2,4,8)]
  self.assertEqual([float(q) for q in ratios],[2.0,4.0,8.0])
 def test_figure_energy_semantics_448(self):
  manifest=(R/'figures/manifests/ATLAS-FIG-DYN-001.yaml').read_text()
  self.assertIn('unit-radius, energy-1/2 harmonic-oscillator orbit',manifest)
  self.assertIn('oscillator_energy: "H=1/2"',manifest)
  self.assertNotIn('unit-energy harmonic-oscillator orbit',manifest)
  self.assertEqual(F(1,2)*(1*1+0*0),F(1,2))
 def test_vector_field_type_scope_448(self):
  # A section of TX must send x to a tangent vector based at x.
  self.assertIn(r'f:\mathcal X\to\mathbb R^d',S)
  self.assertIn(r'f:\mathcal X\to T\mathcal X',S)
  self.assertIn(r'\pi\circ f=\operatorname{id}_{\mathcal X}',S)
  self.assertIn(r'f(x)\in T_x\mathcal X',S)
 def test_three_panel_figure_reader_key(self):
  self.assertIn('**Reading the three panels.**',S)
  for token in (
      r'x_0e^{-2t}',r'+\sqrt{\mu}',r'-\sqrt{\mu}',
      r'H(q,p)=(q^2+p^2)/2',r'H=1/2',
      'clockwise unit circle','normal print size'):
   self.assertIn(token,S)
 def test_source_and_derivation(self):
  for x in ['0<h', 'e^{-3n}', '(-2)^n']:self.assertIn(x,S)
  for x in ['D11a. Exact scalar Euler stability defect','e^{-3n}']:self.assertIn(x,D)
if __name__=='__main__':unittest.main()
