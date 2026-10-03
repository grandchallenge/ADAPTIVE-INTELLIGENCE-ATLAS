# AUDIT-006 — The Residual Formalization

## Disposition

**PASS AFTER ONE FORMAL REPAIR**

\`ATLAS-CH-RESIDUAL-001\` remains at \`draft-v0.1\`.

The merged Residual chapter correctly separated invariance, capability sufficiency, factorization-based leastness, task dependence, and behavior-table trivialization.

AUDIT-006 identified one remaining formal boundary:

> factorization by an arbitrary map defines a semantic information preorder, but does not by itself define operational/computable recoverability.

The chapter, specification, derivation packet, and source lock now include an explicit admissible post-processing class

\[
\mathfrak M.
\]

Leastness is therefore relative to:

\[
(B,G,\mathfrak D,\mathfrak M,\mathcal Q).
\]

This audit does not establish a frontier-model Residual, nor does it promote the Residual programme to established theory.

## Audited baseline

- RESIDUAL-001 merge: \`1d1a0e6ece66b3cca0957064ec00dceaf5c8d841\`;
- audit issue: \`#30\`;
- chapter: \`ATLAS-CH-RESIDUAL-001\`.

## 1. Problem declaration

PASS AFTER REPAIR.

The chapter now declares:

- \(X\): representation/state space;
- \(G\): admissible representation transformations;
- \(\mathcal Q\): capability probes/contexts;
- \(B:X\times\mathcal Q\to\mathcal Y\): behavior profile;
- \(\mathfrak D\): admissible portable descriptor class;
- \(\mathfrak M\): admissible post-processing maps.

The Residual is therefore not specified independently of the task, transfer range, descriptor language, or allowed recovery maps.

## 2. Transformation invariance

PASS.

A descriptor \(R\) is invariant when

\[
R(g\cdot x)=R(x)
\]

for every declared admissible transformation.

The manuscript explicitly demonstrates that invariance alone is insufficient by using the constant descriptor.

## 3. Capability sufficiency

PASS.

A descriptor is sufficient when there exists a declared reconstructor

\[
D:\mathcal Z\times\mathcal Q\to\mathcal Y
\]

with

\[
B(x,q)=D(R(x),q)
\]

for every declared state/probe pair.

The chapter correctly distinguishes this from full-state reconstruction.

## 4. Factorization preorder

PASS AFTER REPAIR.

For

\[
R_1:X\to Z_1,
\qquad
R_2:X\to Z_2,
\]

the chapter now writes

\[
R_1\preceq R_2
\]

when an admissible post-processing map

\[
\phi\in\mathfrak M
\]

satisfies

\[
R_1=\phi\circ R_2.
\]

The chapter states the closure conditions needed for a preorder:

- identity maps belong to \(\mathfrak M\);
- \(\mathfrak M\) is closed under composition.

It then distinguishes:

- semantic factorization: \(\mathfrak M\) contains all maps;
- operational factorization: \(\mathfrak M\) is restricted, for example to efficiently computable or bounded-cost maps.

This distinction prevents an uncomputable post-processing map from silently being treated as an operational reconstruction method.

## 5. Least versus merely minimal

PASS.

The provisional Residual is a **least** element of the invariant sufficient descriptor class under the declared factorization preorder.

Thus for every admissible invariant sufficient \(S\),

\[
R\preceq S.
\]

This is stronger than an informal “small” or merely locally minimal descriptor.

The specification had already corrected this distinction before merge.

## 6. Equivalence of least representatives

PASS.

If \(R\) and \(R'\) are both least, then

\[
R=\phi\circ R',
\]

and

\[
R'=\psi\circ R.
\]

The derivation correctly shows that on realized images,

\[
\psi\circ\phi=\operatorname{id},
\]

and

\[
\phi\circ\psi=\operatorname{id}.
\]

Thus least Residuals are equivalent up to invertible recoding on the states actually realized.

No canonical coordinate system follows.

## 7. Behavior-table trivialization

PASS AFTER REPAIR.

The chapter correctly exposes the trivial candidate

\[
R_B(x)=B_x,
\]

the complete behavior profile.

The audit tightened the statement so that \(R_B\) is least only when:

1. the admissible descriptor class \(\mathfrak D\) contains the behavior-profile object;
2. the behavior profile is invariant under the declared transformations;
3. the admissible post-processing class \(\mathfrak M\) contains the map induced by a sufficient descriptor's decoder that constructs \(B_x\).

Under those assumptions the behavior table is a mathematically valid but potentially scientifically unhelpful least descriptor.

This establishes why descriptor and morphism admissibility are part of the Residual problem.

## 8. Exact calibration model

PASS.

State:

\[
x=(s,n).
\]

Nuisance action:

\[
g_a(s,n)=(s,n+a).
\]

Singleton-probe capability:

\[
B(s,n)=s.
\]

Residual:

\[
R(s,n)=s.
\]

The toy explicitly admits ordinary deterministic decoder/projection maps in \(\mathfrak M\).

### Invariance

\[
R(g_a(s,n))=s=R(s,n).
\]

### Sufficiency

With \(D(r)=r\),

\[
D(R(s,n))=B(s,n).
\]

### Leastness

For every sufficient descriptor \(S\), sufficiency supplies an admissible decoder \(D_S\in\mathfrak M\) such that

\[
B=D_S\circ S.
\]

Since \(R=B\) in this calibration case,

\[
R=D_S\circ S.
\]

Therefore

\[
R\preceq S.
\]

The proof is correct and deliberately toy-level.

It does not establish a frontier-model Residual.

## 9. Invariant but insufficient descriptor

PASS.

The constant descriptor

\[
S_0(x)=0
\]

is invariant.

For

\[
x_1=(2,0),
\qquad
x_2=(3,0),
\]

the descriptor values are equal while the capability values differ.

Therefore no deterministic decoder can reconstruct both.

This correctly demonstrates

\[
\text{invariance}
\not\Rightarrow
\text{sufficiency}.
\]

## 10. Full-state descriptor

PASS.

The identity descriptor

\[
S_{\rm full}(s,n)=(s,n)
\]

is sufficient for the toy capability but retains nuisance information.

The chapter uses this only to show that full-state reconstruction is stronger than capability sufficiency.

## 11. Invertible recoding witness

PASS.

The recoding

\[
T=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
\]

has determinant

\[
-2,
\]

so it is invertible.

For

\[
x=(2,5),
\]

independent Wolfram replay gives

\[
z=Tx=(7,-3).
\]

The Residual reconstructs exactly as

\[
\frac{z_1+z_2}{2}=2.
\]

The same witness verifies nuisance motion

\[
(2,5)\to(2,2)
\]

while preserving Residual value \(2\).

This supports the intended distinction:

\[
\text{transferable structure}
\neq
\text{fixed coordinate slot}.
\]

## 12. Capability-preserving transformation condition

PASS.

The manuscript states the necessary compatibility condition:

if an admissible transformation changes the declared capability, then no descriptor can be both exactly invariant to that transformation and exactly sufficient for the capability.

Thus exact Residual search requires capability-preserving admissible transformations.

## 13. External source scope

PASS.

### Lehmann–Casella

Used for classical sufficiency/minimal-sufficiency background and factorization-style minimality.

The chapter does not claim that classical statistical sufficiency directly proves the generalized Residual theory.

### Achille–Soatto

Used for a task-relative framework combining sufficiency, minimality, and nuisance invariance.

The chapter states that its extension to arbitrary transferable computational structure is Atlas-owned.

### Tishby–Pereira–Bialek

Used as precedent for compression while preserving declared relevant information.

The chapter explicitly does not define the Residual as an information-bottleneck optimum in general.

## 14. Atlas provenance

PASS.

The source lock pins the original Atlas inventory at Git blob

\`ee83f2cadfcf725930b2076ba4c52ae1190647f8\`.

That source explicitly contains:

- semantic equivalence under representational change;
- minimal transferable representations;
- “The Residual”: structure that survives representation change.

The source lock also pins the audited Representation and Quotient manuscripts:

- Representation blob:
  \`6109e6ac9505a339cb8bc2dd85a8b9bc882f72bb\`;
- Quotient blob:
  \`3b372f76765996bf24dac39aec70aa39dc401553\`.

The generalized Residual remains project synthesis rather than external established theory.

## 15. Figure provenance

PASS.

\`ATLAS-FIG-RESIDUAL-001\`:

- generator blob:
  \`718ee3beed852f488c05e5cea08145c06fd2fe7a\`;
- rendered blob:
  \`78083586f7b699db57e068a429efa1a7aed038fa\`;
- rendered bytes:
  \`49,297\`.

The manifest values match the audited Git tree.

The figure is correctly classed schematic because orbit spacing, box placement and arrows are pedagogical even though all annotated coordinates and reconstructions are exact.

## 16. Nonclaims retained

PASS.

The chapter does not claim that a frontier-system Residual is:

- known;
- unique in coordinates;
- finite-dimensional;
- efficiently computable;
- efficiently learnable;
- architecture-independent;
- an information-bottleneck optimum;
- a classical sufficient statistic;
- a universal invariant of intelligence.

Approximate Residuals are identified as a later research problem.

## 17. Final disposition

AUDIT-006 passes after one formal repair.

The durable Residual definition is now relative to:

\[
(B,G,\mathfrak D,\mathfrak M,\mathcal Q).
\]

The chapter remains:

\`draft-v0.1\`.

It is now suitable to act as the formal bridge to later programmes on:

- minimal curriculum;
- minimal reasoning basis;
- model interoperability;
- reconstruction under representational change;
- memory compression;
- governed adaptation.

Those later chapters should inherit the descriptor/morphism-class caveat rather than silently reverting to an unconstrained notion of “minimal transferable structure.”
