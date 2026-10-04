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


## 21. A mixed start converges

Start with:

`z_0=(1,0)`.

One multiplication gives:

`u_1=(5,4)`.

The next gives:

`u_2=(41,40)`.

The corresponding Rayleigh quotients are:

`rho_1=365/41`

and

`rho_2=29525/3281`.

Both approach the exact dominant eigenvalue `9` from below.

Their square roots approach the true singular norm `3`.

## 22. The convergence has a closed form

Because:

`z_0=(q_1+q_2)/sqrt(2)`,

the unnormalized kth iterate is:

`A^k z_0
=
((9^k+1)/2,
 (9^k-1)/2)`.

Its Rayleigh quotient is:

`rho_k
=
(9*81^k+1)/(81^k+1)`.

Hence:

`rho_k -> 9`.

This exact sequence makes the estimator dynamics visible without numerical ambiguity.

## 23. A different start misses the dominant direction

Now choose:

`z_bad=(1,-1)`.

Then:

`A z_bad=z_bad`.

Every iterate remains in the weak eigenspace.

The Rayleigh quotient is always:

`1`.

The inferred singular value is always:

`1`.

The true operator norm remains:

`3`.

Nothing about the component changed.

Only the probe initialization changed.

## 24. One run is not a certificate

Suppose a policy accepts an interface if the reported local gain is below `2`.

The weak-eigenspace run reports `1`.

The true local norm is `3`.

So an unqualified single-run estimate can support a false acceptance decision.

The lesson is not that power iteration is unusable.

The lesson is that estimator metadata and limitations belong to the result.

## 25. Restarts and subspace methods

Random starts reduce the risk of exact orthogonality under ordinary continuous sampling assumptions.

Multiple restarts improve directional coverage.

Subspace iteration can track several modes.

These are useful engineering choices.

They do not turn a local finite estimate into a global nonlinear theorem.

## 26. Probe metadata

A reproducible spectral or sensitivity probe should record at least:

- exact component identity;
- operating point or sampled region;
- input/output norm convention;
- tangent or cotangent initialization;
- random seed;
- iteration count;
- restart count;
- normalization rule;
- stopping criterion;
- Rayleigh or residual trace;
- numerical precision;
- runtime/software environment.

A scalar estimate without this context is weak evidence.

## 27. Boundary-probe contract

Use:

`B=(F,X,Y,O,U,N_X,N_Y,P,E,tau)`.

Here:

- `F` is the component map;
- `X,Y` are typed input/output spaces;
- `O` is the operating point or region;
- `U` is the perturbation or tangent class;
- `N_X,N_Y` are norm or inner-product conventions;
- `P` is the probe procedure;
- `E` is estimator evidence and metadata;
- `tau` is an acceptance threshold or policy.

This is the numerical-probe portion of a later full boundary contract.

## 28. The perturbation class matters

A full Euclidean operator norm ranges over every Euclidean direction.

A real interface may allow only structured perturbations.

Examples include:

- tangent directions on a constrained manifold;
- physically admissible perturbations;
- data-supported directions;
- parameter-induced variations;
- a full norm ball.

A sensitivity statement should name which class is being probed.

## 29. Norm choice matters

A gain measured in Euclidean norm need not have the same value in another norm.

Interfaces may care about:

- Euclidean energy;
- maximum coordinate error;
- weighted physical units;
- probability geometry;
- task-specific seminorms.

The geometry belongs to the contract.

## 30. Units precede numerical norms

If different coordinates represent incompatible physical units, a raw Euclidean norm can be meaningless.

Unit conversion or scaling conventions must be established before the numerical gain is interpreted.

This is not something the Jacobian probe can infer.

It is a semantic interface obligation.

## 31. Relation to NETNUM sensitivity

NETNUM-001 established that residual-step Jacobians propagate first-order perturbations locally.

For:

`Psi(x)=x+F(x)`,

the exact local Jacobian is:

`J_Psi=I+J_F`.

Boundary probes turn that local derivative into an inspectable interface diagnostic.

The NETNUM boundary remains active:

> local perturbation propagation is not a complete global stability theorem.

## 32. Composite interfaces

For two local Jacobians `J_1` and `J_2`:

`J_composite=J_2 J_1`.

The submultiplicative norm bound gives:

`||J_2 J_1||_2
<=
||J_2||_2 ||J_1||_2`.

This can expose possible amplification chains.

The bound can be loose.

The product of individual worst-case gains need not equal the actual composite gain.

## 33. Small sensitivity is not semantic adequacy

Consider a component that maps every input to zero.

Its Jacobian norm is zero.

Numerically it is insensitive.

Semantically it may destroy all information needed downstream.

Therefore:

> low sensitivity is not automatically good composition.

Numerical compatibility and semantic adequacy are separate axes.

## 34. Large sensitivity is not automatically failure

A component may intentionally amplify a weak signal.

If the downstream consumer expects that scale, a large singular value can be acceptable.

The singular value is a diagnostic quantity.

