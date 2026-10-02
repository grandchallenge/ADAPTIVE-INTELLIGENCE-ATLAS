# ATLAS-CH-ATTNOP-001 — Derivation Packet

**Status:** first-pass derivations  
**Source lock:** `sources/source-locks/ATLAS-CH-ATTNOP-001.yaml`

## D1. Standard scaled dot-product attention

For hidden states (Xinmathbb R^{n	imes d}),

[
Q=XW_Q,qquad K=XW_K,qquad V=XW_V.
]

For one head of key dimension (d_k),

[
S(X)=rac{QK^	op}{sqrt{d_k}},
]

and row-wise softmax gives

[
A(X)_{ij}
=
rac{exp S_{ij}}{sum_{ell=1}^nexp S_{iell}}.
]

The head output is

[
oxed{Y=A(X)V.}
]

This is the standard scaled dot-product construction of Vaswani et al. The Atlas separates three mathematical objects:

1. score matrix (S);
2. normalized mixing operator (A);
3. value field (V).

The full map (Xmapsto A(X)V(X)) is a fourth object.

## D2. Conditional linearity in the value field

Fix (Q) and (K). Then (S) and (A) are fixed.

For value fields (V_1,V_2) and scalars (alpha,eta),

[
A(alpha V_1+eta V_2)
=
alpha AV_1+eta AV_2.
]

Thus

[
oxed{Vmapsto AV	ext{ is linear when }Q,K	ext{ are fixed}.}
]

This statement does **not** imply that self-attention is linear in (X), because (A) and (V) normally both depend on (X).

## D3. Row-stochastic structure

For finite unmasked scores,

[
A_{ij}>0,
]

and

[
sum_j A_{ij}
=
rac{sum_j e^{S_{ij}}}{sum_ell e^{S_{iell}}}
=
1.
]

Hence each row lies on a probability simplex:

[
oxed{Amathbf 1=mathbf 1.}
]

With a causal or structural mask implemented by (-infty) logits, disallowed entries become zero after softmax while the remaining admissible row still sums to one, provided at least one entry remains admissible.

This stochastic-matrix structure concerns the **mixing weights**. The complete head also includes learned value transformation and later output projection.

## D4. The full self-attention map is nonlinear

Use the smallest nontrivial scalar self-attention example:

[
X=
egin{pmatrix}
1\
0
end{pmatrix},
qquad
W_Q=W_K=W_V=1.
]

With (d_k=1), the score matrix is (XX^	op). The output is

[
F(X)
=
egin{pmatrix}
rac{e}{1+e}\[4pt]
rac12
end{pmatrix}.
]

Scale the input by (2):

[
F(2X)
=
egin{pmatrix}
rac{2e^4}{1+e^4}\[4pt]
1
end{pmatrix}.
]

But

[
2F(X)
=
egin{pmatrix}
rac{2e}{1+e}\[4pt]
1
end{pmatrix}.
]

Their first components differ by

[
rac{2}{1+e}
-
rac{2}{1+e^4}
approx
0.5019104228.
]

Therefore

[
oxed{F(2X)
e 2F(X).}
]

The operator viewpoint is thus conditional: attention acts linearly on (V) **after** the state-dependent operator (A(X)) has been formed.

## D5. Permutation equivariance without position or asymmetric masking

Let (P) be an (n	imes n) permutation matrix and define

[
X'=PX.
]

Then

[
Q'=PQ,qquad K'=PK,qquad V'=PV.
]

The score matrix transforms as

[
S'
=
rac{Q'K'^	op}{sqrt{d_k}}
=
PSP^	op.
]

Row-wise softmax commutes with simultaneous row/column permutation:

[
operatorname{softmax}_{m row}(PSP^	op)
=
P,operatorname{softmax}_{m row}(S),P^	op.
]

Hence

[
A'=PAP^	op.
]

The output transforms as

[
Y'
=
A'V'
=
PAP^	op PV
=
PY.
]

Thus, absent positional information or an asymmetric mask,

[
oxed{F(PX)=PF(X).}
]

Positional encodings and causal masks deliberately break or modify this symmetry.

## D6. Causal attention changes the admissible operator structure

For causal self-attention, define a mask (M) with

[
M_{ij}
=
egin{cases}
0,&jle i,\
-infty,&j>i.
end{cases}
]

Then

[
A=operatorname{softmax}_{m row}(S+M)
]

has

[
A_{ij}=0
qquad
(j>i).
]

The mixing operator is lower triangular in token order. This is not merely a visualization choice: it encodes a directed information-flow constraint.

## D7. Exact Atlas toy operator

The rendered witness uses

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

Then

[
S=
rac1{sqrt2}
egin{pmatrix}
1&0&1\
0&1&1\
1&1&2
end{pmatrix}.
]

Wolfram Language 15.0.1 evaluates

[
Aapprox
egin{pmatrix}
0.401112&0.197776&0.401112\
0.197776&0.401112&0.401112\
0.248255&0.248255&0.503490
end{pmatrix}
]

with row sums equal to one to the displayed precision.

The output is

[
Y=AVapprox
egin{pmatrix}
0.802224&-0.203336\
0.598888&0\
0.751745&-0.255235
end{pmatrix}.
]

It also verifies exactly at machine tolerance that

[
A(2V)-2(AV)=0
]

when (A) is held fixed.

## D8. State dependence of the operator

Perturb only the first query from

[
q_1=(1,0)
]

to

[
q_1'=(1,1/2),
]

holding (K,V) fixed.

Only the first score row changes, and Wolfram obtains the first-row operator change

[
Delta A_{1,:}
approx
(-0.081246, 0.026831, 0.054415).
]

The remaining rows are unchanged.

This is the operational meaning of a **state-dependent operator**: the map applied to the value field is itself configured by the current query/key state.

## D9. Kernel interpretation boundary

Softmax attention can be written as normalized similarity-weighted averaging, and kernel-smoother formulations have been developed explicitly in the literature. Linear-attention methods further replace the exponential similarity with feature-map factorizations that permit associative evaluation.

The Atlas uses this connection when it clarifies structure, but does not identify every attention mechanism with a fixed positive-definite kernel. In ordinary self-attention, learned projections, normalization, masking, position, and state dependence all matter.

## Source boundary

- Scaled dot-product attention and Transformer formulation: `ATTN-VASWANI-2017`.
- Kernel-smoother interpretation: `ATTN-TSAI-ETAL-2019`.
- Kernel feature-map / linear attention: `ATTN-KATHAROPOULOS-ETAL-2020`.

The operator decomposition and toy derivations above are Atlas-owned expository derivations.
