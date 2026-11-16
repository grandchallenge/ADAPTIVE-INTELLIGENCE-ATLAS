#!/usr/bin/env python3
"""OWI-DS002: explicitly ADAPTED LambdaBeam native 28-head ExeDec execution.

This is not unmodified original LambdaBeam. Only Access and Scanl1 runtime
edge/bounds semantics are overridden, without changing the source files,
operator order, representation identities, argument binders, or model head
count. Separate exact ExeDec AST translation requires an explicit mode opt-in.
No checkpoint is executed and no neural performance claim is made.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

import owi_ds002_exedec_admission as adm
import owi_ds002_lambdabeam_native_bridge as native
import owi_ds002_exedec_lambdabeam_external as source_loader

EXPECTED_ADAPTED = {"Access", "Scanl1"}
SEMANTICS = "explicit_exedec_adapter"
SCANLAMBDAS = {
    "(+)": "Add(u1,u2)", "(-)": "Subtract(u1,u2)",
    "(*)": "Multiply(u1,u2)", "(min)": "Min(u1,u2)",
    "(max)": "Max(u1,u2)",
}


def legal(x):
    try:
        adm.kind(x)
        return True
    except adm.Rejected:
        return False


def load_adapted_operators(source_root: Path, *, authentic_neural: bool = False):
    """Preserve 28 operation heads; use REAL property signatures for neural inference.

    Default legacy source-comparison mode keeps the original benchmark's
    fail-closed unused-lambda stub. For genuine trained inference that stub is
    prohibited: the source-locked upstream signature machinery must execute.
    """
    provenance=native.check_original_grammar(source_root)
    if authentic_neural:
        source_loader.check_source(source_root)
        root=str(Path(source_root).resolve())
        if root not in sys.path:
            sys.path.insert(0,root)
        shim=sys.modules.get("lambdabeam.property_signatures.property_signatures")
        if shim is not None and not hasattr(shim, "property_signature_value"):
            raise adm.Rejected("non-neural property-signature stub already imported")
    else:
        source_loader.load(source_root)
    from lambdabeam.dsl import deepcoder_operations as orig
    original=orig.get_operations()
    original_names=[repr(x) for x in original]
    if original_names!=provenance["original_operator_names"] or len(original)!=28:
        raise adm.Rejected("original operator order drift")

    class ExactAccess(orig.Access):
        def __init__(self):
            super().__init__()
            self.name="Access"

        def __repr__(self):
            return "Access"

        def apply_single(self,args):
            if len(args)!=2:
                return None
            index,values=args
            if not legal(index) or not legal(values):
                return None
            if index<0 or index>=len(values):
                return None
            try:
                result=super().apply_single([index,values])
            except (IndexError,ValueError,TypeError):
                return None
            return result if legal(result) else None

    class ExactScanl1(orig.Scanl1):
        def __init__(self):
            super().__init__()
            self.name="Scanl1"

        def __repr__(self):
            return "Scanl1"

        def apply_single(self,args):
            if len(args)!=2:
                return None
            fun,values=args
            if not callable(fun) or not legal(values):
                return None
            if not values:
                # EXPLICIT semantic change. ExeDec defines empty Scanl1 = [].
                return []
            try:
                result=super().apply_single([fun,values])
            except (IndexError,ValueError,TypeError,OverflowError,ZeroDivisionError):
                return None
            # Check EACH prefix intermediate; original source bound was 255
            # while the pinned ExeDec interpreter caps absolute values at 50.
            return result if legal(result) else None

    adapted=[]
    for op in original:
        if repr(op)=="Access":
            adapted.append(ExactAccess())
        elif repr(op)=="Scanl1":
            adapted.append(ExactScanl1())
        else:
            adapted.append(op)
    if [repr(x) for x in adapted]!=original_names or len(adapted)!=28:
        raise adm.Rejected("model operation-index identity changed")
    if len({repr(x) for x in adapted})!=28:
        raise adm.Rejected("duplicate learned op-head identity")
    for before,after in zip(original,adapted):
        if (before.arity!=after.arity or
            before.num_bound_variables!=after.num_bound_variables or
            before.weight!=after.weight or before.name!=after.name):
            raise adm.Rejected("model op-head ABI or binder changed")
    return original,adapted,provenance


def expanded_witnesses():
    rows=list(native.witness_expressions())
    rows.append(("Access","","Access(x0,x1)",{"x0":"I","x1":"L"}))
    for token,expr in SCANLAMBDAS.items():
        rows.append(("Scanl1",token,
                     "Scanl1(lambda u1,u2: "+expr+",x0)",{"x0":"L"}))
    if len(rows)!=38 or len({(a,b) for a,b,_,_ in rows})!=38:
        raise adm.Rejected("adapted grammar not exactly 38 ExeDec legal atoms")
    return rows


def execute_matched_witnesses(source_root:Path,cache:Path|None=None,
                              offline:bool=False)->dict:
    original,adapted,prov=load_adapted_operators(source_root)
    ops={repr(x):x for x in adapted}
    old={repr(x):x for x in original}
    # Explicit, positive divergence tests against upstream SOURCE.
    if old["Access"].apply_single([-1,[1,2]])!=2:
        raise adm.Rejected("original native Access negative-index divergence lost")
    try:
        old["Scanl1"].apply_single([old["Add"].apply_single,[]])
    except (IndexError,ValueError):
        original_empty="UNDEFINED"
    else:
        raise adm.Rejected("original native Scanl1 empty-list divergence lost")
    if (ops["Access"].apply_single([-1,[1,2]]) is not None or
        ops["Scanl1"].apply_single([old["Add"].apply_single,[]])!=[]):
        raise adm.Rejected("adapter does not repair explicit source differences")
    # ExeDec bounds reject an originally permitted 8*8 intermediate.
    def multiply(a,b):
        return old["Multiply"].apply_single([a,b])
    if old["Scanl1"].apply_single([multiply,[8,8]])!=[8,64]:
        raise adm.Rejected("original Scanl1 bounds changed unexpectedly")
    if ops["Scanl1"].apply_single([multiply,[8,8]]) is not None:
        raise adm.Rejected("adapted Scanl1 failed source-exact overflow guard")

    valsI=[-4,-1,0,1,2,3,5]
    valsL=[[],[-3,-2,-1,0,1],[4],[-4,2],[1,3,5],[0,0],[2,-2,3]]
    cases=0
    invalid_both=0
    count=Counter()
    statements=[]
    for opname,lam,expression,types in expanded_witnesses():
        prog=native.translate(expression,types,semantics=SEMANTICS)
        compiled=adm.compile_program(prog,list(types),types)
        if compiled[-1][1]!=opname:
            raise adm.Rejected("translated adapted operation name mismatch")
        if lam and compiled[-1][2][0]!=lam:
            raise adm.Rejected("translated adapted lambda token mismatch")
        for i in range(7):
            for j in range(7 if len(types)==2 else 1):
                env={k:(valsI[i] if t=="I" else
                        valsL[j if k=="x1" else i]) for k,t in types.items()}
                source_value=native.native_execute(expression,env,ops,semantics=SEMANTICS)
                exact_value=adm.execute(compiled,env)
                if source_value!=exact_value:
                    raise adm.Rejected("adapted original-source / exact ExeDec mismatch: "
                                       +opname+" "+lam+" "+json.dumps(env,sort_keys=True))
                cases+=1
                count[opname]+=1
                if source_value is None:
                    invalid_both+=1
        statements.append({
            "native_expression":expression,"original_operator":opname,
            "legal_fixed_lambda":lam,"exe_dec_program":prog,
            "exedec_program_sha256":hashlib.sha256(prog.encode()).hexdigest(),
        })
    # Additional targeted edge tests include all arithmetic Scanl1 variants
    # and invalid list boundaries beyond the basic source witness matrix.
    probes=[[],[0],[-3],[-3,2],[8,8],[-5,-5],[1,2,3],[2,3,5],[0,0,0]]
    for token,body in SCANLAMBDAS.items():
        expr="Scanl1(lambda u1,u2: "+body+",x0)"
        pgm=native.translate(expr,{"x0":"L"},semantics=SEMANTICS)
        compiled=adm.compile_program(pgm,["x0"],{"x0":"L"})
        for xs in probes:
            a=native.native_execute(expr,{"x0":xs},ops,semantics=SEMANTICS)
            b=adm.execute(compiled,{"x0":xs})
            if a!=b:
                raise adm.Rejected("Scanl1 targeted edge discrepancy "+token+":"+repr(xs))
            cases+=1
            count["Scanl1_edge"]+=1
            if a is None:
                invalid_both+=1
    for index in [-3,-1,0,1,2,5]:
        for xs in ([],[1],[1,2],[2,-2,3]):
            env={"x0":index,"x1":xs}
            a=native.native_execute("Access(x0,x1)",env,ops,semantics=SEMANTICS)
            b=adm.execute([("x2","Access",["x0","x1"])],env)
            if a!=b:
                raise adm.Rejected("Access targeted edge discrepancy "+repr(env))
            cases+=1
            count["Access_edge"]+=1
            if a is None:
                invalid_both+=1
    output={
      "schema":"gcl.owi-ds002.native-28head-adapted-exedec-38atoms.v1",
      "status":"EXPLICIT_28HEAD_SEMANTIC_ADAPTER_38_ATOMS_SOURCE_WITNESSED",
      "original_source":prov,
      "exe_dec_source_revision":adm.manifest()["origin"]["commit"],
      "adaptation":{"changed_native_operations":["Access","Scanl1"],
        "original_source_bytes_modified":False,
        "checkpoint_loaded":False,"trained_search_executed":False,
        "original_operator_head_count":28,"adapted_operator_head_count":28,
        "original_repr_order_preserved":True,"original_arity_binder_weight_name_preserved":True,
        "semantic_contract":"ExeDec exact bounds and definedness, not unmodified LambdaBeam runtime",
        "Access":"reject original Python negative indexing and out-of-range indexes",
        "Scanl1":"empty list returns [] rather than raising; each prefix intermediate must be within ExeDec bounds",
        "original_Access_minus1_result":2,
        "original_Scanl1_empty_result":original_empty,
        "original_Scanl1_mul_8_8_result":[8,64],
        "adapted_Scanl1_mul_8_8_result":None},
      "audit":{"accepted_exe_dec_fixed_atoms":len(statements),
        "source_native_vs_exedec_finite_probe_pairs":cases,
        "undefined_both":invalid_both,
        "mismatches":0,
        "per_operation_probe_counts":dict(count)},
      "witnesses":statements,
      "limitations":[
        "Explicit learned-runtime semantic adaptation; must not call it unmodified original LambdaBeam inference",
        "Original native source operators for Access and Scanl1 are subclassed; the original 28 model-head repr/arity/binder order is preserved, but learned guidance transfer is not established",
        "Real model state_dict load, native beam inference and trained candidate receipts have not been executed",
        "38/38 grammar atomic syntax witnesses do not prove arbitrary nested source programs are representable or universally equivalent",
        "Finite source-native-vs-ExeDec values do not prove universal program equivalence",
        "Public benchmark references are not secret holdout; no equal-compute trained A/B/C/D or C1/D scientific result",
      ],
    }
    if cache is not None:
        by_split={}
        for split in sorted(adm.manifest()["splits"]):
            rows,sha=adm.source_rows(split,cache,offline=offline)
            unknown_ops=Counter()
            for row in rows:
                p=row["test_problem"]
                names,t,_=adm.validate_examples(p)
                for _,op,_ in adm.compile_program(p["program"],names,t):
                    if op not in adm.OPERATIONS:
                        unknown_ops[op]+=1
            if unknown_ops:
                raise adm.Rejected("unknown source operation appears")
            by_split[split]={"reference_tasks":len(rows),"source_blob":sha,
                             "operator_name_coverage_only":len(rows)}
        output["retrospective_source_corpus"]={
            "public_reference_tasks":sum(x["reference_tasks"] for x in by_split.values()),
            "syntactically_covered_operator_names_only":
                sum(x["operator_name_coverage_only"] for x in by_split.values()),
            "by_split":by_split,
            "reference_programs_present_only_during_retrospective_audit":True,
            "not_trained_synthesis_success":True,
            "not_model_output_translation_success":True,
        }
    return output


def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-dir",required=True)
    ap.add_argument("--cache-dir",default="build/owi_ds002/exedec_sources")
    ap.add_argument("--offline",action="store_true")
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    try:
        result=execute_matched_witnesses(Path(args.source_dir),Path(args.cache_dir),
                                         offline=args.offline)
        code=0
    except (adm.Rejected,ValueError,OSError,TypeError,KeyError,RecursionError) as exc:
        result={"status":"REJECTED_OR_INCONCLUSIVE","error":str(exc)}
        code=2
    path=Path(args.output)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="witnesses"},sort_keys=True,indent=2))
    return code


if __name__=="__main__":
    raise SystemExit(main())
