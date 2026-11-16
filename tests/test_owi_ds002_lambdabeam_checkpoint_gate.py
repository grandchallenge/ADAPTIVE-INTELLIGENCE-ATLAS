"""Non-executing LambdaBeam checkpoint compatibility and source lock guards."""
from pathlib import Path
import hashlib
import io
import pickle
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
import owi_ds002_exedec_admission as adm
import owi_ds002_lambdabeam_checkpoint_gate as gate


class CheckpointGateTests(unittest.TestCase):
    def test_exact_exedec_atomic_operator_count_and_lambdas(self):
        count,groups=gate.exedec_atomic_count()
        self.assertEqual(count,38)
        self.assertEqual(groups["Map"],len(adm.UNARY))
        self.assertEqual(groups["Filter"],len(adm.PRED))
        self.assertEqual(groups["ZipWith"],len(adm.BINARY))
        self.assertEqual(groups["Head"],1)

    def test_static_original_declared_operators_not_heuristic(self):
        src=("class A: pass\nclass B: pass\n"
             "def get_operations():\n  return [A(),B()]\n")
        self.assertEqual(gate.original_grammar_operations(src),["A","B"])
        with self.assertRaises(adm.Rejected):
            gate.original_grammar_operations(
                "class A: pass\ndef get_operations():\n return [A(),A()]")
        with self.assertRaises(adm.Rejected):
            gate.original_grammar_operations(
                "class A: pass\ndef get_operations():\n return [Missing()]")

    def test_pinned_evaluation_configuration_requires_specific_model_heads(self):
        good=("def get_config():\n"
              " config.use_op_specific_lstm = True\n"
              " return config\n")
        self.assertTrue(gate.pinned_model_configuration(good)["use_op_specific_lstm"])
        for source in (
          "def f():\n config.use_op_specific_lstm = False",
          "def f():\n config.use_op_specific_lstm = expression",
          "pass",
        ):
            with self.subTest(source=source),self.assertRaises(adm.Rejected):
                gate.pinned_model_configuration(source)

    def test_pickle_metadata_extracts_both_head_families_without_loading(self):
        metadata={"model":{
            "init.op_specific_mod.0.proj.weight":object(),
            "init.op_specific_mod.1.proj.bias":object(),
            "op_specific_lstm.0.lstm.weight_ih_l0":object(),
            "op_specific_lstm.1.lstm.weight_hh_l0":object(),
        },"optimizer":{"other":0},"step":100}
        raw=pickle.dumps(metadata,protocol=4)
        actual=gate.inspect_state_keys(raw)
        self.assertEqual(actual["checkpoint_model_init_operation_indices"],[0,1])
        self.assertEqual(actual["checkpoint_model_operation_lstm_indices"],[0,1])
        self.assertTrue(actual["checkpoint_has_model_marker"])
        self.assertTrue(actual["checkpoint_has_optimizer_marker"])

    def test_checkpoint_raw_bytes_must_match_both_git_and_declared_length(self):
        with tempfile.TemporaryDirectory() as work:
            file=Path(work)/"small.ckpt"
            bio=io.BytesIO()
            with zipfile.ZipFile(bio,"w") as z:
                z.writestr("mock/data.pkl",pickle.dumps({"model":{}},protocol=4))
            raw=bio.getvalue()
            file.write_bytes(raw)
            with self.assertRaises(adm.Rejected):
                gate.checkpoint_pickle_bytes(file)
            with mock.patch.object(gate,"CHECKPOINT_SIZE",len(raw)),mock.patch.object(
                gate,"CHECKPOINT_GIT_BLOB",gate.hash_git_blob(raw)):
                payload,receipt=gate.checkpoint_pickle_bytes(file)
                self.assertIn(b"model",payload)
                self.assertEqual(receipt["sha256"],hashlib.sha256(raw).hexdigest())
                self.assertEqual(receipt["deserialization"],
                                 "NOT PERFORMED; pickletools DATA ONLY")
            with mock.patch.object(gate,"CHECKPOINT_SIZE",len(raw)),mock.patch.object(
                gate,"CHECKPOINT_GIT_BLOB","0"*40):
                with self.assertRaises(adm.Rejected):
                    gate.checkpoint_pickle_bytes(file)

    def test_nonzip_or_malformed_metadata_fails_closed(self):
        with self.assertRaises(adm.Rejected):
            gate.inspect_state_keys(b"not valid pickle")
        with tempfile.TemporaryDirectory() as work:
            file=Path(work)/"wrong.ckpt"
            data=b"arbitrary-code-or-legacy-pickle"
            file.write_bytes(data)
            with mock.patch.object(gate,"CHECKPOINT_SIZE",len(data)),mock.patch.object(
                gate,"CHECKPOINT_GIT_BLOB",gate.hash_git_blob(data)):
                with self.assertRaises(adm.Rejected):
                    gate.checkpoint_pickle_bytes(file)

    def test_embedded_pickle_reduce_does_not_execute(self):
        # Data-only opcode iteration never invokes this malicious reduction.
        class Poison:
            def __reduce__(self):
                return (eval,("1+2",))
        raw=pickle.dumps({"model":{"op_specific_lstm.0.a":Poison()}},protocol=4)
        actual=gate.inspect_state_keys(raw)
        self.assertEqual(actual["checkpoint_model_operation_lstm_indices"],[0])
        self.assertFalse(any("execute" in s for s in actual))

    def test_provenance_byte_contract_is_pinned(self):
        self.assertEqual(gate.UPSTREAM,"61986dc1a6d8cc9521fb17e3152f7f085b5d7c95")
        self.assertEqual(gate.CHECKPOINT_GIT_BLOB,
                         "91ab03f94972f4f523dfaa771a45ea28583f519f")
        self.assertEqual(gate.CHECKPOINT_SIZE,40750571)
        self.assertEqual(len(gate.SOURCE_BLOBS),7)
        self.assertEqual(gate.hash_git_blob(b"abc"),
                         "f2ba8f84ab5c1bce84a7b441cb1959cfc7093b7f")

if __name__=="__main__":
    unittest.main()
