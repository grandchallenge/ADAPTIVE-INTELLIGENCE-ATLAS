# Atlas figure-label repair tranche — Wolfram-native RC2 candidates

Programme: EDITORIAL-REVIEW-001 (#314). Work packages: #362 (MANIFOLD) and #363 (PSPECTRUM). Figure review parent #323. Source candidate predecessor: PR #320 at dcbaf42bb6ab1ea928c20a7c1b03f845fc5c08cc. Scope: editable corrected edition v0.1.1-rc.2 only; no edits to protected historical master images, original Wolfram generator files, public v0.1.0, or protected main.

## Repaired assets and exact identities

| Figure | Derivative PNG | SHA-256 | Dimensions | Derivative Wolfram source blob |
|---|---|---|---|---|
| ATLAS-FIG-MANIFOLD-001 | figures/derivatives/ATLAS-FIG-MANIFOLD-001-v0.1.1.png | `49db8aaeecf2ca3625eb033d842cc022c37bcc4e3134278cc2a76b423b632ccf` | 760×792 | `2cdedefbb3323b36de4c9a7f871adc93342e2447` |
| ATLAS-FIG-PSPECTRUM-001 | figures/derivatives/ATLAS-FIG-PSPECTRUM-001-v0.1.1.png | `98e7228b577c1dea820ee94b8ad71d1da51114068f0d0f0495f861013635c6be` | 1100×418 | `24a45fdf9719d59092d892f3160b235c0ca94874` |

The figures were generated as Wolfram Graphics outputs using the stateless Wolfram Language evaluator, version 15.0.1 for Linux x86-64 (July 2, 2026), matching the version/system of the historical manifests. Image PNG bytes were captured directly from the evaluator. They are **not** claimed byte-identical to a standalone `Export` replay, because PNG timestamp/metadata can differ. Their derivative .wl files provide reproducible Wolfram mathematical definitions and an explicit derivative export path. The original manifests remain untouched; candidate derivative YAMLs bind generator source blob hashes, image SHA-256s, dimensions, source/manifold mathematics and historical identities.

MANIFOLD repair: retained the exact sphere, tangent plane/vector, points `x=(0,0,1)`, `v=(0.8,0,0)`, exponential map and normalized retraction. Only placed separate white-backed endpoint labels with leader lines. Native and PDF inspection show two distinguishable endpoint annotations instead of label collision.

PSPECTRUM repair: retained `a=4/5`, `K=4`, matrices `[[a,K],[0,a]]` and `aI`, 2-norm transient-gain samples, analytic non-normal radii `sqrt(eps(eps+K))`, normal radii `eps`, and epsilon levels `0.01,0.03,0.1,0.3`. Replaced overlapping center epsilon labels with an explicit inner-to-outer ordered legend below the circles, moved the eigenvalue caption out of the center, and labeled the two plot panels. A Wolfram evaluator warning mentioning symbols A/Nmat was emitted but graphical output was produced; a clean standalone local kernel replay is a separate provenance test.

## Verification and remaining scope

- `tools/check_editorial_figure_derivatives.py`: verifies new image hashes and raster dimensions, derived Wolfram source Git blobs, historical master/source Git blobs, mathematical parameters/claim boundaries unchanged, chapter Markdown references, and exactly 18 corrected-edition LaTeX image placements.
- `tools/build_editorial_candidate_rc2.py` regenerated candidate TeX after the two Markdown source links changed. **80 chapters, 2,971 original anchors, 18 figures** preserved.
- Local pdfLaTeX three passes completed without fatal errors. Pixel renders examined: physical PDF page 136 (printed page 66, PSPECTRUM figure 6.1) and physical page 172 (printed page 102, MANIFOLD figure 9.1), both at 125 dpi; formerly overlapping annotation text is separated and the figures are not clipped.
- Pandoc diagnostic HTML normalized all 18 image directives and produced 18 images with 18 `alt` attributes. Image-in-HTML SHA-256 readback matched both new derivative files **byte for byte**.
- Small print labels on these and other Atlas figures still merit a separate typography/accessibility pass. Presence of HTML alt attributes does not certify their semantic quality. This repairs two specific P1 label collisions only, not all 18 figure quality gates or public release authorization.

**Role doctrine:** independent means separately evidenced agent production, visual check and mathematical review passes; no distinct physical person or GitHub login is required. Continue changed-head validation and Figure #325 accessibility review before any acceptance claim.
