#!/usr/bin/env python3
"""Validate and optionally write the chapter-review queue for Parts II–XIV."""
from pathlib import Path
import collections,sys,yaml
R=Path(__file__).resolve().parent.parent
P=R/"governance/editorial/v0.1.0/CHAPTER_AGENT_QUEUE.yaml"
release="1d4c2532533ff98afb998f86e0443d3fa1d8682e"
def create():
    ledger=yaml.safe_load((R/"governance/CHAPTER_LEDGER.yaml").read_text())["chapters"]
    parts=collections.OrderedDict()
    for ch in ledger:parts.setdefault(ch["part_id"],[]).append(ch)
    wps=[]
    number=326
    for part_num,(part,rows) in enumerate(parts.items(),start=1):
        if part_num==1:continue
        pieces=(len(rows)+4)//5
        base,extra=divmod(len(rows),pieces)
        start=0
        for j in range(pieces):
            end=start+base+(1 if j<extra else 0)
            block=rows[start:end]
            name=f"{part_num:02d}"+(f"-{chr(65+j)}" if pieces>1 else "")
            wps.append({
                "assignment_id":f"ATLAS-EDITORIAL-P{name}",
                "issue_number":number,
                "issue_url":f"https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/{number}",
                "part":part,
                "status":"PUBLISHED_UNCLAIMED",
                "chapter_ids":[x["id"] for x in block],
                "return_protocol":"RESULT/1",
                "authenticated_independent_agent_required_for_final_acceptance":True
            })
            number+=1
            start=end
    assert len(wps)==20,(len(wps),number)
    assert number==346
    return {"schema_version":"1.0.0",
            "campaign":"EDITORIAL-REVIEW-001",
            "parent_issue":314,
            "immutable_public_commit":release,
            "corrected_candidate_pr":320,
            "work_packages_published":len(wps),
            "review_scope_chapters":76,
            "part_i_issue":318,
            "publication_authorized":False,
            "note":"GitHub issue availability is NOT an authenticated worker claim, result, review signoff or certification. Agents must pin the live exact candidate head on claim.",
            "work_packages":wps}
def check(x):
    chapters=yaml.safe_load((R/"governance/CHAPTER_LEDGER.yaml").read_text())["chapters"]
    expected={c["id"] for c in chapters if c["part_id"]!="ATLAS-PART-ORIENTATION"}
    actual=[id for wp in x["work_packages"] for id in wp["chapter_ids"]]
    assert len(actual)==76 and set(actual)==expected and len(actual)==len(set(actual))
    assert len(x["work_packages"])==20
    assert [x["issue_number"] for x in x["work_packages"]]==list(range(326,346))
    assert all(x["status"] in {"PUBLISHED_UNCLAIMED", "CLAIMED", "IN_REVIEW", "RETURNED", "ADJUDICATED"} for x in x["work_packages"])
    assert x["immutable_public_commit"]==release and not x["publication_authorized"]
    print("PASS: 76/76 downstream chapters, 20 WPs, #326–#345, no unearned worker claims")
if __name__=="__main__":
    if "--write" in sys.argv:
        o=create()
        P.write_text(yaml.safe_dump(o,sort_keys=False,allow_unicode=True),encoding="utf-8")
    check(yaml.safe_load(P.read_text()))
