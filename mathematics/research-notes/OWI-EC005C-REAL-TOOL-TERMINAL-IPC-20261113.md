# OWI-EC-005C — Real tool IPC and private terminal reward

**Grand Challenge Labs — 2026-11-13**  
**Parent:** [OWI-EC-005 #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466)  
**Status:** bounded intervention and terminal-reward engineering candidate; scientific learning result not established.

## Problem and boundary

PR #467 reproduced an empirical negative result: outcome-only active and passive recurrent policies both achieved 0.077862817 mean cost against 0.072862814 for fixed repair-both. PR #468 established the first real no-network external tool invocation and verified a source-locked EnvScaler dataset of 2,550 tool tasks and 51 reusable executable environments. This third tranche tests the **missing connection** between an actual chosen tool intervention and a *terminal private task verifier*.

The data source remains pinned to revision 337c7eebaa3fd56825602d7252000c55a62e27f3 and raw SHA256 3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a. The source-locked 30/10/11 environment-family split and all 80 Atlas chapters remain unchanged.

## Operational model

A trusted source selector downloads and hashes the complete pinned data before exporting three separate ephemeral payloads:

1. Public policy information: task messages, function signatures, and an eligible read-only probe name. No hidden state, executable class source, private checklist, answer key, or RSD skill.
2. Restricted environment worker: class source, initial state and tool schema in a nonroot, read-only, no-network Docker process. It executes exactly the selected tool calls, preserving state within one episode. It emits actual tool observations and, upon termination, a *private* post-constructor initial/final state snapshot to the trusted bridge.
3. Independent restricted verifier process: only the private checklist and the two snapshot states. The check programs are executed inside this second container; the result is one terminal scalar reward plus aggregate pass/count and validity indicators. Neither its source nor expectations are sent to the tool worker or policy.

The terminal-check protocol follows the [official Agent-Reflex EnvScaler adapter](https://github.com/RUC-NLPIR/Agent-Reflex/blob/main/ORPO/recipe/envscaler_openai_fc/adapters/envscaler.py): each checklist program defines check_func(final_state) with a post-constructor initial_state global. An actual boolean is required. Unlike the upstream adapter, a failed or nonboolean check program makes the **entire terminal measurement invalid** rather than silently treating an evaluator error as failed task behavior. This is conservative and must be kept visible in interpretation.

The Python host orchestrator is trusted and necessarily transports private state between processes; there is no claim of hardware-enforced information isolation. Data is withheld from the policy-facing view; external code never runs on the host and the independent containers have no network access, host credentials, or writable host bind mounts.

## Randomized first-stage experiment

On one pinned real task (source row index 1) reset the environment independently for each episode. A reproducible random seed samples one of three actions with precisely logged probability 1/3: stop without tool calls, call one declared read-only tool, or call that tool twice. Only selected calls are actually executed and charged; no unchosen interventions are evaluated in the training path. The separate private verifier evaluates every resulting terminal state after the episode finishes.

Because all three interventions are intentionally **read-only**, they are a falsifiable negative control for reward-pipeline fidelity, not a credible mechanism for improving task completion. The expected observation is no task-state change; discrepancies reveal hidden side effects or verifier instability. The task is repeated for a plumbing smoke, not used for held-out accuracy claims or policy training.

Save chosen action and propensity, realized selected tool reply hash, actual tool time, child process RSS, environment and verifier wall time, aggregate terminal reward, check count and actual tool-call count. Remove private state hashes from published per-episode records after evaluating equality across arms. No skill/checker code, private state or individual target is retained. A green CI status proves implementation and transport, not emergence of useful introspection.

## Required validation

Adversarial tests exercise trusted state-changing fixtures, correct post-constructor snapshots, absence of verifier/source in the public view, missing/verifier-error invalidity, no-action abstention, and deterministic support for all three randomized arms. A separate GitHub Actions job runs the actual source-locked task in two separately jailed processes and retains only nonprivileged, bounded evidence. Protected merge requires the final head's required Atlas validation and the real live reward-loop job to pass.

## Remaining scientific programme

- Add an independently verifiable **goal-directed mutating** action, not merely read-only probes, and measure causal improvement against no-action.
- Make a second intervention depend on actual received tool observation, rather than a precomputed schedule.
- Train a language-agent or small frozen-model action-value controller using **only chosen realized scalar outcomes**, log exploration support and learning propensity, and compare fixed/always-probe/passive matched-compute baselines.
- Evaluate across 5+ seeds, source-disjoint environments and held-out fault mechanisms with actual token/compute/time measurements, W&B, and adversarial verifier/skill leakage tests.

**Scientific status:** OUTCOME_ONLY_REFLECTIVE_CONTROL_NOT_ESTABLISHED. Neither a change of the Atlas's 80-chapter release/certification state nor a general claim about sapience follows from this tranche.
