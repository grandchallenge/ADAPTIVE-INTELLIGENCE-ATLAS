#!/usr/bin/env python3
"""OWI-DS002: actual pinned original 28-head LambdaBeam neural inference PILOT.

This is **trained** inference with the original model architecture, source
synthesis algorithm, and actual source-lock-verified 40.75MB model checkpoint,
but with explicitly ADAPTED Access/Scanl1 runtime and strict candidate
translation to exact ExeDec. CPU pilot, NOT equal-compute model comparison.
Checkpoint unpickled ONLY with torch.load(weights_only=True) after exact-byte
Git/SHA custody; source-specific checkpoint optimizer is NEVER executed.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import math
from pathlib import Path
import random
import resource
import sys
import time
import types
from types import SimpleNamespace

import owi_ds002_exedec_admission as adm
import owi_ds002_lambdabeam_checkpoint_gate as custody
import owi_ds002_exedec_lambdabeam_external as upstream
import owi_ds002_lambdabeam_native_bridge as bridge
import owi_ds002_lambdabeam_semantics_adapter as adapted

TASKS=((name,0) for name in upstream.SPLITS)
PILOT_IDS=tuple((name,0) for name in upstream.SPLITS)
DEFAULT_MAX_VALUES=80
DEFAULT_TASK_SECONDS=7.0
DEFAULT_BEAM=2
MAX_TASKS=12


def _deny_offpath_scatter():
    """Single-task model does not use upstream training's scatter batch path."""
    mod=sys.modules.get("torch_scatter")
    if mod is not None:
        raise adm.Rejected("torch_scatter implementation already imported; not audited")
    mod=types.ModuleType("torch_scatter")
    calls=[]
    def unavailable(*args,**kwargs):
        calls.append("unsupported_training_batch_scatter")
        raise adm.Rejected("neural pilot must not invoke off-path scatter operation")
    mod.scatter_mean=unavailable
    mod.scatter_max=unavailable
    sys.modules["torch_scatter"]=mod
    return calls


def _args():
    # Actual original experiment runner overlays eval_config.get_config()
    # onto configs_all.get_config(). Only constructor-use fields are needed.
    return SimpleNamespace(
        use_op_specific_lstm=True,io_encoder="lambda_signature",
        value_encoder="lambda_signature",max_num_inputs=3,
        embed_dim=64,encode_weight=True,arg_selector="lstm",
        step_score_func="mlp",score_normed=True,
    )


