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
