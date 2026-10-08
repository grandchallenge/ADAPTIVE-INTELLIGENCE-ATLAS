# ATLAS-CH-NETNUM-001 — Formal and Derivation Packet

## 1. Purpose

This packet identifies the exact mathematical interface required before residual-network depth may be analyzed with numerical-analysis language.

The guiding distinction is:

`discrete residual map`

is not automatically the same object as

`numerical approximation to a declared continuous flow`.

## 2. Residual block and Euler syntax

A residual block has the form

`x_{k+1}=x_k+F_k(x_k)`.

For a nonautonomous ODE

`dx/dt=f(t,x)`,

explicit Euler at time `t_k` with step `h_k` is

`x_{k+1}=x_k+h_k f(t_k,x_k)`.

The two have identical syntax after the modeling declaration

`F_k(x)=h_k f(t_k,x)`.

That declaration supplies semantics not present in the residual algebra itself.

## 3. What must be fixed for a discretization claim

A theorem-grade discretization statement requires at least:

- a continuous problem `dx/dt=f(t,x)`;
- a time grid `t_0<...<t_N`;
- step sizes `h_k=t_{k+1}-t_k`;
- a family of discrete maps `Psi_{h_k}`;
- a norm or metric for error;
- regularity assumptions sufficient for the claimed order;
- a refinement procedure that keeps the continuous problem fixed.

Without these objects, local truncation error and convergence order have no defined referent.

## 4. Autonomous and nonautonomous cases

If

`F_k(x)=h f(x)`

for a common `f`, the blocks have the fixed-step Euler form for an autonomous ODE.

If

`F_k(x)=h_k f(t_k,x)`,

the blocks can represent Euler samples of a nonautonomous field.

Therefore weight sharing is not a universal requirement for a continuous-time interpretation.

Conversely, shared weights do not by themselves prove that the learned block is a faithful discretization of a meaningful ODE.

## 5. Local defect

Let `Phi_{h_k}(t_k,x)` denote the exact flow map.

Let

`Psi_k(x)=x+h_k f(t_k,x)`.

Starting one step from the exact state,

\[
\delta_{k+1}
=
\Phi_{h_k}(t_k,x(t_k))
-
\Psi_k(x(t_k)).
\]

If the exact solution has a bounded third derivative on the time step, Taylor expansion gives

\[
x(t_k+h_k)
=
x(t_k)
+
h_k f(t_k,x(t_k))
+
\frac{h_k^2}{2}x''(t_k)
+
O(h_k^3).
\]

With only a continuously differentiable solution derivative \(x''\), the weaker remainder is \(o(h_k^2)\).

Hence, under the stated bounded-third-derivative condition,

\[
\delta_{k+1}
=
\frac{h_k^2}{2}x''(t_k)
+
O(h_k^3).
\]

Thus explicit Euler has local defect `O(h_k^2)` under the needed smoothness assumptions.

The phrase "local defect of a residual layer" is justified only if the residual layer has been bound to this numerical interface.

## 6. Global error

Define

`e_k=x(t_k)-x_k`.

A repeated numerical scheme propagates both:

- new local defect;
- inherited prior error.

For a one-step method with suitable Lipschitz propagation,

\[
\|e_{k+1}\|
\le
(1+C h_k)\|e_k\|+\|\delta_{k+1}\|,
\]

for an appropriate finite-time constant `C`.

Repeated application yields the familiar principle:

local defect `O(h^{p+1})` plus suitable stability can yield global error `O(h^p)`.

This result is inherited from NUMERICS-001.

It cannot be inferred from small per-layer residuals alone.

## 7. Depth is not automatically mesh refinement

Suppose a 12-layer network is replaced by a 24-layer network.

That does not by itself halve a numerical step size.

The deeper model may have:

- different parameters;
- different residual scales;
- different normalization;
- different feature dimensions;
- different effective dynamics.

A numerical refinement family must specify how the deeper architecture corresponds to a finer mesh for the same reference evolution.

## 8. Residual scale versus step size

Consider

`x_{k+1}=x_k+alpha_k G_k(x_k)`.

If

`G_k(x)=f(t_k,x)`

for a declared field, then `alpha_k` may be interpreted as `h_k`.

If `G_k` itself changes arbitrarily when `alpha_k` changes, then `alpha_k` is merely a scale parameter.

A step-size interpretation requires a quantity that varies while the underlying vector-field semantics remain fixed in the relevant sense.

## 9. Scalar linear flow

Take

`x'=lambda x`.

The exact step is

`Phi_h(x)=e^{h lambda}x`.

Euler gives

`Psi_h(x)=(1+h lambda)x`.

The local one-step error is exactly

`[e^{h lambda}-(1+h lambda)]x`.

Expanding,

`e^{h lambda}-(1+h lambda)
=
(h lambda)^2/2
+
(h lambda)^3/6
+...`.

Thus the leading local error is quadratic in `h`.

## 10. Stability function

Define

`z=h lambda`.

Euler amplification is

`R(z)=1+z`.

The standard non-growth absolute-stability condition is

`|R(z)|<=1`.

