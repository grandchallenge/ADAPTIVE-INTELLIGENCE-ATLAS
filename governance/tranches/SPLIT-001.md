# SPLIT-001 — Split-Operator Networks

## Identity

- chapter: `ATLAS-CH-SPLIT-001`
- issue: #141
- baseline: `b87bad6229896174e6c872994d6a0f4878e2e1d5`
- branch: `work/split-001`
- hard prerequisites:
  - `ATLAS-CH-NUMERICS-001`
  - `ATLAS-CH-TRANSFORMER-001`

Exact prerequisite binds:

- NUMERICS manuscript: `a719a16e86d1feb76679e1f1cda2d9d3393d2e42`
- AUDIT-009: `2bbb1b7687d6c4b8c0bfeed5206de836dac92dca`
- NUMERICS source lock: `7feea1c8ca3026fa1f61f35b87281b4afe9ccd8d`
- TRANSFORMER manuscript: `197b74ffd40fe54b79ca15ab731b73538aada494`
- AUDIT-011: `e8bfa9b062b4b80bd0cccd49f168f99c40843f71`
- TRANSFORMER source lock: `dec885c68a9afb439aed9af5ca35b998519722bc`

## Source-lock phase

Source lock created on branch at commit:

`7a32a7b801d66a0fd79c9a8e903059f7ca96c22c`.

The external theory is intentionally narrow:

- McLachlan–Quispel for splitting/composition;
- Hairer–Lubich–Wanner for geometric/symmetric composition boundaries;
- Vaswani et al. for baseline Transformer sublayer anatomy.

The neural split-operator interpretation is Atlas synthesis, not imported theorem authority.

## Core objects

- exact subflows `exp(hA)`, `exp(hB)`;
- Lie orderings `S_AB`, `S_BA`;
- commutator `[A,B]=AB-BA`;
- Strang composition `exp(hA/2)exp(hB)exp(hA/2)`;
- learned neural submaps `Psi_A`, `Psi_B`;
- additive versus sequential residual composition;
- shared versus layer-varying suboperators;
- explicit error taxonomy.

## Exact witness

\[
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]

Then:

- `A^2=B^2=0`;
- `[A,B]=diag(1,-1)`;
- `S_AB-S_BA=h^2[A,B]` exactly;
- `S_AB-exp(h(A+B))=(h^2/2)[A,B]+O(h^3)`;
- reversed order flips the leading sign;
- Strang local defect is `O(h^3)` in the exact witness;
- commuting diagonal control gives exact order independence.

At `h=1/2`:

- Lie Frobenius error: approximately `0.1793148493970293`;
- Strang Frobenius error: approximately `0.02370487546729764`.

These numeric values are witness checkpoints only.

## Durable distinctions

- exact flow versus learned residual map;
- additive versus sequential composition;
- order dependence versus commutation;
- Lie first-order versus Strang symmetric second-order under assumptions;
- symmetric ordering versus exact invertibility;
- shared/autonomous versus layer-varying/nonautonomous operators;
- splitting error versus approximation/estimation/optimization/implementation error;
- local commutator diagnostic versus global theorem.

## Artifact set

- `sources/source-locks/ATLAS-CH-SPLIT-001.yaml`;
- `manuscript/specifications/ATLAS-CH-SPLIT-001.md`;
- `mathematics/derivations/ATLAS-CH-SPLIT-001-DERIVATIONS.md`;
- `mathematics/computational-witnesses/ATLAS-CW-SPLIT-001.md`;
- `manuscript/parts/04-neural-architectures/ATLAS-CH-SPLIT-001.md`;
- `governance/CHAPTER_LEDGER.yaml`;
- `governance/SOURCE_REGISTER.yaml`;
- this tranche receipt.

## Remaining gates

Repository validation, implementation PR, protected merge, bounded post-draft audit, all in-scope repairs, audit validation/merge, issue closure, frontier recomputation, controller reset.
