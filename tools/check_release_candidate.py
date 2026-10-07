#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, yaml

ROOT=Path(__file__).resolve().parents[1]
VERSION="0.1.0-rc.1"
OUT=ROOT/"build/release-candidate"/f"v{VERSION}"
MANIFEST=OUT/"release-manifest.json"
errors=[]

def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

if not MANIFEST.is_file(): errors.append("release manifest missing")
else:
    m=json.loads(MANIFEST.read_text(encoding="utf-8"))
    if m.get("artifact_class")!="release-candidate": errors.append("artifact_class mismatch")
    if m.get("public_release_authorized") is not False: errors.append("candidate must not authorize public release")
    if m.get("version")!=VERSION: errors.append("version mismatch")
    if m.get("release_date")!="2026-10-07": errors.append("release date mismatch")
    if m.get("source_baseline_commit")!="ab781fbf7861c36b7750a0ba2710a34ade625122": errors.append("source baseline mismatch")
    if m.get("chapter_count")!=80: errors.append("chapter count mismatch")
    if m.get("figure_count")!=18: errors.append("figure count mismatch")
    if len(m.get("assembly_chapters",[]))!=80: errors.append("assembly chapter manifest must contain 80 entries")
    paths={
      "latex":ROOT/m["canonical_source"],
      "pdf":ROOT/m["presentation_artifacts"]["pdf"],
      "html":ROOT/m["presentation_artifacts"]["html"],
    }
    for kind,p in paths.items():
        if not p.is_file(): errors.append(f"{kind} artifact missing: {p}")
        elif sha256(p)!=m["sha256"].get(kind): errors.append(f"{kind} SHA-256 mismatch")
    if paths["latex"].is_file():
        tex=paths["latex"].read_text(encoding="utf-8")
        if sum(1 for x in tex.splitlines() if x.startswith(r"\chapter"))!=80: errors.append("canonical LaTeX must contain exactly 80 chapters")
        if tex.count(r"\includegraphics")!=18: errors.append("canonical LaTeX must contain exactly 18 figures")
        if "Interlude: From Readability to Functional" not in tex: errors.append("MECHDIAG interlude title missing")
    if paths["html"].is_file():
        h=paths["html"].read_text(encoding="utf-8",errors="replace")
        imgs=re.findall(r"<img\b[^>]*>",h)
        if len(imgs)!=18: errors.append(f"HTML image count {len(imgs)} != 18")
        if sum(1 for x in imgs if re.search(r"\balt=",x))!=18: errors.append("HTML must supply alt text for all 18 figures")
        if "Interlude: From Readability to" not in h: errors.append("HTML MECHDIAG interlude missing")
    if paths["pdf"].is_file() and not paths["pdf"].read_bytes().startswith(b"%PDF-"): errors.append("PDF signature missing")

auth_path=ROOT/"governance/RELEASE_AUTHORIZATION.yaml"
auth={}
if auth_path.exists():
    auth=yaml.safe_load(auth_path.read_text(encoding="utf-8")) or {}
public_release_authorized=auth.get("public_release_authorized") is True

citation=yaml.safe_load((ROOT/"CITATION.cff").read_text(encoding="utf-8"))
expected_citation_version="0.1.0" if public_release_authorized else VERSION
if citation.get("version")!=expected_citation_version: errors.append("CITATION.cff version inconsistent with release state")
if str(citation.get("date-released"))!="2026-10-07": errors.append("CITATION.cff date-released not bound")

release_files=[p for p in (ROOT/"releases").rglob("*") if p.is_file() and p.name not in {".gitkeep","README.md"}]
if release_files and not public_release_authorized:
    errors.append("substantive public release artifacts exist without explicit authorization: "+", ".join(str(p.relative_to(ROOT)) for p in release_files))

if errors:
    for e in errors: print("ERROR:",e)
    raise SystemExit(1)
state="authorized public-release promotion" if public_release_authorized else "public release not authorized"
print(f"OK: historical release candidate v0.1.0-rc.1 remains intact; 80 canonical chapters; 18 PDF/HTML figures; hashes verified; {state}")
