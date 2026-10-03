# NETNUM-001 — Networks as Numerical Schemes

## Identity

- chapter: `ATLAS-CH-NETNUM-001`;
- implementation issue: #103;
- drafting baseline: `58da49a2f2969de687cbfd247e488997e57b05d6`;
- work branch: `work/netnum-001`;
- hard prerequisites:
  - `ATLAS-CH-NUMERICS-001` at audited `draft-v0.1`;
  - `ATLAS-CH-ARCHHIST-001` at audited `draft-v0.1`.

## Objective

Promote NETNUM-001 from architecture to a complete `draft-v0.1` chapter that uses numerical-analysis language only when a residual architecture is bound to a declared continuous reference and refinement family.

## Exact prerequisite binds

- NUMERICS manuscript blob:
  `a719a16e86d1feb76679e1f1cda2d9d3393d2e42`;
- AUDIT-009 blob:
  `2bbb1b7687d6c4b8c0bfeed5206de836dac92dca`;
- ARCHHIST manuscript blob:
  `3d373695ed5516dbc3b0557112f204636e911897`;
- AUDIT-010 blob:
  `c9aa1488b5041805e4695f00f462f3773a27dedf`.

## External bridge sources

- Haber and Ruthotto, Stable Architectures for Deep Neural Networks;
- Lu et al., Beyond Finite Layer Neural Networks.

The already locked ResNet and Neural ODE sources are inherited through ARCHHIST.

## Central doctrine

Residual syntax opens a numerical lens but does not itself establish:

- an underlying ODE;
- a time mesh;
- local truncation error;
- global convergence;
- a stability theorem;
- time reversibility.

Those claims require the corresponding numerical objects.

## Exact witness

Reference flow:

`x'=-x`, `x(0)=1`.

Euler/residual step:

`x_{k+1}=(1-h)x_k`.

The witness records:

- stability interval `0<=h<=2`;
- unstable factor `-2` at `h=3`;
- refinement values at `N=2,4,8`;
- exact continuous value `e^{-1}`;
- invertible forward step at `h=1/2`;
- non-reversible round trip `3/4`.

## Durable artifacts

- `sources/source-locks/ATLAS-CH-NETNUM-001.yaml`;
- `manuscript/specifications/ATLAS-CH-NETNUM-001.md`;
- `mathematics/derivations/ATLAS-CH-NETNUM-001-DERIVATIONS.md`;
- `mathematics/computational-witnesses/ATLAS-CW-NETNUM-001.md`;
- `manuscript/parts/07-numerical-intelligence/ATLAS-CH-NETNUM-001.md`;
- Chapter Ledger promotion;
- Source Register entry;
- bibliography updates.

## Remaining transaction work

Repository validation, implementation merge, bounded post-draft audit, audit validation/merge, issue closure verification, frontier recomputation, and controller reset remain mandatory.
