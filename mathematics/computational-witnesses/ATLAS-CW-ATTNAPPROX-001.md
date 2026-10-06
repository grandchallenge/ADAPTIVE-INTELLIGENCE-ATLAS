# ATLAS-CW-ATTNAPPROX-001 — Approximate Attention Witness

**Chapter:** ATLAS-CH-ATTNAPPROX-001  
**Purpose:** exact finite replay for target/error separation, rank reduction, and sparse-alternative support change.

## W1. Exact rank-2 normalized operator

Use

\[
A=
\begin{pmatrix}
1/2&1/3&1/6\\
1/2&1/3&1/6\\
1/6&1/3&1/2
\end{pmatrix}.
\]

Every row sums to one.

All entries are positive.

The first two rows are equal, while the first and third are linearly independent.

Therefore

\[
\operatorname{rank}(A)=2.
\]

Because A is positive and row-stochastic, it can be represented exactly as a row-softmax matrix by taking row scores \(\log A_{ij}\), up to rowwise additive constants.

## W2. Rank-1 row-average approximation

Define

\[
\widehat A=
\begin{pmatrix}
7/18&1/3&5/18\\
7/18&1/3&5/18\\
7/18&1/3&5/18
\end{pmatrix}.
\]

All rows are identical, so

\[
\operatorname{rank}(\widehat A)=1.
\]

It remains positive and row-stochastic.

The error matrix is

\[
E=A-\widehat A
=
\frac19
\begin{pmatrix}
1&0&-1\\
1&0&-1\\
-2&0&2
\end{pmatrix}.
\]

Factor it as

\[
E
=
\frac19
\begin{pmatrix}
1\\
1\\
-2
\end{pmatrix}
\begin{pmatrix}
1&0&-1
\end{pmatrix}.
\]

Thus E is rank one.

## W3. Exact operator error

The squared Frobenius error is

\[
\|E\|_F^2
=
\frac{12}{81}
=
\boxed{\frac4{27}}.
\]

For the spectral norm,

\[
\|E\|_2
=
\frac19
\sqrt{1^2+1^2+(-2)^2}
\sqrt{1^2+0^2+(-1)^2}
\]

so

\[
\boxed{
\|E\|_2
=
\frac{2\sqrt3}{9}
}.
\]

## W4. Exact output error

Use

\[
V=
\begin{pmatrix}
1&0\\
0&1\\
1&-1
\end{pmatrix}.
\]

Then

\[
AV=
\begin{pmatrix}
2/3&1/6\\
2/3&1/6\\
2/3&-1/6
\end{pmatrix},
\]

while

\[
\widehat A V=
\begin{pmatrix}
2/3&1/18\\
2/3&1/18\\
2/3&1/18
\end{pmatrix}.
\]

Therefore

\[
EV=
\begin{pmatrix}
0&1/9\\
0&1/9\\
0&-2/9
\end{pmatrix}
\]

and

\[
\boxed{
\|EV\|_F^2
=
\frac2{27}
}.
\]

Also

\[
\|V\|_F=2,
\]

so the general induced-norm bound gives

\[
\|EV\|_F
\le
\frac{4\sqrt3}{9}.
\]

The actual error is

\[
\frac{\sqrt6}{9}.
\]

## W5. A kernel can move far while the operator does not move

Let K be any positive kernel matrix and choose \(c>0\).

Set

\[
\widehat K=cK.
\]

Then

\[
D(\widehat K)^{-1}\widehat K
=
D(K)^{-1}K.
\]

So

\[
E_A=0
\]

even though

\[
E_K
=
|c-1|\|K\|_F
\]

can be made arbitrarily large.

This is an exact counterexample to treating raw kernel norm error as normalized-attention error.

## W6. Sparse alternative

Take score row

\[
s=(2,0,-1).
\]

Softmax gives

\[
\operatorname{softmax}(s)
=
\frac1{e^2+1+e^{-1}}
(e^2,1,e^{-1}),
\]

