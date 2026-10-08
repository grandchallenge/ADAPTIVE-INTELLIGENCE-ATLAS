# A Mathematical Atlas of Adaptive Intelligence

**Status:** public `v0.1.0` initial-draft release; comprehensive editorial review in progress (issue #314)
**Repository:** `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`
**Bootstrap record:** https://github.com/grandchallenge/.github/issues/99

A Grand Challenge Labs monograph on geometry, operators, dynamics, optimization, composition, memory, coordination, diagnostics, and governed adaptation.

This repository is intended to be a first-class GCL research-publication surface. It is not itself a mathematical certification authority and it does not replace `INTELLECT`, `gcl-standards`, `AETHER`, or the MATHFORGE → MATHSOLVE → MATHCERT pipeline.

## Current manuscript state

The Atlas contains 14 Parts and 80 stable chapter identities. The protected Chapter Ledger records all 80 chapters at `draft-v0.1` and none at `architecture`.

The first bounded full-manuscript global-synthesis pass, release-readiness tranche, and release-candidate tranche are complete and independently audited. `v0.1.0` is the first governed public release: LaTeX is the canonical source of truth, PDF is the primary presentation artifact, and HTML is the broader-accessibility artifact.

Public release does not promote any chapter beyond `draft-v0.1` and does not imply mathematical certification. Claim/evidence status, source locks, witness provenance, and audit boundaries remain authoritative.

## Composition method

`architecture -> dependency graph -> keystone chapters -> six-keystone synthesis -> chapter families -> global synthesis -> release readiness -> audited release candidate -> governed public release`

Core editorial artifacts:

1. `governance/ATLAS_MAP.md`
2. `governance/CHAPTER_LEDGER.yaml`
3. `governance/MATHEMATICAL_LEXICON.yaml`
4. `governance/FIGURE_REGISTER.yaml`
5. `governance/SOURCE_REGISTER.yaml`

## Working manuscript assembly

Canonical manuscript membership and order come from `governance/CHAPTER_LEDGER.yaml`, not by enumerating every Markdown file under `manuscript/parts/`.

Use:

`python tools/assemble_manuscript.py`

to produce a non-promotional working assembly and manifest under `build/`.

## Pedagogical rule

Imaginative work and mathematical rigor are complementary. The default allegory discipline is:

`allegory -> structural correspondence -> mathematics -> limits of allegory`

Figures are part of the reasoning. A computationally rendered image must preserve its generator provenance and distinguish literal from nonliteral semantics.

## Licensing and release boundary

Repository licensing is selected and scoped:

- CC BY 4.0 for manuscript, exposition, documentation, figures, and other non-software publication material;
- MIT for software and executable tooling;
- file-specific notices and third-party rights take precedence.

Copyright © 2026 Grand Challenge Technologies Ltd.

See `LICENSE` and `LICENSES/` for the governing scope and standard license texts.

Public release `v0.1.0` is explicitly authorized under `governance/RELEASE_AUTHORIZATION.yaml` and is a byte-preserving promotion of the independently audited `atlas-v0.1.0-rc.1` candidate. Exact release artifacts, hashes, and notes are under `releases/v0.1.0/`. Publication preserves the Atlas source, witness, audit, citation, artifact-hash, rendering, and mathematical-certification boundaries.
