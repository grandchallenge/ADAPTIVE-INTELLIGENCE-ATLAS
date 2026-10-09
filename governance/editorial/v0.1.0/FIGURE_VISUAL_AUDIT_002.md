# ATLAS FIGURE VISUAL TRIAGE / 002 — RC2

**Campaign:** ATLAS-EDITORIAL-REVIEW-001; issues #314, #323, #324, #325  
**Role:** VISUAL_CHECK (separate critical inspection pass)  
**Run:** ATLAS-FIGURES-RC2-VISUAL-002  
**Exact inspected source:** PR #320 head `0a06b8d419eceab4bd91810effea44126833c9b1`  
**Primary visual samples:** all 18 raster assets in three contact sheets at ~945-pixel tile width, plus full native images for INFO, MANIFOLD, RESIDUAL, PSPECTRUM, TRANSFER and corrected-edition OPTBASE derivative.  
**Input artifacts:** master PNGs in `figures/masters`; declared OPTBASE v0.1.1 derivative in `figures/derivatives`.  
**Classification:** `P1` = unreadable or misleading load-bearing annotations, `P2` = legibility/layout risk needing print-scale inspection, `VISUAL_TRIAGE_OK` = no specific visual anomaly detected **at this inspection resolution**. These labels do not imply mathematical proof, source-generator reproduction, accessibility acceptance or final publication clearance.

The independent provenance inventory (`python3 tools/editorial_figure_inventory.py --check`) reports 18 matched source/render identities, canonical LaTeX placements and HTML images with alt attributes. That is *not* a Wolfram-kernel replay of 18 plots. RC2 has 80 chapters and 18 figures; three-pass PDF compilation, diagnostic HTML embedding and MathJax completed locally, but page-by-page print-scale and screen-reader inspections remain separate work.

| Exact figure ID | Inspected visual content | Disposition / concrete follow-up |
|---|---|---|
| ATLAS-FIG-ARCHHIST-001 | Six architecture sketches: layered maps, convolution, recurrence, encoder/decoder, highway and residual topology | **P2:** architecture names readable in contact sheet, inner node/edge captions visually tiny; verify full-page print, increase typography if needed |
| ATLAS-FIG-ATTNOP-001 | Scores `S`, row-mixing matrix `A`, values `V`, resulting `Y=AV`, grayscale matrix cells | **P2:** tabular quantities discernible and tonal blocks distinct; fine numerical cell annotations may be marginal at book scale; check figure against exact toy matrix values |
| ATLAS-FIG-BCONTRACT-001 | Contract diagram linked to perturbation sensitivity ellipse and unit perturbation circle | **P2:** panel labels and small arrow captions need print-scale verification; elliptical geometry visually distinguishable; inspect line/axis meaning from manifest |
| ATLAS-FIG-DYN-001 | Exponential attraction, saddle-node stable/unstable branches, exact Hamiltonian orbit | **P2:** thin axis labels and branch text in three subpanels need full-page check; dashed/solid styles visible |
| ATLAS-FIG-INFO-001 | Native-resolution 2×2 joint probability grid `3/8,1/8;1/8,3/8`, uniform marginals, `I(X;Y)=0.1887` bits | **VISUAL_TRIAGE_OK for native PNG:** textual values and mathematical takeaway readable; vertically padded layout demands actual PDF-page check |
| ATLAS-FIG-LINALG-001 | Non-normal unit-circle image/ellipse, singular-value formula and matrix conditioning comparison | **P2:** singular-value annotation is much smaller than plot geometry in overview; verify formulas and symbol fidelity at print size |
| ATLAS-FIG-MANIFOLD-001 | Tangent step, sphere and local exponential map vs normalized retraction | **P1 confirmed:** native PNG places `R_x(v)` and `Exp_x(v)` labels directly on top of one another near the endpoint; the distinction between the two constructions is obscured. Repair Wolfram label placement/leader offsets, regenerate with source/render identity and inspect again |
| ATLAS-FIG-NORMREP-001 | Radial versus tangential normalized information, chord/arc/SLERP geometry | **P2:** direction/angle annotations require native or print-scale verification; contrast among radial/tangent/chord features survives overview |
| ATLAS-FIG-NUMERICS-001 | Explicit/implicit Euler stability regions and Lie–Trotter/Strang local-defect scaling | **P2:** dense axes and logarithmic panel labels require high-resolution PDF inspection; log scaling and solid/dashed distinction observed, precise plotted samples not replayed |
| ATLAS-FIG-OPTBASE-001 | **Derivative** displays (A) `|1-a|` with `0<a<2`, (B) norm clipping of `g=(3,4)` to `(6/5,8/5)` with `tau=2`, (C) next-parameter values `183/100` coupled and `181/100` decoupled | **VISUAL TRIAGE PASS on derivative only:** native 2482×738 panels, axes, dashed stability boundary, marked clipping vectors and coupled/decoupled legend placement are visible; source Python Fraction assertions and derivative manifest agree. Historical Wolfram master at 1160×6759 remains **P1** and is deliberately unchanged. No claim of Wolfram replay or final native-Wolfram replacement |
| ATLAS-FIG-OPTDYN-001 | Momentum-state phase trajectories, eigenvalues/unit circle, finite-horizon amplification | **P2:** three dense panels, small eigenvalue labels; line families visible; exact finite-horizon gain requires separate algebraic replay |
| ATLAS-FIG-PSPECTRUM-001 | Finite-horizon non-normal amplification versus normal reference, and 2-norm pseudospectral contour families | **P1 confirmed:** central native-resolution `eps` contour annotations visibly overlap one another and the inner curves, compromising the quantitative legend. Reposition labels outside concentric central cluster or use a separate legend; preserve actual contour values/styles |
| ATLAS-FIG-QUOTIENT-001 | Three parameter representatives to same function, positive-part function graph | **P2:** weight values and small function annotations cramped; no direct contradiction seen in overview |
| ATLAS-FIG-REP-001 | Reflection/equivariance vector diagram, invertible recoding and invariant readout | **P2:** right-panel text is small at contact scale; geometric correspondence visible; verify text sizes and arrows at print scale |
| ATLAS-FIG-REPLAY-001 | Evidence chain Source→Method→Execution→Observation→Interpretation→Claim, plus review/replay→adjudication→certification | **VISUAL_TRIAGE_OK as schema:** conceptual direction and dashed governance path visible; ensure labels accessible as structured text, not only in pixels |
| ATLAS-FIG-RESIDUAL-001 | Native figure: nuisance orbit collapse to invariant signal `s=2`, and inverse recoding preserving the residual | **P2:** native plot/data and right-hand boxes readable; substantial empty space and fine point labels reduce efficiency at printed width; check actual page |
| ATLAS-FIG-TRANSFER-001 | Native 1120×268: common residual reconstruction (left) contrasted with lossy bottleneck failing task sufficiency (right) | **P2 confirmed print-scale risk:** conceptual boxes/arrows distinguishable at full 1120px width, but internal captions and domain coordinates are markedly smaller than headings; verify scaled print plate at intended width; avoid assuming full-resolution screen view guarantees book readability |
| ATLAS-FIG-TRANSFORMER-001 | Residual-stream transformer block, causal mixing matrix with future zeros, encoder/decoder topology | **P2:** multiple small labels in three subpanels, especially mixing table and block diagram; check print and accessible descriptions |

