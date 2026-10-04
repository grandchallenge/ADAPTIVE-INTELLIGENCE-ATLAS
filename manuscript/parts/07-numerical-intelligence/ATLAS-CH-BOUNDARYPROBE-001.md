# Boundary Probes
<!-- ATLAS-CH-BOUNDARYPROBE-001 -->

**Epistemic status:** established linear algebra + established algorithmic differentiation + audited numerical-network sensitivity substrate + Atlas synthesis + exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-BOUNDARYPROBE-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-BOUNDARYPROBE-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-BOUNDARYPROBE-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-BOUNDARYPROBE-001.yaml

A learned component can be shape-compatible with its neighbor and still compose poorly.

One component may amplify a direction the next component cannot tolerate. A downstream objective may be sensitive to one interface coordinate. A finite probe may look benign because it did not explore the dominant singular direction. A local derivative can look small while the nonlinear map changes behavior farther away.

The governing rule is:

> a boundary probe is evidence about a declared local interface question, not a global certificate of the component or system.

## 1. Boundary object

Let a component be

`F:X->Y`.

A later component may consume it:

`G:Y->Z`.

At the interface, several obligations can coexist:

- type and shape compatibility;
- numerical sensitivity;
- semantic compatibility;
- units and conventions;
- provenance;
- downstream task adequacy.

This chapter develops the numerical/local-sensitivity part only.

## 2. Local linearization

Let

`F:R^n->R^m`

be differentiable at operating point `x`.

Write:

`J=J_F(x)`.

Then:

`F(x+delta)
=
F(x)+J delta+r(delta)`

with

`||r(delta)||/||delta|| -> 0`

as `delta -> 0`.

LINALG-001 already established the key boundary: a Jacobian is local.

## 3. Why derivative products matter

The full Jacobian can be too large to materialize.

Many interface questions require only products:

- response to one input perturbation;
- pullback of one output objective;
- dominant local Euclidean gain;
- sensitivity of a selected interface mode.

This motivates JVPs and VJPs.

## 4. JVP

For tangent direction

`v in R^n`,

define:

`JVP_F(x;v)=J_F(x)v`.

Equivalently:

`J_F(x)v
=
d/d epsilon F(x+epsilon v)|_(epsilon=0)`.

A JVP pushes a local input perturbation forward.

Forward-mode algorithmic differentiation computes this product through the computational graph without requiring a dense Jacobian [@GriewankWalther2008; @BaydinEtAl2018].

## 5. JVP versus finite differences

The finite difference

`[F(x+epsilon v)-F(x)]/epsilon`

can approximate the JVP.

It is not the same computational object.

Finite differences depend on a chosen step and carry truncation and roundoff effects. Algorithmic differentiation propagates derivative rules through the represented computation, subject to ordinary numerical arithmetic error.

## 6. VJP

For output covector

`w in R^m`,

use the column-vector convention:

`VJP_F(x;w)
=
J_F(x)^T w`.

If:

`ell(x)=w^T F(x)`,

then:

`grad_x ell(x)=J_F(x)^T w`.

Reverse-mode algorithmic differentiation computes this pullback [@GriewankWalther2008; @BaydinEtAl2018].

## 7. Pairing identity

For compatible `v` and `w`:

`w^T(Jv)
=
(J^T w)^T v`.

This identity gives a compact consistency check between independently implemented JVP and VJP routines.

Agreement is useful evidence.

It is not a proof of complete derivative correctness.

## 8. Chain rule at an interface

For:

`x --F--> y --G--> z`,

the local Jacobian is:

`J_(G o F)(x)
=
J_G(F(x))J_F(x)`.

A JVP propagates forward through this product.

A VJP propagates backward through the transposed factors.

The products follow the chain rule without requiring all intermediate Jacobians to be stored explicitly.

## 9. Local Euclidean gain

LINALG-001 established:

`||J||_2=sigma_max(J)`.

Therefore:

`||J delta||_2
<=
sigma_max(J)||delta||_2`.

The largest singular value is the largest first-order Euclidean amplification factor at the operating point.

## 10. Local does not mean global

The nonlinear map obeys:

`F(x+delta)-F(x)
=
J delta+r(delta)`.

So a known local operator norm controls the linear term.

A global Lipschitz claim needs additional evidence, such as a derivative bound over a region or another nonlinear argument.

## 11. Power iteration as a probe

Define:

`A=J^T J`.

Its eigenvalues are:

`sigma_i(J)^2`.

Power iteration applies:

`u_(k+1)=A z_k`

and normalizes:

`z_(k+1)=u_(k+1)/||u_(k+1)||_2`.

The Rayleigh quotient:

`rho_k=z_k^T A z_k`

can approach the dominant eigenvalue.

Then:

`sqrt(rho_k)`

approaches the dominant singular value.

## 12. JVP and VJP implement the power operator

One application of `A` is:

`A z
=
J^T(Jz)`.

Thus it can be evaluated as:

1. JVP: `u=Jz`;
2. VJP: `J^T u`.

This supports local spectral probing without explicit Jacobian materialization.

## 13. Estimator and quantity are different objects

`sigma_max(J)` is a mathematical quantity.

Power iteration is an estimator procedure.

A finite run can fail to recover the dominant singular direction.

Therefore the procedure that generated an estimate is part of the evidence.

## 14. Initialization matters

Let eigenpairs of `A` be:

`lambda_1 > lambda_2 >= ...`

with eigenvectors `q_i`.

Write:

`z_0=sum_i c_i q_i`.

Then:

`A^k z_0
=
sum_i c_i lambda_i^k q_i`.

If `c_1` is nonzero, the dominant component can eventually control the normalized iterate.

If `c_1=0` exactly, ordinary power iteration cannot create the missing component.

## 15. Finite Rayleigh estimates can be low

For positive semidefinite `A`:

`rho(z)
=
(z^T A z)/(z^T z)
<=
lambda_max(A)`.

Hence:

`sqrt(rho(z))
<=
sigma_max(J)`.

A finite Rayleigh estimate is not automatically a certified upper bound on the true local operator norm.

## 16. Exact witness map

Use:

`F(x_1,x_2)
=
(x_1^2+x_2,
 x_1+2x_2)`.

At:

`x_0=(1,1)`,

`F(x_0)=(2,3)`.

The Jacobian is:

`J=
[[2,1],
 [1,2]]`.

## 17. Exact singular structure

The eigenvectors of `J` are:

`q_1=(1,1)/sqrt(2)`

and

`q_2=(1,-1)/sqrt(2)`

with eigenvalues:

`3` and `1`.

The singular values are therefore:

`3,1`.

Thus:

`||J||_2=3`.

## 18. Exact JVP and nonlinear remainder

Choose:

`v=(1,1)`.

Then:

`Jv=(3,3)`

and the Euclidean gain is exactly `3`.

For scalar `epsilon`:

`F(x_0+epsilon v)-F(x_0)
=
epsilon(3,3)+(epsilon^2,0)`.

The JVP is the exact first-order term. The quadratic remainder makes the local/global distinction explicit.

## 19. Exact VJP

Choose:

`w=(1,2)`.

Then:

`J^T w=(4,5)`.

For:

`ell(x)=w^T F(x)`,

the gradient at `x_0` is exactly:

`(4,5)`.

The pairing check gives:

`w^T(Jv)=9=(J^T w)^T v`.

## 20. Exact power matrix

For the witness:

`A=J^T J
=
[[5,4],
 [4,5]]`.

Its eigenvalues are:

`9,1`.

The exact dominant singular target is therefore:

`sqrt(9)=3`.