For `lambda=-1` and real positive `h`,

`|1-h|<=1`

if and only if

`0<=h<=2`.

Strict asymptotic decay requires

`|1-h|<1`,

which for real `h` is

`0<h<2`.

At `h=2`, the discrete factor is `-1`: non-growing but non-decaying.

The exact continuous flow decays for every `h>0`.

The discrete Euler flow therefore need not share that decay property.

This is the cleanest demonstration that continuous stability and numerical stability are different claims.

## 11. Finite-horizon refinement witness

Set

`lambda=-1`,
`x(0)=1`,
`T=1`,
`h=1/N`.

Then Euler gives

`x_N=(1-1/N)^N`.

Exact flow gives

`x(1)=e^{-1}`.

For declared finite values:

`N=2: x_N=1/4`.

`N=4: x_N=(3/4)^4=81/256`.

`N=8: x_N=(7/8)^8=5764801/16777216`.

These are exact rational discrete values.

The exact errors are

`e^{-1}-1/4`,
`e^{-1}-81/256`,
`e^{-1}-5764801/16777216`.

Numerically they decrease over these three cases.

That finite observation is not itself the convergence theorem.

The convergence theorem comes from the numerical-analysis prerequisite under its assumptions.

## 12. Forward instability witness

For the same continuous system and `h=3`:

exact factor:

`e^{-3}`;

Euler factor:

`1-3=-2`.

Therefore an exact decaying mode is converted into a discrete alternating mode whose magnitude doubles each step.

This is numerical instability of the forward map.

It says nothing directly about stochastic-gradient optimization.

## 13. Perturbation propagation

For a nonlinear residual block

`Psi_k(x)=x+F_k(x)`,

the local Jacobian is

`J_{Psi_k}(x)=I+J_{F_k}(x)`.

A small perturbation obeys, to first order,

`delta x_{k+1}
approximately
J_{Psi_k}(x_k) delta x_k`.

Across depth,

`delta x_N
approximately
J_{Psi_{N-1}}
...
J_{Psi_0}
delta x_0`.

This is a forward sensitivity product.

Its norm can grow even if each residual branch is individually small.

It is related to, but not identical with, the backward optimization problem.

## 14. Numerical stability versus training stability

Numerical stability asks how perturbations/errors behave under the declared discrete approximation.

Training stability can refer to:

- gradient explosion or vanishing;
- optimizer divergence;
- sensitivity to learning rate;
- minibatch noise;
- loss-surface behavior.

The two can interact because both involve Jacobians and repeated maps.

They remain different claims.

A stable forward numerical scheme does not automatically imply stable parameter optimization.

## 15. Invertibility versus time reversibility

For `x'=-x`,

`Psi_h(x)=(1-h)x`.

If `h!=1`, this map is invertible:

`Psi_h^{-1}(x)=x/(1-h)`.

But the same numerical formula with negative step gives

`Psi_{-h}(x)=(1+h)x`.

Compose:

`Psi_{-h}(Psi_h(x))
=
(1+h)(1-h)x
=
(1-h^2)x`.

For nonzero `h`, this is not `x`.

Therefore explicit Euler is generally not time symmetric even where its forward step is invertible.

## 16. Exact reversibility witness

At `h=1/2`:

`Psi_h(x)=(1/2)x`.

Its true inverse is

`Psi_h^{-1}(x)=2x`.

The negative-step Euler map is

`Psi_{-h}(x)=(3/2)x`.

Forward then negative-step:

`Psi_{-h}(Psi_h(x))=(3/4)x`.

Thus:

- forward map invertible: yes;
- recovered by same method with `-h`: no;
- time reversible/symmetric: no.

## 17. Computational reversibility is another object

A network can be designed so that earlier activations can be reconstructed exactly from later activations.

That is computational reversibility.

It can hold for maps that are not symmetric numerical integrators.

Conversely, a symmetric numerical method can still be implemented in a way that stores or loses computational information.

The semantics must remain separate.

## 18. Modified-equation lens

A discrete map may sometimes be interpreted as approximating a nearby modified differential equation.

Lu et al. use numerical differential-equation ideas, including modified-equation reasoning, to motivate deep architectures.

This is a useful bridge.

It does not create a unique continuous model for an arbitrary trained network.

Modified equations are interpretation tools under a declared asymptotic regime.

## 19. Residual and Neural ODE boundary

A residual network directly specifies a finite composition of maps.

A Neural ODE specifies a continuous evolution and delegates trajectory construction to a numerical solver.

The architectures may be related through discretization limits.

They are not identical objects.

This distinction is inherited from ARCHHIST-001 and remains mandatory.

## 20. Downstream interface

ADAPTDEPTH-001 may consume:

- `Psi_k` versus `Phi_h`;
- local defect versus global error;
- refinement-family requirements;
- step-size semantics;
- stability-function reasoning.

BOUNDARYPROBE-001 may consume:

- `J_{Psi_k}` as one-step perturbation propagation;
- accumulated Jacobian products;
- the distinction between local sensitivity and global behavior.

Neither downstream chapter may strengthen the present claims without additional support.
