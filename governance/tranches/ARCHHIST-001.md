# ARCHHIST-001 — From Layered Networks to Residual Systems

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- current reconciled main includes AUDIT-008A at:
  \`c18a5067c29e2c34cfbec770c5220eea51555249\`;
- issue:
  \`#48\`;
- hard prerequisite:
  \`ATLAS-CH-DYN-001\` at audited \`draft-v0.1\`.

## Objective

Use a selective architectural lineage to expose changes in the mathematical object of analysis:

\[
\text{composition}
\to
\text{structured operators}
\to
\text{persistent state}
\to
\text{interfaces}
\to
\text{gated carry}
\to
\text{residual transport}
\to
\text{explicit continuous depth}.
\]

This is a structural history, not a ranking or priority claim.

## A. Layered composition

The chapter begins with

\[
x_{k+1}=F_k(x_k),
\]

so

\[
x_L
=
F_{L-1}\circ\cdots\circ F_0(x_0).
\]

For differentiable layers,

\[
J_{\rm total}
=
J_{F_{L-1}}
\cdots
J_{F_0}.
\]

## B. Convolutional structure

For periodic discrete convolution

\[
(C_kx)_j
=
\sum_r k_r x_{j-r},
\]

and cyclic shift

\[
(S_mx)_j=x_{j-m},
\]

the derivation proves

\[
C_kS_m=S_mC_k.
\]

Exact witness:

\[
C=I+2S,
\]

with

\[
CS-SC=0,
\]

and for

\[
x=(1,2,3,4),
\]

\[
CSx=SCx=(10,9,4,7).
\]

The claim is explicitly restricted to the declared circular-convolution model.

## C. Recurrent state

For

\[
h_{t+1}=a h_t+b x_t,
\]

the derivation gives

\[
h_T
=
a^T h_0
+
b\sum_{j=0}^{T-1}a^{T-1-j}x_j.
\]

Exact witness:

\[
a=\frac12,\quad b=2,\quad h_0=1,\quad (x_0,x_1,x_2)=(3,-1,4),
\]

producing

\[
(h_0,h_1,h_2,h_3)
=
\left(
1,\frac{13}{2},\frac54,\frac{69}{8}
\right).
\]

## D. Encoder–decoder interface

The chapter writes

\[
z=E(x),
\qquad
\hat y=D(z).
\]

If

\[
E(x_1)=E(x_2)
\]

while required outputs differ, no deterministic decoder using only \(z\) can reconstruct both.

This is an interface-sufficiency statement, not a claim that useful encoders must be injective.

## E. Highway gating

Structural form:

\[
y
=
T(x)\odot H(x)
+
C(x)\odot x.
\]

For the tied choice

\[
C=1-T,
\]

the exact carry limit

\[
T=0
\]

gives

\[
y=x,
\]

and the exact transform limit

\[
T=1
\]

gives

\[
y=H(x).
\]

Exact scalar witness:

\[
x=2,\quad H(x)=5,\quad T=\frac14,\quad C=\frac34,
\]

so

\[
y=\frac{11}{4}.
\]

## F. Residual transport

The residual block is

\[
x_{k+1}
=
x_k+F_k(x_k).
\]

Its Jacobian is

\[
J_k
=
I+J_{F_k}(x_k).
\]

For linear branch

\[
F(x)=Ax,
\qquad
A=
\begin{pmatrix}
1&2\\
-1&3
\end{pmatrix},
\]

the exact block Jacobian is

\[
I+A
=
\begin{pmatrix}
2&2\\
-1&4
\end{pmatrix}.
\]

For zero residual branch,

\[
A=0,
\]

the block is exact identity.

## G. Continuous-depth handoff

Neural ODEs are treated as a specific architecture family defined by

\[
\frac{dz}{dt}
=
f(z,t;\theta)
\]

plus numerical integration.

The chapter explicitly denies the stronger retrospective claim that ordinary ResNets are literally solutions of one autonomous ODE.

## H. Source boundary

Primary/influential architecture sources:

- Rumelhart, Hinton, Williams 1986;
- LeCun et al. 1998;
- Hochreiter–Schmidhuber 1997;
- Sutskever–Vinyals–Le 2014;
- Srivastava–Greff–Schmidhuber 2015;
- He et al. 2016;
- Chen et al. 2018.

The Atlas synthesis is the structural lineage connecting those mechanisms.

No blanket historical priority or universal-superiority claim is made.

## I. Dynamics provenance

The hard prerequisite is pinned to the post-AUDIT-008A Dynamics object:

- commit:
  \`c18a5067c29e2c34cfbec770c5220eea51555249\`;
- Dynamics manuscript blob:
  \`f4aa89075f221529401e56a152a6cdfca3dcc47d\`.

## J. Figure

\`ATLAS-FIG-ARCHHIST-001\`

- generator blob:
  \`057e0da8dabc55045bfd9c3afe3014005c6adc76\`;
- rendered blob:
  \`296afa2a50cb63cce04a91ae9ef7b104f438406d\`;
- rendered bytes:
  \`49,015\`;
- representation class:
  schematic.

Panels:

1. layered composition;
2. convolutional sharing;
3. recurrent state;
4. encoder–decoder interface;
5. highway gating;
6. residual identity bypass.

## K. Frozen distinctions

\[
\text{history}
\neq
\text{performance ranking}.
\]

\[
\text{convolutional structure}
\neq
\text{full-pipeline exact equivariance}.
\]

\[
\text{recurrence}
\neq
\text{guaranteed long-term memory}.
\]

\[
\text{encoder bottleneck}
\neq
\text{automatic sufficiency}.
\]

\[
\text{highway gating}
\neq
\text{residual addition}.
\]

\[
\text{identity path}
\neq
\text{guaranteed good conditioning}.
\]

\[
\text{residual form}
\neq
\text{proved underlying ODE}.
\]

## L. Durable objects

The branch contains:

- source lock;
- chapter specification;
- derivation packet;
- exact computational witness;
- complete manuscript;
- Wolfram figure generator/master/manifest;
- Figure Register entry;
- Chapter Ledger promotion to \`draft-v0.1\`.

## M. Next step after merge

Run a bounded post-draft audit checking:

- source scope and historical non-overclaim;
- circular-convolution equivariance;
- recurrence closed form;
- encoder information-loss boundary;
- highway carry/transform limits;
- residual Jacobian and identity limit;
- residual-versus-ODE boundary;
- Neural ODE scope;
- figure provenance.

Do not begin direct consumers until this audit merges.
