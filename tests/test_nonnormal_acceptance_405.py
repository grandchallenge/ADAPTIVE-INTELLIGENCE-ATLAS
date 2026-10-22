"""Independent exact-arithmetic NORMAL/NONNORMAL chapter probes; stdlib-only CI."""
import math,re,unittest
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[1]
S=(R/'manuscript/parts/02-mathematical-substrate/ATLAS-CH-NONNORMAL-001.md').read_text()
D=(R/'mathematics/derivations/ATLAS-CH-NONNORMAL-001-DERIVATIONS.md').read_text()
W=(R/'mathematics/computational-witnesses/ATLAS-CW-NONNORMAL-001.md').read_text()
L=(R/'sources/source-locks/ATLAS-CH-NONNORMAL-001.yaml').read_text()
def gain(p,q):
    return math.sqrt((2*p*p+q*q+abs(q)*math.sqrt(4*p*p+q*q))/2)
class NonnormalExact(unittest.TestCase):
 def test_normal_rotation_requires_complex_eigenvectors(self):
    # R^T R=R R^T=I, but det(lambda I-R)=lambda^2+1.
    a,b,c,d=F(0),F(-1),F(1),F(0)
    self.assertEqual((a*a+c*c,b*b+d*d,a*b+c*d),(1,1,0))
    self.assertTrue(all(k*k+1>0 for k in range(-100,101)))
    self.assertIn('after complexification',S)
    self.assertIn('real symmetric matrices',S)
 def test_nilpotent_powers_and_zero_parameter(self):
    self.assertIn(r'a\in\mathbb R,\quad K>0',S)
    self.assertIn(r'n\ge 2',S)
    for a in (F(0),F(4,5),F(-7,10)):
      K=F(4)
      for n in range(2,41):
        diagonal=a**n
        offdiag=n*K*a**(n-1)
        # Product A^n A = A^(n+1), including a=0.
        self.assertEqual(diagonal*a,a**(n+1))
        self.assertEqual(diagonal*K+offdiag*a,(n+1)*K*a**n)
    self.assertIn(r'A^0=I',S)
    self.assertIn(r'A^1=A',S)
 def test_gain_and_normal_comparison(self):
    a=.8;K=4.
    values=[gain(a**n, (n*K*a**(n-1) if n else 0)) for n in range(41)]
    self.assertEqual(values[0],1.)
    self.assertEqual(values.index(max(values)),4)
    self.assertAlmostEqual(max(values),8.2124290544,places=9)
    self.assertTrue(all(a**(k+1)<a**k for k in range(40)))
 def test_pseudospectrum_disc_and_extraneous_root(self):
    self.assertIn(r'\varepsilon>0',S)
    self.assertIn('negative algebraic branch',S)
    for K in (F(1),F(4),F(13,2)):
      for eps in (F(1,100),F(1,3),F(5)):
        r2=eps*(eps+K)
        self.assertEqual(K*K+4*r2,(K+2*eps)**2)
        sigma_min_squared=(2*r2+K*K-K*(K+2*eps))/2
        self.assertEqual(sigma_min_squared,eps*eps)
        if eps>=K:self.assertLess(eps*(eps-K),eps*eps)
 def test_scope_sources_and_render_math_labels(self):
    self.assertIn('not a causal diagnosis',S)
    self.assertIn('does **not** establish',S)
    self.assertIn(r'\Lambda_\varepsilon',D)
    self.assertIn('at',W)
    for id in ('NONNORMAL-HORN-JOHNSON-2012','NONNORMAL-TREFETHEN-EMBREE-2005',
               'NONNORMAL-REDDY-SCHMID-HENNINGSON-1993',
               'NONNORMAL-TREFETHEN-TREFETHEN-REDDY-DRISCOLL-1993'):
      self.assertIn(id,L)
    tex=(R/'manuscript/latex/atlas-v0.1.1-rc.2.tex').read_text()
    self.assertEqual(len({v.split('}',1)[0] for v in tex.split(chr(92)+'label{')[1:]}),2971)
    self.assertEqual(tex.count(r'\includegraphics'),18)
if __name__=='__main__':unittest.main()
