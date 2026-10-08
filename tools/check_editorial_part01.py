#!/usr/bin/env python3
"""Part I candidate invariance check; not an editorial or mathematical signoff."""
from pathlib import Path
import re
import hashlib

ROOT = Path(__file__).resolve().parent.parent
old = ROOT / "manuscript/latex/atlas-v0.1.0.tex"
new = ROOT / "manuscript/latex/atlas-v0.1.1-rc.1.tex"
expected_old = "0d636871e6875bbadbd244e54bf272fdefe2dbd5179515d9d22d3a25e49c384a"
assert hashlib.sha256(old.read_bytes()).hexdigest() == expected_old, "published canonical source changed"

a = old.read_text(encoding="utf-8")
b = new.read_text(encoding="utf-8")
chapter = re.compile(r"\\chapter\{")
aa = [m.start() for m in chapter.finditer(a)]
bb = [m.start() for m in chapter.finditer(b)]
assert len(aa) == len(bb) == 80, "chapter cardinality"
assert a[:aa[0]] == b[:bb[0]], "preamble was altered"
assert a[aa[4]:] == b[bb[4]:], "chapters 5-80 changed"
old4, new4 = a[aa[0]:aa[4]], b[bb[0]:bb[4]]
assert old4 != new4, "no Part I changes"
old_labels = set(re.findall(r"\\label\{([^}]+)\}", old4))
new_labels = set(re.findall(r"\\label\{([^}]+)\}", new4))
assert old_labels <= new_labels, f"lost original labels: {old_labels - new_labels}"
assert "present foundation tranche now backfills" not in new4
assert "This is why the book is not being written" not in new4
assert r"\mathrel{\rightsquigarrow}_{\Omega,\tau}" in new4
assert "scoped evidentiary support judgment" in new4
assert r"\Phi_0=\mathrm{id}_{\mathcal X}" in new4
assert "state-dependent time domain" in new4
assert "Start here: choose a reading route" in new4
assert "For definitions, examples, promotion failures" in new4
assert "For definitions, examples, promotion failures" not in a
assert new4.count(r"\section{10. Definition}") == 0

# Exact source identity and no claim of editorial acceptance.
receipt = (ROOT / "governance/editorial/v0.1.0/PART01_CORRECTION_CANDIDATE.md").read_text()
for phrase in ("NO EDITORIAL SIGNOFF", "INDEPENDENT TECHNICAL CHECK PENDING",
               "RENDERED PDF/HTML REVIEW PENDING", "atlas-v0.1.0"):
    assert phrase in receipt
print("PASS: public source SHA-256, preamble and 76-chapter invariance, 80 chapters, historical labels, bounded changes")
print("CANDIDATE_SHA256:", hashlib.sha256(new.read_bytes()).hexdigest())
