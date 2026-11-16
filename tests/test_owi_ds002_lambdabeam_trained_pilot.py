"""Controls for original real-checkpoint LambdaBeam neural inference pilot."""
from pathlib import Path
from unittest import mock
import sys
import types
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
import owi_ds002_exedec_admission as adm
import owi_ds002_lambdabeam_trained_pilot as trained


class TrainedPilotTests(unittest.TestCase):
    def test_six_fixed_split_identities_not_selected_by_outcomes(self):
        self.assertEqual(len(trained.PILOT_IDS),6)
        self.assertEqual({x[0] for x in trained.PILOT_IDS},
                         set(adm.manifest()["splits"]))
        self.assertTrue(all(x[1]==0 for x in trained.PILOT_IDS))
        self.assertEqual(trained.DEFAULT_MAX_VALUES,1000)
        self.assertEqual(trained.DEFAULT_BEAM,10)
        self.assertEqual(trained.DEFAULT_TASK_SECONDS,7.0)

    def test_original_pretrained_constructor_config_explicit(self):
        a=trained._args()
        self.assertTrue(a.use_op_specific_lstm)
        self.assertEqual(a.io_encoder,"lambda_signature")
        self.assertEqual(a.value_encoder,"lambda_signature")
        self.assertEqual(a.max_num_inputs,3)
        self.assertEqual(a.embed_dim,64)
        self.assertTrue(a.encode_weight)
        self.assertEqual(a.arg_selector,"lstm")
        self.assertEqual(a.step_score_func,"mlp")
        self.assertTrue(a.score_normed)

    def test_fail_closed_on_task_or_resource_budget_before_loading(self):
        for args in (
            (0,2,7.0),(5001,2,7.0),(80,0,7.0),(80,11,7.0),
            (80,2,0.0),(80,2,21.0),
        ):
            values,beam,seconds=args
            with self.subTest(args=args),self.assertRaises(adm.Rejected):
                trained.execute_pilot(Path("missing"),Path("missing"),11,
                                      values,seconds,beam)
        with self.assertRaises(adm.Rejected):
            trained.execute_pilot(Path("missing"),Path("missing"),11,
                                  80,7.0,2,only_task=("FAKE",0))

    def test_trained_model_checkpoint_pin_not_modified_by_pilot(self):
        import owi_ds002_lambdabeam_checkpoint_gate as checkpoint
        self.assertEqual(checkpoint.UPSTREAM,
                         "61986dc1a6d8cc9521fb17e3152f7f085b5d7c95")
        self.assertEqual(checkpoint.CHECKPOINT_GIT_BLOB,
                         "91ab03f94972f4f523dfaa771a45ea28583f519f")
        self.assertEqual(checkpoint.CHECKPOINT_SIZE,40750571)

    def test_halt_before_neural_inference_when_enumeration_stub_preloaded(self):
        poison=types.ModuleType("lambdabeam.property_signatures.property_signatures")
        with mock.patch.dict(sys.modules,{
            "lambdabeam.property_signatures.property_signatures":poison
        }):
            with self.assertRaisesRegex(adm.Rejected,"already imported"):
                trained.execute_pilot(Path("missing"),Path("missing"),11,
                                      80,7.0,2)

    def test_scatter_offpath_never_replaced_silently(self):
        poison=types.ModuleType("torch_scatter")
        with mock.patch.dict(sys.modules,{"torch_scatter":poison}):
            with self.assertRaisesRegex(adm.Rejected,"already imported"):
                trained._deny_offpath_scatter()
        with mock.patch.dict(sys.modules):
            if "torch_scatter" in sys.modules:
                del sys.modules["torch_scatter"]
            calls=trained._deny_offpath_scatter()
            self.assertEqual(calls,[])
            with self.assertRaisesRegex(adm.Rejected,"must not invoke off-path"):
                sys.modules["torch_scatter"].scatter_mean(None,None)
            self.assertEqual(len(calls),1)

    def test_candidate_grammar_requires_explicit_adapted_semantics(self):
        import owi_ds002_lambdabeam_native_bridge as bridge
        with self.assertRaises(adm.Rejected):
            bridge.translate("Scanl1(lambda u1,u2:Add(u1,u2),x0)",
                             {"x0":"L"})
        candidate=bridge.translate("Scanl1(lambda u1,u2:Add(u1,u2),x0)",
                                   {"x0":"L"},
                                   semantics="explicit_exedec_adapter")
        self.assertEqual(adm.execute(adm.compile_program(candidate,["x0"],
                              {"x0":"L"}),{"x0":[]}),[])
        with self.assertRaises(adm.Rejected):
            bridge.translate("Scanl1(lambda u1,u2:Add(u1,u2),x0)",
                             {"x0":"L"},semantics="undeclared")

if __name__=="__main__":
    unittest.main()
