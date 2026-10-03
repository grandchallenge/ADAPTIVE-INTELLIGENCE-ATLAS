# RESIDUAL-001 — The Minimal Transferable Residual

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- AUDIT-005 merge: \`dcd65b0edcb954f66990aa36b33cda1c7ca2175d\`;
- issue: \`#28\`;
- prerequisite \`ATLAS-CH-QUOTIENT-001\`: audited \`draft-v0.1\`.

## Objective

Formalize the Atlas/GCL Residual programme:

> Find the least admissible transferable structure sufficient to reconstruct a declared capability after admissible changes of representation or parameterization.

The chapter does not claim that such an object exists, is unique in coordinates, is finite-dimensional, or is efficiently learnable for arbitrary neural systems.

## A. Formal problem statement

Declare:

- representation/state space \(X\);
- admissible transformation family \(G\);
- capability probe family \(\mathcal Q\);
- behavior profile
  \[
  B:X\times\mathcal Q\to\mathcal Y;
  \]
- admissible portable descriptor class \(\mathfrak D\).

A descriptor

\[
R:X\to\mathcal Z,
\qquad
R\in\mathfrak D
\]

is transformation-invariant when

\[
R(g\cdot x)=R(x).
\]

It is capability-sufficient when some reconstructor

\[
D:\mathcal Z\times\mathcal Q\to\mathcal Y
\]

satisfies

\[
B(x,q)=D(R(x),q)
\]

for every declared state/probe pair.

## B. Factorization preorder

For descriptors \(R_1,R_2\),

\[
R_1\preceq R_2
\]

when

\[
R_1=\phi\circ R_2
\]

for some post-processing map \(\phi\).

Interpretation:

\(R_1\) retains no more distinctions than \(R_2\).

The provisional Residual is a **least** invariant sufficient descriptor within the declared admissible class.

This tranche explicitly corrected an earlier loose use of “minimal”: a least element factors from every other admissible sufficient invariant descriptor. Merely minimal elements need not have that property.

## C. Equivalence of least representatives

If \(R\) and \(R'\) are both least, then

\[
R=\phi\circ R',
\qquad
R'=\psi\circ R.
\]

On their realized images,

\[
\psi\circ\phi=\operatorname{id},
\qquad
\phi\circ\psi=\operatorname{id}.
\]

Thus least Residuals are equivalent up to invertible recoding on realized states.

No canonical coordinate basis is implied.

## D. Behavior-table trivialization

A second formal correction is load-bearing.

If the admissible descriptor class allows an unconstrained complete behavior profile

\[
R_B(x)=B_x,
\]

then \(R_B\) is already a sufficient object and, when behavior is invariant, a trivial least candidate.

Therefore a nontrivial Residual problem must declare structural restrictions on \(\mathfrak D\), for example:

- portability;
- finite description length;
- bounded reconstruction cost;
- efficient computability;
- architectural independence;
- intervention stability.

Descriptor admissibility is part of the mathematical problem, not editorial metadata.

## E. Exact calibration model

Let

\[
X=\mathbb R^2,
\qquad
x=(s,n).
\]

Nuisance transformations:

\[
g_a(s,n)=(s,n+a).
\]

Singleton-probe capability:

\[
B(s,n)=s.
\]

Candidate Residual:

\[
R(s,n)=s.
\]

### Invariance

\[
R(g_a(s,n))
=
s
=
R(s,n).
\]

### Sufficiency

With \(D(r)=r\),

\[
D(R(s,n))
=
B(s,n).
\]

### Leastness

For any sufficient descriptor \(S\), there is a decoder \(D_S\) with

\[
B=D_S\circ S.
\]

Since in this calibration model

\[
R=B,
\]

we have

\[
R=D_S\circ S,
\]

hence

\[
R\preceq S.
\]

The example is deliberately trivial enough that the definition can be checked exactly.

It is not evidence that frontier-model Residuals have this form.

## F. Invariance is not sufficiency

The constant descriptor

\[
S_0(x)=0
\]

is invariant.

But

\[
B(2,0)=2,
\qquad
B(3,0)=3,
\]

while both states map to the same constant descriptor.

Thus

\[
\text{invariant}
\not\Rightarrow
\text{sufficient}.
\]

## G. Representation-change witness

Let

\[
T=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

For

\[
x=(s,n),
\]

the recoded state is

\[
z=Tx=(s+n,s-n).
\]

The Residual reconstructs as

\[
s=\frac{z_1+z_2}{2}.
\]

For

\[
x=(2,5),
\]

\[
z=(7,-3),
\]

and

\[
\frac{7+(-3)}2=2.
\]

The Wolfram witness also verifies nuisance motion

\[
(2,5)\to(2,2)
\]

without changing the Residual value.

## H. Source boundary

External sources provide only supporting structures:

- Lehmann–Casella: statistical sufficiency/minimal-sufficiency background;
- Achille–Soatto: task-relative sufficient/minimal representations and nuisance invariance under the paper's framework;
- Tishby–Pereira–Bialek: compression while preserving target-relevant information.

The generalized Residual object is Atlas/GCL synthesis.

Its project origin is explicitly source-locked to the original Atlas inventory, which names:

- semantic equivalence under representational change;
- minimal transferable representations;
- “The Residual”: structure that survives representation change.

## I. Figure

\`ATLAS-FIG-RESIDUAL-001\`

- generator blob:
  \`718ee3beed852f488c05e5cea08145c06fd2fe7a\`;
- rendered blob:
  \`78083586f7b699db57e068a429efa1a7aed038fa\`;
- rendered bytes:
  \`49,297\`;
- representation class:
  schematic with exact state, transformation, and reconstruction annotations.

## J. Durable objects

The branch contains:

- \`sources/source-locks/ATLAS-CH-RESIDUAL-001.yaml\`;
- \`manuscript/specifications/ATLAS-CH-RESIDUAL-001.md\`;
- \`mathematics/derivations/ATLAS-CH-RESIDUAL-001-DERIVATIONS.md\`;
- \`mathematics/computational-witnesses/ATLAS-CW-RESIDUAL-001.md\`;
- \`manuscript/parts/03-representation-learning/ATLAS-CH-RESIDUAL-001.md\`;
- Wolfram generator;
- rendered figure;
- figure manifest;
- Figure Register entry;
- Chapter Ledger promotion to \`draft-v0.1\`.

## K. Frozen distinctions

\[
\text{invariance}
\neq
\text{sufficiency}.
\]

\[
\text{capability reconstruction}
\neq
\text{full-state reconstruction}.
\]

\[
\text{least under factorization}
\neq
\text{small by intuition}.
\]

\[
\text{complete behavior profile}
\neq
\text{nontrivial portable mechanism}.
\]

\[
\text{coordinate survival}
\neq
\text{transferable structure}.
\]

\[
\text{toy Residual}
\neq
\text{frontier invariant discovered}.
\]

## L. Next step after merge

Run a bounded post-draft audit.

The audit must check:

- least-versus-minimal logic;
- behavior-table trivialization;
- exact nuisance-orbit proof;
- recoding reconstruction;
- task/transformation dependence;
- external-source scope;
- figure provenance;
- no promotion of the Residual into an established universal invariant.
