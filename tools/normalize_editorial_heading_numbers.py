#!/usr/bin/env python3
"""Normalize redundant leading decimal ordinals in generated LaTeX headings.

Only \section and \subsection LaTeX *headings* are transformed. TeX generated
numbering supplies hierarchy. Preserve every label, byte outside the heading
arguments, and source/claim content. This tool never modifies a public edition.
"""
import argparse
import re
from pathlib import Path

HEAD = re.compile(r"\\(section|subsection|subsubsection)\{")
PREFIX = re.compile(r"^(\d+(?:\.\d+)*)(?:\.)?[ \t\n]+")
TEXORPDF = re.compile(r"^(\\texorpdfstring)\{")

def bracket_end(s, start):
    assert s[start] == "{"
    depth=0
    for i in range(start,len(s)):
        if s[i]=="{" and (i==0 or s[i-1]!="\\"):
            depth+=1
        elif s[i]=="}" and (i==0 or s[i-1]!="\\"):
            depth-=1
            if depth==0:return i
    raise ValueError("unbalanced LaTeX heading brace")

def cleanup(title):
    m=PREFIX.match(title)
    if m:
        return title[m.end():], True
    if title.startswith(r"\texorpdfstring{"):
        a=title.index("{")
        b=bracket_end(title,a)
        c=b+1
        assert title[c]=="{"
        e=bracket_end(title,c)
        assert e==len(title)-1
        first,first_yes=cleanup(title[a+1:b])
        second,second_yes=cleanup(title[c+1:e])
        if not first_yes and not second_yes:
            return title,False
        if not (first_yes and second_yes):
            raise AssertionError("unpaired texorpdfstring section ordinals")
        return title[:a+1]+first+title[b:c+1]+second+title[e:],True
    return title,False

def normalize(text):
    dest=[];pos=0;count=0; changes=[]
    for m in HEAD.finditer(text):
        if m.start()<pos:continue
        start=m.end()-1
        end=bracket_end(text,start)
        title=text[start+1:end]
        repl,yes=cleanup(title)
        if yes:
            dest.extend([text[pos:start+1],repl,"}"])
            changes.append((m.group(1),title[:100].replace("\n"," "),repl[:100].replace("\n"," ")))
            count+=1
        else:dest.append(text[pos:end+1])
        pos=end+1
    dest.append(text[pos:])
    return "".join(dest),changes

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path",type=Path)
    ap.add_argument("--apply",action="store_true")
    ns=ap.parse_args()
    before=ns.path.read_text(encoding="utf-8")
    after,changes=normalize(before)
    assert len(changes)>2200, len(changes)
    assert after.count(r"\chapter{")==80
    labels=lambda s:re.findall(r"\\label\{[^}]+\}",s)
    assert labels(before)==labels(after)
    second,unexpected=normalize(after)
    assert second==after and not unexpected
    print(f"NORMALIZED_HEADINGS {len(changes)}", flush=True)
    print("SPECIAL",sum("texorpdfstring" in a for _,a,_ in changes))
    for row in changes[:5]: print(row)
    if ns.apply:ns.path.write_text(after,encoding="utf-8")

if __name__=="__main__":main()