## Mathematical and source-scope guardrails

The OPTBASE derivative has declared Mathematica/Wolfram *predecessor*, but the new raster is produced by Python Matplotlib with distinct, truthful metadata. Its exact input quantities were checked in the Python generator: `(3,4)` has norm 5; `(6/5,8/5)` has norm 2; `183/100-181/100=1/50`. The visible coupled and decoupled labels match the derivative `MODEL` dictionary and declaration. No empirical optimizer ranking is asserted.

All 18 figures were visually inspected at overview resolution, and six at native resolution. This pass **does not** assert successful Wolfram generator re-execution, exact numerical replay of 17 existing masters, fully legible PDF pages, colorblind accessibility, screen-reader quality, semantic alt-text completeness, or new edition acceptance.

## Repair queue and next exact evidence

1. **P1 MANIFOLD:** resolve `R_x(v)` / `Exp_x(v)` text overlap in governed Wolfram plot, with revised source/render provenance, native and PDF print checks.
2. **P1 PSPECTRUM:** move tightly clustered epsilon contour labels or supply a discrete legend; keep analytic contour and gain geometry unchanged, replay generator and check screenshot.
3. **P1 released OPTBASE historical master:** preserve historical bytes; maintain clearly attributed derivative pending native generator-path reproduction or governed explicit replacement and panel/print review.
4. **P2 typography/print:** audit TRANSFER plus small-panel figures at actual PDF page scale. Expand descriptions of 18 assets beyond caption-derived HTML alt attributes, per #325.
5. For every subsequent image change, rerun figure inventory, PDF/HTML embedding, source hash, agent math and visual review at the **new exact head**.

**Disposition:** `PARTIAL — visual triage and two new confirmed P1 graphic issues`. Zero new final chapter signoffs; no public v0.1.0 mutation.