Whether it violates a contract depends on:

- perturbation class;
- units;
- downstream tolerance;
- application policy.

The threshold is not produced by the Jacobian itself.

## 35. VJP magnitude is not causal attribution

A large coordinate in:

`J^T w`

means the chosen scalarized output is locally sensitive to that input coordinate under the derivative model.

It does not by itself establish causal influence under interventions.

Sensitivity and causal explanation are different objects.

## 36. Probe ensembles

A richer boundary profile may contain:

- several JVP directions;
- several VJP objectives;
- one or more singular-value estimates;
- directional gains;
- local invariant directions;
- estimator residuals.

This can be more informative than a single scalar.

Each statistic still needs an explicit interpretation.

## 37. Probe freshness

Learned components change.

Fine-tuning, quantization, pruning, compilation, or kernel changes can alter boundary behavior.

A probe result should therefore bind to the exact component artifact and execution configuration.

API compatibility does not make an old probe current evidence for a changed component.

## 38. Operating-region coverage

A derivative can be exactly computed at every sampled point while the sampled region fails to represent later inputs.

This separates two questions:

- derivative/probe estimation;
- operating-region coverage.

Power iteration addresses only the first, and only locally.

## 39. Acceptance thresholds are policy

Suppose the measured gain is `1.8` and the threshold is `2`.

The mathematics can establish the measurement and its procedure.

It cannot determine whether `2` is acceptable for the application.

Threshold selection depends on downstream tolerance, uncertainty margins, model role, and governance.

## 40. Numerical versus semantic conditions

A numerical boundary probe can answer questions such as:

- which tangent directions amplify?
- which input directions affect a chosen output objective?
- what local singular gain is observed?
- how stable is the spectral estimate across restarts?

It cannot by itself answer:

- do physical units agree?
- does the output mean what the consumer assumes?
- is provenance acceptable?
- are business, legal, or scientific invariants preserved?
- is the full nonlinear composition globally safe?

Those are separate contract dimensions.

## 41. Failure modes

### Local-to-global promotion

A Jacobian norm at one point is presented as global stability.

### Estimate-to-certificate promotion

A finite power estimate is presented as a proved upper bound.

### Initialization erasure

A spectral estimate is reported without its start or restart procedure.

### Norm erasure

A gain is reported without the geometry in which it was measured.

### Semantic laundering

Low numerical sensitivity is treated as proof of interface meaning.

### VJP-as-causality

A derivative pullback is presented as causal explanation.

### Stale evidence

A probe from an earlier component version is reused after the component changes.

## 42. Practical probe ledger

| Field | Question |
|---|---|
| component | Which exact artifact/version? |
| boundary | Which input and output spaces? |
| operating region | At which point(s) or data region? |
| perturbations | Which directions are admissible? |
| norms | Which input/output geometry? |
| JVP | Which tangent directions were pushed forward? |
| VJP | Which output covectors were pulled back? |
| spectral probe | Which power/subspace procedure? |
| initialization | Which seeds/vectors/restarts? |
| iterations | How many and with what stop rule? |
| estimate | Which Rayleigh/singular values were observed? |
| limitation | What estimator or coverage uncertainty remains? |
| threshold | Which policy determines acceptance? |
| semantic contract | Which non-numerical obligations remain separate? |

This ledger converts **stable interface** into an inspectable claim.

## 43. What the witness establishes

The companion witness proves:

- exact Jacobian `[[2,1],[1,2]]`;
- exact singular values `3,1`;
- JVP `(3,3)` for `v=(1,1)`;
- VJP `(4,5)` for `w=(1,2)`;
- exact JVP/VJP pairing value `9`;
- nonlinear remainder `(epsilon^2,0)` along the chosen tangent;
- mixed-start Rayleigh values `365/41` and `29525/3281` approaching `9`;
- weak-eigenspace initialization returning Rayleigh value `1` forever despite true singular norm `3`.

No global nonlinear theorem is inferred from these finite facts.

## 44. Downstream handoff

**Boundary Contracts — ATLAS-CH-BCONTRACT-001** may now assume:

- JVP semantics;
- VJP semantics;
- local Jacobian composition;
- Euclidean singular-gain interpretation;
- power-iteration estimator behavior and initialization failure;
- probe metadata requirements;
- numerical-versus-semantic separation.

The downstream chapter must independently define:

- semantic interface conditions;
- low-order separator variables;
- admissibility obligations;
- cross-component contract composition;
- governance and evidence rules.

A boundary probe measures.

A boundary contract says what must hold.

## References used in this chapter

- Griewank and Walther, *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation* [@GriewankWalther2008].
- Baydin et al., *Automatic Differentiation in Machine Learning: a Survey* [@BaydinEtAl2018].
- Trefethen and Bau, *Numerical Linear Algebra* [@TrefethenBau1997].
- Golub and Van Loan, *Matrix Computations* [@GolubVanLoan2013].

Exact source identities and authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-BOUNDARYPROBE-001.yaml
