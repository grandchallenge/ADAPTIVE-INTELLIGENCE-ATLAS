# NUMERICS-001 — Discretization, Stability, and Splitting

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- AUDIT-008 merge: \`3c5050b50663e16725620dcf236a6bad61841d82\`;
- issue: \`#43\`;
- hard prerequisite:
  - \`ATLAS-CH-DYN-001\` — audited \`draft-v0.1\`.

## Objective

Develop the numerical-analysis substrate required by later Atlas chapters on adaptive depth, split operators, variational optimization, and Numerical Intelligence.

The chapter keeps three questions separate:

1. local approximation;
2. discrete stability;
3. global convergence.

It then adds stiffness and operator splitting as the first examples where method structure changes qualitative behavior.

## A. One-step framework

For

\[
\dot x=f(t,x),
\]

the numerical method is

\[
x_{n+1}
=
\Psi_h(t_n,x_n).
\]

The local defect from an exact state is

\[
\delta_{n+1}
=
\Phi_h(t_n,x(t_n))
-
\Psi_h(t_n,x(t_n)).
\]

An order-\(p\) method has

\[
\delta_{n+1}
=
O(h^{p+1})
\]

under the required smoothness assumptions.

With a suitable finite-time stability/Lipschitz bound on error propagation, the global error obeys

\[
e_n
=
O(h^p).
\]

The tranche explicitly freezes:

\[
\text{consistency alone}
\not\Rightarrow
\text{convergence}.
\]

## B. Euler methods

Explicit Euler:

\[
x_{n+1}
=
x_n+h f(t_n,x_n).
\]

Implicit Euler:

\[
x_{n+1}
=
x_n+h f(t_{n+1},x_{n+1}).
\]

For the scalar test equation

\[
y'=\lambda y,
\qquad
z=h\lambda,
\]

the exact stability functions are:

\[
R_{\rm EE}(z)=1+z,
\]

\[
R_{\rm IE}(z)=\frac{1}{1-z}.
\]

Absolute stability requires

\[
|R(z)|<1.
\]

Thus:

- explicit Euler:
  \[
  |1+z|<1;
  \]
- implicit Euler:
  \[
  |1-z|>1.
  \]

Implicit Euler is A-stable and L-stable.

## C. Exact stiff witness

Take

\[
y'=-100y,
\qquad
h=0.05.
\]

Then

\[
z=-5.
\]

Exact one-step factor:

\[
e^{-5}
\approx
0.00673795.
\]

Explicit Euler:

\[
R_{\rm EE}(-5)=-4.
\]

Implicit Euler:

\[
R_{\rm IE}(-5)=\frac16.
\]

Therefore:

- explicit Euler is unstable at this step;
- implicit Euler is stable;
- implicit Euler is still inaccurate at this coarse step.

The tranche freezes:

\[
\text{stability}
\neq
\text{accuracy}.
\]

## D. Stiffness scope

The chapter treats stiffness as a problem/method interaction in which numerical stability can force a step size much smaller than the slower behavior of interest would otherwise require.

It does not define stiffness as merely a large derivative or large eigenvalue.

## E. Lie–Trotter splitting

For

\[
\dot x=(A+B)x,
\]

the declared ordering is

\[
S_{\rm LT}(h)
=
e^{hA}e^{hB}.
\]

For bounded matrices,

\[
S_{\rm LT}(h)
-
e^{h(A+B)}
=
\frac{h^2}{2}[A,B]
+
O(h^3),
\]

where

\[
[A,B]=AB-BA.
\]

The exact witness uses

\[
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]

Then

\[
[A,B]
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Wolfram gives the declared leading defect exactly.

## F. Strang splitting

The symmetric composition is

\[
S_{\rm S}(h)
=
e^{hA/2}
e^{hB}
e^{hA/2}.
\]

For the declared bounded-matrix witness, Wolfram verifies that the first nonzero local-defect terms are order

\[
h^3.
\]

This is the expected second-order global Strang behavior under the usual stability/regularity assumptions.

The chapter does not extend this order statement to unbounded operators without the necessary domain assumptions.

## G. Commuting versus noncommuting structure

The tranche preserves the exact constant-matrix identity:

if

\[
[A,B]=0,
\]

then

\[
e^{hA}e^{hB}
=
e^{h(A+B)}.
\]

Thus the leading split obstruction is algebraic noncommutativity, not merely the magnitude of the suboperators.

## H. Structure preservation

The chapter treats “structure-preserving” as incomplete unless the preserved structure is named.

Examples include:

- symplectic form;
- norm;
- positivity;
- mass;
- reversibility;
- constraint manifold.

No generic structure-preservation claim is made.

## I. Source boundary

External references:

- Iserles 2008:
  one-step consistency/convergence/stability language;
- Hairer–Wanner 1996:
  stiff ODEs, implicit methods, absolute stability;
- McLachlan–Quispel 2002:
  splitting/composition methods;
- Hairer–Lubich–Wanner 2006:
  structure-preserving / backward-error handoff.

Atlas-specific synthesis:

- depth as a possible step budget;
- adaptive depth as possible error control;
- commutators as architectural split diagnostics;
- implicit computation as a numerical-design analogy;
- SPINDLE/SPLICE relevance.

No claim is made that learned residual blocks are automatically numerical integrators.

## J. Figure

\`ATLAS-FIG-NUMERICS-001\`

- generator blob:
  \`c7095b46e2ab622eba1e06cc2a19fa6d83e7fa84\`;
- rendered blob:
  \`7f23da82f51ac006cccf1be2e055b06ac8a2b715\`;
- rendered bytes:
  \`46,057\`;
- representation class:
  data-derived.

Panels:

1. exact explicit-Euler stability disk;
2. exact implicit-Euler absolute-stability region in the shown window;
3. exact-matrix Lie/Strang local-defect norms over the declared \(h\)-grid.

## K. Durable objects

The branch contains:

- \`sources/source-locks/ATLAS-CH-NUMERICS-001.yaml\`;
- \`manuscript/specifications/ATLAS-CH-NUMERICS-001.md\`;
- \`mathematics/derivations/ATLAS-CH-NUMERICS-001-DERIVATIONS.md\`;
- \`mathematics/computational-witnesses/ATLAS-CW-NUMERICS-001.md\`;
- \`manuscript/parts/02-mathematical-substrate/ATLAS-CH-NUMERICS-001.md\`;
- Wolfram generator/master/manifest;
- Figure Register entry;
- Chapter Ledger promotion to \`draft-v0.1\`.

## L. Frozen distinctions

\[
\text{local defect}
\neq
\text{global error}.
\]

\[
\text{consistency}
\neq
\text{convergence without stability}.
\]

\[
\text{absolute stability}
\neq
\text{accuracy}.
\]

\[
\text{implicit}
\neq
\text{unconditionally accurate}.
\]

\[
\text{stiffness}
\neq
\text{large derivative alone}.
\]

\[
\text{module composition}
\neq
\text{numerical splitting without an underlying evolution model}.
\]

\[
\text{structure-preserving}
\neq
\text{all structures preserved}.
\]

## M. Downstream gate

Direct consumers are:

- \`ATLAS-CH-DEPTH-001\`;
- \`ATLAS-CH-SPLIT-001\`;
- \`ATLAS-CH-VARIOPT-001\`;
- \`ATLAS-CH-NETNUM-001\`.

NUMERICS-001 alone does **not** necessarily make any of those executable because each has additional hard prerequisites.

After the Numerics audit merges, recompute the Chapter Ledger frontier rather than assuming downstream readiness.

## N. Next step after merge

Run a bounded post-draft audit checking:

- local-defect/global-error statements;
- explicit/implicit Euler stability functions;
- A-stability and L-stability wording;
- stiff exact witness;
- stability-versus-accuracy boundary;
- stiffness scope;
- Lie–Trotter sign/order for the declared ordering;
- exact commutator;
- Strang local defect order;
- commuting exactness;
- structure-preserving scope;
- Dynamics/source pin identities;
- figure provenance.

Do not begin any direct consumer until that audit merges and its other dependencies are checked.
