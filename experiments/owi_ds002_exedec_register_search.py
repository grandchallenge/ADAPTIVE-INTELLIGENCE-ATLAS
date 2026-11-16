#!/usr/bin/env python3
"""OWI-DS-002: ExeDec-semantics-exact outcome-only register-program search.

Unlike the historical 2017 C++ solver, every successor is evaluated with the
source-checked 2024 ExeDec interpreter. Searches finite straight-line typed
register programs (including DAGs and shared intermediates); no target source,
generated evaluator probes, gradient, or independent checker is used to search.
This is a new non-differential comparator, not an independently authored
external mature solver nor a universal equivalence proof.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import itertools
import json
from pathlib import Path
import random
import resource
import time

import owi_ds002_exedec_admission as adm
from owi_ds002_exedec_enumerator import DEFAULT_SPLITS, DEFAULT_INDICES, DEFAULT_SEEDS


@dataclass(slots=True)
class State:
    types: tuple[str, ...]
    observations: tuple[tuple, ...]  # aligned list of values for each register
    statements: tuple[tuple[str, str, tuple[str, ...]], ...]
    score: float = 0.0


def public_only(view: dict):
    if set(view) - {"status", "task_id", "inputs", "outputs",
                    "input_output_examples", "target_program_exposed",
                    "source_blob"}:
        raise adm.Rejected("search input contains non-public fields")
    if view.get("target_program_exposed") is not False:
        raise adm.Rejected("target program not withheld")
    return adm.validate_examples(view)


def signature(observations: tuple) -> str:
    return json.dumps(observations, separators=(",", ":"), ensure_ascii=True)


def _plans(seed: int):
    """Seeded task-independent order over grammar operations and lambdas."""
    rng = random.Random(seed)
    plans = []
    for op, (sig, out) in sorted(adm.OPERATIONS.items()):
        choices = []
        for token in sig:
            if token == "U":
                choices.append(sorted(adm.UNARY))
            elif token == "P":
                choices.append(sorted(adm.PRED))
            elif token == "B":
                choices.append(sorted(adm.BINARY))
            elif token in ("I", "L"):
                choices.append([token])
            else:
                raise adm.Rejected("unrecognized source grammar signature")
        for expanded in itertools.product(*choices):
            plans.append((op, tuple(expanded), out))
    rng.shuffle(plans)
    return plans


def transitions(state: State, plan):
    op, signature, typ = plan
    options = []
    for token in signature:
        if token in ("I", "L"):
            options.append(["x"+str(i) for i, old_type in
                            enumerate(state.types) if old_type == token])
        else:
            options.append([token])
    for args in itertools.product(*options):
        yield op, tuple(args), typ


def _apply(state: State, operation: str, args: tuple[str, ...], output_type: str):
    dest = "x" + str(len(state.types))
    instruction = (dest, operation, list(args))
    n = len(state.observations[0])
    computed = []
    for case_index in range(n):
        env = {"x"+str(i): state.observations[i][case_index]
               for i in range(len(state.types))}
        value = adm.execute([instruction], env)
        if value is None:
            return None
        computed.append(value)
    # All generated intermediate values and results have passed the
    # identical independent ExeDec operation and value bounds.
    return tuple(computed)


def _distance(values: tuple, expected: tuple, output_type: str) -> float:
    score = 0.0
    for actual, desired in zip(values, expected):
        if output_type == "I":
            score += abs(actual-desired)
        else:
            score += abs(len(actual)-len(desired))*12
            score += sum(abs(a-b) for a,b in zip(actual,desired))
    return score/len(values)


def _to_program(names: list[str], statements: tuple) -> str:
    lines=[n+" = INPUT" for n in names]
    for dest, op, args in statements:
        lines.append(" ".join([dest,"=",op]+list(args)))
    return " | ".join(lines)


def synthesize(view: dict, *, seed: int, max_nodes: int = 4,
               max_evals: int = 15000, beam_width: int = 160,
               time_limit_seconds: float = 1.5) -> dict:
    names, initial_types, n=public_only(view)
    if not (1 <= seed <= 2**32-1 and 1 <= max_nodes <= 6 and
            1 <= max_evals <= 2000000 and 4 <= beam_width <= 5000 and
            .05 <= time_limit_seconds <= 120.):
        raise adm.Rejected("unsafe solver budget")
    target=tuple(view["outputs"])
    target_type=adm.kind(target[0])
    if any(adm.kind(v)!=target_type for v in target):
        raise adm.Rejected("inconsistent output type")
    input_obs=tuple(tuple(view["inputs"][name]) for name in names)
    initial=State(tuple(initial_types[n] for n in names),input_obs,())
    first_cpu=time.process_time()
    first_wall=time.perf_counter()
    attempts=invalid=observed_duplicate=state_duplicate=0
    candidate_matches=0
    expanded=0
    frontier=[initial]
    retained=[len(frontier)]
    plans=_plans(seed)
    rng=random.Random(seed^0x571F1E)
    final=None
    reason="EXHAUSTED_FINITE_FRONTIER"
    # Two complementary beam components: numerical closeness and a seeded
    # diversity reserve. Numerical distance is based ONLY on published I/O.
    for depth in range(1,max_nodes+1):
        candidates=[]
        seen_states=set()
        timeout=False
        for state in frontier:
            if attempts >= max_evals or time.perf_counter()-first_wall >= time_limit_seconds:
                reason=("EVAL_BUDGET_EXHAUSTED" if attempts>=max_evals
                        else "WALL_BUDGET_EXHAUSTED")
                timeout=True
                break
            expanded+=1
            for plan in plans:
                for op,args,out_type in transitions(state,plan):
                    if attempts >= max_evals or time.perf_counter()-first_wall >= time_limit_seconds:
                        reason=("EVAL_BUDGET_EXHAUSTED" if attempts>=max_evals
                                else "WALL_BUDGET_EXHAUSTED")
                        timeout=True
                        break
                    attempts+=1
                    values=_apply(state,op,args,out_type)
                    if values is None:
                        invalid+=1
                        continue
                    if out_type==target_type and values==target:
                        # A candidate is admitted on *public* I/O only here;
                        # source reference and independent probe calls happen
                        # later in a separate evaluator-only interface.
                        statement=("x"+str(len(state.types)),op,args)
                        program=_to_program(names,state.statements+(statement,))
                        try:
                            code=adm.compile_program(program,names,initial_types)
                            matches=all(adm.execute(code,{name:view["inputs"][name][j]
                                                         for name in names})==target[j]
                                        for j in range(n))
                        except adm.Rejected:
                            matches=False
                        candidate_matches+=1
                        if matches:
                            final=program
                            reason="PUBLIC_EXAMPLES_MATCH"
                            break
                    sig=signature(values)
                    if any(t==out_type and signature(obs)==sig
                           for t,obs in zip(state.types,state.observations)):
                        observed_duplicate+=1
                        continue
                    reg_key=tuple(sorted((t,signature(obs)) for t,obs in
                        zip(state.types+(out_type,),state.observations+(values,))))
                    if reg_key in seen_states:
                        state_duplicate+=1
                        continue
                    seen_states.add(reg_key)
                    score=(_distance(values,target,target_type)
                           if out_type==target_type else 1000.)
                    statement=("x"+str(len(state.types)),op,args)
                    candidates.append(State(
                        state.types+(out_type,),
                        state.observations+(values,),
                        state.statements+(statement,),score))
                if timeout or final is not None:
                    break
            if timeout or final is not None:
                break
        if final is not None:
            retained.append(len(candidates))
            break
        if not candidates:
            retained.append(0)
            if timeout:
                break
            frontier=[]
            continue
        # One deterministic top-ranked component plus uniform seeded reserve.
        # This is never an oracle, gradient, or reference-program heuristic.
        ranked=sorted(candidates,key=lambda s:s.score)
        focused=ranked[:int(beam_width*.65)]
        unselected=ranked[len(focused):]
        diversity=rng.sample(unselected,min(beam_width-len(focused),len(unselected)))
        frontier=focused+diversity
        rng.shuffle(frontier)
        retained.append(len(frontier))
        if timeout:
            break

    return {
        "status":"PUBLIC_IO_CANDIDATE_FOUND" if final else "NO_PUBLIC_IO_CANDIDATE",
        "program":final,
        "program_sha256":hashlib.sha256(final.encode()).hexdigest() if final else None,
        "seed":seed,"termination":reason,
        "max_nodes":max_nodes,"max_evals":max_evals,
        "beam_width":beam_width,"time_limit_seconds":time_limit_seconds,
        "counts":{"attempted_successors":attempts,"invalid_intermediates":invalid,
                  "repeated_existing_register":observed_duplicate,
                  "duplicate_register_states":state_duplicate,
                  "expanded_register_states":expanded,
                  "public_candidate_matches":candidate_matches,
                  "retained_states_by_depth":retained},
        "search_cpu_seconds":time.process_time()-first_cpu,
        "search_wall_seconds":time.perf_counter()-first_wall,
        "process_peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "source_leakage_controls":"public I/O only; source reference/evaluator consulted only after synthesis",
        "semantics":"source-locked ExeDec interpreter at every successor",
    }


def run(splits:list[str],indices:list[int],seeds:list[int],cache:Path,*,offline:bool,
        max_nodes:int,max_evals:int,beam_width:int,time_limit_seconds:float,
        probes:int)->dict:
    sources={}
    for split in splits:
        rows,blob=adm.source_rows(split,cache,offline=offline)
        if any(i<0 or i>=len(rows) for i in indices):
            raise adm.Rejected("task index outside source-locked cohort")
        sources[split]=(rows,blob)
    cpu0,wall0=time.process_time(),time.perf_counter()
    cases=[]
    for split in splits:
        rows,blob=sources[split]
        for index in indices:
            public=adm.participant_view(split,rows[index])
            public["source_blob"]=blob
            public_hash=hashlib.sha256(json.dumps(
                public,sort_keys=True,separators=(",",":")).encode()).hexdigest()
            for seed in seeds:
                search=synthesize(public,seed=seed,max_nodes=max_nodes,
                                  max_evals=max_evals,beam_width=beam_width,
                                  time_limit_seconds=time_limit_seconds)
                program=search.pop("program")
                eval_result=None
                eval_start=time.perf_counter()
                if program is not None:
                    eval_result=adm.verify(split,index,program,cache,offline=True,
                                           probes=probes)
                eval_time=time.perf_counter()-eval_start
                cases.append({
                    "task_id":public["task_id"],"split":split,"index":index,"seed":seed,
                    "source_git_blob_sha":blob,"public_projection_sha256":public_hash,
                    "reference_operations_evaluator_only":len(
                        rows[index]["test_problem"]["program"].split("|"))-len(public["inputs"]),
                    "search":search,"candidate_program":program,
                    "evaluator":eval_result,"evaluator_wall_seconds":eval_time,
                    "bounded_verified":eval_result is not None and
                        eval_result["status"]=="BOUNDED_EXECUTION_AGREEMENT_ONLY",
                })
    return {
        "schema":"gcl.owi-ds002.exedec-exact-register-search.v1",
        "status":"SEMANTICS_EXACT_OUTCOME_ONLY_REGISTER_SEARCH_EVALUATED",
        "source_revision":adm.manifest()["origin"]["commit"],
        "protocol":{"splits":splits,"indices":indices,"seeds":seeds,
                    "max_nodes":max_nodes,"max_evals":max_evals,
                    "beam_width":beam_width,"time_limit_seconds":time_limit_seconds,
                    "probes":probes,"search_target_program_access":False},
        "aggregate":{"task_seed_trials":len(cases),
                     "unique_task_identities":len(splits)*len(indices),
                     "public_example_candidates":sum(x["candidate_program"] is not None for x in cases),
                     "bounded_verified":sum(x["bounded_verified"] for x in cases),
                     "search_attempts":sum(x["search"]["counts"]["attempted_successors"]
                                           for x in cases),
                     "search_cpu_seconds":sum(x["search"]["search_cpu_seconds"] for x in cases),
                     "search_wall_seconds":sum(x["search"]["search_wall_seconds"] for x in cases),
                     "evaluator_wall_seconds":sum(x["evaluator_wall_seconds"] for x in cases),
                     "end_to_end_cpu_seconds":time.process_time()-cpu0,
                     "end_to_end_wall_seconds":time.perf_counter()-wall0,
                     "peak_rss_kib_process":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},
        "by_split":{split:{
            "trials":sum(x["split"]==split for x in cases),
            "bounded_verified":sum(x["split"]==split and x["bounded_verified"] for x in cases)}
            for split in splits},
        "records":cases,
        "limitations":[
            "A new native source-semantics-exact search comparator, not a mature independently authored external solver",
            "Public source contains target programs; search-function projection prevents direct leakage only",
            "Results are finite evaluator-probe agreement, not universal equivalence",
            "Five seeded search orders on each published task are correlated trials, not distinct tasks",
            "Search-budget and local CPU/wall accounting differs from historical C++ and is not equal total compute",
            "Beam novelty pruning is outcome-only heuristic and may discard valid solutions",
            "No real JVP, smooth differential subcategory or A/B/C/D reflective/causal gain is tested",
        ],
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--splits",default=",".join(DEFAULT_SPLITS))
    ap.add_argument("--indices",default=",".join(map(str,DEFAULT_INDICES)))
    ap.add_argument("--seeds",default=",".join(map(str,DEFAULT_SEEDS)))
    ap.add_argument("--max-nodes",type=int,default=4)
    ap.add_argument("--max-evals",type=int,default=15000)
    ap.add_argument("--beam-width",type=int,default=160)
    ap.add_argument("--time-limit-seconds",type=float,default=1.5)
    ap.add_argument("--probes",type=int,default=16)
    ap.add_argument("--cache-dir",default="build/owi_ds002/exedec_sources")
    ap.add_argument("--offline",action="store_true")
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    try:
        splits=a.splits.split(",")
        indices=[int(x) for x in a.indices.split(",")]
        seeds=[int(x) for x in a.seeds.split(",")]
        if (not splits or len(set(splits))!=len(splits) or any(s not in DEFAULT_SPLITS for s in splits)
            or not 1<=len(indices)<=50 or len(set(indices))!=len(indices) or any(x<0 for x in indices)
            or not 1<=len(seeds)<=10 or len(set(seeds))!=len(seeds)
            or any(x<1 or x>2**32-1 for x in seeds)):
            raise adm.Rejected("invalid cohort or search seeds")
        result=run(splits,indices,seeds,Path(a.cache_dir),offline=a.offline,
                   max_nodes=a.max_nodes,max_evals=a.max_evals,beam_width=a.beam_width,
                   time_limit_seconds=a.time_limit_seconds,probes=a.probes)
    except (adm.Rejected,ValueError,OSError) as exc:
        result={"status":"REJECTED_OR_INCONCLUSIVE","error":str(exc)}
    dest=Path(a.output)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="records"},
                     sort_keys=True,indent=2))
    return 0 if result["status"]=="SEMANTICS_EXACT_OUTCOME_ONLY_REGISTER_SEARCH_EVALUATED" else 2


if __name__=="__main__":
    raise SystemExit(main())
