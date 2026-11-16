# OWI-DS-002 — Source-pinned REAL pretrained LambdaBeam neural inference on exact ExeDec public I/O

**Parent:** OWI-DS-002 #483. Source pinned to original NeurIPS-2023 independent LambdaBeam repository ellisk42/LambdaBeam HEAD 61986dc1a6d8cc9521fb17e3152f7f085b5d7c95. ExeDec dataset pinned to ef046ce2cc3fcd024e32f5dfe00e69700dac82ed.

## Actual trained-model execution gate

Previous protected source and checkpoint work: #500 independently published original enumeration but **not trained neural inference**; #501 source-locks the original 40,750,571-byte pretrained checkpoint, Git blob SHA1 91ab03f94972f4f523dfaa771a45ea28583f519f, SHA256 969450bc6bdba3c7402a3bffd56b116b41a0d842979e4cc59412988561c38043, and confirms 28 original model per-operator-heads vs 38 atomic ExeDec operator instances. #503 admits a conservative 32/38 native program translator and reports 438/1200 published source references structurally eligible. #505 introduces an **explicit semantic adaptation** of the original Access and Scanl1 operator method edge behavior to match the full ExeDec atom vocabulary, preserving all original 28 model op-head names/indexes/binder signatures, tested in 671 cases with no observed mismatch, but not pretrained model execution.

This next tranche actually instantiates original NeurIPS-2023 DeepCoderModel at original published 28-operation learned-head cardinality; loads the original **actual published pretrained weights** under a fail-closed PyTorch weights_only deserialization restriction, using an exact pinned original blob and SHA256 identity check first. The checkpoint model state keys and tensor dimensions/dtypes/finite values must match the instantiated original architecture completely with strict=True. The optimizer is NOT loaded or executed. The reported checkpoint step and exact model tensor-key count are preserved.

The real original model computes LambdaSigIOEncoder and LambdaSigValueEncoder embeddings, per-operation initialization, and at least one genuine trained per-operation arg-selector score. It then invokes the ORIGINAL published neural synthesis.synthesize search algorithm for a preselected six-task pilot; native original expressions are compiled through the protected opt-in exact ExeDec semantic adapter and only exact public example agreement permits the independent source/evaluator-only 16-probe check. Every negative is preserved, with actual model forward, original generated string, translation result, verifier, resource counters, CPU/time/search budgets, and source SHA in machine-readable evidence. No reference program is passed into native trained search. Candidate metadata may be verified only after search.

## Configuration and bounded pilot, not equal-compute

Original model constructor sourced from original eval_config and configs_all: lambda_signature IO/value encoders, embed_dim=64, max_num_inputs=3, per-operator LSTM selector, score function mlp, normalized log scores, encode_weight=True. Run on Ubuntu CPU with pinned CPU PyTorch and original code, no GPU, seed=11. Preregister **index 0 from each of six published ExeDec splits**, one run per split (6 distinct source identities, not six independent seeds); first diagnostic used per-task 80 explored values and k/beam=2 (6 native tasks, 0 candidates, real checkpoint strict 365-key model, authentic step-205000 weights). Substantive replay uses per-task maximum 1000 explored values, nominal timeout 7s, k/beam=10, maximum weight 12, published unique-randomizer mode enabled, no stochastic beam, original synthesis method. Both configurations are recorded rather than conflated. No cherry-picking of tasks after evaluation; no artificial lower bound on successful tasks, no success claims before actual checkpoint inference. Small pilot checks capability, CPU resource use and compatibility failures, not a statistical rate.

The original upstream model import graph includes torch_scatter, but its **single-task forward and search path** uses only PoolingState and not batch_pooling; a strict imported stub raises if any off-path training batch scatter is used and the report requires zero calls. This avoids installing an ABI-sensitive torch_scatter GPU extension solely for an unused source import. This is an explicit runtime environment dependency substitution; it does not alter pretrained model tensors or neural search algorithms.

