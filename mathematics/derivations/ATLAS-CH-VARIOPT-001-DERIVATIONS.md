# ATLAS-CH-VARIOPT-001 — Derivation Packet

## D1. Bregman divergence

Let \(\phi\) be differentiable and strictly convex.

Define:

\[
D_\phi(y,x)
=
\phi(y)-\phi(x)-\langle\nabla\phi(x),y-x\rangle.
\]

Convexity gives:

\[
D_\phi(y,x)\ge0.
\]

Equality conditions depend on the strict-convexity/domain hypotheses.

Symmetry is not assumed.

## D2. Exact asymmetry

Take:

\[
\phi(x)=e^x.
\]

Then:

\[
D_\phi(1,0)
=
e-1-(1)(1)
=
e-2.
\]

Reverse the arguments:

\[
D_\phi(0,1)
=
1-e-e(0-1)
=
1.
\]

Hence:

\[
D_\phi(1,0)\ne D_\phi(0,1).
\]

Therefore this Bregman divergence is not a metric.

## D3. Local Hessian expansion

Let \(y=x+\delta\).

Taylor expansion gives:

\[
\phi(x+\delta)
=
\phi(x)
+
\nabla\phi(x)^\top\delta
+
\frac12\delta^\top\nabla^2\phi(x)\delta
+
O(\|\delta\|^3).
\]

Subtracting the affine part:

\[
D_\phi(x+\delta,x)
=
\frac12\delta^\top\nabla^2\phi(x)\delta
+
O(\|\delta\|^3).
\]

For \(\phi(x)=e^x\) at \(x=0\):

\[
D_\phi(\delta,0)
=
e^\delta-1-\delta
=
\frac12\delta^2+\frac16\delta^3+\cdots.
\]

## D4. Mirror/Bregman proximal stationarity

Consider:

\[
\Psi(x)
=
\eta\langle g_k,x\rangle
+
D_\phi(x,x_k).
\]

Differentiate with respect to the first argument:

\[
\nabla\Psi(x)
=
\eta g_k
+
\nabla\phi(x)
-
\nabla\phi(x_k).
\]

At an interior stationary minimizer:

\[
\nabla\phi(x_{k+1})
=
\nabla\phi(x_k)-\eta g_k.
\]

The update is linear in dual coordinates \(\nabla\phi\), not necessarily in primal coordinates.

## D5. Euclidean generator

Let:

\[
\phi(x)=\frac12\|x\|^2.
\]

Then:

\[
\nabla\phi(x)=x,
\]

and:

\[
D_\phi(y,x)
=
\frac12\|y-x\|^2.
\]

Therefore:

\[
x_{k+1}
=
x_k-\eta g_k.
\]

## D6. Entropic generator

For scalar \(x>0\):

\[
\phi(x)=x\log x-x.
\]

Then:

\[
\nabla\phi(x)=\log x.
\]

The mirror stationarity equation gives:

\[
\log x_{k+1}
=
\log x_k-\eta g_k,
\]

so:

\[
x_{k+1}
=
x_k e^{-\eta g_k}.
\]

For:

\[
x_k=1,
\qquad
\eta=1,
\qquad
g_k=\log2,
\]

we obtain:

\[
x_{k+1}
=
e^{-\log2}
=
\frac12.
\]

## D7. Divergence-derived non-descent control

Take objective:

\[
f(x)=\frac12(x-2)^2.
\]

At:

\[
x_0=0,
\]

the gradient is:

\[
g_0=-2.
\]

For Euclidean Bregman generator and step:

\[
\eta=3,
\]

the exact update is:

\[
x_1
=
x_0-\eta g_0
=
6.
\]

Objective values:

\[
f(0)=2,
\]

\[
f(6)=\frac12(4)^2=8.
\]

Thus the Bregman-proximal linearized update increased the objective under the declared step.

No contradiction occurs: descent requires additional assumptions/step control.

## D8. Continuous action

For path \(q(t)\):

\[
\mathcal A[q]
=
\int L(q,\dot q,t)\,dt.
\]

First variation under endpoint-fixed perturbations yields:

\[
\frac{d}{dt}
\frac{\partial L}{\partial\dot q}
-
\frac{\partial L}{\partial q}
=
0.
\]

