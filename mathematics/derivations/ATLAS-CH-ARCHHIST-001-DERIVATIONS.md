# ATLAS-CH-ARCHHIST-001 — Derivation Packet

## D1. Layered composition

Let

\[
x_{k+1}=F_k(x_k).
\]

Then after \(L\) layers,

\[
x_L
=
F_{L-1}\circ\cdots\circ F_0(x_0).
\]

If every \(F_k\) is differentiable, the chain rule gives

\[
J_{\rm total}
=
J_{F_{L-1}}(x_{L-1})
\cdots
J_{F_0}(x_0).
\]

A feed-forward architecture can therefore be studied as a composition of state transformations.

## D2. Circular convolution and translation equivariance

Work on a periodic discrete signal indexed modulo \(n\).

Define convolution operator

\[
(C_kx)_j
=
\sum_r k_r x_{j-r}.
\]

Define cyclic shift

\[
(S_mx)_j=x_{j-m}.
\]

Then

\[
\begin{aligned}
(C_kS_mx)_j
&=
\sum_r k_r(S_mx)_{j-r}\\
&=
\sum_r k_r x_{j-r-m}\\
&=
(S_m C_kx)_j.
\end{aligned}
\]

Therefore

\[
\boxed{
C_kS_m=S_mC_k.
}
\]

This is exact translation equivariance for the declared periodic convolution model.

Boundary rules, striding, pooling, or other operators can change the result and must be checked separately.

## D3. Exact convolution witness

Use one-site shift

\[
S=
\begin{pmatrix}
0&0&0&1\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.
\]

Take the circulant convolution operator

\[
C=I+2S
=
\begin{pmatrix}
1&0&0&2\\
2&1&0&0\\
0&2&1&0\\
0&0&2&1
\end{pmatrix}.
\]

Because \(C\) is a polynomial in \(S\),

\[
CS=SC.
\]

For

\[
x=(1,2,3,4),
\]

both paths give

\[
CSx
=
SCx
=
(10,9,4,7).
\]

## D4. Recurrent state

A recurrent architecture has state transition

\[
h_{t+1}
=
F(h_t,x_t;\theta).
\]

The parameter \(\theta\) can be reused across time.

For the scalar linear recurrence

\[
h_{t+1}
=
a h_t+b x_t,
\]

repeated substitution gives

\[
h_1=ah_0+bx_0,
\]

\[
h_2=a^2h_0+abx_0+bx_1,
\]

and in general

\[
\boxed{
h_T
=
a^T h_0
+
b
\sum_{j=0}^{T-1}
a^{T-1-j}x_j.
}
\]

This can be proved by induction.

The coefficient

\[
a^{T-1-j}
\]

shows how earlier inputs are transported through repeated state transitions.

## D5. Exact recurrence witness

Use

\[
a=\frac12,
\qquad
b=2,
\qquad
h_0=1,
\]

and

\[
(x_0,x_1,x_2)=(3,-1,4).
\]

Then

\[
h_1=\frac{13}{2},
\]

\[
h_2=\frac54,
\]

and

\[
h_3=\frac{69}{8}.
\]

The closed form gives

\[
\left(\frac12\right)^3
+
2
\left[
\left(\frac12\right)^2 3
+
\left(\frac12\right)(-1)
+
4
\right]
=
\frac{69}{8}.
\]

## D6. Encoder–decoder interface and information loss

Let

\[
z=E(x),
\qquad
\hat y=D(z).
\]

Suppose two inputs satisfy

\[
E(x_1)=E(x_2)=z,
\]

but the required outputs satisfy

\[
y_1\ne y_2.
\]

A deterministic decoder receives the same \(z\) in both cases.

Therefore it must return the same output in both cases:

\[
D(E(x_1))
=
D(E(x_2)).
\]

It cannot equal both distinct targets.

Thus a noninjective encoder can only discard distinctions safely relative to the downstream capability being preserved.

This is an interface-sufficiency statement, not a claim that useful encoders must be injective.

## D7. Highway transform/carry gating

A highway layer has structural form

\[
y
=
T(x)\odot H(x)
+
C(x)\odot x.
\]

A common tied-gate choice is

\[
C(x)=1-T(x).
\]

Then

\[
y
=
T(x)\odot H(x)
+
(1-T(x))\odot x.
\]

If

\[
T(x)=0,
\]

then

\[
\boxed{
y=x.
}
\]

Thus the layer contains an exact carry/identity limit.

If

\[
T(x)=1,
\]

then

\[
y=H(x).
\]

Under the coordinatewise ([0,1]) gate constraint, the gate interpolates between transformed and carried state in this tied formulation.

This is not algebraically identical to a ResNet block.

The highway architecture uses learned multiplicative gating of transform and carry paths.

## D8. Exact highway witness

Take scalar

\[
x=2,
\qquad
H(x)=5,
\qquad
T=\frac14,
\qquad
C=1-T=\frac34.
\]

Then

\[
y
=
\frac14\cdot5
+
\frac34\cdot2
=
\frac{11}{4}.
\]

At the exact carry limit,

\[
T=0,
\qquad
C=1,
\]

we obtain

\[
y=x=2.
\]

At the exact transform limit,

\[
T=1,
\qquad
C=0,
\]

we obtain

\[
y=H(x)=5.
\]

## D9. Residual update

A residual block has form

\[
x_{k+1}
=
x_k+F_k(x_k).
\]

Differentiate:

\[
\boxed{
J_k
=
I+J_{F_k}(x_k).
}
\]

Across \(L\) blocks,

\[
J_{\rm total}
=
\left(I+J_{F_{L-1}}\right)
\cdots
\left(I+J_{F_0}\right),
\]

with Jacobians evaluated along the realized trajectory.

The identity contribution is exact.

It does not by itself bound the product norm or condition number.

## D10. Linear residual witness

Let

\[
F(x)=Ax,
\qquad
A=
\begin{pmatrix}
1&2\\
-1&3
\end{pmatrix}.
\]

The branch Jacobian is

\[
A.
\]

The residual block is

\[
x\mapsto x+Ax,
\]

with Jacobian

\[
I+A
=
\begin{pmatrix}
2&2\\
-1&4
\end{pmatrix}.
\]

If the branch vanishes,

\[
A=0,
\]

then

\[
I+A=I.
\]

The block transports state exactly unchanged.

## D11. Residual systems as discrete state evolution

Write

\[
x_{k+1}-x_k
=
F_k(x_k).
\]

This makes the increment explicit.

If one further writes

\[
F_k(x)=h f_k(x),
\]

the update resembles an Euler-like step.

But the architecture alone does not imply:

- one fixed autonomous vector field;
- small \(h\);
- convergence to a continuous limit;
- numerical stability.

Therefore the legitimate statement is:

> residual systems admit a dynamical or integrator lens.

The stronger ODE identity requires additional construction.

## D12. Explicit continuous-depth architecture

A Neural ODE specifies evolution directly:

\[
\frac{dz}{dt}
=
f(z,t;\theta),
\]

and defines output through numerical solution over a time interval.

Here continuous depth is part of the architecture by construction.

This provides a later explicit bridge between neural computation and differential-equation models.

It does not retrospectively turn every residual network into the exact flow of one ODE.

## Claim boundary

This packet establishes exact composition, periodic convolution equivariance, linear recurrence unrolling, encoder-interface sufficiency limits, and residual Jacobian identities.

The historical narrative that these architectural mechanisms form a progression toward dynamical interpretation is Atlas synthesis; it is not a theorem of architectural evolution or a performance ranking.
