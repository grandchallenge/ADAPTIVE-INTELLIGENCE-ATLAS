# OPTBASE figure repair — candidate receipt

Parent #314 / figure task #324 / draft PR #320.

Published v0.1.0 remains immutable at 1d4c2532533ff98afb998f86e0443d3fa1d8682e.

## Observed defect

The original Wolfram raster ATLAS-FIG-OPTBASE-001.png is 1160 x 6759 pixels. Inspection in four full-resolution quadrants confirms a severe height expansion of the decay panel and the other two panels compressed into the middle. It cannot be repaired by trimming empty margins.
The original WL decay Graphics uses a horizontal range of 1.79..1.85 and vertical range -0.6..0.8 without an explicit AspectRatio. An explicit bounded aspect ratio is a plausible Wolfram-side fix, but a pinned Wolfram 15.0.1 replay has not yet been performed.

## Implemented editorial derivative

- Generator: tools/render_optbase_editorial.py, Python Matplotlib 3.10.3.
- Raster: figures/derivatives/ATLAS-FIG-OPTBASE-001-v0.1.1.png; 2482 x 738 pixels.
- SHA-256: 550ad96bd4f7763260a8b64e79518734b0133dc318f5ee9bb221d2ad1fcf7591.
- Manifest: figures/derivatives/ATLAS-FIG-OPTBASE-001-v0.1.1.yaml.
- This is an expressly labeled Matplotlib derivative, NOT a falsely attributed Wolfram replay. Original Wolfram source and raster remain intact.

## Mathematical quantities verified with exact Fraction arithmetic

- A: scalar amplification abs(1-a), a=eta*lambda, strict contraction when 0<a<2. Boundary points have magnitude one and are drawn open.
- B: gradient (3,4), norm 5, clipping threshold 2 gives (6/5,8/5) with norm 2.
- C: coupled next theta=183/100, decoupled=181/100, exact difference=1/50.
- No general nonlinear convergence theorem or optimizer performance ranking is claimed.

## Validation and gates

The corrected candidate LaTeX changes only one OPTBASE image path in chapters 5-80 beyond normalized heading ordinals. Exact released v0.1.0 source hash remains untouched. The local LaTeX build and diagnostic HTML build completed; CI exact-head replay still required after committing.
The remaining independent agent checks include final print-scale and mathematical review of each panel, HTML embedded-image/alt-text audit, and optional new Wolfram renderer replay. These are ordinary concurrent agent tasks, not a human review stop condition. No final figure approval or publication authorization is asserted.
