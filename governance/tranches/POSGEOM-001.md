# POSGEOM-001 — The Geometry of Position

## Identity

- chapter: ATLAS-CH-POSGEOM-001
- implementation issue: #159
- protected baseline: df99382bf263423fea72bcf75d2d222c19112031
- work branch: work/atlas-159
- hard prerequisites:
  - ATLAS-CH-ATTNOP-001
  - ATLAS-CH-GEOM-001

## Exact prerequisite binds

Attention:
- manuscript: d6fa97fbbd1a2410055ca2cd4bc034ca54ccd26c
- source lock: 4af4e53230776daaf0be825cffd1263957ed97c8
- AUDIT-002: 4671995f0cd7465a5df2bb60431244f482e5e3c9

Geometry:
- manuscript: f8e406f24a01bd852996e11118e04427ff549f35
- source lock: d75e8bcf5a5920eca6b09cb8bb181182c7827b5c
- AUDIT-001: f13b7ac01f7b10dfadd64da6f31c45832344c082

## External source set

- Vaswani et al. (2017), Attention Is All You Need.
- Su et al. (2021), RoFormer: Enhanced Transformer with Rotary Position Embedding.
- Chen et al. (2023), Extending Context Window of Large Language Models via Positional Interpolation.
- Peng et al. (2023), YaRN: Efficient Context Window Extension of Large Language Models.

## Core exact objects

For a 2D rotation block

R(phi)=[[cos(phi),-sin(phi)],[sin(phi),cos(phi)]],

the position-indexed family

R_m=R(m omega)

satisfies

R_m^T R_n=R((n-m)omega).

Therefore

(R_m q)^T(R_n k)=q^T R((n-m)omega)k.

## Exact witness

theta=pi/6,
q=k=(1,0)^T.

Same-offset pairs:
- (0,2) -> score 1/2.
- (3,5) -> score 1/2.

Different offset:
- (1,4) -> score 0.

Generic-vector replay:
- q=(1,2)^T;
- k=(3,-1)^T;
- m=2, n=5;
- direct and relative forms both equal 7.

## Non-orthogonal control

S_m=diag(2^m,1).

With q=k=(1,0)^T:
- (0,2) -> 4.
- (3,5) -> 256.

Thus equal relative offset does not determine the transformed score without the required group/orthogonality relation.

## Multidimensional replay

For p=(u,v),

R_p=diag(R(u omega_x),R(v omega_y)).

Then

R_p^T R_q

depends on the coordinate-wise displacement q-p.

## Durable boundaries

- additive sinusoidal encoding != rotary encoding;
- exact relative phase != universal long-context generalization;
- orthogonal rotation family != arbitrary position-dependent transform;
- frequency schedule != context-extension policy;
- index interpolation != frequency scaling;
- one-dimensional position != multidimensional geometry;
- positional algebra != full-model behavior;
- RoPE vector formulation != downstream Relative-Position Operator theory.

## Artifact set

- sources/source-locks/ATLAS-CH-POSGEOM-001.yaml
- sources/bibliography.bib
- manuscript/specifications/ATLAS-CH-POSGEOM-001.md
- mathematics/derivations/ATLAS-CH-POSGEOM-001-DERIVATIONS.md
- mathematics/computational-witnesses/ATLAS-CW-POSGEOM-001.md
- manuscript/parts/05-attention-sequence-position/ATLAS-CH-POSGEOM-001.md
- governance/CHAPTER_LEDGER.yaml
- governance/SOURCE_REGISTER.yaml
- this receipt

## Remaining gates

Canonical validation, implementation merge, bounded post-draft audit, in-scope repairs, audit validation/merge, issue closure, fresh frontier recomputation, and controller reset.
