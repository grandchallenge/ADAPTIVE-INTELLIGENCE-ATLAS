# Chapter Specification — ATLAS-CH-MANOPT-001

## Identity

**Title:** Optimization on Manifolds  
**Part:** Optimization, Landscapes, and Learning Rules  
**Status:** specification-ready.  
**Epistemic class:** audited Geometry and First-Order Optimization prerequisites + standard matrix-manifold optimization sources + Atlas synthesis.

## Contract

Develop optimization when parameters or states are constrained to smooth manifolds.

The chapter must cover:

- Euclidean versus Riemannian/tangent gradients;
- tangent projection;
- constrained finite motion;
- exponential maps versus practical retractions;
- sphere optimization;
- Stiefel optimization;
- vector transport at a conceptual level;
- stationarity and optimality boundaries.

The chapter must not identify constraint preservation with optimizer quality.

## Hard prerequisites

- ATLAS-CH-GEOM-001
- ATLAS-CH-OPTBASE-001

Exact prerequisite identities and source scopes are locked in:

sources/source-locks/ATLAS-CH-MANOPT-001.yaml

## Core geometry

For an embedded manifold \(M\subseteq\mathbb R^N\) with induced Euclidean metric, let

\[
\Pi_x:\mathbb R^N\to T_xM
\]

denote orthogonal projection onto the tangent space.

For a smooth ambient extension \(F\) of \(f:M\to\mathbb R\),

\[
\operatorname{grad} f(x)
=
\Pi_x(\nabla F(x)).
\]

This identity is metric-dependent.

It is not a universal formula for arbitrary Riemannian metrics.

## Sphere

For the unit sphere

\[
S^{n-1}
=
\{x\in\mathbb R^n:\|x\|=1\},
\]

the tangent space is

\[
T_xS^{n-1}
=
\{\xi:x^\top\xi=0\}.
\]

The induced-metric tangent projection is

\[
\Pi_x(g)
=
(I-xx^\top)g
=
g-(x^\top g)x.
\]

A normalized retraction is

\[
R_x(\xi)
=
\frac{x+\xi}{\|x+\xi\|}
\]

for \(\xi\in T_xS^{n-1}\) where the denominator is nonzero.

Because \(x^\top\xi=0\),

\[
\|x+\xi\|^2
=
1+\|\xi\|^2.
\]

Therefore \(R_x(\xi)\) lies exactly on the sphere.

## Sphere finite witness

Choose

\[
x=(1,0)^\top,
\qquad
a=(1,2)^\top,
\qquad
f(z)=a^\top z.
\]

Ambient gradient:

\[
\nabla F(x)=a.
\]

Tangent gradient:

\[
\operatorname{grad}f(x)
=
a-(x^\top a)x
=
(0,2)^\top.
\]

Choose \(\eta=1/2\).

Tangent step:

\[
\xi
=
-\eta\operatorname{grad}f(x)
=
(0,-1)^\top.
\]

Raw tangent displacement:

\[
x+\xi
=
(1,-1)^\top
\]

does not lie on the unit sphere.

Normalized retraction:

\[
R_x(\xi)
=
\frac{(1,-1)^\top}{\sqrt2}.
\]

Thus

\[
\|R_x(\xi)\|=1.
\]

By contrast, the ambient Euclidean gradient step is

\[
x-\eta a
=
(1/2,-1)^\top,
\]

with norm

\[
\sqrt5/2\neq1.
\]

The witness separates:

- ambient Euclidean descent;
- tangent descent direction;
- tangent displacement;
- finite retraction.

## Sphere exponential comparison

For \(\xi\in T_xS^{n-1}\),

\[
\operatorname{Exp}_x(\xi)
=
\cos(\|\xi\|)x
+
\sin(\|\xi\|)
\frac{\xi}{\|\xi\|}
\]

for nonzero \(\xi\).

For the witness \(\|\xi\|=1\),

\[
\operatorname{Exp}_x(\xi)
=
(\cos1,-\sin1)^\top.
\]

This differs from

\[
R_x(\xi)
=
(1/\sqrt2,-1/\sqrt2)^\top.
\]

Both are legal sphere points.

The retraction is not the exponential map.

## Stiefel manifold

For

