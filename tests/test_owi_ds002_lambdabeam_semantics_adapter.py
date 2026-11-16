"""Exact source-pinned 28-head ABI-preserving Access/Scanl1 runtime adapter tests."""
import os
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
import owi_ds002_exedec_admission as adm
import owi_ds002_lambdabeam_native_bridge as strict
import owi_ds002_lambdabeam_semantics_adapter as adapted


def upstream():
    return Path(os.environ.get("LAMBDABEAM_SOURCE",
        "build/owi_ds002/lambdabeam_native_source"))


class ExactAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original,cls.corrected,cls.provenance=adapted.load_adapted_operators(upstream())
        cls.before={repr(op):op for op in cls.original}
        cls.after={repr(op):op for op in cls.corrected}

    def test_original_head_binding_and_operation_abi_unchanged(self):
        self.assertEqual(len(self.original),28)
        self.assertEqual(len(self.corrected),28)
        self.assertEqual([repr(x) for x in self.original],
                         [repr(x) for x in self.corrected])
        self.assertEqual([x.name for x in self.original],
                         [x.name for x in self.corrected])
        self.assertEqual([x.arity for x in self.original],
                         [x.arity for x in self.corrected])
        self.assertEqual([x.num_bound_variables for x in self.original],
                         [x.num_bound_variables for x in self.corrected])
        self.assertEqual([x.weight for x in self.original],
                         [x.weight for x in self.corrected])
        self.assertEqual(self.provenance["source"]["commit"],
                         "61986dc1a6d8cc9521fb17e3152f7f085b5d7c95")
        for name in self.before:
            if name not in ("Access","Scanl1"):
                self.assertIs(self.before[name],self.after[name])
            else:
                self.assertIsNot(self.before[name],self.after[name])

    def test_default_original_translation_still_fail_closed(self):
        with self.assertRaises(adm.Rejected):
            strict.translate("Access(x0,x1)",{"x0":"I","x1":"L"})
        with self.assertRaises(adm.Rejected):
            strict.translate("Scanl1(lambda u1,u2:Add(u1,u2),x0)",{"x0":"L"})
        for expr,types in (("Access(x0,x1)",{"x0":"I","x1":"L"}),
                           ("Scanl1(lambda u1,u2:Add(u1,u2),x0)",{"x0":"L"})):
            with self.subTest(expr=expr):
                candidate=strict.translate(expr,types,semantics=adapted.SEMANTICS)
                self.assertEqual(len(adm.compile_program(candidate,list(types),types)),1)
        with self.assertRaises(adm.Rejected):
            strict.translate("Scanl1(lambda u1,u2:Sum(u1),x0)",
                             {"x0":"L"},semantics=adapted.SEMANTICS)
        with self.assertRaises(adm.Rejected):
            strict.translate("Scanl1(lambda u1,u2:Add(u1,u2),x0)",
                             {"x0":"L"},semantics="secretly_original")

    def test_original_and_adapter_explicit_empty_and_negative_divergences(self):
        self.assertEqual(self.before["Access"].apply_single([-1,[1,2]]),2)
        self.assertIsNone(self.after["Access"].apply_single([-1,[1,2]]))
        self.assertIsNone(self.after["Access"].apply_single([10,[1,2]]))
        self.assertIsNone(self.after["Access"].apply_single([0,[]]))
        self.assertEqual(self.after["Access"].apply_single([1,[1,2]]),2)
        self.assertEqual(self.after["Scanl1"].apply_single(
            [self.after["Add"].apply_single,[]]),[])
        with self.assertRaises(IndexError):
            self.before["Scanl1"].apply_single([self.before["Add"].apply_single,[]])

    def test_original_bound_wider_than_exact_adapted_scanl1(self):
        multiply=lambda a,b:self.before["Multiply"].apply_single([a,b])
        self.assertEqual(self.before["Scanl1"].apply_single([multiply,[8,8]]),
                         [8,64])
        self.assertIsNone(self.after["Scanl1"].apply_single([multiply,[8,8]]))
        self.assertEqual(self.after["Scanl1"].apply_single([multiply,[2,3,4]]),
                         [2,6,24])
        self.assertIsNone(self.after["Scanl1"].apply_single([multiply,[3,4,5]]))
        self.assertIsNone(self.after["Scanl1"].apply_single([multiply,[51]]))
        self.assertEqual(self.after["Scanl1"].apply_single([multiply,[0]]),[0])

    def test_all_38_fixed_legal_atomic_types_have_explicit_translations(self):
        rows=adapted.expanded_witnesses()
        self.assertEqual(len(rows),38)
        self.assertEqual(sum(op=="Scanl1" for op,_,_,_ in rows),5)
        self.assertEqual(sum(op=="Access" for op,_,_,_ in rows),1)
        for op,lam,expr,types in rows:
            with self.subTest(op=op,lambda_token=lam):
                dst=strict.translate(expr,types,semantics=adapted.SEMANTICS)
                compiled=adm.compile_program(dst,list(types),types)
                self.assertEqual(compiled[-1][1],op)
                if lam:
                    self.assertEqual(compiled[-1][2][0],lam)

    def test_original_source_vs_adapted_semantics_exact_executable_replay(self):
        r=adapted.execute_matched_witnesses(upstream(),cache=None)
        self.assertEqual(r["status"],
                         "EXPLICIT_28HEAD_SEMANTIC_ADAPTER_38_ATOMS_SOURCE_WITNESSED")
        self.assertEqual(r["audit"]["accepted_exe_dec_fixed_atoms"],38)
        self.assertEqual(r["audit"]["source_native_vs_exedec_finite_probe_pairs"],671)
        self.assertEqual(r["audit"]["mismatches"],0)
        self.assertEqual(r["adaptation"]["original_operator_head_count"],28)
        self.assertEqual(r["adaptation"]["adapted_operator_head_count"],28)
        self.assertFalse(r["adaptation"]["original_source_bytes_modified"])
        self.assertFalse(r["adaptation"]["checkpoint_loaded"])
        self.assertFalse(r["adaptation"]["trained_search_executed"])
        self.assertEqual(len(r["witnesses"]),38)

    def test_adapted_source_rejects_closure_and_unrecognized_lambda(self):
        for expr,typ in (
            ("Scanl1(lambda u1,u2:Add(u1,z),x0)",{"x0":"L"}),
            ("Scanl1(lambda u1,u2:Greater(u1,u2),x0)",{"x0":"L"}),
            ("Scanl1(lambda u1,u2:__import__('os'),x0)",{"x0":"L"}),
            ("Scanl1(lambda u1,u2:Add(u2,u1),y0)",{"x0":"L"}),
            ("Access(-1,x0)",{"x0":"L"}),
        ):
            with self.subTest(expr=expr),self.assertRaises(adm.Rejected):
                strict.translate(expr,typ,semantics=adapted.SEMANTICS)

    def test_execute_mode_is_explicit_and_no_original_behavior_regresses(self):
        vals={"x0":[]}
        expr="Scanl1(lambda u1,u2:Add(u1,u2),x0)"
        with self.assertRaises(adm.Rejected):
            strict.native_execute(expr,vals,self.after)
        self.assertEqual(strict.native_execute(expr,vals,self.after,
                         semantics=adapted.SEMANTICS),[])
        with self.assertRaises(adm.Rejected):
            strict.native_execute(expr,vals,self.after,
                                  semantics="unvalidated-model-weights")

if __name__=="__main__":
    unittest.main()
