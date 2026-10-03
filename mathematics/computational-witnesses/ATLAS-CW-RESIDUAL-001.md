# ATLAS-CW-RESIDUAL-001 — Residual Reconstruction Witness

**Chapter:** \`ATLAS-CH-RESIDUAL-001\`  
**Runtime:** Wolfram Language service, 2026-10-02

## Purpose

Replay the exact toy model used to distinguish:

- invariance;
- capability sufficiency;
- full-state reconstruction;
- transfer across an invertible recoding.

## Model

State:

\[
x=(s,n).
\]

Nuisance translation:

\[
g_a(s,n)=(s,n+a).
\]

Capability:

\[
B(s,n)=s.
\]

Residual:

\[
R(s,n)=s.
\]

## Orbit invariance witness

For

\[
s=2,
\qquad
n=5,
\qquad
a=-3,
\]

we have

\[
x=(2,5),
\]

and

\[
g_{-3}(x)=(2,2).
\]

The Residual remains

\[
R(x)=R(g_{-3}(x))=2.
\]

## Invertible recoding witness

Let

\[
T=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

For

\[
x=(2,5),
\]

\[
z=Tx=(7,-3).
\]

Reconstruct:

\[
R_T(z)
=
\frac{z_1+z_2}{2}
=
2.
\]

The capability-relevant signal survives the coordinate change even though it is not stored in one transformed coordinate.

## Invariant-but-insufficient witness

The constant descriptor

\[
S_0(x)=0
\]

is invariant.

But for

\[
x_1=(2,0),
\qquad
x_2=(3,0),
\]

we have

\[
S_0(x_1)=S_0(x_2)=0,
\]

while

\[
B(x_1)=2,
\qquad
B(x_2)=3.
\]

Therefore no deterministic decoder from \(S_0\) can reconstruct the declared capability on both states.

## Replay expression

\`\`\`wolfram
x={2,5};
a=-3;
g[{s_,n_},aa_]:={s,n+aa};
res[{s_,n_}]:=s;
T={{1,1},{1,-1}};
z=T.x;
resT[{z1_,z2_}]:=(z1+z2)/2;
x1={2,0};
x2={3,0};

{x,g[x,a],res[x],res[g[x,a]],
 z,resT[z],
 0,0,res[x1],res[x2]}
\`\`\`

Expected exact result:

\[
\{
(2,5),
(2,2),
2,
2,
(7,-3),
2,
0,
0,
2,
3
\}.
\]

## Claim boundary

This witness establishes the declared finite toy reconstruction only.

It does not establish that a comparable least invariant sufficient descriptor exists for a frontier model, nor that one can be learned efficiently.
