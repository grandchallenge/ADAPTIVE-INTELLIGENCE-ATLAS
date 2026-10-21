# ATLAS #405: Local-to-Global mathematical display repair

**Status: producer mathematics and physical-render pass; independent critic not completed.**

Original history: [#327](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/327#issuecomment-6057807495).
Parent acceptance review: #405. Original P02-B correction [PR #346](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/346) was merged into PR #320's historical workbench. This successor corrects a still-visible issue: mathematical material escaped as source-code text.

## Scope

- Branch parent: producer Krylov PR #408, head 17aa3e8999d566c28557118863ab2517fea3df61. This change is stacked; PR #408 is not yet admitted to PR #320.
- Chapter: manuscript/parts/02-mathematical-substrate/ATLAS-CH-LOCALGLOBAL-001.md.
- Convert 68 historical code-style spans into 49 standalone and 19 inline mathematical expressions. Move 29 punctuation marks inside display math, eliminating orphan periods after Pandoc conversion. Regenerate complete RC2 TeX from canonical source, retaining 80 chapters, 2,971 LaTeX labels and 18 figure placements.
- Do not alter immutable public v0.1.0, any source lock, theorem premise, witness data or cited bibliography.

## Mathematical witness and producer QA

Five tests in tests/test_localglobal_math_typesetting_405.py pass. They independently establish typed restriction composition, injectivity of R from real three-space to real four-space, image(R)=kernel(Delta), exact glue of (1,2) and (2,4), and nonzero obstruction for boundary values 2 versus 3. These are finite examples and not a substitute for a general sheaf theorem.

## Actual same-source physical rendering

- RC2 LaTeX SHA-256: f78ca180556e6c87f64f6551d430128741c7505ece5fd0f570134aedd498caa0.
- Three successful PDF passes, 1,426 physical pages, SHA-256: 7e9748ee4fdc45c75289e7080bc1c0ff41e8a08fdc4269e31222ea605edefbfe.
- Embedded MathJax HTML SHA-256: 132efafefddb5d509c3356d50162d1abaa4a7488ed7c5ed2e27c49d6182e51fe.
- HTML 5,908 unique of 5,908 IDs; 18 figure embeddings and 18 semantic descriptions matched to source figure digests.
- Isolated TeX Live extra distribution overlay used for missing truncate.sty; no source or system package workaround.
- The first PDF showed 29 stranded punctuation marks. These were corrected, rebuilt and final page 227 rasterized and inspected. No orphan period remains in that inspected page.

## Acceptance gate

A different accountable critic run must inspect the complete present Local-to-Global chapter, physical PDF pages beginning at 219, source-derived HTML, mathematical maps and sheaf axioms, link and citation semantics, legibility and overfull regressions. Critic must bind exact commit and artifact SHA-256, declare precise findings and complete corrections. Historical P02-B heading consolidation is NOT discharged by a notation repair.

No final critic verdict or chapter acceptance is implied; #405 remains zero independently signed-off chapters.
