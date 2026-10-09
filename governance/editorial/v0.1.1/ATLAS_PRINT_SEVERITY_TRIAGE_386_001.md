# Atlas print warning severity inventory — WP386 / pass 1

**Evidence status:** measurement and triage, **not** print acceptance, chapter certification or a publisher's proof.  
**Current corrected-edition predecessor:** `editorial/part01-corrections-20261008@213ea1614dc490e851d59df8a786bbedc3102d51` (PR #320).  
**Comparison baseline:** `b3c484a68e54808ee2ff58e6d4c0c5680763a394` before the MAP worked example and EVIDENCE packets.  
**Reproducible full three-pass LaTeX comparison:** [Actions run 37907478148](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/37907478148), emitted by `tools/atlas_print_severity_audit.py` using exact source/TeX filenames and the canonical `governance/CHAPTER_LEDGER.yaml`. Both input revisions compiled successfully.  
**Scope:** 80 chapters; this pass measures TeX `Overfull \hbox` lines and associates warnings with TeX chapter boundaries, nearest TeX section and source path. It does not substitute for a rendered-page inspection.

## Validated counts

| Metric | Earlier physical candidate | Current candidate |
|---|---:|---:|
| All TeX overfull hbox warnings | 965 | 969 |
| Maximum reported excess width | 245.8541 pt | 245.8541 pt |
| Warnings with unambiguous TeX line reference | 794 | 797 |
| Warnings with no source TeX line (LaTeX says *while output is active*) | 171 | 172 |
| Warnings missed by the generalized warning regex | 0 | 0 |

**Interpretation:** the book has four additional warnings after the added MAP/EVIDENCE material. Do **not** claim all four were caused by the tables: source line counts, section wrapping, and LaTeX output-routine warnings complicate attribution. The initial per-chapter delta superficially assigns +64 to OBJECTS and -61 to EVIDENCE because relative paragraph references shift around page/layout changes. Those large local deltas are *not* evidence of a corresponding new mathematical or typographic defect count. The diagnostic has been strengthened to compare source-neighborhood/width fingerprints rather than treating a changed line number as a new warning.

## Largest 20 mapped or reported warnings

These are **measured candidates for visual inspection and source-level repair**; “severity” here means geometric excess width, not yet demonstrated clipping. Warnings without a TeX line are explicitly marked unmapped.

| Rank | Width (pt) | Chapter | Canonical source / interpretation |
|---:|---:|---|---|
| 1 | 245.8541 | THESIS | `manuscript/parts/01-orientation/ATLAS-CH-THESIS-001.md` §10: unbreakable nine-stage reading itinerary boxed as display mathematics |
| 2 | 239.47325 | ARCHHIST | `manuscript/parts/04-neural-architectures/ATLAS-CH-ARCHHIST-001.md` §1: seven-stage historical-pedagogical arrow chain |
| 3 | 220.13547 | ADAPTDEPTH | `manuscript/parts/07-numerical-intelligence/ATLAS-CH-ADAPTDEPTH-001.md` closing: prose-like six-ingredient "adaptive error control" box |
| 4 | 203.60474 | SYSTEMS | `manuscript/parts/13-agents-systems-hardware/ATLAS-CH-SYSTEMS-001.md` opening: long unbreakable distributed-cost qualification |
| 5 | 187.35562 | CONTEXTCOMP | `manuscript/parts/09-memory-beyond-weights/ATLAS-CH-CONTEXTCOMP-001.md` closing: unbreakable context construction qualification |
| 6 | 177.66154 | SPECTRALDIAG | `manuscript/parts/12-diagnostics-robustness-compression/ATLAS-CH-SPECTRALDIAG-001.md` closing: unbreakable operator/evidence qualification |
| 7 | 171.43835 | JOINTUNC | `manuscript/parts/11-decision-making/ATLAS-CH-JOINTUNC-001.md` closing: joint-uncertainty prose box |
| 8 | 166.13441 | NEURALKRYLOV | `manuscript/parts/07-numerical-intelligence/ATLAS-CH-NEURALKRYLOV-001.md` closing: four-step mathematical architecture in a wide box (distinct from closed #380 qualification) |
| 9 | 164.55151 | VARIOPT | `manuscript/parts/05-optimization/ATLAS-CH-VARIOPT-001.md` final architecture list box |
| 10 | 161.44017 | TRANSPORT | `manuscript/parts/04-neural-architectures/ATLAS-CH-TRANSPORT-001.md` closing: path-semantics chain |
| 11 | 150.16180 | COMPINTEL | `manuscript/parts/12-diagnostics-robustness-compression/ATLAS-CH-COMPINTEL-001.md` closing: code/split/control/retained-behavior prose box |
| 12 | 141.16008 | LATENTTIME | `manuscript/parts/05-attention-sequence-position/ATLAS-CH-LATENTTIME-001.md` closing: inferred latent-time meaning qualification |
| 13 | 131.44014 | NONNORMAL | `manuscript/parts/02-mathematical-substrate/ATLAS-CH-NONNORMAL-001.md` connection: boxed mathematical question |
| 14 | 113.96693 | COMPOSE | `manuscript/parts/07-numerical-intelligence-composition/ATLAS-CH-COMPOSE-001.md` closing: formal systems obligation text box |
| 15 | 108.22955 | UNLOCATED | Output-routine warning without source TeX line; cannot be attributed from this log alone |
| 16 | 107.39584 | UNLOCATED | Output-routine warning without source TeX line |
| 17 | 100.79817 | UNLOCATED | Output-routine warning without source TeX line |
| 18 | 100.14000 | SYSTEMS | Same source as #4, expert-parallelism display chain |
| 19 | 94.36205 | TRANSPORT | Chapter-opening layout or display; exact printed page needed |
| 20 | 86.70445 | UNLOCATED | Output-routine warning without source TeX line |

## Priority and bounded corrective policy

**P1 typography repairs:** the top 14 source-mapped warnings predominantly involve English prose forced into `\text{...}` inside a display/box. Replace those with *breakable explanatory prose*, or a genuinely meaningful short aligned mathematical formula where one exists. Preserve conditions and counterexamples. In particular, a claimed “definition” presented with equality signs must not silently become a theorem by being typeset in a box.

**P1 figure/page inspection:** warnings during `\output` are currently unmapped (172 occurrences); investigate using logged page boundaries, PDF crop/visual rendering, and page-level text extraction before attributing them to canonical source chapters.

**P2 newly introduced warning signatures:** use the strengthened warning-fingerprint replay to distinguish changed lines/reflow from genuinely new warnings. Do not rely on naive per-chapter count differencing.

**P3 quality discipline:** not every 1–5pt overfull is a real clipping defect, but the 100–245pt spans warrant print scrutiny. Perform final mathematical critical review separately from mechanical PDF success.

**Next scope:** repair the highest-width mapped prose boxes, replay complete 80-chapter/2,971-anchor/18-figure PDF+HTML output, inspect actual printed pages, merge the bounded repair to the mutable corrected-edition workbench only with critical-role evidence and exact-head checks. No change to protected public v0.1.0; chapter final acceptance remains open.

## Recovery and evidence

- Issue [#386](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/386).
- Temporary [PR #388](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/388) carrying the reusable `tools/atlas_print_severity_audit.py`.
- Editorial workbench [PR #320](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/320).


## Independent warning-signature comparison — second pass

[Run 37907941323](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/37907941323) replayed the same pinned baseline/current sources and passed generalized overfull parsing, again confirming **965 → 969**, zero unparsed warning headers and 171 → 172 warnings with no TeX source line. Comparing warning fingerprints by excess width and nearby TeX text (not unreliable shifted source line numbers) found **88 added occurrences and 84 removed occurrences**, a net difference of four. These are **reflow changes**, not 88 distinct newly introduced source defects.

Among the largest changed signatures are four `\\output is active` warnings of 50.04036pt in the later layout in place of four 45.04036pt warnings in the predecessor, plus numerous small (~4.49997pt) paragraphs whose location shifts between OBJECTS and EVIDENCE as the added support tables change pagination. The 245.8541pt top offender is unchanged. **There is insufficient evidence to attribute the net +4 exclusively to the new evidence tables**: identifying the exact printed page/box for the `\\output` cases remains a bounded physical-inspection obligation. No unearned claim of causal attribution is made.

The next authorized corrective subtranche may remove source-identified unbreakable English displays independently of that unresolved output-routine provenance; source/visual evidence must still close the unresolved page-level cases.
