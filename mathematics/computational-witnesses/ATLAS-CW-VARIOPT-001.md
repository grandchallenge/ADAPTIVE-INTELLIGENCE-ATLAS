# ATLAS-CW-VARIOPT-001 — Exact Divergence, Variational, Symplectic, and MODULUS Witness

**Chapter:** ATLAS-CH-VARIOPT-001

## W1. Bregman asymmetry

Use:

\[
\phi(x)=e^x.
\]

Then:

\[
D_\phi(y,x)
=
e^y-e^x-e^x(y-x).
\]

Therefore:

\[
D_\phi(1,0)=e-2,
\]

while:

\[
D_\phi(0,1)=1.
\]

These are unequal.

The witness therefore blocks the identification:

\[
\text{Bregman divergence}=\text{metric}.
\]

## W2. Local quadratic geometry

At \(x=0\):

\[
D_\phi(\delta,0)
=
e^\delta-1-\delta.
\]

Its expansion is:

\[
D_\phi(\delta,0)
=
\frac12\delta^2
+
\frac16\delta^3
+
O(\delta^4).
\]

The local quadratic coefficient is:

\[
\frac12\phi''(0)=\frac12.
\]

Thus an asymmetric global divergence can still induce a local Hessian quadratic form.

## W3. Entropic mirror step

For:

\[
\phi(x)=x\log x-x,
\qquad
x>0,
\]

we have:

\[
\nabla\phi(x)=\log x.
\]

Mirror stationarity:

\[
\nabla\phi(x_1)
=
\nabla\phi(x_0)-\eta g
\]

gives:

\[
x_1=x_0e^{-\eta g}.
\]

Take:

\[
x_0=1,
\qquad
\eta=1,
\qquad
g=\log2.
\]

Then:

\[
x_1=\frac12.
\]

## W4. Divergence-derived non-descent control

Use Euclidean generator:

\[
\phi(x)=\frac12x^2.
\]

Objective:

\[
f(x)=\frac12(x-2)^2.
\]

At:

\[
x_0=0,
\]

gradient:

\[
g_0=-2.
\]

Choose:

\[
\eta=3.
\]

The exact Bregman/gradient step is:

\[
x_1
=
0-3(-2)
=
6.
\]

Objective values:

\[
f(x_0)=2,
\]

\[
f(x_1)=8.
\]

Thus the exact divergence-derived step increases the objective.

## W5. Discrete Lagrangian

Use continuous harmonic-oscillator Lagrangian:

\[
L(q,\dot q)
=
\frac12\dot q^2-\frac12q^2.
\]

Define:

\[
L_d(q_k,q_{k+1};h)
=
\frac{(q_{k+1}-q_k)^2}{2h}
-
\frac h2q_k^2.
\]

The discrete Euler-Lagrange equation is:

\[
D_2L_d(q_{k-1},q_k)
+
D_1L_d(q_k,q_{k+1})
=
0.
\]

Exact differentiation yields:

\[
q_{k+1}
=
(2-h^2)q_k-q_{k-1}.
\]

## W6. Momentum lift

Define:

\[
p_k=\frac{q_k-q_{k-1}}h.
\]

Then the recurrence becomes:

\[
p_{k+1}=p_k-hq_k,
\]

\[
q_{k+1}=q_k+h p_{k+1}.
\]

This is symplectic Euler in the declared ordering.

## W7. Exact symplectic matrix

The state update is:

\[
\begin{pmatrix}
q_{k+1}\\
p_{k+1}
\end{pmatrix}
=
M_h
\begin{pmatrix}
q_k\\
p_k
\end{pmatrix},
\]

where:

\[
M_h
=
\begin{pmatrix}
1-h^2 & h\\
-h & 1
\end{pmatrix}.
\]

For:

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

direct exact multiplication gives:

\[
M_h^\top J M_h=J.
\]

Also:

\[
\det M_h=1.
\]

## W8. Symplectic but not energy preserving

Take:

\[
h=\frac12,
\qquad
(q_0,p_0)=(0,1).
\]

Then:

\[
p_1=1,
\]

\[
q_1=\frac12.
\]

For Hamiltonian:

\[
H(q,p)=\frac12(q^2+p^2),
\]

we obtain:

\[
H_0=\frac12,
\]

\[
H_1=\frac58.
\]

Therefore:

\[
H_1-H_0=\frac18.
\]

