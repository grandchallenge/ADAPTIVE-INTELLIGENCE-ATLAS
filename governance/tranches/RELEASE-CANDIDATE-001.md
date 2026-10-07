# RELEASE-CANDIDATE-001 — Canonical LaTeX / PDF / HTML

## Status

Implementation candidate prepared from protected baseline:

`ab781fbf7861c36b7750a0ba2710a34ade625122`

Issue: #305

Version identity:

- version: `0.1.0-rc.1`
- release-candidate date: `2026-10-07`
- public release authorized: **NO**

## Human Steward release architecture

- LaTeX is the canonical source of truth.
- PDF is the primary presentation artifact.
- HTML is the broader-accessibility artifact.
- PDF and HTML are generated from the exact canonical LaTeX source and are not independent editorial sources.

## MECHDIAG editorial decision

`ATLAS-CH-MECHDIAG-001` remains intentionally concise and is presented as:

**Interlude: From Readability to Functional Evidence**

The chapter retains its stable identity and downstream handoff. No padding was added merely to match neighboring chapter lengths.

## Canonical source and artifacts

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

Exact input identities, toolchain metadata, and all 80 chapter blob identities are recorded in:

`build/release-candidate/v0.1.0-rc.1/release-manifest.json`

## Structural validation

- canonical chapters: 80
- canonical LaTeX chapter commands: 80
- registered/rendered figures: 18
- HTML embedded images: 18
- HTML image alt attributes: 18
- undefined LaTeX references after stabilization: 0
- unresolved rerun signal after stabilization: 0
- public-release authorization object: absent
- substantive artifacts under `releases/`: absent

## Deterministic rendering

PDF rendering is pinned with:

`SOURCE_DATE_EPOCH=1791331200`

and three pdfLaTeX passes.

An additional same-input replay reproduced the exact PDF SHA-256. The promoted one-command build was then executed twice and reproduced the same LaTeX/PDF/HTML hashes on both runs.

Release build dependency:

`pypandoc_binary==1.17`

which supplies Pandoc `3.9` in the validated environment.

The validated PDF renderer reports pdfTeX `3.141592653-2.6-1.40.22` from TeX Live 2022/dev/Debian.

## Rendering-aware normalizations

The release builder performs bounded presentation normalizations without changing mathematical claims:

1. 26 legacy plain-text equation layouts that Pandoc 3.9 would otherwise misread as Setext H1 headings are neutralized; only the three affected chapters are touched by this normalization (`DEPTH`, `RLBASE`, `EVIDEX`).
2. 11 legacy standalone bracket-delimited TeX display blocks in the MAP reader are emitted as explicit raw-LaTeX displays.
3. three literal `\nRightarrow` drafting typos in MAP are rendered as `\not\Rightarrow`.
4. `Alongrightarrow B.` and `Aleftrightarrow B.` in MAP are rendered as `A \longrightarrow B.` and `A \leftrightarrow B.`.
5. the 18 figure paths are normalized for the canonical repository-root release source.
6. the HTML reader strips only Pandoc’s PDF sizing wrapper around the 18 `\includegraphics` nodes; the canonical LaTeX remains unchanged.
7. each HTML image receives alt text deterministically from its existing descriptive figure caption.

These transformations are encoded in the committed release tooling and are checked by `tools/check_release_candidate.py`.

## Citation identity

`CITATION.cff` is bound to:

- version `0.1.0-rc.1`
- date `2026-10-07`

The citation message continues to require citation of the specific tagged release or commit used.

## Release boundary

This transaction creates a governed release candidate only.

It does **not**:

- authorize a public GitHub release;
- set `public_release_authorized: true`;
- promote chapters beyond `draft-v0.1`;
- confer mathematical certification;
- claim final-copy status beyond the exact audited candidate.

After implementation merge, a fresh release-candidate audit is mandatory before the candidate tag may be considered protected evidence.

