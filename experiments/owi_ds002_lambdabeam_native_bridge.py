#!/usr/bin/env python3
"""OWI-DS002 native LambdaBeam expression -> 2024 ExeDec exact DSL bridge.

Strict positive allowlist over Python AST syntax. NO eval/exec/unpickle.
Rejects all legacy semantics not proven compatible (Access negative indexing,
Scanl1 empty input) and all learned higher-order functions not exactly equal
to a source-pinned ExeDec fixed lambda. Translation is a typed candidate
proposal, not a guarantee of output equivalence or pretrained-model inference.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import time

import owi_ds002_exedec_admission as adm
import owi_ds002_lambdabeam_checkpoint_gate as custody

# All accepted source operator names are required to belong to original
# upstream get_operations(), checked against the exact upstream Git blob.
FIRST = frozenset(("Head","Last","Take","Drop","Minimum","Maximum",
                   "Reverse","Sort","Sum"))
HIGH = frozenset(("Map","Filter","Count","ZipWith"))
NATIVE_SCALAR = frozenset(("Add","Subtract","Multiply","IntDivide",
                          "Square","Min","Max","Greater","Less","IsEven","IsOdd"))
PROHIBITED = frozenset(("Access","Scanl1"))
ALL_TRANSLATABLE = FIRST | HIGH
MAX_EXPRESSION_BYTES = 2048
MAX_AST_NODES = 128

def check_original_grammar(root: Path)->dict:
    lock=custody.source_lock(root)
    names=custody.original_grammar_operations(
        (root/"lambdabeam/dsl/deepcoder_operations.py").read_text())
    if len(names)!=28 or not ALL_TRANSLATABLE|NATIVE_SCALAR|PROHIBITED <= set(names):
        raise adm.Rejected("original native grammar unexpectedly changed")
    return {"source":lock,"original_operator_names":names,
            "safe_operations":sorted(ALL_TRANSLATABLE),
            "semantic_exclusions":sorted(PROHIBITED)}


def _syntax(expression:str)->ast.AST:
    if (type(expression) is not str or
        not 1<=len(expression.encode("utf-8"))<=MAX_EXPRESSION_BYTES):
        raise adm.Rejected("invalid native expression length")
    try:
        result=ast.parse(expression,mode="eval")
    except (SyntaxError,ValueError,TypeError,RecursionError) as exc:
        raise adm.Rejected("native expression syntax rejected") from exc
    if sum(1 for _ in ast.walk(result))>MAX_AST_NODES:
        raise adm.Rejected("native expression AST size exceeded")
    return result.body


def _const(node:ast.AST):
    if isinstance(node,ast.Constant) and type(node.value) is int:
        if node.value in (-1,0,1,2,3,4):
            return ("lit",node.value)
    if (isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub)
        and isinstance(node.operand,ast.Constant) and type(node.operand.value) is int
        and node.operand.value==1):
        return ("lit",-1)
    raise adm.Rejected("scalar lambda literal not in pinned original constants")


def _argnames(lam:ast.Lambda,n:int)->list[str]:
    a=lam.args
    if (len(a.args)!=n or a.posonlyargs or a.vararg or a.kwonlyargs or a.kwarg
        or a.defaults or a.kw_defaults or
        any(z.annotation is not None for z in a.args)):
        raise adm.Rejected("native lambda binding not a fixed-position lambda")
    names=[z.arg for z in a.args]
    if len(set(names))!=n:
        raise adm.Rejected("duplicate bound lambda name")
    return names


def _scalar_ast(node:ast.AST,scope:dict,depth:int=0):
    """Normalize nested *immediately applied* lambdas by capture-safe binding."""
    if depth>16:
        raise adm.Rejected("nested scalar-lambda depth limit")
    if isinstance(node,ast.Name):
        if node.id not in scope:
            raise adm.Rejected("unbound/closure-dependent native lambda variable")
        return scope[node.id]
    if isinstance(node,(ast.Constant,ast.UnaryOp)):
        return _const(node)
    if not isinstance(node,ast.Call) or node.keywords:
        raise adm.Rejected("unsupported native scalar-lambda syntax")
    if isinstance(node.func,ast.Lambda):
        names=_argnames(node.func,len(node.args))
        if not names or len(names)>2:
            raise adm.Rejected("unsupported immediately applied lambda")
        params=[_scalar_ast(z,scope,depth+1) for z in node.args]
        inner=dict(scope)
        inner.update(zip(names,params))
        return _scalar_ast(node.func.body,inner,depth+1)
    if not isinstance(node.func,ast.Name) or node.func.id not in NATIVE_SCALAR:
        raise adm.Rejected("unsupported scalar operation in native lambda")
    if len(node.args)>2:
        raise adm.Rejected("unsupported native scalar operation arity")
    return ("call",node.func.id,tuple(_scalar_ast(z,scope,depth+1)
                                    for z in node.args))


def _call(name:str,*args):
    return ("call",name,tuple(args))


def _fits_commutative(term,op,a,b):
    return term==_call(op,a,b) or term==_call(op,b,a)


def fixed_lambda(node:ast.AST,kind:str)->str:
    if not isinstance(node,ast.Lambda):
        raise adm.Rejected("higher-order argument must be fixed lambda syntax")
    n=2 if kind=="B" else 1
    names=_argnames(node,n)
    args=[("var","u"+str(i+1)) for i in range(n)]
    term=_scalar_ast(node.body,dict(zip(names,args)))
    x=args[0]
    if kind=="U":
        for k in (1,):
            if (_fits_commutative(term,"Add",x,("lit",k))):
                return "(+1)"
        if term==_call("Subtract",x,("lit",1)):
            return "(-1)"
        for k in (2,3,4,-1):
            if _fits_commutative(term,"Multiply",x,("lit",k)):
                return "(*(-1))" if k==-1 else "(*"+str(k)+")"
        if term==_call("Subtract",("lit",0),x):
            return "(*(-1))"
        for k in (2,3,4):
            if term==_call("IntDivide",x,("lit",k)):
                return "(/"+str(k)+")"
        if term==_call("Square",x) or term==_call("Multiply",x,x):
            return "(**2)"
    elif kind=="P":
        if term in (_call("Greater",x,("lit",0)),
                    _call("Less",("lit",0),x)):
            return "(>0)"
        if term in (_call("Less",x,("lit",0)),
                    _call("Greater",("lit",0),x)):
            return "(<0)"
        if term==_call("IsEven",x):
            return "(%2==0)"
        if term==_call("IsOdd",x):
            return "(%2==1)"
    elif kind=="B":
        y=args[1]
        for op,tok in (("Add","(+)"),("Multiply","(*)"),
                       ("Min","(min)"),("Max","(max)")):
            if _fits_commutative(term,op,x,y):
                return tok
        if term==_call("Subtract",x,y):
            return "(-)"
    else:
        raise adm.Rejected("unknown fixed lambda kind")
    raise adm.Rejected("native lambda not provably equal to a legal ExeDec fixed lambda")


def translate(expression:str,types:dict[str,str])->str:
    if (not isinstance(types,dict) or not 1<=len(types)<=3 or
        list(types)!=["x"+str(i) for i in range(len(types))] or
        any(t not in ("I","L") for t in types.values())):
        raise adm.Rejected("noncanonical or invalid native input types")
    tree=_syntax(expression)
    lines=[name+" = INPUT" for name in types]
    emitted={}
    values=dict(types)
    pending=set()

    def visit(node:ast.AST,depth:int=0):
        if depth>16:
            raise adm.Rejected("nested native expression too deep")
        if isinstance(node,ast.Name):
            if node.id not in types:
                raise adm.Rejected("native expression contains unknown input or free variable")
            return node.id,types[node.id]
        if not isinstance(node,ast.Call) or not isinstance(node.func,ast.Name):
            raise adm.Rejected("native program expression is not an approved call")
        op=node.func.id
        if op not in ALL_TRANSLATABLE:
            raise adm.Rejected("native operation outside source-exact safe subset: "+op)
        if node.keywords:
            raise adm.Rejected("native operation keywords not supported")
        signature,out_type=adm.OPERATIONS[op]
        if len(node.args)!=len(signature):
            raise adm.Rejected("native operation arity mismatch")
        key=ast.dump(node,include_attributes=False)
        if key in emitted:
            return emitted[key],out_type
        if key in pending:
            raise adm.Rejected("cyclic native program expression")
        pending.add(key)
        parts=[]
        for source_arg,required in zip(node.args,signature):
            if required in ("U","P","B"):
                parts.append(fixed_lambda(source_arg,required))
            else:
                name,observed=visit(source_arg,depth+1)
                if observed!=required:
                    raise adm.Rejected("native expression register type mismatch")
                parts.append(name)
        if len(lines)>=adm.MAX_LINES:
            raise adm.Rejected("native tree exceeds exact ExeDec line cap")
        dest="x"+str(len(lines))
        lines.append(" ".join([dest,"=",op]+parts))
        values[dest]=out_type
        emitted[key]=dest
        pending.remove(key)
        return dest,out_type

    visit(tree)
    result=" | ".join(lines)
    if len(result)>2048:
        raise adm.Rejected("translated ExeDec source too long")
    adm.compile_program(result,list(types),types)
    return result


def transfer_candidate(expression:str,view:dict)->dict:
    """Search-scoped input only; no reference or private evaluator allowed."""
    allowed={"status","task_id","inputs","outputs","input_output_examples",
             "target_program_exposed","source_blob"}
    if set(view)-allowed or view.get("target_program_exposed") is not False:
        raise adm.Rejected("native translator participant view is not source-blind")
    names,types,n=adm.validate_examples(view)
    program=translate(expression,types)
    code=adm.compile_program(program,names,types)
    all_public=all(adm.execute(code,{k:view["inputs"][k][i] for k in names})
                   ==view["outputs"][i] for i in range(n))
    return {"status":"PUBLIC_IO_CANDIDATE_FOUND" if all_public
                     else "REJECTED_PUBLIC_EXAMPLE",
            "candidate":program if all_public else None,
            "translated_sha256":hashlib.sha256(program.encode()).hexdigest(),
            "original_expression_sha256":hashlib.sha256(expression.encode()).hexdigest(),
            "participant_only":True}


# Source-native witness semantics are intentionally implemented by the exact
# UPSTREAM operation methods, not by calling the protected ExeDec lambdas.
# The original source imports are delayed until upstream Git/blob verification.
def native_execute(expr:str,values:dict,source_ops:dict):
    tree=_syntax(expr)
    def lambda_impl(n,kind):
        token=fixed_lambda(n,kind)
        def fun(*args):
            if kind=="U":
                v=args[0]
                if token=="(+1)": return source_ops["Add"].apply_single([v,1])
                if token=="(-1)": return source_ops["Subtract"].apply_single([v,1])
                if token=="(*(-1))": return source_ops["Multiply"].apply_single([v,-1])
                if token=="(**2)": return source_ops["Square"].apply_single([v])
                if token.startswith("(*"): return source_ops["Multiply"].apply_single([v,int(token[2:-1])])
                if token.startswith("(/"): return source_ops["IntDivide"].apply_single([v,int(token[2:-1])])
            elif kind=="P":
                v=args[0]
                if token=="(>0)": return source_ops["Greater"].apply_single([v,0])
                if token=="(<0)": return source_ops["Less"].apply_single([v,0])
                if token=="(%2==0)": return source_ops["IsEven"].apply_single([v])
                if token=="(%2==1)": return source_ops["IsOdd"].apply_single([v])
            else:
                name={ "(+)":"Add","(-)":"Subtract","(*)":"Multiply",
                       "(min)":"Min","(max)":"Max"}.get(token)
                if name: return source_ops[name].apply_single(list(args))
            raise adm.Rejected("native lambda not implementable")
        return fun
    def walk(node):
        if isinstance(node,ast.Name) and node.id in values:
            return values[node.id]
        if not isinstance(node,ast.Call) or not isinstance(node.func,ast.Name):
            raise adm.Rejected("noncanonical native runnable expression")
        op=node.func.id
        if op not in ALL_TRANSLATABLE:
            raise adm.Rejected("native witness operation not admitted")
        signature,_=adm.OPERATIONS[op]
        args=[lambda_impl(a,k) if k in ("U","P","B") else walk(a)
              for a,k in zip(node.args,signature)]
        try:
            return source_ops[op].apply_single(args)
        except (IndexError,ValueError,TypeError,OverflowError,ZeroDivisionError):
            return None
    return walk(tree)


def witness_expressions():
    """Construct all 32 ExeDec source-grammar safe atomic native representations."""
    native_unary={
       "(+1)":"Add(u1, 1)","(-1)":"Subtract(u1, 1)",
       "(*2)":"Multiply(u1, 2)","(/2)":"IntDivide(u1, 2)",
       "(*(-1))":"Multiply(u1, -1)","(**2)":"Square(u1)",
       "(*3)":"Multiply(u1, 3)","(/3)":"IntDivide(u1, 3)",
       "(*4)":"Multiply(u1, 4)","(/4)":"IntDivide(u1, 4)",
    }
    native_pred={
        "(>0)":"Greater(u1, 0)","(<0)":"Less(u1, 0)",
        "(%2==0)":"IsEven(u1)","(%2==1)":"IsOdd(u1)"
    }
    native_binary={
        "(+)":"Add(u1, u2)","(-)":"Subtract(u1, u2)",
        "(*)":"Multiply(u1, u2)","(min)":"Min(u1, u2)",
        "(max)":"Max(u1, u2)",
    }
    records=[]
    for op in sorted(FIRST):
        if op in ("Take","Drop"):
            e=f"{op}(x0, x1)"
            types={"x0":"I","x1":"L"}
        else:
            e=f"{op}(x0)"
            types={"x0":"L"}
        records.append((op,"",e,types))
    for op in ("Map","Filter","Count","ZipWith"):
        tokens=(native_unary if op=="Map" else native_pred
                if op in ("Filter","Count") else native_binary)
        for tok,body in tokens.items():
            e=(f"{op}(lambda u1, u2: {body}, x0, x1)" if op=="ZipWith"
               else f"{op}(lambda u1: {body}, x0)")
            typ={"x0":"L","x1":"L"} if op=="ZipWith" else {"x0":"L"}
            records.append((op,tok,e,typ))
    return records


def witness_audit(source_dir:Path,cache:Path|None=None,offline:bool=False)->dict:
    provenance=check_original_grammar(source_dir)
    # Only execute original published Python source after hash/source lock.
    import owi_ds002_exedec_lambdabeam_external as baseline
    baseline.load(source_dir)
    from lambdabeam.dsl import deepcoder_operations
    operations={o.__class__.__name__:o for o in deepcoder_operations.get_operations()}
    if list(operations)!=provenance["original_operator_names"]:
        raise adm.Rejected("native executable operator order differs from pinned grammar")
    all_cases=0
    undefined_both=0
    byop=Counter()
    witness=[]
    int_inputs=[-4,-1,0,1,2,3,5]
    list_inputs=[[],[-3,-2,-1,0,1],[4],[-4,2],[1,3,5],[0,0],[2,-2,3]]
    for op,token,expr,types in witness_expressions():
        dsl=translate(expr,types)
        code=adm.compile_program(dsl,list(types),types)
        if op not in adm.OPERATIONS:
            raise adm.Rejected("unrecognized exact operation in witness")
        vals={k:(int_inputs if t=="I" else list_inputs) for k,t in types.items()}
        n=len(int_inputs)
        for i in range(n):
            for j in range(n if len(types)==2 else 1):
                values={k:pool[j if k=="x1" and len(types)==2 else i]
                        for k,pool in vals.items()}
                original=native_execute(expr,values,operations)
                exact=adm.execute(code,values)
                if original!=exact:
                    raise adm.Rejected("native/ExeDec semantics mismatch on "
                        +op+":"+token+":"+json.dumps(values,sort_keys=True))
                all_cases+=1
                byop[op]+=1
                if original is None:
                    undefined_both+=1
        witness.append({"native_expression":expr,"exe_dec_program":dsl,
                        "native_operation":op,"fixed_lambda":token,
                        "input_types":types})
    if len(witness)!=32:
        raise adm.Rejected("not all 32 safe fixed-lambda atoms witnessed")
    # Independent explicit native source counterexamples motivating exclusion.
    native_negative=operations["Access"].apply_single([-1,[1,2]])
    exact_negative=adm.execute([("x2","Access",["x0","x1"])],
                               {"x0":-1,"x1":[1,2]})
    if native_negative!=2 or exact_negative is not None:
        raise adm.Rejected("expected native negative-index semantic divergence disappeared")
    try:
        operations["Scanl1"].apply_single([operations["Add"].apply_single,[]])
    except (IndexError,ValueError):
        original_scan="UNDEFINED"
    else:
        raise adm.Rejected("expected native empty Scanl1 divergence disappeared")
    exact_scan=adm.execute([("x1","Scanl1",["(+)","x0"])],{"x0":[]})
    if exact_scan!=[]:
        raise adm.Rejected("expected ExeDec empty Scanl1 result changed")
    result={
      "status":"NATIVE_SOURCE_EXACT_SUBGRAMMAR_BRIDGE_WITNESSED",
      "schema":"gcl.owi-ds002.lambdabeam-native-28-to-exedec-bridge.v1",
      "source":provenance,"exedec_revision":adm.manifest()["origin"]["commit"],
      "witnesses":witness,
      "audit":{"admitted_exact_atomic_exedec_operations":len(witness),
               "total_exact_atomic_operations":38,
               "excluded_native_semantics":{"Access":1,"Scanl1":5},
               "finite_native_source_vs_exedec_comparisons":all_cases,
               "both_invalid":undefined_both,
               "mismatches":0,
               "per_operator_trial_counts":dict(byop),
               "native_Access_negative_index_result":native_negative,
               "exedec_Access_negative_index_result":exact_negative,
               "native_Scanl1_empty_result":original_scan,
               "exedec_Scanl1_empty_result":exact_scan},
      "limitations":[
        "This is exact syntax normalization for a deliberately restricted native expression subset, not a total translation of unrestricted original 28-op LambdaBeam programs",
        "Access and Scanl1 are rejected because their native and ExeDec empty/negative edge cases differ",
        "Each fixed lambda must be recognized by AST structure; no executing source code, observational matching, or closure-dependent adaptation",
        "Source-concordance comparisons are finite and only under ExeDec bounded admissible inputs/intermediates; not a universal equivalence proof",
        "This source-native witness audit is not trained pretrained-model inference; checkpoint head custody was separately verified in PR #501",
      ],
    }
    if cache is not None:
        coverage={}
        for split in adm.manifest()["splits"]:
            rows,blob=adm.source_rows(split,cache,offline=offline)
            excluded=Counter()
            compatible=0
            for row in rows:
                p=row["test_problem"]
                names,types,_=adm.validate_examples(p)
                code=adm.compile_program(p["program"],names,types)
                bad={op for _,op,_ in code if op in PROHIBITED}
                if not bad:
                    compatible+=1
                for op in bad:
                    excluded[op]+=1
            coverage[split]={"distinct_source_tasks":len(rows),
                             "reference_grammatically_eligible":compatible,
                             "excluded_reference_contains":dict(excluded),
                             "source_git_blob":blob}
        result["source_reference_structural_coverage"]={
            "scope":"retrospective published references only; never provided to trained or outcome-only search",
            "task_count":sum(x["distinct_source_tasks"] for x in coverage.values()),
            "syntactically_eligible":sum(x["reference_grammatically_eligible"] for x in coverage.values()),
            "by_split":coverage,
            "not_an_inference_success_rate":True,
        }
    return result


def check_candidates(records:list,cache:Path,offline:bool=False)->dict:
    """For future original 28-head trained search outputs; NO source solution in search."""
    if not isinstance(records,list) or not 1<=len(records)<=200:
        raise adm.Rejected("candidate receipt batch size invalid")
    results=[]
    for item in records:
        if not isinstance(item,dict) or set(item)!={"split","index","native_expression"}:
            raise adm.Rejected("candidate input must contain only split/index/native_expression")
        split,index,expr=item["split"],item["index"],item["native_expression"]
        if split not in adm.manifest()["splits"] or type(index) is not int or not 0<=index<200:
            raise adm.Rejected("unknown/invalid source task identity")
        rows,blob=adm.source_rows(split,cache,offline=offline)
        view=adm.participant_view(split,rows[index])
        view["source_blob"]=blob
        try:
            check=transfer_candidate(expr,view)
            candidate=check.pop("candidate")
            evaluator=(adm.verify(split,index,candidate,cache,offline=True,probes=16)
                       if candidate else None)
            outcome={**check,"translated_program":candidate,
                     "evaluator":evaluator,
                     "bounded_verified":evaluator is not None and
                         evaluator["status"]=="BOUNDED_EXECUTION_AGREEMENT_ONLY"}
        except adm.Rejected as exc:
            outcome={"status":"REJECTED_NATIVE_TRANSLATION","reason":str(exc),
                     "bounded_verified":False,"translated_program":None,
                     "evaluator":None}
        results.append({"task_id":view["task_id"],"split":split,"index":index,
                        "source_blob":blob,"outcome":outcome})
    return {"schema":"gcl.owi-ds002.lambdabeam-native-candidate-replay.v1",
            "status":"TRANSLATION_AND_INDEPENDENT_CHECKER_EXECUTED",
            "source_revision":adm.manifest()["origin"]["commit"],
            "count":len(results),
            "bounded_verified":sum(x["outcome"]["bounded_verified"] for x in results),
            "records":results,
            "restriction":"NO native source reference enters translation; independent evaluator accessed only after candidate emitted",
            "trained_model_status":"INCONCLUSIVE; candidate provenance not established by this adapter"}


def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-dir",required=True)
    ap.add_argument("--cache-dir",default="build/owi_ds002/exedec_sources")
    ap.add_argument("--offline",action="store_true")
    ap.add_argument("--mode",required=True,choices=("witness","candidates"))
    ap.add_argument("--candidate-file")
    ap.add_argument("--output",required=True)
    opts=ap.parse_args()
    start=time.perf_counter()
    try:
        root=Path(opts.source_dir)
        if opts.mode=="witness":
            result=witness_audit(root,Path(opts.cache_dir),offline=opts.offline)
        else:
            check_original_grammar(root)
            if not opts.candidate_file:
                raise adm.Rejected("missing candidate JSON")
            path=Path(opts.candidate_file)
            if not path.is_file() or path.stat().st_size>200_000:
                raise adm.Rejected("candidate JSON not bounded")
            receipts=json.loads(path.read_text(encoding="utf-8"))
            result=check_candidates(receipts,Path(opts.cache_dir),offline=opts.offline)
        result["job_wall_seconds"]=time.perf_counter()-start
        rc=0
    except (adm.Rejected,ValueError,TypeError,KeyError,OSError,RecursionError) as exc:
        result={"status":"REJECTED_OR_INCONCLUSIVE","reason":str(exc)}
        rc=2
    out=Path(opts.output)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("witnesses","records")},
                     indent=2,sort_keys=True))
    return rc

if __name__=="__main__":
    raise SystemExit(main())
