# ATLAS-CW-REP-001 — Representation Witness

**Chapter:** `ATLAS-CH-REP-001`  
**Runtime:** Wolfram Language service, 2026-10-02

## Purpose

Replay one exact invariance example, one exact equivariance example, and one invertible recoding that preserves a linear readout.

## Reflection action

Let

[
G=
egin{pmatrix}
-1&0\
0&1
end{pmatrix},
qquad
x=(2,3).
]

Then

[
Gx=(-2,3).
]

For the scalar representation

[
r_{m inv}(x)=|x|_2^2,
]

Wolfram gives

[
r_{m inv}(x)
=
r_{m inv}(Gx)
=
13.
]

For the identity representation (r(x)=x),

[
r(Gx)=G,r(x),
]

so it is equivariant under the declared reflection representation.

## Invertible recoding

Let

[
T=
egin{pmatrix}
1&1\
0&1
end{pmatrix},
qquad
z=(2,3),
qquad
w=(4,-1).
]

The original readout is

[
w^	op z=5.
]

Define

[
	ilde z=Tz=(5,3),
]

and

[
	ilde w=T^{-	op}w=(4,-5).
]

Then

[
	ilde w^	op	ilde z=5.
]

This demonstrates exact task-preserving recoding for this declared linear readout.

## Claim boundary

The witness establishes invariance/equivariance and readout-preserving invertible recoding in a two-dimensional toy system. It does not establish semantic equivalence for arbitrary downstream tasks or identifiability of learned latent factors.
