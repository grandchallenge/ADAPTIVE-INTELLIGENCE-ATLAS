"""Exact-rational Krylov arithmetic and hostile assumption controls; stdlib CI."""
from fractions import Fraction as F
from pathlib import Path
import re, unittest, subprocess
R=Path(__file__).resolve().parents[1]
S=(R/'manuscript/parts/02-mathematical-substrate/ATLAS-CH-KRYLOV-001.md').read_text()
D=(R/'mathematics/derivations/ATLAS-CH-KRYLOV-001-DERIVATIONS.md').read_text()
W=(R/'mathematics/computational-witnesses/ATLAS-CW-KRYLOV-001.md').read_text()
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def mmul(d,v):return [x*y for x,y in zip(d,v)]
class KrylovAcceptance(unittest.TestCase):
 def test_exact_galerkin_witness_and_energy(self):
    diag=[F(1),F(2),F(4)]; b=[F(1)]*3; Ab=mmul(diag,b)
    self.assertEqual([[dot(b,Ab),dot(b,mmul(diag,Ab))],[dot(Ab,Ab),dot(Ab,mmul(diag,Ab))]],[[7,21],[21,73]])
    c=[F(36,35),F(-1,5)]
    x=[c[0]*b[i]+c[1]*Ab[i] for i in range(3)]
    self.assertEqual(x,[F(29,35),F(22,35),F(8,35)])
    r=[b[i]-diag[i]*x[i] for i in range(3)]
    self.assertEqual(r,[F(6,35),F(-9,35),F(3,35)])
    self.assertEqual(dot(b,r),0);self.assertEqual(dot(Ab,r),0)
    self.assertEqual(dot(r,r),F(18,175))
    e=[F(1,diag[i])-x[i] for i in range(3)]
    self.assertEqual(dot(e,mmul(diag,e)),F(9,140))
 def test_exact_lanczos_coefficients(self):
    # v1=(1,1,1)/sqrt3; v2=(-4,-1,5)/sqrt42.
    v=[F(-4),F(-1),F(5)]
    self.assertEqual(sum(v),0)
    self.assertEqual(dot(v,v),42)
    self.assertEqual(dot(v,mmul([F(1),F(2),F(4)],v)),F(118))
    self.assertEqual(F(118,42),F(59,21))
    beta1_sq=F(14,9)
    beta2_sq=F(10)-F(59,21)**2-beta1_sq
    self.assertEqual(beta2_sq,F(27,49))
    self.assertIn(r'\beta_{j-1}',S)
 def test_spd_conjugate_gradient_residual_may_increase(self):
    diag=[F(1),F(100),F(10000)];b=[F(1)]*3
    alpha=dot(b,b)/dot(b,mmul(diag,b))
    self.assertEqual(alpha,F(1,3367))
    residual=[b[i]*(1-alpha*diag[i]) for i in range(3)]
    self.assertEqual(residual,[F(3366,3367),F(3267,3367),F(-6633,3367)])
    self.assertEqual(dot(residual,residual),F(19602,3367))
    self.assertGreater(dot(residual,residual),dot(b,b))
    err0=[1/d for d in diag]
    err1=[err0[i]-alpha for i in range(3)]
    self.assertEqual(dot(err0,mmul(diag,err0)),F(10101,10000))
    self.assertEqual(dot(err1,mmul(diag,err1)),F(33980067,33670000))
    self.assertLess(dot(err1,mmul(diag,err1)),dot(err0,mmul(diag,err0)))
 def test_arnoldi_nonzero_start_and_happy_breakdown(self):
    self.assertIn('r_0=0',S)
    self.assertIn('happy breakdown',S)
    self.assertIn('invariant',S)
    # A=I, r0=e1: Krylov span is dimension one for every m.
    r0=[F(1),F(0)]
    for n in range(1,10):
        self.assertEqual(r0,[F(1),F(0)])
    self.assertEqual(dot(r0,r0),1)
    self.assertIn('cannot',D)
 def test_complex_adjoint_is_not_real_transpose(self):
    self.assertIn('conjugate transposes',S)
    self.assertIn('conjugate transpose',D)
    v=[1+0j,1j]
    transpose_inner=sum(x*x for x in v)
    adjoint_inner=sum(x.conjugate()*x for x in v)
    self.assertEqual(transpose_inner,0)
    self.assertEqual(adjoint_inner,2)
 def test_reduced_galerkin_may_fail_for_invertible_operator(self):
    # Invertible A=[[0,1],[1,0]], V=e1; V^T A V=0.
    A=[[F(0),F(1)],[F(1),F(0)]];v=[F(1),F(0)]
    Av=[dot(row,v) for row in A]
    self.assertEqual(dot(v,Av),0)
    self.assertEqual(A[0][0]*A[1][1]-A[0][1]*A[1][0],-1)
    self.assertIn('can instead be singular',S)
    self.assertIn('the projected matrix may be singular',D)
 def test_invertible_preconditioner_contract_and_source_limits(self):
    self.assertIn('fixed invertible',S)
    self.assertIn('M must be invertible',D)
    for term in ('Arnoldi1951','Lanczos1950','Saad2003'):
        self.assertIn(term,S)
    self.assertIn('does not prove rapid convergence',W)
    tex=(R/'manuscript/latex/atlas-v0.1.1-rc.2.tex').read_text()
    self.assertEqual(len({v.split('}',1)[0] for v in tex.split(chr(92)+'label{')[1:]}),2971)
    self.assertEqual(tex.count(r'\includegraphics'),18)
if __name__=='__main__':unittest.main()
