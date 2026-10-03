# DYNAMICS-001 — Flows, Stability, and Bifurcation

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- starting main: \`283a992504e685d1e53c210aee91f89d9d448f9f\`;
- issue: \`#38\`;
- prerequisite:
  - \`ATLAS-CH-LINALG-001\` at \`draft-v0.1\`.

## Objective

Draft \`ATLAS-CH-DYN-001\` as the smallest dynamical-systems substrate needed by the downstream Atlas.

Direct consumers include:

- \`ATLAS-CH-NUMERICS-001\`;
- \`ATLAS-CH-ARCHHIST-001\`;
- \`ATLAS-CH-LATENTTIME-001\`;
- \`ATLAS-CH-OPTBASE-001\`;
- \`ATLAS-CH-RLBASE-001\`.

The chapter intentionally defers:

- numerical method stability/error analysis;
- operator splitting;
- optimizer-state block dynamics;
- Koopman lifting.

## A. Continuous and discrete dynamics

Continuous system:

\[
\dot x=f(x).
\]

Autonomous flow:

\[
\Phi_{t+s}
=
\Phi_t\circ\Phi_s.
\]

Discrete system:

\[
x_{k+1}=F(x_k).
\]

The chapter freezes the distinction:

\[
\text{vector field}
\neq
\text{trajectory}
\neq
\text{flow}.
\]

It also freezes:

\[
\text{continuous stability criterion}
\neq
\text{discrete stability criterion}.
\]

## B. Local linearization

At equilibrium

\[
f(x_\star)=0,
\]

\[
\dot\delta
=
J_f(x_\star)\delta
+
O(\|\delta\|^2).
\]

Under the standard smoothness/hyperbolicity conditions:

- all eigenvalues with negative real part imply local asymptotic stability;
- any eigenvalue with positive real part implies instability;
- zero-real-part eigenvalues can leave first-order classification inconclusive.

For discrete fixed points, the analogous boundary is the unit circle.

## C. Zero-linearization calibration

Two scalar systems:

\[
\dot x=-x^3,
\]

and

\[
\dot x=x^3
\]

both satisfy

\[
f'(0)=0.
\]

Yet:

- the first origin is asymptotically stable;
- the second origin is unstable.

This exact pair prevents zero linearization from being misread as neutral nonlinear behavior.

## D. Lyapunov witness

For

\[
\dot x=-x^3,
\qquad
V(x)=\frac12x^2,
\]

\[
\dot V
=
-x^4.
\]

The chapter uses this as an exact calibration of a nonlinear stability certificate.

## E. Pitchfork bifurcation

Calibration system:

\[
\dot x
=
\mu x-x^3.
\]

Equilibria:

\[
x_\star=0
\]

for all \(\mu\), plus

\[
x_\star=\pm\sqrt\mu
\]

for \(\mu>0\).

Jacobian:

\[
\lambda
=
\mu-3x_\star^2.
\]

Therefore:

\[
\lambda_0=\mu,
\]

and

\[
\lambda_\pm=-2\mu.
\]

Thus:

- origin stable for \(\mu<0\);
- origin unstable for \(\mu>0\);
- outer branches stable for \(\mu>0\);
- \(\mu=0\) is nonhyperbolic.

At the bifurcation point the system reduces to \(\dot x=-x^3\), so nonlinear analysis recovers asymptotic stability despite zero linearization.

## F. Hamiltonian and symplectic structure

Canonical Hamiltonian dynamics:

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

The chapter derives:

\[
\frac{dH}{dt}
=
\nabla H^\top J\nabla H
=
0.
\]

Exact Hamiltonian flows satisfy:

\[
D\Phi_t^\top J D\Phi_t
=
J.
\]

The chapter also records:

\[
\text{symplectic}
\Rightarrow
\text{volume-preserving},
\]

but not the converse in general dimension.

## G. Harmonic-oscillator witness

For

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

Exact flow:

\[
M(t)
=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}.
\]

The computational witness verifies:

\[
M^\top J M-J=0,
\]

\[
\det M=1,
\]

and

\[
H(Mz)-H(z)=0.
\]

## H. Figure

\`ATLAS-FIG-DYN-001\`

- generator blob:
  \`2cca3d0875f35d88d38fa9d9f1bd65d560ef4ad3\`;
- rendered blob:
  \`b57903c3b8d1c86f37343784eee0aed9893a62a8\`;
- rendered bytes:
  \`186,291\`;
- representation class:
  \`computed\`.

The left panel shows exact pitchfork equilibrium branches and stability class over the displayed parameter range.

The right panel shows the harmonic-oscillator vector field and exact \(H=1/2\) circular trajectory.

## I. Source boundary

External sources:

- Strogatz 2015:
  nonlinear flows, fixed points, bifurcations, phase portraits;
- Khalil 2002:
  nonlinear/Lyapunov stability;
- Hairer–Lubich–Wanner 2006:
  Hamiltonian and symplectic structure.

Atlas-owned interpretation:

- depth as computational time;
- training as coupled dynamics;
- bifurcation/stability as lenses for adaptive systems;
- downstream use in optimization, routing, and architecture.

The chapter does not claim that generic neural or optimizer dynamics are Hamiltonian, symplectic, autonomous, or described by the pitchfork normal form.

## J. Frozen distinctions

\[
\text{local}
\neq
\text{global stability}.
\]

\[
\text{asymptotic stability}
\neq
\text{monotone finite-time contraction}.
\]

\[
\text{exact continuous flow}
\neq
\text{numerical discretization}.
\]

\[
\text{volume-preserving}
\neq
\text{symplectic}.
\]

\[
\text{parameter-dependent change}
\neq
\text{bifurcation without dynamical evidence}.
\]

## K. Durable outputs

The branch contains:

- source lock;
- specification;
- derivation packet;
- exact computational witness;
- complete manuscript;
- Wolfram figure generator;
- rendered figure;
- figure manifest;
- Figure Register entry;
- Chapter Ledger promotion to \`draft-v0.1\`.

## L. Next step after merge

Run a bounded post-draft audit checking:

- continuous/discrete stability criteria;
- zero-linearization counterexample pair;
- Lyapunov argument;
- pitchfork branch/stability algebra;
- Hamiltonian conservation derivation;
- symplectic identity and determinant boundary;
- figure identity;
- source scope;
- no leakage of numerical-analysis claims into this chapter.
