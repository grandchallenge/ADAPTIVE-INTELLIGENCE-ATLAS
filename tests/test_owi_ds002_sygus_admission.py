#!/usr/bin/env python3
"""SyGuS official invariant admission: parser, hash gate, positive/negative VCs.

Positive witnesses are restricted to the *developer* split. Tests do not
publish held-out solutions or use held-out source in candidate selection.
"""
from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments"))
from owi_ds002_sygus_admission import (
    AdmissionError, emit, git_blob, locked_source, manifest_tasks,
    parse, read_task, typecheck, verify)


WITNESSES_DEV_ONLY = {
    "inc": "(and (>= x 0) (<= x 100))",
    "dec": "(and (>= x 0) (<= x 100))",
    "w1": "(and (>= x 0) (<= x n) (>= n 0))",
    "ex11": "(and (>= c 0) (<= c 4))",
    "sum4": "(and (>= i 1) (<= i 9) (= sn (- i 1)))",
}


class PureChecks(unittest.TestCase):
    def test_parser_round_trip(self):
        term = "(and (>= x -50) (<= y (+ x 1)))"
        self.assertEqual(emit(parse(term)[0]), term)
        for bad in ("(and x", ")(", "x )"):
            with self.assertRaises(AdmissionError):
                parse(bad)

    def test_candidate_type_rejects_spec_oracle_and_primed_state(self):
        good = parse("(and (>= x 0) (= (+ x 1) y))")[0]
        self.assertEqual(typecheck(good, {"x", "y"})[0], "Bool")
        for expression in ("(pre-f x)", "(= x x!)", "(+ x 1)",
                           "(and x true)", "(* x y)", "(= x 0) (= y 1)"):
            try:
                nodes = parse(expression)
                if len(nodes) != 1:
                    raise AdmissionError("multiple candidate expressions")
                typecheck(nodes[0], {"x", "y"})
            except AdmissionError:
                continue
            self.fail(f"unsupported candidate passed grammar: {expression}")

    def test_manifest_pinned_splits(self):
        manifest, tasks = manifest_tasks()
        self.assertEqual(len(tasks), 10)
        self.assertEqual(set(k for k,v in tasks.items() if v["split"]=="dev"),
                         set(WITNESSES_DEV_ONLY))
        self.assertEqual(len([t for t in tasks.values() if t["split"]=="heldout"]), 5)

    def test_modified_offline_source_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            folder = Path(td)
            (folder / "inc.sl").write_text("(set-logic LIA)\n")
            with self.assertRaisesRegex(AdmissionError, "source lock mismatch"):
                locked_source("inc", folder, offline=True)

    def test_paired_induction_vcs_not_self_reported(self):
        # Purposefully *not* the origin text: tests parser and signature only.
        spec = """(set-logic LIA)
        (synth-inv inv-f ((x Int)))
        (declare-primed-var x Int)
        (define-fun pre-f ((x Int)) Bool (= x 0))
        (define-fun trans-f ((x Int) (x! Int)) Bool (= x! (+ x 1)))
        (define-fun post-f ((x Int)) Bool (>= x 0))
        (inv-constraint inv-f pre-f trans-f post-f)
        (check-synth)"""
        self.assertEqual(read_task(spec)["vars"], ["x"])


class OfficialSourceAndSolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import z3  # CI pins an independent SMT backend
        cls.cache = Path("build/owi_ds002/sygus2017")
        cls.cache.mkdir(parents=True, exist_ok=True)

    def test_all_ten_competition_tasks_have_exact_pinned_bytes(self):
        _, tasks = manifest_tasks()
        for name, record in tasks.items():
            with self.subTest(task=name):
                source, fetched = locked_source(name, self.cache)
                self.assertEqual(fetched["git_blob_sha"],
                                 git_blob(source.encode("utf-8")))
                self.assertGreaterEqual(len(read_task(source)["vars"]), 1)

    def test_positive_dev_invariants_all_three_vcs_unsat(self):
        for task, expression in WITNESSES_DEV_ONLY.items():
            with self.subTest(task=task):
                report = verify(task, expression, self.cache, offline=True)
                self.assertEqual(report["status"],
                                 "SOLVER_CHECKED_RELATIVE_TO_PINNED_SYGUS_SPEC",
                                 report)
                self.assertEqual(set(report["vcs"]),
                                 {"initiation", "consecution", "safety"})
                self.assertTrue(all(v["result"] == "unsat"
                                    for v in report["vcs"].values()))

    def test_negative_invariants_have_executable_counterexamples(self):
        for term, expected in (
            ("false", "initiation"),
            ("true", "safety"),
            ("(= x 0)", "consecution"),
        ):
            with self.subTest(term=term):
                r = verify("inc", term, self.cache, offline=True)
                self.assertEqual(r["status"], "REJECTED_OR_UNDECIDED")
                self.assertEqual(r["vcs"][expected]["result"], "sat")
                self.assertIn("counterexample", r["vcs"][expected])


if __name__ == "__main__":
    unittest.main()
