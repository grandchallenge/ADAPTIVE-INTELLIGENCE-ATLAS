# Chapter Specification — ATLAS-CH-EXPERIMENT-001

## Identity

- Stable ID: `ATLAS-CH-EXPERIMENT-001`
- Title: **Experiments as Arguments**
- Part: `ATLAS-PART-GOV`
- Status target: `draft-v0.1`
- Hard prerequisite: `ATLAS-CH-EVIDENCE-001`
- Implementation issue: #96
- Drafting baseline: `55085755626d60d2981a7cf17a6af7cbac60f9fc`

## Contract

Develop falsifiability, baselines, controls, ablations, counterfactuals, effect sizes, seeds, and reproducibility as parts of an evidentiary argument rather than as a checklist of experimental rituals.

## Opening obstruction

A single run reports a metric.

That metric does not yet say:

- what quantity the experiment meant to estimate;
- what alternative world supplied the contrast;
- what nuisance variables differed;
- what randomness was sampled;
- what stopping or selection rule generated the reported number;
- what uncertainty remains;
- what claim the result is allowed to support.

The chapter begins from the mismatch between **a run** and **an argument**.

## Formal object

Represent a bounded experiment by

`E = (q, theta, U, A, Z, Y, g, V, rho, Omega)`.

Here:

- `q` is the bounded claim under examination;
- `theta` is the estimand or target contrast;
- `U` is the declared unit/population/sample frame;
- `A` is the intervention or assignment rule;
- `Z` records measured or controlled nuisance variables;
- `Y` is the outcome object;
- `g` is the estimator or comparison rule;
- `V` is the uncertainty/variation description;
- `rho` is the stopping, selection, and reporting rule;
- `Omega` is the scope in which the result may be interpreted.

The tuple is an Atlas synthesis, not a claim that experimental science has one universal canonical tuple.

## Required distinctions

The manuscript must keep separate:

1. hypothesis versus estimand;
2. intervention versus observation;
3. baseline versus ablation;
4. randomized assignment versus random seed;
5. seed variance versus sampling/population uncertainty;
6. effect magnitude versus statistical significance;
7. reproducibility versus replication and validity;
8. benchmark performance versus mechanism evidence;
9. prespecified stopping versus adaptive selection;
10. internal validity versus external scope.

## Causal and counterfactual core

For finite units `i=1,...,n`, use potential outcomes `Y_i(1)` and `Y_i(0)` only to make the missing counterfactual explicit.

Define the finite-population average treatment effect

`Delta = (1/n) sum_i [Y_i(1)-Y_i(0)]`.

Only one potential outcome is observed per unit under one assignment. The design determines what comparisons can identify or estimate `Delta` under stated assumptions.

The chapter must not imply that every machine-learning comparison is a randomized causal experiment.

## Baselines and ablations

A baseline is a comparator.

An ablation is a structured intervention on a component relative to a reference system.

Therefore:

- every ablation contains a comparison;
- not every comparison is an ablation;
- an ablation supports a mechanism claim only to the extent that the intervention isolates the component and other relevant conditions are held fixed or modeled.

## Seeds

A random seed indexes one source of execution or sampling randomness under a fixed protocol.

Seed sweeps can estimate conditional run-to-run variability.

They do not, by themselves, estimate:

- shift across datasets;
- uncertainty over the target population;
- implementation uncertainty across codebases;
- sensitivity to hidden preprocessing;
- external validity.

## Statistical reporting

Effect magnitude and uncertainty must remain visible.

Statistical significance may be reported when appropriate, but a threshold crossing is not the claim.

Stopping, hyperparameter search, benchmark selection, and best-seed selection are part of the design and must not be erased from the argument.

## Reproducibility boundary

Adopt the NASEM terminology for this chapter:

- reproducibility: consistent computational results using the same data, code/methods, and analysis conditions;
- replication: a new study aimed at the same scientific question with newly obtained data.

The chapter must state explicitly that reproducibility is valuable but does not certify validity.

## Exact computational witness

Use a 20-unit, two-stratum deterministic population.

Potential outcomes:

- easy stratum: `Y(0)=10`, `Y(1)=11`;
- hard stratum: `Y(0)=0`, `Y(1)=1`.

Observed assignment:

- treatment: 1 easy + 9 hard;
- control: 9 easy + 1 hard.

Then:

- naive treated mean = 2;
- naive control mean = 9;
- naive difference = -7;
- within each stratum the treatment contrast is +1;
- equal-stratum standardized contrast = +1;
- exact finite-population average treatment effect = +1.

This is a deterministic confounding witness. It proves only that an uncontrolled aggregate can reverse the sign of a controlled finite comparison under the declared table.

## Source basis

Source-lock:

- NIST DOE material for intervention, nuisance factors, blocking, randomization, replication;
- Rubin (1974) for causal-treatment framing and randomization/nonrandomized control;
- Wasserstein and Lazar (2016) for p-value interpretation;
- NASEM (2019) for reproducibility/replication terminology;
- Henderson et al. (2018) for representative ML/RL run variance and reporting concerns;
- audited `ATLAS-CH-EVIDENCE-001`.

## Downstream handoff

`ATLAS-CH-REPLAY-001` may assume:

- an experiment has a declared claim, estimand, design, comparison rule, variation model, stopping/reporting rule, and scope;
- reproducibility is not validity;
- seed identity is part of experimental provenance but not a universal uncertainty model;
- computational support inherits the Evidence chapter's claim-boundary discipline.

No already-drafted Replay manuscript may be used as prerequisite authority during composition of this chapter.

## Completion criteria

- source lock exists and pins the audited prerequisite;
- formal/derivation packet exposes the argument object and exact witness mathematics;
- computational witness has an explicit Claim boundary;
- manuscript includes `**Epistemic status:**`, references, and source-lock path;
- Chapter Ledger records `draft-v0.1`;
- Source Register contains the chapter source lock;
- bibliography closes all manuscript citation keys;
- repository validation is green;
- bounded post-draft audit repairs all in-scope defects before completion.
