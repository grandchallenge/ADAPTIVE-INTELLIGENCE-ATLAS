"""OWI-DS002 independent typed parser and bounded execution safety gates."""
import importlib.util
from pathlib import Path
import unittest

MODULE = Path(__file__).resolve().parents[1] / "experiments/owi_ds002_exedec_admission.py"
spec = importlib.util.spec_from_file_location("owi_ds002_exedec_admission", MODULE)
ds = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ds)


class TypedExecutionTests(unittest.TestCase):
    def test_faithful_composition(self):
        src = "x0 = INPUT | x1 = Map (+1) x0 | x2 = Reverse x1 | x3 = Sum x2"
        code = ds.compile_program(src, ["x0"], {"x0": "L"})
        self.assertEqual(ds.execute(code, {"x0": [3, -2, 5]}), 9)

    def test_stateful_fold_and_negative_integer_division(self):
        src = "x0 = INPUT | x1 = Scanl1 (+) x0 | x2 = Map (/2) x1"
        code = ds.compile_program(src, ["x0"], {"x0": "L"})
        self.assertEqual(ds.execute(code, {"x0": [-3, 1, -4]}), [-2, -1, -3])

    def test_conditional_undefined_and_bound_check(self):
        code = ds.compile_program("x0 = INPUT | x1 = Head x0", ["x0"], {"x0": "L"})
        self.assertIsNone(ds.execute(code, {"x0": []}))
        code = ds.compile_program("x0 = INPUT | x1 = Map (**2) x0", ["x0"], {"x0": "L"})
        self.assertIsNone(ds.execute(code, {"x0": [8]}))

    def test_no_untyped_or_uncharged_execution(self):
        bad = (
            "x0 = INPUT | x1 = eval x0",
            "x0 = INPUT | x1 = Map (+1) x1",
            "x0 = INPUT | x1 = Sum x0 | x2 = Reverse x1",
            "x0 = INPUT | x1 = Map (__import__('os')) x0",
            "x0 = INPUT | x1 = Reverse x0 | x1 = Sort x0",
        )
        for src in bad:
            with self.subTest(src=src), self.assertRaises(ds.Rejected):
                ds.compile_program(src, ["x0"], {"x0": "L"})

    def test_reference_consistency_and_public_projection(self):
        p = {"inputs": {"x0": [[1, -2], [0, 3], [-4]]},
             "outputs": [[2, -1], [1, 4], [-3]],
             "program": "x0 = INPUT | x1 = Map (+1) x0"}
        ns, ts, n = ds.validate_examples(p)
        code = ds.compile_program(p["program"], ns, ts)
        self.assertEqual(n, 3)
        self.assertEqual([ds.execute(code, x) for x, _ in ds.examples(p)], p["outputs"])
        proj = ds.participant_view("NONE", {"index": 3, "test_problem": p,
                                             "few_shot_examples": [{"program": "secret"}]})
        self.assertNotIn("program", proj)
        self.assertNotIn("few_shot_examples", proj)
        self.assertFalse(proj["target_program_exposed"])

    def test_source_blobs_and_immutable_manifest(self):
        m = ds.manifest()
        self.assertEqual(len(m["splits"]), 6)
        self.assertEqual(ds.git_blob(b"hi"),
                         "32f95c0d1244a78b2be1bab8de17906fabb2c4a8")
        self.assertEqual(m["origin"]["commit"],
                         "ef046ce2cc3fcd024e32f5dfe00e69700dac82ed")

    def test_reproducible_evaluator_only_probes(self):
        p = {"inputs": {"x0": [[0, 1], [3], []]}, "outputs": [[1, 2], [4], []]}
        a = list(ds.generated_inputs(p, 123))[:12]
        b = list(ds.generated_inputs(p, 123))[:12]
        self.assertEqual(a, b)
        self.assertNotEqual(a, list(ds.generated_inputs(p, 456))[:12])

    def test_real_verification_decision_with_evaluator_custody(self):
        from tempfile import TemporaryDirectory
        from unittest.mock import patch
        p = {"inputs": {"x0": [[1, -2], [0, 3], [-4]]},
             "outputs": [[2, -1], [1, 4], [-3]],
             "program": "x0 = INPUT | x1 = Map (+1) x0"}
        source_row = {"index": 0, "test_problem": p,
                      "few_shot_examples": [{"program": "not for learner"}] * 4}
        with TemporaryDirectory() as tmp:
            with patch.object(ds, "source_rows",
                              return_value=([source_row], "0" * 40)):
                correct = ds.verify("NONE", 0, p["program"], Path(tmp), True)
                wrong = ds.verify("NONE", 0,
                                  "x0 = INPUT | x1 = Map (-1) x0",
                                  Path(tmp), True)
        self.assertEqual(correct["status"], "BOUNDED_EXECUTION_AGREEMENT_ONLY")
        self.assertEqual(correct["independent_valid_cases"], 16)
        self.assertEqual(wrong["status"], "REJECTED_PUBLIC_COUNTEREXAMPLE")
        self.assertNotIn("program", ds.participant_view("NONE", source_row))

    def test_tampered_source_cache_is_rejected_offline(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmp:
            cache = Path(tmp)
            (cache / "NONE.jsonl").write_text("{}\\n", encoding="utf-8")
            with self.assertRaisesRegex(ds.Rejected, "source hash/size mismatch"):
                ds.source_rows("NONE", cache, offline=True)

    def test_source_example_shape_rejected(self):
        with self.assertRaises(ds.Rejected):
            ds.validate_examples({"inputs": {"x0": [[1], ["invalid"]]},
                                  "outputs": [[1], [2]]})


if __name__ == "__main__":
    unittest.main()
