# ATLAS-CW-TRANSFER-001 — Reconstruction and Transfer Witness

**Chapter:** \`ATLAS-CH-TRANSFER-001\`  
**Runtime:** Wolfram Language service, 2026-10-02

## Purpose

Replay:

- exact source and target recodings of one transferable Residual;
- exact reconstruction of two target tasks;
- exact failure of a lossy one-dimensional bottleneck.

## Transferable structure

\[
r=(3,1).
\]

Source map:

\[
A_s=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

Target map:

\[
A_t=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix}.
\]

The representations are

\[
z_s=(4,2),
\]

and

\[
z_t=(6,1/2).
\]

Using

\[
C_s=A_s^{-1},
\qquad
C_t=A_t^{-1},
\]

both reconstruct

\[
r=(3,1).
\]

## Target tasks

\[
D_1(a,b)=a+b,
\]

\[
D_2(a,b)=2a-b.
\]

Both representations reconstruct

\[
D_1=4,
\]

and

\[
D_2=5.
\]

## Lossy bottleneck

Let

\[
P(a,b)=a.
\]

For

\[
r_A=(1,0),
\qquad
r_B=(1,1),
\]

we have

\[
P(r_A)=P(r_B)=1.
\]

But

\[
D_2(r_A)=2,
\]

and

\[
D_2(r_B)=1.
\]

No deterministic decoder from \(P(r)\) alone can reconstruct \(D_2\) on both states.

## Replay expression

\`\`\`wolfram
As={{1,1},{1,-1}};
At={{2,0},{0,1/2}};
r={3,1};

zs=As.r;
zt=At.r;

Cs=Inverse[As];
Ct=Inverse[At];

d1[v_]:=v[[1]]+v[[2]];
d2[v_]:=2 v[[1]]-v[[2]];

rA={1,0};
rB={1,1};
p[v_]:=v[[1]];

{zs,zt,
 FullSimplify[Cs.zs],
 FullSimplify[Ct.zt],
 d1[Cs.zs],d1[Ct.zt],
 d2[Cs.zs],d2[Ct.zt],
 p[rA],p[rB],
 d2[rA],d2[rB]}
\`\`\`

Expected exact result:

\[
\{
(4,2),
(6,1/2),
(3,1),
(3,1),
4,4,5,5,1,1,2,1
\}.
\]

## Claim boundary

This witness establishes exact reconstruction and exact bottleneck failure only for the declared deterministic toy system.

It does not establish empirical transfer benefit, optimization success, or robustness to distribution shift.
