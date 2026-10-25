"""Exact numerical and domain regressions for the geometry chapter."""
import math
import unittest
from pathlib import Path

R = Path(__file__).resolve().parents[1]
S = (R/"manuscript/parts/02-mathematical-substrate/ATLAS-CH-GEOM-001.md").read_text()
D = (R/"mathematics/derivations/ATLAS-CH-GEOM-001-DERIVATIONS.md").read_text()

class Geometry(unittest.TestCase):
    def test_retraction_and_exp_are_distinct_unit_endpoints(self):
        t=0.8
        e=(math.sin(t), math.cos(t))
        r=(t/math.hypot(1,t), 1/math.hypot(1,t))
        for a in (e,r):
            self.assertAlmostEqual(sum(v*v for v in a),1,places=13)
        self.assertGreater(math.dist(e,r),0.01)

    def test_cubic_difference(self):
        for t in (0.03,0.02,0.01):
            self.assertAlmostEqual((math.sin(t)-t/math.hypot(1,t))/t**3,1/3,delta=.001)
            self.assertAlmostEqual((math.cos(t)-1/math.hypot(1,t))/t**4,-1/3,delta=.001)
        self.assertIn(r'\frac{r^2}{3}v', S)
        self.assertIn(r'\frac{r^2}{3}v', D)

    def test_dimension_metric_and_antipodal_scope(self):
        for k in (r'd\ge2',r'1\le p\le n',
                  'induced Euclidean metric',
                  'single full-space point',
                  'minimizing geodesic is not unique'):
            self.assertIn(k,S)
        self.assertIn(r'1\le p\le n',D)
        self.assertAlmostEqual(math.acos(-1),math.pi)

    def test_original_anchors_figures_and_math_pairing(self):
        self.assertEqual(S.count(r'\['),S.count(r'\]'))
        self.assertEqual(D.count(r'\['),D.count(r'\]'))
        tex=(R/"manuscript/latex/atlas-v0.1.1-rc.2.tex").read_text()
        self.assertEqual(len({x.split('}',1)[0] for x in tex.split(chr(92)+'label{')[1:]}),2971)
        self.assertEqual(tex.count(r'\includegraphics'),18)

if __name__=="__main__":
    unittest.main()
