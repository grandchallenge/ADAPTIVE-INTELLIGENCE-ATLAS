"""Scoped mathematical gluing and rendering-source identity checks, #405."""
import unittest
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
CHAPTER=ROOT/'manuscript/parts/02-mathematical-substrate/ATLAS-CH-LOCALGLOBAL-001.md'
BOOK=ROOT/'manuscript/latex/atlas-v0.1.1-rc.2.tex'
class LocalGlobalMath(unittest.TestCase):
    def test_source_is_math_not_code(self):
        s=CHAPTER.read_text()
        self.assertNotIn(chr(96),s)
        self.assertEqual(s.count('\\['),49)
        self.assertEqual(s.count('\\]'),49)
        self.assertNotRegex(s,r'(?m)^\\\][.,]$')
        for item in (r'\rho^V_W\circ\rho^U_V=\rho^U_W',
                     r'\mathcal F(S)=\mathbb R^S',
                     r'\operatorname{im}(R)=\ker(\Delta)',
                     r'\Delta(u_a,u_b,v_b,v_c)=u_b-v_b'):
            self.assertIn(item,s)
        self.assertEqual(s.count('<!-- ATLAS-CH-LOCALGLOBAL-001 -->'),1)
    def test_full_book_embeds_repaired_math(self):
        t=BOOK.read_text()
        for item in (r'\mathcal F(S)',r'\ker',r'\rho^V_W'):
            self.assertIn(item,t)
        self.assertEqual(t.count(r'\chapter{'),80)
        self.assertEqual(t.count(r'\includegraphics'),18)
    def test_exact_equalizer_and_injectivity(self):
        def restrict(x):
            a,b,c=x;return (a,b,b,c)
        def defect(v):return v[1]-v[2]
        for v in ((1,2,4),(0,0,0),(F(3,7),F(1,5),F(4,3))):
            self.assertEqual(defect(restrict(v)),0)
        self.assertNotEqual(restrict((1,2,4)),restrict((2,2,4)))
        for v in ((1,2,2,4),(0,5,5,7),(-1,F(1,3),F(1,3),19)):
            self.assertEqual(defect(v),0)
            self.assertEqual(restrict((v[0],v[1],v[3])),v)
    def test_compatible_incompatible_and_nonzero_obstruction(self):
        compatible=((F(1),F(2)),(F(2),F(4)))
        incompatible=((F(1),F(2)),(F(3),F(4)))
        self.assertEqual(compatible[0][1]-compatible[1][0],0)
        self.assertEqual(incompatible[0][1]-incompatible[1][0],-1)
        # The compatible global function is unique; the incompatible pair
        # cannot be the restriction of any global function.
        self.assertEqual((compatible[0][0],compatible[0][1],compatible[1][1]),(1,2,4))
        def global_pair(z):return ((z[0],z[1]),(z[1],z[2]))
        self.assertEqual(global_pair((1,2,4)),compatible)
        for a in (-1,0,1,2,3):
            for b in (-1,0,1,2,3):
                for c in (-1,0,1,2,3):
                    self.assertNotEqual(global_pair((a,b,c)),incompatible)
    def test_restriction_composition_exact(self):
        X={'a':F(1,2),'b':F(2,3),'c':F(3,4)}
        def rest(section,subset):return {k:section[k] for k in subset}
        U={'a','b'}; V={'b'};W={'b'}
        self.assertEqual(rest(rest(X,U),V),rest(X,V))
        self.assertEqual(rest(rest(X,U),W),rest(X,W))
        self.assertEqual(rest(X,set(X)),X)
if __name__=='__main__':unittest.main()
