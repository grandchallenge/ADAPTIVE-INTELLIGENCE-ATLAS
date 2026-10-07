# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-07  
**Recovery authority:** `governance/ACTIVE_TRANSACTION.yaml` on `state/atlas-controller`  
**Current protected main:** `498e4c2f517255883f83bf8e23afba8841e5c9dc`

## Restart rule

1. Read `governance/ACTIVE_TRANSACTION.yaml` first.
2. Read this handoff.
3. Fetch live `main`.
4. Verify candidate tag `atlas-v0.1.0-rc.1` still dereferences to the exact implementation merge below.
5. Repository state overrides chat history.

## Current state

- architecture drafting: complete;
- global synthesis: complete and audited;
- release readiness: complete and audited;
- repository licensing: complete and audited;
- release candidate: complete and audited;
- Chapter Ledger: 80/80 chapters remain `draft-v0.1`;
- public release: **not authorized**;
- controller state: `blocked-human-governance`.

## RELEASE-CANDIDATE-001 — complete

Implementation:

- issue #305 — closed completed;
- PR #306 — merged;
- source baseline: `ab781fbf7861c36b7750a0ba2710a34ade625122`;
- exact validated implementation head: `00f608264bd40a9e24c073e99a10b6f5df121657`;
- Actions run: `37634048971` — success;
- protected implementation merge: `e6a97fe9cf2ef4577f046c95f74f5eb690ba2e0e`;
- implementation merge tree: zero file differences from exact validated head.

Fresh audit:

- `AUDIT-076`;
- issue #307 — closed completed;
- PR #308 — merged;
- exact validated audit head: `a1b1e35e24efdbca1301b01057969422f7d457f9`;
- Actions run: `37634616690` — success;
- final audit merge / current protected main: `498e4c2f517255883f83bf8e23afba8841e5c9dc`;
- audit merge tree: zero file differences from exact validated audit head;
- disposition: **PASS — NO REPAIR**.

## Candidate identity

Annotated tag:

`atlas-v0.1.0-rc.1`

The tag dereferences to:

`e6a97fe9cf2ef4577f046c95f74f5eb690ba2e0e`

This is the exact audited implementation merge containing the candidate artifacts.

The tag is a release-candidate identity only. It is not a GitHub Release and does not authorize public release.

## Release architecture

Human Steward decision:

- **LaTeX** is the canonical source of truth;
- **PDF** is the primary presentation artifact;
- **HTML** is the broader-accessibility artifact.

Canonical LaTeX:

`manuscript/latex/atlas-v0.1.0-rc.1.tex`

SHA-256:

`0d636871e6875bbadbd244e54bf272fdefe2dbd5179515d9d22d3a25e49c384a`

PDF:

`build/release-candidate/v0.1.0-rc.1/atlas-v0.1.0-rc.1.pdf`

SHA-256:

`efd0f21088ced19e5cc706069cc57cd4d0fa57ffc402c63767d8ad4939d96b96`

HTML:

`build/release-candidate/v0.1.0-rc.1/atlas-v0.1.0-rc.1.html`

SHA-256:

`795700db6ac8cd689d8dcfad7d116734015f7a196e3fd3fce2608eb5cac7daa4`

Exact input chapter identities, toolchain details, and hashes are recorded in:

`build/release-candidate/v0.1.0-rc.1/release-manifest.json`

## MECHDIAG treatment

`ATLAS-CH-MECHDIAG-001` remains intentionally concise and is presented as:

**Interlude: From Readability to Functional Evidence**

Its stable chapter identity and downstream handoff are preserved. No mathematical strengthening or padding was introduced.

## Validation boundary

Protected exact-head validation confirms:

- 80 canonical chapters;
- 126 hard dependency edges;
- one graph root;
- 18 registered/rendered figures;
- 85 sources;
- 175 bibliography keys;
- 18 embedded HTML images;
- 18 HTML alt attributes;
- exact release-candidate artifact hashes;
- deterministic promoted build path;
- no public-release authorization;
- no substantive files under `releases/`.

## Licensing

Copyright holder:

**Grand Challenge Technologies Ltd.**

Repository licensing remains:

- CC BY 4.0 for publication/documentation/figure material;
- MIT for software/tooling;
- file-specific and third-party rights take precedence.

## Remaining governance boundary

No further mechanical release-candidate work is pending.

Public release requires a new explicit Human Steward authorization before any of the following may occur:

- creation of a GitHub Release;
- population of `releases/` with substantive public-release artifacts;
- creation or mutation of `governance/RELEASE_AUTHORIZATION.yaml` to record `public_release_authorized: true`;
- representation of the candidate as publicly released/final.

**Boundary name: HUMAN_STEWARD_PUBLIC_RELEASE_AUTHORIZATION.**
