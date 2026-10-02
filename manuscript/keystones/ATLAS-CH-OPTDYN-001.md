# Keystone Specification — ATLAS-CH-OPTDYN-001

## Identity

**Title:** Optimizer-State Dynamics  
**Part:** Optimization as Geometry and Dynamics  
**Status:** specification-ready  
**Keystone role:** make the optimizer's internal state part of the mathematical state being analyzed.

## Chapter contract

The chapter must replace the simplified picture

\[
\theta_{t+1}=\theta_t-\eta \nabla L(\theta_t)
\]

with the more general state-space picture

\[
z_{t+1}=F_t(z_t,\xi_t),
\qquad
z_t=(\theta_t,s_t),
\]

where \(s_t\) contains optimizer state and \(\xi_t\) represents stochastic or data-dependent input.

Its governing question is:

> what dynamical behavior appears only when model parameters and optimizer state are analyzed together?

## Dependency contract

Immediate hard prerequisites:

- ATLAS-CH-NONNORMAL-001 — formal;
- ATLAS-CH-OPTBASE-001 — formal/conceptual.

Inherited prerequisites include linear algebra, the Atlas object taxonomy, and basic dynamics through the first-order optimization chapter.

The chapter may assume SGD, momentum, Adam-like state, Jacobians, singular values, and non-normal transient amplification. It may not assume Coupling-Phase Spectroscopy.

## Reader outcome

The reader should be able to:

1. write common optimizers as augmented-state recurrences;
2. linearize the augmented map around a fixed point or trajectory;
3. distinguish parameter-space curvature from optimizer-state dynamics;
4. compute or interpret a local state Jacobian;
5. understand how non-normality can create transient amplification without asymptotic linear instability;
6. separate a diagnostic mechanism from a universal explanation of training failure;
7. understand why a learning-rate boundary may be a property of the coupled system rather than the loss landscape alone.

## Formal spine

### Augmented state

For momentum, begin with a simple deterministic form such as

\[
v_{t+1}=\beta v_t + g(\theta_t),
\qquad
\theta_{t+1}=\theta_t-\eta v_{t+1}.
\]

Write the joint update as \(z_{t+1}=F(z_t)\) and derive its block Jacobian.

For adaptive optimizers, introduce first- and second-moment state only after the two-state example is completely transparent.

### Core objects

- augmented optimizer state;
- update map \(F\);
- local Jacobian \(J_F\);
- instantaneous singular amplification;
- spectral radius;
- non-normality;
- finite-horizon propagator:
  \[
  J_{t+k-1}\cdots J_t.
  \]

### Core derivations

At minimum:

1. exact Jacobian for a one-dimensional quadratic with momentum;
2. stability region or characteristic equation for the linearized recurrence;
3. a two-dimensional or augmented-state example where eigenvalue analysis and finite-horizon amplification diverge;
4. time-varying product-of-Jacobians interpretation for nonstationary training.

The text must distinguish autonomous fixed-point analysis from a trajectory-dependent nonautonomous system.

## Principal intuition device

### Allegory: steering with a flywheel

The model parameter is the vehicle's position; optimizer state is a flywheel carrying momentum from previous motion.

Structural correspondence:

- parameter ↔ position;
- momentum/moment state ↔ stored dynamical state;
- learning rate ↔ control gain;
- transient overshoot ↔ coupled-state amplification.

Limit of allegory:

Adaptive optimizers have richer, coordinatewise state and stochastic forcing; no literal mechanical conservation law is implied.

## Figure programme

### ATLAS-FIG-OPTDYN-001 — Coupled optimizer-state phase portrait

Use a deliberately low-dimensional system for which the complete update and Jacobian are stated.

Required panels:

- state-space vector field or discrete trajectory family;
- eigenvalue location;
- singular amplification or finite-horizon gain;
- stable versus unstable or low-gain versus transient-growth parameter regimes.

Representation class: simulation-derived.

The caption must say that the toy system establishes mechanism visibility, not frontier-model prevalence.

## Wolfram computational witnesses

1. symbolic Jacobian of momentum on a quadratic;
2. exact characteristic polynomial;
3. parameter sweep over \((\eta,\beta)\);
4. finite-horizon singular-value growth;
5. comparison of eigenvalue-based and singular-value-based diagnostics;
6. optional time-varying Jacobian product for a nonquadratic toy loss.

## Counterexamples and failure boundaries

The chapter must block:

- "large Hessian eigenvalue implies optimizer instability" as a universal statement;
- "spectral radius below one means no dangerous transient";
- "a transient spike proves divergence";
- "local linearization predicts the full nonlinear trajectory globally";
- "optimizer state is merely an implementation detail."

## Bridge to CPS

The final section should motivate Coupling-Phase Spectroscopy as an instrumentation problem: if phase changes are properties of the augmented state, probes should observe the augmented-state Jacobian or an informative approximation.

The chapter itself should not claim CPS is validated generally.

## Downstream obligations

Provides formal language for:

- ATLAS-CH-CPS-001;
- ATLAS-CH-ROUTERDYN-001;
- ATLAS-CH-SPECTRALDIAG-001.

## Source-lock plan

Before review-ready drafting, source-lock:

- canonical optimizer formulations;
- reliable discrete-dynamical-systems references;
- matrix-analysis/non-normal references already used upstream;
- primary research sources for any optimizer-specific stability result.

GCL experimental observations may be introduced only with exact provenance and the appropriate empirical status.

## Acceptance criteria

The drafted chapter must contain:

- at least one full augmented-state derivation;
- a block Jacobian;
- a stability calculation;
- a transient-growth witness;
- explicit fixed-point versus trajectory-dependent distinctions;
- a toy-system claim boundary;
- a clean handoff to CPS.
