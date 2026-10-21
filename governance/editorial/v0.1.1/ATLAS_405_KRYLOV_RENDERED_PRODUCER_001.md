# ATLAS #405: Krylov P02-A mathematical typography; exact-source producer evidence

**Disposition: PRODUCTION PASS; exact-revision independent critic remains REQUIRED.**
Original historical issue [#326](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/326);
original RESULT/1 [comment 6058138109](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/326#issuecomment-6058138109).
Immutable public v0.1.0, its manifest and tag remain untouched.

## Source and correction identities

- Parent editorial PR #320 base: 07ea97f688bd8eab54f4d395aa2f6b1f1fa2c6ef.
- Original P02-A PR #349 is an actual ancestor of that head.
- **New producer correction:** 48 standalone mathematical expressions and eight inline spans
  in ATLAS-CH-KRYLOV-001.md; the corresponding full-book RC2 TeX regenerated
  from canonical Markdown. No chapter identity, theorem scope, input matrices,
  proof, algorithms, reference citekeys, or original figure source was altered.
- The repaired displays include the Arnoldi Hessenberg relation, symmetric Lanczos
  recurrence, Galerkin projection, orthonormal Lanczos matrix, exact rational witness,
  residual/error norm relations, CG conditioning counterexample and preconditioner
  systems. Previously these printed in unformatted ASCII as
  'A V_m = V_(m+1) Hbar_m.' and similar.
- Final RC2 TeX SHA-256:
  ba69c91022ff8ab8a92a9c0daa4cd1e2046d7ec62f521b4020e9cb6fb15505cd.

## Exact rendered book; producer evidence

Three successive pdflatex -halt-on-error passes from the changed canonical RC2
source finished using TeX Live plus a **local, unpacked**
texlive-latex-extra distribution overlay for missing truncate.sty.
The Debian package bytes had SHA-256:
d0436f2a183211918f6b575a2c00913880cb0ab3d9278f19e37d8c76054b0772.
No global TeX installation or repo vendoring was performed.

- PDF: 1,426 physical pages; SHA-256
  edf7d49e3698d294db77c4b4e8b43b13b4d64c550f38226f4884cbf661555420.
- Embedded standalone MathJax HTML SHA-256
  3f4c6ce90f9db056c8b92cf5b81f5ac1f04395cadefa75bff802901efa9eef3a.
- HTML: 5,908 IDs, all unique; 18 figure embeddings; all 18 source-semantic
  descriptions verified by content digest and figure identity.
- RC2 recomposition: 80 chapter boundaries, 2,971 original LaTeX labels
  and 18 figure placements unchanged; no duplicate display-heading ordinals.
- PDF physical page 138 was rasterized with Ghostscript and inspected after repair;
  Arnoldi now appears as displayed mathematics, not raw ASCII.
  Extracted PDF page text contains neither 'Hbar_m' nor 'beta_(j-1)'.
- The exact Fraction arithmetic regressions validate the 2D Galerkin witness,
  orthogonality/residual norm and SPD CG Euclidean residual increase against
  A-error improvement. Four tests pass; these do not replace mathematical review.

The rendered PDF and HTML are **local evidence outputs**, not authorized
publication artifacts. All SHA-256 values refer to actual files produced from
this same candidate correction, not the preceding 2026-10-09 outputs.

## Critic obligations and acceptance limit

A different accountable critic run with independent substantive reading of
this exact source must:
1. Check complete derivations/witness, including exact-arithmetic scope and
   nontrivial distinctions between Arnoldi, Lanczos, Galerkin and CG.
2. Inspect full Krylov chapter PDF pages 137–146 and corresponding HTML;
   matrix line breaks, glyphs, citation anchors and print legibility matter.
3. Check remaining mathematical prose typography and preservation of chapter
   boundary, figure, anchor and immutable public-release identities.
4. Return the exact reviewed producer commit, critic role/run ID, findings,
   source and rendered artifact digests, independent verification evidence.

No chapter becomes ACCEPTED from producer tests alone. A subsequent changed
source head invalidates critic approval; a new exact-head replay is required.
Original issue #326 stays historically returned; do not reopen as a new job.
The companion reconciliation JSON maps all twenty historical review packets
and source-correction PR merges to their seventy-six assigned chapters.

## Critic-driven correction

The separate-role CRITIC pass on original head 17aa3e8 found one additional raw Hbar_m on physical PDF page 139 (chapter section 5). See #409. Canonical Markdown now uses inline barred-H math; source and TeX regression reject raw Hbar_m. Updated three-pass PDF and HTML digests belong to corrected source. A new role pass must adjudicate changed head; no certification implied.
