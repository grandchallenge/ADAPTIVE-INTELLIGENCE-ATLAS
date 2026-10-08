# RC2 corrected-edition recomposition evidence

**Programme:** EDITORIAL-REVIEW-001 / parent #314 / editable workbench PR #320  
**Status:** NON-PROMOTIONAL REVISION CANDIDATE. No final chapter acceptance or public release.

## Inputs and exact identities

- Published immutable source: manuscript/latex/atlas-v0.1.0.tex SHA-256 `0d636871e6875bbadbd244e54bf272fdefe2dbd5179515d9d22d3a25e49c384a`.
- Prior Part I editorial overlay: manuscript/latex/atlas-v0.1.1-rc.1.tex SHA-256 `9818f897e2cba7482a1853467e30d9cb14890d68923e83d9368a6d57f766372a`.
- Full corrected chapter source aggregation: workbench at `b3a966d0a5c710f04de509a9c34b6f6d6006a143`, after math/editorial source PRs #346–#355 and #357–#358 merged with individually recorded agent-role critical checks; synchronized with ops protected main PR #356.
- Generator: tools/assemble_manuscript.py then tools/editorial_prepare_markdown.py (editorial-only fork of release preprocessing) then Pandoc via `pypandoc_binary 1.17`, followed by tools/build_editorial_candidate_rc2.py for the declared four-chapter RC1 overlay plus freshly generated last 76 chapters and heading normalization.
- Exact output source: manuscript/latex/atlas-v0.1.1-rc.2.tex SHA-256 `fb638c98863eeeca1130d4a60b306a7536572c807ab01b8736ac99f39eea9414`.
- Baseline-generation control: Pandoc regenerated the published v0.1.0 LaTeX source with identical mathematical/chapter content, differing only in the deterministic PDF trailer-ID block added in the original release candidate. RC2 preserves the predecessor preamble for that historical behavior.

## Structural and mathematical-source checks

- 80/80 chapter boundaries matched old and reconstructed LaTeX.
- 2,971/2,971 historical LaTeX label IDs preserved exactly; no lost or added anchors.
- 18/18 governed images in RC2, including the declared Matplotlib OPTBASE derivative from candidate provenance. Original published Wolfram master and all published v0.1.0 release files unchanged.
- 2,389 redundant downstream generated heading ordinals normalized; the first four edited orientation chapters retained from the earlier candidate overlay.
- Most source corrections are mathematical scope/typing improvements, not new GCL-certified theorems. This is a content-synchronized draft, not independent claim promotion.

## Renderer replay (local diagnostic, not release authorization)

- pdfLaTeX three successive passes completed successfully on the exact RC2 prototype source.
- Diagnostic Pandoc HTML conversion initially omitted all images when fed raw Pandoc-bounded LaTeX, exposing a real release-pipeline dependency. Replayed tools/release_tex_for_html.py first, normalizing **18/18** image directives; then tools/release_add_alt.py added **18/18** caption-derived alt attributes. Resulting HTML contains 18 embedded figures and MathJax markup.
- A nonempty alt attribute is **not** a complete accessible figure description, nor evidence of correct graphical semantics. Exact axes/geometry, print-scale legibility, figure source replay, reading order and accessibility require actual agent visual inspection.
- Review remains required for known excessively wide TRANSFER, original malformed Wolfram OPTBASE master and the new derivative's printed/panel semantics. The public release remains an immutable historical edition.

## Next agent work

1. Run `python3 tools/build_editorial_candidate_rc2.py --check` on the exact candidate revision and require green CI.
2. Rebuild PDF/HTML from committed RC2 via the documented release image normalization path; inspect actual render at sample pages and all 18 figure locations, not merely HTML image counts.
3. Transfer Part I corrections back to canonical chapter Markdown to end the temporary four-chapter overlay, then recompose again with exact-head invariants.
4. Adjudicate per-chapter source findings and individual Figure #323 / Accessibility #325 tasks, without assuming another physical human reviewer or GitHub login is necessary.
