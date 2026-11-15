#!/usr/bin/env python3
"""cvc5 reference output must pass independent Z3 candidate admission."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments"))
from owi_ds002_sygus_admission import AdmissionError
from owi_ds002_sygus_reference import extract_solution


class Tests(unittest.TestCase):
    def test_extract_single_valid_sygus_definition(self):
        output = """success
        (
         (define-fun inv-f ((x Int)) Bool (and (>= x 0) (<= x 100)))
        )"""
        self.assertEqual(extract_solution(output, ["x"]),
                         "(and (>= x 0) (<= x 100))")

    def test_reject_missing_duplicate_and_untrusted_constructs(self):
        for output in (
            "unknown",
            "(define-fun z ((x Int)) Bool true)",
            "(define-fun inv-f ((y Int)) Bool true)",
            "(define-fun inv-f ((x Int)) Bool (pre-f x))",
            "(define-fun inv-f ((x Int)) Bool true) "
            "(define-fun inv-f ((x Int)) Bool false)",
        ):
            with self.subTest(output=output):
                with self.assertRaises(AdmissionError):
                    extract_solution(output, ["x"])

    def test_reject_non_boolean_and_primed_solution(self):
        for output in (
            "(define-fun inv-f ((x Int)) Int (+ x 1))",
            "(define-fun inv-f ((x Int)) Bool (= x x!))",
        ):
            with self.assertRaises(AdmissionError):
                extract_solution(output, ["x"])


if __name__ == "__main__":
    unittest.main()
