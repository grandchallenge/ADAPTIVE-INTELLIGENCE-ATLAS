# Canonical LaTeX release sources

## Public release v0.1.0

The canonical editorial source for the first governed public release is:

`manuscript/latex/atlas-v0.1.0.tex`

It is byte-identical to the independently audited release-candidate source:

`manuscript/latex/atlas-v0.1.0-rc.1.tex`

SHA-256:

`0d636871e6875bbadbd244e54bf272fdefe2dbd5179515d9d22d3a25e49c384a`

The final PDF and HTML artifacts are byte-preserving promotions of the audited candidate outputs. They must not be edited independently to create content differences.

## Provenance

The Chapter Ledger and Markdown chapter corpus remain the governed provenance/input substrate from which the canonical LaTeX source was constructed. The RC source remains preserved as the exact audited predecessor.

Release-candidate reproducibility remains available through:

`bash tools/build_release_candidate.sh`

Public-release authorization and exact final artifact identities are recorded in `governance/RELEASE_AUTHORIZATION.yaml` and `releases/v0.1.0/release-manifest.json`.

Publication does not imply mathematical certification; claim/evidence/provenance distinctions remain those of the governed Atlas corpus.
