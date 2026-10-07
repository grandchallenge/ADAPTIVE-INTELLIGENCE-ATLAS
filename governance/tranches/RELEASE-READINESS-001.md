# RELEASE-READINESS-001 — Non-Promotional Release Readiness

## Status

Bounded release-readiness implementation record.

## Identity

- issue: #297
- protected baseline: `e22d9d383d048626797d7865bc7e9d3daebe1887`
- branch: `release-readiness/297`
- authority: documentary/infrastructure readiness only
- promotion authority: none

## Baseline

At launch:

- 14 Parts;
- 80 canonical ledger chapters;
- 80 chapters at `draft-v0.1`;
- 82 Markdown files under `manuscript/parts/`;
- 126 hard dependency edges;
- 18 rendered-witness figures;
- 85 registered sources;
- approximately 200,000 words in the 80 canonical chapter readers;
- `build/`: placeholder only;
- `releases/`: placeholder only;
- `LICENSE`: `LICENSE SELECTION PENDING`.

The two non-ledger manuscript files are preserved MECHDIAG historical/companion readers:

- `manuscript/parts/12-diagnostics-robustness-compression/_probe.md`;
- `manuscript/parts/12-diagnostics-robustness-compression/ATLAS-CH-DIAGREAD-001.md`.

They are not canonical release chapters.

## Finding 1 — release corpus was not mechanically defined

Before this tranche, a naive filesystem-based build would see 82 manuscript Markdown files for an 80-chapter Atlas.

That is unsafe because historical/companion material can be duplicated into a release artifact.

### Repair

`tools/assemble_manuscript.py` now defines the working manuscript assembly strictly from `governance/CHAPTER_LEDGER.yaml`, in ledger order.

The tool:

- requires unique canonical manuscript paths;
- requires all canonical paths under `manuscript/parts/`;
- requires every selected reader to exist;
- emits exactly one marker per ledger chapter;
- writes a machine-readable manifest containing chapter identity, Part identity, lifecycle state, path, and Git blob identity;
- marks the result as a **non-promotional working assembly**;
- records the source commit.

Generated build output is not committed as a release artifact by this tranche.

## Finding 2 — release-readiness boundary was not machine-enforced

The repository validator protects manuscript architecture and evidence integrity, but it did not enforce the separate release boundary.

### Repair

`tools/check_release_readiness.py` now checks:

- exactly 80 canonical chapters;
- all remain `draft-v0.1`;
- all canonical reader paths are unique, exist, and live under `manuscript/parts/`;
- the only non-ledger manuscript files are the two preserved MECHDIAG historical/companion files;
- `CITATION.cff` preserves required book and commit/tag citation metadata;
- `LICENSE_SELECTION_PENDING` remains explicit;
- no substantive file is committed under `releases/` while the license gate is active.

The check reports editorial maturity warnings but does not convert them into lifecycle promotion rules.

## Finding 3 — build and release directories lacked operating semantics

Both `build/` and `releases/` contained only `.gitkeep`.

### Repair

- `build/README.md` defines build output as generated, non-authoritative working material.
- `releases/README.md` defines release artifacts as governed outputs and records the license gate.

## Finding 4 — public phase wording lagged the repository state

The README still described global synthesis as the current phase after GLOBAL-SYNTHESIS-001 and AUDIT-073 had completed.

### Repair

The README now records the **release-readiness phase** while preserving:

- 80/80 `draft-v0.1`;
- no publication-ready/final-copy status;
- no mathematical certification;
- the explicit separate release-promotion boundary.

## Finding 5 — CI workflow title and coverage lagged the project phase

The sole workflow was still named `Validate Atlas architecture`.

### Repair

The workflow is renamed `Validate Atlas repository` and now executes:

1. `tools/validate_atlas.py`;
2. `tools/check_release_readiness.py`;
3. a deterministic 80-chapter working assembly to temporary paths.

This does not publish or retain a release artifact.

## Finding 6 — copy-edit maturity is not uniform

The canonical 80-reader corpus is approximately 200,000 words.

The median chapter is roughly 2,550 words. One chapter is a material length outlier:

- `ATLAS-CH-MECHDIAG-001`: approximately 236 words.

AUDIT-047 established that the mature companion is technically sufficient for its bounded claim and documentary role. That does not establish publication-length maturity.

### Disposition

No prose is expanded automatically.

A release-candidate transaction must explicitly adjudicate whether MECHDIAG should:

- remain intentionally concise;
- be expanded editorially without changing claims;
- be paired/presented with adjacent diagnostic material;
- or receive another documented editorial treatment.

This is an editorial judgment boundary, not a mathematical defect.

## Finding 7 — Markdown hard breaks are widespread and intentional-looking

A raw whitespace scan reports trailing spaces in many chapter readers. Inspection shows this overlaps the repository's established Markdown hard-break convention in status/metadata lines.

### Disposition

No mass whitespace rewrite is performed.

A final copy-edit pass may normalize style only with rendering-aware checks. Blind stripping would create needless provenance churn and may change Markdown rendering.

## Citation/version readiness

`CITATION.cff` presently supplies:

- CFF 1.2.0;
- book title;
- Grand Challenge Labs authorship;
- repository identity;
- explicit instruction to cite a specific tagged release or commit.

It does not yet supply a release version or release date.

### Disposition

No version/date is invented.

A release-promotion transaction must bind version/date/tag metadata to the exact protected release commit.

## Explicit governance gate — LICENSE_SELECTION_PENDING

Protected `LICENSE` states:

`LICENSE SELECTION PENDING`

and requires explicit license selection before public release of substantive manuscript content.

This tranche does not change that file.

The Human Steward must select and record the license before any public-release promotion.

## Release-readiness checklist

### Mechanically satisfied by this tranche

- [x] canonical release corpus is defined by Chapter Ledger, not filesystem enumeration;
- [x] deterministic 80-chapter working assembly exists;
- [x] machine-readable working manifest exists at build time;
- [x] canonical/noncanonical reader distinction is machine-checked;
- [x] citation metadata is machine-checked;
- [x] license gate is machine-checked;
- [x] committed public-release artifacts are prohibited while license selection is pending;
- [x] build/release directory semantics are documented;
- [x] repository CI includes release-readiness checks;
- [x] chapter lifecycle remains 80/80 `draft-v0.1`.

### Required before release-candidate promotion

- [ ] Human Steward selects and records repository license;
- [ ] editorial judgment on MECHDIAG publication maturity;
- [ ] rendering-aware full-corpus copy-edit;
- [ ] choose release format(s): Markdown bundle, PDF, HTML, EPUB, or explicitly scoped subset;
- [ ] select release version/tag;
- [ ] bind `CITATION.cff` version/date to exact release tag/commit;
- [ ] generate final build artifact(s) from the ledger-driven assembly;
- [ ] verify internal links, figures, equations, references, and typography in each chosen rendered format;
- [ ] produce release manifest with exact hashes;
- [ ] execute a separate release-candidate audit;
- [ ] Human Steward authorizes public release.

## Promotion boundary

RELEASE-READINESS-001 does not:

- alter the repository license;
- create a public release;
- promote any chapter beyond `draft-v0.1`;
- certify any mathematical result;
- establish publication-ready or final-copy status.

Its purpose is to make the remaining release boundary explicit, deterministic, and testable.
