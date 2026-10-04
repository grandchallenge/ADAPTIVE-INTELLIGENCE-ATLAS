# AUDIT-029 — Boundary Probes

## Disposition

**PASS AFTER TWO FORMAL PRECISION REPAIRS AND ONE SOURCE-METADATA REPAIR**

ATLAS-CH-BOUNDARYPROBE-001 remains at `draft-v0.1`.

The chapter correctly develops JVPs, VJPs, local Jacobian sensitivity, power iteration on `J^T J`, estimator metadata, and numerical boundary-probe conditions while preserving the distinction between local numerical evidence and global or semantic guarantees.

AUDIT-029 found three in-scope defects:

1. the VJP definition used `J^T w` without explicitly binding the Euclidean coordinate/inner-product convention that makes a covector represented by a column vector. The specification, derivation, and manuscript now state that convention;
2. the boundary-probe contract allowed `hat sigma <= tau` to appear as an acceptance condition even though the chapter had already proved that ordinary finite power iteration can underestimate the true norm. The repaired chapter now distinguishes a monitoring observation from the stronger claim `||J||_2 <= tau`; the latter requires a justified upper enclosure or another independently justified method;
3. the bibliography used an abbreviated Griewank–Walther title. It now matches the locked second-edition SIAM source identity, including full title, edition, ISBN, and DOI.

No exact witness arithmetic, prerequisite identity, local/global boundary, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  `a6ef32bbd43347907833b0812cb776162ade01c6`;
- implementation PR:
  #116;
- audit issue:
  #117;
- chapter:
  `ATLAS-CH-BOUNDARYPROBE-001`.

## 1. Hard prerequisites

PASS.

The source lock binds exactly:

### Linear Maps and Decompositions

- manuscript blob:
  `e7fcf56322f26d232d3a3043038d9850792b4bde`;
- Foundation audit blob:
  `948f76b3f86d27fa4830efc30d8ef0135134256e`;
- source-lock blob:
  `f24e93ee0c2496ca0b9d71f6f824b0d13dbdc08e`.

### Networks as Numerical Schemes

- manuscript blob:
  `cbaf0b96c996c821df50f985075f64028459c587`;
- AUDIT-023 blob:
  `746e0c297e4ddf29122d4735108becc33e599030`;
- source-lock blob:
  `02bbe77d19da4a6a123e430f8aae058d666c4e35`.

No Boundary Contracts manuscript is used as hidden prerequisite authority.

## 2. External differentiation sources

PASS AFTER METADATA REPAIR.

The source lock identifies:

- Griewank and Walther, *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation*, second edition, SIAM, 2008;
- Baydin, Pearlmutter, Radul, and Siskind, *Automatic Differentiation in Machine Learning: a Survey*, JMLR 18(153), 1–43, 2018.

They are used for forward/reverse algorithmic-differentiation terminology and derivative-product computation, not as global sensitivity theorems.

## 3. Local linearization

PASS.

For differentiable `F` at `x`:

`F(x+delta)=F(x)+J_F(x)delta+r(delta)`

with

`||r(delta)||/||delta|| -> 0`.

The chapter consistently treats the Jacobian as a local first-order object rather than a global nonlinear model.

## 4. JVP

PASS.

The JVP is defined as:

`J_F(x)v`

and equivalently as the directional derivative:

`d/d epsilon F(x+epsilon v)|_{epsilon=0}`.

The manuscript correctly distinguishes algorithmic differentiation from finite-difference approximation.

## 5. VJP

PASS AFTER REPAIR.

Under the declared Euclidean coordinate convention, an output covector is represented by a column vector `w` and the VJP is:

`J_F(x)^T w`.

For:

`ell(x)=w^T F(x)`,

the chapter correctly gives:

`grad_x ell=J_F(x)^T w`.

The column/transpose convention is now explicit in all load-bearing artifacts.

## 6. Pairing and chain rule

PASS.

The pairing identity:

`w^T(Jv)=(J^T w)^T v`

is correct.

For composition:

`J_{G o F}(x)=J_G(F(x))J_F(x)`.

The chapter correctly interprets JVPs as forward tangent propagation and VJPs as backward pullback through transposed factors.

## 7. Local Euclidean sensitivity

PASS.

Inherited from LINALG-001:

`||J||_2=sigma_max(J)`.

Therefore:

`||J delta||_2 <= sigma_max(J)||delta||_2`.

The chapter does not promote this first-order local statement into a global nonlinear Lipschitz theorem.

## 8. Power iteration semantics

PASS.

