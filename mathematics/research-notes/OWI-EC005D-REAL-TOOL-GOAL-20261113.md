# OWI-EC-005D — Public-feedback-conditioned real task mutation

**Grand Challenge Labs, 13 November 2026.** Research continuation of [OWI-EC-005 #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466), following the real terminal-checker admission in [PR #469](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/469).

**Status:** actual goal-directed intervention improvement observed on one source-locked real environment, with private terminal verification. **Not** evidence of an outcome-only trained controller, general introspection, or an Atlas release change.

## Scientific question

The preceding real-tool negative control established that stop, one read-only probe, and two read-only probes all produced terminal reward 0.1538 on the same task, leaving the environment unchanged. This tranche asks whether a controller given only a public user task and its *actual chosen tool replies* can select a consequential intervention and obtain a higher final reward from an independent private checker. The target is **causal action-to-feedback infrastructure**, rather than self-observation learning itself.

The source is the complete pinned 2,550-task Agent-Reflex-RL-2K corpus at revision `337c7eebaa3fd56825602d7252000c55a62e27f3` with raw JSONL SHA256 `3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a`. This tranche uses pinned row 1 solely for intervention feasibility, not for the separate 30/10/11 environment-family transfer test.

## Source-derived public task and allowable observations

The public task asks the agent to create a Tarvio Gastroenteritis outbreak report for the Old Market location, submitted by Miguel Torres with six cases, then verify credentials, change the count to twelve, cross-reference previous reports, attribute review to a healthcare professional, and escalate. The read-only public tool interfaces include `get_location_by_name`, `list_reporters_by_type`, and `list_reports_by_disease`. The state-mutating public tools include `create_outbreak_report`, `validate_reporter_credentials`, `update_case_count`, `verify_outbreak_report`, and `escalate_outbreak_report`. The names and expected arguments were recovered from *public agent-facing tool schemas*.

The actual source-pinned, no-network public probes returned Old Market as location `LOC5`, Miguel Torres as reporter `REP4`, and an earlier same-disease report dated 2024-04-17. These values were discovered through executed selected tools; **they are not hard-coded into the final policy**. The policy parses the public task, looks up those records itself and derives the new report date as the day after the latest prior same-location/same-disease report. Where required public fields cannot be resolved, it abstains instead of inventing IDs.

## Executed conditional agent

The benchmark introduces three randomized arms with first-stage assignment probability 1/3: immediate stop, three read-only task-specific observations, and a goal-directed scripted controller. The controller is **not** trained by reinforcement learning, not a language model, and not supplied with private verifier information. It is a deliberately transparent baseline isolating whether the real environment and feedback transport can support beneficial state-changing behavior.

For its goal arm, the agent takes actual observations from the three declared read tools, conditionally creates the report with the public task's disease, location, reporter and case-count fields, then queries the public report list to discover the new ID. This last read is essential: the real `create_outbreak_report` method reports `success` and a message **without a report ID**. A controller that assumes the creation reply includes an ID cannot continue. The revised controller matches a unique public report by location, reporter, date and initial case count, then conditionally invokes the credential validator, case-count update and verification operation. Its live episode budget is eight selected calls, all executed in a restricted no-network Docker child. The private terminal checker is a *different* Docker child, receiving the actual post-constructor initial and terminal environment state only after the policy finishes.

The policy's decisions are based on the **selected** tool replies, not unchosen counterfactuals or a latent fault label. The program neither enumerates other actions during a trajectory nor reads the private checklist, RSD skills, or initial hidden environment state to decide an action. The trusted host bridges terminal state directly to the isolated verifier; only the final scalar reward/aggregates appear in research evidence.

## Measured live outcome

The [first live candidate run 43397678840](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43397678840) proved that a real state-changing `create_outbreak_report` action raised the private checklist reward from 0.1538 to 0.3077 (4/13 conditions), compared with stop/read-only. However, the controller then stopped because it incorrectly expected the new report ID in the creation response. That API mismatch was diagnosed from **only the public creation result shape** and repaired by a new actual public `list_reports_by_disease` call.

The [corrected candidate run 43398289223](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43398289223) executed twelve independently reset real episodes under seed 12 and reported:

| Assigned arm | Episodes | Mean terminal reward | Mean actual selected tool calls |
| --- | ---: | ---: | ---: |
| Stop | 2 | 0.1538 | 0 |
| Read-only inspection | 7 | 0.1538 | 3 |
| Feedback-conditional goal | 3 | **0.3846** | **8** |

This corresponds to approximately **2/13 private conditions** for stop and read-only inspection versus **5/13** for the goal-directed arm. The raw mean improvement is **0.2308** in terminal checklist fraction. The next selected action genuinely depends on results previously observed from live calls: a new report ID is discovered only after creating the report. The result is not a vectorized pseudo-intervention.

The experiment demonstrates consequential interaction *on this one task*. It does not demonstrate that a learned policy discovered these steps, that all requested operations completed, or that the policy has a positive **task-plus-physical-compute** advantage. Eight tool calls cost more than zero or three; container elapsed times and per-call tool times are recorded separately. No five-seed, held-out environment family, new-tool schema, persistent-fault, or adversarial reflection-training comparison has been performed.

## Reproduction and controls

`experiments/owi_ec005_realtools_goal_discover.py` audits source-pinned public task/tool declarations only. `experiments/owi_ec005_realtools_goal_probe.py` performs selected read-only calls inside the restricted child. `experiments/owi_ec005_realtools_goal_policy.py` runs stop/read-only/goal arms and routes terminal initial/final states to the preexisting independent private verifier. `tests/test_owi_ec005_realtools_goal.py` checks public-only task parsing, actual returned-ID conditioning, date inference, abstention on missing reporter information, invalid tool-return resistance and absence of unchosen verifier outcomes.

The CI workflow `.github/workflows/owi-ec005-realtools-mutation.yml` reproduces exact source intake, untrusted-tool containment and randomized real terminal outcomes; uploaded evidence includes only selected call names, chosen propensities, hashed tool returns, measured costs and aggregate terminal scores. Private initial/final state contents, checker source and reflection skills remain outside policy inputs and retained artifacts.

## Next scientific obligations

The next research unit must abandon the hand-authored action sequence as the learning mechanism. Train a frozen language-agent or bounded action-value policy on **chosen actions and terminal scalar outcomes only**, using the real environment while preserving the private verifier barrier. Compare against equal-budget no-reflection, always-verify, passive telemetry and scripted-control baselines, with zero/shuffled-feedback ablations, logged action probabilities and measured compute/latency. Evaluate five or more independent seeds and hold out full environment families and perturbation mechanisms. Explicitly distinguish causal effect of an action from *learned causal self-observation*.

Issue #466 remains open. The Atlas 80-chapter ledger, release state and mathematical certification authority remain unchanged.
