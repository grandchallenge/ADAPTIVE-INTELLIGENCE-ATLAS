#!/usr/bin/env python3
"""Exact-ExeDec DSL adapter for original, hash-locked LambdaBeam enumeration.

The independently published bottom-up search runs unchanged. Its pretrained
neural policy is NOT used. ExeDec DSL operations are enacted by the existing
source-concordance-tested interpreter; no reference program reaches search.
"""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import io
import json
from pathlib import Path
import random
import resource
import subprocess
import sys
import time
from types import SimpleNamespace

import owi_ds002_exedec_admission as adm

SOURCE = "61986dc1a6d8cc9521fb17e3152f7f085b5d7c95"
BLOBS = {
 "lambdabeam/algorithm/baseline_enumeration.py": "9516ffb26e95e3208fc41e1773955bbfa39b36ef",
 "lambdabeam/algorithm/variables.py": "c49f016fc241e4eca5c5388cda0072bfcd373293",
 "lambdabeam/dsl/value.py": "b04094fe4b7528d41cd7fe70fbf26e433ba70c66",
 "lambdabeam/dsl/operation_base.py": "7ea6b5c4dc36b5fa5c2965676786bee5659107c3",
 "lambdabeam/dsl/task.py": "b76f3a8d29c02e727ac328a542760014e2cc9c0d",
 "lambdabeam/property_signatures/property_signatures.py": "f93b313edf1c07c743b6350ff56085d310cc86c6",
 "lambdabeam/dsl/domains.py": "970e78c78df1e5e1a39c4252990ed10bcbec5cb1",
 "lambdabeam/dsl/deepcoder_operations.py": "d33550eae87de3c4f5717aeca9247e7e5eaa9776",
}
SPLITS = ("NONE","LENGTH_GENERALIZATION","COMPOSE_DIFFERENT_CONCEPTS",
          "SWITCH_CONCEPT_ORDER","COMPOSE_NEW_OP","ADD_OP_FUNCTIONALITY")

def check_source(root):
    root=Path(root).resolve()
    if not (root/".git").is_dir():
        raise adm.Rejected("missing external Git checkout")
    sha=subprocess.run(["git","-C",str(root),"rev-parse","HEAD"],check=True,
                       capture_output=True,text=True,timeout=10).stdout.strip()
    if sha!=SOURCE:
        raise adm.Rejected("external source revision drift")
    for rel,expected in BLOBS.items():
        path=root/rel
        if not path.is_file() or adm.git_blob(path.read_bytes())!=expected:
            raise adm.Rejected("external source blob drift: "+rel)
    return {"repository":"ellisk42/LambdaBeam","commit":SOURCE,
            "verified_git_blobs":len(BLOBS),
            "original_baseline_source_blob":BLOBS["lambdabeam/algorithm/baseline_enumeration.py"]}

def load(root):
    root=Path(root).resolve()
    check_source(root)
    if str(root) not in sys.path:
        sys.path.insert(0,str(root))
    # Official enumeration imports property_signatures only when generating
    # general lambda expressions. ExeDec grammar uses strictly closed,
    # finite fixed lambda tokens and the search config forbids free variables.
    # An explicit fail-closed stub avoids pulling the UNUSED neural-training
    # import graph (including torch). Reaching the stub is a hard failure.
    import types
    shim="lambdabeam.property_signatures.property_signatures"
    if shim not in sys.modules:
        unused=types.ModuleType(shim)
        def _forbidden_lambda(*args,**kwargs):
            raise adm.Rejected("invalid free-variable lambda path in exact ExeDec")
        unused.run_lambda=_forbidden_lambda
        sys.modules[shim]=unused
    from lambdabeam.algorithm import baseline_enumeration as algorithm
    from lambdabeam.algorithm import variables
    from lambdabeam.dsl import operation_base, value, task
    if Path(algorithm.__file__).resolve() != (root/"lambdabeam/algorithm/baseline_enumeration.py"):
        raise adm.Rejected("unexpected external Python import")
    return algorithm,variables,operation_base,value,task

def public_only(view):
    if set(view)-{"status","task_id","inputs","outputs","input_output_examples",
                  "target_program_exposed","source_blob"}:
        raise adm.Rejected("private field delivered to external search")
    if view.get("target_program_exposed") is not False:
        raise adm.Rejected("reference not masked")
    return adm.validate_examples(view)

def legal(value):
    try:
        adm.kind(value)
        return True
    except adm.Rejected:
        return False

