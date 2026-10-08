# Atlas TRANSFER — vertical Wolfram print-layout repair

**Programme:** EDITORIAL-REVIEW-001, parent #314 and figure triage #323. **Role:** CONSTRUCTIVE. Baseline mutable manuscript workbench head `7009dd8ca120d1fcd3b99636fba7be5d9ed44eba`. Not a public release or mathematical claim promotion.

## Defect and versioned repair

The historical `ATLAS-FIG-TRANSFER-001.png` image is a very wide 1120×268 horizontal pair of mathematically distinct schematics. At the printed Atlas page width, the internal box labels and decoder annotations become significantly smaller than surrounding body text. The historical master and `figures/wolfram/ATLAS-FIG-TRANSFER-001.wl` source are immutable for published v0.1.0.

- New derivative: `figures/derivatives/ATLAS-FIG-TRANSFER-001-v0.1.1.png`, **700×760**, SHA-256 `cc03d27f8c6384940606982199abb8527daf71b6ace09c3645c5b93515c0f2ba`.
- New Wolfram source: `figures/derivatives/ATLAS-FIG-TRANSFER-001-v0.1.1.wl`, Git blob SHA-1 `31e684f131b6fc959231d95414a7776175b2b6e3`. Generated with Wolfram evaluator version 15.0.1, matching historical generator family; standalone `Export` byte-equivalence is **not** claimed.
- Source/render provenance and mathematical limits are recorded in versioned `figures/derivatives/ATLAS-FIG-TRANSFER-001-v0.1.1.yaml`, referencing the exact historical source/master SHA-1s.
- Uses two vertically stacked Wolfram Graphics insets and native `Subscript` typesetting, rather than squeezing both schematics into the same horizontal strip. This changes box positions, layout and literal typographic representation only.
- The canonical chapter `manuscript/parts/03-representation-learning/ATLAS-CH-TRANSFER-001.md` now points to the corrected-edition derivative. The original figure/master path and source locks remain unchanged.

## Immutable mathematical boundaries

Left reconstructive schematic: the source representation `z_s=(4,2)` and target representation `z_t=(6,1/2)` produce the common residual `r=(3,1)` with declared target readouts `D_1=4`, `D_2=5`. Right failure schematic: `r_A=(1,0)` and `r_B=(1,1)` collide at `P(r)=1` while `D_2(r_A)=2` and `D_2(r_B)=1`. The arrow direction and boxes were retained. No empirical transfer advantage, robustness or learned-model performance is claimed. Manifest `parameters`, `literal_semantics` and `claim_boundary` are byte-equivalent to historical manifest values.

## Render and regression verification

- `tools/check_editorial_figure_derivatives.py`: PASS for all **four** derivative Wolfram images; checked transfer PNG byte SHA256, exact dimensions, derivative Wolfram source Git blob identity and original historical generator/master identities; candidate chapter link, PDF image reference and nonchanged mathematical parameters verified.
- `tools/build_editorial_candidate_rc2.py --check`: PASS, generated RC2 SHA-256 `887e7c0aa5fdf8b7a19b6398d319af23243c62eaeafe0d421e90c5a2711f0d49`, 80 chapters, 2,971 LaTeX labels and 18 images.
- Three-pass pdfLaTeX: PASS. Actual rendered physical PDF page **324**, printed page **254**, inspected at 110dpi: both diagrams appear on a single page, with separate titles and complete boxes/arrows. Font size remains a later overall book-scale consideration, but the original side-by-side cramped layout is corrected.
- Pandoc HTML: 18 PNG images embedded, 18 semantic alt attributes; `tools/editorial_export_figure_alts.py --write` then `--verify` PASS, resulting HTML 5,213,213 bytes. The new derivative is matched to its source alt via actual PNG bytes.
- Structural repository check, public release exact-byte audit, and 5 semantic-alt hostile/positive tests PASS.

## Residual review gates

This is a candidate-edition print legibility repair for the P2 TRANSFER finding, not a final screen reader, WCAG, mathematical certification or typography clearance. The historical figure inventory correctly continues to flag the immutable released 1120×268 master. Agent-role adversarial visual and mathematical review and exact-head CI are required for admission to editable PR #320. Source/public edition promotion and chapter acceptance are separate.
