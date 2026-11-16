#!/usr/bin/env python3
"""Pinned original pretrained neural solver: independent *synthetic* positive controls.

No benchmark source reference is read by these controls. These two simple
public-only IO tasks probe whether the source-locked actual 205k pretrained
model's ORIGINAL neural search can emit a typed candidate and independently
agree with a known exact ExeDec program on 16 fresh inputs. They are explicitly
NOT held-out, benchmark rates, or equal resource comparators.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import random
import resource
import sys
import time

import owi_ds002_exedec_admission as adm
import owi_ds002_lambdabeam_native_bridge as bridge
import owi_ds002_lambdabeam_semantics_adapter as adapter
import owi_ds002_lambdabeam_trained_pilot as pilot

CONTROLS={
    "Reverse":{"examples":[[3,1,-2],[],[4],[0,-3,2],[2,2,5]],
               "reference":"x0 = INPUT | x1 = Reverse x0"},
    "Sum":{"examples":[[3,1],[],[-1,5,2],[2],[-3,-2]],
           "reference":"x0 = INPUT | x1 = Sum x0"},
}
FRESH=tuple([
    [],[0],[1],[-1],[2,3],[-3,2],[5,-2,0],[-4,-3,-2,1],
    [1,1,1],[2,2],[4,5,0],[0,3,-3],[-1,0,1],[-2,-2,2],
    [4,-4,1],[3,1,2,0,4],
])


def evaluate(source:Path,seed:int,max_values:int,beam:int,
             seconds:float)->dict:
    if not 100<=max_values<=10000 or not 1<=beam<=10 or not 1<=seconds<=20:
        raise adm.Rejected("invalid pretrained positive-control budget")
    calls=pilot._deny_offpath_scatter()
    torch,model,ops,source_receipt=pilot.load_real_checkpoint(source)
    from lambdabeam.algorithm import synthesis
    from lambdabeam.dsl import domains
    from lambdabeam.dsl.task import Task
    d=domains.get_domain("deepcoder")
    if [repr(x) for x in d.operations]!=[repr(x) for x in ops]:
        raise adm.Rejected("original learned 28 operator head identity drift")
    domain=d._replace(operations=ops,small_value_filter=adapter.legal)
    records=[]
    for name,item in CONTROLS.items():
        reference=adm.compile_program(item["reference"],["x0"],{"x0":"L"})
        batch=item["examples"]
        outputs=[adm.execute(reference,{"x0":list(values)}) for values in batch]
        assert all(out is not None for out in outputs)
        t=Task(inputs_dict={"x0":batch},outputs=outputs,solution=None,name="SYNTHETIC_POSITIVE_CONTROL_"+name)
        torch.manual_seed(seed)
        random.seed(seed)
        import numpy as np
        np.random.seed(seed)
        beginning=time.perf_counter()
        cpustart=time.process_time()
        first=None
        stats={}
        failure=None
        with torch.no_grad():
            try:
                first,(_, _),stats=synthesis.synthesize(
                    t,domain,model,device=torch.device("cpu"),max_weight=12,
                    k=beam,is_training=False,timeout=seconds,
                    max_values_explored=max_values,use_ur=True,masking=False,
                    is_stochastic=False,random_beam=False,
                    static_weight=False,temperature=1.0)
            except (AssertionError,IndexError,ValueError,RuntimeError,TypeError) as exc:
                failure={"type":type(exc).__name__,"message":str(exc)[:400]}
        cpu=time.process_time()-cpustart
        wall=time.perf_counter()-beginning
        expression=first.expression() if first is not None else None
        output=None
        verified=0
        reject=None
        if expression is not None:
            try:
                output=bridge.translate(expression,{"x0":"L"},semantics=adapter.SEMANTICS)
                code=adm.compile_program(output,["x0"],{"x0":"L"})
                if not all(adm.execute(code,{"x0":xs})==target
                           for xs,target in zip(batch,outputs)):
                    reject="PUBLIC_EXAMPLES_NOT_EXEDEC_AGREEMENT"
                    output=None
                else:
                    for xs in FRESH:
                        expected=adm.execute(reference,{"x0":list(xs)})
                        if expected is None: continue
                        observed=adm.execute(code,{"x0":list(xs)})
                        if expected!=observed:
                            reject="FRESH_COUNTEREXAMPLE"
                            break
                        verified+=1
            except adm.Rejected as exc:
                reject="UNSUPPORTED_NATIVE_EXPRESSION:"+str(exc)
                output=None
                verified=0
        rows={"name":name,"task_class":"SYNTHETIC_POSITIVE_CONTROL_NOT_PUBLIC_BENCHMARK",
              "native_model_expression":expression,"translated_exedec":output,
              "fresh_probe_agreements":verified,"fresh_probe_budget":len(FRESH),
              "native_search_exception":failure,"source_search_stats":stats,
              "search_cpu_seconds":cpu,"search_wall_seconds":wall,
              "typed_translation_rejection":reject,
              "independently_synthetic_bounded_validated":output is not None and verified==len(FRESH)}
        records.append(rows)
        print(json.dumps({"control":name,"native":expression,"candidate":output,
                          "fresh_agreements":verified,"rejection":reject,
                          "explored":stats.get("num_values_explored"),
                          "cpu_seconds":round(cpu,5)}),flush=True)
    if calls:
        raise adm.Rejected("off-path upstream scatter was invoked")
    return {"schema":"gcl.owi-ds002.original-trained-neural-synthetic-positive-controls.v1",
            "status":"AUTHENTIC_CHECKPOINT_NEURAL_SEARCH_POSITIVE_CONTROLS_EXECUTED",
            "source":source_receipt,
            "device":"cpu","seed":seed,"beam":beam,
            "max_values":max_values,"max_seconds_per_control":seconds,
            "num_controls":len(records),
            "native_solutions":sum(z["native_model_expression"] is not None for z in records),
            "typed_candidates":sum(z["translated_exedec"] is not None for z in records),
            "independently_bounded_verified":sum(z["independently_synthetic_bounded_validated"] for z in records),
            "offpath_scatter_calls":len(calls),
            "max_rss_kb":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "records":records,
            "disclaimers":[
                "Synthetic controls are NOT sampled public ExeDec source benchmark tasks or trained policy evaluation accuracy",
                "Reference solutions for synthetic controls are fixed a priori for verification and never passed to original neural search",
                "Checkpoint original trained weights; explicit ExeDec Access/Scanl1 runtime adapter is not unmodified original LambdaBeam",
                "Finite 16 fresh sample agreement does not prove universal equivalence",
                "No equal-compute trained A/B/C/D, legal JVP C1 or D causal identification",
            ]}


def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-dir",required=True)
    ap.add_argument("--output",required=True)
    ap.add_argument("--seed",type=int,default=11)
    ap.add_argument("--beam",type=int,default=10)
    ap.add_argument("--max-values",type=int,default=5000)
    ap.add_argument("--task-seconds",type=float,default=12)
    o=ap.parse_args()
    try:
        result=evaluate(Path(o.source_dir),o.seed,o.max_values,o.beam,o.task_seconds)
        rc=0
    except Exception as exc:
        result={"status":"REJECTED_OR_INCONCLUSIVE","exception":type(exc).__name__,
                "error":str(exc)[:900]}
        rc=2
    dest=Path(o.output)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="records"},sort_keys=True),flush=True)
    return rc


if __name__=="__main__":
    raise SystemExit(main())
