# A Mathematical Atlas of Adaptive Intelligence

**Status:** full first-draft corpus; release-readiness phase
**Repository:** `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`
**Bootstrap record:** https://github.com/grandchallenge/.github/issues/99

A Grand Challenge Labs monograph on geometry, operators, dynamics, optimization, composition, memory, coordination, diagnostics, and governed adaptation.

This repository is intended to be a first-class GCL research-publication surface. It is not itself a mathematical certification authority and it does not replace `INTELLECT`, `gcl-standards`, `AETHER`, or the MATHFORGE → MATHSOLVE → MATHCERT pipeline.

## Current manuscript state

The Atlas contains 14 Parts and 80 stable chapter identities. The protected Chapter Ledger records all 80 chapters at `draft-v0.1` and none at `architecture`.

The first bounded full-manuscript global-synthesis pass is complete and independently audited. The current project phase is non-promotional release readiness: deterministic manuscript assembly, build/copy-edit planning, citation/version preparation, packaging controls, and explicit release gates.

This phase does not itself promote any chapter beyond `draft-v0.1` and does not imply publication readiness, certification, final-copy status, or public-release authorization.

## Composition method

`architecture -> dependency graph -> keystone chapters -> six-keystone synthesis -> chapter families -> global synthesis -> release readiness`

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

## Release boundary

The repository license remains explicitly unresolved. No public release of substantive manuscript content is authorized until the Human Steward selects and records the repository license.

Any release-candidate or publication promotion is a separate governed transaction and must preserve the Atlas source, witness, audit, citation, artifact-hash, and authority boundaries.
