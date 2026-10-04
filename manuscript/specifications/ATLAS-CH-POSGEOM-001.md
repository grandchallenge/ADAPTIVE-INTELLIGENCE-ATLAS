# Chapter Specification — ATLAS-CH-POSGEOM-001

## Identity

**Title:** The Geometry of Position  
**Part:** Attention, Sequence, and Position  
**Status:** specification-ready.  
**Epistemic class:** audited attention/geometry prerequisites + primary positional-encoding sources + Atlas synthesis.

## Chapter contract

Develop positional information as explicit geometry acting on attention representations.

Cover:

- additive sinusoidal position;
- rotary position embedding as block rotations;
- the exact relative-offset identity in query-key inner products;
- frequency allocation and phase;
- multidimensional position as a product of coordinate-wise rotation groups;
- context-window interpolation/extrapolation methods as separate empirical interventions;
- the boundary between positional algebra and long-context model quality.

## Hard prerequisites

- ATLAS-CH-ATTNOP-001;
- ATLAS-CH-GEOM-001.

May inherit from ATTNOP:

- query/key/value and score/operator notation;
- permutation equivariance in the absence of positional asymmetry;
- state-dependent attention operator semantics.

May inherit from GEOM:

- orthogonal rotations;
- invariance discipline;
- exact geometric versus heuristic analogy boundaries.

## Absolute sinusoidal encoding

The original Transformer uses additive sine/cosine features of geometrically spaced frequencies.

For one frequency omega, represent position m by

p_m(omega) =
[ sin(m omega), cos(m omega) ]^T.

A fixed offset delta acts linearly on this 2-vector by a rotation.

This exact trigonometric fact motivates relative-offset accessibility, but additive positional features and RoPE are not the same mechanism.

## Rotary block

Define

R(phi) =
[[cos(phi), -sin(phi)],
 [sin(phi),  cos(phi)]].

For frequency omega and position m,

R_m(omega)=R(m omega).

Apply blocks to queries and keys before the dot product.

Orthogonality gives

R_m(omega)^T R_n(omega)
=
R((n-m)omega).

Hence for 2D query/key subvectors q,k,

(R_m q)^T (R_n k)
=
q^T R((n-m)omega) k.

The transformed dot product depends on relative offset n-m through the rotation block.

## Multi-frequency form

For d even, use block-diagonal rotations

R_m =
diag(
R(m omega_1),
...,
R(m omega_(d/2))
).

Then

R_m^T R_n
=
R_(n-m)

blockwise.

The frequency schedule is part of the positional design.

## Exact witness

Choose theta=pi/6 and q=k=(1,0)^T.

For positions (m,n)=(0,2),

score = cos(2 theta)=1/2.

For positions (m,n)=(3,5),

score = cos(2 theta)=1/2.

The absolute positions differ but the relative offset is the same.

## Non-orthogonal control

Replace rotations by

S_m=diag(2^m,1).

With q=k=(1,0)^T,

(S_m q)^T(S_n k)=2^(m+n).

Then equal-offset pairs give:

(m,n)=(0,2): score=4;

(m,n)=(3,5): score=256.

So equal relative offset no longer determines the score.

The witness isolates the load-bearing group/orthogonality structure.

## Generic-vector replay

With theta=pi/6,

q=(1,2)^T,

k=(3,-1)^T,

m=2,

n=5,

both

(R_m q)^T(R_n k)

and

q^T R((n-m)theta)k

evaluate exactly to 7.

## Multidimensional position

For 2D coordinate p=(u,v), define

R_p =
diag(
R(u omega_x),
R(v omega_y)
).

Then

R_p^T R_q
=
R_(q-p)

coordinate-wise.

This gives an exact product-group construction for multidimensional relative position.

A 2D positional method is not justified merely by duplicating a 1D scalar index; the coordinate action must be declared.

## Context extension

Distinguish:

1. direct extrapolation beyond the trained positional range;
2. index interpolation/rescaling into the trained range;
3. frequency/base scaling;
4. fine-tuning on longer contexts;
5. combinations such as YaRN.

Position Interpolation and YaRN are paper-scoped methods with empirical/theoretical evidence under their stated settings.

Do not turn them into universal guarantees of long-context reliability.

## Long-context boundary

The exact algebraic identity

R_m^T R_n=R_(n-m)

does not by itself imply:

- stable attention logits at arbitrary lengths;
- preserved task quality;
- preserved calibration;
- preserved retrieval;
- preserved optimization behavior.

These are model-level empirical questions.

## Failure boundaries

Include:

- additive sinusoidal encoding != rotary encoding;
- relative-phase identity != universal extrapolation guarantee;
- rotation-block orthogonality != arbitrary positional transform;
- frequency schedule != context-scaling policy;
- one-dimensional position != multidimensional geometry;
- index interpolation != frequency scaling;
- positional geometry != semantic/content geometry;
- empirical context-extension success != theorem;
- RoPE vector formulation != downstream Relative-Position Operator decomposition.

## Downstream handoff

Direct consumer:

- ATLAS-CH-RPO-001.

RPO may inherit:

- block-rotation notation;
- exact relative-offset identity;
- multi-frequency decomposition;
- multidimensional product-group construction;
- explicit separation between algebraic positional structure and empirical long-context behavior.

RPO must independently justify frequency modes, DC components, low-dimensional operator reduction, and head specialization.

## Sources

- [@VaswaniEtAl2017]
- [@SuEtAl2021RoFormer]
- [@ChenEtAl2023PositionInterpolation]
- [@PengEtAl2023YaRN]

Source lock:

sources/source-locks/ATLAS-CH-POSGEOM-001.yaml
