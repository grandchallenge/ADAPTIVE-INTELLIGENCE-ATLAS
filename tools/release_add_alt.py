from pathlib import Path
import html as html_lib
import re
p=Path("/tmp/atlas-rc.html")
s=p.read_text(encoding="utf-8")
pat=re.compile(r"(<figure>\s*<img\b)([^>]*?)(\s*/?>)\s*<figcaption>(.*?)</figcaption>", re.DOTALL)
count=0
def repl(m):
    global count
    attrs=m.group(2)
    cap_html=m.group(4)
    cap=re.sub(r"<[^>]+>", " ", cap_html)
    cap=html_lib.unescape(re.sub(r"\s+", " ", cap)).strip()
    if not cap: raise SystemExit("empty figure caption")
    if " alt=" in attrs: raise SystemExit("unexpected existing alt")
    count += 1
    return m.group(1)+attrs+f' alt="{html_lib.escape(cap, quote=True)}"'+m.group(3)+"\n<figcaption>"+cap_html+"</figcaption>"
s=pat.sub(repl,s)
if count != 18: raise SystemExit(f"expected 18 alt attributes, got {count}")
p.write_text(s,encoding="utf-8",newline="\n")
print("alt_attributes",count)