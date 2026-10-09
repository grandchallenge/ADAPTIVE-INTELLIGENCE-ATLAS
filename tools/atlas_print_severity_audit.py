#!/usr/bin/env python3
"""Source-aware TeX overfull warning inventory; non-certifying diagnostic.

Map each warning to the exact current TeX line, its chapter ID/path from the
frozen ledger, and nearest source Markdown section. Compare counts against a
pinned preceding TeX/log; do not infer actual visual clipping from warnings.
"""
from __future__ import annotations
import argparse, bisect, collections, json, re
from pathlib import Path

WARN=re.compile(r"Overfull \\hbox \(([\d.]+)pt too wide\)([^\n]*)")
CHAPTER=re.compile(r"\\chapter(?:\[[^\]]*\])?\{")
SECTION=re.compile(r"\\(?:sub)*section(?:\[[^\]]*\])?\{")
def parse(tex_path:Path,log_path:Path,ledger_path:Path):
    lines=tex_path.read_text(encoding="utf8").splitlines()
    chapters=json.loads(ledger_path.read_text(encoding="utf8"))["chapters"]
    chap_idx=[i+1 for i,s in enumerate(lines) if CHAPTER.search(s)]
    if len(chap_idx)!=len(chapters):
        raise ValueError(f"expected {len(chapters)} TeX chapters, found {len(chap_idx)}")
    sec_idx=[i+1 for i,s in enumerate(lines) if SECTION.search(s)]
    events=[]
    for m in WARN.finditer(log_path.read_text(errors="replace")):
        width=float(m.group(1))
        lm=re.search(r"(?:lines (\d+)(?:--\d+)?|line (\d+))",m.group(2))
        line=int(lm.group(1) or lm.group(2)) if lm else 0
        chapter_position=bisect.bisect_right(chap_idx,line)-1 if line else -1
        if chapter_position<0: cid="UNLOCATED" if not line else "FRONT_MATTER";source_path="";section="no source line" if not line else "front matter";source_line=None
        else:
            ch=chapters[chapter_position]
            cid=ch["id"];source_path=ch["manuscript_path"]
            lower=chap_idx[chapter_position]
            si=bisect.bisect_right(sec_idx,line)-1
            if si>=0 and sec_idx[si]>=lower:
                section_tex=lines[sec_idx[si]-1]
                section=re.sub(r".*?\\(?:sub)*section(?:\[[^\]]*\])?\{","",section_tex).split("}",1)[0]
            else:section="chapter introduction"
            source_line=None
            sp=Path(source_path)
            if sp.exists():
                md=sp.read_text(encoding="utf8").splitlines()
                text=section.strip().lower().replace(r"\_","_")
                hits=[i+1 for i,s in enumerate(md) if s.lstrip("# ").strip().lower()==text]
                if hits:source_line=hits[0]
        excerpt=" ".join(s.strip() for s in lines[max(0,line-3):min(len(lines),line+2)]) if line else m.group(2)
        events.append(dict(width_pt=width,tex_line=line,chapter_id=cid,
                           source_path=source_path,section=section,
                           source_heading_line=source_line,tex_excerpt=excerpt[:380]))
    return events

def main():
    ap=argparse.ArgumentParser()
    for x in ("current_tex","current_log","baseline_tex","baseline_log","ledger"):ap.add_argument("--"+x.replace("_","-"),required=True,type=Path)
    ap.add_argument("--top",type=int,default=30)
    a=ap.parse_args()
    current=parse(a.current_tex,a.current_log,a.ledger)
    prior=parse(a.baseline_tex,a.baseline_log,a.ledger)
    cc=collections.Counter(x["chapter_id"] for x in current)
    pc=collections.Counter(x["chapter_id"] for x in prior)
    # A changed TeX line number is not a new mathematical warning. Compare
    # stable measured width and nearby TeX excerpt, not raw line locations.
    def fingerprint(e):
        return (round(e["width_pt"],5),e["tex_excerpt"])
    old=collections.Counter(fingerprint(e) for e in prior)
    new=collections.Counter(fingerprint(e) for e in current)
    added=new-old;removed=old-new
    def examples(counter,rows):
        return [dict(count=n,width_pt=key[0],chapter_id=e["chapter_id"],
                     source_path=e["source_path"],tex_line=e["tex_line"],
                     tex_excerpt=key[1][:180])
                for key,n in sorted(counter.items(),key=lambda x:(-x[0][0],x[0][1]))[:40]
                for e in rows if fingerprint(e)==key][:40]
    count_delta=[(id,cc[id]-pc[id],pc[id],cc[id]) for id in set(cc)|set(pc) if cc[id]!=pc[id]]
    count_delta.sort(key=lambda row:(-abs(row[1]),row[0]))
    result=dict(baseline_count=len(prior),current_count=len(current),
                delta=len(current)-len(prior),
                current_top=sorted(current,key=lambda x:x["width_pt"],reverse=True)[:a.top],
                chapter_deltas=count_delta,
                current_chapter_counts=cc.most_common(25),
                baseline_max=max((x["width_pt"] for x in prior),default=0),
                current_max=max((x["width_pt"] for x in current),default=0),
                unparsed_current_count=a.current_log.read_text(errors="replace").count("Overfull \\hbox")-len(current),
                unparsed_baseline_count=a.baseline_log.read_text(errors="replace").count("Overfull \\hbox")-len(prior),
                unlocated_current=sum(1 for x in current if x["chapter_id"]=="UNLOCATED"),
                unlocated_baseline=sum(1 for x in prior if x["chapter_id"]=="UNLOCATED"),
                added_warning_count=sum(added.values()),removed_warning_count=sum(removed.values()),
                added_warning_signatures=examples(added,current)[:25],
                removed_warning_signatures=examples(removed,prior)[:15])
    print("ATLAS_PRINT_SEVERITY_AUDIT_JSON="+json.dumps(result,separators=(",",":"),ensure_ascii=True))
    if result["unparsed_current_count"] or result["unparsed_baseline_count"]:raise SystemExit("WARNING: unparsed overfull patterns")
if __name__=="__main__":main()
