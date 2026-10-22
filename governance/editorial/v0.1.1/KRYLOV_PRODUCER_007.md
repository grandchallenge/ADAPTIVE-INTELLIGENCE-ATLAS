# ATLAS #405: KRYLOV chapter producer review

Status: PRODUCED, NOT YET CRITIC ACCEPTED; original workbench source
bce09f0e4149f29131114d827b4084724ac962d3.
GCL producer issue #435, authenticated Editorial START run
a0435e5cf0f04b2fb2c3d0e91a814e86. Previously completed #408/#410
Krylov mathematical typesetting repairs and reviewer #409 are source
corrections, not the present chapter's final scoped acceptance.

## Substantive bounded repairs

- Arnoldi assumes nonzero starting residual and absence of early happy
  breakdown before the extra basis vector V_(m+1) can be defined.
  A=I with a nonzero start is a concrete counterexample to an
  unconditional m+1-vector Arnoldi claim; the Krylov space is invariant.
  Krylov dimension is at most m, not automatically exactly m.
- The main displayed projection and transpose conventions are explicitly
  real finite-dimensional conventions. Complex Hilbert-space Arnoldi,
  Hermitian Lanczos and Galerkin orthogonality use conjugate transpose,
  not ordinary transpose. For v=(1,i), v^T v=0 although v* v=2.
- Invertibility of the projected Galerkin matrix does not follow from
  invertibility of a nonsymmetric A. The exact invertible 2x2 swap
  operator and V=e1 give V^T A V=0. For SPD A and full-rank V, the
  reduced matrix remains SPD and the projected solve is unique.
- Both preconditioning equivalences assume a fixed invertible M;
  a singular or iteration-dependent M requires different semantics.

The original three-dimensional SPD examples, two-dimensional subspace,
the exact rational Lanczos recurrence, CG-versus-residual counterexample,
source lock bibliographic authority, and later learned-model claim
boundaries were preserved. Derivation D2/D4/D10 now state the same
hypotheses explicitly.

Seven independent stdlib-only tests verify the exact Galerkin reduced
matrix, coefficients, solution, residual, orthogonality and energy error;
Lanczos alpha/beta squared; conditioning control with increasing
Euclidean CG residual and decreasing SPD energy error; happy breakdown;
complex conjugate transpose; singular projected system despite
invertible A; preconditioner and historical TeX/figure identities.

Current source Git blobs: chapter
405fbe3f462998b3950b232309d811763108f3c7,
derivation ba4ac3e46e3ba887e50b27218ca40a603cb85b3a,
and unchanged computational witness c8fcb7d719fcf452813727e91d27bc2c48a19a20.
All three historical pinned LINALG Git objects match the original
source lock, together with three historical bibliographic entries.

## Actual new rendered book

Three-pass full PDF: 1428 physical pages; SHA256
6843346661657caad7f0706cc6e972cc5906284def5195864d1bb998f29893ef.
MathJax full-book HTML: SHA256
dd32fdbc348f2985f73fa90f24e36aade78a3f5515b37fd4ad26bca8a4335492.
Full corrected-edition TeX SHA256
e19f5e0827060cdd90ecef17a7eda4571cfe91d4cc0a3b7b456f416f2221b2e3.
All 2971 historical LaTeX labels and 18 figures with matching
semantic alt descriptions remain. KRYLOV pages 137-148 are selectable
text with zero edge/margin text collisions. The earlier six accepted
chapter Git sources and PDF/HTML chapter anchors are unchanged;
rechecked physical pages THESIS 69-76, MAP 77-82, OBJECTS 83-93,
EVIDENCE 95-107, LINALG 109-123 and NONNORMAL 125-136.

The new PDF/HTML digests are not historical versions of the previous
five/six critic returns. An independent GCL role critic must revalidate
current rendered artifacts separately and preserve original evidence.

This producer grants neither chapter admission nor formal mathematical
certification, PDF/UA conformity or public release authority.
