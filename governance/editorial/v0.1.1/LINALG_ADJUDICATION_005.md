# ATLAS #405: fifth corrected-edition substantive chapter acceptance

Decision: ACCEPT ATLAS-CH-LINALG-001 within GCL editorial scope.
The canonical 80-row ledger advances to exactly 5/80, leaving 75
chapters UNVERIFIED. This decision does not constitute formal proof
certification, publication approval, or whole-book accessibility review.

## Source mathematics and historical corrections

Historical P02-A issue #326 had checked the elementary linear algebra
but withheld chapter acceptance pending corrupt source mathematics.
Its already merged #349 repairs remain in force.

The current corrected LINALG chapter addresses remaining precision
gaps and its acceptance specification with explicit exact witnesses:
general coordinate representations S_W^-1 A S_V, rather than only
similarity transforms; the complex spectral theorem for real normal
rotation matrices with no nonzero real eigenvectors; full rectangular
and compact rank-r SVD with a zero-rank limit; Jordan powers for the
non-normal triangular witness; the unique minimum-norm pseudoinverse
solution among nonunique rank-deficient least-squares minimizers.

The computational witness now actually covers the pseudoinverse and
real normal rotation, in addition to projection, conditioning and
the 2x2 nonnormal singular values. The claims are finite-dimensional
and no neural-training dynamics are inferred.

Original LINALG canonical Git blob before producer correction:
ee19bb8abe978c78e34120349206e45f3a70d662.
Corrected canonical Git blob:
9d74b3f4e2939cf4362a050b0851cd47f822788d.
Corrected derivation Git blob:
f322c866b2f08f94f1b4672d6e2c595f2d963bc0.
Corrected computational witness Git blob:
17026041d75406e8981f7a55f5b2f6d1c068874f.

The figure's unchanged original Wolfram-source Git blob:
94450cbddb6c10c06d61f758454ef0aa0090caf8;
rendered master PNG Git blob:
d861c038e841450ccfabb8f0709e161d6a555450.
The three original standard bibliographic sources and exact scope
in the source-lock register remain unchanged.

## Accountable GCL role evidence

Producer: issue #427, authenticated run
a0427e5cf0f04b2fb2c3d0e91a814e83;
https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/427#issuecomment-6330255452.

Separate critic: issue #429, authenticated run
a0429e5cf0f04b2fb2c3d0e91a814e84;
https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/429#issuecomment-6330301636.

The GCL critic independently executed exact SymPy algebra for the
nonnormal matrix, singular values, Jordan powers, eigenvectors,
rotation, rank-deficient pseudoinverse, projection, rank-one spectral
error, ordinary basis transforms and condition number. It independently
read the actual corrected source, source lock, derivations and
computational witness, matching visual figure identities and citations.
All checks passed. Producer and critic are separate auditable role
runs on the same authenticated GitHub transport account, not fictitious
separate people or an external formal certifier.

## Exact book rendering and protected earlier acceptances

Assembled full-book TeX SHA-256:
5f6e7854d5984e19425694434b4232a68bbd6f4eee79e7f09e2981cf1eac9419.

True three-pass full book 1426-page PDF SHA-256:
6c430c1acc4eb2b91106847aba4ac6e456a09906972e6535ab3cee88f813b7e2.

True complete embedded-MathJax HTML SHA-256:
9d6c9bcd5d339af49b8b049f656a613e2119021e51d60fe81baa35b7be91ca01.

Native LINALG print reading pages 109-123; running-header-only
physical page 124 flagged P2, separately from mathematical validity.
No page-edge text clipping in substantive LINALG pages, source citations,
figure and semantic alt present, unique chapter and historical HTML
anchors retained.

All 2971 historical LaTeX labels, 18 figures/alt texts and 5883
unique HTML IDs remain. No protected original source-lock/figure bytes
changed. Before LINALG acceptance, critic additionally verified that
the prior four accepted chapter source Git blobs are unchanged and
rechecked their new-render PDF and MathJax HTML locations: THESIS
pages 69-76, MAP 77-82, OBJECTS 83-93 and EVIDENCE 95-107.

Their original first-acceptance producer/critic decisions and old exact
render hashes remain recorded; distinct new-render revalidation
records for critic #429 are appended to the canonical chapter ledger.

## Admission and remaining work

The canonical ledger requires eight acceptance tests, including 80
source identities, exact source tree, prior acceptances, distinct
producer and critic, source/figure/witness hashes, new renderer
revalidation and explicit non-publication boundary. Existing
Part I, MAP notation and LINALG maths tests remain in protected CI.

This editorial admission becomes effective after the protected
correction PR's validation check passes and it is merged into the
mutable corrected-edition workbench PR #320. The immutable public
v0.1.0 release remains untouched. The other 75 chapters still
require their own evidence-backed substantive review. The next
keystone in the printed sequence is NONNORMAL.
