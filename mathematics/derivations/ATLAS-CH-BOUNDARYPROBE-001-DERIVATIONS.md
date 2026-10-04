# ATLAS-CH-BOUNDARYPROBE-001 — Formal and Derivation Packet

## 1. Local component map

Let

`F:R^n -> R^m`

be differentiable at `x`.

Write

`J=J_F(x)`.

Differentiability means:

`F(x+delta)=F(x)+J delta+r(delta)`

with

`||r(delta)||/||delta|| -> 0`

as `delta -> 0`.

The Jacobian is therefore the first-order local map from input perturbations to output perturbations.

## 2. JVP

For tangent direction `v in R^n`:

`JVP_F(x;v)=Jv`.

Equivalently:

`Jv
=
d/d epsilon F(x+epsilon v)|_{epsilon=0}`.

A JVP answers:

> what first-order output perturbation follows from this input direction?

Forward-mode algorithmic differentiation can compute this product through the computational graph without explicitly materializing the full Jacobian.

## 3. VJP

For output covector `w in R^m`:

`VJP_F(x;w)=J^T w`.

Let

`ell(x)=w^T F(x)`.

Then by the chain rule:

`grad_x ell(x)=J^T w`.

A VJP answers:

> how does an output-side linear sensitivity pull back to the input?

Reverse-mode algorithmic differentiation computes such pullbacks efficiently for scalar or low-dimensional output objectives.

## 4. Composition

Let

`F:R^n->R^m`

and

`G:R^m->R^p`.

Then:

`J_{G o F}(x)
=
J_G(F(x))J_F(x)`.

For tangent `v`:

`J_{G o F}(x)v
=
J_G(F(x))(J_F(x)v)`.

For output covector `w`:

`J_{G o F}(x)^T w
=
J_F(x)^T(J_G(F(x))^T w)`.

Thus JVPs naturally propagate forward, while VJPs naturally propagate backward.

## 5. Local Euclidean gain

Inherited from LINALG-001:

`||J||_2=sigma_max(J)`.

For every perturbation direction `delta`:

`||J delta||_2
<=
||J||_2 ||delta||_2`.

The bound is exact in a dominant right-singular direction.

For the nonlinear component itself:

`F(x+delta)-F(x)
=
J delta+r(delta)`.

Therefore the Jacobian norm controls only the first-order term unless a larger-region derivative bound or other nonlinear argument is supplied.

## 6. Interface composition and amplification

For a composition:

`x -> F -> y -> G -> z`,

first-order perturbations satisfy:

`delta y approx J_F delta x`;

`delta z approx J_G delta y
approx
J_G J_F delta x`.

Hence:

`||delta z||_2
lesssim
||J_G||_2 ||J_F||_2 ||delta x||_2`

locally, with nonlinear remainder terms suppressed by the approximation sign.

This product bound is sufficient as a local diagnostic.

It is not a proof that the full nonlinear composition has the same global Lipschitz constant.

## 7. Power iteration for a singular-value probe

Define:

`A=J^T J`.

Then `A` is symmetric positive semidefinite.

Its eigenvalues are:

`sigma_i(J)^2`.

Power iteration applies:

`u_{k+1}=A z_k`;

`z_{k+1}=u_{k+1}/||u_{k+1}||_2`.

The Rayleigh quotient is:

`rho_k=z_k^T A z_k`.

When the iteration aligns with the dominant eigenspace:

`rho_k -> sigma_max(J)^2`.

Then:

`hat sigma_k=sqrt(rho_k)`.

## 8. Convergence condition

Let the eigenpairs of `A` be:

`lambda_1 > lambda_2 >= ... >= 0`

with orthonormal eigenvectors `q_i`.

Expand the initial vector:

`z_0=sum_i c_i q_i`.

Then:

`A^k z_0
=
sum_i c_i lambda_i^k q_i`.

If:

`c_1 != 0`,

the dominant component eventually controls the normalized iterate, with relative subdominant factor governed by powers of:

`|lambda_2/lambda_1|`

in the simple dominant-eigenvalue case.

If:

`c_1=0`,

ordinary power iteration cannot create a component in the missing dominant eigenspace.

## 9. Finite estimate is not an upper certificate

For symmetric positive semidefinite `A`, a Rayleigh quotient satisfies:

`rho(z)
=
z^T A z / z^T z
<=
lambda_max(A)`.

Thus:

`sqrt(rho(z)) <= sigma_max(J)`.

A finite Rayleigh estimate can therefore underestimate the true operator norm.

Without an independent error bound or certified enclosure, it is not a safe upper certificate.

## 10. Exact nonlinear witness

Define:

`F(x_1,x_2)
=
(x_1^2+x_2,
 x_1+2x_2)`.

At:

`x_0=(1,1)`,

`F(x_0)=(2,3)`.

Jacobian:

`J(x_1,x_2)
=
[[2x_1,1],
 [1,2]]`.

Therefore:

`J=J(x_0)
=
[[2,1],
 [1,2]]`.

## 11. Exact singular structure

Because `J` is symmetric positive definite:

- eigenvector `q_1=(1,1)/sqrt(2)` has eigenvalue 3;
- eigenvector `q_2=(1,-1)/sqrt(2)` has eigenvalue 1.

Hence the singular values are:

`3,1`.

Therefore:

`||J||_2=3`.

Also:

`A=J^T J=J^2=[[5,4],[4,5]]`

with eigenvalues:

`9,1`.

## 12. Exact JVP witness

Take:

`v=(1,1)`.

Then:

`Jv=(3,3)`.

Input norm:

`||v||_2=sqrt(2)`.

Output norm:

`||Jv||_2=3sqrt(2)`.

Gain:

`||Jv||_2/||v||_2=3`.

This direction attains the Euclidean operator norm.

## 13. Exact nonlinear remainder

For scalar `epsilon`:

`x_0+epsilon v=(1+epsilon,1+epsilon)`.

First output coordinate:

`(1+epsilon)^2+(1+epsilon)
=
2+3epsilon+epsilon^2`.

Second:

`(1+epsilon)+2(1+epsilon)
=
3+3epsilon`.

Therefore:

`F(x_0+epsilon v)-F(x_0)
=
epsilon(3,3)+(epsilon^2,0)`.

The JVP is exactly the first-order coefficient.

The residual is exactly quadratic in this direction.

## 14. Exact VJP witness

Take:

`w=(1,2)`.

Since `J^T=J`:

`J^T w
=
[[2,1],
 [1,2]]
(1,2)^T
=
(4,5)^T`.

Define:

`ell(x)=w^T F(x)`.

Then:

`grad ell(x_0)=(4,5)`.

## 15. Product consistency identity

For any `v,w`:

`w^T(Jv)
=
(J^T w)^T v`.

For the witness choices:

`v=(1,1)`,
`w=(1,2)`.

Left side:

`w^T Jv
=
(1,2) dot (3,3)
=
9`.

Right side:

`(J^T w)^T v
=
(4,5) dot (1,1)
=
9`.

This identity is a useful implementation consistency check for paired JVP/VJP routines.

## 16. Exact power iteration from a mixed start

Take:

`z_0=(1,0)`.

In the eigenbasis:

`z_0=(q_1+q_2)/sqrt(2)`.

Unnormalized iterates satisfy:

`A^k z_0
=
((9^k+1)/2,
 (9^k-1)/2)`.

For `k=1`:

`u_1=(5,4)`.

For `k=2`:

`u_2=(41,40)`.

## 17. Exact Rayleigh sequence

For `u_k=A^k z_0`, the Rayleigh quotient is:

`rho_k
=
(9*81^k+1)/(81^k+1)`.

At `k=1`:

`rho_1=730/82=365/41`.

At `k=2`:

`rho_2=59050/6562=29525/3281`.

As `k->infinity`:

`rho_k -> 9`.

Therefore:

`sqrt(rho_k) -> 3`.

## 18. Exact missed-direction witness

Take instead:

`z_0=(1,-1)`.

This is the weak eigenvector direction.

Then:

`A z_0=z_0`.

Every iterate remains proportional to `z_0`.

The Rayleigh quotient is always:

`1`.

The inferred singular value is always:

`1`.

But the true operator norm is:

`3`.

Thus a single power iteration can miss the dominant sensitivity exactly.

## 19. Probe metadata

A reproducible power/sensitivity probe should record at least:

- component identity/version;
- operating point or sampled region;
- input/output norm conventions;
- tangent/cotangent initialization;
- random seed when applicable;
- iteration count;
- normalization rule;
- restart count;
- stopping criterion;
- Rayleigh/residual trace;
- precision/runtime environment.

Without these, the reported estimate is hard to reproduce or interpret.

## 20. Boundary-probe contract

Use:

`B=(F,X,Y,O,U,N_X,N_Y,P,E,tau)`.

Here:

- `F`: component map;
- `X,Y`: typed input/output spaces;
- `O`: operating point or region;
- `U`: perturbation/tangent class;
- `N_X,N_Y`: norm/inner-product conventions;
- `P`: probe procedure;
- `E`: evidence/estimator metadata;
- `tau`: acceptance policy or threshold.

An example numerical obligation is:

`estimated local gain <= tau`

under the declared probe.

The estimator semantics must remain attached to the result.

## 21. Numerical versus semantic interface conditions

A numerical probe can answer questions such as:

- is a chosen tangent amplified strongly?
- is an output covector sensitive to an input direction?
- what local singular gain is observed/estimated?

It cannot by itself answer:

- are physical units compatible?
- does the output mean what the consumer assumes?
- is provenance acceptable?
- are invariants or legal constraints preserved?
- is the interface globally safe?

These are separate contract dimensions.

## 22. Downstream interface

BCONTRACT-001 may consume:

- JVP/VJP definitions;
- chain-rule composition;
- local singular-gain semantics;
- power-iteration estimator limitations;
- probe metadata;
- numerical/semantic boundary separation.

It must independently define the complete boundary contract and any separator variables or governance obligations.
