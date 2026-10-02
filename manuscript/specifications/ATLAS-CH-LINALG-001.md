# Chapter Specification — ATLAS-CH-LINALG-001

## Identity

**Title:** Linear Maps and Decompositions  
**Part:** Mathematical Substrate  
**Status:** specification-ready.

## Chapter contract

Develop exactly the finite-dimensional linear-algebra substrate later Atlas chapters consume.

This is not a generic linear-algebra textbook chapter.

## Dependency contract

Hard prerequisite:

- `ATLAS-CH-OBJECTS-001`.

May assume basic algebra and Euclidean vectors.

## Reader outcome

A reader should be able to:

1. interpret a matrix as a representation of a linear map;
2. distinguish basis-dependent coordinates from the underlying transformation;
3. work with subspaces, orthogonal projections, rank, null spaces, and pseudoinverses;
4. derive and interpret the SVD;
5. distinguish eigendecomposition from SVD;
6. compute operator (2)-norms and condition numbers;
7. understand low-rank approximation;
8. recognize block/Kronecker structure when later chapters use it.

## Formal spine

Cover:

- linear maps and bases;
- range/null spaces;
- orthogonal projection;
- eigenvalues/eigenvectors;
- normal matrices as a handoff concept;
- singular-value decomposition;
- Moore–Penrose pseudoinverse;
- induced (2)-norm;
- condition number;
- Eckart–Young low-rank approximation statement;
- block matrices and Kronecker products only to the degree later chapters need.

## Principal pedagogical device

### Allegory: changing lenses versus changing the machine

Changing basis changes coordinates used to describe the same linear map. Changing the operator changes the transformation.

Limit:

Not every useful neural transformation is linear, diagonalizable, or well described by one fixed basis.

## Exact derivations

At minimum:

[
A=USigma V^\top,
qquad
|A|_2=sigma_{max}(A),
]

orthogonal projection

[
P=QQ^\top
]

for orthonormal columns of (Q), and the least-squares pseudoinverse relation.

Use a small exact matrix where SVD and eigendecomposition visibly answer different questions.

## Computational witness

Wolfram exact/numerical replay of:

- SVD;
- projection idempotence;
- pseudoinverse least-squares solution;
- rank-(k) approximation error;
- condition-number amplification.

## Failure boundaries

Include:

- defective/non-normal matrix where eigenvectors are a poor explanatory basis;
- near-singular system with large condition number;
- low-rank approximation preserving Frobenius/2-norm structure but not arbitrary semantics.

## Downstream obligations

Immediate or important consumers:

- `ATLAS-CH-GEOM-001`;
- `ATLAS-CH-NONNORMAL-001`;
- optimization and numerical-analysis families.

## Sources

- [@TrefethenBau1997]
- [@HornJohnson2012]
- [@GolubVanLoan2013]

Source lock: `sources/source-locks/ATLAS-CH-LINALG-001.yaml`.

## Acceptance

The chapter must be selective, derivational, and operator-centered; it must not become a survey of every matrix decomposition.
