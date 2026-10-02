# ATLAS-CH-ATTNOP-001 — Derivation Packet

**Status:** first-pass derivations  
**Source lock:** \`sources/source-locks/ATLAS-CH-ATTNOP-001.yaml\`  
**Norm convention:** ordinary Euclidean/Frobenius conventions unless stated otherwise.

## D1. Standard scaled dot-product attention

For hidden states \(X\in\mathbb R^{n\times d}\),

\[
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V.
\]

For one head of key dimension \(d_k\),

\[
S(X)=\frac{QK^\top}{\sqrt{d_k}},
\]

and row-wise softmax gives

\[
A(X)_{ij}
=
\frac{\exp S_{ij}}{\sum_{\ell=1}^n \exp S_{i\ell}}.
\]

The head output is

\[
\boxed{Y=A(X)V.}
\]

This is the standard scaled dot-product attention construction [@VaswaniEtAl2017].

The Atlas keeps four objects distinct:

\[
S=\text{score matrix},\qquad
A=\text{normalized mixing operator},\qquad
V=\text{value field},\qquad
F(X)=A(X)V(X).
\]

## D2. Conditional linearity in the value field

Fix \(Q\) and \(K\), hence fix \(A\).

For value fields \(V_1,V_2\) and scalars \(\alpha,\beta\),

\[
A(\alpha V_1+\beta V_2)
=
\alpha AV_1+\beta AV_2.
\]

Therefore

\[
V\mapsto AV
\]

is linear when the mixing operator is held fixed.

This does **not** imply that self-attention is linear in \(X\), because both \(A(X)\) and \(V(X)\) depend on \(X\).

## D3. Row-stochastic structure

For every finite unmasked score row,

\[
A_{ij}>0
\]

and

\[
\sum_{j=1}^n A_{ij}=1.
\]

Hence

\[
\boxed{A\mathbf 1=\mathbf 1.}
\]

Each output row is therefore a convex combination of value rows before any later output projection.

This algebraic fact does not make the whole attention layer a Markov process.

## D4. The full self-attention map is nonlinear

Take

\[
X=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
W_Q=W_K=W_V=1,
\qquad d_k=1.
\]

Then

\[
Q=K=V=X,\qquad
S=XX^\top.
\]

The first output component is

\[
F(X)_1=\frac{e}{1+e}.
\]

For \(2X\),

\[
F(2X)_1=\frac{2e^4}{1+e^4},
\]

whereas

\[
2F(X)_1=\frac{2e}{1+e}.
\]

Thus

\[
F(2X)_1-2F(X)_1
=
\frac{2e^4}{1+e^4}
-
\frac{2e}{1+e}
\neq 0.
\]

Numerically the magnitude of the discrepancy is about \(0.5019104228\).

Therefore

\[
\boxed{F(2X)\neq 2F(X).}
\]

## D5. Exact three-token witness

Use

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
\qquad d_k=2.
\]

Then

\[
S=
\frac1{\sqrt2}
\begin{pmatrix}
1&0&1\\
0&1&1\\
1&1&2
\end{pmatrix}.
\]

The row-softmax operator is approximately

\[
A\approx
\begin{pmatrix}
0.401112&0.197776&0.401112\\
0.197776&0.401112&0.401112\\
0.248255&0.248255&0.503490
\end{pmatrix},
\]

and

\[
Y=AV\approx
\begin{pmatrix}
0.802224&-0.203336\\
0.598888&0\\
0.751745&-0.255235
\end{pmatrix}.
\]

Wolfram replay gives row sums equal to \(1\) to numerical precision and fixed-\(A\) linearity residual \(0\).

## D6. Query perturbation induces operator perturbation

Perturb only the first query,

\[
q_1=(1,0)
\quad\longrightarrow\quad
q_1'=(1,\tfrac12),
\]

holding \(K\) and \(V\) fixed.

Only the first score row changes, hence only the first row of \(A\) changes.

Wolfram replay gives

\[
\Delta A_{1,:}
\approx
(-0.08124593,\;0.02683053,\;0.05441540).
\]

This is a bounded example of

\[
\text{state perturbation}
\longrightarrow
\text{operator perturbation}
\longrightarrow
\text{output perturbation}.
\]

## D7. Permutation equivariance without positional asymmetry

Let \(P\) be a permutation matrix and \(X'=PX\). Then

\[
Q'=PQ,\qquad K'=PK,\qquad V'=PV.
\]

Therefore

\[
S'
=
\frac{Q'K'^\top}{\sqrt{d_k}}
=
PSP^\top.
\]

Row-wise softmax commutes with the simultaneous row/column permutation:

\[
A'=PAP^\top.
\]

Hence

\[
Y'=A'V'
=
PAP^\top PV
=
PY.
\]

So, in the absence of positional encodings or asymmetric masks,

\[
\boxed{F(PX)=PF(X).}
\]

This is permutation **equivariance**, not invariance.

## D8. Causal masking as an operator constraint

Let

\[
M_{ij}
=
\begin{cases}
0,&j\le i,\\
-\infty,&j>i.
\end{cases}
\]

Then

\[
A=\operatorname{softmax}_{\rm row}(S+M)
\]

satisfies

\[
A_{ij}=0\qquad\text{for }j>i.
\]

The mask therefore constrains the admissible support pattern of the mixing operator.

## D9. Differential sensitivity of a softmax row

For a softmax row

\[
a=\operatorname{softmax}(s),
\]

the Jacobian is

\[
J_{\rm softmax}(a)
=
\operatorname{diag}(a)-aa^\top.
\]

A query perturbation \(\delta q_i\) induces

\[
\delta s_i
=
\frac{\delta q_i K^\top}{\sqrt{d_k}},
\]

and, to first order,

\[
\delta a_i
\approx
\left(\operatorname{diag}(a_i)-a_i a_i^\top\right)
\frac{\delta q_iK^\top}{\sqrt{d_k}}.
\]

This gives a concrete local operator-sensitivity calculation without elevating attention weights to causal explanations.

## D10. Kernel-feature reassociation

For a similarity admitting

\[
k(q,k)=\phi(q)^\top\phi(k),
\]

an unnormalized numerator

\[
\sum_j \phi(q_i)^\top\phi(k_j)v_j^\top
\]

can be reassociated as

\[
\phi(q_i)^\top
\left(
\sum_j \phi(k_j)v_j^\top
\right).
\]

This algebra is the basis of linear-attention constructions such as Katharopoulos et al. [@KatharopoulosEtAl2020]. It changes the computational factorization of the operator action; it does not license a universal claim that every attention mechanism is a fixed kernel machine.

## Claim boundary

This packet establishes algebraic properties of standard scaled dot-product attention and two finite toy systems. It does not establish that attention weights are causal explanations, that the toy matrices resemble a trained head, or that kernel language exhausts the possible interpretations of attention.
