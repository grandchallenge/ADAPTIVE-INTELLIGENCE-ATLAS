# ATLAS-CH-NORMREP-001 — Derivation Packet

## D1. Normalization map

For nonzero

\[
x\in\mathbb R^d,
\]

define

\[
N(x)
=
\frac{x}{\|x\|_2}.
\]

Let

\[
u=N(x).
\]

Write

\[
r=\|x\|_2.
\]

Then

\[
N(x)=r^{-1}x.
\]

Using

\[
\nabla r
=
\frac{x}{\|x\|_2}
=
u,
\]

the differential is

\[
dN_x[\delta]
=
\frac{\delta}{r}
-
\frac{x}{r^2}
\,dr_x[\delta].
\]

Since

\[
dr_x[\delta]
=
u^\top\delta,
\]

we obtain

\[
dN_x[\delta]
=
\frac{1}{r}
\left(
I-uu^\top
\right)\delta.
\]

Therefore

\[
\boxed{
J_N(x)
=
\frac{1}{\|x\|_2}
\left(
I-uu^\top
\right).
}
\]

The matrix in parentheses is the orthogonal projector onto the tangent space of the sphere at \(u\).

## D2. Radial annihilation

The radial direction is proportional to \(u\).

Because

\[
(I-uu^\top)u
=
u-u(u^\top u)
=
0,
\]

normalization removes first-order radial perturbations:

\[
J_N(x)u=0.
\]

Equivalently,

\[
J_N(x)x=0.
\]

This does not say radial information was irrelevant.

It says the normalization map discards it.

## D3. Tangential scaling

If

\[
u^\top\delta=0,
\]

then \(\delta\) is tangent and

\[
J_N(x)\delta
=
\frac{\delta}{\|x\|_2}.
\]

Thus normalization keeps the tangent direction but rescales it by the inverse radius of the pre-normalized vector.

## D4. Exact witness at x=(3,4)

For

\[
x=(3,4),
\qquad
\|x\|_2=5,
\]

we have

\[
u=(3/5,4/5).
\]

Hence

\[
J_N(x)
=
\frac{1}{5}
\left(
I-
\begin{pmatrix}
9/25&12/25\\
12/25&16/25
\end{pmatrix}
\right)
=
\begin{pmatrix}
16/125&-12/125\\
-12/125&9/125
\end{pmatrix}.
\]

Direct computation gives

\[
J_N(x)x=0.
\]

For the tangent vector

\[
t=(-4,3),
\]

since

\[
x^\top t=0,
\]

we obtain

\[
J_N(x)t
=
(-4/5,3/5).
\]

## D5. Chord and angle on the unit sphere

For unit vectors \(u,v\),

\[
\|u-v\|_2^2
=
(u-v)^\top(u-v)
=
2-2u^\top v.
\]

If

\[
u^\top v=\cos\theta,
\]

then

\[
\boxed{
\|u-v\|_2^2
=
2-2\cos\theta.
}
\]

Thus Euclidean chord distance and angular distance are monotonically related on the unit sphere, but they are not numerically identical.

## D6. Sixty-degree witness

Take

\[
a=(1,0),
\]

and

\[
b=
\left(
\frac12,
\frac{\sqrt3}{2}
\right).
\]

Then

\[
a^\top b=\frac12,
\]

so

\[
\theta=\frac{\pi}{3}.
\]

The chord length satisfies

\[
\|a-b\|_2=1.
\]

The SLERP midpoint is

\[
\operatorname{SLERP}(a,b;1/2)
=
\left(
\frac{\sqrt3}{2},
\frac12
\right),
\]

which remains unit norm and lies halfway along the great-circle arc.

## D7. Normalized retraction

For unit \(u\) and tangent \(\xi\) satisfying

\[
u^\top\xi=0,
\]

define

\[
R_u(\xi)
=
\frac{u+\xi}{\|u+\xi\|_2}.
\]

This maps the ambient step back to the sphere.

It is a retraction, not generally the exact exponential map.

## D8. Radial-information counterexample

Consider two nonzero vectors

\[
x_1=(1,0),
\qquad
x_2=(2,0).
\]

Normalization gives

\[
N(x_1)=N(x_2)=(1,0).
\]

Any downstream target that depends on the original norm, for example

\[
y=\|x\|_2,
\]

cannot be recovered from the normalized representation alone.

Therefore normalization builds an invariance to positive radial scaling.

That invariance is beneficial only when radial information is intentionally irrelevant or supplied elsewhere.

## D9. Scope of nGPT connection

The nGPT papers study architectures in which representations and parameter vectors are constrained to hyperspherical geometry.

Those papers are empirical/architectural evidence for one realization of the geometry developed here.

They do not establish that every useful Transformer should be normalized or that radial degrees of freedom are universally redundant.

The public GCL MODULUS Hyperball module implements tangent projection, angular/update scaling and retraction machinery and explicitly describes itself as intended for nGPT / MODULUS-style training.

That is implementation-context evidence only.

## Claim boundary

This packet establishes the normalization differential, radial/tangent decomposition, chord-angle identity, one SLERP witness, and one explicit information-loss counterexample.

It does not establish universal superiority of hyperspherical representations or reproduce the empirical claims of the nGPT papers.
