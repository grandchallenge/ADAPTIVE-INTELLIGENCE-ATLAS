from pathlib import Path
import re
src=Path("/tmp/atlas-rc-canonical.tex")
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
Path("/tmp/atlas-rc-html-input.tex").write_text("\n".join(out)+"\n",encoding="utf-8")
print("normalized_images",n)