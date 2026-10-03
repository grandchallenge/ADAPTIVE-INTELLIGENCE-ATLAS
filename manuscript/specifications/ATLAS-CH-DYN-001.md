# Chapter Specification — ATLAS-CH-DYN-001

## Identity

**Title:** Flows, Stability, and Bifurcation  
**Part:** Mathematical Substrate  
**Status:** specification-ready.  
**Epistemic class:** Established Theory + Atlas Derivation + Atlas Interpretation.

## Chapter contract

Develop the minimum dynamical-systems language required to treat learning and neural computation as evolving systems rather than isolated function evaluations.

The chapter must establish:

- continuous flows;
- discrete maps;
- equilibria/fixed points;
- local linearization;
- local versus global stability;
- Lyapunov functions;
- qualitative phase portraits;
- bifurcation under parameter variation;
- Hamiltonian dynamics;
- symplectic structure.

It must not become a generic survey of nonlinear dynamics.

## Dependency contract

Hard prerequisite:

- \`ATLAS-CH-LINALG-001\`.

May assume:

- eigenvalues/eigenvectors;
- Jacobian matrices;
- operator norms;
- basic multivariable differentiation.

Must not assume:

- numerical integration theory;
- operator splitting;
- optimizer-state dynamics;
- Koopman lifting.

Those are downstream.

## Reader outcome

A reader should be able to:

1. distinguish a vector field from a trajectory and a trajectory from a flow;
2. distinguish continuous-time and discrete-time stability criteria;
3. identify equilibria/fixed points;
4. linearize a nonlinear system near an equilibrium;
5. state when linearized eigenvalues give decisive local stability information and when they do not;
6. verify a Lyapunov-function argument;
7. analyze the exact supercritical pitchfork calibration system;
8. explain bifurcation as qualitative change in invariant structure under parameter variation;
9. derive Hamiltonian conservation from skew-symmetry;
10. state the symplectic-flow condition;
11. understand why stability, phase-space geometry, and computational time become reusable Atlas concepts.

## Formal spine

### Continuous autonomous systems

\[
\dot x=f(x).
\]

A flow \(\Phi_t\) satisfies

\[
\Phi_0=\operatorname{id},
\qquad
\Phi_{t+s}=\Phi_t\circ\Phi_s
\]

when a well-defined autonomous flow exists.

### Equilibria

\[
f(x_\star)=0.
\]

### Linearization

For perturbation \(\delta\),

\[
\dot\delta
=
J_f(x_\star)\delta
+
O(\|\delta\|^2).
\]

Use the standard hyperbolic local classification:

- all eigenvalues with negative real part:
  locally asymptotically stable;
- at least one eigenvalue with positive real part:
  unstable;
- eigenvalues on the imaginary axis:
  first-order test can be inconclusive.

### Discrete maps

\[
x_{k+1}=F(x_k).
\]

At a fixed point \(x_\star\),

\[
F(x_\star)=x_\star.
\]

Local linearization uses

\[
\delta_{k+1}
=
J_F(x_\star)\delta_k.
\]

For a hyperbolic fixed point:

- spectral radius \(<1\):
  locally asymptotically stable;
- an eigenvalue with modulus \(>1\):
  unstable;
- unit-circle eigenvalues:
  linear test can be inconclusive.

### Lyapunov function

State a bounded theorem form:

if \(V(x)\) is positive definite near \(x_\star\) and

\[
\dot V(x)
=
\nabla V(x)^\top f(x)
\]

is negative definite, then the equilibrium is locally asymptotically stable under the usual smoothness/domain assumptions.

Use the exact scalar witness

\[
\dot x=-x^3,
\qquad
V(x)=\frac12x^2,
\qquad
\dot V=-x^4.
\]

### Bifurcation calibration

Use

\[
\dot x
=
\mu x-x^3.
\]

Equilibria:

\[
x_\star=0
\]

for all \(\mu\), and

\[
x_\star=\pm\sqrt\mu
\]

for \(\mu\ge0\).

Linearized scalar eigenvalue:

\[
\lambda
=
\mu-3x_\star^2.
\]

Thus:

- origin stable for \(\mu<0\);
- origin unstable for \(\mu>0\);
- outer branches stable for \(\mu>0\);
- \(\mu=0\) is nonhyperbolic.

### Hamiltonian system

For canonical coordinates \(z=(q,p)\),

\[
\dot z
=
J\nabla H(z),
\]

with

\[
J=
\begin{pmatrix}
0&I\\
-I&0
\end{pmatrix}.
\]

Derive

\[
\frac{dH}{dt}
=
\nabla H^\top J\nabla H
=
0.
\]

State the symplectic-flow identity

\[
D\Phi_t(z)^\top
J
D\Phi_t(z)
=
J.
\]

### Harmonic oscillator witness

Use

\[
H(q,p)
=
\frac12(q^2+p^2),
\]

so

\[
\dot q=p,
\qquad
\dot p=-q.
\]

Exact flow:

\[
\Phi_t
=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}.
\]

Verify:

\[
\Phi_t^\top J\Phi_t=J,
\qquad
H(\Phi_t z)=H(z).
\]

## Principal pedagogical device

### Allegory: wind field and carried particle

- vector field \(f(x)\):
  local wind assigned to each state;
- trajectory:
  one particle's path through that wind;
- flow:
  the transformation carrying every admissible initial state through time;
- equilibrium:
  a point with zero local wind;
- bifurcation:
  a qualitative reorganization of the flow as a control parameter changes.

Limit:

A dynamical system is not literally a physical fluid. Neural depth, optimizer steps, and training time may be discrete, state-dependent, stochastic, or nonautonomous. The analogy is only for separating local law, realized path, and global evolution map.

## Computational witness

One exact Wolfram packet should verify:

- pitchfork equilibria;
- pitchfork stability derivatives;
- scalar Lyapunov derivative;
- harmonic-oscillator matrix exponential;
- energy conservation;
- symplectic identity;
- determinant one of the exact oscillator flow.

## Figure programme

### ATLAS-FIG-DYN-001

Two panels:

1. supercritical pitchfork equilibrium branches versus \(\mu\), with stable and unstable branches visually distinguished;
2. harmonic-oscillator phase portrait with circular energy levels and one exact rotational trajectory.

Representation class:
computed from exact declared equations, with styling explicitly nonliteral.

## Counterexamples and failure boundaries

Include:

- \(\dot x=-x^3\):
  linearization at zero has eigenvalue \(0\) yet the equilibrium is asymptotically stable;
- \(\dot x=x^3\):
  same zero linearization but unstable;
- a stable continuous flow does not imply an arbitrary discrete numerical method is stable;
- conservation/symplectic structure is not generic;
- local stability does not imply global stability;
- transient amplification is not captured solely by asymptotic eigenvalue stability in non-normal systems.

The final point should hand off to the existing Non-normality keystone without duplicating it.

## Downstream obligations

Direct consumers:

- \`ATLAS-CH-NUMERICS-001\`;
- \`ATLAS-CH-ARCHHIST-001\`;
- \`ATLAS-CH-LATENTTIME-001\`;
- \`ATLAS-CH-OPTBASE-001\`;
- \`ATLAS-CH-RLBASE-001\`.

Important later consumers include:

- adaptive depth;
- split-operator computation;
- variational optimization;
- network numerics;
- transport interpretations.

## Sources

- [@Strogatz2015]
- [@Khalil2002]
- [@HairerLubichWanner2006]

Source lock:
\`sources/source-locks/ATLAS-CH-DYN-001.yaml\`.

## Acceptance

The draft must:

- preserve continuous/discrete distinction;
- make local linearization assumptions explicit;
- include the zero-linearization counterexample pair;
- verify one Lyapunov argument exactly;
- derive the pitchfork stability switch;
- derive Hamiltonian conservation;
- state and verify the exact harmonic-oscillator symplectic flow;
- defer numerical-method stability to \`ATLAS-CH-NUMERICS-001\`;
- include one useful allegory with an explicit limit;
- include source lock, witness, and figure provenance.
