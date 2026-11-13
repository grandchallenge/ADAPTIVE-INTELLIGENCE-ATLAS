# OWI-EC-005B — From Binary-Majority Repair to Real Tool-Using Agents

**Grand Challenge Labs · 2026-11-13 UTC**  
**Parent:** [OWI-EC-005 issue #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466), [conditional implementation PR #467](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/467).  
**Status:** source-verified experiment design and real-environment intake gate; **no positive outcome-only empirical result**. This is not an Atlas chapter, an admitted scientific theorem, or a revision of release authority.

## Diagnosis: why the previous example is too forgiving of indiscriminate repair

The two-branch, nine-symbol majority problem has essentially no useful semantics beyond two small output bits. Its pretrained GRU is near-perfect on clean data; replaying the final suffix of both branches costs just 0.07 normalized loss units, and its measured end-task loss after repair is small. With perturbation prevalence 0.8, always repairing both is an unusually competitive solution. There is insufficient diversity in information needs, task difficulty, delayed credit assignment or conditional re-planning.

In the five-seed outcome-only EC-005 replay, active and passive actors both converged to the same charged objective (0.077862817), while fixed-both achieved 0.072862814. They did not meaningfully exploit the probe outcome; active paid an extra controller charge. This is an **observed failure of that learning algorithm in that environment**, not a theorem that online introspective learning is impossible.

Simply increasing hidden width, sequence length, corruption severity or the number of independent seeds may leave the basic defect intact. In particular, more severe corruption might *strengthen* the always-repair policy. The next discriminating experiment should therefore change the **decision problem**, not merely its size.

## Recommended scientific object: a real, stateful tool-using language agent

Use reproducible multi-turn tasks with executable tool APIs, state-dependent consequences, user corrections, and verifiable terminal success. The agent forms a plan, makes real calls, sees partial/noisy responses, and may choose **stop**, **inspect**, **retry**, **replan** or **escalate**. Tools have heterogeneous time/token/compute costs and may return misleading success messages, timeouts, state corruption, or failures with delayed visible consequences. Some clean tasks should *not* justify additional verification.

Unlike binary-majority repair, these decisions require an agent to maintain a working hypothesis about what its own actions accomplished. For example: a retrieved record can be correct, stale or incomplete; rerunning the same lookup may recover transient failure but waste time under a persistent fault; obtaining independent evidence costs extra; submitting without verification sometimes succeeds and sometimes loses a long task. Genuine introspection must improve **the agent's own future choices** as a function of its own trace, not merely classify a pre-labelled fault.

The closest open research resource is the [Agent-Reflex repository](https://github.com/RUC-NLPIR/Agent-Reflex), whose [RL task corpus](https://huggingface.co/datasets/dongguanting/Agent-Reflex-RL-2K) publicly describes 2,550 executable tool-use tasks with final environment-state checkers. The authors use reflection skills, supervised trajectories and on-policy skill-guided distillation; their *published success is not evidence for our outcome-only hypothesis*. We intend to reuse **only the task environment and private final verifier**, removing `rsd_skill`, `rsd_skills`, `rsd_skill_meta`, reference actions, and all verifier targets from the learner's observable state and training labels. External code must execute only in a constrained, vetted, nonprivileged container without host secrets or unscoped network writes. An intake script must **never** execute an environment.

As additional external measurement, [ReflecTool-Bench](https://aclanthology.org/2026.findings-acl.86/) distinguishes third-party critique from own-trajectory self-reflection over 968 multi-turn tool-use dialogues. It provides an appropriate *detection* and *correction* diagnostic but does not alone supply on-policy action effects. A second phase may evaluate actual code-repair work using the 23 development tasks from [SWE-bench Lite](https://www.swebench.com/lite.html). Its Docker-based full harness is substantially more resource intensive (the official documentation recommends at least 120 GB available storage and 16 GB RAM); do not pretend a synthetic tool simulator is a SWE-bench result.

## Executed source and structural audit (read-only, not agent performance)

At [source-intake run 43383816390](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43383816390), the complete **159,084,981-byte** external JSONL file was read as untrusted data and hashed against pinned revision `337c7eebaa3fd56825602d7252000c55a62e27f3`, raw SHA256 `3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a`. Both a Python-syntax AST audit and the source-isolation tests passed without executing a third-party class body.

Measured structure: 2,550 task records, exactly 5 fixed environment metadata fields per record (`env_id`, `class_name`, `class_code`, `initial_state`, `tools`); **51 distinct environment IDs** rather than 2,550 independent environments; **45,600 declared function tools** across task records (12–25 per task); 73,311,750 bytes of recorded Python class source; verifier `checklist` and `kind` in every record; and reflection-skill fields in all 2,550 records. Common tool names include account lookup, patient lookup, appointment updates and other stateful database-style operations. These are genuine environment definitions, not evidence that our model executed any task.

**Transfer consequence:** random task-level splits would share environment implementations across training and testing. The source-locked split constructor unions environment IDs with identical class-code hashes, then partitions whole connected families; it asserts no shared environment identity, executable class body, or public prompt across train/dev/test. Held-out intervention mechanisms and held-out domains still require separate controlled randomization. The split numbers and environment-family sizes must be read from the exact-head split artifact, not inferred from the existence of 51 distinct IDs.

**Executed grouped split:** [run 43384172025](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43384172025) confirmed 51 distinct executable class bodies, each reused in exactly 50 tasks. The source-locked partition seed `4611` produced **train: 30 environment families / 1,500 tasks; development: 10 / 500; test: 11 / 550**. The automated overlap audit passed for public prompt fingerprints, environment identity and class-code SHA256 across all three partitions. This isolates distinct tool implementations across the splits, though it does not establish isolation from common natural-language task templates or pretrained-model contamination. No solver has yet executed on these partitions.\n\nThis corpus supplies a more relevant scientific object but introduces a clear safety and validity boundary: executing arbitrary third-party `class_code` requires a vetted nonprivileged, network-isolated tool sandbox. Parsing the code as AST does not grant its execution authority. Similarly, removing declared `rsd_skill` fields does not automatically prove that no analogous privileged information was copied into natural-language prompt text; prompt-content concordance remains a distinct audit before policy training.

## Enforced information boundary

Separate **agent view**, **environment executor**, and **terminal verifier** as distinct interfaces. The learner may observe only the task messages, explicitly approved tool schemas, its own past actions, actual tool replies, elapsed/compute cost and final scalar environment outcome. The hidden simulator state, verifier checklist, source reflection skills, gold trace, fault type, and unchosen action results are prohibited in policy inputs, optimizer targets, model context, W&B training records, and actor/critic baselines.

The first executable intake, `experiments/owi_ec005_realtools_intake.py`, implements this separation for public prompts versus all `extra_info` private fields, records source identity/byte hashes and schema, checks record bounds and refuses unknown public message structure. It never imports/executes third-party environment source. Its adversarial test inserts a unique sentinel in tool code, private state, verifier, and skill fields, and proves that the public view and printed inventory contain none. This is a **source-isolation preflight**, not yet a trusted executable environment adapter.

Before any on-policy training, separately audit that the approved public tool schema really contains no callable body, hidden initial state, answer-key field or protected metadata. There must be no convenience Python object that provides policy code with direct access to the private verifier. A policy-facing `step(action)` process should receive only a sanitised returned observation; `settle()` must return one terminal scalar score and realized charges, not alternate-action outcomes. Execution must sandbox untrusted dataset tool code, enforce per-action timeouts, and log provenance/sha hashes. Refuse live training if the source cannot be made to satisfy this contract.

## Identification and learning design

A trajectory is \(\tau=(o_0,a_0,o_1,a_1,\ldots,o_T,r_T,c_T)\), where \(o_i\) contains the **actual** tool feedback, \(a_i\) is the selected action and \(r_T\) is the terminal task outcome. Optimize a preregistered expected objective, for example

\[
J(\pi)=\mathbb E_\pi[\mathbf1\{\mathrm{task\ failed}\}
 + \lambda_{\mathrm{tool}} N_{\mathrm{tool}}
 + \lambda_{\mathrm{token}} N_{\mathrm{tokens}}
 + \lambda_{\mathrm{wall}} T_{\mathrm{wall}}],
\]

with heterogeneous tool-specific prices measured from execution, not guessed proxy savings. Report the entire success–cost Pareto frontier and fixed-budget success; a scalar preference should not conceal materially worse task success.

A practical first controller is a small *separate* action-value head over the frozen language agent's trace features, trained using randomized **chosen** verification actions and their realized terminal outcomes (epsilon-supported on-policy actor-critic, or a well-defined contextual-bandit estimator for frozen downstream control). This separates whether information is learnable from whether costly end-to-end language-model training is effective. A second experiment may train a LoRA-adapted policy using group-relative outcome rewards, but cannot use reflection skill supervision, gold trajectories, the verifier's hidden checklist, or privileged counterfactual labels. The choice of offline trajectories alone is **not** an on-policy outcome-only result.

For first-stage active causal identification, randomly assign one allowable probe at a bounded decision point with full logged propensity, freeze the downstream policy, and compute inverse-propensity / doubly robust *population* contrasts only if overlap and ESS are adequate. These identify the effect of actually selecting that probe under the frozen continuation policy. They do not reveal unobserved individual counterfactuals. After a successful randomized intervention preflight, train and evaluate truly adaptive policies on fresh task instances.

## Matched comparisons and falsifiers

- **No-reflection**: freeze the same base agent and forbid extra verification or recovery.
- **Always-verify/always-retry**: same base agent, systematic costly verification.
- **Matched budget**: same maximum model calls, tool actions, tokens, and elapsed-time envelope.
- **Passive telemetry**: same trace features and control overhead, but no active verification choice.
- **Zero/shuffled feedback**: preserve the action and its cost while removing/misaligning the actual probe information.
- **Oracle upper bound**: offline evaluator may inspect hidden state to estimate an upper bound; it must never train the learned policy.
- **Negative-control tasks**: clean/low-risk tasks where probing should be declined.
- **Cross-mechanism/domain holdout**: withhold entire tool-error families and tool schemas, not merely new examples of the same corruption.
- **Interference, delayed errors and persistent damage**: transient timeout versus persistent bad state, contradictory records, two simultaneous faults and unrecoverable checkpoints.

Use 5+ independent model and policy seeds, split by underlying environment/tool family, prevent near-duplicate task templates from crossing splits, and report uncertainty with cluster-aware or task-stratified intervals. Record full token counts, tool calls, tool time, wall latency, GPU utilization/peak allocated memory where applicable, and the actual chosen intervention propensities and delayed outcomes. W&B runs, CLI arguments and exact model/data hashes must be retained.

The primary success criterion remains issue #466: **one outcome-only controller** that beats both passive and fixed intervention policies on *terminal task outcome plus physical computation cost* out of sample, survives zero/shuffled-information controls, and improves under at least one unseen intervention mechanism across repeated independent seeds. Positive evaluation on the original binary-majority task is neither sufficient nor required for this new external-validity test.

## Staged executable programme and current boundary

1. **Source intake (this PR):** read the real 2,550-task source as untrusted data, pin immutable dataset commit and raw-file SHA256, inspect schema/hidden-field inventory, prove private/public separation without executing environment code, and retain a safe JSON evidence artifact.
2. **Executable env preflight:** inspect several real task schemas, implement sandboxed tool execution and final verifier IPC; demonstrate actual state transitions and nonleakage through a small set of authorized, reproducible tasks. No privileged debug fields in the learner.
3. **Frozen agent & randomized action identification:** demonstrate positive intervention support and variance/ESS, compare selective probe vs no probe and fixed always-probe at matched actual tool and inference cost.
4. **Five-seed outcome-only policy training:** with W&B, single-GPU early tests when feasible; persist action-level trajectories and check for no-probe learning, transfer and conditional abstention.
5. **Independent replication / second domain:** tool-use held-out mechanisms first, then source-pinned real repository repair (SWE-bench Lite development subset) after feasibility and container capacity are demonstrated.

This note records a substantive change of experimental object and a reproducible provenance gate. It claims **no** measured success, no emergent sapience/consciousness, and no modification to the 80-chapter Atlas manuscript, release ledger, or mathematics-certification authority.
