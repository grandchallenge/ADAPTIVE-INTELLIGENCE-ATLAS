#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


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

license_path = ROOT / "LICENSE"
if not license_path.is_file():
    errors.append("repository LICENSE is missing")
else:
    license_text = license_path.read_text(encoding="utf-8")
    required_license_markers = (
        "Copyright © 2026 Grand Challenge Technologies Ltd.",
        "CC BY 4.0",
        "CC-BY-4.0",
        "LICENSES/CC-BY-4.0.txt",
        "MIT License",
        "LICENSES/MIT.txt",
        "Third-party material",
        "No endorsement or certification implication",
    )
    for marker in required_license_markers:
        if marker not in license_text:
            errors.append(f"repository LICENSE missing selected-license marker: {marker}")
    if "LICENSE SELECTION PENDING" in license_text:
        errors.append("repository LICENSE still contains pending-selection state")

license_files = {
    "LICENSES/CC-BY-4.0.txt": "13ca539f377dc705af32b8d2ce89262298ea2f06",
    "LICENSES/MIT.txt": "a431eb26664c286c260aa831d9a57adf32d303f0",
}
for rel, expected_blob in license_files.items():
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"selected standard license text missing: {rel}")
        continue
    actual_blob = git_blob_sha1(path.read_bytes())
    if actual_blob != expected_blob:
        errors.append(
            f"selected standard license text changed: {rel}: "
            f"expected {expected_blob}, got {actual_blob}"
        )

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
    if p.is_file() and p.name not in {".gitkeep", "README.md"}
)
release_auth_path = ROOT / "governance/RELEASE_AUTHORIZATION.yaml"
if release_files:
    if not release_auth_path.is_file():
        errors.append(
            "release artifacts exist without governance/RELEASE_AUTHORIZATION.yaml: "
            + ", ".join(release_files)
        )
    else:
        release_auth = yaml.safe_load(release_auth_path.read_text(encoding="utf-8")) or {}
        if release_auth.get("public_release_authorized") is not True:
            errors.append(
                "release artifacts exist without explicit public_release_authorized: true"
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
    f"{sum(word_counts.values())} approximate words; scoped CC-BY-4.0/MIT licensing verified; "
    "public release still requires explicit governance authorization"
)
