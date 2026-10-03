# Chapter Specification — ATLAS-CH-QUOTIENT-001

## Identity

**Title:** Equivalence and Quotient Geometry  
**Part:** Representation Learning  
**Status:** specification-ready.

## Chapter contract

Develop quotient thinking as the mathematical response to redundant parameterizations and representations.

The chapter asks:

> When multiple coordinates represent the same functional object, should analysis be performed on the representatives or on the equivalence classes?

It must distinguish established quotient geometry from the open programme of using quotient structure to simplify learning landscapes.

## Dependency contract

Hard prerequisites:

- \`ATLAS-CH-GEOM-001\`;
- \`ATLAS-CH-REP-001\`.

May assume:

- equivalence under invertible recoding;
- Stiefel versus Grassmann distinction;
- basic group-action language.

Must not assume:

- a generic quotient of neural-network parameter space is globally a smooth manifold;
- quotienting removes every degeneracy;
- quotient geometry guarantees easier optimization.

## Reader outcome

A reader should be able to:

1. define an equivalence relation and equivalence class;
2. define a quotient set \(X/{\sim}\);
3. interpret a group orbit as an equivalence class under a group action;
4. explain Grassmann as a quotient of Stiefel by orthogonal basis changes;
5. derive hidden-unit permutation symmetry in a two-layer network;
6. derive positive rescaling symmetry for ReLU networks;
7. distinguish parameter equality from functional equality;
8. explain vertical/orbit directions versus function-changing directions locally;
9. state why quotienting can remove redundancy without guaranteeing a simple global landscape.

## Formal spine

Define:

\[
x\sim y
\]

with reflexivity, symmetry, and transitivity.

Define

\[
X/{\sim}
=
\{[x]:x\in X\}.
\]

For a group \(G\) acting on \(X\), define the orbit

\[
G\cdot x
=
\{g\cdot x:g\in G\}.
\]

Use

\[
\operatorname{Gr}(n,p)
\cong
\operatorname{St}(n,p)/O(p)
\]

as the canonical geometry example.

For a one-hidden-layer network

\[
f(x)
=
W_2\sigma(W_1x),
\]

derive exact hidden-unit permutation symmetry:

\[
W_1'=PW_1,
\qquad
W_2'=W_2P^{-1}.
\]

For elementwise ReLU and positive diagonal \(D\), derive exact positive-rescaling symmetry:

\[
W_1'=DW_1,
\qquad
W_2'=W_2D^{-1}.
\]

## Principal pedagogical device

### Allegory: many addresses, one place

Different coordinate addresses can refer to the same mathematical location.

Structural correspondence:

- address ↔ parameter representative;
- location ↔ equivalence class / function;
- changing address convention ↔ symmetry action;
- quotient map ↔ forgetting redundant labeling.

Limit:

Neural parameter spaces can have singular orbits, hidden symmetries, and changing stabilizers. The quotient need not be globally smooth or simple.

## Exact witness

Use a scalar-input, two-hidden-unit ReLU network.

Choose

\[
W_1=
\begin{pmatrix}
1\\
2
\end{pmatrix},
\qquad
W_2=
\begin{pmatrix}
3&4
\end{pmatrix}.
\]

Verify exactly on symbolic structure and a finite input grid that:

- swapping hidden units leaves \(f\) unchanged;
- positive diagonal rescaling leaves \(f\) unchanged.

Also show the parameter vectors are numerically different.

## Figure programme

### ATLAS-FIG-QUOTIENT-001

Show three distinct parameter representatives connected by symmetry arrows and mapping to one identical function curve.

Representation class: exact/data-derived hybrid only if every curve is computed from the declared toy network; otherwise schematic with exact numeric annotations.

Prefer exact if practical.

## Counterexamples and failure boundaries

Include:

- quotienting by an equivalence relation that is too coarse and merges functionally distinct models;
- singular/non-free group actions;
- a quotient that removes redundancy but leaves nonconvexity;
- hidden symmetries beyond permutation and positive scaling [@GrigsbyLindseyRolnick2023];
- symmetry effects on learning that depend on objective/dynamics assumptions [@Ziyin2024Symmetry].

## Atlas research question

State explicitly:

> Can a useful class of benign neural nonconvexity be identified as redundancy that disappears, or becomes simpler, after quotienting by known representation/parameter symmetries?

This is an Atlas/GCL research question.

It is not an established theorem.

## Downstream obligations

Primary consumer:

- \`ATLAS-CH-RESIDUAL-001\`.

Also supplies language to:

- benign nonconvexity;
- optimizer geometry;
- representation equivalence;
- symmetry-aware diagnostics.

## Sources

- [@Lee2018Riemannian]
- [@AbsilMahonySepulchre2008]
- [@EdelmanAriasSmith1998]
- [@GrigsbyLindseyRolnick2023]
- [@Ziyin2024Symmetry]

Source lock: \`sources/source-locks/ATLAS-CH-QUOTIENT-001.yaml\`.

## Acceptance

The draft must:

- include exact permutation and positive-rescaling derivations;
- preserve the regular/singular quotient caveat;
- distinguish parameter-space and function-space identity;
- keep “quotient simplifies learning landscape” at open-problem status;
- include a reproducible exact toy witness/figure.
