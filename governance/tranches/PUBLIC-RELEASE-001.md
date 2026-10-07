# PUBLIC-RELEASE-001 — Atlas v0.1.0

## Human Steward authorization

On 2026-10-07 the Human Steward instructed the controller to **"resume to completion"** immediately after the recorded boundary `HUMAN_STEWARD_PUBLIC_RELEASE_AUTHORIZATION`.

That instruction is the explicit authority for this bounded public-release transaction.

## Protected predecessor

- protected main: `498e4c2f517255883f83bf8e23afba8841e5c9dc`
- audited candidate tag: `atlas-v0.1.0-rc.1`
- audited candidate implementation merge: `e6a97fe9cf2ef4577f046c95f74f5eb690ba2e0e`
- audited candidate audit merge: `498e4c2f517255883f83bf8e23afba8841e5c9dc`
- candidate audit: `AUDIT-076 — PASS — NO REPAIR`

## Promotion policy

Final version: `0.1.0`

Final tag to be created only after fresh final-release audit:

`atlas-v0.1.0`

The promotion is byte-preserving for all substantive release artifacts. No mathematical-content mutation is authorized.

Exact inherited SHA-256 values:

- LaTeX: `0d636871e6875bbadbd244e54bf272fdefe2dbd5179515d9d22d3a25e49c384a`
- PDF: `efd0f21088ced19e5cc706069cc57cd4d0fa57ffc402c63767d8ad4939d96b96`
- HTML: `795700db6ac8cd689d8dcfad7d116734015f7a196e3fd3fce2608eb5cac7daa4`

## Authorized repository state

The transaction may:

1. record `governance/RELEASE_AUTHORIZATION.yaml` with `public_release_authorized: true`;
2. create final canonical source `manuscript/latex/atlas-v0.1.0.tex` as an exact byte copy of the audited candidate source;
3. populate `releases/v0.1.0/` with exact byte-preserving LaTeX/PDF/HTML copies;
4. bind `CITATION.cff` to version `0.1.0` and date `2026-10-07`;
5. add final manifest, checksums, notes, and validation;
6. merge only after exact-head CI;
7. conduct a fresh public-release audit;
8. only after that audit, create tag `atlas-v0.1.0`, create the GitHub Release, upload the exact governed assets, and verify published asset hashes.

## Prohibited mutation

This transaction does not authorize:

- mathematical-content changes;
- silent replacement of audited release bytes;
- removal of source/evidence/provenance distinctions;
- relicensing third-party material;
- representation of the release as mathematical certification.

## Publication state

At this receipt's implementation stage, public release is **authorized but not yet published**. Publication occurs only after the final-release audit passes and the GitHub Release is created from the exact protected final tag.