def load_real_checkpoint(source_root:Path):
    """Source/hash verified, safe torch-only tensor checkpoint, exact strict weights."""
    custody.source_lock(source_root)
    upstream.check_source(source_root)
    original,ops,prov=adapted.load_adapted_operators(
        source_root,authentic_neural=True)
    import torch
    from lambdabeam.model.deepcoder_model import DeepCoderModel
    ckpt_path=source_root/custody.CHECKPOINT
    # Double custody: actual 40.75 MB checkpoint and pinned blob/SHA.
    raw=ckpt_path.read_bytes()
    if len(raw)!=custody.CHECKPOINT_SIZE or custody.hash_git_blob(raw)!=custody.CHECKPOINT_GIT_BLOB:
        raise adm.Rejected("pinned checkpoint Git byte identity mismatch")
    checksum=hashlib.sha256(raw).hexdigest()
    if checksum!="969450bc6bdba3c7402a3bffd56b116b41a0d842979e4cc59412988561c38043":
        raise adm.Rejected("pinned checkpoint SHA-256 mismatch")
    torch.manual_seed(11)
    torch.set_num_threads(1)
    try:
        checkpoint=torch.load(io.BytesIO(raw),map_location="cpu",weights_only=True)
    except Exception as exc:
        raise adm.Rejected("safe weights_only checkpoint load failed: "+
                           type(exc).__name__) from exc
    if (type(checkpoint) is not dict or
        set(checkpoint)!={"model","optimizer","step"} or
        not isinstance(checkpoint["model"],dict) or
        type(checkpoint["step"]) is not int):
        raise adm.Rejected("published checkpoint structure not safe expected schema")
    model=DeepCoderModel(_args(),ops)
    expected=model.state_dict()
    supplied=checkpoint["model"]
    if set(supplied)!=set(expected):
        raise adm.Rejected("checkpoint tensor state keys differ from full original 28-head architecture")
    for key in expected:
        a,b=supplied[key],expected[key]
        if (not torch.is_tensor(a) or a.shape!=b.shape or
            a.dtype!=b.dtype or not torch.isfinite(a).all().item()):
            raise adm.Rejected("checkpoint tensor shape/type/finite mismatch: "+key)
    model.load_state_dict(supplied,strict=True)
    model.eval()
    if list(model.op_idx_map)!=[repr(x) for x in original]:
        raise adm.Rejected("checkpoint model learned operation mapping changed")
    if len(model.op_specific_lstm)!=28 or len(model.init.op_specific_mod)!=28:
        raise adm.Rejected("checkpoint learned original 28 operation heads drift")
    del checkpoint,raw
    return torch,model,ops,{"original_repository":custody.REPO,
                            "source_commit":custody.UPSTREAM,
                            "source_blobs":len(custody.SOURCE_BLOBS)+len(upstream.BLOBS),
                            "checkpoint_blob":custody.CHECKPOINT_GIT_BLOB,
                            "checkpoint_sha256":checksum,
                            "checkpoint_training_step":checkpoint_step if False else None,
                            "weights_only":True,
                            "strict_model_state_loaded":True,
                            "trained_tensor_keys":len(expected),
                            "original_operation_heads":28,
                            "adapter_mode":adapted.SEMANTICS}


def _model_probe(torch,model,domain,task):
    from lambdabeam.algorithm import synthesis
    values=[]
    output=synthesis.init_values(task,domain,values)
    with torch.no_grad():
        io_embed=model.io([task.inputs_dict],[task.outputs],device=torch.device("cpu"))
        val_embed,signatures=model.val(values,device=torch.device("cpu"),
                                       output_values=output,need_signatures=True)
        weights=[v.get_weight() for v in values]
        encoded=model.encode_weight(val_embed,weights)
        operation=domain.operations[[repr(o) for o in domain.operations].index("Reverse")]
        init_embed=model.init(io_embed,encoded,operation)
        arg=model.arg(operation)
        logits=arg.step_score(arg.get_init_state(init_embed,batch_size=1),encoded)
    if (io_embed.shape!=(1,128) or
        len(values)<1 or not torch.isfinite(logits).all().item()):
        raise adm.Rejected("actual pretrained forward produced illegal dimensions/NaN")
    return {"io_embed_shape":list(io_embed.shape),
            "value_embeddings_shape":list(val_embed.shape),
            "pretrained_logits_shape":list(logits.shape),
            "pretrained_logits_sha256":hashlib.sha256(logits.detach().cpu().numpy().tobytes()).hexdigest(),
            "pretrained_logit_min":float(logits.min()),
            "pretrained_logit_max":float(logits.max()),
            "model_head":"Reverse","actual_forward_pass":True,
            "source_public_io_only":True}


