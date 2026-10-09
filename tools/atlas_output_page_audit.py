#!/usr/bin/env python3
"""Bounded, noncertifying correlation of TeX output-active warnings with PDF geometry."""
from __future__ import annotations
import argparse,bisect,collections,hashlib,json,re,subprocess
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    for name in ("pdf","log","json","markdown","preview_dir"):
        p.add_argument("--"+name.replace("_","-"),type=Path,required=True)
    a=p.parse_args()
    import fitz
    log=a.log.read_text(errors="replace")
    shipouts=[(m.start(),int(m.group(1))) for m in re.finditer(r"\[(\d+)(?=\]|[ <])",log)]
    locations=[x[0] for x in shipouts]
    doc=fitz.open(a.pdf)
    warnings=[]
    pat=r"Overfull \\hbox \(([\d.]+)pt too wide\) has occurred while \\output is active"
    for m in re.finditer(pat,log):
        i=bisect.bisect_left(locations,m.start())
        prev=shipouts[i-1][1] if i else None
        following=shipouts[i][1] if i<len(shipouts) else None
        candidate=list(dict.fromkeys(x for x in [prev,following] if x and 1<=x<=len(doc)))
        warnings.append(dict(width_pt=float(m.group(1)),previous_shipout=prev,
                             following_shipout=following,candidate_pages=candidate,
                             attribution="UNRESOLVED_OUTPUT_ROUTINE"))
    outside=collections.Counter()
    edge=collections.Counter()
    examples=[]
    image_pages=set()
    for n,page in enumerate(doc,1):
        w,h=page.rect.width,page.rect.height
        for b in page.get_text("dict").get("blocks",[]):
            if b.get("type")==1:
                image_pages.add(n)
                continue
            for line in b.get("lines",[]):
                for sp in line.get("spans",[]):
                    x0,y0,x1,y1=sp["bbox"]
                    if not sp.get("text","").strip():continue
                    if x0<-.5 or y0<-.5 or x1>w+.5 or y1>h+.5:
                        outside[n]+=1
                        if len(examples)<50:examples.append(dict(page=n,bbox=[round(v,2) for v in (x0,y0,x1,y1)],text=sp["text"][:110]))
                    if x0<18 or x1>w-18:edge[n]+=1
    top=sorted(warnings,key=lambda v:v["width_pt"],reverse=True)
    candidate_pages=list(dict.fromkeys(p for row in top[:15] for p in row["candidate_pages"]))
    a.preview_dir.mkdir(parents=True,exist_ok=True)
    for n in candidate_pages[:8]:
        doc[n-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(str(a.preview_dir/("page-%04d.png"%n)))
    source=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    data=dict(source_head=source,pdf_sha256=sha(a.pdf),log_sha256=sha(a.log),
              pages=len(doc),output_active_count=len(warnings),shipout_tokens=len(shipouts),
              max_width_pt=max((r["width_pt"] for r in warnings),default=0),
              all_output_active_warnings=warnings,outside_page_span_count=sum(outside.values()),
              outside_page_examples=examples,outside_page_top=outside.most_common(40),
              near_18pt_edge_count=sum(edge.values()),near_edge_top=edge.most_common(40),
              pages_with_extracted_images=len(image_pages),sample_raster_pages=candidate_pages[:8],
              attribution_limitation="shipout neighborhoods are candidates, not exact source-line or affected-page proof",
              geometry_limitation="extracted text bounds cannot certify graphical legibility, clipping or accessible reading order")
    a.json.parent.mkdir(parents=True,exist_ok=True)
    a.json.write_text(json.dumps(data,indent=2)+"\n")
    table="| Rank | Excess width pt | Before shipout | After shipout | Candidate pages |\n|---:|---:|---:|---:|---|\n"
    for i,r in enumerate(top[:25],1):
        table+="| {} | {:.5f} | {} | {} | {} |\n".format(i,r["width_pt"],r["previous_shipout"] or "unknown",r["following_shipout"] or "unknown",",".join(map(str,r["candidate_pages"])) or "unresolved")
    report=("# Atlas source-less output-active PDF warning audit\n\n"
      "Status: DIAGNOSTIC ONLY — no print or chapter acceptance.\n\n"
      "Exact head: "+source+"\n\nPDF SHA256: "+sha(a.pdf)+"\n\nLog SHA256: "+sha(a.log)+"\n\n"
      "PDF pages: "+str(len(doc))+". TeX output-active warnings: "+str(len(warnings))+". "
      "Shipout tokens: "+str(len(shipouts))+". Worst width: "+str(data["max_width_pt"])+"pt.\n\n"
      "## Warning candidate-page neighborhoods\n\n"+table+"\n"
      "The before/after shipout pair is not a proven individual page or TeX source line. This source-less attribution remains uncertain.\n\n"
      "## Independent PDF geometry\n\n"
      "Text spans outside the PDF page box: "+str(sum(outside.values()))+" (pages: "+str(len(outside))+"). "
      "Spans within 18pt of a physical edge: "+str(sum(edge.values()))+" (not necessarily clipped). "
      "Pages with extracted image blocks: "+str(len(image_pages))+".\n\n"
      "Eight or fewer candidate pages were rasterized as samples for a human/critical agent reader; this does not establish all-page visual quality.\n\n"
      "The complete  warning inventory and span examples are in the companion JSON. "
      "Remaining: inspect actual renders and caption/figure layout, diagnose print margins, mathematical fidelity, reading order and chapter-level quality. "
      "No inference of complete acceptance or public publication is warranted.\n")
    a.markdown.parent.mkdir(parents=True,exist_ok=True)
    a.markdown.write_text(report)
    print("ATLAS_OUTPUT_PAGE_QA="+json.dumps({k:data[k] for k in ("source_head","pdf_sha256","pages","output_active_count","shipout_tokens","max_width_pt","outside_page_span_count","near_18pt_edge_count","sample_raster_pages")}))
    if not warnings:raise SystemExit("Expected unresolved warning population; recheck input")
if __name__=="__main__":main()
