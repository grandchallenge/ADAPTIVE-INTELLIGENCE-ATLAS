# Chapter Specification — ATLAS-CH-BOUNDARYPROBE-001

## Identity

- Stable ID: `ATLAS-CH-BOUNDARYPROBE-001`
- Title: **Boundary Probes**
- Part: `ATLAS-PART-NUMINT`
- Status target: `draft-v0.1`
- Hard prerequisites: `ATLAS-CH-LINALG-001`, `ATLAS-CH-NETNUM-001`
- Implementation issue: #116
- Baseline: `c82f61da1ca457b9670273669c04fe3fd5459652`

## Contract

Develop JVPs, VJPs, power iteration, sensitivity, and interface conditions for learned components.

## Local derivative object

For differentiable `F:R^n->R^m` at operating point `x`, let `J=J_F(x)`.

`F(x+delta)=F(x)+J delta+r(delta)`

with `||r(delta)||/||delta|| -> 0` as `delta -> 0`.

This is local first-order structure, not a global nonlinear guarantee.

## JVP and VJP

For tangent `v`:

`JVP_F(x;v)=Jv=d/d epsilon F(x+epsilon v)|_{epsilon=0}`.

Under the declared Euclidean coordinate convention, represent an output covector by `w` and define:

`VJP_F(x;w)=J^T w`.

For `ell(x)=w^T F(x)`, `grad ell(x)=J^T w`.

## Composition

For `G o F`:

`J_{G o F}(x)=J_G(F(x))J_F(x)`.

JVPs propagate forward; VJPs propagate backward through transposed local factors.

## Local Euclidean gain

`||J||_2=sigma_max(J)`.

Therefore

`||J delta||_2 <= sigma_max(J)||delta||_2`.

This is a local linear sensitivity statement.

## Power-iteration probe

Apply power iteration to `A=J^T J`.

For normalized `z_k`:

`u_{k+1}=A z_k`;

`z_{k+1}=u_{k+1}/||u_{k+1}||_2`.

Rayleigh estimate:

`rho_k=z_k^T A z_k`.

Estimated singular value:

`hat sigma_k=sqrt(rho_k)`.

Finite power iteration requires declared initialization, iteration count, normalization, stopping rule, and restart policy. It is not automatically a certified upper bound on `||J||_2`.

## Exact witness

Use

`F(x_1,x_2)=(x_1^2+x_2, x_1+2x_2)`

at

`x_0=(1,1)`.

Then

`J=[[2,1],[1,2]]`

with singular values `3,1`.

For `v=(1,1)`:

`Jv=(3,3)`

and the norm gain is exactly `3`.

Moreover,

`F(x_0+epsilon v)-F(x_0)=epsilon(3,3)+(epsilon^2,0)`,

which exposes the nonlinear remainder.

For `w=(1,2)`:

`J^T w=(4,5)`.

For `A=J^T J=[[5,4],[4,5]]`, the eigenvalues are `9,1`.

Starting from `z_0=(1,0)`, successive unnormalized vectors are:

`u_1=(5,4)`;

`u_2=(41,40)`.

Their Rayleigh quotients are:

`365/41`;

`29525/3281`;

approaching `9`.

Starting instead from `z_0=(1,-1)` leaves the iterate in the weak eigenspace with Rayleigh quotient `1` forever. Thus one finite power-iteration run need not recover the true norm `3`.

## Boundary-probe contract

Use

`B=(F,X,Y,x_0,U,N_X,N_Y,P,E,tau)`

for component map, typed spaces, operating point/region, perturbation class, norms, probe procedure, estimator evidence, and threshold.

A monitoring condition may record

`hat sigma <= tau`.

Because plain finite power iteration can underestimate `||J||_2`, that observation alone does not certify the stronger requirement `||J||_2 <= tau`. A true norm-threshold certificate requires an independently justified upper bound/enclosure or another certified procedure. Numerical sensitivity remains distinct from semantic compatibility.

## Semantic boundary

Local sensitivity does not prove:

- semantic correctness;
- unit compatibility;
- provenance validity;
- downstream assumption satisfaction;
- global nonlinear stability.

Those belong to downstream boundary-contract obligations.

## Downstream handoff

`ATLAS-CH-BCONTRACT-001` may inherit JVP/VJP semantics, local norm sensitivity, power-iteration limits, and probe metadata requirements.

It must independently define complete semantic/numerical contracts and separator variables.