def make_domain(base):
    class ExactOp(base.OperationBase):
        def __init__(self,op,lam,sig,typ):
            self.exedec_op=op
            self.exedec_lambda=lam
            self.register_types=tuple(c for c in sig if c in ("L","I"))
            self.result_type=typ
            super().__init__("Exact"+op+"-"+lam,len(self.register_types),weight=1)
        def __repr__(self):
            return "ExactExeDec("+self.exedec_op+","+self.exedec_lambda+")"
        def arg_types(self):
            return tuple(int if c=="I" else list for c in self.register_types)
        def return_type(self):
            return int if self.result_type=="I" else list
        def apply_single(self,args):
            if not all(legal(v) for v in args):
                return None
            vars=["v"+str(i) for i in range(len(args))]
            tokens=([self.exedec_lambda] if self.exedec_lambda else [])+vars
            return adm.execute([("z",self.exedec_op,tokens)],dict(zip(vars,args)))
    ops=[]
    for op,(sig,typ) in sorted(adm.OPERATIONS.items()):
        if "U" in sig: lambdas=sorted(adm.UNARY)
        elif "P" in sig: lambdas=sorted(adm.PRED)
        elif "B" in sig: lambdas=sorted(adm.BINARY)
        else: lambdas=[""]
        ops.extend(ExactOp(op,lam,sig,typ) for lam in lambdas)
    if len(ops)!=len(set(map(repr,ops))):
        raise adm.Rejected("nonunique grammar operations")
    return SimpleNamespace(operations=ops,constants=[],constants_extractor=None,
                           small_value_filter=legal)

def extract(node,names,value):
    if node is None: return None
    lines=[x+" = INPUT" for x in names]
    seen={}
    def build(x):
        if isinstance(x,value.InputVariable):
            if x.name not in names: raise adm.Rejected("unknown input")
            return x.name
        if not isinstance(x,value.OperationValue):
            raise adm.Rejected("unsupported external expression")
        if id(x) in seen: return seen[id(x)]
        op=x.operation
        if not hasattr(op,"exedec_op") or op.exedec_op not in adm.OPERATIONS:
            raise adm.Rejected("unapproved operation")
        args=[build(child) for child in x.arg_values]
        dest="x"+str(len(lines))
        parts=[dest,"=",op.exedec_op]
        if op.exedec_lambda: parts.append(op.exedec_lambda)
        parts.extend(args)
        lines.append(" ".join(parts))
        seen[id(x)]=dest
        return dest
    build(node)
    if not len(names)<len(lines)<=adm.MAX_LINES:
        raise adm.Rejected("invalid candidate program size")
    return " | ".join(lines)

def synthesize(view,root,*,seed,max_weight,max_explored,timeout):
    names,types,n=public_only(view)
    if not 1<=seed<=2**32-1 or not 2<=max_weight<=10 or not 10<=max_explored<=2000000 or not .1<=timeout<=30:
        raise adm.Rejected("invalid external budget")
    algorithm,variables,base,value,task=load(root)
    domain=make_domain(base)
    source_task=task.Task({k:view["inputs"][k] for k in names},
                          view["outputs"],solution=None,name=view["task_id"])
    prior=variables.MAX_NUM_FREE_VARS
    stdout=io.StringIO()
    start_wall,start_cpu=time.perf_counter(),time.process_time()
    try:
        # ExeDec has a fixed set of lambdas. Configure original search with
        # no general/free lambdas, since all fixed lambdas are atomic ops.
        variables.MAX_NUM_FREE_VARS=0
        random.seed(seed)
        with contextlib.redirect_stdout(stdout):
            result,_,_,stats=algorithm.synthesize_baseline(
                source_task,domain,max_weight=max_weight,timeout=timeout,
                max_values_explored=max_explored,shuffle_ops=True)
    finally:
        variables.MAX_NUM_FREE_VARS=prior
    candidate=None
    status="NO_PUBLIC_IO_CANDIDATE"
    if result is not None:
        try:
            candidate=extract(result,names,value)
            instructions=adm.compile_program(candidate,names,types)
            if not all(adm.execute(instructions,{k:view["inputs"][k][j] for k in names})
                       ==view["outputs"][j] for j in range(n)):
                status="REJECTED_PUBLIC_EXAMPLES"
                candidate=None
            else: status="PUBLIC_IO_CANDIDATE_FOUND"
        except adm.Rejected:
            status="UNTRANSLATABLE_EXTERNAL_CANDIDATE"
            candidate=None
    return {"status":status,"candidate":candidate,
            "seed":seed,"counts":stats,
            "search_wall_seconds":time.perf_counter()-start_wall,
            "search_cpu_seconds":time.process_time()-start_cpu,
            "process_peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "original_stdout_sha256":hashlib.sha256(stdout.getvalue().encode()).hexdigest(),
            "source_leakage_controls":"published I/O only",
            "algorithm_identity":"unmodified external LambdaBeam bottom-up enumeration",
            "fixed_lambda_configuration":"free-variable count zero"}

