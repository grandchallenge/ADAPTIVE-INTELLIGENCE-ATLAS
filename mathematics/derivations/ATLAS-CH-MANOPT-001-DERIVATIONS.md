# MANOPT-001 Derivations — Tangent Gradients, Retractions, and Constraint Preservation

## 1. Sphere tangent space

Let

\[
S^{n-1}
=
\{x\in\mathbb R^n:x^\top x=1\}.
\]

Let \(\gamma(t)\in S^{n-1}\) be a differentiable curve with

\[
\gamma(0)=x,
\qquad
\dot\gamma(0)=\xi.
\]

Because

\[
\gamma(t)^\top\gamma(t)=1,
\]

differentiate at \(t=0\):

\[
2x^\top\xi=0.
\]

Therefore

\[
T_xS^{n-1}
=
\{\xi:x^\top\xi=0\}.
\]

## 2. Sphere tangent projection

Let \(g\in\mathbb R^n\).

Decompose:

\[
g
=
\bigl(g-(x^\top g)x\bigr)
+
(x^\top g)x.
\]

The first term is tangent because

\[
x^\top
\bigl(g-(x^\top g)x\bigr)
=
x^\top g
-
(x^\top g)x^\top x
=
0.
\]

Therefore the orthogonal tangent projection is

\[
\Pi_x(g)
=
g-(x^\top g)x
=
(I-xx^\top)g.
\]

For the induced Euclidean metric, the Riemannian gradient of a restricted ambient objective is this projected gradient.

## 3. Sphere witness gradient

Let

\[
x=(1,0)^\top,
\qquad
a=(1,2)^\top,
\qquad
F(z)=a^\top z.
\]

Then

\[
\nabla F=a.
\]

Since

\[
x^\top a=1,
\]

the tangent gradient is

\[
\operatorname{grad}f(x)
=
a-(x^\top a)x
=
(1,2)^\top-(1,0)^\top
=
(0,2)^\top.
\]

Choose step size

\[
\eta=\frac12.
\]

Then the tangent descent vector is

\[
\xi
=
-\eta\operatorname{grad}f(x)
=
(0,-1)^\top.
\]

Check tangency:

\[
x^\top\xi
=
0.
\]

## 4. Ambient Euclidean step leaves the sphere

The ambient Euclidean step is

\[
x-\eta a
=
(1,0)^\top
-
\frac12(1,2)^\top
=
(1/2,-1)^\top.
\]

Its squared norm is

\[
\frac14+1
=
\frac54.
\]

Therefore

\[
\|x-\eta a\|
=
\frac{\sqrt5}{2}
\neq1.
\]

Thus the unconstrained Euclidean step is not feasible on the unit sphere.

## 5. Raw tangent displacement also need not be feasible

The raw tangent displacement is

\[
x+\xi
=
(1,-1)^\top.
\]

Its squared norm is

\[
2.
\]

Thus

\[
x+\xi
\notin S^1.
\]

Tangency is a local velocity constraint, not a guarantee that ambient addition stays on the manifold.

## 6. Normalized sphere retraction

Define

\[
R_x(\xi)
=
\frac{x+\xi}{\|x+\xi\|}.
\]

For tangent \(\xi\),

\[
x^\top\xi=0.
\]

Hence

\[
\|x+\xi\|^2
=
\|x\|^2
+
2x^\top\xi
+
\|\xi\|^2
=
1+\|\xi\|^2.
\]

Therefore

\[
\|R_x(\xi)\|=1.
\]

For the witness:

\[
R_x(\xi)
=
\frac{(1,-1)^\top}{\sqrt2}.
\]

This is exactly feasible.

## 7. First-order retraction property on the sphere

Consider

\[
R_x(t\xi)
=
\frac{x+t\xi}
{\sqrt{1+t^2\|\xi\|^2}}
\]

for tangent \(\xi\).

At \(t=0\),

\[
R_x(0)=x.
\]

Differentiate:

\[
\left.\frac{d}{dt}R_x(t\xi)\right|_{t=0}
=
\xi.
\]

Therefore the differential at zero is the identity on the tangent space.

This is the local first-order retraction property.

## 8. Sphere exponential comparison

For nonzero tangent \(\xi\),

\[
\operatorname{Exp}_x(\xi)
=
\cos(\|\xi\|)x
+
\sin(\|\xi\|)
\frac{\xi}{\|\xi\|}.
\]

For the witness,

\[
\|\xi\|=1,
\]

so

\[
\operatorname{Exp}_x(\xi)
=
(\cos1,-\sin1)^\top.
\]

The normalized retraction endpoint is

\[
R_x(\xi)
=
(1/\sqrt2,-1/\sqrt2)^\top.
\]

Since

\[
1\neq\pi/4,
\]

these are different points.

Both are feasible.