This is not an **unmodified original LambdaBeam** inference benchmark: Access and Scanl1 runtime are explicitly adapted to ExeDec definedness/bounds, though model 28-head ABI matches. The pretrained policy may be miscalibrated for the new semantics. The CPU task budgets and original training regime do not match previously reported original enumeration/GCL register compute. No equal-total-resource superiority or original best-known results may be claimed. Source public reference programs may overlap original model pretraining. Finite 16-probe candidate agreement is not formal or universal semantic equivalence. C1 selected-run JVP and D causal reflective mechanism remain separate and unresolved.

## Admission and evidence disposition

Require exact Git provenance for original source/weights, safe restricted deserialization, full actual model parameter key/tensor-shape match, and **real full checkpoint-backed model forward** before stating trained inference occurred. If safe loading, dependencies, source semantics or runtime fail: report REJECTED_OR_INCONCLUSIVE, not a fake neural result and not alternative enumeration. Exact-head CI, role-separated internal critical review, protected merge readback under PAAR, and original parent issue #483 remaining OPEN are required. Preserve all negative searches, source/compute/identity receipts in the CI artifact.


## Real checkpoint first executed diagnostic (not final substantive replay)

First candidate branch head f40a52fac46af6815a7cc68734ece42fd150e36d executed [GitHub Actions 43810491142](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43810491142), passing real strict 365-tensor-key pretrained model state load under torch.load(weights_only=True), trained checkpoint step 205000, six LambdaSigIO/Value/arg-head neural forward passes, and six original neural synthesis calls. This step completed in CPU PyTorch 2.5.1+cpu, original source Git pinned; all six source tasks index 0 returned no native candidate at shallow 80-value/beam2 budget, 80 successors explored each, total source search CPU 0.262s. No trained candidate could be translated or evaluator checked. Evidence artifact 14200326525 ZIP SHA256 edae2f52960979dc551152a12c37f0cad806e565e953a5a21171505b6be3a755.

This does NOT establish poor trained policy competence because the extremely shallow first-run search budget can trivially fail to reach relevant programs. The source-published eval_config.py uses use_ur=True, beam_size=10. Exact subsequent candidate revision therefore increases search to 1000 explored values and k10, with UniqueRandomizer true, preserves the same six task IDs and original checkpoint, and counts all resource use. No outcome-dependent task replacement or assumption that 1000 explored values constitutes comparable compute is permitted.


## Extended preregistered 5,000-exploration budget and neural synthetic mechanism controls

Published-mode intermediate run [43810644245](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43810644245) executed source-pinned actual trained step-205000 model on the same six fixed source tasks, beam 10 / original UniqueRandomizer / at most 1,000 successors per task. Exactly 1,000 successors were explored on each; zero native candidates, zero translated/evaluator candidates, and total measured source CPU 2.360 seconds (not full end-to-end cost). This is bounded negative evidence, not an adequate performance comparison to the different GCL enumeration/search algorithms.

The next complete exact-head test raises the budget once to at most 5,000 successors per task, 12s cap, same six identities, same model/checkpoint and inference configuration. Also adds two explicitly synthetic positive mechanism controls: a one-step Reverse and a one-step Sum public-input-only task, with independent 16 fresh exact ExeDec interpreter comparisons against their known target transformations. This gauges whether pretrained original neural search can emit a typed source-native expression and whether the opt-in adapter can independently verify a selected result. These controls are NOT held-out source benchmark tasks, and their target references never enter neural search. Their outcomes, whether success or negative, must be preserved. The CI workflow now cancels superseded runs on a PR head to avoid repeated CPU-wheel downloads after an obsolete branch update.


## Final preregistered real pretrained inference results

The original trained checkpoint CPU execution at candidate branch head c5fcb7ea7e67c343bd15da4e114229b919050265 completed with [actual trained-model workflow 43810871819](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43810871819), [adapted source regression 43810871810](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43810871810) and [Atlas validation 43810871799](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43810871799) all PASS. Source pinned LambdaBeam checkpoint step 205000, all 365 trained tensor keys, full original 28 operation-head architecture loaded with weights_only=True and strict=True. Authentic pretrained model forward and original trained neural synthesis executed; no substitution by random model or non-neural enumerator.

**Public ExeDec six-task pilot:** one a priori selected published index-0 task per split, maximum 5000 explored values each, seed 11, beam 10, original UniqueRandomizer enabled, nominal 12 seconds per task.

