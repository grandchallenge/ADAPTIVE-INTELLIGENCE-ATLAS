# AUDIT-076 — RELEASE-CANDIDATE-001

## Disposition

**PASS — NO REPAIR**

The protected release candidate is internally consistent, reproducible under the declared build path, and remains correctly separated from public-release authorization.

## Audited identities

- source baseline: `ab781fbf7861c36b7750a0ba2710a34ade625122`
- implementation issue: #305
- implementation PR: #306
- exact validated implementation head: `00f608264bd40a9e24c073e99a10b6f5df121657`
- implementation Actions run: `37634048971` — success
- protected implementation merge: `e6a97fe9cf2ef4577f046c95f74f5eb690ba2e0e`
- implementation merge tree: zero file differences from the validated head
- audit issue: #307
- audit branch: `audit/a307`

## Release identity

- candidate version: `0.1.0-rc.1`
- candidate date: `2026-10-07`
- canonical source: LaTeX
- presentation artifact: PDF
- accessibility artifact: HTML
- public release authorized: **NO**

## Artifact hashes

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

The committed release manifest reproduces these hashes and records all 80 input chapter blob identities.

## Structural audit

PASS.

Protected replay reports:

- 80 canonical chapters;
- 126 hard dependency edges;
- one graph root;
- 80/80 chapters remain `draft-v0.1`;
- 18 registered/rendered figures;
- 85 sources;
- 175 bibliography keys;
- release-candidate checker green;
- no public-release authorization.

The canonical LaTeX contains exactly 80 chapter commands and 18 figure nodes.

The HTML contains 18 embedded images and 18 alt attributes derived from the existing descriptive captions.

## MECHDIAG treatment

PASS.

`ATLAS-CH-MECHDIAG-001` remains approximately 236 words and remains technically/documentarily adequate under AUDIT-047.

The release candidate presents it intentionally as:

**Interlude: From Readability to Functional Evidence**

No claim-strengthening or padding was introduced.

The readiness warning for its short length is therefore an acknowledged editorial characteristic, not a release-candidate defect.

## Rendering-aware copy edits

PASS.

The release tranche includes bounded source/presentation repairs needed for valid rendering:

- MAP arrow notation is made explicit;
- MAP non-implication notation is restored to `\not\Rightarrow`;
- SPLIT removes malformed escaped parentheses from mathematical function application;
- ADAPTDEPTH escapes underscores inside textual status labels;
- 26 legacy plain-text equation layouts that Pandoc would otherwise parse as Setext chapter headings are neutralized in the release conversion;
- 11 MAP legacy bracket-delimited displays are normalized for LaTeX output;
- figure paths are normalized for the canonical release source;
- the HTML conversion removes only Pandoc's PDF sizing wrapper around the 18 image nodes;
- figure captions are deterministically reused as HTML alt text.

These are rendering/copy-edit changes. The audit found no mathematical-claim promotion caused by them.

## Determinism

PASS.

The release build fixes:

`SOURCE_DATE_EPOCH=1791331200`

and uses a three-pass pdfLaTeX render.

Repeated execution of the promoted build path reproduced the same LaTeX/PDF/HTML SHA-256 values.

## Citation identity

PASS.

`CITATION.cff` binds:

- version `0.1.0-rc.1`;
- date `2026-10-07`;
- citation to the specific tagged release or commit used.

## Public-release boundary

PASS.

No `governance/RELEASE_AUTHORIZATION.yaml` authorizing public release exists.

No substantive public-release artifact exists under `releases/`.

The committed release manifest states:

`public_release_authorized: false`

The candidate artifacts are stored under `build/release-candidate/`, not the public-release directory.

Thus:

[
\text{audited release candidate}
\not\Rightarrow
\text{public release authorization}.
]

## Tag gate

PASS.

Before this audit, tag `atlas-v0.1.0-rc.1` was confirmed absent.

After this audit merges green, that candidate tag may be created at the exact protected implementation merge:

`e6a97fe9cf2ef4577f046c95f74f5eb690ba2e0e`

The tag is a release-candidate identity only and does not constitute a GitHub Release or public-release authorization.

## Final disposition

**AUDIT-076: PASS — NO REPAIR**, subject only to repository validation on the exact audit-record head before merge.
