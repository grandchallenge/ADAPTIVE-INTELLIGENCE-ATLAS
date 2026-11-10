"""Independent, dependency-free numerical witness for ATLAS NUMERICS #459.

Run: python3 -m unittest discover -s tests -p 'test_atlas_numerics_459.py'
This tests mathematics, NOT Wolfram rendering, image layout, or print acceptance.
"""
import math
import unittest


def frobenius(a, b):
    return math.sqrt(sum((x - y) ** 2 for row_a, row_b in zip(a, b)
                         for x, y in zip(row_a, row_b)))


def exact(h):
    # A+B=[[0,1],[1,0]], so exp(h(A+B)) is hyperbolic.
    return ((math.cosh(h), math.sinh(h)),
            (math.sinh(h), math.cosh(h)))


def lie(h):
    # (I+hA)(I+hB), because A^2=B^2=0.
    return ((1+h*h, h), (h, 1.0))


def strang(h):
    # (I+hA/2)(I+hB)(I+hA/2).
    return ((1+h*h/2, h+h**3/4), (h, 1+h*h/2))


class NumericsFigureWitness(unittest.TestCase):
    def test_euler_stability_regions(self):
        for x, y in [(-1.0, 0.0), (-0.5, 0.0)]:
            self.assertLess((x+1)**2+y*y, 1)
            self.assertGreater((x-1)**2+y*y, 1)
        # The boundary is non-growing but is not strictly decaying.
        self.assertEqual((0+1)**2, 1)
        self.assertEqual((0-1)**2, 1)
        # z=1 is an implicit Euler pole, not a valid numerical update.
        self.assertEqual((1-1)**2, 0)

    def test_leading_coefficients(self):
        h = 1e-3
        e = exact(h)
        l = lie(h)
        s = strang(h)
        # Lie defect: diag(+1/2,-1/2)*h^2 + O(h^3).
        self.assertAlmostEqual((l[0][0]-e[0][0])/h**2, 0.5, places=3)
        self.assertAlmostEqual((l[1][1]-e[1][1])/h**2, -0.5, places=3)
        # Strang defect: (0,1/12;-1/6,0)*h^3 + O(h^4).
        self.assertAlmostEqual((s[0][1]-e[0][1])/h**3, 1/12, places=4)
        self.assertAlmostEqual((s[1][0]-e[1][0])/h**3, -1/6, places=4)

    def test_local_defect_slopes(self):
        hs = (0.01, 0.005)
        for method, order in ((lie, 2), (strang, 3)):
            errors = [frobenius(method(h), exact(h)) for h in hs]
            slope = math.log(errors[0]/errors[1]) / math.log(hs[0]/hs[1])
            self.assertAlmostEqual(slope, order, delta=0.03)

    def test_wolfram_grid_bounds(self):
        # Wolfram Range[-3,-.25,.2] stops at -0.4, not -0.25.
        exponents = [-3 + 0.2*i for i in range(14)]
        self.assertAlmostEqual(exponents[-1], -0.4, places=12)
        self.assertEqual(len(exponents), 14)


if __name__ == "__main__":
    unittest.main()
