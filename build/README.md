# Build workspace

This directory contains generated artifacts and governed release-candidate renderings.

Canonical manuscript membership and order originate from `governance/CHAPTER_LEDGER.yaml`.

For ordinary working assembly use:

`python tools/assemble_manuscript.py`

For release candidate `v0.1.0-rc.1`:

- canonical editorial source: `manuscript/latex/atlas-v0.1.0-rc.1.tex`;
- PDF presentation artifact: `build/release-candidate/v0.1.0-rc.1/atlas-v0.1.0-rc.1.pdf`;
- HTML accessibility artifact: `build/release-candidate/v0.1.0-rc.1/atlas-v0.1.0-rc.1.html`;
- exact hashes/toolchain/input identities: `build/release-candidate/v0.1.0-rc.1/release-manifest.json`.

Release-candidate artifacts are not public-release artifacts. They do not change chapter lifecycle status and do not imply certification or publication authorization.
