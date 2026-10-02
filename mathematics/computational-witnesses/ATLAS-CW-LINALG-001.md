# ATLAS-CW-LINALG-001 — Linear Algebra Witness

**Chapter:** `ATLAS-CH-LINALG-001`  
**Runtime:** Wolfram Language service, 2026-10-02

## Purpose

Check the exact distinction among eigenvalues, singular values, projection structure, low-rank approximation error, and conditioning.

## Witness A — non-normal matrix

[
A=
\begin{pmatrix}
1&1\
0&1
end{pmatrix}.
]

Wolfram returns eigenvalues

[
{1,1},
]

but singular values

[
left{
\frac{1+sqrt5}{2},
\frac{sqrt5-1}{2}
\right}.
]

Thus equal eigenvalue moduli do not determine one-step Euclidean amplification.

The best rank-one approximation error in induced (2)-norm is

[
sigma_2(A)
=
\frac{sqrt5-1}{2}.
]

## Witness B — orthogonal projection

For

[
P=
\begin{pmatrix}
1&0\
0&0
end{pmatrix},
]

Wolfram returns

[
P^2=P.
]

## Witness C — conditioning

For

[
D=
\begin{pmatrix}
1&0\
0&1/100
end{pmatrix},
]

the singular values are

[
1,quad 1/100,
]

hence

[
kappa_2(D)=100.
]

## Replay expression

```wolfram
aa={{1,1},{0,1}};
sv=SingularValueList[aa];
pp={{1,0},{0,0}};
dd={{1,0},{0,1/100}};
{Eigenvalues[aa],FullSimplify[sv],pp.pp==pp,
 SingularValueList[dd],
 FullSimplify[Max[SingularValueList[dd]]/Min[SingularValueList[dd]]],
 FullSimplify[Last[sv]]}
```

## Claim boundary

This witness checks exact finite-dimensional identities and one conditioning example. It does not establish claims about optimization dynamics, model training, or empirical representation geometry.
