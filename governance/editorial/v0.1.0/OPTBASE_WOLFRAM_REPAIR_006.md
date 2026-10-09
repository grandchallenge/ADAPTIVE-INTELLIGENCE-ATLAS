# Atlas OPTBASE — Wolfram vertical correction and rendered replay

**Programme:** ATLAS-EDITORIAL-REVIEW-001; #314, #323, #324, editable PR #320.
**Work unit:** FIG-OPTBASE-WOLFRAM-RC2-006. Role CONSTRUCTIVE; distinct adversarial visual/mathematical check required for admission. Baseline workbench head `750ad947a6466d5664ab175b55b05d5d89591001`.

## Historical and revised identities

- Original v0.1.0 master `figures/masters/ATLAS-FIG-OPTBASE-001.png` (1160×6759) and original Wolfram source `figures/wolfram/ATLAS-FIG-OPTBASE-001.wl` are **untouched**, with SHA-1 Git blobs `7abd93008e812514667652200ec1d79ba89b5248` and `61123040326f80ec73a170778ba1140ef3f8fcb9`.
- The earlier v0.1.1 Matplotlib figure remains separately attributed, not erased or misrepresented as Wolfram.
- New Wolfram-source derivative: `figures/derivatives/ATLAS-FIG-OPTBASE-001-v0.1.2.wl`, with YAML manifest `figures/derivatives/ATLAS-FIG-OPTBASE-001-v0.1.2.yaml`, generated with Wolfram Language evaluator 15.0.1 on Linux x86-64; same release-family kernel as source manifest, but no claim of byte-exact standalone `Export` metadata equivalence.
- Candidate PNG `figures/derivatives/ATLAS-FIG-OPTBASE-001-v0.1.2.png`, **700×990**, SHA-256 `b704c720fe3ac90148c310ce6d188264c2d0eb968df6e3324fdadc8327d72179`. PNG byte digest, source Git blob and immutable predecessor source/master blobs are checked by `tools/check_editorial_figure_derivatives.py`.
- Generated manuscript `manuscript/latex/atlas-v0.1.1-rc.2.tex` SHA-256 `f64081df79f1a21bca0cb91e00055b1621873aa9419bd92d7eccde0e2e1d425b` after correct canonical source chapter repointing, 80 chapters, 2,971 historical LaTeX labels and 18 figures.

## Mathematical and visual checks

An initial fixed 1200×400 horizontal Wolfram plate was generated as a diagnostic. Though mathematically correct and its PDF compiled, its image lettering was very small on the book page; it was **rejected** as a final substitute. A vertically stacked Wolfram `Graphics` composition was then generated without changing the mathematical input.

- Panel A is the exact scalar amplification `Abs[1-a]`, `a=eta lambda`, on `[0,3]`, with strict contraction `0<a<2` and the boundary `a=2`.
- Panel B uses `g=(3,4)`, norm `5`, and `tau=2`, yielding clipped `g=(6/5,8/5)`, norm `2`, with unchanged direction.
- Panel C uses decoupled next-theta `181/100`, coupled next-theta `183/100`, exact difference `1/50`. The figure makes **no** optimizer performance, model-training or general convergence assertion.
- Native 700×990 derivative inspected visually. A three-pass PDF rebuild succeeded. Actual physical PDF page **513**, printed page **443**, displays the three panels completely on one page, without a clipped figure or a 6,759-pixel historical blank column. Numeric annotations remain somewhat small: this is a bounded improvement, not a global figure typography signoff.
- Diagnostic HTML built via Pandoc with `tools/release_tex_for_html.py`, resulting in 18 embedded figure PNGs, 18 alt attributes, and a source-semantic `tools/editorial_export_figure_alts.py --write` then `--verify` PASS. Output HTML 5,199,445 bytes.
- Source-to-TeX deterministic `tools/build_editorial_candidate_rc2.py --check` PASS, 80 chapters / 2,971 historical labels / 18 figures. Figure derivative validator checks 3 candidate Wolfram images and original master integrity. `tools/validate_atlas.py`, published v0.1.0 exact-byte checks and 18-figure inventory passed. The inventory correctly retains the **historical** OPTBASE 1160×6759 P1 warning: it is not an RC2 current-derivative failure.

## Residual / governance

Viewers should be able to inspect this actual printed page for remaining small axes and labels. Further print accessibility, Wolfram generator-replay agreement beyond evaluator output, exact mathematical review, all-figure typography, and screen-reader tasks remain. This is a corrected-edition draft only; no automatic human or alternative-GitHub-account ceremony is needed for a distinct agent check, but no chapter final acceptance/public new edition authorization follows.

**Return decision:** submit distinct role-based mathematical and visual review at the exact PR head. Merge only into mutable RC2 workbench with green CI and unchanged protected public release; update #324 with RESULT/1 and preserve controller checkpoint.
