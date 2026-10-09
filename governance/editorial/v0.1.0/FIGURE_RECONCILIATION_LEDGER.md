# Editorial figure and plot reconciliation — initial inventory

**Scope:** published v0.1.0 (immutable); editorial work for #314, #321, draft #320.
**Disposition:** MECHANICAL INVENTORY ONLY; NO VISUAL OR SEMANTIC APPROVAL.

Automated checks: 18/18 figure-register entries have a manifest, Wolfram generator,
PNG master, expected source and output git-blob SHA-1, and canonical LaTeX
references. The published HTML contains 18 embedded images with 18 nonempty
caption-derived alt attributes. These checks establish identity and cardinality,
not correct geometry, numbers, axes, legends, vector quality, contrast,
accessibility, or accurate rendering within the PDF.

| Figure | Chapter | Class | Raster px | Triage |
|---|---|---|---:|---|
| ATLAS-FIG-PSPECTRUM-001 | ATLAS-CH-NONNORMAL-001 | data-derived | 1100x421 | VISUAL_REVIEW |
| ATLAS-FIG-MANIFOLD-001 | ATLAS-CH-GEOM-001 | schematic | 760x810 | VISUAL_REVIEW |
| ATLAS-FIG-ATTNOP-001 | ATLAS-CH-ATTNOP-001 | data-derived | 1000x388 | VISUAL_REVIEW |
| ATLAS-FIG-OPTDYN-001 | ATLAS-CH-OPTDYN-001 | simulation-derived | 1120x390 | VISUAL_REVIEW |
| ATLAS-FIG-BCONTRACT-001 | ATLAS-CH-BCONTRACT-001 | schematic | 1100x554 | VISUAL_REVIEW |
| ATLAS-FIG-REPLAY-001 | ATLAS-CH-REPLAY-001 | exact | 1100x416 | VISUAL_REVIEW |
| ATLAS-FIG-LINALG-001 | ATLAS-CH-LINALG-001 | exact | 1100x470 | VISUAL_REVIEW |
| ATLAS-FIG-INFO-001 | ATLAS-CH-INFO-001 | exact | 700x796 | VISUAL_REVIEW |
| ATLAS-FIG-REP-001 | ATLAS-CH-REP-001 | schematic | 1100x555 | VISUAL_REVIEW |
| ATLAS-FIG-NORMREP-001 | ATLAS-CH-NORMREP-001 | exact | 1100x555 | VISUAL_REVIEW |
| ATLAS-FIG-QUOTIENT-001 | ATLAS-CH-QUOTIENT-001 | schematic | 1100x465 | VISUAL_REVIEW |
| ATLAS-FIG-RESIDUAL-001 | ATLAS-CH-RESIDUAL-001 | schematic | 1120x755 | VISUAL_REVIEW |
| ATLAS-FIG-TRANSFER-001 | ATLAS-CH-TRANSFER-001 | schematic | 1120x268 | P2: VERY WIDE; check legibility |
| ATLAS-FIG-DYN-001 | ATLAS-CH-DYN-001 | exact | 1160x400 | VISUAL_REVIEW |
| ATLAS-FIG-NUMERICS-001 | ATLAS-CH-NUMERICS-001 | data-derived | 1160x384 | VISUAL_REVIEW |
| ATLAS-FIG-ARCHHIST-001 | ATLAS-CH-ARCHHIST-001 | schematic | 1120x508 | VISUAL_REVIEW |
| ATLAS-FIG-TRANSFORMER-001 | ATLAS-CH-TRANSFORMER-001 | schematic | 1240x363 | VISUAL_REVIEW |
| ATLAS-FIG-OPTBASE-001 | ATLAS-CH-OPTBASE-001 | exact | 1160x6759 | P1: EXTREME PORTRAIT; inspect and regenerate |

## Substantive tasks (agent-executable)

1. Compare the 18 figure masters with Wolfram generators, exact source
   manifests, chapter claims and the compiled PDF. Require an explicit
   correct / revision-required / uninspected judgment for each figure.
2. Reconcile numerical labels, axes, ranges, styles, grayscale distinctions,
   mathematical typography and print legibility. Compare literal and
   nonliteral semantics, and the individual manifest claim boundary.
3. Replace insufficient caption-derived HTML alt text with descriptive
   semantics including trend/structure. Check zoom and links.
4. For ATLAS-FIG-OPTBASE-001 master dimensions are **1160x6759**.
   Contact-sheet inspection shows three panels squeezed into a very long
   predominantly empty canvas: confirmed layout defect. Regenerate from
   the pinned Wolfram source or separately document an exact alternative.
   Validate the three components, revise provenance, replay PDF and HTML.
5. Separately attribute an oversized-float warning outside Part I.
6. Harden 17 source Markdown figure paths after verifying rendered figures.
7. Bind reviews to the corrected exact revision; agents may review and fix.
   A separate checker validates results, but no reviewer thereby gains
   authority to promote research claims or publish a release.

**Next statuses:** all 18 figures NEEDS_VISUAL_SEMANTIC_REVIEW; OPTBASE
also requires P1 layout repair. This is an agent work queue, not an
external-human-review waiting room.