def run(root,cache,splits,indices,seeds,*,max_weight,max_explored,timeout,probes,offline):
    external=check_source(root)
    pinned={}
    for split in splits:
        rows,blob=adm.source_rows(split,cache,offline=offline)
        if any(k<0 or k>=len(rows) for k in indices):
            raise adm.Rejected("invalid source index")
        pinned[split]=(rows,blob)
    records=[]
    started=time.perf_counter()
    for split,(rows,blob) in pinned.items():
        for index in indices:
            view=adm.participant_view(split,rows[index])
            view["source_blob"]=blob
            sha=hashlib.sha256(json.dumps(view,sort_keys=True).encode()).hexdigest()
            for seed in seeds:
                outcome=synthesize(view,root,seed=seed,max_weight=max_weight,
                                   max_explored=max_explored,timeout=timeout)
                candidate=outcome.pop("candidate")
                ev=None
                start_eval=time.perf_counter()
                if candidate:
                    ev=adm.verify(split,index,candidate,cache,offline=True,probes=probes)
                records.append({"task_id":view["task_id"],"split":split,"index":index,
                                "seed":seed,"public_projection_sha256":sha,
                                "source_git_blob_sha":blob,"search":outcome,
                                "candidate_program":candidate,"evaluator":ev,
                                "evaluator_wall_seconds":time.perf_counter()-start_eval,
                                "bounded_verified":ev is not None and
                                    ev["status"]=="BOUNDED_EXECUTION_AGREEMENT_ONLY"})
    return {"schema":"gcl.owi-ds002.external-lambdabeam-exact-adapter.v1",
            "status":"ORIGINAL_EXTERNAL_ENUMERATOR_EXACT_EXEDEC_ADAPTER_EXECUTED",
            "external_source":external,"exedec_source_revision":adm.manifest()["origin"]["commit"],
            "protocol":{"splits":splits,"indices":indices,"seeds":seeds,
                        "max_weight":max_weight,"max_explored":max_explored,
                        "timeout_seconds":timeout,"probes":probes,
                        "source_reference_used_for_search":False},
            "aggregate":{"trial_count":len(records),"distinct_tasks":len(splits)*len(indices),
                         "public_candidates":sum(x["candidate_program"] is not None for x in records),
                         "bounded_verified":sum(x["bounded_verified"] for x in records),
                         "search_explored":sum(x["search"]["counts"]["num_values_explored"] for x in records),
                         "search_cpu_seconds":sum(x["search"]["search_cpu_seconds"] for x in records),
                         "search_wall_seconds":sum(x["search"]["search_wall_seconds"] for x in records),
                         "end_to_end_wall_seconds":time.perf_counter()-started,
                         "process_peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},
            "by_split":{split:{"trials":sum(x["split"]==split for x in records),
                               "verified":sum(x["bounded_verified"] and x["split"]==split for x in records)}
                        for split in splits},"records":records,
            "limitations":[
                "Original independent published enumeration, NOT trained LambdaBeam neural search",
                "GCL exact ExeDec DSL adapter and extraction are new and separately audited",
                "No full-compute equal matching; original source algorithm and new search use different costs",
                "Public benchmark source and reference solutions are not secret",
                "Finite evaluator probes give bounded agreement, not universal equivalence",
                "No real C1 JVP or D causal intervention/reflective policy tested"]}

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--source-dir",required=True)
    a.add_argument("--splits",default=",".join(SPLITS))
    a.add_argument("--indices",default="0,17")
    a.add_argument("--seeds",default="1,2,3,4,5")
    a.add_argument("--max-weight",type=int,default=7)
    a.add_argument("--max-explored",type=int,default=15000)
    a.add_argument("--timeout-seconds",type=float,default=1.5)
    a.add_argument("--probes",type=int,default=16)
    a.add_argument("--cache-dir",default="build/owi_ds002/exedec_sources")
    a.add_argument("--offline",action="store_true")
    a.add_argument("--output",required=True)
    args=a.parse_args()
    try:
        splits=args.splits.split(",")
        indices=[int(v) for v in args.indices.split(",")]
        seeds=[int(v) for v in args.seeds.split(",")]
        if not splits or len(set(splits))!=len(splits) or any(v not in SPLITS for v in splits) or not 1<=len(indices)<=50 or len(set(indices))!=len(indices) or any(v<0 for v in indices) or not 1<=len(seeds)<=10 or len(set(seeds))!=len(seeds) or any(v<1 or v>2**32-1 for v in seeds):
            raise adm.Rejected("invalid external cohort")
        data=run(Path(args.source_dir),Path(args.cache_dir),splits,indices,seeds,
                 max_weight=args.max_weight,max_explored=args.max_explored,
                 timeout=args.timeout_seconds,probes=args.probes,offline=args.offline)
    except (adm.Rejected,ValueError,OSError,subprocess.SubprocessError,MemoryError) as exc:
        data={"status":"REJECTED_OR_INCONCLUSIVE","error":str(exc)}
    dest=Path(args.output)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in data.items() if k!="records"},indent=2,sort_keys=True))
    return 0 if data["status"]=="ORIGINAL_EXTERNAL_ENUMERATOR_EXACT_EXEDEC_ADAPTER_EXECUTED" else 2

if __name__=="__main__":
    raise SystemExit(main())
