#!/usr/bin/env python3
"""Bounded read-only ATLAS #405 evidence; issue returns are NOT chapter acceptance."""
import json, yaml, re, hashlib, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
R="grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS"
OUT=Path("governance/editorial/v0.1.1/CHAPTER_ACCEPTANCE_EVIDENCE_080.json")
HEAD_RE=re.compile(r"(?im)^\s*(?:input_head|reviewed_head)\s*:\s*([a-f0-9]{40})\b")
def gh(path,raw=False):
    args=["gh","api",path]
    if raw: args+=["-H","Accept: application/vnd.github.raw"]
    x=subprocess.run(args,check=True,capture_output=True,text=True,timeout=65)
    return x.stdout if raw else json.loads(x.stdout)
def check(d,canonical,wp,tree):
    rows=d["chapters"]; expected={c["id"]:c for c in canonical["chapters"]}
    if len(rows)!=80 or len(expected)!=80 or {r["chapter_id"] for r in rows}!=set(expected):raise ValueError("incomplete 80 canonical chapter rows")
    blobs={v["path"]:v["sha"] for v in tree["tree"] if v["type"]=="blob"}
    for row in rows:
        c=expected[row["chapter_id"]]
        if row["source_path"]!=c["manuscript_path"] or row["source_blob_sha1"]!=blobs.get(c["manuscript_path"]):raise ValueError("source blob mismatch")
        if row["state"]=="ACCEPTED":
            e=row.get("accepted_evidence")
            if not isinstance(e,dict) or not all(e.get(k) for k in ("head","producer_run","critic_run","pdf_sha256","html_sha256","critic_url")):raise ValueError("fabricated chapter acceptance")
            if e["head"]!=d["candidate_head"] or e["producer_run"]==e["critic_run"]:raise ValueError("stale/unseparated acceptance")
        elif row["state"]!="UNVERIFIED":raise ValueError("unknown state")
    assigned=[x for p in wp["work_packages"] for x in p["chapter_ids"]]
    if len(wp["work_packages"])!=20 or len(assigned)!=76 or len(set(assigned))!=76:
        raise ValueError("review-work assignment coverage drift")
    return True
def main():
    pr=gh(f"repos/{R}/pulls/320")
    head=pr["head"]["sha"]
    if pr["state"]!="open" or len(head)!=40:raise ValueError("workbench source identity drift")
    tree=gh(f"repos/{R}/git/trees/{head}?recursive=1")
    if tree.get("truncated"):raise ValueError("Git tree truncated")
    base=json.loads(Path("governance/CHAPTER_LEDGER.yaml").read_text())
    wp=yaml.safe_load(gh(f"repos/{R}/contents/governance/editorial/v0.1.0/CHAPTER_AGENT_QUEUE.yaml?ref={head}",True))
    work={cid:p for p in wp["work_packages"] for cid in p["chapter_ids"]}
    issues=gh(f"repos/{R}/issues?state=all&labels=gcl-job&per_page=100")
    issues=[i for i in issues if "pull_request" not in i]
    expected=set(range(321,346))|{359,362,363}
    if len(issues)!=28 or {i["number"] for i in issues}!=expected:raise ValueError("Atlas job inventory changed")
    with ThreadPoolExecutor(max_workers=6) as pool:
        comments=list(pool.map(lambda i:gh(f"repos/{R}/issues/{i['number']}/comments?per_page=100"),issues))
    bound={}; total=0
    for issue,cs in zip(issues,comments):
        labels={l["name"] for l in issue["labels"]}
        if issue["state"]!="closed" or not {"gcl-job","gcl-pickup:direct-editorial","gcl-state:returned"}<=labels or "gcl-state:available" in labels:raise ValueError("issue state drift #"+str(issue["number"]))
        if len(cs)!=issue["comments"] or len(cs)>=100:raise ValueError("partial comment inventory")
        matches=[c for c in cs if c.get("body","").startswith("RESULT/1\n")]
        if not matches:raise ValueError("missing real RESULT #"+str(issue["number"]))
        total+=len(matches); bound[issue["number"]]=[]
        for c in matches:
            h=HEAD_RE.search(c["body"]);actor=(c.get("user") or {}).get("login")
            if not actor:raise ValueError("missing Github actor")
            bound[issue["number"]].append({"id":c["id"],"url":c["html_url"],"actor":actor,
                "body_sha256":hashlib.sha256(c["body"].encode()).hexdigest(),
                "declared_head":h.group(1) if h else None})
    blobs={v["path"]:v["sha"] for v in tree["tree"] if v["type"]=="blob"}
    rows=[]
    for c in base["chapters"]:
        p=work.get(c["id"]);issue=p["issue_number"] if p else 318
        rows.append({"chapter_id":c["id"],"part_id":c["part_id"],"source_path":c["manuscript_path"],
            "source_blob_sha1":blobs.get(c["manuscript_path"]),"review_issue":issue,
            "assignment_id":p["assignment_id"] if p else "PART-I-EDITORIAL",
            "issue_bound_return_evidence":bound.get(issue,[]),"state":"UNVERIFIED",
            "accepted_evidence":None,"unresolved":"Exact-head substantive critic, findings disposition and rendered PDF/HTML readback"})
    d={"record_type":"ATLAS_CHAPTER_ACCEPTANCE_EVIDENCE/1","candidate_pr":320,"candidate_head":head,
       "protected_main_sha":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
       "immutable_release_unchanged":True,"chapters":rows,"accepted_count":0,
       "issue_inventory":{"total":28,"closed_returned":28,"authentic_RESULT_1_comments":total,
           "live_open":0,"synthetic_test_issue_excluded_from_chapter_evidence":359}}
    check(d,base,wp,tree)
    if len([r for r in rows if r["review_issue"]==318])!=4:raise ValueError("Part I mapping invalid")
    if gh(f"repos/{R}/pulls/320")["head"]["sha"]!=head:raise ValueError("concurrent candidate head changed")
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"chapters":len(rows),"accepted":0,"issue_returns":total,"issues_closed_returned":28,"candidate_head":head}))
if __name__=="__main__":
    try:main()
    except (ValueError,subprocess.CalledProcessError,OSError,KeyError) as e:
        print("BLOCKED:",str(e),file=sys.stderr);sys.exit(2)