The chapter applies power iteration to:

`A=J^T J`.

Its eigenvalues are the squared singular values of `J`.

The Rayleigh quotient is used to estimate the dominant eigenvalue, and its square root estimates the dominant singular value.

The chapter records initialization, iterations, normalization, stopping rule, and restarts as part of the evidence.

## 9. Finite estimate versus norm bound

PASS AFTER REPAIR.

For positive semidefinite `A`:

`rho(z)<=lambda_max(A)`.

Thus a finite Rayleigh estimate can underestimate the true top eigenvalue.

The chapter now states explicitly that:

`hat sigma <= tau`

from ordinary finite power iteration is a monitoring observation, not by itself proof of:

`||J||_2 <= tau`.

This repair is mathematically necessary for downstream contract use.

## 10. Exact nonlinear witness

PASS.

For:

`F(x1,x2)=(x1^2+x2,x1+2x2)`

at:

`x0=(1,1)`,

the exact Jacobian is:

`J=[[2,1],[1,2]]`.

Its singular values are:

`3,1`.

Therefore:

`||J||_2=3`.

## 11. Exact JVP and remainder

PASS.

For:

`v=(1,1)`,

the JVP is:

`Jv=(3,3)`.

The Euclidean gain is exactly 3.

The finite perturbation identity:

`F(x0+epsilon v)-F(x0)
=
epsilon(3,3)+(epsilon^2,0)`

correctly exposes the nonlinear remainder.

## 12. Exact VJP and pairing

PASS.

For:

`w=(1,2)`,

the VJP is:

`J^T w=(4,5)`.

The exact pairing check gives:

`w^T(Jv)=9=(J^T w)^T v`.

Independent rational replay confirms both sides.

## 13. Exact power-iteration witness

PASS.

For:

`A=J^T J=[[5,4],[4,5]]`,

the eigenvalues are:

`9,1`.

Starting from:

`z0=(1,0)`,

the first two unnormalized iterates are:

`(5,4)`;

`(41,40)`.

Their exact Rayleigh quotients are:

`365/41`;

`29525/3281`.

These approach 9, so the corresponding singular-value estimates approach 3.

## 14. Missed-direction witness

PASS.

Starting from:

`z0=(1,-1)`,

the iterate remains in the weak eigenspace:

`A z0=z0`.

The Rayleigh quotient remains 1, giving an inferred singular value 1 although the true norm is 3.

This is an exact finite counterexample to treating one unqualified power run as an upper norm certificate.

## 15. Probe contract

PASS AFTER REPAIR.

The chapter uses:

`B=(F,X,Y,O,U,N_X,N_Y,P,E,tau)`

for component map, typed spaces, operating point/region, perturbation class, norm conventions, probe procedure, estimator evidence, and threshold/policy.

The contract now keeps a measured/estimated threshold observation distinct from a mathematically established bound on the true operator norm.

## 16. Numerical versus semantic interface conditions

PASS.

The chapter explicitly refuses to infer from local numerical sensitivity:

- semantic correctness;
- unit compatibility;
- provenance validity;
- global nonlinear stability;
- downstream assumption satisfaction;
- causal attribution.

Those obligations are deferred to BCONTRACT-001 or other relevant layers.

## 17. Freshness and operating-region scope

PASS.

Probe evidence is bound to component identity/version and execution configuration.

The chapter separately identifies operating-region coverage as a source of uncertainty distinct from derivative-estimation error.

## 18. Integrity

PASS subject to audit-PR validation.

The Chapter Ledger records BOUNDARYPROBE-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-BOUNDARYPROBE-LOCK-001`.

The bibliography closes:

- `GriewankWalther2008`;
- `BaydinEtAl2018`;
- `TrefethenBau1997`;
- `GolubVanLoan2013`.

The exact witness contains an explicit Claim boundary.

No governed figure is required.

## 19. Downstream handoff

PASS.

ATLAS-CH-BCONTRACT-001 may inherit:

- JVP/VJP semantics;
- local Jacobian composition;
- local singular-gain interpretation;
- finite power-estimator limitations;
- probe metadata requirements;
- numerical-versus-semantic separation.

It must independently define complete semantic/numerical boundary contracts, separator variables, admissibility, and governance obligations.

## 20. Final disposition

AUDIT-029 passes after the three repairs above.

The durable boundary-probe layer is:

**exact component/version + declared operating region + perturbation geometry -> JVP/VJP local derivative products -> explicitly qualified spectral estimator -> evidence-bearing numerical interface observation, without promotion to global or semantic certification.**
