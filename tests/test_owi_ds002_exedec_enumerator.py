"""Source-blind initial outcome-only enumerator: accuracy, no-leak and budgets."""
from pathlib import Path
import importlib.util
import sys
import unittest
from unittest.mock import patch

MODULE_DIR = Path(__file__).resolve().parents[1] / "experiments"
sys.path.insert(0, str(MODULE_DIR))
import owi_ds002_exedec_admission as adm
import owi_ds002_exedec_enumerator as enum


def problem():
    return {"inputs": {"x0": [[1, -2], [0, 3], [-4]]},
            "outputs": [[2, -1], [1, 4], [-3]],
            "program": "x0 = INPUT | x1 = Map (+1) x0"}


def public():
    return adm.participant_view("NONE", {"index": 17, "test_problem": problem()})


class EnumerationGates(unittest.TestCase):
    def test_complete_discrete_program_and_local_replay(self):
        p = public()
        result = enum.synthesize(p, seed=1, max_nodes=2, max_evals=3000)
        self.assertEqual(result["status"], "PUBLIC_IO_CANDIDATE_FOUND", result)
        candidate = result["program"]
        names, types, n = adm.validate_examples(p)
        compiled = adm.compile_program(candidate, names, types)
        self.assertTrue(all(adm.execute(compiled, {v: p["inputs"][v][i] for v in names})
                            == p["outputs"][i] for i in range(n)))
        self.assertLessEqual(result["counts"]["attempts"], 3000)

    def test_strong_guards_no_private_evaluator_or_reference(self):
        p = public()
        for private in ("program", "hidden_test", "reference", "fault_identity"):
            with self.subTest(private=private), self.assertRaises(adm.Rejected):
                enum.synthesize({**p, private: "secret"}, seed=1)
        with self.assertRaises(adm.Rejected):
            enum.synthesize({**p, "target_program_exposed": True}, seed=1)

    def test_fixed_budget_and_seeded_replay(self):
        p = public()
        x = enum.synthesize(p, seed=9, max_nodes=3, max_evals=90, max_width=15)
        y = enum.synthesize(p, seed=9, max_nodes=3, max_evals=90, max_width=15)
        self.assertEqual(x["program"], y["program"])
        self.assertEqual(x["counts"], y["counts"])
        self.assertLessEqual(x["counts"]["attempts"], 90)
        self.assertEqual(len(x["counts"]["per_layer_attempts"]), 3)

    def test_grammatical_catalog_and_extraction_typecheck(self):
        names, types, _ = adm.validate_examples(public())
        x = enum.Expr("L", ([1, 2], [3], [4]), 0, name="x0")
        inner = enum.Expr("L", ([2, 3], [4], [5]), 1, op="Map",
                          lam="(+1)", children=(x,))
        outer = enum.Expr("L", ([3, 2], [4], [5]), 2,
                          op="Reverse", children=(inner,))
        expression = enum.extract(outer, names)
        self.assertEqual(expression, "x0 = INPUT | x1 = Map (+1) x0 | x2 = Reverse x1")
        self.assertIsInstance(adm.compile_program(expression, names, types), list)

    def test_eval_count_and_invalid_case(self):
        x = enum.Expr("L", ([], [2], [3]), 0, name="x0")
        self.assertIsNone(enum._evaluate("Head", "", (x,), 3))
        self.assertEqual(enum._evaluate("Reverse", "", (x,), 3),
                         ([], [2], [3]))

    def test_independent_evaluator_only_after_search(self):
        item = {"index": 17, "test_problem": problem(),
                "few_shot_examples": [{"program": "private"}] * 4}
        fake_verify = {"status": "BOUNDED_EXECUTION_AGREEMENT_ONLY"}
        with patch.object(adm, "source_rows", return_value=([item] * 18, "0" * 40)):
            with patch.object(adm, "verify", return_value=fake_verify) as gate:
                result = enum.run(["NONE"], [17], [1], cache=Path("unused"),
                                  offline=True, max_nodes=2, max_evals=3000,
                                  max_width=200, probes=16)
        self.assertEqual(result["aggregate"]["cases"], 1)
        self.assertEqual(result["aggregate"]["bounded_verified"], 1)
        self.assertEqual(gate.call_count, 1)
        self.assertEqual(result["records"][0]["search"]["status"], "PUBLIC_IO_CANDIDATE_FOUND")

    def test_reject_unexpected_command_args(self):
        with self.assertRaises(ValueError):
            enum._list_argument("NONE,NONE", set(enum.DEFAULT_SPLITS), "splits")
        with self.assertRaises(ValueError):
            enum._list_argument("evil", set(enum.DEFAULT_SPLITS), "splits")


if __name__ == "__main__":
    unittest.main()