| Pinned split / task | Actual native trained solution | Explored | Search CPU seconds | Exact ExeDec verdict |
|---|---|---:|---:|---|
| NONE:0 | yes | 3014 | 1.7653 | strict translator rejects general lambda |
| LENGTH_GENERALIZATION:0 | no | 5000 | 2.8802 | no native candidate |
| COMPOSE_DIFFERENT_CONCEPTS:0 | no | 5000 | 2.9421 | no native candidate |
| SWITCH_CONCEPT_ORDER:0 | yes | 3870 | 2.3099 | strict translator rejects non-finite lambda expression |
| COMPOSE_NEW_OP:0 | yes | 3468 | 2.0400 | strict translator rejects generalized scalar/lambda expression |
| ADD_OP_FUNCTIONALITY:0 | no | 5000 | 3.0111 | no native candidate |

Original generated LambdaBeam expressions, reproduced verbatim as code lines below:

    NONE:0  Take(-1, Scanl1(lambda u1, u2: Last(x0), x0))
    SWITCH_CONCEPT_ORDER:0  Scanl1(lambda u1, u2: Subtract(4, Last(x0)), Reverse(Scanl1(lambda u1, u2: 0, Sort(x0))))
    COMPOSE_NEW_OP:0  Scanl1(lambda u1, u2: Multiply(2, Subtract(Add(x0, -1), Square(x0))), Sort(x1))

These three native-source programs matched their source-public I/O under the original trained search but are NOT legal ExeDec fixed-lambda grammar programs. No source target reference or evaluator probe was used to rewrite any native result. Therefore outcome is **three genuine native solutions from six published tasks, zero typed-translated ExeDec benchmark candidates, zero benchmark results admitted to independent 16-probe checks**. Total trained search CPU 14.9486s, excluding full model load/setup/runtime accounting. Source-public benchmark programmes are not confidential heldout.

**Separate synthetic mechanism controls (NOT ExeDec benchmark tasks):**

| Synthetic task | Genuine model-generated native expression | Explored values | Search CPU seconds | Exact independent fresh-input comparison |
|---|---|---:|---:|---:|
| Reverse | Reverse(x0) | 1473 | 0.82267 | 16/16 |
| Sum | Sum(x0) | 1593 | 0.88869 | 16/16 |

The original pretrained model generated both native expressions; each was automatically translated to exact ExeDec, then independently compared with a precommitted simple semantic function on 16 fresh inputs. Synthetic control reference programmes were NEVER passed to neural search, only the I/O examples. This demonstrates a nontrivial actual checkpoint-trained search-to-ExeDec-verifier positive-control path, not a benchmark win, hidden-heldout rate or universal program proof.

**Source/record custody:** Machine-readable six-task and two-control receipts are retained in [artifact 14200566448](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43810871819/artifacts/14200566448); ZIP SHA256 11be50d98133b6677d8360106d0250d14e0d11f5db904cf2d7c9d22dc679f461. Earlier 80- and 1000-value diagnostics remain individually preserved rather than overwritten. Updated workflow-level concurrency cancels superseded runs to reduce repeat CPU-wheel installs on subsequent commits.

**Technical disposition:** ACTUAL_PINNED_PRETRAINED_NEURAL_INFERENCE_EXECUTED__TWO_CONTROL_PROGRAMS_VERIFIED__GENERAL_LAMBDA_EXEDEC_TRANSFER_BLOCKS_3_PUBLIC_CANDIDATES. The learned source-native model supports general input-capturing and nested lambdas, while ExeDec only admits finite fixed-lambda tokens. A full 38/38 operator-name semantic adaptation does not resolve this source-language representational mismatch. Further blind budget increases do not solve the translation problem. Next: a source-blind, mechanically checked exact-grammar semantic reduction of selected learned native expressions when possible, or appropriate fixed-lambda-constrained training; keep equal-total-compute A/B/C/D, legal C1 JVP, and D causal self-model OPEN. Do not promote as a six-task trained benchmark success; actual exact ExeDec verified benchmark solutions were 0/6.