This stationarity statement concerns the action functional.

## D9. Discrete action

Let:

\[
\mathcal A_d
=
\sum_{k=0}^{N-1}
L_d(q_k,q_{k+1};h).
\]

Vary interior \(q_k\).

The coefficient of \(\delta q_k\) is:

\[
D_2L_d(q_{k-1},q_k)
+
D_1L_d(q_k,q_{k+1}).
\]

Discrete stationarity gives:

\[
D_2L_d(q_{k-1},q_k)
+
D_1L_d(q_k,q_{k+1})
=
0.
\]

## D10. Harmonic-oscillator discrete Lagrangian

Take continuous:

\[
L(q,\dot q)
=
\frac12\dot q^2-\frac12q^2.
\]

Choose:

\[
L_d(q_k,q_{k+1};h)
=
\frac{(q_{k+1}-q_k)^2}{2h}
-
\frac h2 q_k^2.
\]

Then:

\[
D_2L_d(q_{k-1},q_k)
=
\frac{q_k-q_{k-1}}{h}.
\]

Also:

\[
D_1L_d(q_k,q_{k+1})
=
-\frac{q_{k+1}-q_k}{h}
-hq_k.
\]

Set the sum to zero:

\[
\frac{q_k-q_{k-1}}h
-
\frac{q_{k+1}-q_k}h
-hq_k
=
0.
\]

Multiply by \(h\):

\[
q_k-q_{k-1}-q_{k+1}+q_k-h^2q_k=0.
\]

Therefore:

\[
q_{k+1}
=
(2-h^2)q_k-q_{k-1}.
\]

## D11. Momentum variable

Define:

\[
p_k
=
\frac{q_k-q_{k-1}}h.
\]

Then:

\[
p_{k+1}
=
\frac{q_{k+1}-q_k}h.
\]

Using the recurrence:

\[
p_{k+1}
=
\frac{q_k-q_{k-1}}h
-hq_k
=
p_k-hq_k.
\]

Then:

\[
q_{k+1}
=
q_k+h p_{k+1}.
\]

Thus the discrete variational recurrence is exactly the declared symplectic-Euler map.

## D12. Symplectic-Euler matrix

Write:

\[
z_k=
\begin{pmatrix}
q_k\\
p_k
\end{pmatrix}.
\]

Then:

\[
z_{k+1}
=
M_h z_k
\]

with:

\[
M_h
=
\begin{pmatrix}
1-h^2 & h\\
-h & 1
\end{pmatrix}.
\]

Its determinant is:

\[
\det M_h
=
(1-h^2)(1)-h(-h)
=
1.
\]

## D13. Exact symplectic identity

For:

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

direct multiplication gives:

\[
M_h^\top J M_h=J.
\]

Thus the map preserves the canonical two-form exactly for every scalar \(h\).

## D14. Energy control

Take:

\[
h=\frac12,
\qquad
(q_0,p_0)=(0,1).
\]

Then:

\[
p_1
=
1-\frac12(0)
=
1,
\]

\[
q_1
=
0+\frac12(1)
=
\frac12.
\]

For:

\[
H(q,p)=\frac12(q^2+p^2),
\]

we have:

\[
H_0=\frac12,
\]

\[
H_1
=
\frac12\left(\frac14+1\right)
=
\frac58.
\]

Therefore:

\[
H_1-H_0
=
\frac18.
\]

The map is exactly symplectic but not exactly energy preserving.

## D15. Objective control

Let:

\[
F(q)=\frac12q^2.
\]

For the same step:

\[
F(q_0)=0,
\]

\[
F(q_1)=\frac12\left(\frac12\right)^2
=
\frac18.
\]

Hence structure preservation does not imply one-step objective descent.

## D16. Source-scoped Bregman Lagrangian

Wibisono, Wilson, and Jordan define a Bregman Lagrangian of the form:

\[
\mathcal L(X,V,t)
=
e^{\alpha_t+\gamma_t}
\left(
D_h(X+e^{-\alpha_t}V,X)
-
e^{\beta_t}f(X)
\right),
\]

under declared time-dependent scaling functions and regularity assumptions.

The source derives accelerated continuous-time optimization dynamics and a systematic relation to discrete algorithms.

