#!/usr/bin/env python3
"""Historical Microsoft DeepCoder solver as source-locked I/O-only candidate proposer.

IMPORTANT: C++ operator semantics differ from ExeDec. A C++ 'Solved!' is NEVER
an accepted task: every extracted program is rechecked by the ExeDec verifier.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import resource
import subprocess
import tempfile
import time

import owi_ds002_exedec_admission as adm
from owi_ds002_exedec_enumerator import DEFAULT_SPLITS

UPSTREAM = "794057dc41aab0bea3818b75416da06b25aff12f"
BLOBS = {
    "enumerative-search/main.cc": "1010467567c6b0fe1e520c20beaefd83e559e6df",
    "enumerative-search/ops.cc": "703bd1154b8024543c917696e53316ec3efddc57",
    "enumerative-search/io_set.cc": "110716dc572cd3c321f128777d3b6238581f199b",
    "enumerative-search/successor.cc": "c60cc8dede0c0df071f1c2cf198f437e6a62b471",
    "enumerative-search/Makefile": "379d5f3d086917d679d93ad92953f2bb99cf08ed",
    "enumerative-search/data/example/prior.txt": "5cb0aa60e08d69226d00db2cddb4f1feda004ba0",
}
OPS = {
    "arr_min": ("Minimum", ""), "arr_max": ("Maximum", ""),
    "arr_head": ("Head", ""), "arr_last": ("Last", ""),
    "arr_sum": ("Sum", ""), "sort": ("Sort", ""), "reverse": ("Reverse", ""),
    "access": ("Access", ""), "take": ("Take", ""), "drop": ("Drop", ""),
}
for stem, lam in {"increment": "(+1)", "decrement": "(-1)", "mult2": "(*2)",
                  "div2": "(/2)", "negate": "(*(-1))", "sqr": "(**2)",
                  "mult3": "(*3)", "div3": "(/3)", "mult4": "(*4)",
                  "div4": "(/4)"}.items():
    OPS["map_" + stem] = ("Map", lam)
for stem, lam in {"pos": "(>0)", "neg": "(<0)", "even": "(%2==0)",
                  "odd": "(%2==1)"}.items():
    for op in ("Count", "Filter"):
        OPS[op.lower()+"_is_"+stem] = (op, lam)
for stem, lam in {"add": "(+)", "subtract": "(-)", "mult": "(*)",
                  "min": "(min)", "max": "(max)"}.items():
    OPS["scanl_"+stem] = ("Scanl1", lam)
    OPS["zipwith_"+stem] = ("ZipWith", lam)

LINE = re.compile(r"\s*%(\d+)\s+<-\s+([a-z_0-9]+)\s+%(\d+)(?:\s+%(\d+))?\s*\Z")


def provenance(root: Path) -> dict:
    try:
        revision = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True, timeout=8).stdout.strip()
    except subprocess.SubprocessError as exc:
        raise adm.Rejected("external source checkout unavailable") from exc
    if revision != UPSTREAM:
        raise adm.Rejected("external solver Git commit mismatch")
    for relpath, digest in BLOBS.items():
        path = root / relpath
        if not path.is_file() or adm.git_blob(path.read_bytes()) != digest:
            raise adm.Rejected("external solver source blob mismatch: "+relpath)
    binary = root/"enumerative-search"/"search"
    if not binary.is_file():
        raise adm.Rejected("external solver binary unavailable")
    return {"upstream": "microsoft/DeepCoder-Utils", "commit": UPSTREAM,
            "source_blob_count": len(BLOBS),
            "binary_sha256": hashlib.sha256(binary.read_bytes()).hexdigest()}


def _value(x):
    return str(x) if type(x) is int else " ".join(str(k) for k in x)


def write_fixture(view: dict, path: Path, seed: int, prior: str) -> None:
    if view.get("target_program_exposed") is not False:
        raise adm.Rejected("target-reference leakage")
    names, typ, n = adm.validate_examples(view)
    if n != 3:
        raise adm.Rejected("historical solver requires 3 I/O samples")
    path.mkdir()
    (path/"input_types.txt").write_text(" ".join(
        "Int" if typ[k] == "I" else "Array" for k in names)+"\n")
    (path/"input_values.txt").write_text("\n".join(
        " | ".join(_value(view["inputs"][k][j]) for k in names)
        for j in range(n))+"\n")
    kinds = {adm.kind(x) for x in view["outputs"]}
    if len(kinds) != 1:
        raise adm.Rejected("inconsistent output type")
    (path/"output_types.txt").write_text("Int\n" if "I" in kinds else "Array\n")
    (path/"output_values.txt").write_text(
        "\n".join(_value(v) for v in view["outputs"])+"\n")
    toks = [s.split()[1] for s in prior.splitlines() if s.strip()]
    if len(toks) < 30 or len(set(toks)) != len(toks):
        raise adm.Rejected("bad historical source prior")
    # Task-independent seed permutes function order, not task labels.
    weights = []
    for tok in toks:
        bits = hashlib.sha256((str(seed)+":"+tok).encode()).digest()
        val = .01+.98*int.from_bytes(bits[:8], "big")/2**64
        weights.append(f"{val:.12f} {tok}")
    (path/f"random_ordering_{seed}.txt").write_text("\n".join(weights)+"\n")
    (path/"prior.txt").write_text(prior)


def extract(stdout: str, names: list[str]) -> str | None:
    if not re.search(r"(?m)^Solved!\s*$", stdout):
        return None
    if "Solution:\n" not in stdout:
        raise adm.Rejected("external solver claimed success without candidate")
    lines = [name+" = INPUT" for name in names]
    for raw in stdout.split("Solution:\n", 1)[1].splitlines():
        if not raw.strip():
            continue
        match = LINE.fullmatch(raw)
        if match is None:
            raise adm.Rejected("unrecognized external program syntax")
        dest, opname, a1, a2 = match.groups()
        if opname not in OPS:
            raise adm.Rejected("external operation not translatable")
        op, lam = OPS[opname]
        arity = 2 if op in ("Access", "Take", "Drop", "ZipWith") else 1
        if int(dest) != len(lines) or (a2 is not None) != (arity == 2):
            raise adm.Rejected("external program register/arity mismatch")
        args = [int(a1)]+([int(a2)] if a2 is not None else [])
        if any(k >= int(dest) for k in args):
            raise adm.Rejected("external program uses unbound register")
        lines.append(" ".join(["x"+dest, "=", op] +
                              ([lam] if lam else [])+
                              ["x"+str(k) for k in args]))
    if len(lines) <= len(names):
        raise adm.Rejected("empty claimed solution")
    return " | ".join(lines)


def propose(view: dict, root: Path, seed: int, depth: int, timeout: float) -> dict:
    if not 1 <= seed <= 999 or not 1 <= depth <= 6 or not .1 <= timeout <= 20.:
        raise adm.Rejected("invalid external search budget")
    if set(view) - {"status","task_id","inputs","outputs",
                    "input_output_examples","target_program_exposed","source_blob"}:
        raise adm.Rejected("private data passed to external search")
    names, _, n = adm.validate_examples(view)
    search_dir = root/"enumerative-search"
    data_dir = search_dir/"data"
    prior=(data_dir/"example"/"prior.txt").read_text()
    with tempfile.TemporaryDirectory(prefix="gcl_owi_ds002_", dir=data_dir) as temp:
        case=Path(temp)/"sample"
        write_fixture(view, case, seed, prior)
        relative=case.relative_to(data_dir)
        cmd=[str(search_dir/"search"), str(relative), str(n),
             str(depth), "0", str(-seed), "-1"]
        def limits():
            resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
            resource.setrlimit(resource.RLIMIT_CPU, (int(timeout)+2, int(timeout)+3))
        start=time.perf_counter()
        try:
            proc=subprocess.run(cmd, cwd=search_dir, capture_output=True,
                                text=True, timeout=timeout, preexec_fn=limits)
            status=("SOLVED_BY_HISTORICAL_SEMANTICS" if "Solved!" in proc.stdout
                    else "NOT_SOLVED_BY_HISTORICAL_SEMANTICS"
                    if "Failed!" in proc.stdout else "EXTERNAL_EXIT_NONSTANDARD")
            if proc.returncode != 0:
                status="EXTERNAL_EXIT_NONZERO"
            candidate=extract(proc.stdout, names) if proc.returncode == 0 else None
            match=re.search(r"Nodes explored:\s*(\d+)",proc.stdout)
            explored=int(match.group(1)) if match else None
            rc=proc.returncode
        except subprocess.TimeoutExpired:
            status,candidate,explored,rc="EXTERNAL_TIMEOUT",None,None,None
        wall=time.perf_counter()-start
    return {"external_status":status,"candidate":candidate,"seed":seed,
            "external_nodes_explored":explored,"external_exit_code":rc,
            "external_worker_wall_seconds":wall,"wall_timeout_seconds":timeout}


def run(root:Path, cache:Path, splits:list[str], indices:list[int], seeds:list[int],
        depth:int, timeout:float, probes:int)->dict:
    identity=provenance(root)
    sources={s:adm.source_rows(s,cache,offline=False) for s in splits}
    started=time.perf_counter()
    rows=[]
    for split in splits:
        tasks,blob=sources[split]
        for idx in indices:
            if not 0<=idx<len(tasks):
                raise adm.Rejected("index outside pinned ExeDec source")
            public=adm.participant_view(split,tasks[idx])
            public["source_blob"]=blob
            for seed in seeds:
                trial=propose(public,root,seed,depth,timeout)
                candidate=trial.pop("candidate")
                evaluator=None
                if candidate is not None:
                    try:
                        # Eval gate knows original source; solver never does.
                        evaluator=adm.verify(split,idx,candidate,cache,
                                             offline=True,probes=probes)
                    except adm.Rejected as exc:
                        evaluator={"status":"REJECTED_TYPED_OR_GRAMMAR",
                                   "error":str(exc)}
                rows.append({"task_id":public["task_id"],"split":split,"index":idx,
                             "seed":seed,"source_git_blob_sha":blob,
                             "external":trial,"extracted_program":candidate,
                             "evaluator":evaluator,
                             "bounded_verified":evaluator is not None and
                                 evaluator["status"]=="BOUNDED_EXECUTION_AGREEMENT_ONLY"})
    return {"status":"LEGACY_EXTERNAL_CANDIDATE_PROPOSER_DIAGNOSTIC",
            "schema":"gcl.owi-ds002.historical-deepcoder-v1",
            "external_source":identity,
            "source_revision":adm.manifest()["origin"]["commit"],
            "protocol":{"splits":splits,"indices":indices,"seeds":seeds,
                        "max_nodes":depth,"timeout_seconds":timeout,
                        "evaluator_probes":probes,"solver_target_access":False},
            "summary":{"trials":len(rows),
                       "external_claimed_solved":sum(x["external"]["external_status"]==
                            "SOLVED_BY_HISTORICAL_SEMANTICS" for x in rows),
                       "bounded_verified":sum(x["bounded_verified"] for x in rows),
                       "external_timeouts":sum(x["external"]["external_status"]==
                            "EXTERNAL_TIMEOUT" for x in rows),
                       "script_wall_seconds":time.perf_counter()-started},
            "records":rows,
            "scientific_limits":[
                "2017 historical C++ semantics differ from 2024 ExeDec on negative division, empty lists, negative slicing, and out-of-range access",
                "All external claimed solutions require independent ExeDec verifier admission",
                "Historical solver is not a semantics-identical reference and may reject or accept different programs",
                "Bounded time and memory; no equal full-compute A/B/C/D or differential evidence",
            ]}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-dir",required=True)
    ap.add_argument("--splits",default="NONE,LENGTH_GENERALIZATION,COMPOSE_DIFFERENT_CONCEPTS")
    ap.add_argument("--indices",default="0")
    ap.add_argument("--seeds",default="1")
    ap.add_argument("--max-nodes",type=int,default=3)
    ap.add_argument("--timeout-seconds",type=float,default=2.)
    ap.add_argument("--probes",type=int,default=16)
    ap.add_argument("--cache-dir",default="build/owi_ds002/exedec_sources")
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    try:
        splits=a.splits.split(",")
        indices=[int(x) for x in a.indices.split(",")]
        seeds=[int(x) for x in a.seeds.split(",")]
        if (not splits or any(x not in DEFAULT_SPLITS for x in splits)
                or len(set(splits))!=len(splits) or not 1<=len(indices)<=50
                or len(set(indices))!=len(indices) or any(x<0 for x in indices)
                or not 1<=len(seeds)<=20 or len(set(seeds))!=len(seeds)
                or any(not 1<=x<=999 for x in seeds)):
            raise adm.Rejected("invalid public cohort or seed")
        result=run(Path(a.source_dir),Path(a.cache_dir),splits,indices,seeds,
                   a.max_nodes,a.timeout_seconds,a.probes)
    except (OSError,ValueError,subprocess.SubprocessError) as exc:
        result={"status":"REJECTED_OR_INCONCLUSIVE","error":str(exc)}
    out=Path(a.output)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="records"},
                     indent=2,sort_keys=True))
    return 0 if result["status"]=="LEGACY_EXTERNAL_CANDIDATE_PROPOSER_DIAGNOSTIC" else 2


if __name__=="__main__":
    raise SystemExit(main())
