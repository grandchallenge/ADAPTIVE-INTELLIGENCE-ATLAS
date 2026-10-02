# Keystone Specification — ATLAS-CH-GEOM-001

## Identity

**Title:** Geometry of Constrained State Spaces  
**Part:** Mathematical Substrate  
**Status:** specification-ready  
**Keystone role:** establish the geometric language consumed throughout the Atlas.

## Chapter contract

The chapter must teach the reader to distinguish an ambient coordinate space from the admissible state space embedded in it. It must develop manifolds, tangent spaces, metrics, geodesics, exponential maps, retractions, spheres, Stiefel manifolds, and Grassmannians only to the degree required by later Atlas arguments.

The chapter is not a compressed course in differential geometry. Its task is narrower:

> make “legal motion in a constrained representation space” mathematically precise.

## Dependency contract

Immediate hard prerequisite:

- `ATLAS-CH-LINALG-001` — formal.

Inherited prerequisite cone:

- `ATLAS-CH-OBJECTS-001`;
- `ATLAS-CH-THESIS-001`.

The chapter may therefore assume vectors, linear maps, inner products, orthogonality, projections, SVD, and operator norms. It may not assume prior manifold optimization, information geometry, normalized neural architectures, or quotient geometry.

## Reader outcome

After the chapter, a reader should be able to:

1. identify the state space and ambient space in a constrained learning problem;
2. compute or characterize a tangent space in canonical examples;
3. explain why an unconstrained Euclidean step may leave the admissible state space;
4. distinguish exponential maps from practical retractions;
5. derive great-circle geodesics and SLERP on a sphere;
6. describe Stiefel and Grassmann geometry at an operational level;
7. recognize when two coordinate descriptions may represent the same geometric object;
8. understand exactly what later Atlas chapters mean by “geometry-preserving update.”

## Formal spine

### Definitions

The chapter should introduce stable Atlas definitions for:

- smooth embedded manifold;
- tangent vector and tangent space;
- Riemannian metric;
- geodesic;
- exponential map;
- retraction;
- sphere (S^{d-1});
- Stiefel manifold (mathrm{St}(n,p));
- Grassmann manifold (mathrm{Gr}(n,p));
- geodesic distance;
- orthogonal projection to a tangent space.

### Core results to establish or source-lock

At minimum:

1. tangent space of the unit sphere:
   [
   T_xS^{d-1}={v:x^	op v=0};
   ]

2. normalized first-order retraction on the sphere:
   [
   R_x(v)=rac{x+v}{|x+v|};
   ]

3. great-circle interpolation / SLERP and its domain restrictions;

4. tangent characterization for the Stiefel manifold:
   [
   T_Xmathrm{St}(n,p)={Z:X^	op Z+Z^	op X=0};
   ]

5. the distinction between the Stiefel object “ordered orthonormal frame” and the Grassmann object “subspace independent of basis.”

The chapter should not state a general theorem unless its hypotheses are explicit and sourced or proved.

## Principal intuition device

### Allegory: the cartographer and the mountain

A Euclidean optimizer behaves like a traveler who owns a flat map of a mountain and is allowed to walk through the paper. A constrained optimizer must walk on the mountain.

Structural correspondence:

- map coordinates ↔ ambient coordinates;
- mountain surface ↔ admissible manifold;
- locally flat patch ↔ tangent space;
- shortest route on the surface ↔ geodesic;
- “step then return to the surface” ↔ retraction.

Limit of allegory:

A mathematical manifold need not be physically embedded as a visible surface, and a retraction is not literally a physical projection. The image teaches admissible versus ambient motion, not the full intrinsic theory.

## Working examples

The progression should be:

1. circle (S^1);
2. sphere (S^2);
3. hypersphere (S^{d-1});
4. orthonormal two-frame in (mathbb{R}^3);
5. subspace equivalence leading to the Grassmannian.

The reader should see the same ideas repeated with increasing abstraction.

## Figure programme

### ATLAS-FIG-MANIFOLD-001 — Tangent update, exponential map, and retraction

Primary class: `schematic`.

Required visible elements:

- point (x) on a manifold;
- tangent space (T_xM);
- tangent vector (v);
- exponential-map destination;
- retraction destination;
- ambient straight step shown separately.

The plate should make one fact memorable: the tangent vector lives in a linear space, but its update is interpreted through the manifold.

### Proposed computational figure — sphere geodesic family

A Wolfram-rendered exact/data-derived figure should compare linear interpolation followed by normalization against SLERP for several angular separations.

Claim boundary: the figure illustrates geometry on a sphere; it does not establish that a particular neural representation is empirically spherical.

## Computational witnesses

1. symbolic verification that a projected vector is tangent to the sphere;
2. numerical comparison of Euclidean interpolation, normalization, and SLERP;
3. finite-dimensional Stiefel tangent-condition check;
4. geodesic-distance versus chord-distance plot.

Each witness must preserve exact equations, parameter values, precision, and rendering source.

## Counterexamples and failure boundaries

The chapter should include:

- antipodal ambiguity in SLERP;
- a naive Euclidean update that violates a unit-norm constraint;
- a retraction that is locally valid without being the exponential map;
- the distinction between local Euclidean approximation and global flatness.

These are essential because later chapters will rely on geometry without re-explaining these caveats.

## Downstream obligations

The chapter must provide stable notation and definitions consumed by:

- `ATLAS-CH-REP-001`;
- `ATLAS-CH-NORMREP-001`;
- `ATLAS-CH-QUOTIENT-001`;
- `ATLAS-CH-POSGEOM-001`;
- `ATLAS-CH-SECOND-001`;
- `ATLAS-CH-MANOPT-001`;
- `ATLAS-CH-TRANSPORT-001`;
- later frontier synthesis.

The chapter should therefore avoid notation that conflicts with later optimization notation.

## Source-lock plan

Before manuscript drafting reaches review-ready state, source-lock:

- one standard differential-geometry reference;
- one manifold-optimization reference;
- one canonical spherical-geometry/SLERP source where historically appropriate;
- primary sources for Stiefel/Grassmann optimization if a specific algorithm is discussed.

GCL programme material may motivate examples but cannot substitute for mathematical references.

## Acceptance criteria

The specification is discharged when the drafted chapter has:

- explicit ambient/admissible distinction;
- stable definitions;
- at least one proved or fully derived sphere example;
- one Stiefel example;
- one Grassmann equivalence example;
- the allegory with an explicit limit;
- registered computational witnesses;
- figure manifests with literal/nonliteral semantics;
- no hidden use of later manifold-optimization machinery.
