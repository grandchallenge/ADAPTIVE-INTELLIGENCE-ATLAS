#!/usr/bin/env python3
"""Whole-corpus editorial triage. Heuristics do not certify any chapter."""
import collections, hashlib, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LEDGER=json.loads((ROOT/"governance/CHAPTER_LEDGER.yaml").read_text(encoding="utf-8"))
BIB=(ROOT/"sources/bibliography.bib").read_text(encoding="utf-8")
BIBKEYS=set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,",BIB))
PROCESS=re.compile(r"\b(?:tranche|work package|source lock|source-locked|repository|pull request|CI|GitHub|handoff|bootstrap|protected main|ledger|reviewer|audited|audit)\b",re.I)
PLACEHOLDER=re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER|INSERT HERE)\b",re.I)
IMAGE=re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
ROWS=[]; ISSUES=[]; REPEATS=collections.defaultdict(set)
for i,c in enumerate(LEDGER["chapters"],1):
    path=ROOT/c["manuscript_path"]
    t=path.read_text(encoding="utf-8")
    words=re.findall(r"\b[\w]+(?:[-'][\w]+)*\b",t)
    h2=re.findall(r"(?m)^## (.+)",t)
    h3=re.findall(r"(?m)^### (.+)",t)
    prose_only=re.sub(r"(?s)\\\[.*?\\\]","\n\n",t)
    prose_only=re.sub(r"(?s)\$\$.*?\$\$","\n\n",prose_only)
    paragraphs=[]
    for block in re.split(r"\n\s*\n",prose_only):
        b=block.strip()
        if not b or b.startswith(("<!--","#","-","*",">","|",r"\[",r"\(","!","**Epistemic","**Spec","**Derivation","**Source","**Primary","**Computational")):
            continue
        n=len(re.findall(r"\b\w+\b",b))
        if n<3:continue
        paragraphs.append((n,b))
        if n>=35: REPEATS[re.sub(r"\s+"," ",b).lower()].add(c["id"])
    citation_groups=re.findall(r"\[(@[^\]]+)\]",t)
    citations=[]
    for group in citation_groups:
        citations+=re.findall(r"@([\w:-]+)",group)
    missing=sorted(set(citations)-BIBKEYS)
    if missing: ISSUES.append([c["id"],"UNRESOLVED_CITATION",missing])
    figures=IMAGE.findall(t)
    figure_errors=[]
    for alt,target in figures:
        if not alt.strip():figure_errors.append("empty_alt:"+target)
        if not (path.parent/target).is_file():
            normalized=ROOT/"figures/masters"/Path(target).name
            if normalized.is_file():figure_errors.append("source-relative path needs release normalization:"+target)
            else:figure_errors.append("unresolvable figure:"+target)
    if figure_errors:ISSUES.append([c["id"],"FIGURE",figure_errors])
    placeholders=PLACEHOLDER.findall(t)
    if placeholders:ISSUES.append([c["id"],"PLACEHOLDER_POSSIBLE",len(placeholders)])
    row=dict(ordinal=i,id=c["id"],part=c["part_id"],path=c["manuscript_path"],words=len(words),h2=len(h2),h3=len(h3),short_prose=sum(n<=15 for n,b in paragraphs),prose_paragraphs=len(paragraphs),short_prose_pct=round(100*sum(n<=15 for n,b in paragraphs)/max(1,len(paragraphs)),1),process_hits=len(PROCESS.findall(t)),citation_count=len(citations),missing_citations=missing,figure_count=len(figures),figure_errors=figure_errors,placeholder_count=len(placeholders),manual_review="NOT_REVIEWED")
    ROWS.append(row)
