# ATLAS-CW-INFO-001 — Information Witness

**Chapter:** `ATLAS-CH-INFO-001`  
**Runtime:** Wolfram Language service, 2026-10-02  
**Log base:** 2

## Purpose

Replay a small joint distribution whose mutual information is nonzero, compare it with deterministic dependence, and keep the causal interpretation separate.

## Correlated binary witness

Let

[
P_{XY}
=
\begin{pmatrix}
3/8&1/8\
1/8&3/8
end{pmatrix}.
]

Both marginals are

[
(1/2,1/2).
]

Wolfram evaluates

[
I(X;Y)
=
\frac{log(27/16)}{log 16}
approx
0.1887218755408671
]

bits.

The joint entropy is

[
H(X,Y)
approx
1.811278124459133
]

bits.

## Deterministic witness

For a fair binary variable with (Y=X),

[
P_{XY}
=
\begin{pmatrix}
1/2&0\
0&1/2
end{pmatrix},
]

Wolfram gives

[
I(X;Y)=1
]

bit.

Neither computation identifies a causal direction.

## Support failure

If

[
P=(1/2,1/2),
qquad
Q=(1,0),
]

then (P) assigns positive mass where (Q) assigns zero mass, so

[
D_{\rm KL}(P|Q)=infty.
]

## Claim boundary

This witness establishes exact information quantities for small declared probability models. It does not measure semantic meaning or causal influence.
