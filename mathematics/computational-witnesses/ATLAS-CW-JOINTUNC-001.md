# ATLAS-CW-JOINTUNC-001 — Exact Joint-Uncertainty Witness

**Chapter:** ATLAS-CH-JOINTUNC-001  
**Purpose:** exact rational replay of covariance-sensitive propagation for reward, transition, observation, and future-value error coordinates.

## W1. Functional

Use:

\[
\delta
=
\varepsilon_R
+
\varepsilon_T
+
\varepsilon_O
+
\frac12\varepsilon_V.
\]

Thus:

\[
a=(1,1,1,1/2)^\top.
\]

All four coordinates have unit marginal variance.

Therefore the diagonal-only result is:

\[
\boxed{
V_{\rm diag}
=
1+1+1+\frac14
=
\frac{13}{4}.
}
\]

## W2. Positive common shock

Let \(U,W\) be independent centered Rademacher variables and set:

\[
(\varepsilon_R,\varepsilon_T,\varepsilon_O,\varepsilon_V)
=
(U,U,U,W).
\]

Then:

\[
\delta_+
=
3U+\frac12W.
\]

Therefore:

\[
\boxed{
V_+
=
\operatorname{Var}(\delta_+)
=
\frac{37}{4}.
}
\]

Covariance correction:

\[
\boxed{
V_+-V_{\rm diag}=6.
}
\]

## W3. Cancellation common shock

Set:

\[
(\varepsilon_R,\varepsilon_T,\varepsilon_O,\varepsilon_V)
=
(U,U,-U,W).
\]

Then:

\[
\delta_-
=
U+\frac12W,
\]

so:

\[
\boxed{
V_-=\frac54.
}
\]

Covariance correction:

\[
\boxed{
V_--V_{\rm diag}=-2.
}
\]

## W4. Independence control

Let:

\[
U_R,U_T,U_O,U_V
\]

be mutually independent centered Rademacher variables and set:

\[
(\varepsilon_R,\varepsilon_T,\varepsilon_O,\varepsilon_V)
=
(U_R,U_T,U_O,U_V).
\]

Then:

\[
\Sigma_0=I_4
\]

and:

\[
\boxed{
V_0=\frac{13}{4}.
}
\]

## W5. Covariance matrices

Positive common shock:

\[
\Sigma_+
=
\begin{pmatrix}
1&1&1&0\\
1&1&1&0\\
1&1&1&0\\
0&0&0&1
\end{pmatrix}.
\]

Cancellation:

\[
\Sigma_-
=
\begin{pmatrix}
1&1&-1&0\\
1&1&-1&0\\
-1&-1&1&0\\
0&0&0&1
\end{pmatrix}.
\]

Independence:

\[
\Sigma_0=I_4.
\]

The first two matrices are positive semidefinite because:

\[
\Sigma_+=bb^\top+e_4e_4^\top,
\qquad
b=(1,1,1,0)^\top,
\]

and:

\[
\Sigma_-=cc^\top+e_4e_4^\top,
\qquad
c=(1,1,-1,0)^\top.
\]

## W6. Same marginals, different result

All three cases have identical marginal variances:

\[
(1,1,1,1).
\]

But:

\[
\boxed{
\frac{37}{4}
\neq
\frac{13}{4}
\neq
\frac54.
}
\]

Hence marginal variances do not determine the propagated variance.

## W7. Minimal exact replay code

    from fractions import Fraction as F
    from itertools import product

    a = (F(1), F(1), F(1), F(1, 2))

    def mean(xs):
        return sum(xs, F(0)) / len(xs)

    def variance(xs):
        m = mean(xs)
        return mean([(x - m) ** 2 for x in xs])

    def cov(xs, ys):
        mx, my = mean(xs), mean(ys)
        return mean([(x - mx) * (y - my) for x, y in zip(xs, ys)])

    def propagated(rows):
        values = [
            sum(ai * ei for ai, ei in zip(a, row))
            for row in rows
        ]
        return variance(values)

    # Positive common shock: (U,U,U,W)
    positive = [
        (F(u), F(u), F(u), F(w))
        for u, w in product((-1, 1), repeat=2)
    ]

    # Cancellation: (U,U,-U,W)
    cancellation = [
        (F(u), F(u), F(-u), F(w))
        for u, w in product((-1, 1), repeat=2)
    ]

    # Independence control
    independent = [
        tuple(F(x) for x in row)
        for row in product((-1, 1), repeat=4)
    ]

    assert propagated(positive) == F(37, 4)
    assert propagated(cancellation) == F(5, 4)
    assert propagated(independent) == F(13, 4)

    diag_only = F(13, 4)

    assert propagated(positive) - diag_only == F(6)
    assert propagated(cancellation) - diag_only == F(-2)

    # Exact marginal variances are all one in every case.
    for rows in (positive, cancellation, independent):
        cols = list(zip(*rows))
        assert [variance(list(c)) for c in cols] == [F(1)] * 4

    # Positive-case covariance checks.
    pcols = list(zip(*positive))
    assert cov(pcols[0], pcols[1]) == F(1)
    assert cov(pcols[0], pcols[2]) == F(1)
    assert cov(pcols[1], pcols[2]) == F(1)

    # Cancellation-case covariance checks.
    ccols = list(zip(*cancellation))
    assert cov(ccols[0], ccols[1]) == F(1)
    assert cov(ccols[0], ccols[2]) == F(-1)
    assert cov(ccols[1], ccols[2]) == F(-1)

    # Independence-control off-diagonal covariances vanish.
    icols = list(zip(*independent))
    for i in range(4):
        for j in range(i + 1, 4):
            assert cov(icols[i], icols[j]) == F(0)

    print("JOINTUNC_EXACT_WITNESS_OK")

## W8. Interpretation

The code verifies:

- exact marginal variances;
- exact propagated variances;
- exact covariance corrections;
- the independence control.

It does not assert that real sequential-decision errors have these toy joint laws.

## Claim boundary

This witness proves only the finite covariance arithmetic. It does not establish causal relations among the four uncertainty coordinates, a complete tail-risk model, or global multi-step uncertainty propagation.