REPEATED=[{"chapters":sorted(ch),"excerpt":p[:160]} for p,ch in REPEATS.items() if len(ch)>1]
REPEATED.sort(key=lambda r:(-len(r["chapters"]),r["excerpt"]))
out=ROOT/"governance/editorial/v0.1.0"
out.mkdir(parents=True,exist_ok=True)
report=dict(schema_version="1.0.0",exact_tag="atlas-v0.1.0",exact_release_commit="1d4c2532533ff98afb998f86e0443d3fa1d8682e",coverage="AUTOMATED_TRIAGE_ONLY",chapters=ROWS,issues=ISSUES,repeated_paragraphs=REPEATED[:80])
(out/"STATIC_TRIAGE.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
lines=["# Atlas v0.1.0 editorial static triage","", "Source: exact released v0.1.0. This report is a mechanical screen, NOT substantive editorial approval.","", "## Summary",""]
lines += ["- Source chapters scanned: "+str(len(ROWS)),"- Approximate words: "+str(sum(r["words"] for r in ROWS)),"- H2/H3 headers: "+str(sum(r["h2"]+r["h3"] for r in ROWS)),"- Short prose blocks (15 words or fewer): "+str(sum(r["short_prose"] for r in ROWS)),"- Process-token matches: "+str(sum(r["process_hits"] for r in ROWS)),"- Unresolved citation keys: "+str(sum(len(r["missing_citations"]) for r in ROWS)),"- Figure references: "+str(sum(r["figure_count"] for r in ROWS)),"- Mechanical issue records: "+str(len(ISSUES)),"- Repeated long paragraphs across chapters: "+str(len(REPEATED)),"", "A high score is a candidate for editorial examination, not automatically a defect.","","## Chapter coverage: 80 source files scanned, zero chapter-level editorial signoffs","", "| # | ID | Words | Sections | Short prose % | Process terms | Citations | Figures | Manual review |", "|---:|---|---:|---:|---:|---:|---:|---:|---|"]
for r in ROWS:
    lines.append(f'| {r["ordinal"]} | {r["id"]} | {r["words"]} | {r["h2"]+r["h3"]} | {r["short_prose_pct"]}% | {r["process_hits"]} | {r["citation_count"]} | {r["figure_count"]} | NOT REVIEWED |')
lines+=["","## Highest section density",""]
for r in sorted(ROWS,key=lambda v:(v["h2"]+v["h3"])/max(100,v["words"]),reverse=True)[:15]:
    lines.append(f'- {r["id"]}: {r["h2"]+r["h3"]} headings in {r["words"]} words')
lines+=["","## Process-oriented vocabulary candidates",""]
for r in sorted(ROWS,key=lambda v:v["process_hits"],reverse=True)[:15]:
    lines.append(f'- {r["id"]}: {r["process_hits"]} matches')
lines+=["","## Mechanical anomalies",""]
lines += ([str(i) for i in ISSUES] if ISSUES else ["No anomalies detected by these limited checks."])
lines+=["","## Editorial boundary","", "All 80 chapters still require a new publication-level editorial read. The scan records coverage but cannot judge claim correctness, pedagogy, figure accuracy, copy-edit quality, or the honesty of citations.",""]
(out/"STATIC_TRIAGE.md").write_text("\n".join(lines),encoding="utf-8")
print("chapters",len(ROWS),"words",sum(r["words"] for r in ROWS),"headings",sum(r["h2"]+r["h3"] for r in ROWS))
print("short_prose",sum(r["short_prose"] for r in ROWS),"process_matches",sum(r["process_hits"] for r in ROWS))
print("citations_unresolved",sum(len(r["missing_citations"]) for r in ROWS),"figure_refs",sum(r["figure_count"] for r in ROWS),"anomalies",len(ISSUES))
print("highest_density",[(r["id"],r["h2"]+r["h3"],r["words"]) for r in sorted(ROWS,key=lambda v:(v["h2"]+v["h3"])/max(100,v["words"]),reverse=True)[:8]])
print("highest_process",[(r["id"],r["process_hits"]) for r in sorted(ROWS,key=lambda v:v["process_hits"],reverse=True)[:8]])
print("issues",ISSUES[:20])
