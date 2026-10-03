# Chapter Specification — ATLAS-CH-DYN-001

## Identity

**Title:** Flows, Stability, and Bifurcation  
**Part:** Mathematical Substrate  
**Status:** specification-ready.  
**Epistemic class:** established dynamical-systems theory + Atlas synthesis.

## Chapter contract

Develop exactly the dynamical-systems substrate consumed by later Atlas chapters on:

- numerical integration;
- architecture-as-flow;
- latent computational time;
- optimization dynamics;
- reinforcement-learning dynamics;
- split/operator methods.

This is not a general dynamical-systems textbook chapter.

## Dependency contract

Hard prerequisite:

- \`ATLAS-CH-LINALG-001\`.

May assume:

- eigenvalues/eigenvectors;
- norms and linearization language.

Must not assume:

- numerical integration methods;
- optimizer-specific dynamics;
- stochastic differential equations;
- control-theoretic machinery beyond basic Lyapunov reasoning.

## Reader outcome

A reader should be able to:

1. distinguish a vector field, trajectory, flow map, and discrete update;
2. define equilibria and local linearization;
3. distinguish Lyapunov, asymptotic, and exponential stability;
4. use a Lyapunov function in a declared neighborhood;
5. interpret phase portraits;
6. derive saddle-node and pitchfork normal-form branches and stability;
7. understand the qualitative role of a Hopf bifurcation;
8. write a Hamiltonian system as \(\dot z=J\nabla H(z)\);
9. verify symplecticity of an exact linear Hamiltonian flow;
10. explain why a numerical method is not the continuous flow it approximates.

## Formal spine

### Autonomous ODE

\[
\dot x=f(x),
\qquad
x(0)=x_0.
\]

Where existence and uniqueness hold, define the flow

\[
\Phi_t(x_0)=x(t;x_0).
\]

For an autonomous true flow:

\[
\Phi_{t+s}
=
\Phi_t\circ\Phi_s.
\]

### Equilibrium

\[
f(x_\star)=0.
\]

### Linearization

For perturbation \(\delta=x-x_\star\),

\[
\dot\delta
=
J_f(x_\star)\delta
+
O(\|\delta\|^2).
\]

State the standard hyperbolic local result carefully:

- all eigenvalues with strictly negative real parts imply local asymptotic/exponential stability;
- at least one eigenvalue with positive real part implies instability;
- eigenvalues on the imaginary axis / zero real part make linearization alone inconclusive.

### Lyapunov function

For equilibrium at the origin, use a continuously differentiable candidate \(V\) with

\[
V(0)=0,
\qquad
V(x)>0
\]

near the origin, and

\[
\dot V(x)
=
\nabla V(x)^\top f(x).
\]

Distinguish:

- \(\dot V\le0\): stability under appropriate local conditions;
- \(\dot V<0\) for \(x\neq0\): asymptotic stability under standard hypotheses.

Do not overstate global conclusions.

## Exact witness A — stable scalar flow

Use

\[
\dot x=-2x,
\qquad
x(0)=3.
\]

Then

\[
x(t)=3e^{-2t}.
\]

For

\[
V(x)=\frac12x^2,
\]

\[
\dot V=-2x^2.
\]

## Exact witness B — saddle-node

Use

\[
\dot x=\mu-x^2.
\]

Equilibria satisfy

\[
x_\star=\pm\sqrt{\mu}
\]

for \(\mu>0\), one nonhyperbolic equilibrium at \((\mu,x)=(0,0)\), and no real equilibria for \(\mu<0\).

Since

\[
f'(x)=-2x,
\]

the positive branch is locally stable and the negative branch unstable.

## Exact witness C — pitchfork

Use

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

Use

\[
f'(x)=\mu-3x^2
\]

to classify the branches.

## Hopf handoff

Introduce the supercritical normal form in polar coordinates:

\[
\dot r=\mu r-r^3,
\qquad
\dot\theta=\omega.
\]

Use it only to show how a stable fixed point can give way to a stable periodic orbit as a parameter crosses a critical value.

Do not attempt a full Hopf theorem proof.

## Hamiltonian structure

For canonical coordinates

\[
z=(q,p),
\]

and Hamiltonian \(H(q,p)\), define

\[
\dot z
=
J\nabla H(z),
\qquad
J=
\begin{pmatrix}
0&I\\
-I&0
\end{pmatrix}.
\]

For the unit harmonic oscillator,

\[
H(q,p)
=
\frac12(q^2+p^2),
\]

\[
\dot q=p,
\qquad
\dot p=-q.
\]

The exact flow is

\[
M(t)
=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}.
\]

Verify:

\[
M(t)^\top J M(t)=J,
\]

and

\[
H(M(t)z)=H(z).
\]

## Principal pedagogical device

### Allegory: law of motion versus film frames

A flow is the law that moves the state.

A sequence of sampled states is a film of that motion.

A numerical integrator produces approximate frames according to its own update rule.

Correspondence:

- vector field ↔ local law of motion;
- trajectory ↔ one realized path;
- flow map ↔ exact time-\(t\) transport;
- numerical step ↔ approximation to transport.

Limit:

Many neural layers are not samples of one autonomous continuous system. “Flow-like” is weaker than “is an exact ODE flow.”

## Figure programme

### ATLAS-FIG-DYN-001

Three exact/derived panels:

1. stable scalar trajectories for \(\dot x=-2x\);
2. saddle-node equilibrium branches with stable/unstable styling;
3. harmonic-oscillator phase orbit with exact circular energy level.

Representation class: data-derived/exact analytic curves.

## Computational witness

Wolfram exact/symbolic checks of:

- scalar solution and Lyapunov derivative;
- saddle-node equilibria/stability derivative;
- pitchfork branches/stability derivative;
- harmonic-oscillator matrix exponential;
- symplectic identity;
- energy conservation.

## Failure boundaries

Include:

- stable linearization cannot be inferred from a zero eigenvalue;
- local stability does not imply global stability;
- conserved energy does not imply asymptotic convergence;
- phase portraits are coordinate/model-dependent representations;
- a numerical integrator may destroy or invent qualitative structure;
- layer depth is not automatically physical time.

## Downstream obligations

Immediate consumers:

- \`ATLAS-CH-NUMERICS-001\`;
- \`ATLAS-CH-ARCHHIST-001\`;
- \`ATLAS-CH-LATENTTIME-001\`;
- \`ATLAS-CH-OPTBASE-001\`;
- \`ATLAS-CH-RLBASE-001\`.

## Sources

- [@Khalil2002]
- [@Kuznetsov2004]
- [@HairerLubichWanner2006]

Source lock: \`sources/source-locks/ATLAS-CH-DYN-001.yaml\`.

## Acceptance

The draft must:

- preserve flow/trajectory/vector-field distinctions;
- state linearization limits correctly;
- separate Lyapunov, asymptotic, and exponential stability;
- include exact saddle-node and pitchfork branch classifications;
- include Hamiltonian/symplectic exact witness;
- keep continuous flow distinct from numerical discretization;
- include source lock, derivation packet, computational witness, and reproducible figure.
