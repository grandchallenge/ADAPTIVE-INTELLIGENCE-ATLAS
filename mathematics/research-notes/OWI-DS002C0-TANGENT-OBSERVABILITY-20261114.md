# OWI-DS-002 C0 — Chosen-run tangent information: five-seed privileged observability diagnostic

Grand Challenge Labs · 14 November 2026 Vancouver / 15 November UTC. Parent issue [#483](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/483). Candidate draft [PR #489](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/489). Exact executed source head: `72e3a7ef4863fe9183345fe67278c439b6ff0072`. [GitHub Actions run 43657710881](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43657710881); five-seed artifact `14137973806`, ZIP SHA256 `c6fc3afb81febd9786cdcc47521ca28c145e648087cadaf4f0826b577594cd9e`.

## Evaluator-only method

Use a fixed selected branch-A probe across all examples of the existing conditional recurrent environment, with `p_fault=1`, comparing paired Gaussian raw-state faults and damaged checkpoint faults on identical initial task input sequences and affected-branch masks. The legal checkpoint JVP is obtained *only after actual selected replay*, via `ChosenRunTangents` with a fixed normalized all-ones direction. Every JVP query is recorded. The private fault index is inspected **only after measurement** to select the branch-A-affected cohort; the mechanism label is supplied to a *privileged diagnostic classifier* and is NEVER supplied to policy synthesis or a causal self-model.

Five seeded frozen cores were separately pretrained for 250 steps. Per seed, the diagnostic uses three training cohorts of 256 samples per mechanism and a separately seeded held-out cohort of 512 samples per mechanism; branch-A-affected audit filtering leaves approximately half the examples. Each seed has eight JVP calls and 2,560 queried examples. This is a **mechanism-label upper-bound information test** and expressly not outcome-only causal learning.

Two pairs of logistic evaluators were fitted with the same labeled data:

1. selected replay residual alone versus residual plus selected-run JVP;
2. four public pre-probe telemetry features plus residual versus those five features plus JVP.

Evaluations used fresh held-out exogenous seeds. No counterfactual reward was used in A/B programme training; this separate diagnostic uses privileged mechanism labels solely to quantify observable separability.

## Direct five-seed evidence

| Diagnostic input | Mean held-out AUC | Mean held-out accuracy | Mean Brier |
|---|---:|---:|---:|
| Probe residual | 0.574796 | 0.548710 | 0.246378 |
| Probe residual + measured JVP | 0.606142 | 0.566333 | 0.240657 |
| Public telemetry + residual | 0.895463 | 0.814098 | 0.128947 |
| Public telemetry + residual + measured JVP | 0.898222 | 0.825300 | 0.126241 |

All rows are means of five independently seeded *source-labelled diagnostic* runs; not confidence intervals or task success rates.

Paired per-seed JVP-minus-no-JVP AUC deltas:

- Residual only: `[+0.00477,+0.04324,+0.08861,+0.00649,+0.01361]`, mean `+0.03135`, sample SD `0.03556`.
- Public telemetry plus residual: `[-0.00077,+0.00418,+0.00879,+0.00119,+0.00042]`, mean `+0.00276`, sample SD `0.00383`.

Mean accuracy delta on the full telemetry-plus-residual comparison: `+0.01120`, SD `0.01411`. Mean Brier change: `-0.00271`, SD `0.00370`. No inferential superiority claim follows from these descriptive statistics.

Mean total observed diagnostic runtime: `1.408` seconds per seed, including core pretraining and all labelled classifiers; JVP execution is explicitly charged in query counts and timed internally but lacks physical GPU MAC certification.

## Interpretation and failure boundaries

The measurement provides evidence that chosen-replay checkpoint JVPs *can carry some source-mechanism-discriminating information* in the constructed, source-labelled evaluation. Relative to the stronger public telemetry plus probe-residual comparator, the incremental held-out AUC is small and inconsistent in magnitude. The signal may be too weak, costly, or insufficiently identifiable for an outcome-only agent to exploit.

The training and held-out cohorts share the same known mechanism families and labelled task structure. The diagnosis uses labels a learner cannot see, source-side selection of affected fault cases, and a fixed branch-A probe. It therefore establishes **neither** general intervention identification **nor** runtime differentiable program synthesis, causal introspection, transfer to unseen mechanisms, formal correctness, or matched-compute benefit. Do not promote it as a learned C policy.

## Next scientific obligation: C1

Implement a genuinely outcome-only C learner with typed executable conditional probe/repair programs, access only to selected-run, charged JVP measurements, and no source labels or unchosen outcomes. Compare against A and B under the same logged environment cohorts and total compute (including derivative-query cost). Mandatory controls: C-shuffled within comparable chosen-probe strata and C-surrogate-only with no new environment derivative measurement. Evaluate checkpoint intervention *held out from training* and report when JVP information is insufficient. Require repeated seeds, paired uncertainty accounting and independent verification; no C1 success may be inferred from this C0 upper bound.

**Disposition:** `C0_PRIVILEGED_OBSERVABILITY_SIGNAL_SMALL__C1_OUTCOME_ONLY_UNTESTED`.