VARIOPT uses this as established source-scoped theory.

It does not transfer acceleration guarantees to arbitrary discrete updates.

## D17. MODULUS tangent projection

At the exact protected programme snapshot, Hyperball receives a base optimizer proposal \(u\) at parameter \(w\).

It computes:

\[
u_{\parallel}
=
\frac{\langle u,w\rangle}{\|w\|^2}w,
\]

and:

\[
u_\perp
=
u-u_{\parallel}.
\]

This is the Euclidean tangent projection onto the sphere through \(w\), up to the implementation epsilon and chosen grouping axes.

## D18. MODULUS target-angle branch

The current implementation sets:

\[
\mathrm{desired}
=
\alpha\|w\|.
\]

It rescales the tangent proposal so its norm approximately equals this desired value.

For unit \(w\) and unit tangent \(v\), the pre-retraction point is:

\[
w+\alpha v.
\]

Sphere retraction gives:

\[
R(w,\alpha v)
=
\frac{w+\alpha v}{\sqrt{1+\alpha^2}}.
\]

## D19. Exact finite MODULUS-style angle

Let:

\[
w=(1,0),
\qquad
u=(1,1).
\]

Then:

\[
u_\perp=(0,1).
\]

For \(\alpha=1\), the sphere-retracted update is:

\[
w_+
=
\frac{(1,1)}{\sqrt2}.
\]

Its angle from \(w\) satisfies:

\[
\cos\theta
=
\frac1{\sqrt2}.
\]

Therefore:

\[
\theta=\frac\pi4.
\]

The finite angle is not \(1\) radian.

## D20. General angle formula

For orthonormal \(w,v\):

\[
w_+
=
\frac{w+\alpha v}{\sqrt{1+\alpha^2}}.
\]

Then:

\[
\cos\theta
=
\frac1{\sqrt{1+\alpha^2}},
\]

\[
\sin\theta
=
\frac{\alpha}{\sqrt{1+\alpha^2}}.
\]

Hence for \(\alpha\ge0\):

\[
\theta=\arctan\alpha.
\]

As:

\[
\alpha\to0,
\]

\[
\arctan\alpha
=
\alpha-\frac{\alpha^3}{3}+O(\alpha^5).
\]

Thus the tangent-norm knob is first-order equivalent to an angular step for small \(\alpha\), but not an exact finite geodesic-angle parameterization.

## D21. Geometry-to-update versus variational derivation

MODULUS supplies an explicit geometric transformation:

\[
u
\to
u_\perp
\to
\tilde u
\to
R_w(\tilde u).
\]

This is a legitimate geometry-derived update pipeline.

No discrete action or Bregman objective is identified in the protected implementation evidence.

Therefore VARIOPT must not describe Hyperball as a variational integrator or Bregman-Lagrangian discretization.

## D22. Authority typing

The GCL repository profile states that MODULUS has:

- versioned implementation authority;
- benchmark authority;
- empirical-evidence authority;

but no claim-promotion or certification authority.

Thus programme observations can motivate or instantiate Atlas concepts without becoming established mathematical theorems.

## Durable propositions

1. Bregman divergence can induce local Hessian geometry without becoming a global metric.
2. A mirror/Bregman-proximal linearized step is a dual-coordinate update determined by the generator.
3. Divergence-derived updates need not be one-step descent methods without further conditions.
4. A discrete action yields a discrete Euler-Lagrange recurrence.
5. The declared discrete oscillator action yields symplectic Euler exactly.
6. The resulting map is exactly symplectic but not exactly energy preserving.
7. Symplecticity does not imply objective descent.
8. The Bregman Lagrangian is established source-scoped continuous-time optimization theory, not an arbitrary discretization guarantee.
9. MODULUS Hyperball is an exact programme example of explicit geometry-to-update construction.
10. The current Hyperball target-angle branch controls pre-retraction tangent norm; finite post-retraction angle is \(\arctan\alpha\) in the exact orthogonal unit witness.
11. Programme implementation evidence remains distinct from general mathematical authority.

## Claim boundary

This packet establishes the displayed identities and finite constructions only. It does not prove universal convergence, acceleration, numerical stability, accuracy, energy conservation, optimizer superiority, or empirical model-training gains.
