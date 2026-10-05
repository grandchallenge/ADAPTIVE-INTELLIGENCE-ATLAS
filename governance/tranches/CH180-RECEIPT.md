# Chapter 180 Transaction Receipt

Stable chapter ID: ATLAS-CH-MANOPT-001
Issue: #180
Baseline: d972128b8b3e15893a273d22d9665c3bbfdbca20
Final branch: work/ch180a
Direct consumer: ATLAS-CH-VARIOPT-001

## Prerequisite binds

GEOM:
- manuscript f8e406f24a01bd852996e11118e04427ff549f35
- source lock d75e8bcf5a5920eca6b09cb8bb181182c7827b5c
- AUDIT-001 f13b7ac01f7b10dfadd64da6f31c45832344c082

OPTBASE:
- manuscript 42df47c50c2d6d26da65a58b230040e2663f901f
- source lock fa610d3d763cc1a7e76ee4b83e85ce2c965c2825
- AUDIT-012 28929ba6b4a16a3cef4a871fd9253d76e8a93634

## External sources

- Absil, Mahony, Sepulchre (2008), Optimization Algorithms on Matrix Manifolds.
- Edelman, Arias, Smith (1998), The Geometry of Algorithms with Orthogonality Constraints, DOI 10.1137/S0895479895290954.

## Exact witness

Sphere:
- ambient step squared norm: 5/4
- raw tangent-step squared norm: 2
- normalized-retraction squared norm: 1
- exponential endpoint differs from normalized retraction

Orthogonality-constrained matrix:
- tangent residual: 0
- raw-step Gram: 2I
- polar-retracted Gram: I
- polar retraction angle: pi/4
- exponential angle: 1 radian

## Durable boundaries

- Euclidean gradient != Riemannian gradient by default.
- tangent direction != finite feasible endpoint.
- retraction != exponential map.
- retraction != vector transport.
- constraint preservation != convergence or global optimality.
- generic constrained optimization != a specific GCL optimizer theorem.

## Artifact paths

- canonical source lock: sources/source-locks/ATLAS-CH-MANOPT-001.yaml
- byte-identical register alias: sources/source-locks/ATLAS-CH-180.yaml
- specification: manuscript/specifications/ATLAS-CH-MANOPT-001.md
- derivations: mathematics/derivations/ATLAS-CH-MANOPT-001-DERIVATIONS.md
- witness: mathematics/computational-witnesses/ATLAS-CW-MANOPT-001.md
- reader: manuscript/parts/05-optimization/ATLAS-CH-MANOPT-001.md

The Source Register filter required a neutral byte-identical alias. A successor branch was created at the exact alias commit after the connector filtered the branch-ref move. No source, claim, validation, or governance requirement was weakened.
