# ATLAS-CW-COMPOSE-001 — Exact Composition Witness

**Chapter:** ATLAS-CH-COMPOSE-001  
**Purpose:** exact replay of order-sensitive gain, commuting control, and finite error-budget accumulation.

## W1. Components

Let

\[
A=
\begin{pmatrix}
3/2&0\\
0&2/3
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&3/2\\
2/3&0
\end{pmatrix}.
\]

Each satisfies

\[
\|A\|_2=\|B\|_2=\frac32.
\]

Declare component-local gain ceiling:

\[
L_{\rm local}=\frac32.
\]

Declare system gain budget:

\[
\tau=2.
\]

## W2. Chronological A then B

For column-vector states, chronological \(A\) then \(B\) is the product \(BA\).

\[
BA
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

Since this matrix is orthogonal,

\[
\boxed{\|BA\|_2=1.}
\]

Therefore

\[
1<2.
\]

This order passes the system budget.

## W3. Chronological B then A

Reverse the chronology.

\[
AB
=
\begin{pmatrix}
0&9/4\\
4/9&0
\end{pmatrix}.
\]

Then

\[
(AB)^\top(AB)
=
\begin{pmatrix}
16/81&0\\
0&81/16
\end{pmatrix}.
\]

Hence the singular values are

\[
4/9,\quad 9/4,
\]

and

\[
\boxed{\|AB\|_2=\frac94.}
\]

Therefore

\[
\frac94>2.
\]

This order violates the system budget.

## W4. Exact noncommutativity

\[
[A,B]
=
AB-BA
=
\begin{pmatrix}
0&5/4\\
-5/9&0
\end{pmatrix}
\ne0.
\]

The ordering effect is not caused by notation alone.

## W5. Product-bound comparison

The generic norm product is

\[
\|A\|_2\|B\|_2
=
\frac94.
\]

For \(AB\), the upper bound is attained:

\[
\|AB\|_2=\frac94.
\]

For \(BA\), the same upper bound is loose:

\[
\|BA\|_2=1<\frac94.
\]

Thus local component norms do not determine the exact composite gain.

## W6. Compatible commuting control

Let

\[
A_c=
\begin{pmatrix}
3/2&0\\
0&2/3
\end{pmatrix},
\qquad
B_c=
\begin{pmatrix}
2/3&0\\
0&3/2
\end{pmatrix}.
\]

Then

\[
[A_c,B_c]=0
\]

and

\[
A_cB_c=B_cA_c=I.
\]

Each still has norm

\[
\frac32,
\]

while either composition has norm

\[
\boxed{1.}
\]

This is the matched compatible control.

## W7. Scalar error-budget witness

Let

\[
f(x)=x,
\qquad
g(y)=\frac32y.
\]

Suppose the implementation-local error budgets are

\[
|\widehat f(x)-f(x)|\le\frac1{10},
\]

\[
|\widehat g(y)-g(y)|\le\frac1{10}.
\]

The downstream true map has Lipschitz constant

\[
L_g=\frac32.
\]

Therefore the derived composition error budget is

\[
\begin{aligned}
E
&\le
\frac1{10}
+
\frac32\frac1{10}\\
&=
\frac14.
\end{aligned}
\]

Declare the system error budget

\[
E_{\rm sys}\le\frac15.
\]

Then

\[
\boxed{
\frac14>\frac15.
}
\]

The local \(1/10\) budgets are individually acceptable, but the derived composition guarantee violates the stricter system budget.

## W8. Minimal replay code

    from fractions import Fraction as F
    import numpy as np

    A = np.array([[1.5, 0.0], [0.0, 2.0/3.0]])
    B = np.array([[0.0, 1.5], [2.0/3.0, 0.0]])

    BA = B @ A
    AB = A @ B

    assert np.allclose(BA, np.array([[0.0, 1.0], [1.0, 0.0]]))
    assert np.allclose(AB, np.array([[0.0, 2.25], [4.0/9.0, 0.0]]))

    assert np.isclose(np.linalg.norm(A, 2), 1.5)
    assert np.isclose(np.linalg.norm(B, 2), 1.5)
    assert np.isclose(np.linalg.norm(BA, 2), 1.0)
    assert np.isclose(np.linalg.norm(AB, 2), 2.25)

    Ac = np.array([[1.5, 0.0], [0.0, 2.0/3.0]])
    Bc = np.array([[2.0/3.0, 0.0], [0.0, 1.5]])

    assert np.allclose(Ac @ Bc, np.eye(2))
    assert np.allclose(Bc @ Ac, np.eye(2))

    eps_f = F(1,10)
    eps_g = F(1,10)
    Lg = F(3,2)
    E = eps_g + Lg * eps_f

    assert E == F(1,4)
    assert E > F(1,5)

## W9. Claim boundary

This witness establishes only:

- exact component norms for the declared matrices;
- exact chronological-order products under column-vector convention;
- exact system-budget pass/fail for \(\tau=2\);
- exact commuting control;
- exact two-stage error-budget arithmetic.

It does not establish:

- that arbitrary learned modules are linear;
- that component norm \(3/2\) is universally safe or unsafe;
- that the product norm bound is globally valid for arbitrary nonlinear systems;
- that commutativity in a local linearization implies global commutativity;
- that passing this witness certifies a real deployed system;
- that local contracts alone yield a global safety theorem.
