# OWI-DS-002 — ExeDec executable-program admission gate (candidate)

**Governing issue:** #483. **Status:** candidate engineering gate; independent GCL review and protected admission outstanding.

## Why this source

The earlier official SyGuS 2017 ten-invariant cohort was saturated by cvc5 (10/10), and checked inductive SMT formulae, not execution of synthesized programs. This candidate adds a separate, genuinely executable reference corpus: Kensen Shi et al., *ExeDec: Execution Decomposition for Compositional Generalization in Neural Program Synthesis* (ICLR 2024), Google DeepMind [source repository](https://github.com/google-deepmind/exedec/tree/ef046ce2cc3fcd024e32f5dfe00e69700dac82ed). Source code is Apache-2.0; datasets are CC BY 4.0.

**Source lock:** Exact upstream commit ef046ce2cc3fcd024e32f5dfe00e69700dac82ed, six original data/llm_data/deepcoder JSONL Git-blob SHA1 identities in the local manifest, 200 published test problems per distribution (1,200 total), four train-distribution few-shot examples per problem. Upstream DSL semantics anchored to tasks/deepcoder/deepcoder_dsl.py, blob 8bc0db8516e132aef19c9ca85cbb0d5210a9c565. Originals are downloaded without alteration, hash verified before parsing, and replayed using an independently written, bounded DSL interpreter.

The six published distributions are NONE; LENGTH_GENERALIZATION; COMPOSE_DIFFERENT_CONCEPTS; SWITCH_CONCEPT_ORDER; COMPOSE_NEW_OP; ADD_OP_FUNCTIONALITY. They distinguish algorithmic compositional structures rather than a single-step synthetic repair policy. They are public test splits, not undisclosed scientific holdout data.

## Admission contract

The executable verifier accepts only x0–x9, typed integers / integer lists, upstream DeepCoder operators/lambda tokens, and at most ten total lines. It rejects untyped expressions, undeclared variables, unsupported calls, arbitrary Python, and out-of-range intermediate states. It never calls Python exec/eval.

It first replays upstream reference programs against the published I/O examples. A participant-facing projection includes examples but excludes target programs and few-shot solution programs. A submitted discrete program must match every published example, then agree with the source reference program on 16 deterministic, evaluator-only, fresh valid inputs; otherwise it receives a rejected or inconclusive status. These finite checks are stronger than just reusing the three published examples, but do **not** establish universal program equivalence. The reference program is publicly distributed; contamination prevention is procedural, not cryptographic.

A source audit demands six matching original file Git blobs, exactly 200 rows per split, all reference programs parsed and all their source I/O examples replayed. Tests and CI cover static type rejection, malformed candidates, illegal calls, bounds, negative-integer division, Scanl1 accumulation, deterministic probes, and exclusion of held-out target program fields from the participant projection.

## Mathematical boundary for C1

Full DeepCoder is not a smooth typed category: it uses integers and variable-length lists as well as sorting, filtering, indexing and predicates with discrete discontinuities. A JVP of a learned relaxation or surrogate is **not** a derivative of these discrete programs.

A legal differentiable experiment must specify separately a fixed-shape real-valued smooth submodule, its actual chosen-run input-output map, its directional derivative and a charged query API. It must prove the derivative pertains to the selected execution rather than an unexecuted counterfactual. No such bridge is implemented here. No C1/D evidence is claimed.

## Experiment plan and stop conditions

This module is **not** A/B/C/D synthesis, a solver win, a complete source-native industrial task or a proof assistant certificate. Following independent adjudication of the DSL semantics and exact-head six-split audit, the next executable step is a strong nondifferential baseline on the *same grammar and I/O*: ordinary enumerative search and an established external synthesizer where language support permits. Record actual unsolved headroom. Then freeze five-plus seed split manifests and all-in training/synthesis/probe/evaluation wall time, CPU/GPU cycles and memory budgets before any C1 experiment; apply mandatory shuffled-tangent and surrogate-only controls, paired verified solve rates, source- and OOD-generalization slices, calibration and negative-result reporting. Do not claim improved reasoning from surrogate regression or a synthetic C0 classifier.

**Explicit nonclaims:** general syntactic CDC derivative, introspection, causal identification, universal program equivalence, model-free independence of published target programs, or differential advantage.

**Admission state:** exact-head CI and independent role-separated review required; protected merge pending.
