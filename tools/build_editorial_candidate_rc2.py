#!/usr/bin/env python3
"""Reproducibly recompose non-public Atlas editorial candidate v0.1.1-rc.2.

The first four edited orientation chapters are explicitly overlaid from
immutable RC1 workbench TeX. The other 76 chapters come directly from the
current Chapter Ledger Markdown assembly through pinned Pandoc conversion.
Public v0.1.0 and its release manifest are never modified.
"""
from pathlib import Path
import argparse, hashlib, re, subprocess, sys

ROOT=Path(__file__).resolve().parent.parent
RC1=ROOT/"manuscript/latex/atlas-v0.1.1-rc.1.tex"
RC2=ROOT/"manuscript/latex/atlas-v0.1.1-rc.2.tex"
BASE=ROOT/"manuscript/latex/atlas-v0.1.0.tex"
BASE_SHA="0d636871e6875bbadbd244e54bf272fdefe2dbd5179515d9d22d3a25e49c384a"
RC1_SHA="9818f897e2cba7482a1853467e30d9cb14890d68923e83d9368a6d57f766372a"

def sha(bs):return hashlib.sha256(bs).hexdigest()
def run(args):
    print("RUN", " ".join(str(a) for a in args[:3]),flush=True)
    subprocess.run([str(v) for v in args],cwd=ROOT,check=True)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--check",action="store_true")
    opts=parser.parse_args()
    assert sha(BASE.read_bytes())==BASE_SHA, "protected v0.1.0 canonical source changed"
    assert sha(RC1.read_bytes())==RC1_SHA, "RC1 overlay predecessor changed"
    if str(ROOT/"tools") not in sys.path:sys.path.insert(0,str(ROOT/"tools"))
    from normalize_editorial_heading_numbers import normalize
    import pypandoc

    run([sys.executable,"tools/assemble_manuscript.py",
         "--output","/tmp/atlas-rc.md",
         "--manifest","/tmp/atlas-editorial-rc2-source-manifest.json","--check"])
    run([sys.executable,"tools/editorial_prepare_markdown.py"])
    pandoc=pypandoc.get_pandoc_path()
    source=Path("/tmp/atlas-rc-release-clean.md")
    assert source.read_text().count("<!-- ATLAS_CHAPTER ")==80
    out=Path("/tmp/atlas-editorial-rc2-pandoc.tex")
    run([pandoc,str(source),
        "--from=markdown+tex_math_dollars+tex_math_single_backslash+citations+raw_attribute",
        "--to=latex","--standalone","--top-level-division=chapter",
        "--toc","--number-sections","--citeproc",
        "--bibliography=sources/bibliography.bib","--resource-path=.",
        "-V","documentclass=book","-H","tools/release_header.tex",
        "-o",str(out)])
    previous=RC1.read_text(encoding="utf-8")
    generated=out.read_text(encoding="utf-8")
    chapter=re.compile(r"\\chapter\{")
    pch=[m.start() for m in chapter.finditer(previous)]
    gch=[m.start() for m in chapter.finditer(generated)]
    assert len(pch)==len(gch)==80
    tail,num=normalize(generated[gch[4]:])
    assert num and len(num)>1800, "expected corpus-wide chapter heading normalization"
    rc2=previous[:pch[4]]+tail
    assert len(list(chapter.finditer(rc2)))==80
    labels=lambda s:set(re.findall(r"\\label\{([^}]+)\}",s))
    assert len(labels(rc2))==2971
    assert labels(rc2)==labels(previous), "lost or unexpectedly gained historical anchors"
    assert rc2.count(r"\includegraphics")==18
    assert rc2.count("figures/derivatives/ATLAS-FIG-OPTBASE-001-v0.1.2.png")==1
    assert not normalize(rc2)[1], "redundant heading ordinals remain"
    assert "state-dependent time domain" in rc2[:pch[4]]
    assert "separate agent roles" not in rc2, "governance note leaked into chapter math"

    if opts.check:
        assert RC2.exists() and RC2.read_text(encoding="utf-8")==rc2,"RC2 stale relative to source chapters/Part I overlay"
        print("RC2_RECOMPOSITION_PASS",sha(rc2.encode()),"labels",len(labels(rc2)),"figures",18,flush=True)
    else:
        RC2.write_text(rc2,encoding="utf-8")
        print("RC2_WRITTEN",str(RC2),"sha256",sha(RC2.read_bytes()),"bytes",RC2.stat().st_size,
          "labels",len(labels(rc2)),"figures",18,flush=True)
if __name__=="__main__":main()
