# AUDIT-023 — Networks as Numerical Schemes

## Disposition

**PASS AFTER ONE STABILITY-CONVENTION REPAIR**

ATLAS-CH-NETNUM-001 remains at `draft-v0.1`.

The chapter correctly uses numerical-analysis language only after binding a residual update to a declared continuous reference, step semantics, error metric, and refinement family.

The audit found one in-scope precision defect:

- the scalar witness sometimes summarized `0<=h<=2` as a generic "stability interval" without repeating the prerequisite distinction between non-growth and strict asymptotic decay.

The repaired chapter now states:

- non-growth:
  `|1-h|<=1`, hence `0<=h<=2`;
- strict decay:
  `|1-h|<1`, hence `0<h<2`;
- boundary case:
  `h=2` gives amplification `-1`, so magnitude is preserved rather than decayed.

No exact witness arithmetic, source identity, residual/ODE boundary, refinement claim, reversibility claim, or downstream handoff required reversal.

## Audited baseline

- implementation merge:
  `e7c0cda1a96f23e78120c02f66511488612a4035`;
- implementation PR:
  #103;
- audit issue:
  #104;
- chapter:
  `ATLAS-CH-NETNUM-001`.

## 1. Hard prerequisites

PASS.

The source lock binds exactly:

- NUMERICS manuscript blob:
  `a719a16e86d1feb76679e1f1cda2d9d3393d2e42`;
- AUDIT-009 blob:
  `2bbb1b7687d6c4b8c0bfeed5206de836dac92dca`;
- ARCHHIST manuscript blob:
  `3d373695ed5516dbc3b0557112f204636e911897`;
- AUDIT-010 blob:
  `c9aa1488b5041805e4695f00f462f3773a27dedf`.

No Adaptive Depth or Boundary Probes manuscript is used as hidden prerequisite authority.

## 2. External bridge sources

PASS.

The source lock identifies:

- Eldad Haber and Lars Ruthotto, "Stable Architectures for Deep Neural Networks," Inverse Problems 34(1), 014004, DOI `10.1088/1361-6420/aa9a90`;
- Yiping Lu, Aoxiao Zhong, Quanzheng Li, and Bin Dong, "Beyond Finite Layer Neural Networks: Bridging Deep Architectures and Numerical Differential Equations," PMLR 80, 3276–3285 (2018).

Their roles remain bounded to numerical/dynamical interpretations and architecture-design bridges.

The chapter does not use either source to claim that every residual network is literally one ODE solver.

## 3. Residual-to-Euler bridge

PASS.

The chapter distinguishes the residual update

`x_{k+1}=x_k+F_k(x_k)`

from Euler applied to

`dx/dt=f(t,x)`:

`x_{k+1}=x_k+h_k f(t_k,x_k)`.

The identification

`F_k(x)=h_k f(t_k,x)`

is explicitly labeled a modeling declaration rather than a consequence of residual syntax.

## 4. Autonomous/nonautonomous scope

PASS.

Shared residual fields support the direct autonomous interpretation.

Layer-varying fields may support a nonautonomous interpretation when tied to declared times and a common continuous model.

The chapter correctly rejects both false converses:

- untied weights do not automatically rule out a continuous-time interpretation;
- tied weights do not automatically prove a faithful ODE discretization.

## 5. Local defect

PASS.

The chapter defines local defect only relative to an exact flow:

`delta_{k+1}=Phi_{h_k}(t_k,x(t_k))-Psi_k(x(t_k))`.

For Euler-compatible steps under smoothness assumptions, the `O(h_k^2)` local defect is inherited correctly from NUMERICS-001.

A small residual norm is not promoted into a truncation-error statement.

## 6. Global error and refinement

PASS.

The chapter preserves the distinction between local defect and accumulated global error.

It requires a refinement family that keeps the continuous reference problem fixed before interpreting greater depth as a finer mesh.

Thus:

`more layers != smaller discretization error`

without additional structure.

## 7. Residual scale versus step size

PASS.

A multiplier in

