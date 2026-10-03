# Chapter Specification — ATLAS-CH-NORMREP-001

## Identity

**Title:** Normalized and Hyperspherical Representations  
**Part:** Representation Learning  
**Status:** specification-ready.

## Chapter contract

Develop the consequences of deliberately removing radial degrees of freedom from a representation and placing state on the unit hypersphere.

The chapter must distinguish:

- normalization as a map;
- sphere geometry as the resulting admissible state space;
- angular similarity as one downstream choice;
- architectural normalization as a modeling decision;
- empirical claims about normalized networks as source-scoped evidence.

## Dependency contract

Hard prerequisites:

- \`ATLAS-CH-GEOM-001\`;
- \`ATLAS-CH-REP-001\`.

May assume:

- sphere tangent spaces;
- retractions;
- SLERP;
- representation invariance/equivariance language.

Must not assume:

- quotient geometry;
- manifold optimization beyond the sphere operations already developed;
- nGPT as an established universal architecture.

## Reader outcome

A reader should be able to:

1. derive the normalization map and its differential;
2. separate radial and tangential perturbations;
3. relate cosine similarity, angle, and Euclidean chord distance on unit vectors;
4. explain what information normalization removes;
5. derive a normalized tangent update/retraction;
6. understand SLERP as great-circle interpolation;
7. distinguish hyperspherical representation geometry from claims about model quality;
8. state what the cited nGPT papers actually claim;
9. understand the bounded public GCL connection without inferring a public GCL nGPT implementation.

## Formal spine

For \(x\neq0\), define

\[
N(x)=\frac{x}{\|x\|_2}.
\]

Let

\[
u=N(x).
\]

Derive

\[
J_N(x)
=
\frac{1}{\|x\|_2}
\left(I-uu^\top\right).
\]

Use the radial/tangential decomposition

\[
\delta
=
(uu^\top)\delta
+
(I-uu^\top)\delta.
\]

For unit \(u,v\),

\[
\|u-v\|_2^2
=
2-2u^\top v
=
2-2\cos\theta.
\]

Reintroduce the sphere retraction

\[
R_u(\xi)
=
\frac{u+\xi}{\|u+\xi\|_2},
\qquad
u^\top\xi=0,
\]

and SLERP from the Geometry chapter without duplicating its full derivation.

## Principal pedagogical device

### Allegory: direction without volume

A normalized vector is like an arrow whose direction remains but whose length has been deliberately erased.

Structural correspondence:

- direction ↔ angular information;
- length ↔ radial information;
- tangent step ↔ change of direction;
- renormalization ↔ return to the sphere.

Limit:

Radial information is not “noise” by definition. A task can depend essentially on norm.

## Exact witness

Use \(x=(3,4)\):

\[
u=(3/5,4/5),
\]

\[
J_N(x)
=
\begin{pmatrix}
16/125&-12/125\\
-12/125&9/125
\end{pmatrix}.
\]

Verify:

\[
J_N(x)x=0,
\]

and for tangent direction \((-4,3)\),

\[
J_N(x)(-4,3)^\top
=
(-4/5,3/5)^\top.
\]

Use a 60-degree unit-vector pair to compare:

- angular distance;
- chord distance;
- midpoint by SLERP.

## Figure programme

### ATLAS-FIG-NORMREP-001

Two panels:

1. radial versus tangential perturbations at \(x=(3,4)\), showing normalization removes first-order radial motion;
2. unit-circle chord versus geodesic arc for two vectors separated by 60 degrees, with SLERP midpoint.

Representation class: exact.

## Empirical/source programme

Use:

- Wang–Isola for one peer-reviewed hyperspherical representation-learning setting;
- nGPT 2024 and Training nGPT 2026 as research-preprint architecture/training evidence;
- the public GCL MODULUS \`hyperball.py\` only as bounded implementation-context evidence.

## Failure boundaries

Include:

- two states with same direction but different norms becoming identical after normalization;
- normalization singularity at \(x=0\);
- cosine similarity discarding norm by construction;
- a task where radius encodes confidence or magnitude;
- empirical nGPT results not generalized beyond the cited experiments.

## Downstream obligations

Supply normalized-geometry language to:

- later nGPT/RUNT discussion;
- normalized attention and optimizer chapters;
- positional geometry;
- residual/transfer questions where radial gauge removal matters.

## Sources

- [@Lee2018Riemannian]
- [@AbsilMahonySepulchre2008]
- [@WangIsola2020Hypersphere]
- [@LoshchilovEtAl2024nGPT]
- [@LoshchilovGinsburg2026TrainingNGPT]

Source lock: \`sources/source-locks/ATLAS-CH-NORMREP-001.yaml\`.

## Acceptance

The draft must:

- derive the normalization Jacobian exactly;
- distinguish angular from radial information;
- include one explicit radial-information-loss counterexample;
- preserve source scope for nGPT;
- keep the public GCL connection narrower than the paper evidence;
- include a reproducible exact figure/witness.
