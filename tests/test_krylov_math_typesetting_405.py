"""Exact rational and Markdown/LaTeX boundary regression for Atlas #405."""
from fractions import Fraction as F
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'manuscript/parts/02-mathematical-substrate/ATLAS-CH-KRYLOV-001.md'
TEX=ROOT/'manuscript/latex/atlas-v0.1.1-rc.2.tex'
LEGACY=(
    'A V_m = V_(m+1) Hbar_m.',
    'beta_(j-1) v_(j-1)',
    'T2=[[7/3,sqrt(14)/3]',
    '||r2||_2^2=18/175.',
    'V^T A V=[[7,21],[21,73]]',
)

class KrylovMathContract(unittest.TestCase):
    def test_semantic_equations_typeset(self):
        s=SOURCE.read_text()
        for p in LEGACY:
            with self.subTest(legacy=p):self.assertNotIn(p,s)
        self.assertEqual(s.count('\\[\n'),48)
        self.assertEqual(s.count('\\]\n'),48)
        self.assertIn(r'AV_m=V_{m+1}\overline H_m',s)
        self.assertIn(r'\beta_{j-1}v_{j-1}',s)
        self.assertIn(r'T_2=\begin{bmatrix}',s)
        self.assertIn(r'\lVert r_2\rVert_2^2=\frac{18}{175}',s)
    def test_same_equation_in_assembled_tex(self):
        tex=TEX.read_text()
        self.assertIn(r'\overline H_m',tex)
        self.assertIn(r'\begin{bmatrix}',tex)
        self.assertNotIn('Hbar_m',tex)
        self.assertEqual(tex.count(r'\includegraphics'),18)
        self.assertEqual(tex.count(r'\chapter{'),80)
    def test_galerkin_exact_rational(self):
        a=(F(1),F(2),F(4)); b=(F(1),)*3
        V=((F(1),F(1)),(F(1),F(2)),(F(1),F(4)))
        gram=tuple(tuple(sum(V[k][i]*a[k]*V[k][j] for k in range(3)) for j in range(2)) for i in range(2))
        self.assertEqual(gram,((7,21),(21,73)))
        c=(F(36,35),F(-1,5))
        x=tuple(sum(V[k][j]*c[j] for j in range(2)) for k in range(3))
        self.assertEqual(x,(F(29,35),F(22,35),F(8,35)))
        residual=tuple(b[k]-a[k]*x[k] for k in range(3))
        self.assertEqual(residual,(F(6,35),F(-9,35),F(3,35)))
        self.assertEqual(sum(V[k][j]*residual[k] for k in range(3) for j in (0,)),0)
        self.assertEqual(sum(V[k][j]*residual[k] for k in range(3) for j in (1,)),0)
        self.assertEqual(sum(r*r for r in residual),F(18,175))
    def test_spd_cg_norm_separation(self):
        a=(F(1),F(100),F(10000))
        alpha=F(3,sum(a))
        self.assertEqual(alpha,F(1,3367))
        r=tuple(F(1)-alpha*t for t in a)
        self.assertEqual(r,(F(3366,3367),F(3267,3367),F(-6633,3367)))
        self.assertEqual(sum(t*t for t in r),F(19602,3367))
        self.assertGreater(sum(t*t for t in r),F(3))
        e0=sum(F(1,a0) for a0 in a)
        e1=sum((v*v)/a0 for v,a0 in zip(r,a))
        self.assertLess(e1,e0)

if __name__=='__main__':unittest.main()
