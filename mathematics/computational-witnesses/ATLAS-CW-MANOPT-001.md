# ATLAS-CW-MANOPT-001

Exact finite constraint-preservation witness.


## Sphere witness

Let

\[
x=(1,0)^\top,\qquad a=(1,2)^\top,\qquad f(z)=a^\top z.
\]

The ambient gradient is \(a\). Since \(x^\top a=1\), the tangent gradient on the unit circle is

\[
\operatorname{grad}f(x)
=
a-(x^\top a)x
=
(0,2)^\top.
\]

Choose \(\eta=1/2\). Then

\[
\xi
=
-\eta\,\operatorname{grad}f(x)
=
(0,-1)^\top,
\qquad
x^\top\xi=0.
\]

The unconstrained Euclidean update is

\[
x-\eta a
=
(1/2,-1)^\top,
\]

with squared norm

\[
5/4.
\]

It is not feasible.

The raw tangent displacement is

\[
x+\xi=(1,-1)^\top,
\]

with squared norm \(2\). Tangency alone does not make ambient addition feasible.

Apply the normalized retraction

\[
R_x(\xi)
=
\frac{x+\xi}{\|x+\xi\|}
=
\frac1{\sqrt2}(1,-1)^\top.
\]

Then

\[
\|R_x(\xi)\|^2=1.
\]

The retracted point is exactly feasible.

For comparison, the sphere exponential gives

\[
\operatorname{Exp}_x(\xi)
=
(\cos1,-\sin1)^\top.
\]

Both endpoints have unit norm, but they are different.


## Orthogonality-constrained witness

Take

\[
X=I_2,
\qquad
\Xi=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

The tangent condition is exact:

\[
X^\top\Xi+\Xi^\top X
=
\Xi+\Xi^\top
=
0.
\]

The raw tangent displacement is

\[
X+\Xi
=
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix},
\]

with Gram matrix

\[
(X+\Xi)^\top(X+\Xi)=2I.
\]

So the raw displacement is not orthogonal.

Because

\[
\Xi^\top\Xi=I,
\]

the polar retraction is

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

Then

\[
R_X(\Xi)^\top R_X(\Xi)=I.
\]

Exact orthogonality is restored.

For the same skew generator,

\[
e^\Xi
=
\begin{pmatrix}
\cos1&-\sin1\\
\sin1&\cos1
\end{pmatrix}.
\]

The polar retraction is rotation by \(\pi/4\), whereas the exponential is rotation by \(1\) radian.

They are both feasible and different.

## Replay table

| Check | Exact result |
| --- | --- |
| sphere ambient-step squared norm | \(5/4\) |
| sphere raw tangent-step squared norm | \(2\) |
| sphere retraction squared norm | \(1\) |
| sphere exponential endpoint | \((\cos1,-\sin1)\) |
| sphere retraction endpoint | \((1,-1)/\sqrt2\) |
| tangent-condition residual | \(0\) |
| raw constrained-step Gram | \(2I\) |
| polar-retracted Gram | \(I\) |
| polar retraction angle | \(\pi/4\) |
| exponential angle | \(1\) radian |

## Claim boundary

This witness proves exact constraint and endpoint arithmetic for the declared examples.

It does not prove global convergence, rate improvement, better conditioning, or superiority over an unconstrained parameterization.
