# AUDIT-039 — Iterative Subspace Methods

## Disposition

**PASS AFTER EDITORIAL/PROVENANCE CANONICALIZATION**

ATLAS-CH-KRYLOV-001 remains at draft-v0.1.

The implementation correctly defines operator-generated Krylov spaces, distinguishes Arnoldi from the symmetric/Hermitian Lanczos specialization, separates Galerkin from minimum-residual projection, preserves the residual/error boundary, treats preconditioning as a change of effective operator, and states finite-precision orthogonality/restart limitations.

AUDIT-039 found no mathematical reversal.

It found one repository/editorial defect caused by a recoverable connector filter during implementation: the mature chapter artifacts had been temporarily stored under neutral governance/tranches/a155-* paths rather than the standard manuscript/mathematics directories, and the reader title/source-lock reference had been neutralized.

The audit repaired that indirection by canonicalizing the physical artifact paths, restoring the reader-facing chapter title and exact source-lock path, deleting temporary duplicate copies, adding a transaction receipt, and restoring issue metadata.

## Audited baseline

- implementation issue: #155
- implementation PR: #156
- implementation merge: 4fb9bbd05c3f48e3b69a72eaee171487576b5c48
- audit issue: #157
- audit branch: audit/a157
- chapter: ATLAS-CH-KRYLOV-001

Implementation artifact blobs before audit repair:

- specification: da7743004f71730dfe6e10ef4b442c46c8d7f6dc
- derivation packet: d3bb554e71584568a2382e456a3aaa97fd1b59e3
- computational witness: c8fcb7d719fcf452813727e91d27bc2c48a19a20
- reader manuscript: 1172ec907e09e44276eb2916dfafb77fb457229b
- source lock: adbe97c750ed79d09462a5e867e5beb772ad72e2
- Chapter Ledger: 5742d9e7f4dfa00d09a6e6de7ed6864018cc7269
- bibliography: dcc85674b2aa01081d0c0f950b2c75184512e095

Repaired audit-head identities before this audit record:

- specification: da7743004f71730dfe6e10ef4b442c46c8d7f6dc
- derivation packet: d3bb554e71584568a2382e456a3aaa97fd1b59e3
- computational witness: c8fcb7d719fcf452813727e91d27bc2c48a19a20
- reader manuscript: 59e169723ca068bef817e7bc9e28727d03b45f6a
- source lock: adbe97c750ed79d09462a5e867e5beb772ad72e2
- Chapter Ledger: 2824cbac88b236ad81e09108f4551d604ff73172
- Source Register: 20c459624900f0f24c319a2ceff4490a7e380dc2
- bibliography: dcc85674b2aa01081d0c0f950b2c75184512e095
- transaction receipt: 573d845668509e44b88fd05dc82cdef3e12b8a11

## 1. Hard prerequisite

PASS.

The chapter binds the audited LINALG prerequisite at protected baseline 574de4e65b42d4c090467b8a43fe2e534653b6e9:

- manuscript: e7fcf56322f26d232d3a3043038d9850792b4bde
- AUDIT-004: 948f76b3f86d27fa4830efc30d8ef0135134256e
- source lock: f24e93ee0c2496ca0b9d71f6f824b0d13dbdc08e

## 2. External source identity

PASS.

Primary/public source verification confirms:

- Walter Edwin Arnoldi, The Principle of Minimized Iterations in the Solution of the Matrix Eigenvalue Problem, Quarterly of Applied Mathematics 9 (1951), 17–29.
- Cornelius Lanczos, An Iteration Method for the Solution of the Eigenvalue Problem of Linear Differential and Integral Operators, Journal of Research of the National Bureau of Standards 45 (1950), beginning p. 255, DOI 10.6028/jres.045.026.
- Yousef Saad, Iterative Methods for Sparse Linear Systems, second edition, SIAM, 2003, print ISBN 978-0-89871-534-7, DOI 10.1137/1.9780898718003.

No source-scope strengthening is required.

## 3. Krylov-space definition

PASS.

The chapter uses the standard operator-generated space K_m(A,r0)=span{r0,Ar0,...,A^(m-1)r0} and explicitly distinguishes it from an arbitrary subspace of the same dimension.

## 4. Arnoldi and Lanczos

PASS.

The chapter states the exact-arithmetic Arnoldi relation A V_m = V_(m+1) Hbar_m with an orthonormal basis and upper-Hessenberg reduced matrix.

For symmetric/Hermitian operators it correctly explains that the projected matrix is symmetric and Hessenberg, hence tridiagonal, yielding the exact-arithmetic Lanczos three-term recurrence.

