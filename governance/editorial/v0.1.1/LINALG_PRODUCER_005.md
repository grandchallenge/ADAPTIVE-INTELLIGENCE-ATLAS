# ATLAS #405: first Part II chapter, Linear Maps and Decompositions

PRODUCER_RESULT: CORRECTED; GCL role-critic source adjudication pending.
Original workbench PR #320 HEAD 344e16b74d0f6ad67a3c68a596b3f4aaccf41007,
original chapter source blob ee19bb8abe978c78e34120349206e45f3a70d662.
Historical review result for this chapter at #326 found core algebra correct and
an earlier P1 packet delimiter problem already repaired on PR #349;
do not conflate that 2026-10-08 review with final corrected-edition acceptance.

Actual current mathematical refinements:
- Full SVD, real orthogonal U/V, rectangular Sigma, positive-rank thin SVD
  and r=0 case explicitly dimensioned.
- Real normal rotation has no nonzero real eigenvectors; complex unitary
  diagonalization, not a false automatic real orthogonal eigenbasis.
- Domain/codomain change-of-basis formula with two independent coordinate
  conversions, and similarity only for the same endomorphism coordinates.
- Defective 2x2 Jordan witness A^k=[[1,k],[0,1]] adds an exact repeated-gain
  counterexample to spectral-radius-only reasoning.
- Rank-deficient least-squares minimizers can be nonunique. The Moore-Penrose
  pseudoinverse uniquely selects the smallest Euclidean norm. For
  diag(1,0), b=(2,3), all (2,t) minimize, but A+ b=(2,0) with residual 3.
  This last example is now in both derivation packet and computational witness,
  correcting the earlier explicit specification-versus-witness gap.
- All original standard finite-dimensional sources and claim boundaries
  remain scoped; the corrections assert no general neural-network property.

New canonical chapter Git blob:
9d74b3f4e2939cf4362a050b0851cd47f822788d.
Updated derivation packet Git blob:
f322c866b2f08f94f1b4672d6e2c595f2d963bc0.
Updated witness Git blob:
17026041d75406e8981f7a55f5b2f6d1c068874f.

Exact independent symbolic replay: SymPy rational/matrix calculations verified
Jordan A^k for k=0..17, exact 2x2 singulars (1+sqrt5)/2 and
(sqrt5-1)/2, complex eigenvalues +/-i and normality of real rotation,
rank-deficient pseudoinverse and entire affine least-squares minimizer
family, and two-sided basis transformation not a similarity.
Six new source-and-arithmetic regression tests PASS.

Real full-book canonical TeX SHA256:
5f6e7854d5984e19425694434b4232a68bbd6f4eee79e7f09e2981cf1eac9419.
Actual 3-pass 1426-page PDF SHA256:
6c430c1acc4eb2b91106847aba4ac6e456a09906972e6535ab3cee88f813b7e2.
Actual MathJax HTML SHA256:
9d6c9bcd5d339af49b8b049f656a613e2119021e51d60fe81baa35b7be91ca01.
The book preserves all original 2971 LaTeX labels, 18 images/semantic alt
descriptions and 5883 unique HTML anchor IDs. LINALG substantive physical
pages 109-123, page124 running-header-only. Every substantive page has
selectable text and zero detected near-page-edge glyphs.
Previous four accepted chapter Git blobs THESIS/MAP/OBJECTS/EVIDENCE are
unchanged; fresh PDF pages 69-76,77-82,83-93,95-107 and matching HTML
were read, EVIDENCE tables retain 12/7/7 rows. Additional running-header-only
pages 94 and 108 are separate P2 print concerns, not mathematical defects.

Do not claim an accepted 5/80 chapter until a separately recorded GCL role
CRITIC verifies exact producer head, sources, mathematical examples, native
renders and previous accepted chapter revalidation, and a GCL adjudicator
passes protected CI and merges ledger correction on editable PR #320.
No protected main/public release authority or formal theorem certification.
