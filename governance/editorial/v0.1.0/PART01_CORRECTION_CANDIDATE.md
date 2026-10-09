# Part I correction candidate — editorial assessment, not acceptance

**Parent:** #314; **Part I task:** #318; **source-reading predecessor:** PR #319.  
**Review base:** immutable annotated tag `atlas-v0.1.0` -> commit `1d4c2532533ff98afb998f86e0443d3fa1d8682e`.  
**Prepared against protected main:** `f6f3a0c5fa681dd5f1556cb6e0cbaf0ebc1b7f04`.  
**Candidate:** `manuscript/latex/atlas-v0.1.1-rc.1.tex`; this is **not** an approved public-release candidate.  
**Original source SHA-256:** `0d636871e6875bbadbd244e54bf272fdefe2dbd5179515d9d22d3a25e49c384a`.  
**Candidate SHA-256:** `9818f897e2cba7482a1853467e30d9cb14890d68923e83d9368a6d57f766372a`.

**Disposition: NO EDITORIAL SIGNOFF. INDEPENDENT TECHNICAL CHECK PENDING. RENDERED PDF/HTML REVIEW PENDING. Repairs and agent review proceed concurrently.**

## Bounded editorial work

| ID | Chapter | Candidate correction | Remaining gate |
|---|---|---|---|
| ER-P1-01 | THESIS | Replaced historical drafting/backfilling narration with enduring dependency explanation. | Editorial reread of surrounding transitions. |
| ER-P1-02 | THESIS | Reframed repetitive chapter promises as four falsifiable demands; no thesis promotion. | Full narrative read; 10 conceptual shifts not yet reduced to proposed compact table. |
| ER-P1-03 | MAP | Collapsed sections 9–27 into a concise status/source/figure/replay legend referring readers to EVIDENCE. Kept 19 prior target labels as historical anchors, not 19 visible sections. | Confirm no incoming references relied on original section granularity. |
| ER-P1-04 | MAP | Added early six-route selector immediately after opening. | Consider full repositioning of navigation table and route examples. |
| ER-P1-05 | MAP | No normalization of all source-TeX display math claimed. | Manual mathematical typography comparison in rendered HTML/PDF. |
| ER-P1-06 | OBJECTS | Consolidated selected microheadings to subordinate subsections, preserving original text/labels. | Editorial read for narrative pacing and mathematical comprehension. |
| ER-P1-07 | OBJECTS | Distinguished two-sided global flow, one-sided semiflow, and local flow with conditional composition law. | **Independent mathematical review** before acceptance; this is a mathematical-meaning edit, not a copy-edit. |
| ER-P1-08 | EVIDENCE | Typeset the six-field packet and the scoped support relation in LaTeX; explicitly distinguished support from entailment. | Check rendering, semantically compare to source lock. |
| ER-P1-09 | EVIDENCE | Cross-reference to detailed evidence chapter is now explicit in MAP. | Worked cross-class reader exercise remains to be written and reviewed. |

No modifications to released `atlas-v0.1.0` or its PDF/HTML assets are authorized. The canonical v0.1.0 source remains unchanged. In chapters 5–80, only redundant section/subsection heading ordinals changed; equations and prose are unchanged, per normalized-tail invariant. The public first release must continue to be described as technically verified but not publication-editorially accepted.

## Validation and known limitations

- The generated candidate compiled with `pdflatex` successfully through **three** passes, producing a local 1360-page PDF from the previous candidate head; a fresh changed-head build supersedes it. No compiled binary is promoted or committed as a release asset.
- The candidate retains all chapter-level and section-level LaTeX labels from the original four chapters. The public edition's unmodified source hash is confirmed in the candidate-generation check.
- The released LaTeX displays double heading numbering (for example, `1.1 1. What...`). The candidate removes **2,467** redundant heading ordinals throughout; retain issue #321 until fresh PDF/HTML check is complete.
- A third-pass LaTeX warning reports a figure float too large by approximately 60.4pt at input line 27504, outside the edited Part I span. Track separately under the figure/typesetting review; compilation is not visual acceptance.
- A complete side-by-side PDF/HTML visual and accessibility pass, including math semantics and anchors, is still outstanding. Existing v0.1.0 assets are immutable.
- Source locks remain project-local synthesis/documentary-synthesis. No mathematical theorem, experimental result, or certification status is promoted through this edit.

## Required next evidence

1. Run and retain the Part I invariance checker against the exact candidate head; independently review the flow classification and all claim-boundary changes.
2. Inspect rendered PDF/HTML side-by-side with the public snapshot; verify first four chapters, formula rendering, route navigation, accessibility, and retained reference anchors.
3. Resolve all nine Part I findings to accepted, explicitly deferred, or still open; do not treat candidate preparation as final correction.
4. Use independent agent editorial/technical checks and a later exact-head audit for acceptance, not an external-human gate to ordinary corrections. At parent #314, final editorial coverage remains **0/80** until those decisions are evidenced.
5. Continue parts 2–14 under separately bounded reviews, maintaining claim/source/figure and editorial states independently. Public-release authorization for a later version remains a separate Human Steward governance gate.

## OPTBASE derivative (continuation)

The corrected-edition candidate uses a declared Matplotlib derivative for one figure path, leaving the original Wolfram master and public v0.1.0 untouched. See OPTBASE_FIGURE_REPAIR_001.md and the candidate derivative manifest. The 76 downstream chapters otherwise retain text and formulas except normalized heading prefixes.

## Part II mathematical scope note

The candidate now also contains the narrowly scoped NONNORMAL exponent-domain correction documented in PART02_MATH_REVIEW_001.md and checked by tools/check_editorial_part01.py. No other downstream prose or equations are changed beyond heading normalization and OPTBASE image substitution.
