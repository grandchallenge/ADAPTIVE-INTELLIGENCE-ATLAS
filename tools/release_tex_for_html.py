#!/usr/bin/env python3
"""Create HTML-safe TeX from an explicitly bound Atlas manuscript source.

Default is the canonical mutable RC2 artifact in this repository, never a
process-global temporary 'canonical' alias left by an unrelated run.
"""
from pathlib import Path
import argparse
import re

ROOT=Path(__file__).resolve().parent.parent
parser=argparse.ArgumentParser()
parser.add_argument("--source",type=Path,default=ROOT/"manuscript/latex/atlas-v0.1.1-rc.2.tex")
parser.add_argument("--output",type=Path,default=Path("/tmp/atlas-rc-html-input.tex"))
args=parser.parse_args()
src=args.source.resolve()
expected=(ROOT/"manuscript/latex/atlas-v0.1.1-rc.2.tex").resolve()
if src != expected:
    raise SystemExit("HTML source must equal canonical RC2 TeX: "+str(expected))
lines=src.read_text(encoding="utf-8").splitlines()
out=[]; n=0
for line in lines:
    if "\\pandocbounded{\\includegraphics" in line:
        m=re.search(r"\]\{([^{}]+)\}\}\s*$", line)
        if not m: raise SystemExit("unparsed image line: "+line[:200])
        path=m.group(1)
        out.append(r"\includegraphics{"+path+"}")
        n+=1
    else:
        out.append(line)
if n!=18:raise SystemExit("unexpected figure count: "+str(n))
args.output.write_text("\n".join(out)+"\n",encoding="utf-8")
print("HTML_SOURCE_BINDING_PASS",src,"figures",n,"bytes",args.output.stat().st_size)
