"""Source-bound LambdaBeam original enumerator and ExeDec semantic bridge tests."""
from pathlib import Path
import os
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
import owi_ds002_exedec_admission as adm
import owi_ds002_exedec_lambdabeam_external as ext


def source():
    return Path(os.environ.get("LAMBDABEAM_SOURCE","build/owi_ds002/lambdabeam_source"))


def public(program,inputs,outputs):
    return adm.participant_view("NONE",{"index":0,"test_problem":{
        "program":program,"inputs":inputs,"outputs":outputs}})


class OfficialSearchBridgeTests(unittest.TestCase):
    def test_exact_pinned_source_and_import(self):
        r=ext.check_source(source())
        self.assertEqual(r["commit"],ext.SOURCE)
        self.assertEqual(r["verified_git_blobs"],8)
        algorithm,variables,opbase,value,task=ext.load(source())
        self.assertTrue(algorithm.__file__.endswith(
            "lambdabeam/algorithm/baseline_enumeration.py"))

    def test_all_exact_exedec_operations_and_lambda_bindings(self):
        _,_,base,_,_=ext.load(source())
        domain=ext.make_domain(base)
        expected=sum(len(adm.UNARY) if "U" in sig
                     else len(adm.PRED) if "P" in sig
                     else len(adm.BINARY) if "B" in sig else 1
                     for sig,_ in adm.OPERATIONS.values())
        self.assertEqual(len(domain.operations),expected)
        for operation in domain.operations:
            sig,typ=adm.OPERATIONS[operation.exedec_op]
            self.assertEqual(operation.result_type,typ)
            self.assertEqual(tuple(c for c in sig if c in "IL"),
                             operation.register_types)
            self.assertEqual(
                tuple(int if c=="I" else list for c in operation.register_types),
                operation.arg_types())

    def test_negative_division_and_undefined_operations(self):
        _,_,base,_,_=ext.load(source())
        ops=ext.make_domain(base).operations
        div=next(o for o in ops if o.exedec_op=="Map" and
                 o.exedec_lambda=="(/2)")
        head=next(o for o in ops if o.exedec_op=="Head")
        acc=next(o for o in ops if o.exedec_op=="Access")
        self.assertEqual(div.apply_single([[-3,3]]),[-2,1])
        self.assertIsNone(head.apply_single([[]]))
        self.assertIsNone(acc.apply_single([-1,[3,4]]))
        self.assertIsNone(div.apply_single([[50,50,50,50,50,50]]))

    def test_source_cannot_reach_external_algorithm(self):
        p=public("x0 = INPUT | x1 = Reverse x0",
                 {"x0":[[2,1],[4,3],[0,-1]]},
                 [[1,2],[3,4],[-1,0]])
        for name in ("program","reference","evaluator","hidden","gradient"):
            with self.subTest(name=name),self.assertRaises(adm.Rejected):
                ext.synthesize({**p,name:"private"},source(),seed=1,
                               max_weight=4,max_explored=500,timeout=1.)
        with self.assertRaises(adm.Rejected):
            ext.synthesize({**p,"target_program_exposed":True},source(),
                           seed=1,max_weight=4,max_explored=500,timeout=1.)

    def test_original_search_executes_real_one_step_program(self):
        p=public("x0 = INPUT | x1 = Reverse x0",
                 {"x0":[[2,1],[4,3],[0,-1]]},
                 [[1,2],[3,4],[-1,0]])
        r=ext.synthesize(p,source(),seed=3,max_weight=3,
                         max_explored=1500,timeout=5.)
        self.assertEqual(r["status"],"PUBLIC_IO_CANDIDATE_FOUND",r)
        names,types,n=adm.validate_examples(p)
        compiled=adm.compile_program(r["candidate"],names,types)
        self.assertTrue(all(adm.execute(compiled,
                    {k:p["inputs"][k][j] for k in names})==p["outputs"][j]
                    for j in range(n)))
        self.assertLessEqual(r["counts"]["num_values_explored"],1500)

    def test_external_candidate_is_replayable_exact_typed_program(self):
        p=public("x0 = INPUT | x1 = Map (+1) x0",
                 {"x0":[[2,1],[-3,0],[5,2]]},
                 [[3,2],[-2,1],[6,3]])
        r=ext.synthesize(p,source(),seed=1,max_weight=4,
                         max_explored=1800,timeout=5.)
        self.assertEqual(r["status"],"PUBLIC_IO_CANDIDATE_FOUND",r)
        name,typ,n=adm.validate_examples(p)
        compiled=adm.compile_program(r["candidate"],name,typ)
        self.assertEqual(adm.execute(compiled,{"x0":[-3,0]}),[-2,1])

if __name__=="__main__":
    unittest.main()
