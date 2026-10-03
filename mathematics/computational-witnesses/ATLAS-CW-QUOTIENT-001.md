# ATLAS-CW-QUOTIENT-001 — Quotient Symmetry Witness

**Chapter:** \`ATLAS-CH-QUOTIENT-001\`  
**Runtime:** Wolfram Language service, 2026-10-02

## Purpose

Replay three different parameter representatives of one scalar-input, two-hidden-unit ReLU function.

## Original representative

\[
W_1=
\begin{pmatrix}
1\\
2
\end{pmatrix},
\qquad
W_2=
\begin{pmatrix}
3&4
\end{pmatrix}.
\]

The network is

\[
f(x)
=
3\operatorname{ReLU}(x)
+
4\operatorname{ReLU}(2x).
\]

## Permuted representative

Using hidden-unit swap

\[
P=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]

the parameters become

\[
W_1'=
\begin{pmatrix}
2\\
1
\end{pmatrix},
\qquad
W_2'=
\begin{pmatrix}
4&3
\end{pmatrix}.
\]

## Positive-rescaling representative

Using

\[
D=\operatorname{diag}(2,1/3),
\]

the parameters become

\[
W_1''=
\begin{pmatrix}
2\\
2/3
\end{pmatrix},
\qquad
W_2''=
\begin{pmatrix}
3/2&12
\end{pmatrix}.
\]

## Exact output replay

For the grid

\[
x\in
\{-2,-3/2,-1,-1/2,0,1/2,1,3/2,2\},
\]

all three parameterizations give the exact output sequence

\[
\{0,0,0,0,0,11/2,11,33/2,22\}.
\]

The derivation packet proves equality for every real \(x\), not only this grid.

## Replay expression

\`\`\`wolfram
relu[z_]:=Max[0,z];
w1={1,2};
w2={3,4};
p={{0,1},{1,0}};
d=DiagonalMatrix[{2,1/3}];

f[z_]:=
 w2.{relu[w1[[1]] z],relu[w1[[2]] z]};

w1p=p.w1;
w2p=w2.Inverse[p];
fp[z_]:=
 w2p.{relu[w1p[[1]] z],relu[w1p[[2]] z]};

w1d=d.w1;
w2d=w2.Inverse[d];
fd[z_]:=
 w2d.{relu[w1d[[1]] z],relu[w1d[[2]] z]};

grid=Range[-2,2,1/2];

{w1,w2,w1p,w2p,w1d,w2d,
 f/@grid,fp/@grid,fd/@grid,
 And@@Thread[(f/@grid)==(fp/@grid)],
 And@@Thread[(f/@grid)==(fd/@grid)]}
\`\`\`

## Hessian null-direction witness

For the smooth scalar model

\[
f(a,b)=ab
\]

with loss

\[
L(a,b)=\frac12(ab-y)^2,
\]

the positive rescaling

\[
(a,b)\mapsto(a/c,cb)
\]

leaves the model output unchanged.

On the critical manifold

\[
y=ab,
\]

the Hessian is

\[
H=
\begin{pmatrix}
b^2&ab\\
ab&a^2
\end{pmatrix}.
\]

The infinitesimal scaling-orbit tangent is

\[
v=(-a,b).
\]

Wolfram verifies

\[
Hv=(0,0).
\]

Replay:

\`\`\`wolfram
loss=(a b-y)^2/2;
h=D[loss,{{a,b},2}];
hc=FullSimplify[h/.y->a b];
v={-a,b};
{hc,v,FullSimplify[hc.v]}
\`\`\`

## Claim boundary

This witness reconstructs exact function-preserving permutation and positive-rescaling transformations for one declared ReLU architecture.

It does not establish that these are the only symmetries of that architecture class, that arbitrary neural-network parameter quotients are smooth manifolds, or that quotient optimization is easier.