The map is exactly symplectic but not exactly energy preserving.

## W9. Symplectic but not objective descending

Take objective:

\[
F(q)=\frac12q^2.
\]

For the same step:

\[
F(q_0)=0,
\]

\[
F(q_1)=\frac18.
\]

The objective increases.

## W10. Exact MODULUS-style geometry pipeline

At protected MODULUS commit:

7ca4ffcdace32d5ff79c27ad557bfb690fac0af3

the Hyperball implementation uses tangent projection and sphere retraction.

Use exact toy inputs:

\[
w=(1,0),
\qquad
u=(1,1).
\]

The radial projection is:

\[
u_\parallel
=
\frac{\langle u,w\rangle}{\|w\|^2}w
=
(1,0).
\]

Hence:

\[
u_\perp=(0,1).
\]

Take programme parameter:

\[
\alpha=1.
\]

The implementation target-angle branch asks for tangent-update norm:

\[
\alpha\|w\|=1.
\]

So the tangent proposal remains \((0,1)\).

Sphere retraction gives:

\[
w_+
=
\frac{w+u_\perp}{\|w+u_\perp\|}
=
\frac{(1,1)}{\sqrt2}.
\]

## W11. Exact post-retraction angle

The exact cosine is:

\[
\frac{\langle w,w_+\rangle}
{\|w\|\|w_+\|}
=
\frac1{\sqrt2}.
\]

Therefore:

\[
\theta=\frac\pi4.
\]

Thus at finite step:

\[
\theta\ne\alpha
\]

for \(\alpha=1\).

More generally, for unit tangent \(v\):

\[
w_+
=
\frac{w+\alpha v}{\sqrt{1+\alpha^2}},
\]

which gives:

\[
\theta=\arctan\alpha.
\]

Hence:

\[
\theta=\alpha+O(\alpha^3)
\]

only in the small-step sense.

## W12. Minimal replay code

    import math
    import sympy as sp

    # Bregman asymmetry.
    assert abs((math.e - 2.0) - 0.7182818284590451) < 1e-15
    assert 1.0 != math.e - 2.0

    # Entropic mirror step.
    x0 = 1.0
    eta = 1.0
    g = math.log(2.0)
    x1 = x0 * math.exp(-eta * g)
    assert abs(x1 - 0.5) < 1e-15

    # Euclidean Bregman non-descent control.
    f = lambda x: 0.5 * (x - 2.0) ** 2
    x0 = 0.0
    grad0 = -2.0
    x1 = x0 - 3.0 * grad0
    assert x1 == 6.0
    assert f(x0) == 2.0
    assert f(x1) == 8.0
    assert f(x1) > f(x0)

    # Symplectic Euler exact symbolic identity.
    h = sp.symbols("h", real=True)
    M = sp.Matrix([[1-h**2, h], [-h, 1]])
    J = sp.Matrix([[0, 1], [-1, 0]])
    assert sp.simplify(M.T * J * M - J) == sp.zeros(2)
    assert sp.simplify(M.det()) == 1

    # Energy/objective control at h=1/2, z0=(0,1).
    hq = sp.Rational(1, 2)
    q0 = sp.Rational(0)
    p0 = sp.Rational(1)
    p1 = p0 - hq*q0
    q1 = q0 + hq*p1
    H0 = sp.Rational(1,2)*(q0*q0 + p0*p0)
    H1 = sp.Rational(1,2)*(q1*q1 + p1*p1)
    F0 = sp.Rational(1,2)*q0*q0
    F1 = sp.Rational(1,2)*q1*q1

    assert p1 == 1
    assert q1 == sp.Rational(1,2)
    assert H0 == sp.Rational(1,2)
    assert H1 == sp.Rational(5,8)
    assert F0 == 0
    assert F1 == sp.Rational(1,8)

    # MODULUS-style exact geometry.
    # w=(1,0), tangent v=(0,1), alpha=1.
    theta = math.atan(1.0)
    assert abs(theta - math.pi/4) < 1e-15
    assert abs(theta - 1.0) > 0.2

    print("VARIOPT_EXACT_WITNESS_OK")

Expected output:

    VARIOPT_EXACT_WITNESS_OK

## Claim boundary

This witness proves only the displayed finite and symbolic identities. It does not establish universal convergence, acceleration, optimizer superiority, numerical stability, empirical training gains, or a general equivalence between MODULUS Hyperball and variational integrators.
