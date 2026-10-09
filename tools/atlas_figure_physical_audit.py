#!/usr/bin/env python3
"""Source-linked Atlas figure placement and effective-DPI audit (not math certification)."""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    for field in ("pdf","report","data","samples"):ap.add_argument("--"+field,required=True,type=Path)
    a=ap.parse_args()
    import fitz,yaml
    from PIL import Image
    sys.path.insert(0,str(Path("tools").resolve()))
    from editorial_export_figure_alts import tex_figures
    root=Path.cwd()
    tex=(root/"manuscript/latex/atlas-v0.1.1-rc.2.tex").read_text(encoding="utf8")
    ordered=list(tex_figures(tex).values())
    register=yaml.safe_load((root/"governance/FIGURE_REGISTER.yaml").read_text())
    ids={f["id"]:f for f in register["figures"]}
    assert len(ordered)==len(ids)==18
    assert set(f[0] for f in ordered)==set(ids)
    doc=fitz.open(a.pdf)
    placed=[]
    for num,page in enumerate(doc,1):
        for img in page.get_images(full=True):
            xref,w,h=img[0],img[2],img[3]
            for rect in page.get_image_rects(xref):
                placed.append(dict(page=num,xref=xref,native_pdf_px=[w,h],
                                   width_pt=round(rect.width,2),height_pt=round(rect.height,2),
                                   x0=round(rect.x0,2),y0=round(rect.y0,2),
                                   outside_page=rect.x0<0 or rect.y0<0 or rect.x1>page.rect.width or rect.y1>page.rect.height,
                                   caption_word_present="Figure" in page.get_text()))
    placed.sort(key=lambda x:(x["page"],x["y0"],x["x0"]))
    if len(placed)!=18:
        raise RuntimeError(f"Expected 18 actual placed PDF rasters; found {len(placed)}")
    records=[]
    for (figid,alt,rel),pdf in zip(ordered,placed):
        path=root/rel
        with Image.open(path) as im:width,height=im.size
        reg=ids[figid]
        src=reg["generator"]["source"]
        manifest=reg["generator"]["manifest"]
        if not (root/src).exists() or not (root/manifest).exists():
            raise RuntimeError("Missing figure source/manifest for "+figid)
        same_dims=(width,height)==tuple(pdf["native_pdf_px"])
        dx=width*72/pdf["width_pt"]
        dy=height*72/pdf["height_pt"]
        records.append(dict(id=figid,chapter_id=reg["chapter_id"],
            representation_class=reg["representation_class"],
            source=src,manifest=manifest,raster=rel,
            native_px=[width,height],pdf_native_pixel_identity=same_dims,
            page=pdf["page"],rectangle_pt={k:pdf[k] for k in ("x0","y0","width_pt","height_pt")},
            dpi_x=round(dx,1),dpi_y=round(dy,1),min_effective_dpi=round(min(dx,dy),1),
            physical_width_in=round(pdf["width_pt"]/72,2),
            physical_height_in=round(pdf["height_pt"]/72,2),
            outside_pdf_box=pdf["outside_page"],
            caption_word_detected=pdf["caption_word_present"],
            alt_chars=len(alt),
            flag="CHECK_EFFECTIVE_DPI" if min(dx,dy)<200 else "NO_DPI_THRESHOLD_FLAG"))
    assert all(x["pdf_native_pixel_identity"] for x in records),"source to PDF pixel-dimension order mismatch"
    chosen=sorted(set(x["page"] for x in records))
    a.samples.mkdir(parents=True,exist_ok=True)
    for page in chosen:
        doc[page-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(str(a.samples/("figure-page-%04d.png"%page)))
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    state=dict(source_head=__import__("subprocess").check_output(["git","rev-parse","HEAD"],text=True).strip(),
        pdf_sha256=sha(a.pdf),tex_sha256=sha(root/"manuscript/latex/atlas-v0.1.1-rc.2.tex"),
        physical_page_count=len(doc),figure_count=len(records),
        source_assets_and_witness_manifests_exist=True,source_asset_pixel_dimensions_match_pdf=True,
        distinct_printed_figure_pages=len(chosen),
        outside_page_count=sum(r["outside_pdf_box"] for r in records),
        sub_200_dpi_count=sum(r["min_effective_dpi"]<200 for r in records),
        min_dpi=min(r["min_effective_dpi"] for r in records),
        by_figure=records,
        limitations=["TeX/figure ordering is assumed to preserve raster placement; per-figure native dimensions are cross-checked but image-pixel algebra is not re-proved.",
                     "A 200 DPI threshold is an editorial review trigger, not a formal mathematical or publisher quality standard.",
                     "Raster samples require independent visual reading; HTML alt checks do not establish PDF/UA tagging or screen-reader reading order.",
                     "Source-manifest existence does not mathematically certify all plotted values."])
    a.data.parent.mkdir(parents=True,exist_ok=True)
    a.data.write_text(json.dumps(state,indent=2)+"\n")
    table="| Figure ID | PDF page | Physical width (in) | Min effective DPI | Source ↔ PDF pixels | Flag |\n|---|---:|---:|---:|---|---|\n"
    for r in records:
        table+="| {} | {} | {:.2f} | {:.1f} | {} | {} |\n".format(r["id"],r["page"],r["physical_width_in"],r["min_effective_dpi"],"MATCH" if r["pdf_native_pixel_identity"] else "MISMATCH",r["flag"])
    report=("# Atlas figure physical-scale and image-source audit\n\n"
        "Disposition: MEASURED PRINT GEOMETRY ONLY — mathematical-fidelity and assistive technology critical review separately required.\n\n"
        "Exact source head: "+state["source_head"]+"\n\nPDF SHA256: "+state["pdf_sha256"]+"\n\n"
        "PDF pages: "+str(len(doc))+". Registered and placed figures: "+str(len(records))+". "
        "Distinct figure-bearing PDF pages: "+str(len(chosen))+".\n\n"
        "Figure images outside PDF page box: "+str(state["outside_page_count"])+". "
        "Effective resolution below a 200 DPI review threshold: "+str(state["sub_200_dpi_count"])+". "
        "Minimum measured DPI: "+str(state["min_dpi"])+".\n\n"
        "## Exact PDF measurements and registered source identities\n\n"+table+"\n"
        "All 18 exact figures have their own register entries, original source files, manifests and matching raster pixel dimensions in the PDF at the tested source head. "
        "The source/figure correspondence is checked by physical order and pixel size and should not be mistaken for an independent mathematical plot-proof.\n\n"
        "## Editorial boundaries\n\n"
        "The 18 actual printed PDF pages have been retained as raster samples for a separate figure critical-role reading. "
        "Physical DPI and page-bounds checks do not establish legible mathematical text, correct symbols, complete figure captions, alternate-text semantics in PDF, accessible reading order, or validity of Wolfram computation. "
        "Any negative case must be a concrete follow-on correction with fresh exact-head replay; no publication/80-chapter signoff is granted.\n")
    a.report.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text(report)
    print("ATLAS_FIGURE_PHYSICAL_QA="+json.dumps({k:state[k] for k in ("source_head","pdf_sha256","physical_page_count","figure_count","outside_page_count","sub_200_dpi_count","min_dpi","distinct_printed_figure_pages")}))
if __name__=="__main__":main()
