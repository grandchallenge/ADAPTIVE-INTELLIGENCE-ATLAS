# PUBLIC-RELEASE-001 — Publication Receipt

## Final state

**PUBLISHED AND VERIFIED**

Public release:

`https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/releases/tag/atlas-v0.1.0`

Published at:

`2026-10-07T23:24:43Z`

## Final tag identity

- tag: `atlas-v0.1.0`
- tag target: `1d4c2532533ff98afb998f86e0443d3fa1d8682e`
- target is the exact protected implementation merge audited by `AUDIT-077`

## Implementation and audit

- PUBLIC-RELEASE-001 issue: #309
- implementation PR: #310
- exact implementation head: `5058b6d49b1605e6d8889bbfddc14d583c560784`
- implementation Actions run: `37701495663` — success
- protected implementation merge: `1d4c2532533ff98afb998f86e0443d3fa1d8682e`
- final audit: `AUDIT-077 — PASS — NO REPAIR`
- audit issue: #311
- audit PR: #312
- exact audit head: `25e62c35cdbd63a6dedc9ccf1f5e1a384274979b`
- audit Actions run: `37701860716` — success
- protected audit merge: `202c84308ea0a3adbe6bf1dd6c426e3d43dfe2ed`

## GitHub Release state

- draft: false
- prerelease: false
- title: `A Mathematical Atlas of Adaptive Intelligence v0.1.0`
- tag: `atlas-v0.1.0`

## Published asset round-trip verification

All six release assets were downloaded back from GitHub after publication and their SHA-256 values matched the protected repository payload exactly.

- `atlas-v0.1.0.tex` — `0d636871e6875bbadbd244e54bf272fdefe2dbd5179515d9d22d3a25e49c384a`
- `atlas-v0.1.0.pdf` — `efd0f21088ced19e5cc706069cc57cd4d0fa57ffc402c63767d8ad4939d96b96`
- `atlas-v0.1.0.html` — `795700db6ac8cd689d8dcfad7d116734015f7a196e3fd3fce2608eb5cac7daa4`
- `release-manifest.json` — `3b33f827b687a4ace3a585805a5f88f84da0b58c463d167e69c97808f2250b44`
- `RELEASE_NOTES.md` — `d0b503aec5ea3a5166ec963ea76231ff4197cf67b78f8b4ae6d3584308e4e50f`
- `SHA256SUMS.txt` — `7834397751ded9c8d91db350ca1c1786f20fb2c42f6c7d24e1febbbc662a61bf`

GitHub's own reported digests for the three substantive assets matched the governed hashes before the independent download replay.

## Release architecture

- canonical source of truth: LaTeX
- primary presentation artifact: PDF
- broader-accessibility artifact: HTML
- final artifacts are byte-preserving promotions of the independently audited `atlas-v0.1.0-rc.1` candidate

## Governance conclusion

The Human Steward's explicit public-release authorization has been fully executed.

No further action is required for Atlas `v0.1.0` publication. Future manuscript changes require a new bounded transaction and a new release identity.
