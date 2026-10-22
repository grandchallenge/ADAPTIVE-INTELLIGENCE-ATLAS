# ATLAS-405-P02-LINALG-PRODUCER-001

Status: CORRECTED; separate GCL CRITIC required before chapter acceptance.
Producer issue #427, authenticated role run a0427e5cf0f04b2fb2c3d0e91a814e83.
Base editable corrected-edition workbench #320:
344e16b74d0f6ad67a3c68a596b3f4aaccf41007.
Earlier P02-A role review #326 and protected correction PR #349 are
historical antecedents, not an acceptance decision.

The manuscript candidate contains bounded mathematical improvements:
- domain/codomain basis changes S_W^{-1}AS_V versus similarity S^{-1}AS,
  with an exact distinct-basis two-dimensional counterexample;
- real normal rotation requiring complex eigenvectors, not an imaginary
  real-orthogonal spectral theorem;
- dimensionally explicit full rectangular SVD and compact rank-r SVD,
  with rank-zero covered by the full construction;
- nonnormal Jordan powers A^k=[[1,k],[0,1]] and strict separation
  of finite operator amplification from model-training claims;
- rank-deficient least squares with nonunique minimizers and unique
  minimum-norm Moore-Penrose solution; exact residual norm 3.

The source comparison was taken from a currently uncommitted, external
concurrent worktree candidate, captured verbatim in private evidence
patch with SHA256
d33c524f5a3d547aebd450f1b960da606b7103395ed92bbe4fe880c1a5c037af.
The producer audited and imported the bounded diff into an isolated Git
worktree; this attribution is not an independent critic signature.
The accompanying Wolfram witness now contains the missing fourth
pseudoinverse replay and real-normal rotation counterexample.
No figure/source-lock content was changed.

Canonical LINALG chapter blob 9d74b3f4e2939cf4362a050b0851cd47f822788d.
Derivation packet blob f322c866b2f08f94f1b4672d6e2c595f2d963bc0.
Computational witness blob 17026041d75406e8981f7a55f5b2f6d1c068874f.

The selected standard references remain Trefethen/Bau, Horn/Johnson
and Golub/Van Loan, with the same bounded historical source-lock.
The single original figure remains represented by a Wolfram source and
master image with pinned Git blobs in its manifest.

Current recomposed canonical book TeX SHA256:
5f6e7854d5984e19425694434b4232a68bbd6f4eee79e7f09e2981cf1eac9419.
Actual three-pass PDF has 1426 pages, SHA256:
6c430c1acc4eb2b91106847aba4ac6e456a09906972e6535ab3cee88f813b7e2.
Actual full-book HTML MathJax SHA256:
9d6c9bcd5d339af49b8b049f656a613e2119021e51d60fe81baa35b7be91ca01.
The LINALG chapter occupies printed pages 109-124. Physical text and
edge glyphs have been checked on pages 109-123 with no clipping; page
124 contains only running header. This is a P2 print-quality issue.
All 2971 historical TeX labels, 18 figures with semantic alt text,
and 5883 unique HTML IDs remain. Original Part I accepted source
blobs and positions are unchanged, but must be formally revalidated
by the separate critic on the current full-book renderer.

Six new LINALG source/symbolic tests pass (plus independent SymPy
counterchecks for rotation, singular values, Jordan powers, rank
deficiency, projection and conditioning). The ordinary 4/80 acceptance
ledger must remain at four ACCEPTED rows until separate critic
adjudication. This document does not authorize mathematical
certification or public release.