whose three coordinates are strictly positive.

At alpha=2, entmax equals sparsemax.

Using simplex-projection threshold \(\tau=1\),

\[
\max(s-\tau,0)
=
(1,0,0).
\]

Thus

\[
\boxed{
\operatorname{entmax}_{2}(2,0,-1)
=
(1,0,0)
}.
\]

The exact zero entries are a change of normalization family, not a finite-sample failure to reproduce softmax.

## W7. Positive random-feature identity

For

\[
\phi_\omega(x)
=
\exp(
\omega^\top x-\|x\|^2/2
),
\qquad
\omega\sim N(0,I),
\]

the Gaussian moment-generating function gives

\[
\mathbb E[
\phi_\omega(q)\phi_\omega(k)
]
=
e^{q^\top k}.
\]

This verifies the expectation identity only.

It does not verify a finite-feature concentration theorem or the complete FAVOR+ construction.

## W8. Minimal exact replay code

    from fractions import Fraction as F

    A = [
        [F(1,2), F(1,3), F(1,6)],
        [F(1,2), F(1,3), F(1,6)],
        [F(1,6), F(1,3), F(1,2)],
    ]

    Ah = [
        [F(7,18), F(1,3), F(5,18)],
        [F(7,18), F(1,3), F(5,18)],
        [F(7,18), F(1,3), F(5,18)],
    ]

    V = [
        [F(1), F(0)],
        [F(0), F(1)],
        [F(1), F(-1)],
    ]

    def mm(X, Y):
        return [
            [
                sum(X[i][k] * Y[k][j] for k in range(len(Y)))
                for j in range(len(Y[0]))
            ]
            for i in range(len(X))
        ]

    def sub(X, Y):
        return [
            [X[i][j] - Y[i][j] for j in range(len(X[0]))]
            for i in range(len(X))
        ]

    def frob2(X):
        return sum(x*x for row in X for x in row)

    assert all(sum(row) == 1 for row in A)
    assert all(sum(row) == 1 for row in Ah)

    E = sub(A, Ah)

    assert E == [
        [F(1,9), F(0), F(-1,9)],
        [F(1,9), F(0), F(-1,9)],
        [F(-2,9), F(0), F(2,9)],
    ]

    assert frob2(E) == F(4,27)

    AV = mm(A, V)
    AhV = mm(Ah, V)
    EV = sub(AV, AhV)

    assert AV == [
        [F(2,3), F(1,6)],
        [F(2,3), F(1,6)],
        [F(2,3), F(-1,6)],
    ]

    assert AhV == [
        [F(2,3), F(1,18)],
        [F(2,3), F(1,18)],
        [F(2,3), F(1,18)],
    ]

    assert frob2(EV) == F(2,27)

    # Sparsemax / alpha=2 entmax witness for s=(2,0,-1).
    s = [F(2), F(0), F(-1)]
    tau = F(1)
    sparse = [max(x - tau, F(0)) for x in s]
    assert sparse == [F(1), F(0), F(0)]
    assert sum(sparse) == 1

## W9. What is and is not replayed

The exact replay verifies:

- row-stochasticity of A and \(\widehat A\);
- the rank-1 error factorization;
- exact Frobenius operator error;
- exact output error;
- exact sparsemax support for the declared score row.

The spectral norm is verified analytically from the rank-one factorization.

The random-feature identity is verified analytically from the Gaussian moment-generating function.

No stochastic finite-sample experiment is promoted to theorem status.

## Claim boundary

This witness does not establish:

- that the rank-1 approximation is optimal;
- that trained attention matrices are generically rank two or nearly rank one;
- that small Frobenius error implies small task loss;
- that one value field is sufficient to identify operator error;
- that alpha-entmax is better than softmax;
- that sparse support guarantees computational savings;
- that a finite FAVOR+ feature budget meets a particular error tolerance;
- that low-rank, random-feature, landmark, and sparse methods are equivalent.
