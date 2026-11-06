"""ATLAS #448: exact Hopf frequency-domain editorial regressions."""
from fractions import Fraction
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "manuscript/parts/02-mathematical-substrate/ATLAS-CH-DYN-001.md"
SPEC = ROOT / "manuscript/specifications/ATLAS-CH-DYN-001.md"
DERIVATION = ROOT / "mathematics/derivations/ATLAS-CH-DYN-001-DERIVATIONS.md"


def radial_velocity(mu, radius):
    return mu * radius - radius ** 3


class HopfFrequencyScopeTests(unittest.TestCase):
    def test_stationary_circle_at_zero_frequency(self):
        mu = Fraction(1)
        radius = Fraction(1)
        omega = Fraction(0)
        self.assertEqual(radial_velocity(mu, radius), 0)
        self.assertEqual(omega * radius, 0)

    def test_nonzero_angular_motion(self):
        mu = Fraction(1)
        radius = Fraction(1)
        omega = Fraction(2)
        self.assertEqual(radial_velocity(mu, radius), 0)
        self.assertEqual(omega * radius, 2)
        # At omega=2, one full revolution takes pi time units.
        self.assertEqual(Fraction(2, 1) / abs(omega), 1)

    def test_source_declares_frequency_condition(self):
        for source in (CHAPTER, SPEC):
            with self.subTest(source=source):
                text = source.read_text(encoding="utf-8")
                self.assertIn(r"$\\omega\\ne 0$", text)
                self.assertIn("period", text)
                self.assertIn("origin", text)

    def test_derivation_already_has_frequency_hypothesis(self):
        text = DERIVATION.read_text(encoding="utf-8")
        self.assertIn(r"\\omega\\neq0", text)


if __name__ == "__main__":
    unittest.main()
