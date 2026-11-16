#!/usr/bin/env python3
"""OWI-DS-002: non-executing, source-locked pretrained-checkpoint layout gate.

Never torch.load or pickle.load untrusted checkpoint bytes. Decode only safe
pickle opcodes as DATA via pickletools.genops, and inspect per-operation state
key names in the original published model. This is a shape/vocabulary
*compatibility obstruction* gate, not neural inference or model certification.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import io
import json
from pathlib import Path
import pickletools
import re
import subprocess
import zipfile

import owi_ds002_exedec_admission as adm

REPO = "ellisk42/LambdaBeam"
UPSTREAM = "61986dc1a6d8cc9521fb17e3152f7f085b5d7c95"
CHECKPOINT = "lambdabeam-model.ckpt"
CHECKPOINT_GIT_BLOB = "91ab03f94972f4f523dfaa771a45ea28583f519f"
CHECKPOINT_SIZE = 40_750_571
SOURCE_BLOBS = {
    "lambdabeam/dsl/deepcoder_operations.py": "d33550eae87de3c4f5717aeca9247e7e5eaa9776",
    "lambdabeam/model/deepcoder_model.py": "06bc357ebc5010f0b7535046ac972aa8ea8b0762",
    "lambdabeam/model/op_init.py": "aa47c4d5b390306ac66c295d96ab360646ea70ef",
    "lambdabeam/model/op_arg.py": "e78e541a1105811763bae7681e2f1ee7797323db",
    "lambdabeam/experiment/run_lambdabeam.py": "8994dd1c1d74f4079fa2d475952d5766626adbf3",
    "lambdabeam/experiment/train_eval.py": "c1966662050f1dd3f6b03fdd2feebb0fff5e868e",
    "eval_config.py": "df6142a4cc5558ab5e6cb0ce8a116fdc751d24a2",
}
MAX_SOURCE_BYTES = 3_000_000
MAX_PICKLE_BYTES = 12_000_000
OP_SPECIFIC = re.compile(r"op_specific_lstm\.([0-9]+)\..+")
INIT_SPECIFIC = re.compile(r"init\.op_specific_mod\.([0-9]+)\..+")


def hash_git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\x00"+data).hexdigest()


def source_lock(root: Path) -> dict:
    root=root.resolve()
    if not (root/".git").is_dir():
        raise adm.Rejected("external checkout .git missing")
    try:
        revision=subprocess.run(
            ["git","-C",str(root),"rev-parse","HEAD"],
            check=True,capture_output=True,text=True,timeout=10
        ).stdout.strip()
    except (subprocess.SubprocessError,OSError) as exc:
        raise adm.Rejected("external Git identity unavailable") from exc
    if revision!=UPSTREAM:
        raise adm.Rejected("external source Git revision drift")
    for rel,digest in SOURCE_BLOBS.items():
        path=root/rel
        if not path.is_file() or path.stat().st_size>MAX_SOURCE_BYTES:
            raise adm.Rejected("missing or oversized external source: "+rel)
        if hash_git_blob(path.read_bytes())!=digest:
            raise adm.Rejected("external source Git blob mismatch: "+rel)
    return {"repository":REPO,"commit":UPSTREAM,
            "verified_source_git_blobs":len(SOURCE_BLOBS)}


def original_grammar_operations(source: str) -> list[str]:
    """Extract explicit upstream get_operations return list via AST only."""
    tree=ast.parse(source)
    defs=[node for node in tree.body if isinstance(node,ast.FunctionDef)
          and node.name=="get_operations"]
    if len(defs)!=1:
        raise adm.Rejected("original DeepCoder get_operations not uniquely declared")
    expressions=[item for node in defs[0].body if isinstance(node,ast.Return)
                 and isinstance(node.value,(ast.List,ast.Tuple))
                 for item in node.value.elts]
    if not expressions or any(not isinstance(x,ast.Call)
        or not isinstance(x.func,ast.Name) or x.args or x.keywords
        for x in expressions):
        raise adm.Rejected("original DeepCoder operation list not static")
    names=[x.func.id for x in expressions]
    if len(set(names))!=len(names):
        raise adm.Rejected("duplicate original operator classes")
    classes={n.name for n in tree.body if isinstance(n,ast.ClassDef)}
    if any(name not in classes for name in names):
        raise adm.Rejected("missing original DeepCoder operator class")
    return names


def pinned_model_configuration(source: str) -> dict:
    tree=ast.parse(source)
    matches=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Assign):
            for target in node.targets:
                if (isinstance(target,ast.Attribute)
                    and isinstance(target.value,ast.Name)
                    and target.value.id=="config"
                    and target.attr=="use_op_specific_lstm"):
                    matches.append(node.value)
    if len(matches)!=1 or not isinstance(matches[0],ast.Constant) or matches[0].value is not True:
        raise adm.Rejected("published evaluation config is not operation-specific")
    return {"use_op_specific_lstm":True}


def exedec_atomic_count() -> tuple[int,dict]:
    opgroups={}
    for op,(signature,_) in adm.OPERATIONS.items():
        if "U" in signature:
            count=len(adm.UNARY)
        elif "P" in signature:
            count=len(adm.PRED)
        elif "B" in signature:
            count=len(adm.BINARY)
        else:
            count=1
        opgroups[op]=count
    return sum(opgroups.values()),opgroups


def checkpoint_pickle_bytes(ckpt: Path) -> tuple[bytes,dict]:
    if not ckpt.is_file() or ckpt.stat().st_size!=CHECKPOINT_SIZE:
        raise adm.Rejected("checkpoint missing or original byte-size drift")
    raw=ckpt.read_bytes()
    blob=hash_git_blob(raw)
    if blob!=CHECKPOINT_GIT_BLOB:
        raise adm.Rejected("checkpoint Git blob mismatch")
    if not zipfile.is_zipfile(io.BytesIO(raw)):
        raise adm.Rejected("checkpoint format not zip/pickle; do not deserialize")
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        pickles=[f for f in archive.infolist() if
                 f.filename=="data.pkl" or f.filename.endswith("/data.pkl")]
        if len(pickles)!=1:
            raise adm.Rejected("checkpoint data pickle entry ambiguous")
        item=pickles[0]
        if item.file_size>MAX_PICKLE_BYTES:
            raise adm.Rejected("checkpoint pickle metadata exceeds size limit")
        pkl=archive.read(item.filename)
    return pkl,{"git_blob_sha":blob,"byte_size":len(raw),
                "sha256":hashlib.sha256(raw).hexdigest(),
                "metadata_pickle_entry":item.filename,
                "metadata_pickle_size":len(pkl),
                "deserialization":"NOT PERFORMED; pickletools DATA ONLY"}


def inspect_state_keys(pkl:bytes) -> dict:
    if len(pkl)>MAX_PICKLE_BYTES:
        raise adm.Rejected("pickle metadata too large")
    # Parsing pickle opcodes is not executing the pickle; no torch, pickle.loads,
    # custom persistent loads, arbitrary imports or code evaluation is involved.
    textvals=[]
    try:
        for opcode,arg,_ in pickletools.genops(pkl):
            if opcode.name in ("BINUNICODE","SHORT_BINUNICODE","UNICODE",
                               "BINUNICODE8") and isinstance(arg,str):
                textvals.append(arg)
    except (ValueError,EOFError,UnicodeError) as exc:
        raise adm.Rejected("invalid checkpoint pickle metadata") from exc
    def indices(pattern):
        return sorted({int(m.group(1)) for s in textvals
                       if (m:=pattern.fullmatch(s))})
    op=indices(OP_SPECIFIC)
    init=indices(INIT_SPECIFIC)
    # Source's op-index order matters. Counts alone do not prove identities.
    return {"checkpoint_model_operation_lstm_indices":op,
            "checkpoint_model_init_operation_indices":init,
            "checkpoint_has_model_marker":"model" in textvals,
            "checkpoint_has_optimizer_marker":"optimizer" in textvals,
            "distinct_string_values":len(set(textvals))}


def evaluate(root:Path)->dict:
    upstream=source_lock(root)
    original=original_grammar_operations(
        (root/"lambdabeam/dsl/deepcoder_operations.py").read_text(encoding="utf-8"))
    evalcfg=pinned_model_configuration(
        (root/"eval_config.py").read_text(encoding="utf-8"))
    exact_count,groups=exedec_atomic_count()
    pkl,receipt=checkpoint_pickle_bytes(root/CHECKPOINT)
    keys=inspect_state_keys(pkl)
    src_count=len(original)
    original_indices=list(range(src_count))
    observed_op=keys["checkpoint_model_operation_lstm_indices"]
    observed_init=keys["checkpoint_model_init_operation_indices"]
    if observed_op!=original_indices or observed_init!=original_indices or not keys["checkpoint_has_model_marker"]:
        # Do not assert a mismatch unless we have structurally located the
        # expected original model heads in the actual pinned checkpoint.
        raise adm.Rejected("checkpoint model-head indexing differs from published original operator vocabulary; requires manual custody review")
    if src_count==exact_count:
        raise adm.Rejected("original and source-exact cardinality unexpectedly equal")
    return {
      "schema":"gcl.owi-ds002.lambdabeam-trained-checkpoint-compatibility.v1",
      "status":"DIRECT_CHECKPOINT_REUSE_IN_EXACT_EXEDEC_OPERATOR_MODEL_INCOMPATIBLE",
      "original_source":upstream,"checkpoint":receipt,
      "published_eval_config":evalcfg,
      "original_operator_classes":{"count":src_count,"ordered_names":original},
      "exact_exedec_ops":{"count":exact_count,"variants_per_operator":groups,
                          "source_revision":adm.manifest()["origin"]["commit"]},
      "original_checkpoint_state":keys,
      "technical_obstruction":{
        "operator_specific_lstm_heads_missing_for_exact_vocabulary":exact_count-src_count,
        "operator_index_semantics_unmatched":True,
        "exact_model_load_directly_allowed":False,
        "reason":"published model has an indexed head for each of its original 28 operator classes; exact ExeDec adapter exposes 38 fixed-lambda operations, with different operator identities/order",
        "consequence":"direct state_dict load cannot establish valid per-operation weights or exact DSL execution",
      },
      "safe_paths":[
        "Rebuild restricted native 28-op trained search with an exact interpreter/evaluator adapter and rejection-only translation of generated expressions to ExeDec programs; validate actual supported lambda grammar before claiming comparison",
        "Or initialize a new 38-operation model head and retrain or fine-tune on ExeDec-matched data, explicitly accounting for new operation parameters and contamination controls",
        "Compare on exact source tasks, count training and adaptation compute, include independent evaluator probes and separate local GCL search costs",
      ],
      "limits":[
        "Structural checkpoint metadata audit; does not instantiate or execute trained neural model",
        "No arbitrary pickle or torch weights deserialization, no optimizer state executed",
        "Operation-head indices and counts do not by themselves establish semantic weight mappings",
        "No unmodified trained LambdaBeam result, no trained model speed, no full-compute A/B/C/D, no C1 JVP or D causal intervention evidence",
      ],
    }


def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-dir",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    try:
        result=evaluate(Path(args.source_dir))
        status=0
    except (adm.Rejected,ValueError,OSError,subprocess.SubprocessError,
            zipfile.BadZipFile) as exc:
        result={"status":"REJECTED_OR_INCONCLUSIVE","error":str(exc)}
        status=2
    target=Path(args.output)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))
    return status

if __name__=="__main__":
    raise SystemExit(main())
