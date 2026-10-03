# Chapter Specification — ATLAS-CH-RESIDUAL-001

## Identity

**Title:** The Residual  
**Part:** Representation Learning  
**Status:** specification-ready.  
**Epistemic class:** Atlas/GCL research synthesis grounded in established sufficiency and invariance ideas.

## Chapter contract

Formalize the search for the smallest transferable structure from which a declared capability can be reconstructed after admissible changes of representation or parameterization.

The chapter must not assume that the Residual:

- exists for every system;
- is unique;
- is a vector;
- is low-dimensional;
- is efficiently computable;
- is independent of task/capability definition.

## Dependency contract

Hard prerequisite:

- \`ATLAS-CH-QUOTIENT-001\`.

Inherited:

- \`ATLAS-CH-REP-001\`;
- \`ATLAS-CH-INFO-001\`;
- \`ATLAS-CH-GEOM-001\`.

## Reader outcome

A reader should be able to:

1. distinguish an invariant from a capability-sufficient descriptor;
2. define a factorization preorder among descriptors;
3. define a provisional minimal sufficient Residual;
4. explain why capability sufficiency is weaker than full-state reconstruction;
5. distinguish coordinate survival from reconstructable structure;
6. understand why a Residual may be an equivalence class, operator, program, graph, or relation rather than a vector;
7. state nonexistence/nonuniqueness/learnability caveats;
8. identify exact reconstruction tests that could falsify a proposed Residual.

## Formal spine

Let:

- \(X\) be a representation/state space;
- \(G\) be a declared family of admissible transformations acting on \(X\);
- \(B:X\to\mathcal Y\) be a declared capability/behavior map.

A descriptor

\[
R:X\to\mathcal Z
\]

is **transformation invariant** if

\[
R(g\cdot x)=R(x)
\]

for all admissible \(g\).

It is **capability sufficient** if there exists a reconstructor

\[
D:\mathcal Z\to\mathcal Y
\]

such that

\[
B=D\circ R.
\]

For descriptors \(R_1,R_2\), define

\[
R_1\preceq R_2
\]

when there exists \(\phi\) with

\[
R_1=\phi\circ R_2.
\]

Thus \(R_1\) contains no more distinctions than \(R_2\).

A provisional **Residual** is an invariant, capability-sufficient descriptor minimal under this preorder:

for every other invariant capability-sufficient descriptor \(S\),

\[
R\preceq S.
\]

The chapter must state that minimal objects need not exist or be unique without additional assumptions.

## Principal pedagogical device

### Allegory: the message that survives translation

Different encodings can rewrite every surface symbol while preserving what a receiver still needs to act correctly.

Correspondence:

- encoding ↔ representation;
- translation ↔ admissible transformation;
- task-relevant meaning ↔ declared capability;
- shortest adequate message ↔ minimal sufficient Residual.

Limit:

Natural-language “meaning” is not a formal capability map, and shortest messages depend on the language/coding class. The allegory teaches survival plus sufficiency, not universal semantic essence.

## Exact toy model

Use

\[
X=\mathbb R^2
\]

with state

\[
x=(s,n).
\]

Let nuisance transformations translate only the second coordinate:

\[
g_a(s,n)
=
(s,n+a).
\]

Let declared capability be

\[
B(s,n)=s.
\]

Define

\[
R(s,n)=s.
\]

Then:

- \(R\) is invariant under every \(g_a\);
- \(B=R\), so it is sufficient;
- any invariant sufficient descriptor \(S\) admits a decoder \(D_S\) with
  \[
  R=D_S\circ S,
  \]
  so \(R\preceq S\).

Thus \(R=s\) is minimal in this declared toy setting.

## Representation-change witness

Use invertible recoding

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

the new coordinates are

\[
z=T x=(s+n,s-n).
\]

The same Residual can be reconstructed as

\[
s=\frac{z_1+z_2}{2}.
\]

Therefore the transferable object is not tied to one coordinate slot.

## Counterexamples and failure boundaries

Include:

- invariant but insufficient descriptor:
  \[
  R(x)=0;
  \]
- sufficient but nonminimal descriptor:
  \[
  S(s,n)=(s,n);
  \]
- task dependence:
  if capability changes to \(B'(s,n)=(s,n)\), then \(R=s\) is no longer sufficient;
- too-large transformation family that identifies capability-distinct states;
- no finite-dimensional Residual guaranteed in general;
- two incomparable minimal candidates may exist without stronger structure.

## Computational witness

Exact Wolfram replay of:

- nuisance-orbit invariance;
- reconstruction from transformed coordinates;
- constant descriptor insufficiency on two different signal values.

## Figure programme

### ATLAS-FIG-RESIDUAL-001

Show:

1. vertical nuisance orbits in \((s,n)\)-space collapsing to the \(s\)-axis;
2. an invertible coordinate recoding where the Residual must be reconstructed from both new coordinates.

Representation class: schematic with exact coordinates/relations.

## Source roles

Use:

- Lehmann–Casella for classical sufficiency/minimal-sufficiency background;
- Achille–Soatto for task-relative sufficient/minimal representations and nuisance invariance;
- Tishby–Pereira–Bialek for compression while preserving declared relevant information;
- audited Atlas Representation and Quotient chapters for the project-local generalization.

## Downstream obligations

The chapter should supply a precise object to later programmes on:

- transfer;
- minimal reasoning basis;
- minimal curriculum;
- model interoperability;
- reconstruction under representational change;
- benign nonconvexity;
- governed adaptation.

## Acceptance

The draft must:

- define invariance, sufficiency, and minimality separately;
- include the factorization preorder;
- prove the toy Residual's minimality in the declared setting;
- include one invertible recoding reconstruction;
- state explicit nonexistence/nonuniqueness caveats;
- include a falsifiable reconstruction test;
- avoid presenting the Residual as already discovered in frontier models;
- include source lock, witness, and figure provenance.
