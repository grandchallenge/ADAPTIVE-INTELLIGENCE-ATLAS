# ATLAS-CW-ATTNOP-001 — Attention Operator Witness

**Chapter:** \`ATLAS-CH-ATTNOP-001\`  
**System:** Wolfram Language 15.0.1 for Linux x86 (64-bit), July 2 2026  
**System ID:** Linux-x86-64  
**Figure source:** \`figures/wolfram/ATLAS-FIG-ATTNOP-001.wl\`

## Purpose

Reconstruct one attention head as four explicit objects:

\[
S,\qquad
A=\operatorname{softmax}_{\rm row}(S),\qquad
V,\qquad
Y=AV.
\]

## Parameters

\[
Q=K=
\begin{pmatrix}
1&0\\
0&1\\
1&1
\end{pmatrix},
\qquad
V=
\begin{pmatrix}
1&0\\
0&1\\
1&-1
\end{pmatrix},
\qquad
d_k=2.
\]

## Computed operator

Wolfram evaluates

\[
A\approx
\begin{pmatrix}
0.401112&0.197776&0.401112\\
0.197776&0.401112&0.401112\\
0.248255&0.248255&0.503490
\end{pmatrix}.
\]

Each row sums to one to numerical precision.

The output is

\[
Y\approx
\begin{pmatrix}
0.80222418536&-0.20333627804\\
0.59888790732&0\\
0.75174492174&-0.25523476523
\end{pmatrix}.
\]

## Conditional-linearity check

Holding \(Q,K\), hence \(A\), fixed, Wolfram returns residual

\[
A(2V)-2(AV)=0.
\]

## State-dependence check

Perturb only

\[
q_1=(1,0)
\quad\longrightarrow\quad
q_1'=(1,\tfrac12).
\]

The first operator row changes by approximately

\[
(-0.08124592681,\;0.02683052899,\;0.05441539782),
\]

while the other rows remain unchanged.

## Full-map nonlinearity check

For scalar self-attention with

\[
X=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
W_Q=W_K=W_V=1,
\]

the first component satisfies

\[
F(2X)_1-2F(X)_1
=
\frac{2e^4}{1+e^4}
-
\frac{2e}{1+e},
\]

whose magnitude is approximately

\[
0.5019104228.
\]

Thus the full self-attention map is not linear in \(X\).

## Rendered witness

\`figures/masters/ATLAS-FIG-ATTNOP-001.png\`

Committed PNG Git blob:

\`2ba96f6f30311c117f27c0717961145ce9cbb0cd\`.

## Claim boundary

The witness reconstructs one exact toy attention computation. It establishes the distinction between a fixed mixing operator acting linearly on values and the full state-dependent nonlinear transformation. It does not show that attention weights are causal explanations, semantic importance scores, or a complete mechanistic account.
