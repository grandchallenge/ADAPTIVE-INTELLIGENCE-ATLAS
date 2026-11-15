"""Historical DeepCoder external candidate and source-semantic boundary tests."""
import sys
from pathlib import Path
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
import owi_ds002_exedec_admission as adm
import owi_ds002_exedec_legacy_solver as ext

class SourceGate(unittest.TestCase):
    def test_convert_official_solution_shape_to_typed_candidate(self):
        s="Solved!\nNodes explored: 53084\nSolution:\n %2 <- sort %1\n %3 <- arr_head %1\n %4 <- access %3 %2\n"
        actual=ext.extract(s,["x0","x1"])
        self.assertEqual(actual,"x0 = INPUT | x1 = INPUT | x2 = Sort x1 | x3 = Head x1 | x4 = Access x3 x2")
        adm.compile_program(actual,["x0","x1"],{"x0":"I","x1":"L"})

    def test_solver_output_must_not_execute_arbitrary_code(self):
        bad=["Solved!\n","Solved!\nSolution:\n %1 <- system %0\n",
             "Solved!\nSolution:\n %1 <- reverse %7\n",
             "Solved!\nSolution:\n %1 <- zipwith_add %0\n"]
        for s in bad:
            with self.subTest(s=s),self.assertRaises(adm.Rejected):
                ext.extract(s,["x0"])
        self.assertIsNone(ext.extract("Failed!\nNodes explored: 9\n",["x0"]))

    def test_public_fixture_removes_reference_program(self):
        program={"inputs":{"x0":[[-3,1],[2,4],[]]},
                 "outputs":[[-2,2],[3,5],[]],
                 "program":"x0 = INPUT | x1 = Map (+1) x0"}
        view=adm.participant_view("NONE",{"index":0,"test_problem":program})
        prior="".join("1 "+v+"\n" for v in
            "ZIPWITH * MAP SQR MUL4 DIV4 - MUL3 DIV3 MIN + SCANL SHR SHL MAX HEAD DEC SUM doNEG isNEG INC LAST MINIMUM isPOS SORT FILTER isODD REVERSE ACCESS isEVEN COUNT TAKE MAXIMUM DROP".split())
        with tempfile.TemporaryDirectory() as d:
            dest=Path(d)/"fixture"
            ext.write_fixture(view,dest,1,prior)
            self.assertEqual((dest/"input_types.txt").read_text(),"Array\n")
            self.assertEqual((dest/"input_values.txt").read_text(),"-3 1\n2 4\n\n")
            self.assertNotIn("program",(dest/"input_values.txt").read_text())
            self.assertTrue((dest/"random_ordering_1.txt").is_file())

    def test_external_semantics_not_identical_to_exedec(self):
        # C++ negative integer division truncates toward zero; ExeDec floors.
        self.assertNotEqual(int(-3/2),adm.UNARY["(/2)"](-3))
        self.assertEqual(ext.OPS["map_div2"],("Map","(/2)"))
        self.assertEqual(ext.UPSTREAM,"794057dc41aab0bea3818b75416da06b25aff12f")
        self.assertEqual(len(ext.BLOBS),6)

if __name__=="__main__":
    unittest.main()
