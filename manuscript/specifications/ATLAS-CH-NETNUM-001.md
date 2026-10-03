# Chapter Specification — ATLAS-CH-NETNUM-001

## Identity

- Stable ID: `ATLAS-CH-NETNUM-001`
- Title: **Networks as Numerical Schemes**
- Part: `ATLAS-PART-NUMINT`
- Status target: `draft-v0.1`
- Hard prerequisites:
  - `ATLAS-CH-NUMERICS-001`
  - `ATLAS-CH-ARCHHIST-001`
- Implementation issue: #103
- Drafting baseline: `58da49a2f2969de687cbfd247e488997e57b05d6`

## Contract

Recast residual networks as discretizations and distinguish local error, global error, stability, and reversibility.

## Opening obstruction

The residual algebra

`x_{k+1}=x_k+F_k(x_k)`

resembles explicit Euler.

That resemblance is mathematically useful.

It is not yet a numerical-analysis theorem.

To speak of local truncation error, global error, step size, consistency, or reversible integration, the chapter must identify the continuous object being approximated and the family of discrete maps used to approximate it.

## Central discipline

A residual network admits a **numerical-scheme interpretation** only after enough structure is declared to answer:

1. What is the reference continuous evolution?
2. What does one layer correspond to?
3. What quantity plays the role of step size?
4. How does the architecture change under refinement?
5. Which norm or state metric defines error or stability?
6. Are layer parameters samples of one autonomous field, one nonautonomous field, or merely unrelated maps?
7. Which numerical property is actually being claimed?

Residual form by itself answers none of these completely.

## Formal bridge

Start from

`dx/dt=f(t,x)`.

Explicit Euler gives

`x_{k+1}=x_k+h_k f(t_k,x_k)`.

A residual block

`x_{k+1}=x_k+F_k(x_k)`

matches this syntax if one declares

`F_k(x)=h_k f(t_k,x)`.

This declaration is a modeling interface, not a consequence of the identity skip alone.

## Autonomous versus nonautonomous interpretation

If

`F_k(x)=h f(x)`

with a common vector field, the family has the direct form of a fixed-step discretization of an autonomous ODE.

If

`F_k(x)=h_k f(t_k,x)`

with layer-varying fields tied to declared times, a nonautonomous interpretation is possible.

Arbitrary untied `F_k` still define a finite composition, but without an interpolation or refinement rule they do not by themselves define one continuous-time model.

## Local defect

Given exact flow `Phi_{h_k}(t_k,x)` and network step

`Psi_k(x)=x+F_k(x)`,

define

`delta_{k+1}=Phi_{h_k}(t_k,x(t_k))-Psi_k(x(t_k))`.

For Euler-compatible `F_k=h_k f(t_k,.)` under standard smoothness,

`delta_{k+1}=O(h_k^2)`.

If no continuous reference flow is declared, "local truncation error of the layer" is undefined.

## Global error

For a refinement family approximating the same continuous evolution, define

`e_k=x(t_k)-x_k`.

Small local defect does not imply small global error without suitable stability and error-propagation assumptions.

Depth alone is not a convergence parameter.

A convergence claim requires a family in which the effective mesh is refined while the target continuous problem remains fixed.

## Stability

For

`x'=lambda x`,

the residual/Euler step is

`x_{k+1}=(1+h lambda)x_k`.

The amplification factor is

`R(z)=1+z`, with `z=h lambda`.

Absolute non-growth stability is

`|1+h lambda|<=1`.

This is forward numerical stability for the declared linear mode.

It is not automatically optimization stability, gradient stability, data robustness, generalization, or nonlinear global stability.

## Step size versus residual scale

A multiplier `alpha_k` in

`x_{k+1}=x_k+alpha_k G_k(x_k)`

can play a step-size role only when the family `G_k` has declared vector-field semantics.

Without that semantics, `alpha_k` is simply a residual scale.

## Reversibility

Distinguish:

1. map invertibility;
2. computational reversibility;
3. time reversibility or symmetry, `Psi_{-h}=Psi_h^{-1}`.

These are not equivalent.

For `x'=-x`, explicit Euler has

`Psi_h(x)=(1-h)x`.

It is invertible when `h!=1`, but

`Psi_{-h}(Psi_h(x))=(1-h^2)x`,

so it is not time-reversible for nonzero `h`.

## Exact computational witness

Use

`x'=-x`, `x(0)=1`.

Exact solution:

`x(t)=e^{-t}`.

Residual/Euler step:

`x_{k+1}=(1-h)x_k`.

### Stability

`|1-h|<=1`

gives

`0<=h<=2`.

For `h=3`, the continuous system decays but the discrete factor is `-2`.

### Finite-horizon refinement

For `T=1` and `N` equal steps, `h=1/N`:

`x_N=(1-1/N)^N`.

For `N=2,4,8`:

- `1/4`;
- `81/256`;
- `5764801/16777216`.

The exact continuous value is `e^{-1}`.

The witness records the exact symbolic error

`e^{-1}-(1-1/N)^N`

and shows it decreases across the declared finite values.

No infinite convergence theorem is inferred from that finite table.

### Reversibility test

For `h=1/2`:

- forward Euler factor: `1/2`;
- negative-step Euler factor: `3/2`;
- forward then backward: `3/4 != 1`;
- inverse of the forward map: multiplier `2`.

Thus invertibility does not imply time reversibility.

## Architecture interpretation

The chapter may use the already source-locked residual-network and Neural ODE sources from ARCHHIST, plus Haber–Ruthotto and Lu et al. as explicit numerical-analysis bridge sources.

It must not claim that every residual architecture has a unique underlying ODE.

## Required failure boundaries

Reject:

- residual block = Euler theorem;
- depth = time without a declared mesh;
- small residual norm = small local truncation error;
- numerical stability = training stability;
- invertible layer = reversible integrator;
- more layers = smaller global discretization error;
- untied weights = no possible ODE interpretation;
- tied weights = automatically faithful ODE discretization.

## Downstream handoff

`ATLAS-CH-ADAPTDEPTH-001` may inherit the network/numerical-step interface, local versus global error, refinement-family discipline, numerical stability boundary, and step-size versus residual-scale distinction.

`ATLAS-CH-BOUNDARYPROBE-001` may inherit the one-step map `Psi_k`, its Jacobian as a local perturbation propagator, and the distinction between one-step sensitivity and accumulated global behavior.

Neither downstream chapter may serve as prerequisite authority here.

## Completion criteria

- exact prerequisite locks;
- external bridge source lock;
- derivation packet;
- exact scalar witness;
- complete manuscript;
- Chapter Ledger promotion;
- Source Register and bibliography closure;
- tranche receipt;
- repository validation green;
- bounded post-draft audit with all in-scope repairs.
