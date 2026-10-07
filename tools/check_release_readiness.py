#!/usr/bin/env python3
from pathlib import Path
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

ledger = json.loads((ROOT / "governance/CHAPTER_LEDGER.yaml").read_text(encoding="utf-8"))
chapters = ledger.get("chapters", [])
paths = [c.get("manuscript_path") for c in chapters]

if len(chapters) != 80:
    errors.append(f"expected 80 canonical chapters, found {len(chapters)}")
if any(c.get("status") != "draft-v0.1" for c in chapters):
    errors.append("release-readiness transaction must not promote chapter lifecycle state")
if any(not p for p in paths):
    errors.append("canonical chapter missing manuscript_path")
if len(paths) != len(set(paths)):
    errors.append("duplicate canonical manuscript path")
if any(p and not p.startswith("manuscript/parts/") for p in paths):
    errors.append("canonical manuscript path outside manuscript/parts")
for rel in paths:
    if rel and not (ROOT / rel).is_file():
        errors.append(f"missing canonical manuscript: {rel}")

all_md = {
    str(p.relative_to(ROOT)).replace("\\", "/")
    for p in (ROOT / "manuscript/parts").rglob("*.md")
}
extras = sorted(all_md - set(paths))
expected_extras = sorted(
    [
        "manuscript/parts/12-diagnostics-robustness-compression/ATLAS-CH-DIAGREAD-001.md",
        "manuscript/parts/12-diagnostics-robustness-compression/_probe.md",
    ]
)
if extras != expected_extras:
    errors.append(f"unexpected non-ledger manuscript files: {extras}")

license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
if not license_text.startswith("LICENSE SELECTION PENDING"):
    errors.append("license gate changed without an explicit release-promotion transaction")
if "before public release" not in license_text:
    errors.append("license file no longer records the public-release gate")

citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
for key in ("cff-version", "title", "type", "authors", "message", "repository-code"):
    if not citation.get(key):
        errors.append(f"CITATION.cff missing {key}")
if citation.get("type") != "book":
    errors.append("CITATION.cff type must remain book")
if "specific tagged release or commit" not in str(citation.get("message", "")):
    errors.append("CITATION.cff must preserve commit/tag citation semantics")

release_files = sorted(
    str(p.relative_to(ROOT)).replace("\\", "/")
    for p in (ROOT / "releases").rglob("*")
    if p.is_file() and p.name != ".gitkeep" and p.name != "README.md"
)
if release_files:
    errors.append(
        "public release artifacts exist while LICENSE_SELECTION_PENDING is active: "
        + ", ".join(release_files)
    )

word_counts = {}
for c in chapters:
    text = (ROOT / c["manuscript_path"]).read_text(encoding="utf-8")
    word_counts[c["id"]] = len(re.findall(r"\b\w+[\w'-]*\b", text))
short = sorted((cid, n) for cid, n in word_counts.items() if n < 1000)
if short:
    warnings.append(
        "editorial maturity review required for short canonical chapters: "
        + ", ".join(f"{cid}={n}" for cid, n in short)
    )

if errors:
    for error in errors:
        print("ERROR:", error)
    for warning in warnings:
        print("WARNING:", warning)
    raise SystemExit(1)

for warning in warnings:
    print("WARNING:", warning)
print(
    "OK: release-readiness boundary intact; "
    f"{len(chapters)} canonical chapters, {len(extras)} preserved non-ledger companions, "
    f"{sum(word_counts.values())} approximate words; LICENSE_SELECTION_PENDING blocks public release"
)