\[
\operatorname{St}(n,p)
=
\{X\in\mathbb R^{n\times p}:X^\top X=I_p\},
\]

the tangent space satisfies

\[
T_X\operatorname{St}(n,p)
=
\{Z:X^\top Z+Z^\top X=0\}.
\]

Under the induced Euclidean metric, one tangent projection is

\[
\Pi_X(G)
=
G-X\,\operatorname{sym}(X^\top G),
\]

where

\[
\operatorname{sym}(A)
=
\frac12(A+A^\top).
\]

## Stiefel polar retraction

For tangent \(\Xi\),

\[
R_X(\Xi)
=
(X+\Xi)
(I+\Xi^\top\Xi)^{-1/2}.
\]

Using the tangent condition,

\[
(X+\Xi)^\top(X+\Xi)
=
I+\Xi^\top\Xi.
\]

Hence

\[
R_X(\Xi)^\top R_X(\Xi)
=
I.
\]

The retraction preserves the Stiefel constraint exactly when the inverse square root is well defined.

## Exact \(O(2)\) witness

Take

\[
X=I_2,
\qquad
\Omega=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
\Xi=\Omega.
\]

Since

\[
\Omega+\Omega^\top=0,
\]

\(\Xi\) is tangent at \(I_2\).

The raw tangent step is

\[
X+\Xi
=
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix},
\]

and

\[
(X+\Xi)^\top(X+\Xi)=2I.
\]

Thus the raw step is not orthogonal.

Because

\[
\Xi^\top\Xi=I,
\]

the polar retraction is

\[
R_X(\Xi)
=
\frac1{\sqrt2}
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix}.
\]

Then

\[
R_X(\Xi)^\top R_X(\Xi)=I.
\]

The exact exponential endpoint is

\[
X\exp(\Omega)
=
\begin{pmatrix}
\cos1&-\sin1\\
\sin1&\cos1
\end{pmatrix}.
\]

The polar retraction is instead rotation by \(\pi/4\).

Therefore legal finite motion does not imply geodesic/exponential motion.

## Retraction boundary

A retraction \(R_x:T_xM\to M\) satisfies locally:

\[
R_x(0_x)=x
\]

and

\[
D R_x(0_x)
=
\operatorname{id}_{T_xM}.
\]

This first-order agreement is the relevant defining local property.

A retraction need not preserve geodesic distance exactly.

## Constrained first-order update

A generic first-order manifold step may be written:

\[
\xi_k
=
-\eta_k \operatorname{grad}f(x_k),
\]

\[
x_{k+1}
=
R_{x_k}(\xi_k).
\]

This notation hides several choices:

- metric;
- gradient construction;
- step-size rule;
- retraction;
- stochastic estimator;
- momentum/optimizer state;
- vector transport if tangent-space history is reused.

## Vector transport boundary

A momentum-like tangent vector at \(x_k\) belongs to \(T_{x_k}M\).

At \(x_{k+1}\), the new tangent space is generally different.

Reusing the same coordinate vector without justification is not automatically geometrically valid.

A vector transport supplies a declared map between tangent spaces.

The chapter develops this concept but does not claim one universal best transport.

## Stationarity

A manifold stationary point satisfies

\[
\operatorname{grad}f(x)=0.
\]

This means there is no first-order descent direction in the tangent space under the declared metric.

It does not imply global optimality.

## Failure boundaries

- Euclidean gradient != Riemannian gradient by default.
- tangent projection != complete optimizer.
- tangent vector != legal finite endpoint.
- retraction != exponential map.
- first-order retraction agreement != geodesic exactness.
- sphere != Stiefel manifold.
- constraint preservation != descent.
- descent != convergence.
- manifold stationarity != global optimality.
- orthogonality preservation != good optimization.
- generic manifold optimization != a specific GCL optimizer.

## Downstream handoff

Direct consumer:

- ATLAS-CH-VARIOPT-001.

VARIOPT may inherit:

- tangent-gradient/retraction language;
- constrained finite-motion discipline;
- metric dependence;
- sphere/Stiefel examples;
- vector-transport distinction.

VARIOPT must independently justify variational, divergence-derived, or symplectic update claims.

## Sources

- [@AbsilMahonySepulchre2008]
- [@EdelmanAriasSmith1998]

Exact source authority and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-MANOPT-001.yaml
