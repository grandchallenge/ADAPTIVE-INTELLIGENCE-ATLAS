# Keystone Specification — ATLAS-CH-GEOM-001

## Identity

**Title:** Geometry of Constrained State Spaces  
**Part:** Mathematical Substrate  
**Status:** specification-ready  
**Keystone role:** establish the geometric language consumed throughout the Atlas.

## Chapter contract

The chapter must teach the reader to distinguish an ambient coordinate space from the admissible state space embedded in it. It develops manifolds, tangent spaces, metrics, geodesics, exponential maps, retractions, spheres, Stiefel manifolds, and Grassmannians only to the degree required by later Atlas arguments.

Its governing question is:

> What does it mean for a representation update to move legally inside a constrained state space?

The chapter is not a compressed differential-geometry textbook.

## Dependency contract

Immediate hard prerequisite:

- \`ATLAS-CH-LINALG-001\` — formal.

Inherited foundation:

- \`ATLAS-CH-OBJECTS-001\`;
- \`ATLAS-CH-THESIS-001\`.

The chapter may assume vectors, linear maps, inner products, orthogonality, projections, SVD, and operator norms. It may not assume manifold optimization, normalized neural architectures, quotient geometry, or information geometry.

## Reader outcome

After the chapter, a reader should be able to:

1. distinguish ambient and admissible state spaces;
2. compute canonical tangent spaces;
3. explain why Euclidean steps can violate constraints;
4. distinguish exponential maps from retractions;
5. derive great-circle interpolation and SLERP on a sphere;
6. state the Stiefel tangent condition;
7. distinguish Stiefel frames from Grassmann subspaces;
8. understand later uses of “geometry-preserving update.”

## Formal spine

Introduce stable Atlas definitions for:

- smooth embedded manifold;
- tangent vector and tangent space;
- Riemannian metric;
- geodesic;
- exponential map;
- retraction;
- sphere \(S^{d-1}\);
- Stiefel manifold \(\operatorname{St}(n,p)\);
- Grassmann manifold \(\operatorname{Gr}(n,p)\);
- geodesic distance;
- tangent projection.

Core results include:

\[
T_xS^{d-1}
=
\{v\in\mathbb R^d:x^\top v=0\},
\]

the normalized sphere retraction

\[
R_x(v)
=
\frac{x+v}{\|x+v\|},
\]

SLERP on non-antipodal unit vectors, and

\[
T_X\operatorname{St}(n,p)
=
\{Z:X^\top Z+Z^\top X=0\}.
\]

The chapter must also explain that \(\operatorname{St}(n,p)\) represents ordered orthonormal frames whereas \(\operatorname{Gr}(n,p)\) represents subspaces independent of basis.

## Principal intuition device

### Allegory: the cartographer and the mountain

A Euclidean optimizer behaves like a traveler who owns a flat map of a mountain and is allowed to walk through the paper. A constrained optimizer must walk on the mountain.

Structural correspondence:

- map coordinates ↔ ambient coordinates;
- mountain surface ↔ admissible manifold;
- locally flat patch ↔ tangent space;
- shortest surface route ↔ geodesic;
- step then return to the surface ↔ retraction.

Limit of allegory:

A mathematical manifold need not be visibly embedded in three dimensions, and a retraction is not literally a physical projection. The allegory teaches admissible versus ambient motion, not the full intrinsic theory.

## Working examples

Progress through:

1. \(S^1\);
2. \(S^2\);
3. \(S^{d-1}\);
4. an orthonormal two-frame in \(\mathbb R^3\);
5. equivalence of frames representing one subspace.

## Figure programme

### ATLAS-FIG-MANIFOLD-001

Show:

- a point \(x\) on the sphere;
- the tangent space \(T_xM\);
- tangent vector \(v\);
- exponential-map endpoint;
- normalized-retraction endpoint;
- ambient straight step separately.

A second computational comparison may show normalized linear interpolation against SLERP over several angular separations.

## Computational witnesses

1. symbolic tangent projection on the sphere;
2. numerical comparison of Euclidean interpolation, normalization, and SLERP;
3. Stiefel tangent-condition check;
4. chord distance versus geodesic distance.

## Counterexamples and failure boundaries

Include:

- antipodal ambiguity in SLERP;
- a Euclidean step violating unit norm;
- a retraction that is not the exponential map;
- local Euclidean approximation without global flatness.

## Downstream obligations

Supply stable geometry and notation to:

- \`ATLAS-CH-REP-001\`;
- \`ATLAS-CH-NORMREP-001\`;
- \`ATLAS-CH-QUOTIENT-001\`;
- \`ATLAS-CH-POSGEOM-001\`;
- \`ATLAS-CH-SECOND-001\`;
- \`ATLAS-CH-MANOPT-001\`;
- \`ATLAS-CH-TRANSPORT-001\`.

## Source-lock plan

Source-lock:

- a standard Riemannian-geometry reference;
- a matrix-manifold optimization reference;
- a canonical Stiefel/Grassmann source;
- the historical SLERP source where used.

## Acceptance criteria

The draft must have:

- explicit ambient/admissible distinction;
- stable definitions;
- a complete sphere tangent/retraction derivation;
- a Stiefel derivation;
- a Grassmann quotient explanation;
- the allegory with its explicit limit;
- reproducible figure/witness provenance;
- no hidden use of later optimization machinery.