Thus retraction feasibility does not imply equality with the exponential map.

## 9. Stiefel tangent condition

Let

\[
\operatorname{St}(n,p)
=
\{X\in\mathbb R^{n\times p}:X^\top X=I_p\}.
\]

Let \(X(t)\in\operatorname{St}(n,p)\) be a differentiable curve with

\[
X(0)=X,
\qquad
\dot X(0)=Z.
\]

Differentiate

\[
X(t)^\top X(t)=I.
\]

At \(t=0\),

\[
X^\top Z+Z^\top X=0.
\]

Therefore

\[
T_X\operatorname{St}(n,p)
=
\{Z:X^\top Z+Z^\top X=0\}.
\]

## 10. Embedded-metric Stiefel projection

For ambient matrix \(G\), define

\[
\Pi_X(G)
=
G-X\operatorname{sym}(X^\top G),
\]

where

\[
\operatorname{sym}(A)
=
\frac12(A+A^\top).
\]

Check tangency.

Let

\[
Z=\Pi_X(G).
\]

Then:

\[
X^\top Z
=
X^\top G
-
\operatorname{sym}(X^\top G),
\]

while

\[
Z^\top X
=
G^\top X
-
\operatorname{sym}(X^\top G).
\]

Because

\[
G^\top X
=
(X^\top G)^\top,
\]

the sum is zero.

Hence \(Z\in T_X\operatorname{St}(n,p)\).

## 11. Polar Stiefel retraction

For tangent \(\Xi\),

\[
R_X(\Xi)
=
(X+\Xi)
(I+\Xi^\top\Xi)^{-1/2}.
\]

Using the tangent condition:

\[
X^\top\Xi+\Xi^\top X=0.
\]

Thus

\[
(X+\Xi)^\top(X+\Xi)
=
X^\top X
+
X^\top\Xi
+
\Xi^\top X
+
\Xi^\top\Xi
=
I+\Xi^\top\Xi.
\]

Therefore:

\[
R_X(\Xi)^\top R_X(\Xi)
=
(I+\Xi^\top\Xi)^{-1/2}
(I+\Xi^\top\Xi)
(I+\Xi^\top\Xi)^{-1/2}
=
I.
\]

So the polar retraction lands exactly on the Stiefel manifold.

## 12. Exact \(O(2)\) witness

Let

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
\Omega^\top=-\Omega,
\]

we have

\[
X^\top\Xi+\Xi^\top X
=
\Omega+\Omega^\top
=
0.
\]

Thus \(\Xi\) is tangent.

The raw step is

\[
X+\Xi
=
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix}.
\]

Its Gram matrix is

\[
(X+\Xi)^\top(X+\Xi)
=
2I.
\]

So the raw step is not orthogonal.

Also,

\[
\Xi^\top\Xi=I.
\]

Therefore the polar retraction is

\[
R_X(\Xi)
=
(X+\Xi)(2I)^{-1/2}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix}.
\]

Check:

\[
R_X(\Xi)^\top R_X(\Xi)=I.
\]

Thus exact orthogonality is restored.

## 13. Polar retraction versus matrix exponential

For \(X=I\) and skew-symmetric \(\Omega\), the exponential curve is:

\[
\operatorname{Exp}_I(\Omega)
=
e^\Omega.
\]

For the chosen \(2\times2\) generator,

\[
e^\Omega
=
\begin{pmatrix}
\cos1&-\sin1\\
\sin1&\cos1
\end{pmatrix}.
\]

The polar retraction is

\[
\frac1{\sqrt2}
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix}
=
\begin{pmatrix}
\cos(\pi/4)&-\sin(\pi/4)\\
\sin(\pi/4)&\cos(\pi/4)
\end{pmatrix}.
\]

Since

\[
1\neq\pi/4,
\]

the endpoints differ.

Both are orthogonal.

This is the finite separation between:

- exact constraint preservation;
- exact geodesic/exponential motion.

## 14. Manifold stationarity

For a smooth manifold objective \(f\), first-order stationarity is:

\[
\operatorname{grad}f(x)=0.
\]

For an embedded manifold under induced metric, this means the ambient gradient has no tangent component.

It may still have a normal component.

Thus constrained stationarity differs from ambient Euclidean stationarity.

A constrained stationary point need not be globally optimal.

## 15. Scope

Established here:

- sphere and Stiefel tangent constraints;
- induced-metric tangent projections;
- exact feasibility of normalized sphere and polar Stiefel retractions;
- exact finite sphere and \(O(2)\) examples;
- explicit separation of retraction from exponential motion;
- stationarity as a local tangent condition.

Not established here:

- global convergence for arbitrary objectives;
- superiority of manifold optimization over unconstrained parameterizations;
- a universal best retraction or vector transport;
- any specific GCL optimizer theorem.
