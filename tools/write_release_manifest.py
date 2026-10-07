#!/usr/bin/env python3
from pathlib import Path
import hashlib, importlib.metadata, json, subprocess

ROOT=Path(__file__).resolve().parents[1]
VERSION="0.1.0-rc.1"
BASELINE="ab781fbf7861c36b7750a0ba2710a34ade625122"
EPOCH=1791331200
TEX=ROOT/"manuscript/latex"/f"atlas-v{VERSION}.tex"
OUT=ROOT/"build/release-candidate"/f"v{VERSION}"
PDF=OUT/f"atlas-v{VERSION}.pdf"
HTML=OUT/f"atlas-v{VERSION}.html"

def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

assembly=Path("/tmp/atlas-rc-manifest.json")
chapters=[]
if assembly.exists():
    chapters=json.loads(assembly.read_text(encoding="utf-8")).get("chapters",[])
else:
    ledger=json.loads((ROOT/"governance/CHAPTER_LEDGER.yaml").read_text(encoding="utf-8"))
    for i,c in enumerate(ledger["chapters"],start=1):
        raw=(ROOT/c["manuscript_path"]).read_bytes()
        header=f"blob {len(raw)}\0".encode()
        blob=hashlib.sha1(header+raw).hexdigest()
        chapters.append({"index":i,"id":c["id"],"part_id":c["part_id"],"status":c["status"],"path":c["manuscript_path"],"git_blob_sha1":blob})

pandoc_version=subprocess.check_output(["python3","-c","import pypandoc; print(pypandoc.get_pandoc_version())"],text=True).strip()
pdflatex_version=subprocess.check_output(["pdflatex","--version"],text=True).splitlines()[0]
manifest={
 "schema_version":"1.0.0",
 "artifact_class":"release-candidate",
 "public_release_authorized":False,
 "version":VERSION,
 "release_date":"2026-10-07",
 "source_baseline_commit":BASELINE,
 "source_date_epoch":EPOCH,
 "canonical_source":f"manuscript/latex/atlas-v{VERSION}.tex",
 "presentation_artifacts":{
   "pdf":f"build/release-candidate/v{VERSION}/atlas-v{VERSION}.pdf",
   "html":f"build/release-candidate/v{VERSION}/atlas-v{VERSION}.html"},
 "chapter_count":80,
 "figure_count":18,
 "legacy_map_display_normalizations":11,
 "false_setext_normalizations":26,
 "html_image_wrapper_normalizations":18,
 "html_alt_attributes":18,
 "assembly_chapters":chapters,
 "toolchain":{"pypandoc_binary":importlib.metadata.version("pypandoc_binary"),"pandoc":pandoc_version,"pdflatex":pdflatex_version},
 "sha256":{"latex":sha256(TEX),"pdf":sha256(PDF),"html":sha256(HTML)}
}
OUT.mkdir(parents=True,exist_ok=True)
(OUT/"release-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(manifest["sha256"],indent=2))
