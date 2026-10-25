"""ATLAS #443: exact sphere and manifold-scope producer regression witnesses."""
import math
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = (ROOT / "manuscript/parts/02-mathematical-substrate/ATLAS-CH-GEOM-001.md").read_text(encoding="utf-8")
DER = (ROOT / "mathematics/derivations/ATLAS-CH-GEOM-001-DERIVATIONS.md").read_text(encoding="utf-8")

class GeomProducerWitness(unittest.TestCase):
    def test_exact_plate_and_distinct_angles(self):
        # x=(0,0,1), v=(4/5,0,0); ||x+v||=sqrt(41)/5.
        self.assertEqual(F(4*4 + 5*5, 41), 1)
        t = F(4, 5)
        self.assertGreater(float(t) - math.atan(float(t)), 0)
        normalized = (4/math.sqrt(41), 0., 5/math.sqrt(41))
        exponential = (math.sin(float(t)), 0., math.cos(float(t)))
        self.assertAlmostEqual(sum(a*a for a in normalized), 1, places=14)
        self.assertAlmostEqual(sum(a*a for a in exponential), 1, places=14)
        self.assertGreater(math.dist(normalized, exponential), 0.1)

    def test_exact_taylor_coefficients(self):
        # Coefficients of sin(t), t(1+t^2)^(-1/2), cos(t), (1+t^2)^(-1/2).
        tangential_cubic = F(-1,6) - F(-1,2)
        radial_quartic = F(1,24) - F(3,8)
        self.assertEqual(tangential_cubic, F(1,3))
        self.assertEqual(radial_quartic, F(-1,3))
        self.assertIn(r"\\frac{t^3}{3}u", SRC)
        self.assertIn(r"\\frac{t^4}{3}x", DER)

    def test_stiefel_quotient_dimensions(self):
        for n in range(2,9):
            for p in range(1,n+1):
                st = n*p - p*(p+1)//2
                orth = p*(p-1)//2
                self.assertEqual(st-orth,p*(n-p))
        self.assertEqual(3*1-1,2)  # St(3,1) = S^2
        self.assertEqual(3*(3-3),0)  # Gr(3,3) is a single point

    def test_metric_scope(self):
        # For df(v)=v1+v2 and g=diag(2,3), grad_g=(1/2,1/3), not (1,1).
        v=(F(2,5),F(-1,7))
        metric_grad=(F(1,2),F(1,3))
        df_v=sum(v)
        self.assertEqual(2*metric_grad[0]*v[0]+3*metric_grad[1]*v[1],df_v)
        self.assertNotEqual(metric_grad,(F(1),F(1)))
        self.assertIn("induced Euclidean metric",SRC)
        self.assertIn("Euclidean projection alone",DER)

    def test_domain_source_and_equations(self):
        self.assertIn(r"d\\ge 2",SRC)
        self.assertIn(r"n\\ge p\\ge1",SRC)
        self.assertIn(r"p(n-p)",SRC)
        self.assertIn(r"\\theta=\\pi",DER)
        for text in (SRC,DER):
            self.assertEqual(text.count(r"\\["),text.count(r"\\]"))
            self.assertFalse(any(ord(ch)<32 and ch not in "\\n\\t" for ch in text))
        for ref in ("Lee2018Riemannian","AbsilMahonySepulchre2008",
                    "EdelmanAriasSmith1998","Shoemake1985"):
            self.assertIn(ref,SRC)

if __name__=="__main__":
    unittest.main()
