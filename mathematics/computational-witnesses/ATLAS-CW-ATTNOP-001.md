# ATLAS-CW-ATTNOP-001 — Attention Operator Witness

**Chapter:** `ATLAS-CH-ATTNOP-001`  
**System:** Wolfram Language 15.0.1 for Linux x86 (64-bit), July 2 2026  
**System ID:** Linux-x86-64  
**Figure source:** `figures/wolfram/ATLAS-FIG-ATTNOP-001.wl`

## Purpose

Reconstruct one attention head as four explicit objects:

[
S,qquad A=operatorname{softmax}_{m row}(S),qquad V,qquad Y=AV.
]

## Parameters

[
Q=K=
egin{pmatrix}
1&0\
0&1\
1&1
end{pmatrix},
qquad
V=
egin{pmatrix}
1&0\
0&1\
1&-1
end{pmatrix},
qquad
d_k=2.
]

## Computed operator

Wolfram evaluates

[
Aapprox
egin{pmatrix}
0.401112&0.197776&0.401112\
0.197776&0.401112&0.401112\
0.248255&0.248255&0.503490
end{pmatrix}.
]

Each row sums to one to the displayed precision.

The output is

[
Yapprox
egin{pmatrix}
0.802224&-0.203336\
0.598888&0\
0.751745&-0.255235
end{pmatrix}.
]

## Conditional-linearity check

Holding (Q,K), hence (A), fixed, Wolfram returns exactly zero at machine tolerance for

[
A(2V)-2(AV).
]

## State-dependence check

Perturb only (q_1) from ((1,0)) to ((1,1/2)). The first operator row changes by approximately

[
(-0.081246, 0.026831, 0.054415),
]

while the other rows remain unchanged.

## Full-map nonlinearity check

For scalar self-attention with

[
X=(1,0)^	op,qquad W_Q=W_K=W_V=1,
]

Wolfram returns

[
F(2X)-2F(X)
=
egin{pmatrix}
rac{2}{1+e}-rac{2}{1+e^4}\
0
end{pmatrix}
approx
egin{pmatrix}
0.5019104228\
0
end{pmatrix}.
]

Thus the full self-attention map is not linear in (X).

## Rendered witness

`figures/masters/ATLAS-FIG-ATTNOP-001.png`

Committed PNG Git blob:

`2ba96f6f30311c117f27c0717961145ce9cbb0cd`.

## Claim boundary

The witness reconstructs an exact toy attention computation. It establishes the distinction between a fixed mixing operator acting linearly on values and the full state-dependent nonlinear transformation. It does not show that attention weights are causal explanations, semantic importance scores, or a complete mechanistic account.
