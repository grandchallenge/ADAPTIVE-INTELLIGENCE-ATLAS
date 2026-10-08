#!/usr/bin/env python3
"""Atlas corrected-edition: propagate exact TeX figure alt text into HTML.

Source of truth is the scoped [alt={...}] field in RC2 LaTeX, not a
duplicated caption or manually ordered figure list. Match embedded raster
bytes by digest to bind text to the right figure under reordering.
"""
import argparse
import base64
import hashlib
import html
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent.parent
TEX=ROOT/"manuscript/latex/atlas-v0.1.1-rc.2.tex"

def tex_figures(source):
    markers=list(re.finditer(r"\\includegraphics\[",source))
    out={}
    for m in markers:
        k=source.find("alt={",m.end())
        stop=source.find("]{",m.end())
        if k<0 or stop<0 or k>stop:
            raise ValueError("figure image missing alt text")
        at=k+len("alt={")
        depth=1
        pos=at
        while depth and pos<len(source):
            c=source[pos]
            if c=="{" and (pos==0 or source[pos-1]!="\\"):depth+=1
            elif c=="}" and (pos==0 or source[pos-1]!="\\"):depth-=1
            pos+=1
        if depth:raise ValueError("unterminated TeX alt")
        alt=source[at:pos-1].strip()
        path_start=source.find("]{",pos)
        if path_start<0 or path_start-pos>200:
            raise ValueError("missing figure filename")
        path_end=source.find("}",path_start+2)
        path=source[path_start+2:path_end]
        assert path.startswith("figures/"),path
        full=ROOT/path
        if not full.is_file():raise ValueError("missing figure asset "+str(full))
        dg=hashlib.sha256(full.read_bytes()).hexdigest()
        # TeX brace escapes here are native Pandoc source encodings,
        # converted to plain text for assistive technology.
        alt=alt.replace("{[}","[").replace("{]} ","] ").replace("{]}","]")
        alt=alt.replace("\\{","{").replace("\\}","}")
        if "\\" in alt:raise ValueError("unconverted TeX escape in alt "+alt)
        if len(alt)<65:raise ValueError("insufficient semantic alt for "+path)
        figid=re.search(r"ATLAS-FIG-[A-Z0-9]+-001",path)
        if not figid:raise ValueError("missing stable figure identity "+path)
        if dg in out:raise ValueError("duplicate raster digest")
        out[dg]=(figid.group(),alt,path)
    if len(out)!=18:raise ValueError("expected 18 figures; found "+str(len(out)))
    if len(set(x[0] for x in out.values()))!=18:raise ValueError("duplicate figure ID")
    return out

FIG=re.compile(r"(<figure>\s*<img\b)([^>]*?)(\s*/?>\s*<figcaption>)",re.S)
ALT=re.compile(r'\s+alt="[^"]*"')
SRC=re.compile(r'\bsrc="data:image/png;base64,([^"]+)"')

def rewrite_document(raw,figs,verify=False):
    seen=set()
    def apply(m):
        attrs=m.group(2)
        p=SRC.search(attrs)
        if not p:raise ValueError("figure missing embedded png")
        try:digest=hashlib.sha256(base64.b64decode(p.group(1),validate=True)).hexdigest()
        except Exception as e:raise ValueError("invalid embedded png") from e
        if digest not in figs:raise ValueError("unexpected figure raster "+digest)
        if digest in seen:raise ValueError("duplicated figure")
        seen.add(digest)
        figid,alt,_=figs[digest]
        escaped=html.escape(alt,quote=True)
        prior=ALT.search(attrs)
        if verify and (prior is None or prior.group().strip()!=f'alt="{escaped}"'):
            raise ValueError("mismatched semantic alt "+figid)
        if prior:
            attrs=attrs[:prior.start()]+attrs[prior.end():]
        attrs+=' alt="'+escaped+'"'
        return m.group(1)+attrs+m.group(3)
    result=FIG.sub(apply,raw)
    if seen!=set(figs):raise ValueError("missing figures "+str([figs[k][0] for k in set(figs)-seen]))
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--html",type=Path,help="fully embedded corrected-edition HTML")
    parser.add_argument("--write",action="store_true")
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    if args.write and args.verify:parser.error("--write and --verify are exclusive")
    figures=tex_figures(TEX.read_text())
    print("SOURCE_SEMANTIC_ALT_PASS",len(figures),"figures")
    if args.html is None:
        if args.write or args.verify:parser.error("--write/--verify require --html")
        return
    before=args.html.read_text()
    after=rewrite_document(before,figures,verify=args.verify)
    if args.write:args.html.write_text(after)
    print("HTML_SEMANTIC_ALT_PASS",len(figures),"figures",
          "mode",("write" if args.write else "verify" if args.verify else "diagnostic"),
          "byte_count",len(after))
if __name__=="__main__":main()
