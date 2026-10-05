# Computational Witness — ATLAS-CW-COMPRESS-001

## Purpose

Replay the exact finite coding examples used by ATLAS-CH-COMPRESS-001.

## W1. Exact dense versus rank-one code

Let u=v=(1,1,1,1)^T and W=uv^T.

Then W is the 4 by 4 all-ones matrix.

Declared codec:
- shape is known;
- payload entries are binary;
- one format bit identifies dense or rank-one encoding.

Dense representation:
- one format bit;
- sixteen matrix-entry bits;
- total 17 bits.

Rank-one representation:
- one format bit;
- four bits for u;
- four bits for v;
- total 9 bits.

Both decode to exactly the same matrix W.

For every x,

Wx=u(v^T x).

## W2. Low-rank control

Let A=diag(4,3,1).

Rank-one truncated approximation:

A1=diag(4,0,0).

Squared Frobenius error:

||A-A1||_F^2=10.

Rank-two truncated approximation:

A2=diag(4,3,0).

Squared Frobenius error:

||A-A2||_F^2=1.

## W3. Pruning control

Let w=(1,1/8)^T and x=(0,8)^T.

Original output:

w^T x=1.

After removing the second component by threshold 1/4:

w_reduced=(1,0)^T,

and

w_reduced^T x=0.

## W4. Fixed-grid quantization

Let w=(1/4,1/2,1/2,1/4).

Use the fixed grid

{0,1/4,1/2,3/4}.

All four values are represented exactly.

With four raw 8-bit values:

32 bits.

With four 2-bit fixed-grid indices:

8 bits.

Parameter error is zero.

## W5. Weight sharing

Store two 8-bit centroids:

{1/4,1/2}.

Store four one-bit indices.

Total:

16+4=20 bits.

The four connections remain present.

## W6. Two-part description accounting

Declare:

L(H_A)=3,
L(H_B)=7,

and

L(D|H_A)=L(D|H_B)=5.

Then

L(H_A,D)=8,

L(H_B,D)=12.

Under this declared code, H_A has the shorter total description.

## Replay table

| Check | Exact result |
| --- | --- |
| dense code | 17 bits |
| rank-one code | 9 bits |
| exact map equality | W=uv^T |
| rank-one control error squared | 10 |
| rank-two control error squared | 1 |
| original threshold-control output | 1 |
| reduced output | 0 |
| fixed-grid payload | 8 bits |
| fixed-grid parameter error | 0 |
| shared-centroid payload | 20 bits |
| total code for H_A | 8 bits |
| total code for H_B | 12 bits |

## Claim boundary

This witness proves only the declared finite arithmetic under the declared codecs and domains.

It does not establish a universal codec, universal model-quality preservation, interpretability, or intelligence.
