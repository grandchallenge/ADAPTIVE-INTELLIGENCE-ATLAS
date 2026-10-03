# AUDIT-008 — Flows, Stability, and Bifurcation

## Disposition

**PASS AFTER ONE PROVENANCE / SELF-CONTAINMENT REPAIR**

\`ATLAS-CH-DYN-001\` remains at \`draft-v0.1\`.

The chapter's dynamical-systems mathematics, exact witnesses, source scope, and figure provenance pass audit.

AUDIT-008 found one documentary overreach:

> the Dynamics source lock said the upstream Linear Algebra chapter supplied matrix-exponential material, but that audited chapter did not actually develop matrix exponentials.

The repair:

- removes matrix exponentials from the prerequisite assumption list;
- narrows the Linear Algebra source-role statement;
- defines
  \[
  e^{tA}
  =
  \sum_{k=0}^{\infty}\frac{(tA)^k}{k!}
  \]
  inside Dynamics;
- records the derivative/initial-value identities needed for
  \[
  x(t)=e^{tA}x_0.
  \]

No numerical-integration chapter has been started by this audit.

## Audited baseline

- DYNAMICS-001 merge:
  \`d2976b981c6acf44c597fe97532d206fb1fcfe0a\`;
- audit issue:
  \`#40\`;
- chapter:
  \`ATLAS-CH-DYN-001\`.

## 1. Vector field / trajectory / flow distinction

PASS.

The chapter distinguishes:

- vector field:
  local law of motion;
- trajectory:
  one realized solution path;
- flow map:
  exact finite-time transport;
- numerical update:
  a separate discrete map.

For an autonomous flow,

\[
\Phi_{t+s}
=
\Phi_t\circ\Phi_s.
\]

The chapter explicitly states that a depth-indexed neural computation is only flow-like unless this stronger structure is justified.

## 2. Constant linear flow

PASS AFTER REPAIR.

For

\[
\dot x=Ax,
\]

Dynamics now defines

\[
e^{tA}
=
\sum_{k=0}^{\infty}
\frac{(tA)^k}{k!}.
\]

It states

\[
\frac{d}{dt}e^{tA}
=
Ae^{tA},
\qquad
e^{0A}=I,
\]

so

\[
x(t)=e^{tA}x_0
\]

solves the constant linear initial-value problem.

This construction is now chapter-local rather than incorrectly attributed to the upstream Linear Algebra manuscript.

## 3. Equilibrium and linearization

PASS.

For

\[
f(x_\star)=0,
\]

the chapter uses

\[
f(x_\star+\delta)
=
J_f(x_\star)\delta
+
O(\|\delta\|^2)
\]

and therefore

\[
\dot\delta
=
J_f(x_\star)\delta
+
O(\|\delta\|^2).
\]

The claim remains local.

## 4. Hyperbolic stability claims

PASS.

Under the differentiability/local regularity assumed by the chapter:

- all Jacobian eigenvalues with strictly negative real part imply local exponential stability;
- at least one eigenvalue with strictly positive real part implies instability;
- zero-real-part / imaginary-axis cases are explicitly declared inconclusive under linearization alone.

The chapter's examples

\[
\dot x=-x^3
\]

and

\[
\dot x=x^3
\]

correctly show opposite nonlinear outcomes with identical zero linearization.

## 5. Lyapunov distinctions

PASS.

The chapter distinguishes:

- Lyapunov stability;
- asymptotic stability;
- exponential stability.

For a positive-definite local Lyapunov candidate \(V\),

\[
\dot V\le0
\]

is not promoted into automatic asymptotic convergence.

The chapter explicitly notes that negative-semidefinite derivative can require additional invariant-set reasoning.

## 6. Exact scalar witness

PASS.

Independent symbolic replay gives, for

\[
\dot x=-2x,
\qquad
x(0)=3,
\]

\[
x(t)=3e^{-2t}.
\]

For

\[
V(x)=x^2/2,
\]

replay gives

\[
\dot V=-2x^2.
\]

The exponential-stability example is exact.

## 7. Saddle-node classification

PASS.

For

\[
\dot x=\mu-x^2,
\]

the equilibria are

\[
x_\star=\pm\sqrt{\mu}
\]

for \(\mu>0\).

The derivative is

\[
f'(x)=-2x.
\]

Therefore:

- \(+\sqrt{\mu}\) is locally stable;
- \(-\sqrt{\mu}\) is unstable;
- the collision at \(\mu=0\) is nonhyperbolic;
- no real equilibria exist for \(\mu<0\).

## 8. Pitchfork classification

PASS.

For

\[
\dot x=\mu x-x^3,
\]

equilibria are

\[
x=0,
\]

and, for \(\mu>0\),

\[
x=\pm\sqrt{\mu}.
\]

With

\[
f'(x)=\mu-3x^2,
\]

the origin is locally stable for \(\mu<0\) and unstable for \(\mu>0\), while both nonzero branches are locally stable for \(\mu>0\).

## 9. Hopf scope

PASS.

The chapter uses only the qualitative supercritical normal form

\[
\dot r=\mu r-r^3,
\qquad
\dot\theta=\omega.
\]

It does not claim to prove the general Hopf theorem.

It correctly identifies the stable fixed-point / stable-cycle qualitative transition in the normal form.

## 10. Hamiltonian conservation

PASS.

For canonical Hamiltonian dynamics

\[
\dot z=J\nabla H(z),
\qquad
J^\top=-J,
\]

the derivation gives

\[
\frac{dH}{dt}
=
\nabla H^\top J\nabla H
=
0.
\]

The claim is correctly scoped to autonomous canonical Hamiltonian dynamics.

## 11. Harmonic-oscillator exact flow

PASS.

For

\[
A=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

independent Wolfram replay gives

\[
e^{tA}
=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}.
\]

## 12. Symplectic identity

PASS.

With

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

independent replay gives

\[
M(t)^\top J M(t)-J
=
0.
\]

The exact harmonic-oscillator flow is symplectic.

## 13. Energy conservation

PASS.

For

\[
H(q,p)=\frac12(q^2+p^2),
\]

independent replay gives

\[
H(M(t)z)-H(z)=0.
\]

The chapter explicitly separates exact energy conservation from symplecticity as general properties.

## 14. Continuous flow versus numerical update

PASS.

The chapter freezes

\[
\Phi_h
\neq
\Psi_h
\]

in general.

It uses explicit Euler on

\[
\dot x=-\lambda x
\]

to show that the exact continuous system is exponentially stable for every \(\lambda>0\), while the discrete update

\[
x_{n+1}=(1-h\lambda)x_n
\]

is asymptotically stable only when

\[
|1-h\lambda|<1.
\]

This is an appropriate handoff to Numerics.

## 15. Neural flow interpretation boundary

PASS.

The chapter states that residual updates can resemble numerical discretizations but do not prove the existence of one underlying autonomous ODE.

The source lock likewise denies a universal ODE/Hamiltonian interpretation of neural networks.

## 16. External source scope

PASS.

### Khalil 2002

Used for nonlinear stability, Lyapunov methods, and local/global stability language.

### Kuznetsov 2004

Used for local bifurcation theory and normal forms.

### Hairer–Lubich–Wanner 2006

Used for Hamiltonian/symplectic structure and the later geometric-numerics handoff.

No source is used to support Atlas-specific claims about neural depth or optimization dynamics.

## 17. Atlas provenance

PASS AFTER REPAIR.

Pinned seed inventory:

\`ee83f2cadfcf725930b2076ba4c52ae1190647f8\`.

Pinned audited Linear Algebra manuscript:

\`e7fcf56322f26d232d3a3043038d9850792b4bde\`.

The Linear Algebra source role is now accurately limited to eigenvalues, singular values, norms, and finite-dimensional linear-map language.

Matrix-exponential construction is owned by Dynamics.

## 18. Figure provenance

PASS.

\`ATLAS-FIG-DYN-001\`:

- generator blob:
  \`7ebe6417e356defc326e60c4bb0c95f4458a406e\`;
- rendered blob:
  \`4b1215889f85c29f36fa7e5f419f755068ba19e5\`;
- rendered bytes:
  \`50,300\`.

The three panels use exact analytic curves for:

- exponential attraction;
- saddle-node branches;
- harmonic-oscillator orbit.

The manifest matches the audited Git tree.

## 19. Chapter status

PASS.

\`ATLAS-CH-DYN-001\` remains:

\`draft-v0.1\`.

Its hard prerequisite remains:

- \`ATLAS-CH-LINALG-001\`.

## 20. Final disposition

AUDIT-008 passes after one provenance/self-containment repair.

The Dynamics chapter now supplies a clean audited substrate for:

- \`ATLAS-CH-NUMERICS-001\`;
- \`ATLAS-CH-ARCHHIST-001\`;
- \`ATLAS-CH-LATENTTIME-001\`;
- \`ATLAS-CH-OPTBASE-001\`;
- \`ATLAS-CH-RLBASE-001\`.

The next dependency-led mathematical tranche may begin with \`ATLAS-CH-NUMERICS-001\`.
