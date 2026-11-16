"""Executable source-semantics-exact register search and confidentiality gates."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
import owi_ds002_exedec_admission as adm
import owi_ds002_exedec_register_search as reg


def view(program,inputs,outputs):
    return adm.participant_view("NONE",{"index":0,"test_problem":{
        "program":program,"inputs":inputs,"outputs":outputs}})


class RegisterSearchTests(unittest.TestCase):
    def test_actual_one_step_typed_search(self):
        p=view("x0 = INPUT | x1 = Reverse x0",
               {"x0":[[1,2,3],[4,5],[-2,0]]},
               [[3,2,1],[5,4],[0,-2]])
        result=reg.synthesize(p,seed=1,max_nodes=1,max_evals=1000,
                              beam_width=32,time_limit_seconds=5.)
        self.assertEqual(result["status"],"PUBLIC_IO_CANDIDATE_FOUND",result)
        self.assertLessEqual(result["counts"]["attempted_successors"],1000)
        names,typ,n=adm.validate_examples(p)
        code=adm.compile_program(result["program"],names,typ)
        self.assertEqual([adm.execute(code,{"x0":p["inputs"]["x0"][j]})
                          for j in range(n)],p["outputs"])

    def test_binary_zipwith_operands_have_source_types(self):
        p=view("x0 = INPUT | x1 = INPUT | x2 = ZipWith (+) x0 x1",
               {"x0":[[1,2],[4,3],[-2,1]],
                "x1":[[3,4],[0,8],[1,1]]},
               [[4,6],[4,11],[-1,2]])
        result=reg.synthesize(p,seed=3,max_nodes=1,max_evals=1500,
                              beam_width=20,time_limit_seconds=5.)
        self.assertEqual(result["status"],"PUBLIC_IO_CANDIDATE_FOUND",result)
        names,typ,n=adm.validate_examples(p)
        code=adm.compile_program(result["program"],names,typ)
        self.assertTrue(all(adm.execute(code, {x:p["inputs"][x][j] for x in names})
                            ==p["outputs"][j] for j in range(n)))

    def test_shared_subexpression_register_dag(self):
        root=reg.State(("L",),(([-3,2],[4,1],[0,2]),),())
        a=reg._apply(root,"Map",("(+1)","x0"),"L")
        self.assertEqual(a,([-2,3],[5,2],[1,3]))
        child=reg.State(("L","L"),root.observations+(a,),
                        (("x1","Map",("(+1)","x0")),))
        b=reg._apply(child,"ZipWith",("(+)","x1","x1"),"L")
        self.assertEqual(b,([-4,6],[10,4],[2,6]))
        candidate=reg._to_program(["x0"],child.statements+(
            ("x2","ZipWith",("(+)","x1","x1")),))
        code=adm.compile_program(candidate,["x0"],{"x0":"L"})
        self.assertEqual(adm.execute(code,{"x0":[-3,2]}),[-4,6])

    def test_negative_floor_division_and_bounded_invalid(self):
        root=reg.State(("L",),(([-3,3],[1,2],[0,4]),),())
        obs=reg._apply(root,"Map",("(/2)","x0"),"L")
        self.assertEqual(obs,([-2,1],[0,1],[0,2]))
        bad=reg.State(("L",),(([],[1],[3]),),())
        self.assertIsNone(reg._apply(bad,"Head",("x0",),"I"))
        oversized=reg.State(("L",),(([40],[50],[1]),),())
        self.assertIsNone(reg._apply(oversized,"Map",("(*3)","x0"),"L"))

    def test_source_private_field_must_be_rejected(self):
        p=view("x0 = INPUT | x1 = Reverse x0",
               {"x0":[[1],[2],[3]]},[[1],[2],[3]])
        for key in ("program","reference","evaluator","gradients","source_target"):
            with self.subTest(key=key),self.assertRaises(adm.Rejected):
                reg.synthesize({**p,key:"private"},seed=1,max_nodes=1)
        with self.assertRaises(adm.Rejected):
            reg.synthesize({**p,"target_program_exposed":True},seed=1)

    def test_finite_budget_and_seeded_determinism(self):
        p=view("x0 = INPUT | x1 = Filter (>0) x0",
               {"x0":[[-2,4,3],[0,-3,1],[-1,-2,4]]},
               [[4,3],[1],[4]])
        r1=reg.synthesize(p,seed=7,max_nodes=3,max_evals=95,
                          beam_width=12,time_limit_seconds=5.)
        r2=reg.synthesize(p,seed=7,max_nodes=3,max_evals=95,
                          beam_width=12,time_limit_seconds=5.)
        self.assertEqual(r1["program"],r2["program"])
        self.assertEqual(r1["counts"],r2["counts"])
        self.assertLessEqual(r1["counts"]["attempted_successors"],95)

    def test_prevents_mutating_governed_source(self):
        self.assertEqual(len(reg._plans(2)),len(reg._plans(2)))
        self.assertEqual(reg._plans(2),reg._plans(2))
        self.assertNotEqual(reg._plans(2),reg._plans(3))
        self.assertTrue(all(x[0] in adm.OPERATIONS for x in reg._plans(3)))

if __name__=="__main__":
    unittest.main()
