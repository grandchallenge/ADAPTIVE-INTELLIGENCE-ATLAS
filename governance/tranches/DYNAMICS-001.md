# DYNAMICS-001 — Flows, Stability, and Bifurcation

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- validated main: \`283a992504e685d1e53c210aee91f89d9d448f9f\`;
- issue: \`#37\`;
- hard prerequisite:
  - \`ATLAS-CH-LINALG-001\` — \`draft-v0.1\`.

## Why this tranche

At instantiation, \`ATLAS-CH-DYN-001\` was the highest-leverage unlocked architecture node:

- five direct consumers;
- forty-five remaining architecture nodes downstream.

Direct consumers:

- \`ATLAS-CH-NUMERICS-001\`;
- \`ATLAS-CH-ARCHHIST-001\`;
- \`ATLAS-CH-LATENTTIME-001\`;
- \`ATLAS-CH-OPTBASE-001\`;
- \`ATLAS-CH-RLBASE-001\`.

## A. Object discipline

The chapter distinguishes:

- vector field;
- trajectory;
- exact flow map;
- equilibrium;
- numerical update.

For an autonomous ODE

\[
\dot x=f(x),
\]

the exact flow satisfies

\[
\Phi_{t+s}
=
\Phi_t\circ\Phi_s.
\]

A depth-indexed family of learned transformations is therefore only “flow-like” unless this stronger structure is actually justified.

## B. Linearization and stability

At equilibrium

\[
f(x_\star)=0,
\]

local perturbations satisfy

\[
\dot\delta
=
J_f(x_\star)\delta
+
O(\|\delta\|^2).
\]

The chapter preserves the standard hyperbolic distinctions:

- strictly negative real-part spectrum:
  local exponential stability;
- at least one positive-real-part eigenvalue:
  instability;
- zero-real-part / imaginary-axis spectrum:
  linearization alone may be inconclusive.

## C. Lyapunov witness

For

\[
\dot x=-2x,
\qquad
x(0)=3,
\]

the exact solution is

\[
x(t)=3e^{-2t}.
\]

Using

\[
V(x)=\frac12x^2,
\]

the exact orbital derivative is

\[
\dot V=-2x^2.
\]

This provides a clean local/global toy witness for asymptotic/exponential decay.

## D. Saddle-node bifurcation

Normal form:

\[
\dot x=\mu-x^2.
\]

For \(\mu>0\),

\[
x_\star=\pm\sqrt{\mu}.
\]

The derivative

\[
f'(x)=-2x
\]

gives:

- \(+\sqrt{\mu}\): locally stable;
- \(-\sqrt{\mu}\): unstable.

At \(\mu=0\), the collision is nonhyperbolic.

## E. Pitchfork bifurcation

Normal form:

\[
\dot x=\mu x-x^3.
\]

Equilibria:

\[
x_\star=0,
\]

and for \(\mu>0\),

\[
x_\star=\pm\sqrt{\mu}.
\]

With

\[
f'(x)=\mu-3x^2,
\]

the central branch changes from stable to unstable at \(\mu=0\), while the two nonzero branches are stable for \(\mu>0\).

## F. Hopf handoff

The chapter introduces only the qualitative supercritical normal form

\[
\dot r=\mu r-r^3,
\qquad
\dot\theta=\omega.
\]

It is used to demonstrate fixed-point-to-cycle transition.

No general Hopf theorem is claimed or proved.

## G. Hamiltonian and symplectic structure

For canonical state

\[
z=(q,p),
\]

with

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

Hamiltonian dynamics are

\[
\dot z=J\nabla H(z).
\]

For the harmonic oscillator

\[
H(q,p)=\frac12(q^2+p^2),
\]

the exact flow is

\[
M(t)
=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}.
\]

Wolfram verifies exactly:

\[
M(t)^\top J M(t)=J,
\]

and

\[
H(M(t)z)-H(z)=0.
\]

The chapter explicitly separates symplecticity from exact energy conservation in general numerical methods.

## H. Continuous versus discrete dynamics

The chapter freezes the distinction:

\[
\text{exact flow } \Phi_h
\neq
\text{numerical update } \Psi_h.
\]

Even when

\[
\Psi_h(x)
=
\Phi_h(x)
+
O(h^{p+1}),
\]

the discrete method is its own dynamical system and may have different stability, invariants, and long-time geometry.

Explicit Euler on

\[
\dot x=-\lambda x
\]

is used as the handoff example:

\[
x_{n+1}
=
(1-h\lambda)x_n.
\]

The continuous system is stable for all \(\lambda>0\), while the discrete method is stable only when

\[
|1-h\lambda|<1.
\]

## I. Source boundary

External references:

- Khalil 2002:
  nonlinear stability and Lyapunov methods;
- Kuznetsov 2004:
  local bifurcation theory and normal forms;
- Hairer–Lubich–Wanner 2006:
  Hamiltonian/symplectic structure and geometric numerical integration handoff.

Atlas-specific synthesis:

- depth as possible computational time;
- dynamical framing of optimizer/recurrent computation;
- machine-learning relevance of bifurcation and structure-preserving viewpoints.

No claim is made that generic neural networks are exact autonomous ODEs or Hamiltonian systems.

## J. Figure

\`ATLAS-FIG-DYN-001\`

- generator blob:
  \`7ebe6417e356defc326e60c4bb0c95f4458a406e\`;
- rendered blob:
  \`4b1215889f85c29f36fa7e5f419f755068ba19e5\`;
- rendered bytes:
  \`50,300\`;
- representation class:
  exact analytic curves.

Panels:

1. exact exponential attraction for \(\dot x=-2x\);
2. exact saddle-node branches;
3. exact harmonic-oscillator energy orbit.

## K. Durable objects

The branch contains:

- \`sources/source-locks/ATLAS-CH-DYN-001.yaml\`;
- \`manuscript/specifications/ATLAS-CH-DYN-001.md\`;
- \`mathematics/derivations/ATLAS-CH-DYN-001-DERIVATIONS.md\`;
- \`mathematics/computational-witnesses/ATLAS-CW-DYN-001.md\`;
- \`manuscript/parts/02-mathematical-substrate/ATLAS-CH-DYN-001.md\`;
- Wolfram generator/master/manifest;
- Figure Register entry;
- Chapter Ledger promotion to \`draft-v0.1\`.

## L. Frozen distinctions

\[
\text{vector field}
\neq
\text{trajectory}.
\]

\[
\text{trajectory}
\neq
\text{flow map}.
\]

\[
\text{local linearization}
\neq
\text{global nonlinear behavior}.
\]

\[
\text{Lyapunov stability}
\neq
\text{asymptotic stability}.
\]

\[
\text{symplecticity}
\neq
\text{exact energy conservation}.
\]

\[
\text{continuous flow}
\neq
\text{numerical integrator}.
\]

\[
\text{flow-like neural architecture}
\neq
\text{proved autonomous ODE}.
\]

## M. Next step after merge

Run a bounded post-draft audit checking:

- flow composition law;
- local stability statements;
- Lyapunov scope;
- saddle-node and pitchfork classifications;
- Hopf scope;
- harmonic-oscillator matrix exponential;
- symplectic identity;
- energy conservation;
- continuous/discrete separation;
- figure provenance.

Do not draft \`ATLAS-CH-NUMERICS-001\` until the Dynamics audit merges.
