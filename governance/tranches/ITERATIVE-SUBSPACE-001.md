# Iterative Subspace Methods — Transaction Receipt

## Identity

- chapter: ATLAS-CH-KRYLOV-001
- implementation issue: #155
- implementation PR: #156
- implementation baseline: 574de4e65b42d4c090467b8a43fe2e534653b6e9
- implementation merge: 4fb9bbd05c3f48e3b69a72eaee171487576b5c48
- audit: AUDIT-039
- audit issue: #157
- audit branch: audit/a157

## Hard prerequisite

- ATLAS-CH-LINALG-001

Exact prerequisite identities at implementation baseline:

- manuscript: e7fcf56322f26d232d3a3043038d9850792b4bde
- AUDIT-004: 948f76b3f86d27fa4830efc30d8ef0135134256e
- source lock: f24e93ee0c2496ca0b9d71f6f824b0d13dbdc08e

## External sources

- Arnoldi (1951)
- Lanczos (1950)
- Saad (2003)

## Core artifact paths after AUDIT-039 repair

- manuscript/specifications/ATLAS-CH-KRYLOV-001.md
- manuscript/parts/02-mathematical-substrate/ATLAS-CH-KRYLOV-001.md
- mathematics/derivations/ATLAS-CH-KRYLOV-001-DERIVATIONS.md
- mathematics/computational-witnesses/ATLAS-CW-KRYLOV-001.md
- sources/source-locks/ATLAS-CH-KRYLOV-001.yaml

## Exact witness

For A=diag(1,2,4), b=(1,1,1)^T, x0=0 and trial basis V=[b,Ab]:

- reduced matrix: [[7,21],[21,73]]
- reduced right-hand side: [3,7]^T
- coefficient vector: [36/35,-1/5]^T
- approximate solution: [29/35,22/35,8/35]^T
- residual: [6,-9,3]^T/35
- Galerkin orthogonality: V^T r2=0
- squared Euclidean residual norm: 18/175

Conditioning control:

- Ac=diag(1,100,10000)
- one-step coefficient: 1/3367
- squared Euclidean residual grows from 3 to 19602/3367
- squared Ac-energy error decreases from 10101/10000 to 33980067/33670000

## Audit repair surface

AUDIT-039 canonicalizes the physical artifact placement and reader-facing identity after a connector-filter workaround. No mathematical reversal is required.
