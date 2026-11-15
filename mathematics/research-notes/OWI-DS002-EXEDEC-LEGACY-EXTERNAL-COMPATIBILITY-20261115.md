# OWI-DS-002: historical external DeepCoder search semantics gate

Research issue #483. Source and experimental candidate only; no scientific promotion or protected admission until exact-head replay and review.

Microsoft DeepCoder-Utils is the historical ICLR 2017 C++ enumerative search utility. It is archived, unmodified in this experiment, and source-locked to commit 794057dc41aab0bea3818b75416da06b25aff12f with six selected code/prior Git blob checks. It is an external independent search implementation, not a contemporary state-of-the-art DeepCoder solver.

**Substantive mismatch:** Historical C++ integer division truncates toward zero; pinned 2024 ExeDec uses Python floor division. Historical empty Head/Last and out-of-range Access return numerical values where ExeDec execution is undefined. Negative Take/Drop also differ. These are semantic incompatibilities, not cosmetic syntax mismatches. Therefore historical C++ Solved! is never by itself a verified ExeDec solve.

The source-blind adapter accepts only the participant I/O view, converts exact three examples to C++ input/output text fixtures, and generates seeded task-independent operator-order weights. Original C++ emits candidate programs; the adapter uses a strict operation map, rejects unsupported or malformed outputs, and independently verifies every emitted typed ExeDec candidate against the pinned #493 verifier (published examples and 16 evaluator-only valid inputs). Historical source code executes only in a disposable GitHub Actions runner, with a hard subprocess wall timeout and 512 MiB address-space cap. No private model input, gradients, target program or evaluator counterexample is passed to the solver.

The preregistered pilot runs six published structural splits, two fixed task indices per split, five search-order seeds, maximum four solver steps, 1.5-second worker wall cap. It retains all 60 outcomes, including timeouts and incompatible candidates. Scope is diagnostic; worker time plus whole-script wall time are reported, without physical FLOP accounting or equal A/B/C/D budgets.

The source-semantic mismatch precludes treating the original tool as a semantics-identical mature reference, even if the bounded diagnostic succeeds. A fully conforming strong external solver or independently justified compatibility transformation remains an open scientific obligation.


## Exact-head paired external versus GCL pilot — 15 November 2026 UTC

**Evidence class:** experimentally executed original source plus independently rechecked candidate outputs, not semantics-aligned solver equivalence or independent scientific certification.

The [source-locked historical C++ run 43713009374](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43713009374) passed at candidate head 5c94d27411499eb8de8c98bdf99dfac01c59407e. The study ran on six ExeDec structural splits with indices 0 and 17, search-order seeds 1–5 (60 paired trials, **12 distinct task identities**), historical maximum four operations, 1.5-second subprocess wall caps, and strict post hoc original ExeDec checking. The identical task/seed set was run by the protected GCL bounded enumerator at maximum four expression nodes, 15,000 attempted expressions and width 600, without target-program access. Archived JSON receipts for each tool and their paired join are retained in artifact 14161067097, archive SHA256 aff4483419d2c89eeb83c3481d72431a293b8d8731acf444b4859e0dc9635c4f.

| Adjudicated measure | Count |
| --- | ---: |
| Historical C++ claims Solved! | 59 / 60 |
| Historical C++ claims accepted by independent ExeDec checker | 50 / 60 |
| Historical C++ candidate failures on published ExeDec I/O | 9 / 60 |
| Historical C++ subprocess timeouts | 1 / 60 |
| GCL local bounded-verified | 44 / 60 |
| Both independently bounded-verified | 38 / 60 |
| Historical only independently bounded-verified | 12 / 60 |
| GCL local only independently bounded-verified | 6 / 60 |
| Neither independently bounded-verified | 4 / 60 |

The nine mismatches are not silently converted to passes. The original C++ semantics are demonstrably nonidentical to ExeDec for negative integer division, empty lists, out-of-range access and negative slicing, although the nine individual counterexamples have not all been categorized by the precise operator responsible. They could also reflect adapter or historical implementation limitations. The independent checker outcome, rather than the historical tool's own success text, is the admitted bounded behavioral evidence.

**Compute and interpretation:** The sum of historical search subprocess wall times was 3.895 seconds; the GCL enumerator's end-to-end script CPU time was 3.516 seconds, with 147,505 attempted expressions. These numbers have **different timing boundaries** and omit compilation, source acquisition, environment provisioning and independent checker costs in different ways. They are not equal-full-compute evidence. The 60 paired records are not independent because five seeds rerun each of 12 task identities. Historical solver execution and the GCL enumerator also have different search semantics and pruning rules. Do not infer a statistically established +6-task improvement, a validated strong solver advantage, or differential reasoning from the descriptive 50/60 versus 44/60 counts.

**Disposition:** HISTORICAL_EXTERNAL_COMPARATOR_EXECUTED__NINE_SOURCE_SEMANTIC_REJECTIONS__SCIENTIFIC_ADMISSION_WITHHELD. This diagnostic is meaningful evidence against treating cross-version solver claims as interchangeable. Further work must establish a conformant external semantics-adapted baseline (or another compatible contemporary solver), rigorous source-native correctness and equal-total-compute matched comparisons before C1/D scientific adjudication.
