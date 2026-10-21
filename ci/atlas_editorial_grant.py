#!/usr/bin/env python3
"""Check Atlas RESULT/1 against one authentic unexpired CONTROLLED Editorial grant."""
import json,re
from datetime import datetime,timezone
from typing import Any
PREFIX="GCL-EDITORIAL-DECISION/1\n"
START=re.compile(r'^EDITORIAL-START/1\nrepository: (grandchallenge/[A-Za-z0-9-]+)\nissue: ([1-9][0-9]{0,5})\nrun_id: ([0-9a-f]{32})\nsource_head: ([0-9a-f]{40})\s*$')
END=re.compile(r'^EDITORIAL-END/1\nrepository: (grandchallenge/[A-Za-z0-9-]+)\nissue: ([1-9][0-9]{0,5})\nrun_id: ([0-9a-f]{32})\s*$')
REPO="grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS"
CUTOVER=datetime(2026,10,21,0,0,tzinfo=timezone.utc)
def when(value):
    if not isinstance(value,str):raise ValueError("timestamp_missing")
    x=datetime.fromisoformat(value.replace("Z","+00:00"))
    if x.tzinfo is None:raise ValueError("timestamp_no_timezone")
    return x
def check(event:dict,comments:list[dict],run_id:str,reviewed_head:str)->str:
    result=event["comment"];received=when(result.get("created_at"))
    if received < CUTOVER:return "legacy_before_cutover"
    if not re.fullmatch(r"[0-9a-f]{32}",run_id or ""):return "missing_exact_granted_run_id"
    if not isinstance(comments,list):return "incomplete_grant_history"
    repo=(event["repository"] or {}).get("full_name")
    number=event["issue"].get("number")
    actor=(result.get("user") or {}).get("login")
    if repo!=REPO or not actor:return "wrong_actor_or_repo"
    requests={};granted={};closed=set();seen=set()
    try:
        for c in comments:
            n=c.get("id")
            if type(n)is not int or n in seen:raise ValueError("duplicate_history")
            seen.add(n);sender=(c.get("user") or {}).get("login")
            ctime=when(c.get("created_at"))
            if sender!="github-actions[bot]":
                m=START.fullmatch(c.get("body") or "")
                if m:requests[n]=(m.groups(),sender,ctime)
                else:
                    e=END.fullmatch(c.get("body") or "")
                    if e:requests[n]=(e.groups(),sender,ctime)
                continue
            text=c.get("body") or ""
            if not text.startswith(PREFIX):continue
            d=json.loads(text[len(PREFIX):])
            request=requests.get(d["request_id"])
            if not request or request[1]!=d.get("worker") or ctime<request[2]:raise ValueError("unbound_bot_response")
            fields=request[0]
            if d.get("repo")!=fields[0] or d.get("issue")!=int(fields[1]) or d.get("run")!=fields[2] or d.get("op") not in ("START","END"):raise ValueError("misbound_response")
            if d["op"]=="START":
                if d.get("source_head")!=fields[3]:raise ValueError("source_mismatch")
                if d.get("outcome")=="GRANTED":granted[(d["repo"],d["issue"],d["run"],d["worker"])]=(ctime,when(d["expires_at"]),d["source_head"])
            elif d.get("outcome")=="ENDED":
                closed.add((d["repo"],d["issue"],d["run"],d["worker"],ctime))
        key=(repo,number,run_id,actor);entry=granted.get(key)
        if entry is None:return "no_authenticated_grant"
        started,expires,head=entry
        if head!=reviewed_head:return "source_head_drift"
        if not(started<=received<expires):return "no_active_grant_at_return"
        if any(k[:4]==key and k[4]<=received for k in closed):return "grant_ended_before_result"
        return "granted"
    except (KeyError,TypeError,ValueError,IndexError):
        return "grant_history_invalid_fail_closed"