`x_{k+1}=x_k+alpha_k G_k(x_k)`

is treated as a numerical step size only when `G_k` has declared vector-field semantics.

Otherwise it remains a residual scale.

## 8. Scalar stability

PASS AFTER REPAIR.

For

`x'=-x`

and Euler/residual step

`x_{k+1}=(1-h)x_k`,

the amplification factor is

`R(-h)=1-h`.

The standard non-growth condition is now stated consistently as

`|1-h|<=1`

with real nonnegative interval

`0<=h<=2`.

Strict decay is separately stated as

`0<h<2`.

At `h=2`, the factor `-1` is bounded but non-decaying.

At `h=3`, the factor is `-2`, while the exact continuous factor is `e^{-3}`; the discrete mode is unstable although the continuous mode decays.

## 9. Exact finite-horizon witness

PASS.

For `T=1`, `h=1/N`:

`x_N=(1-1/N)^N`.

Independent replay confirms:

- `N=2: 1/4`;
- `N=4: 81/256`;
- `N=8: 5764801/16777216`.

Against `e^{-1}`, the absolute errors decrease over this declared finite sequence.

The witness does not promote this finite table into the general convergence theorem.

First-order convergence remains inherited from the audited numerical-analysis prerequisite under its assumptions.

## 10. Numerical versus training stability

PASS.

The manuscript distinguishes forward numerical perturbation/error propagation from optimization stability, gradient stability, learning-rate behavior, and generalization.

Haber–Ruthotto is used as a bridge showing why discrete-dynamics stability can inform architecture design, not as an identity between all stability notions.

## 11. Jacobian propagation

PASS.

For

`Psi_k(x)=x+F_k(x)`,

the exact local Jacobian identity

`J_{Psi_k}=I+J_{F_k}`

is correct.

Accumulated Jacobian products are treated as first-order forward sensitivity propagation rather than as a complete optimization theorem.

## 12. Invertibility versus reversibility

PASS.

For `x'=-x`:

`Psi_h(x)=(1-h)x`.

When `h!=1`, the map is invertible.

At `h=1/2`:

- forward factor: `1/2`;
- true inverse factor: `2`;
- negative-step Euler factor: `3/2`;
- forward/negative-step round trip: `3/4`.

Therefore map invertibility does not imply the time-symmetry condition

`Psi_{-h}=Psi_h^{-1}`.

Computational activation reconstruction is also kept separate from numerical time reversibility.

## 13. Residual versus Neural ODE boundary

PASS.

Residual networks are finite compositions with a possible continuous interpretation.

Neural ODEs specify continuous dynamics and numerically construct trajectories.

The chapter treats them as related through discretization, not identical.

## 14. Stiffness boundary

PASS.

The manuscript does not use "stiff" as a synonym for large derivatives or difficult training.

It requires a declared dynamical problem, method, scale separation, and resulting step/solver restriction before importing stiffness language.

## 15. Downstream handoffs

PASS.

ATLAS-CH-ADAPTDEPTH-001 may inherit:

- exact-flow versus step-map distinction;
- local versus global error;
- refinement-family semantics;
- step-size boundary;
- stability-function reasoning.

ATLAS-CH-BOUNDARYPROBE-001 may inherit:

- one-step maps;
- local Jacobians;
- perturbation propagation;
- local-versus-global sensitivity distinction.

Neither chapter is consumed as prerequisite authority.

## 16. Integrity

PASS subject to audit merge validation.

The Chapter Ledger records NETNUM-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-NETNUM-LOCK-001`.

The bibliography contains the Haber–Ruthotto and Lu et al. keys used by the manuscript.

The exact witness contains an explicit Claim boundary.

No governed figure is required for this tranche; the scalar witness exposes the distinctions directly.

## 17. Final disposition

AUDIT-023 passes after the scalar stability-convention repair.

The durable chapter boundary is:

**residual syntax -> declared continuous reference -> numerical step family -> local defect -> stability/error propagation -> global approximation, with invertibility and time reversibility kept separate.**
