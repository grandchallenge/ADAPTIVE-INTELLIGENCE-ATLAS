# ATLAS-CW-NORMREP-001 — Normalized Representation Witness

**Chapter:** \`ATLAS-CH-NORMREP-001\`  
**Runtime:** Wolfram Language service, 2026-10-02

## Purpose

Replay the normalization differential, radial annihilation, tangent transport, chord-angle identity, and SLERP midpoint used by the chapter.

## Witness A — normalization differential

Let

\[
x=(3,4),
\qquad
\|x\|_2=5,
\qquad
u=(3/5,4/5).
\]

The exact Jacobian is

\[
J_N(x)
=
\frac{1}{5}(I-uu^\top)
=
\begin{pmatrix}
16/125&-12/125\\
-12/125&9/125
\end{pmatrix}.
\]

Wolfram verifies

\[
J_N(x)x=(0,0).
\]

Thus the radial direction is annihilated to first order.

For the tangent vector

\[
t=(-4,3),
\]

Wolfram verifies

\[
J_N(x)t=(-4/5,3/5).
\]

## Witness B — chord and angular geometry

Let

\[
a=(1,0),
\qquad
b=
\left(
1/2,\sqrt3/2
\right).
\]

Wolfram verifies:

\[
\theta=\arccos(a^\top b)=\pi/3,
\]

\[
\|a-b\|_2^2=1,
\]

and

\[
\operatorname{SLERP}(a,b;1/2)
=
\left(
\sqrt3/2,1/2
\right),
\]

with unit norm.

## Replay expression

\`\`\`wolfram
x={3,4};
n=Sqrt[x.x];
u=x/n;
j=(IdentityMatrix[2]-Outer[Times,u,u])/n;
t={-4,3};
a={1,0};
b={1/2,Sqrt[3]/2};
theta=ArcCos[a.b];
slerpHalf=
 (Sin[(1-1/2) theta]/Sin[theta]) a+
 (Sin[(1/2) theta]/Sin[theta]) b;
{n,u,FullSimplify[j],FullSimplify[j.x],
 FullSimplify[j.t],FullSimplify[theta],
 FullSimplify[(a-b).(a-b)],
 FullSimplify[slerpHalf],
 FullSimplify[Sqrt[slerpHalf.slerpHalf]]}
\`\`\`

## Claim boundary

This witness establishes exact local properties of the Euclidean normalization map and one exact spherical interpolation example.

It does not establish that normalization improves a learning system, nor does it reproduce empirical nGPT results.
