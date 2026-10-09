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
from normalize_editorial_heading_numbers import normalize
normalized_tail, changes = normalize(a[aa[4]:])
assert normalize(b)[1] == [], 'candidate contains duplicate ordinals'
from normalize_editorial_heading_numbers import cleanup
assert cleanup('2x2 quadratic example') == ('2x2 quadratic example',False)
assert cleanup('12. Operator type') == ('Operator type',True)
assert cleanup('Chapter 2. geometry') == ('Chapter 2. geometry',False)
legacy_path='figures/masters/ATLAS-FIG-OPTBASE-001.png'
candidate_path='figures/derivatives/ATLAS-FIG-OPTBASE-001-v0.1.1.png'
assert a.count(legacy_path)==1
assert b.count(candidate_path)==1
assert legacy_path not in b
expected_tail=normalized_tail.replace(legacy_path,candidate_path)
assert expected_tail.count("The binomial expansion truncates:")==1
expected_tail=expected_tail.replace("The binomial expansion truncates:\n",
    "For every integer \\(n\\ge 2\\), the nilpotent binomial expansion truncates:\n",1)
assert expected_tail.count("Therefore\n\n\\[\n\\boxed{") >= 1
expected_tail=expected_tail.replace("Therefore\n\n\\[\n\\boxed{",
    "For these \\(n\\), therefore\n\n\\[\n\\boxed{",1)
assert expected_tail.count("The eigenvalue is always ")==1
expected_tail=expected_tail.replace("The eigenvalue is always ",
    "The low powers are \\(A^0=I\\) and \\(A^1=A\\). Treating them separately avoids the \\(a^0\\) convention at \\(a=0\\).\n\nThe eigenvalue is always ",1)
assert expected_tail.count("For \\(A^n\\),\n\n\\[\np=a^n,")==1
expected_tail=expected_tail.replace("For \\(A^n\\),\n\n\\[\np=a^n,",
    "For \\(B=A^n\\) with \\(n\\ge 2\\),\n\n\\[\np=a^n,",1)
assert expected_tail == b[bb[4]:], "chapters 5-80 changed beyond heading ordinals, declared OPTBASE image, and NONNORMAL exponent-domain clarification"
import struct, yaml, subprocess
asset=ROOT/candidate_path
assert asset.exists()
data=asset.read_bytes()
assert data[:8]==bytes.fromhex("89504e470d0a1a0a")
w,h=struct.unpack(">II",data[16:24])
assert (w,h)==(2482,738)
asset_hash=hashlib.sha256(data).hexdigest()
assert asset_hash=="550ad96bd4f7763260a8b64e79518734b0133dc318f5ee9bb221d2ad1fcf7591"
manifest=yaml.safe_load((ROOT/"figures/derivatives/ATLAS-FIG-OPTBASE-001-v0.1.1.yaml").read_text())
assert manifest["generator"]["image_sha256"]==asset_hash
assert manifest["generator"]["render_pixels"]==[w,h]
assert manifest["generator"]["system"]=="Python Matplotlib"
assert manifest["original_wolfram_provenance"]["original_master"]==legacy_path
assert manifest["generator"]["source_git_blob_sha1"]==subprocess.check_output(["git","hash-object",str(ROOT/manifest["generator"]["source"])],text=True).strip()
assert manifest["original_wolfram_provenance"]["source_git_blob_sha1"]==subprocess.check_output(["git","hash-object",str(ROOT/manifest["original_wolfram_provenance"]["source"])],text=True).strip()
from fractions import Fraction
assert (Fraction(6,5)**2+Fraction(8,5)**2)==4
assert Fraction(183,100)-Fraction(181,100)==Fraction(1,50)
assert len(changes)>2000, "expected corpus-wide heading normalization"
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
print("PASS: public source SHA-256; 80 chapters; original labels; 76 downstream chapters differ only by normalized headings and one OPTBASE derivative and a scoped NONNORMAL exponent-domain clarification; exact figure inputs and hash")
print("CANDIDATE_SHA256:", hashlib.sha256(new.read_bytes()).hexdigest())
