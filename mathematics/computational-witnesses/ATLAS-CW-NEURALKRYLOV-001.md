# ATLAS-CW-NEURALKRYLOV-001 — Exact Short-Horizon Krylov Witness

**Chapter:** ATLAS-CH-NEURALKRYLOV-001  
**Purpose:** exact rational replay of a fixed-left-preconditioned one-step versus two-step Krylov solve, a low-dimension failure control, and a task-readout metric firewall.

## W1. Positive local solve

\[
A=
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

Exact solution:

\[
\boxed{
x^\star=
\begin{pmatrix}
1\\1/4
\end{pmatrix}.
}
\]

Fixed left preconditioner:

\[
M=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix}.
\]

Thus:

\[
B=M^{-1}A=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\qquad
c=M^{-1}b=
\begin{pmatrix}
1\\1/2
\end{pmatrix}.
\]

## W2. Best one-dimensional Krylov approximation

\[
\mathcal K_1(B,c)=\operatorname{span}\{c\}.
\]

The transformed-residual minimizing scalar is:

\[
\boxed{
\alpha=\frac34.
}
\]

Hence:

\[
x_1=
\begin{pmatrix}
3/4\\3/8
\end{pmatrix}.
\]

Transformed residual:

\[
\widehat r_1=
\begin{pmatrix}
1/4\\-1/4
\end{pmatrix},
\qquad
\boxed{
\|\widehat r_1\|_2^2=\frac18.
}
\]

Original residual:

\[
r_1=
\begin{pmatrix}
1/4\\-1/2
\end{pmatrix},
\qquad
\boxed{
\|r_1\|_2^2=\frac5{16}.
}
\]

True error:

\[
e_1=
\begin{pmatrix}
1/4\\-1/8
\end{pmatrix},
\qquad
\boxed{
\|e_1\|_2^2=\frac5{64}.
}
\]

## W3. Two-dimensional exact solve

\[
Bc=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

The basis matrix:

\[
\begin{pmatrix}
1&1\\
1/2&1
\end{pmatrix}
\]

has determinant:

\[
\boxed{
\frac12.
}
\]

Therefore:

\[
\boxed{
\mathcal K_2(B,c)=\mathbb R^2.
}
\]

The exact solution has expansion:

\[
\boxed{
x^\star=\frac32c-\frac12Bc.
}
\]

Thus an exact residual-minimizing solve over \(\mathcal K_2\) yields:

\[
\boxed{
\widehat r_2=r_2=e_2=0.
}
\]

## W4. Exact task-readout firewall

Use:

\[
w=
\begin{pmatrix}
1\\2
\end{pmatrix}.
\]

Then:

\[
w^\top x^\star
=
\frac32,
\]

and:

\[
w^\top x_1
=
\frac32.
\]

Therefore:

\[
\boxed{
w^\top x_1=w^\top x^\star
}
\]

despite:

\[
r_1\neq0,
\qquad
e_1\neq0.
\]

## W5. Low-dimension failure control

Use:

\[
B_{\rm bad}
=
\begin{pmatrix}
1&0\\
0&10
\end{pmatrix},
\qquad
c_{\rm bad}
=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

Again:

\[
\mathcal K_1(B_{\rm bad},c_{\rm bad})
=
\operatorname{span}\{c_{\rm bad}\}.
\]

The exact residual-minimizing scalar is:

\[
\boxed{
\alpha_{\rm bad}
=
\frac{11}{101}.
}
\]

Residual:

\[
r_{\rm bad}
=
\begin{pmatrix}
90/101\\
-9/101
\end{pmatrix}.
\]

Thus:

\[
\boxed{
\|r_{\rm bad}\|_2^2
=
\frac{81}{101}.
}
\]

A one-dimensional trial space can therefore be computationally small while still giving a poor one-step solve.

## W6. Minimal exact replay code

    from fractions import Fraction as F

    def matvec(A, x):
        return tuple(sum(A[i][j] * x[j] for j in range(len(x)))
                     for i in range(len(A)))

    def sub(x, y):
        return tuple(a-b for a,b in zip(x,y))

    def scale(a, x):
        return tuple(a*v for v in x)

    def dot(x, y):
        return sum((a*b for a,b in zip(x,y)), F(0))

    def norm2(x):
        return dot(x, x)

    A = ((F(1),F(0)),(F(0),F(4)))
    b = (F(1),F(1))

    M_inv = ((F(1),F(0)),(F(0),F(1,2)))
    B = ((F(1),F(0)),(F(0),F(2)))
    c = (F(1),F(1,2))

    x_star = (F(1),F(1,4))

    Bc = matvec(B, c)

    alpha = dot(Bc, c) / dot(Bc, Bc)
    assert alpha == F(3,4)

    x1 = scale(alpha, c)

    rhat1 = sub(c, matvec(B, x1))
    r1 = sub(b, matvec(A, x1))
    e1 = sub(x_star, x1)

    assert rhat1 == (F(1,4), F(-1,4))
    assert norm2(rhat1) == F(1,8)

    assert r1 == (F(1,4), F(-1,2))
    assert norm2(r1) == F(5,16)

    assert e1 == (F(1,4), F(-1,8))
    assert norm2(e1) == F(5,64)

    # K2 basis determinant and exact-solution expansion.
    det = c[0] * Bc[1] - Bc[0] * c[1]
    assert det == F(1,2)

    x_from_k2 = tuple(F(3,2)*c[i] - F(1,2)*Bc[i] for i in range(2))
    assert x_from_k2 == x_star

    # Task-readout firewall.
    w = (F(1), F(2))
    assert dot(w, x1) == dot(w, x_star) == F(3,2)

    # Bad one-dimensional control.
    B_bad = ((F(1),F(0)),(F(0),F(10)))
    c_bad = (F(1),F(1))
    Bc_bad = matvec(B_bad, c_bad)

    alpha_bad = dot(Bc_bad, c_bad) / dot(Bc_bad, Bc_bad)
    assert alpha_bad == F(11,101)

    r_bad = sub(c_bad, matvec(B_bad, scale(alpha_bad, c_bad)))
    assert r_bad == (F(90,101), F(-9,101))
    assert norm2(r_bad) == F(81,101)

    print("NEURALKRYLOV_EXACT_WITNESS_OK")

## Claim boundary

This witness proves only the finite exact arithmetic for the declared linear operators, fixed left preconditioner, Krylov trial spaces, and scalar readout.

It does not establish:

- global convergence of a learned nonlinear transport block;
- correctness of a learned or state-dependent preconditioner;
- a high-dimensional convergence rate;
- finite-precision basis orthogonality;
- equivalence between residual quality, representation quality, and downstream task quality.
