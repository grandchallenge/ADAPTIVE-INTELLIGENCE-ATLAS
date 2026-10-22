# ATLAS #405; first Part II substantive chapter acceptance, LINALG

**Decision:** ACCEPT ATLAS-CH-LINALG-001 for corrected-edition GCL
editorial scope, conditional on protected candidate-workbench PR
validation and merger. Complete 80-row ledger increases 4 to 5 accepted
chapters: THESIS, MAP, OBJECTS, EVIDENCE and LINALG; 75 UNVERIFIED.

This is not a formal theorem certificate, PDF/UA accessibility approval,
merge to protected main, or authority to publish the next edition.

## Mathematical and editorial changes

The previously corrected historical delimiter problems from P02-A #326,
PR #349 are preserved and not double-counted as a new achievement.
The new substantive exact-source changes address the following reader
risks instead:

1. Full rectangular SVD U(m,m) Sigma(m,n) V(n,n) versus compact rank-r
   SVD with U_r(m,r), Sigma_r(r,r), V_r(n,r), including zero matrix r=0.
2. A real normal operator may have non-real eigenvalues. The real
   rotation matrix [[0,-1],[1,0]] is normal with eigenvalues +/-i,
   so a real orthonormal eigenbasis cannot be claimed universally.
3. Two-sided input/output basis conversion is S_W^(-1) A S_V;
   similarity S^(-1) A S only when the same endomorphism basis
   conversion is applied to both domain and codomain.
4. Jordan A=[[1,1],[0,1]] has eigenvalues both 1 but
   A^k=[[1,k],[0,1]], with finite and repeated gain not reflected
   by its spectral radius alone.
5. For A0=diag(1,0), b=(2,3), the residual norm squared is
   (x1-2)^2+9. All (2,t) minimize least-squares residual;
   Moore-Penrose A0+ b=(2,0) uniquely minimizes solution norm.
   Added the missing executable pseudoinverse witness required by
   the LINALG specification, instead of asserting a test that was
   not part of the prior actual witness.

Three long-standing monograph source-lock references are preserved
(Trefethen/Bau; Horn/Johnson; Golub/Van Loan), along with their narrow
finite-dimensional claim-authority boundary. These are bibliographic
source entries, not asserted to be Git-pinned source PDFs.

## Accountable GCL role review

Producer issue #426 authenticated START/RESULT/END, run
a0426e5cf0f04b2fb2c3d0e91a814e83,
producer result comment #6330257665.
Critical role issue #430 on producer exact head
8e4ebce996f116f4fcabd9a73b3901845bea813c,
authenticated START/RESULT/END run
a0430e5cf0f04b2fb2c3d0e91a814e84,
critical-result comment #6330288300.
The critic independently replayed exact rational/symbolic matrix
calculations (Jordan powers k=0..26, exact singulars, rank-deficient
pseudoinverse, complex real-rotation spectrum, distinct basis transforms)
and read the actual candidate print and HTML. Distinct accountable
GCL logical roles use the same ordinary authenticated GitHub actor;
this is neither external independent-human review nor formal math
certification.

Producer Git blob identities:

- Canonical LINALG Markdown:
  9d74b3f4e2939cf4362a050b0851cd47f822788d.
- Derivation packet:
  f322c866b2f08f94f1b4672d6e2c595f2d963bc0.
- Computational witness:
  17026041d75406e8981f7a55f5b2f6d1c068874f.

## Actual renderer and prior chapter continuity

Compiled canonical RC2 full-book TeX SHA256:
5f6e7854d5984e19425694434b4232a68bbd6f4eee79e7f09e2981cf1eac9419.

Three-pass full-book PDF: **1,426 pages**, SHA256
6c430c1acc4eb2b91106847aba4ac6e456a09906972e6535ab3cee88f813b7e2.

MathJax HTML SHA256:
9d6c9bcd5d339af49b8b049f656a613e2119021e51d60fe81baa35b7be91ca01.

The candidate retains 2,971 historical LaTeX labels and 18 original
figures with descriptive alternatives. HTML has exactly 5,883
unique IDs. Native LINALG physical reading pages 109–123 have text
and no detected page-edge glyph clipping; page 124 contains only a
running header. Minor P2 print-layout follow-ups also remain at
pages 94 and 108. No P0/P1 mathematical defect was found.

All four previously accepted Part I canonical chapter Git blobs remain
unchanged. Under the new full-book render, the critic separately
rechecked THESIS pages 69–76, MAP 77–82, OBJECTS 83–93,
EVIDENCE 95–107 and corresponding HTML anchors. The EVIDENCE
three historical HTML tables still have 12, 7 and 7 rows.
Original producer/critic mathematical acceptance receipts and old
render identities have NOT been rewritten; the complete ledger holds
distinct current-render critic revalidation fields and archived
historical render identities.

A separate isolated Git worktree was used for source commits after
a shared checkout unexpectedly switched to another branch. The
intended editorial branch was checked against remote and exact
source commit before the critic and ledger ran, avoiding mistaken
acceptance of a stale or unrelated local branch.

Six LINALG, six full-ledger, six MAP, six OBJECTS and six THESIS
local regression tests pass; protected validate must also pass on
the exact proposed PR head before candidate-workbench admission.
The published v0.1.0 tag and distribution remain unchanged.

**Next acceptance target:** ATLAS-CH-NONNORMAL-001, which has
historical P02-A mathematical evidence and an earlier correction
packet but no substantive 80-row accepted receipt.
