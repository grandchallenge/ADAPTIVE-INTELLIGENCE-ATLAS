# REPRESENTATION-001 — Normalized and Quotient Geometry

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- AUDIT-004 merge: \`b2a59985122fbc701d2699473fe843f06320a56c\`;
- issue: \`#24\`;
- both hard prerequisites already audited at \`draft-v0.1\`:
  - \`ATLAS-CH-GEOM-001\`;
  - \`ATLAS-CH-REP-001\`.

## Objective

Draft the first post-Foundation representation-geometry pair:

1. \`ATLAS-CH-NORMREP-001\` — Normalized and Hyperspherical Representations;
2. \`ATLAS-CH-QUOTIENT-001\` — Equivalence and Quotient Geometry.

\`ATLAS-CH-RESIDUAL-001\` remains blocked until Quotient passes post-draft audit.

## A. Normalized and Hyperspherical Representations

### Formal core

The normalization map

\[
N(x)=\frac{x}{\|x\|_2}
\]

has differential

\[
J_N(x)
=
\frac{1}{\|x\|_2}
(I-uu^\top),
\qquad
u=N(x).
\]

This explicitly separates radial and tangential perturbations.

For

\[
x=(3,4),
\]

the exact witness gives

\[
u=(3/5,4/5),
\]

\[
J_N(x)
=
\begin{pmatrix}
16/125&-12/125\\
-12/125&9/125
\end{pmatrix},
\]

\[
J_N(x)x=0,
\]

and for tangent

\[
t=(-4,3),
\]

\[
J_N(x)t=(-4/5,3/5).
\]

### Spherical witness

For

\[
a=(1,0),
\qquad
b=(1/2,\sqrt3/2),
\]

the exact angle is

\[
\pi/3,
\]

the chord length is \(1\), and the SLERP midpoint is

\[
(\sqrt3/2,1/2).
\]

### Radial-information counterexample

\[
(1,0)
\quad\text{and}\quad
(2,0)
\]

normalize to the same unit vector.

A task requiring the original norm cannot recover it from the normalized representation alone.

### External evidence

The source lock separates:

- standard sphere/manifold geometry;
- Wang–Isola 2020 peer-reviewed hyperspherical contrastive-representation evidence;
- nGPT 2024 and Training nGPT 2026 research-preprint evidence.

The nGPT paper claims remain paper-scoped.

### Public GCL boundary

A search of public \`grandchallenge\` repositories found no separate public nGPT repository.

The exact public GCL object used by this chapter is:

- repository: \`grandchallenge/MODULUS\`;
- commit: \`9fc42eb5f29d5fff396f13e1a6c972af8fe64b35\`;
- path: \`modulus/optim/hyperball.py\`;
- Git blob: \`88b5e2b4c9abe760b8670f7fd2691fee25587b17\`.

Its module documentation states that it implements hyperspherical/hyperball dynamics and is designed for "nGPT / MODULUS-style training."

The chapter uses that only as bounded implementation-context evidence.

It does not infer that GCL publishes a complete nGPT implementation.

### Figure

\`ATLAS-FIG-NORMREP-001\`

- generator blob: \`e6d05741ce7918d2ceb64f37bae92b3586c3a27e\`;
- rendered blob: \`691015fde4f682505dcb6afe6120638936118cc0\`;
- rendered bytes: 61,355;
- representation class: exact.

## B. Equivalence and Quotient Geometry

### Formal core

The chapter develops:

- equivalence relations;
- equivalence classes;
- group orbits;
- quotient sets/manifolds under appropriate regularity;
- Grassmann as the canonical quotient example.

It preserves

\[
\operatorname{Gr}(n,p)
\cong
\operatorname{St}(n,p)/O(p).
\]

### Exact hidden-unit permutation symmetry

For

\[
f(x)=W_2\sigma(W_1x),
\]

and permutation matrix \(P\),

\[
W_1'=PW_1,
\qquad
W_2'=W_2P^{-1}
\]

leaves the function unchanged because

\[
\sigma(Pz)=P\sigma(z)
\]

for elementwise activation.

### Exact positive-rescaling symmetry

For ReLU and positive diagonal \(D\),

\[
W_1'=DW_1,
\qquad
W_2'=W_2D^{-1}
\]

leaves the function unchanged because

\[
\operatorname{ReLU}(Dz)
=
D\operatorname{ReLU}(z).
\]

### Two-unit witness

Original:

\[
W_1=(1,2)^\top,
\qquad
W_2=(3,4).
\]

Permutation representative:

\[
W_1'=(2,1)^\top,
\qquad
W_2'=(4,3).
\]

Positive-rescaling representative:

\[
W_1''=(2,2/3)^\top,
\qquad
W_2''=(3/2,12).
\]

All three compute

\[
f(x)=11\max(0,x).
\]

The Wolfram witness verifies exact agreement on a finite rational grid, while the derivation proves equality for every real input.

### Symmetry scope

Peer-reviewed sources support:

- permutation/positive-scaling and hidden symmetries in ReLU networks;
- learning consequences of declared symmetries under source-specific assumptions.

The chapter explicitly denies:

\[
\text{quotienting redundancy}
\Rightarrow
\text{convex or globally easy optimization}.
\]

### Open research question

The stronger programme remains:

> What portion of neural nonconvexity is benign redundancy induced by symmetries or representational equivalence, and what portion remains intrinsic after quotienting?

This is Atlas/GCL research framing, not an established theorem.

### Figure

\`ATLAS-FIG-QUOTIENT-001\`

- generator blob: \`39d00b3e601cb4490e0c8c0755b5f4a8bcf63ef1\`;
- rendered blob: \`0fd0154aca1a70a622c43f726fd31532a2092341\`;
- rendered bytes: 39,297;
- representation class: schematic with exact parameter/function annotations.

## C. Source and bibliography state

New bibliography entries:

- Loshchilov et al. 2024 nGPT;
- Loshchilov and Ginsburg 2026 Training nGPT;
- Wang and Isola 2020;
- Grigsby, Lindsey and Rolnick 2023;
- Ziyin 2024.

New source locks:

- \`sources/source-locks/ATLAS-CH-NORMREP-001.yaml\`;
- \`sources/source-locks/ATLAS-CH-QUOTIENT-001.yaml\`.

## D. Durable chapter objects

For each chapter, the branch contains:

- specification;
- source lock;
- derivation packet;
- computational witness;
- complete manuscript;
- Wolfram generator;
- rendered figure;
- figure manifest;
- figure-register entry;
- ledger promotion to \`draft-v0.1\`.

## E. Frozen distinctions

The tranche preserves:

\[
\text{unit norm}
\neq
\text{information preservation}.
\]

\[
\text{angular geometry}
\neq
\text{proof that radius was irrelevant}.
\]

\[
\text{public GCL nGPT-style optimizer context}
\neq
\text{public GCL nGPT implementation}.
\]

\[
\text{parameter difference}
\neq
\text{functional difference}.
\]

\[
\text{symmetry reduction}
\neq
\text{global landscape simplification}.
\]

\[
\text{regular quotient geometry}
\neq
\text{generic global neural parameter geometry}.
\]

## F. Next step

After merge, run a bounded post-draft audit over both chapters.

Do not begin \`ATLAS-CH-RESIDUAL-001\` until the quotient chapter's exact symmetry claims, source scope, figure identities, and open-problem boundary pass that audit.
