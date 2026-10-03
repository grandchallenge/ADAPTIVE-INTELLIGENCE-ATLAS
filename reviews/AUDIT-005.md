# AUDIT-005 — Normalized and Quotient Representation Geometry

## Disposition

**PASS AFTER ONE RIGOR REPAIR**

The two REPRESENTATION-001 chapters remain at \`draft-v0.1\`.

The audit found no defect in the normalization geometry, exact ReLU symmetry examples, source boundaries, dependency state, or figure provenance.

One mathematical statement in the quotient chapter required tightening:

> a constant-loss path is not by itself sufficient to conclude that its tangent is a Hessian null vector.

The manuscript and derivation packet now state the stronger assumptions required for an actual Hessian null direction: a smooth exact one-parameter symmetry of the loss in a neighborhood, evaluated at a smooth critical point. An exact scaling-symmetry witness was added to the computational packet.

No publication, theorem-certification, or release promotion is implied.

## Audited baseline

- REPRESENTATION-001 merge: \`ba35ee233d1f586a5445a93f2d45eda159cecab5\`;
- audit issue: \`#26\`;
- chapters:
  - \`ATLAS-CH-NORMREP-001\`;
  - \`ATLAS-CH-QUOTIENT-001\`.

## 1. Normalized and Hyperspherical Representations

### Normalization differential

PASS.

For

\[
N(x)=\frac{x}{\|x\|_2},
\qquad
u=N(x),
\]

the chapter derives

\[
J_N(x)
=
\frac{1}{\|x\|_2}
\left(I-uu^\top\right).
\]

Independent Wolfram replay for

\[
x=(3,4)
\]

gives

\[
\|x\|_2=5,
\qquad
u=(3/5,4/5),
\]

and

\[
J_N(x)
=
\begin{pmatrix}
16/125&-12/125\\
-12/125&9/125
\end{pmatrix}.
\]

### Radial annihilation

PASS.

Independent replay gives

\[
J_N(x)x=(0,0).
\]

The manuscript correctly interprets this as first-order removal of radial motion by the normalization map.

It does not infer that radial information was semantically irrelevant.

### Tangent direction

PASS.

For

\[
t=(-4,3),
\]

we have

\[
x^\top t=0.
\]

Independent replay gives

\[
J_N(x)t=(-4/5,3/5).
\]

Thus the tangent direction is preserved up to the expected inverse-radius scaling.

### Chord-angle identity

PASS.

For unit vectors,

\[
\|u-v\|_2^2
=
2-2u^\top v
=
2-2\cos\theta.
\]

For

\[
a=(1,0),
\qquad
b=(1/2,\sqrt3/2),
\]

independent replay gives

\[
\theta=\pi/3,
\]

and

\[
\|a-b\|_2^2=1.
\]

### SLERP witness

PASS.

For the same pair, the exact halfway SLERP point is

\[
(\sqrt3/2,1/2),
\]

with unit norm.

The chapter retains the Geometry chapter's antipodal ambiguity and retraction-versus-exponential-map distinctions.

### Singularity at zero

PASS.

The manuscript explicitly records that

\[
N(x)=x/\|x\|_2
\]

is undefined at \(x=0\).

It does not silently identify ideal normalization with epsilon-regularized implementation.

### Radial-information counterexample

PASS.

The manuscript uses

\[
x_1=(1,0),
\qquad
x_2=(2,0),
\]

which satisfy

\[
N(x_1)=N(x_2).
\]

A target depending on original norm therefore cannot be reconstructed from the normalized representation alone.

This is a correct bounded demonstration that normalization declares positive radial scale invariant.

### Hyperspherical representation-learning source scope

PASS.

The source lock distinguishes:

- standard sphere/manifold geometry;
- Wang–Isola 2020 as peer-reviewed hyperspherical representation-learning evidence under its setting;
- nGPT 2024 as a research preprint;
- Training nGPT 2026 as a research preprint.

The chapter does not promote paper-specific empirical results into a universal claim that normalized Transformers are superior.

### Public GCL nGPT boundary

PASS.

A public GitHub repository search scoped to the \`grandchallenge\` organization and query \`nGPT\` returned no repository matches during this audit.

The exact GCL public object used by the chapter is instead:

- repository: \`grandchallenge/MODULUS\`;
- commit: \`9fc42eb5f29d5fff396f13e1a6c972af8fe64b35\`;
- path: \`modulus/optim/hyperball.py\`;
- Git blob: \`88b5e2b4c9abe760b8670f7fd2691fee25587b17\`.

The inspected file explicitly describes itself as implementing hyperspherical/hyperball dynamics and as designed for “nGPT / MODULUS-style training.”

The chapter correctly treats that as implementation-context evidence only.

It does not claim that GCL publishes a separate nGPT implementation.

### Figure identity

PASS.

\`ATLAS-FIG-NORMREP-001\`:

- generator blob:
  \`e6d05741ce7918d2ceb64f37bae92b3586c3a27e\`;
- rendered blob:
  \`691015fde4f682505dcb6afe6120638936118cc0\`;
- rendered bytes:
  \`61,355\`.

The manifest values match the audited Git tree.

The figure's literal semantics and nonliteral layout choices are separated correctly.

## 2. Equivalence and Quotient Geometry

### Equivalence relation and quotient

PASS.

The chapter defines:

- reflexive, symmetric, transitive equivalence;
- equivalence classes;
- quotient set;
- group orbit.

It does not assume every quotient set is automatically a smooth manifold.

### Grassmann quotient

PASS.

The chapter preserves the standard identification

\[
\operatorname{Gr}(n,p)
\cong
\operatorname{St}(n,p)/O(p),
\]

with the intended interpretation that orthogonal changes of frame preserve the represented subspace.

### Hidden-unit permutation symmetry

PASS.

For

\[
f(x)=W_2\sigma(W_1x),
\]

the transformation

\[
W_1'=PW_1,
\qquad
W_2'=W_2P^{-1}
\]

is derived using

\[
\sigma(Pz)=P\sigma(z)
\]

for elementwise activation.

The algebra is exact.

### Positive-rescaling symmetry

PASS.

For elementwise ReLU and positive diagonal \(D\),

\[
\operatorname{ReLU}(Dz)
=
D\operatorname{ReLU}(z).
\]

Therefore

\[
W_1'=DW_1,
\qquad
W_2'=W_2D^{-1}
\]

preserves the declared one-hidden-layer function.

The chapter keeps this symmetry scoped to the architectural/activation conditions under which the algebra holds.

### Exact two-unit witness

PASS.

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

Independent Wolfram replay gives identical outputs on the declared exact rational grid:

\[
\{0,0,0,0,0,11/2,11,33/2,22\}.
\]

The derivation packet, rather than the finite grid alone, establishes equality for every real input.

### Hessian null-direction audit finding

REPAIRED.

The original chapter stated that continuous exact symmetries can contribute Hessian-degenerate directions at a smooth critical point.

The statement was plausible but the derivation only established that one path had zero function/loss directional derivative.

A constant scalar path by itself does not establish

\[
Hv=0.
\]

The audit therefore strengthens the hypothesis.

Assume a smooth one-parameter group action

\[
g_s:\Theta\to\Theta
\]

is an exact loss symmetry in a neighborhood:

\[
L(g_s\theta)=L(\theta).
\]

If

\[
\nabla L(\theta_\star)=0,
\]

then symmetry maps \(\theta_\star\) to other critical points.

For

\[
v=
\frac{d}{ds}g_s\theta_\star
\Big|_{s=0},
\]

differentiating the zero-gradient identity gives

\[
\boxed{
H_L(\theta_\star)v=0.
}
\]

This is now the statement in the manuscript and derivation packet.

### Exact Hessian scaling witness

PASS.

For

\[
L(a,b)
=
\frac12(ab-y)^2,
\]

the positive rescaling

\[
(a,b)\mapsto(a/c,cb)
\]

preserves the model product.

On the critical manifold

\[
y=ab,
\]

Wolfram gives

\[
H=
\begin{pmatrix}
b^2&ab\\
ab&a^2
\end{pmatrix}.
\]

For scaling-orbit tangent

\[
v=(-a,b),
\]

independent symbolic replay gives

\[
Hv=(0,0).
\]

This exact witness was added to the computational packet.

### Hidden symmetries

PASS.

Grigsby, Lindsey and Rolnick are used to support the bounded claim that ReLU-network symmetry structure can include permutation, positive scaling and additional hidden symmetries.

The chapter does not infer that permutation and scaling generate the entire functional-equivalence relation.

### Learning consequences of symmetry

PASS.

Ziyin 2024 is used only to support the bounded statement that declared symmetries can affect learning structure under the paper's assumptions.

The chapter does not claim one universal quotient geometry determines all training dynamics.

### Regular versus singular quotient

PASS.

The chapter explicitly records:

- fixed points;
- changing stabilizers;
- hidden symmetries;
- singular orbit types.

It refuses to refer unqualifiedly to one globally smooth “neural-network quotient manifold.”

### Quotienting versus optimization simplicity

PASS.

The chapter states

\[
\text{symmetry removed}
\not\Rightarrow
\text{convex landscape}.
\]

It lists possible remaining:

- distinct minima;
- saddles;
- barriers;
- poor conditioning;
- singular regions.

The proposition that quotienting may expose a constructive class of benign nonconvexity remains an Atlas/GCL open research question.

### Figure identity

PASS.

\`ATLAS-FIG-QUOTIENT-001\`:

- generator blob:
  \`39d00b3e601cb4490e0c8c0755b5f4a8bcf63ef1\`;
- rendered blob:
  \`0fd0154aca1a70a622c43f726fd31532a2092341\`;
- rendered bytes:
  \`39,297\`.

The manifest values match the audited Git tree.

The figure is correctly classed schematic because representative placement and arrows do not encode parameter-space geometry, even though the displayed parameter/function identities are exact.

## 3. Citation and provenance closure

PASS.

The bibliography contains:

- \`LoshchilovEtAl2024nGPT\`;
- \`LoshchilovGinsburg2026TrainingNGPT\`;
- \`WangIsola2020Hypersphere\`;
- \`GrigsbyLindseyRolnick2023\`;
- \`Ziyin2024Symmetry\`.

Both manuscripts contain the canonical reader-facing source-lock and reference markers.

All rendered-figure Git blob and byte identities are now enforced by the repository validator inherited from AUDIT-004.

## 4. Dependency and promotion state

PASS.

Both chapters remain:

\`draft-v0.1\`.

Their hard prerequisites are:

- \`ATLAS-CH-GEOM-001\`;
- \`ATLAS-CH-REP-001\`.

Both prerequisites are already audited drafts.

\`ATLAS-CH-RESIDUAL-001\` remains at architecture state until this audit merges.

## 5. Final disposition

AUDIT-005 passes after one rigor repair.

The Representation branch now supports the next conceptual step:

\[
\text{representation}
\to
\text{normalized geometry}
\to
\text{quotient equivalence}
\to
\text{Residual}.
\]

The next tranche may instantiate \`ATLAS-CH-RESIDUAL-001\`, but should treat the Residual as an open reconstruction/minimal-transfer programme rather than as a discovered invariant.