def execute_pilot(source_root:Path,cache:Path,seed:int,max_values:int,
                  task_seconds:float,beam:int,only_task:tuple[str,int]|None=None)->dict:
    if not 1<=max_values<=1000 or not 0.5<=task_seconds<=20 or not 1<=beam<=10:
        raise adm.Rejected("experimental budget out of allowed range")
    if only_task and (only_task[0] not in adm.manifest()["splits"] or
                      type(only_task[1]) is not int or not 0<=only_task[1]<200):
        raise adm.Rejected("unknown preselected source task")
    # Fail closed if any original enumeration shim was loaded in this interpreter.
    shim=sys.modules.get("lambdabeam.property_signatures.property_signatures")
    if shim is not None:
        raise adm.Rejected("property-signatures already imported before real-model verification")
    calls=_deny_offpath_scatter()
    torch,model,ops,cust=load_real_checkpoint(source_root)
    from lambdabeam.algorithm import synthesis
    from lambdabeam.dsl import domains
    from lambdabeam.dsl.task import Task
    base_domain=domains.get_domain("deepcoder")
    if [repr(x) for x in base_domain.operations]!=[repr(x) for x in ops]:
        raise adm.Rejected("upstream DeepCoder full neural domain operation ordering drift")
    domain=base_domain._replace(operations=ops,small_value_filter=adapted.legal)
    if model.ops!=tuple(ops):
        raise adm.Rejected("trained model adapted op roster mismatch")
    task_list=[only_task] if only_task else list(PILOT_IDS)
    if len(task_list)>MAX_TASKS:
        raise adm.Rejected("too many pilot tasks")
    records=[]
    for split,index in task_list:
        rows,blob=adm.source_rows(split,cache,offline=False)
        view=adm.participant_view(split,rows[index])
        # Delete local source-reference-bearing object from search inputs.
        public_inputs=view["inputs"]
        public_outputs=view["outputs"]
        names,types,n=adm.validate_examples(view)
        task=Task(public_inputs,public_outputs,solution=None,
                  name=split+":"+str(index))
        torch.manual_seed(seed)
        random.seed(seed)
        probe=_model_probe(torch,model,domain,task)
        start_wall=time.perf_counter()
        start_cpu=time.process_time()
        first=None
        stats={}
        outcome="NO_NATIVE_CANDIDATE"
        with torch.no_grad():
            try:
                first,(_, _),stats=synthesis.synthesize(
                    task,domain,model,device=torch.device("cpu"),
                    max_weight=12,k=beam,is_training=False,
                    timeout=task_seconds,max_values_explored=max_values,
                    is_stochastic=False,random_beam=False,use_ur=False,
                    masking=False,static_weight=False,temperature=1.0)
            except (AssertionError,IndexError,ValueError,RuntimeError,
                    TypeError,RecursionError) as exc:
                outcome="NATIVE_SEARCH_DIAGNOSTIC_EXCEPTION"
                stats={"exception_type":type(exc).__name__,
                       "exception_message":str(exc)[:500]}
        wall=time.perf_counter()-start_wall
        cpu=time.process_time()-start_cpu
        expression=None
        candidate=None
        evaluation=None
        if first is not None:
            expression=first.expression()
            outcome="NATIVE_PUBLIC_IO_CANDIDATE"
            try:
                candidate=bridge.translate(expression,types,semantics=adapted.SEMANTICS)
                compiled=adm.compile_program(candidate,names,types)
                good_public=all(adm.execute(compiled,{k:public_inputs[k][i] for k in names})
                                ==public_outputs[i] for i in range(n))
                if good_public:
                    evaluation=adm.verify(split,index,candidate,cache,
                                          offline=True,probes=16)
                    outcome=("INDEPENDENT_BOUNDED_VERIFIED" if
                             evaluation["status"]=="BOUNDED_EXECUTION_AGREEMENT_ONLY"
                             else "EVALUATOR_REFUSED_CANDIDATE")
                else:
                    candidate=None
                    outcome="EXEDEC_PUBLIC_IO_REJECTED"
            except adm.Rejected as exc:
                outcome="NATIVE_EXPRESSION_TRANSLATION_REJECTED"
                stats["translator_rejection"]=str(exc)
        rr=resource.getrusage(resource.RUSAGE_SELF)
        records.append({"task_id":view["task_id"],"source_blob":blob,
                        "participant_view_only":True,
                        "native_pretrained_generated_expression":expression,
                        "translated_candidate":candidate,
                        "independent_evaluator":evaluation,
                        "outcome":outcome,"model_actual_pretrained_probe":probe,
                        "source_search_stats":stats,
                        "search_cpu_seconds":cpu,"search_wall_seconds":wall,
                        "process_peak_rss_kb":rr.ru_maxrss,
                        "model_source_training_step":cust["checkpoint_training_step"],
                        "seed":seed,"beam":beam,"max_weight":12,
                        "max_values_budget":max_values,
                        "max_task_wall_seconds":task_seconds})
        print(json.dumps({"task":view["task_id"],"outcome":outcome,
                          "native_expression":expression,
                          "cpu_seconds":round(cpu,4),
                          "explored":stats.get("num_values_explored")}),flush=True)
    if calls:
        raise adm.Rejected("off-path training scatter called: "+repr(calls))
    report={"schema":"gcl.owi-ds002.real-checkpoint-native-beam-pilot.v1",
            "status":"REAL_ORIGINAL_TRAINED_CHECKPOINT_MODEL_FORWARD_AND_NATIVE_SEARCH_EXECUTED",
            "source":cust,"device":"cpu",
            "search_algorithm":"original published lambdabeam.algorithm.synthesis.synthesize",
            "adapter":"EXPLICIT adapted Access/Scanl1 28-head roster; not unmodified original",
            "task_preselection":"index 0, one from each of six ExeDec source splits, before search",
            "num_tasks":len(records),
            "checkpoint_backed_real_model_forwards":sum(r["model_actual_pretrained_probe"]["actual_forward_pass"] for r in records),
            "native_public_io_candidates":sum(r["native_pretrained_generated_expression"] is not None for r in records),
            "typed_translated_candidates":sum(r["translated_candidate"] is not None for r in records),
            "independently_bounded_verified":sum(r["outcome"]=="INDEPENDENT_BOUNDED_VERIFIED" for r in records),
            "offpath_scatter_calls":len(calls),
            "total_search_cpu_seconds":sum(r["search_cpu_seconds"] for r in records),
            "total_search_wall_seconds":sum(r["search_wall_seconds"] for r in records),
            "records":records,
            "scope_limits":[
                "Actual exact published pretrained checkpoint and native trained search are executed, not merely original enumeration",
                "Synthesis uses explicit Access/Scanl1 semantic adaptation: NOT unmodified original trained LambdaBeam deployment",
                "Source reference programme not supplied to neural inference; reference only accessible after typed public-input candidate via independent source verifier",
                "No solved rate over 1200 public tasks from this tiny preregistered six task CPU pilot",
                "CPU wall/time budgets are not equal resource budgets across GCL/external approaches",
                "No trained model retraining, no C1 legal chosen-run derivative or D causal self-model claim",
            ]}
    return report


def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument("--source-dir",required=True)
    p.add_argument("--cache-dir",default="build/owi_ds002/exedec_sources")
    p.add_argument("--output",required=True)
    p.add_argument("--seed",type=int,default=11)
    p.add_argument("--max-values",type=int,default=DEFAULT_MAX_VALUES)
    p.add_argument("--task-seconds",type=float,default=DEFAULT_TASK_SECONDS)
    p.add_argument("--beam",type=int,default=DEFAULT_BEAM)
    p.add_argument("--split",default="")
    p.add_argument("--index",type=int,default=0)
    o=p.parse_args()
    start=time.perf_counter()
    try:
        chosen=(o.split,o.index) if o.split else None
        result=execute_pilot(Path(o.source_dir),Path(o.cache_dir),o.seed,
                             o.max_values,o.task_seconds,o.beam,only_task=chosen)
        rc=0
    except Exception as exc:
        result={"status":"REJECTED_OR_INCONCLUSIVE","exception":type(exc).__name__,
                "error":str(exc)[:800]}
        rc=2
    result["total_job_wall_seconds"]=time.perf_counter()-start
    target=Path(o.output)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="records"},sort_keys=True,indent=2),flush=True)
    return rc

if __name__=="__main__":
    raise SystemExit(main())
