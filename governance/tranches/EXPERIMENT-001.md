# EXPERIMENT-001 — Experiments as Arguments

## Identity

- chapter: `ATLAS-CH-EXPERIMENT-001`;
- implementation issue: #96;
- drafting baseline: `55085755626d60d2981a7cf17a6af7cbac60f9fc`;
- work branch: `work/experiment-001`;
- hard prerequisite:
  - `ATLAS-CH-EVIDENCE-001` at audited `draft-v0.1`.

## Objective

Promote EXPERIMENT-001 from architecture to a complete `draft-v0.1` chapter that treats experiments as bounded evidentiary arguments rather than metric-producing runs.

## Source lock

The tranche binds:

- audited Evidence manuscript blob `17eaa9caf90ede47c74dccff052f93d9fb3d901e`;
- Evidence audit blob `6af518de0687a9cd8fe5635e2fba8f6a6271c77c`;
- NIST DOE guidance;
- Rubin (1974) on causal treatment effects and randomization/nonrandomized control;
- ASA p-value statement;
- NASEM reproducibility/replication report;
- Henderson et al. (2018) as representative ML/RL variance and reporting evidence.

No downstream Replay chapter content is used as prerequisite authority.

## Formal object

The chapter introduces

`E = (q, theta, U, A, Z, Y, g, V, rho, Omega)`

for claim, estimand, units/population, intervention/assignment, nuisance structure, outcome, comparison rule, uncertainty/variation, stopping/selection/reporting rule, and interpretation scope.

## Exact witness

A deterministic 20-unit two-stratum table has individual treatment effect +1 for every unit.

Imbalanced assignment produces:

- naive aggregate contrast: -7;
- easy-stratum contrast: +1;
- hard-stratum contrast: +1;
- equal-stratum standardized contrast: +1.

The witness proves only this finite confounding reversal.

## Artifacts

- `sources/source-locks/ATLAS-CH-EXPERIMENT-001.yaml`;
- `manuscript/specifications/ATLAS-CH-EXPERIMENT-001.md`;
- `mathematics/derivations/ATLAS-CH-EXPERIMENT-001-DERIVATIONS.md`;
- `mathematics/computational-witnesses/ATLAS-CW-EXPERIMENT-001.md`;
- `manuscript/parts/14-scientific-method-governed-adaptation/ATLAS-CH-EXPERIMENT-001.md`;
- `governance/CHAPTER_LEDGER.yaml`;
- `governance/SOURCE_REGISTER.yaml`;
- `sources/bibliography.bib`.

## Tranche state

Implementation artifacts written on the work branch.

Validation, implementation PR merge, and bounded post-draft audit remain part of this same transaction and must complete before the controller returns to `idle-ready`.
