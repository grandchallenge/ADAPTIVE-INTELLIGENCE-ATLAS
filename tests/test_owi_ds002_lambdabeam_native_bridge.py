"""OWI-DS002 original LambdaBeam native program -> exact ExeDec fail-closed bridge."""
import ast
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
import owi_ds002_exedec_admission as adm
import owi_ds002_lambdabeam_native_bridge as native


class NativeBridgeTests(unittest.TestCase):
    def test_all_admitted_source_atomic_operations_are_total_syntactic_witnesses(self):
        witnesses=native.witness_expressions()
        self.assertEqual(len(witnesses),32)
        seen=set()
        for op,token,expr,types in witnesses:
            with self.subTest(op=op,token=token):
                result=native.translate(expr,types)
                names=list(types)
                compiled=adm.compile_program(result,names,types)
                self.assertEqual(compiled[-1][1],op)
                if token:
                    self.assertEqual(compiled[-1][2][0],token)
                self.assertNotIn((op,token),seen)
                seen.add((op,token))

    def test_negative_index_and_empty_scan_denied(self):
        with self.assertRaisesRegex(adm.Rejected,"outside source-exact"):
            native.translate("Access(x0, x1)",{"x0":"I","x1":"L"})
        with self.assertRaisesRegex(adm.Rejected,"outside source-exact"):
            native.translate("Scanl1(lambda u1,u2: Add(u1,u2), x0)",{"x0":"L"})

    def test_scalar_unary_lambda_exact_floor_and_source_precedence(self):
        for expr,token in (
           ("Map(lambda u1: IntDivide(u1,2), x0)","(/2)"),
           ("Map(lambda u1: Multiply(u1,-1), x0)","(*(-1))"),
           ("Map(lambda u1: (lambda v1: Add(v1,1))(u1), x0)","(+1)"),
           ("Map(lambda u1: Add(1,u1), x0)","(+1)"),
           ("Map(lambda u1: Multiply(u1,u1), x0)","(**2)"),
           ("Map(lambda u1: Subtract(0,u1), x0)","(*(-1))"),
        ):
            with self.subTest(expression=expr):
                program=native.translate(expr,{"x0":"L"})
                self.assertEqual(
                    adm.compile_program(program,["x0"],{"x0":"L"})[-1][2][0],
                    token)
        pgm=native.translate("Map(lambda u1: IntDivide(u1,2), x0)",{"x0":"L"})
        self.assertEqual(adm.execute(adm.compile_program(pgm,["x0"],{"x0":"L"}),
                                     {"x0":[-3,3]}),[-2,1])

    def test_predicate_and_binary_exact_native_rewrites(self):
        for expr,token in (
          ("Filter(lambda u1: Greater(0, u1),x0)","(<0)"),
          ("Count(lambda u1: IsEven(u1),x0)","(%2==0)"),
          ("ZipWith(lambda u1,u2: Max(u2,u1),x0,x1)","(max)"),
          ("ZipWith(lambda u1,u2: Subtract(u1,u2),x0,x1)","(-)"),
        ):
            types={"x0":"L","x1":"L"} if expr.startswith("ZipWith") else {"x0":"L"}
            self.assertEqual(adm.compile_program(
                native.translate(expr,types),list(types),types)[-1][2][0],token)

    def test_nested_pipeline_is_typed_and_roundtrips_to_source_exact(self):
        program=native.translate(
            "Sort(Reverse(Map(lambda u1: Add(u1,1),x0)))",{"x0":"L"})
        self.assertEqual(adm.execute(
            adm.compile_program(program,["x0"],{"x0":"L"}),
            {"x0":[3,-1,2]}),[0,3,4])
        self.assertEqual(len(program.split("|")),4)

    def test_native_higher_order_dynamic_capture_rejected(self):
        expressions=(
            "Map(lambda u1: Add(x0,u1),x1)",
            "Map(lambda u1: (lambda v1: Add(x0,v1))(u1), x1)",
            "Filter(lambda u1: Greater(u1,x0),x1)",
            "Map(lambda u1: Add(Add(u1,1),1),x1)",
            "Map(lambda u1: IntDivide(u1, -1),x1)",
            "Map(lambda u1: Multiply(u1,0),x1)",
        )
        for expr in expressions:
            with self.subTest(expression=expr),self.assertRaises(adm.Rejected):
                native.translate(expr,{"x0":"I","x1":"L"})

    def test_native_program_code_injection_and_unknown_syntax_rejected(self):
        values=(
          "__import__('os').system('id')","open('/etc/passwd').read()",
          "Reverse(x0).__class__","x0[0]","(lambda x:x)(x0)",
          "Map(lambda u1: __import__('os'),x0)",
          "Reverse(x0,evil=True)", "Reverse(x0) or Sort(x0)",
          "Count(lambda u1: IsEven(u1), [1,2,3])",
          "Reverse(x0)\nPrint('boom')",
          "Reverse(x0"+" "*2500+")",
          "Map(lambda *x: Square(x), x0)",
        )
        for expr in values:
            with self.subTest(expression=expr),self.assertRaises(adm.Rejected):
                native.translate(expr,{"x0":"L"})

    def test_wrong_type_and_unbound_vars_rejected(self):
        for expr,types in (
          ("Head(x0)",{"x0":"I"}),
          ("Take(x0,x1)",{"x0":"L","x1":"L"}),
          ("Reverse(y)",{"x0":"L"}),
          ("Reverse(x0)",{"x1":"L"}),
          ("Reverse(x0)",{"x0":"L","x2":"I"}),
        ):
            with self.subTest(expr=expr),self.assertRaises(adm.Rejected):
                native.translate(expr,types)

    def test_excess_nodes_and_lines_rejected_without_partial_program(self):
        expr="x0"
        for i in range(16):
            expr="Reverse("+expr+")"
        with self.assertRaises(adm.Rejected):
            native.translate(expr,{"x0":"L"})
        with self.assertRaises(adm.Rejected):
            native.translate("Reverse(x0)"*100,{"x0":"L"})

    def test_participant_view_enforces_no_reference_leakage(self):
        p={"status":"PARTICIPANT_VIEW_ONLY","task_id":"NONE:0",
           "inputs":{"x0":[[1,2],[3,4]]},"outputs":[[2,1],[4,3]],
           "target_program_exposed":False,"input_output_examples":2}
        good=native.transfer_candidate("Reverse(x0)",p)
        self.assertEqual(good["status"],"PUBLIC_IO_CANDIDATE_FOUND")
        self.assertTrue(good["participant_only"])
        for field in ("reference","program","hidden","gradient","evaluator","private"):
            with self.subTest(field=field),self.assertRaises(adm.Rejected):
                native.transfer_candidate("Reverse(x0)",{**p,field:1})
        with self.assertRaises(adm.Rejected):
            native.transfer_candidate("Reverse(x0)",
                                     {**p,"target_program_exposed":True})
        mismatch=native.transfer_candidate("Sort(x0)",p)
        self.assertEqual(mismatch["status"],"REJECTED_PUBLIC_EXAMPLE")
        self.assertIsNone(mismatch["candidate"])

    def test_actual_original_upstream_demo_closure_requires_rejection(self):
        # This exact expression is the pinned original upstream benchmark test:
        # its delta is a dynamic task input, NOT an ExeDec fixed lambda.
        original=("Map(lambda u1: (lambda v1: Add(delta, v1))(u1), lst)")
        with self.assertRaises(adm.Rejected):
            native.translate(original,{"x0":"I","x1":"L"})

    def test_fixed_lambda_bound_argument_substitution_is_capture_safe(self):
        source=("Map(lambda u1: (lambda v1: Add(1,v1))(u1),x0)")
        self.assertEqual(adm.compile_program(
            native.translate(source,{"x0":"L"}),["x0"],{"x0":"L"})[-1][2][0],
            "(+1)")
        with self.assertRaises(adm.Rejected):
            native.translate("Map(lambda u1: (lambda v1: Add(v1,v1))(u1), x0)",
                             {"x0":"L"})
        with self.assertRaises(adm.Rejected):
            native.translate("Map(lambda u1: (lambda v1: Add(v1,1))(x0),x0)",
                             {"x0":"L"})


    def test_candidate_receipt_executes_reference_only_after_valid_public_candidate(self):
        from unittest import mock
        from pathlib import Path
        # Reference program deliberately not a valid executable statement;
        # its existence must not influence search translation.
        source=[{"index":0,"test_problem":{
            "inputs":{"x0":[[1,2],[3,4]]},
            "outputs":[[2,1],[4,3]],
            "program":"CONFIDENTIAL_REFERENCE_DO_NOT_READ"}}]
        records=[
            {"split":"NONE","index":0,"native_expression":"Reverse(x0)"},
            {"split":"NONE","index":0,"native_expression":"Sort(x0)"},
            {"split":"NONE","index":0,"native_expression":"__import__('os')"},
        ]
        with mock.patch.object(native.adm,"source_rows",return_value=(source,"pinnedblob")),mock.patch.object(
            native.adm,"verify",return_value={"status":"BOUNDED_EXECUTION_AGREEMENT_ONLY"}) as checker:
            report=native.check_candidates(records,Path("unused"),offline=True)
        self.assertEqual(report["count"],3)
        self.assertEqual(report["bounded_verified"],1)
        self.assertEqual([r["outcome"]["status"] for r in report["records"]],[
            "PUBLIC_IO_CANDIDATE_FOUND",
            "REJECTED_PUBLIC_EXAMPLE",
            "REJECTED_NATIVE_TRANSLATION",
        ])
        self.assertEqual(checker.call_count,1)
        args=checker.call_args.args
        self.assertEqual(args[:2],("NONE",0))
        self.assertEqual(args[2],"x0 = INPUT | x1 = Reverse x0")
        self.assertNotIn("CONFIDENTIAL",args[2])


if __name__=="__main__":
    unittest.main()
