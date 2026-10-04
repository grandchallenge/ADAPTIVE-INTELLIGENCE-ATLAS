# Computational Witness — ATLAS-CW-POSGEOM-001

## Purpose

Replay the exact finite positional-geometry identities used by ATLAS-CH-POSGEOM-001.

This is an algebraic witness, not an empirical long-context benchmark.

## W1. Same relative offset under rotary position

Let

theta=pi/6,

q=k=(1,0)^T.

For a position m, use

R_m=R(m theta).

Pair A:

m=0,
n=2.

Then

(R_0 q)^T(R_2 k)
=
cos(2 theta)
=
cos(pi/3)
=
1/2.

Pair B:

m=3,
n=5.

Then

(R_3 q)^T(R_5 k)
=
cos((5-3)theta)
=
1/2.

The absolute positions differ.

The relative offset is 2 in both pairs.

The score is identical.

## W2. Different offset

Take

m=1,
n=4.

Then n-m=3, so

score
=
cos(3 theta)
=
cos(pi/2)
=
0.

The witness is sensitive to relative offset.

## W3. Generic-vector replay

Let

q=(1,2)^T,

k=(3,-1)^T,

m=2,

n=5.

Because

(n-m)theta
=
3 pi/6
=
pi/2,

R(pi/2)k=(1,3)^T.

Therefore

q^T R(pi/2)k
=
(1,2) dot (1,3)
=
7.

Direct evaluation of

(R_2 q)^T(R_5 k)

also gives 7.

## W4. Non-orthogonal control

Define

S_m=diag(2^m,1).

For q=k=(1,0)^T,

(S_m q)^T(S_n k)=2^(m+n).

Same-offset pair A:

(0,2) -> 2^2 = 4.

Same-offset pair B:

(3,5) -> 2^8 = 256.

Thus equal relative offset no longer determines the transformed inner product.

## W5. Translation replay

For rotary blocks,

R_(m+c)^T R_(n+c)
=
R_(n-m).

Use the first pair and shift both positions by c=7:

(0,2) -> (7,9).

The score remains

cos(2 theta)=1/2.

This is the exact common-translation invariance of the rotary score contribution.

## W6. Multidimensional product action

Let a 2D position be p=(u,v).

Use two independent 2D blocks:

R_p =
diag(
R(u pi/2),
R(v pi/3)
).

For positions

p=(1,2),

q=(3,5),

the relative displacement is

q-p=(2,3).

Therefore

R_p^T R_q
=
diag(
R(pi),
R(pi)
)
=
-I_4.

If both positions are translated by c=(4,-1),

p'=(5,1),

q'=(7,4),

the relative displacement remains (2,3), so the relative operator remains -I_4.

## W7. Interpolation phase map

Let original context scale be L and target context scale L'=4L.

Position Interpolation maps

m -> m/4

in the positional coordinate.

A rotary phase m omega becomes

(m/4) omega.

This replay demonstrates only the coordinate transformation.

It does not test a trained model's quality.

## Replay table

| Check | Exact result |
| --- | --- |
| rotary score, (0,2) | 1/2 |
| rotary score, (3,5) | 1/2 |
| rotary score, (1,4) | 0 |
| generic-vector score | 7 |
| non-orthogonal score, (0,2) | 4 |
| non-orthogonal score, (3,5) | 256 |
| shifted rotary pair, (7,9) | 1/2 |
| 2D relative operator | -I_4 |

## Claim boundary

This witness proves only:

1. the declared finite rotary identities;
2. same-offset equality for the chosen rotary block;
3. common-translation invariance of the rotary score contribution;
4. failure of same-offset dependence for the chosen non-orthogonal control;
5. the direct-product multidimensional identity;
6. the coordinate rescaling used in the interpolation illustration.

It does not prove model-level long-context generalization, retrieval quality, calibration, or training stability.