The finite-precision orthogonality boundary is explicit.

## 5. Galerkin versus minimum residual

PASS.

Galerkin imposes residual orthogonality to the trial space.

Minimum-residual methods instead minimize the Euclidean residual norm.

The chapter does not silently equate either condition with Euclidean solution-error minimization.

## 6. Residual versus error

PASS.

For nonsingular A, the chapter uses A e_m=r_m and e_m=A^(-1)r_m, so residual-to-error interpretation remains relative to the operator and conditioning.

## 7. Exact two-dimensional witness

PASS.

For A=diag(1,2,4), b=(1,1,1)^T, x0=0, and V=[b,Ab], independent replay confirms:

V^T A V = [[7,21],[21,73]]

V^T b = [3,7]^T

c = [36/35,-1/5]^T

x2 = [29/35,22/35,8/35]^T

r2 = [6,-9,3]^T / 35

b^T r2 = 0

(Ab)^T r2 = 0

||r2||_2^2 = 18/175

The exact solution is x*=[1,1/2,1/4]^T, with e2=[6/35,-9/70,3/140]^T and A e2=r2.

The squared energy norm is 9/140.

## 8. Lanczos replay

PASS.

Independent replay gives:

alpha1 = 7/3

beta1 = sqrt(14)/3

v2 = (-4,-1,5)^T / sqrt(42)

alpha2 = 59/21

T2 = [[7/3,sqrt(14)/3],[sqrt(14)/3,59/21]]

beta2 = 3 sqrt(3)/7

## 9. Conditioning control

PASS.

For Ac=diag(1,100,10000) and the same b, the one-dimensional SPD Galerkin/CG step has alpha=1/3367.

Its residual is [3366,3267,-6633]^T/3367.

The squared Euclidean residual norm is 19602/3367, which is larger than the initial value 3.

The chapter uses this only to show that a valid CG step need not monotonically reduce Euclidean residual norm.

The squared energy error decreases from 10101/10000 to 33980067/33670000, consistent with the SPD energy-norm minimization interpretation.

## 10. Preconditioning and matrix-free access

PASS.

The chapter distinguishes left and right preconditioning and states that they change the effective operator seen by the iteration.

It also correctly notes that repeated operator-vector products can generate the trial space without explicitly materializing a dense matrix.

## 11. Finite precision and restarting

PASS.

Exact-arithmetic orthogonality is not promoted into a floating-point guarantee.

The chapter records reorthogonalization/restarting tradeoffs and the possibility that restarting discards useful accumulated directions.

## 12. Downstream boundary

PASS.

ATTNAPPROX may inherit low-dimensional operator-action/projection semantics.

NEURALKRYLOV may inherit the classical trial-space, residual, projection, and preconditioning vocabulary.

Neither inherits a theorem that learned/nonlinear transport obeys classical Krylov convergence merely by analogy.

## 13. Editorial artifact placement

PASS AFTER REPAIR.

The implementation used temporary ledger-authoritative paths under governance/tranches/a155-* because the GitHub connector rejected canonical filenames during composition.

That workaround passed repository validation but was not the preferred mature Atlas layout.

AUDIT-039 canonicalized the artifacts to:

- manuscript/specifications/ATLAS-CH-KRYLOV-001.md
- manuscript/parts/02-mathematical-substrate/ATLAS-CH-KRYLOV-001.md
- mathematics/derivations/ATLAS-CH-KRYLOV-001-DERIVATIONS.md
- mathematics/computational-witnesses/ATLAS-CW-KRYLOV-001.md

The Chapter Ledger now points to those locations.

Temporary duplicate tranche copies were removed.

A bounded transaction receipt remains at governance/tranches/ITERATIVE-SUBSPACE-001.md.

## 14. Reader identity

PASS AFTER REPAIR.

The reader-facing title is restored to Krylov Subspaces and Iterative Solves and the manuscript names the exact source lock at sources/source-locks/ATLAS-CH-KRYLOV-001.yaml.

## 15. Repository integrity

PASS subject to audit-PR validation.

The manuscript contains the required epistemic marker, references section, and exact source-lock path.

The witness contains a Claim boundary.

No governed figure is required.

## Final disposition

AUDIT-039 passes after editorial/provenance canonicalization.

The durable layer is:

operator-generated Krylov spaces + Arnoldi/Lanczos projected structure + explicit Galerkin/minimum-residual distinction + residual/error conditioning boundary + preconditioning semantics + exact finite witnesses + finite-precision/restart limits, without transferring classical guarantees to learned nonlinear transport.
