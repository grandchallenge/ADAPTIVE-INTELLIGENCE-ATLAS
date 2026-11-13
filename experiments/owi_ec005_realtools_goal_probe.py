#!/usr/bin/env python3
"""Read only actual policy-visible tool replies from one pinned real task.

External class executes ONLY in existing restricted no-network Docker child.
Checker, hidden state, gold actions, RSD skills never provided. Prints only
selected tool observations; this is discovery, not a measured policy gain.
"""
import argparse
import json
from pathlib import Path
from owi_ec005_realtools_randomized import call_child, IMAGE

PROBES = [
    ("get_location_by_name", {"name": "Old Market"}),
    ("get_disease_by_name", {"disease_name": "Tarvio Gastroenteritis"}),
    ("list_reporters_by_type", {"reporter_type": "citizen"}),
    ("list_reporters_by_type", {"reporter_type": "healthcare_professional"}),
    ("list_reports_by_disease", {"disease_name": "Tarvio Gastroenteritis"}),
]
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--environment",required=True)
    ap.add_argument("--public",required=True)
    args=ap.parse_args()
    public=json.loads(Path(args.public).read_text())
    allowed={t["name"] for t in public["tools"]}
    if not all(name in allowed for name,_ in PROBES):
        raise ValueError("requested undeclared public tool")
    commands=[{"action":"call","tool":name,"arguments":parameters}
              for name,parameters in PROBES]+[{"action":"finish"}]
    data="".join(json.dumps(x)+"\n" for x in commands)
    rows,sec=call_child(IMAGE,"experiments/owi_ec005_realtools_episode_worker.py",
                        args.environment,input_text=data)
    if len(rows)!=len(PROBES)+2 or rows[0].get("kind")!="ready":
        raise RuntimeError("IPC mismatch")
    result=[]
    for spec,observed in zip(PROBES,rows[1:-1]):
        if observed.get("kind")!="observation":
            raise RuntimeError("unrecognized tool reply")
        result.append({"tool":spec[0],"args":spec[1],
                       "ok":observed["ok"],
                       "content":observed["content"][:2800]})
    print("PUBLIC_TOOL_OBSERVATIONS",json.dumps(result,sort_keys=True,ensure_ascii=False))
    print("PROBE_ONLY",json.dumps({"declared_tools":len(public["tools"]),
                                   "executed_tool_calls":len(PROBES),
                                   "private_verifier_invoked":False,
                                   "wall_seconds":round(sec,5)}))
if __name__=="__main__":
    main()
