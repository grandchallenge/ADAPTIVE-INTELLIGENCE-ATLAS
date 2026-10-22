# ATLAS #405: seventh corrected-edition chapter editorial acceptance

Decision: ACCEPT ATLAS-CH-KRYLOV-001 in the limited *editorial* scope.
Canonical complete 80-row ledger now proposes 7 ACCEPTED and 73
UNVERIFIED. This is not theorem certification, full book PDF/UA
attestation, protected-main integration or publication authorization.

## Concrete corrected mathematics

Arnoldi's (m+1)-basis vector exists only without early breakdown.
The zero-residual case already solves the system; K_m dimension can be
strictly smaller than m if generated vectors become dependent. A=I
and nonzero e1 give a one-dimensional invariant Krylov subspace.

The displayed Galerkin matrix in the real chapter uses transpose.
Complex Arnoldi and Hermitian Lanczos instead use conjugate adjoints.
The critic reproduced v=(1,i) for which v^T v=0 but v* v=2.

Galerkin solvability for an arbitrary nonsymmetric invertible operator
requires a further assumption: invertible 2x2 swap A and V=e1 give
V^T A V=0. By contrast, an SPD A gives an SPD projected matrix when
V has full column rank. Both displayed left/right preconditioning
identities require fixed invertible M. These hypotheses now appear in
canonical manuscript and derivation packet.

The original finite witness remains mathematically unchanged:
diag(1,2,4), b=(1,1,1), Krylov K_2, projected [[7,21],[21,73]],
coefficients [36/35,-1/5], residual [6,-9,3]/35 and Euclidean
residual squared 18/175. Independent exact Lanczos checks obtain
alpha2=59/21 and beta2 squared 27/49. The SPD conditioning control
diag(1,100,10000) genuinely increases the one-step Euclidean
residual squared from 3 to 19602/3367 while reducing the squared
A-norm of the error from 10101/10000 to 33980067/33670000.
The source forbids transferring these classical identities directly
to learned nonlinear architectures.

## Accountable role passes and exact source

Producer [#435](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/435#issuecomment-6338539836),
run a0435e5cf0f04b2fb2c3d0e91a814e86, initial source
bce09f0e4149f29131114d827b4084724ac962d3.

Separate GCL CRITIC [#436](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/436#issuecomment-6338591282),
run a0436e5cf0f04b2fb2c3d0e91a814e87, reviewed exact
candidate head 132d55571e3dfa2cda3cd62be868498354eb5eba.

Corrected canonical chapter Git blob
405fbe3f462998b3950b232309d811763108f3c7;
derivation blob ba4ac3e46e3ba887e50b27218ca40a603cb85b3a;
unchanged exact computational witness blob
c8fcb7d719fcf452813727e91d27bc2c48a19a20.
Three pinned historical LINALG prerequisite Git source identities
all matched; three classical bibliographic entries are distinct.

## Actual rendered artifact and preservation

Full RC2 TeX SHA256:
e19f5e0827060cdd90ecef17a7eda4571cfe91d4cc0a3b7b456f416f2221b2e3.
Actual triple-pass 1428-page PDF SHA256:
6843346661657caad7f0706cc6e972cc5906284def5195864d1bb998f29893ef.
Actual MathJax HTML SHA256:
dd32fdbc348f2985f73fa90f24e36aade78a3f5515b37fd4ad26bca8a4335492.
KRYLOV pp137–148 pass selectable-text and page-edge checks.
All 2971 original LaTeX labels and all 18 figures with semantic
HTML descriptions are retained.

The six prior accepted chapter Git source blobs remain unchanged.
The critic separately examined their current native PDF page ranges
(THESIS 69–76, MAP 77–82, OBJECTS 83–93, EVIDENCE 95–107,
LINALG 109–123, NONNORMAL 125–136) and matching HTML chapter anchors.
Historical source/math critical evidence and former output hashes
are preserved unchanged; current-render revalidation is additional.

Seven Krylov exact-arithmetic hostile tests and eight 7/80
ledger tests pass; all old MAP checks pass as well. The
corrected-edition ledger is only **operationally admitted** after
protected validate SUCCESS and governed merge into editable PR #320.

Next candidate chapter: ATLAS-CH-PROBINFO-001. Public v0.1.0
and separate publication/accessibility/certification gates stay untouched.
