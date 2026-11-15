# OWI-DS-002: historical external DeepCoder search semantics gate

Research issue #483. Source and experimental candidate only; no scientific promotion or protected admission until exact-head replay and review.

Microsoft DeepCoder-Utils is the historical ICLR 2017 C++ enumerative search utility. It is archived, unmodified in this experiment, and source-locked to commit 794057dc41aab0bea3818b75416da06b25aff12f with six selected code/prior Git blob checks. It is an external independent search implementation, not a contemporary state-of-the-art DeepCoder solver.

**Substantive mismatch:** Historical C++ integer division truncates toward zero; pinned 2024 ExeDec uses Python floor division. Historical empty Head/Last and out-of-range Access return numerical values where ExeDec execution is undefined. Negative Take/Drop also differ. These are semantic incompatibilities, not cosmetic syntax mismatches. Therefore historical C++ Solved! is never by itself a verified ExeDec solve.

The source-blind adapter accepts only the participant I/O view, converts exact three examples to C++ input/output text fixtures, and generates seeded task-independent operator-order weights. Original C++ emits candidate programs; the adapter uses a strict operation map, rejects unsupported or malformed outputs, and independently verifies every emitted typed ExeDec candidate against the pinned #493 verifier (published examples and 16 evaluator-only valid inputs). Historical source code executes only in a disposable GitHub Actions runner, with a hard subprocess wall timeout and 512 MiB address-space cap. No private model input, gradients, target program or evaluator counterexample is passed to the solver.

The preregistered pilot runs six published structural splits, two fixed task indices per split, five search-order seeds, maximum four solver steps, 1.5-second worker wall cap. It retains all 60 outcomes, including timeouts and incompatible candidates. Scope is diagnostic; worker time plus whole-script wall time are reported, without physical FLOP accounting or equal A/B/C/D budgets.

The source-semantic mismatch precludes treating the original tool as a semantics-identical mature reference, even if the bounded diagnostic succeeds. A fully conforming strong external solver or independently justified compatibility transformation remains an open scientific obligation.
