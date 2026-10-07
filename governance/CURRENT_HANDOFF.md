# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-07  
**Recovery authority:** `governance/ACTIVE_TRANSACTION.yaml` on `state/atlas-controller`  
**Current protected main:** `e096897e2e30459bfd5a3af660fd3e9dee53a1c9`

## Restart rule

1. Read `governance/ACTIVE_TRANSACTION.yaml` first.
2. Read this handoff.
3. Fetch live `main`.
4. Verify public tag `atlas-v0.1.0` still dereferences to the protected implementation merge below.
5. Verify the GitHub Release remains published and its governed asset digests remain unchanged.
6. Repository state overrides chat history.

## Terminal state

Atlas `v0.1.0` is **published and verified**.

There is no pending bounded transaction.

- controller state: `complete`;
- architecture drafting: complete;
- global synthesis: complete and audited;
- release readiness: complete and audited;
- repository licensing: complete and audited;
- release candidate: complete and audited;
- public release: complete and audited;
- publication round-trip verification: complete;
- Chapter Ledger: 80/80 chapters remain `draft-v0.1`.

## Public release

Release URL:

`https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/releases/tag/atlas-v0.1.0`

Published at:

`2026-10-07T23:24:43Z`

Release state:

- draft: false;
- prerelease: false;
- tag: `atlas-v0.1.0`;
- title: `A Mathematical Atlas of Adaptive Intelligence v0.1.0`.

## Final tag identity

`atlas-v0.1.0`

dereferences to:

`1d4c2532533ff98afb998f86e0443d3fa1d8682e`

This is the exact protected PUBLIC-RELEASE-001 implementation merge audited by AUDIT-077.

## PUBLIC-RELEASE-001

Implementation:

- issue #309 — closed completed;
- PR #310 — merged;
- exact validated implementation head: `5058b6d49b1605e6d8889bbfddc14d583c560784`;
- Actions run: `37701495663` — success;
- protected implementation merge: `1d4c2532533ff98afb998f86e0443d3fa1d8682e`;
- implementation merge tree: zero file differences from exact validated head.

Fresh final audit:

- `AUDIT-077`;
- issue #311 — closed completed;
- PR #312 — merged;
- exact validated audit head: `25e62c35cdbd63a6dedc9ccf1f5e1a384274979b`;
- Actions run: `37701860716` — success;
- protected audit merge: `202c84308ea0a3adbe6bf1dd6c426e3d43dfe2ed`;
- disposition: **PASS — NO REPAIR**.

Post-publication reconciliation:

- PR #313 — merged;
- exact reconciliation head: `4af3b3531b520121d53deef0a2b7eb6b633b36fa`;
- Actions run: `37702438193` — success;
- current protected main: `e096897e2e30459bfd5a3af660fd3e9dee53a1c9`.

## Release architecture

- **LaTeX** — canonical source of truth;
- **PDF** — primary presentation artifact;
- **HTML** — broader-accessibility artifact.

Final artifacts are byte-preserving promotions of the independently audited `atlas-v0.1.0-rc.1` candidate.

## Governed artifact hashes

- LaTeX: `0d636871e6875bbadbd244e54bf272fdefe2dbd5179515d9d22d3a25e49c384a`
- PDF: `efd0f21088ced19e5cc706069cc57cd4d0fa57ffc402c63767d8ad4939d96b96`
- HTML: `795700db6ac8cd689d8dcfad7d116734015f7a196e3fd3fce2608eb5cac7daa4`
- release manifest: `3b33f827b687a4ace3a585805a5f88f84da0b58c463d167e69c97808f2250b44`
- release notes: `d0b503aec5ea3a5166ec963ea76231ff4197cf67b78f8b4ae6d3584308e4e50f`
- checksums: `7834397751ded9c8d91db350ca1c1786f20fb2c42f6c7d24e1febbbc662a61bf`

All six GitHub Release assets were downloaded after publication and matched the protected repository payload byte-for-byte.

GitHub's reported digests for the substantive LaTeX/PDF/HTML assets also match the governed hashes.

## Durable publication evidence

Protected main contains:

- `governance/RELEASE_AUTHORIZATION.yaml`;
- `governance/tranches/PUBLIC-RELEASE-001.md`;
- `governance/tranches/PUBLIC-RELEASE-001-PUBLICATION.md`;
- `reviews/AUDIT-077.md`;
- `releases/v0.1.0/`;
- final public-release validation in `tools/check_public_release.py`.

## Licensing

Copyright holder:

**Grand Challenge Technologies Ltd.**

- CC BY 4.0 for publication/documentation/figure material;
- MIT for software/tooling;
- file-specific and third-party rights take precedence.

## Completion boundary

**Boundary name: PUBLIC_RELEASE_COMPLETE.**

No further action is required for Atlas `v0.1.0`.

Any future manuscript/content change requires a new bounded transaction, fresh validation/audit appropriate to the change, and a new release identity.
