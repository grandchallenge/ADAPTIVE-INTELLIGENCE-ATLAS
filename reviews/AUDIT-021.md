# AUDIT-021 — Experiments as Arguments

## Disposition

**PASS WITH ONE FORMAL NOTATION REPAIR**

ATLAS-CH-EXPERIMENT-001 remains at draft-v0.1.

The chapter correctly develops experiments as bounded evidentiary arguments connecting a claim, estimand, units/population, intervention/assignment rule, nuisance structure, outcome, comparison rule, variation model, selection/reporting rule, and interpretation scope.

The audit found one in-scope formal defect:

- the implementation draft used `tau` for the experiment's stopping/selection/reporting rule, while the audited Evidence prerequisite already uses `tau` as the epistemic-class coordinate in its claim-support packet.

The audit repaired the experiment notation to `rho` everywhere.

No source identity, source authority, computational-witness arithmetic, causal-scope boundary, statistical-significance boundary, reproducibility boundary, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  `0e441ea8725a7527f138bf0b11b202a737b0dec8`;
- implementation PR:
  #97;
- audit issue:
  #98;
- chapter:
  `ATLAS-CH-EXPERIMENT-001`.

## 1. Hard prerequisite

PASS.

The source lock binds the audited Evidence prerequisite exactly:

- `manuscript/parts/01-orientation/ATLAS-CH-EVIDENCE-001.md`
  blob `17eaa9caf90ede47c74dccff052f93d9fb3d901e`;
- `reviews/AUDIT-014.md`
  blob `6af518de0687a9cd8fe5635e2fba8f6a6271c77c`.

The chapter inherits the Evidence distinction among claim, epistemic class, support route, scope, non-entailments, and downstream permission.

No downstream Replay manuscript is used as hidden prerequisite authority.

## 2. External experimental-method sources

PASS.

The source lock identifies and scopes:

- NIST/SEMATECH e-Handbook of Statistical Methods, Process Improvement / Design of Experiments, including deliberate factor intervention, nuisance factors, randomized block designs, randomization, and replication;
- Donald B. Rubin, "Estimating causal effects of treatments in randomized and nonrandomized studies," Journal of Educational Psychology 66(5), 688-701 (1974), DOI `10.1037/h0037350`;
- Ronald L. Wasserstein and Nicole A. Lazar, "The ASA Statement on p-Values: Context, Process, and Purpose," The American Statistician 70(2), 129-133 (2016), DOI `10.1080/00031305.2016.1154108`;
- National Academies of Sciences, Engineering, and Medicine, Reproducibility and Replicability in Science (2019), DOI `10.17226/25303`;
- Henderson et al., "Deep Reinforcement Learning That Matters," AAAI 32(1) (2018), DOI `10.1609/aaai.v32i1.11694`.

The source roles are bounded correctly.

NIST is used for experimental-design concepts.

Rubin is used for treatment-effect/randomization reasoning.

The ASA statement is used to separate p-value significance from effect magnitude and practical importance.

NASEM supplies the chapter's declared reproducibility/replication terminology.

Henderson et al. is used only as representative machine-learning evidence concerning nondeterminism, variance, baselines, and reporting in deep RL.

No source is treated as proof of a universal Atlas experimental standard.

## 3. Experiment-argument object

PASS AFTER FORMAL REPAIR.

The repaired object is

`E = (q, theta, U, A, Z, Y, g, V, rho, Omega)`.

The fields are:

- `q`: bounded claim;
- `theta`: estimand;
- `U`: units/population/sample frame;
- `A`: intervention/assignment rule;
- `Z`: nuisance structure;
- `Y`: outcome;
- `g`: estimator/comparison rule;
- `V`: variation/uncertainty description;
- `rho`: stopping, tuning, selection, and reporting rule;
- `Omega`: interpretation scope.

The original use of `tau` collided with the Evidence prerequisite's established use of `tau` for epistemic class.

The repair to `rho` removes that ambiguity without changing mathematical content.

## 4. Hypothesis versus estimand

PASS.

The chapter does not treat a verbal hypothesis such as "improves performance" as self-specifying.

It requires the quantity, population/task scope, comparator, and aggregation to be explicit through the estimand and experiment object.

Metric and estimand remain distinct.

## 5. Intervention versus observation

PASS.

The manuscript distinguishes an observational association from a designed intervention.

It states correctly that randomization addresses assignment-related confounding under the declared design but does not automatically repair measurement error, coding defects, selection effects, hidden preprocessing, or external-validity limits.

## 6. Finite potential-outcome formulation

PASS.

For finite units `i=1,...,n`, the derivation packet defines:

- `Y_i(1)`;
- `Y_i(0)`;
- finite-population average treatment effect
  `Delta = (1/n) sum_i (Y_i(1)-Y_i(0))`;
- observed outcome under one assignment.

The missing counterfactual is used only to explain why assignment/comparison design matters.

The chapter does not claim that every machine-learning comparison is a randomized causal experiment.

## 7. Baseline versus ablation

PASS.

A baseline is any comparator.

An ablation is a structured intervention on a component relative to a reference system.

The chapter explicitly notes that an ablation may become a compound intervention when removing a component also changes compute, parameter count, optimization, training duration, interface semantics, or other relevant conditions.

Mechanism evidence is therefore not inferred merely from the label "ablation."

## 8. Nuisance variables and blocking

PASS.

The derivation distinguishes the naive aggregate contrast

`E[Y | A=1] - E[Y | A=0]`

from a nuisance-stratified or standardized contrast.

The manuscript connects this to NIST's blocking concept without claiming that blocking universally solves observational confounding.

## 9. Exact computational witness

PASS.

The 20-unit deterministic witness has:

easy stratum:

- `Y(0)=10`;
- `Y(1)=11`.

hard stratum:

- `Y(0)=0`;
- `Y(1)=1`.

Every unit has treatment effect +1.

Observed assignment:

- treatment: 1 easy + 9 hard;
- control: 9 easy + 1 hard.

Independent exact arithmetic confirms:

- treatment mean = 2;
- control mean = 9;
- naive aggregate difference = -7;
- easy within-stratum difference = +1;
- hard within-stratum difference = +1;
- equal-stratum standardized difference = +1.

The witness's Claim boundary is correct.

It proves only the finite sign reversal in the declared table.

It does not promote stratification into a general causal-identification theorem.

## 10. Seeds and uncertainty

PASS.

The chapter models an ML outcome schematically as

`Y = F(a,d,s,h,e)`

for algorithm, data, seed, hyperparameter/search choice, and environment/implementation conditions.

A seed sweep is correctly described as sampling variation in `s` conditional on the fixed remaining coordinates.

The chapter explicitly refuses to treat seed variance as a substitute for data/population, distribution-shift, implementation, preprocessing, or mechanism uncertainty.

## 11. Selection and stopping

PASS.

The chapter includes the search/reporting rule inside `rho`.

For noisy candidate outcomes

`X_j = mu_j + epsilon_j`

and selected index

`j* = argmax_j X_j`,

the manuscript correctly notes that the reported statistic is the maximum of a selection process rather than a prespecified single-run observation.

The argument applies equally to hidden selection over seeds, hyperparameters, checkpoints, prompts, benchmark subsets, or architecture variants.

## 12. Effect size versus statistical significance

PASS.

The chapter preserves the ASA boundary:

- statistical significance is not effect magnitude;
- p-value threshold crossing is not practical importance;
- one index does not replace study design and scientific reasoning.

The manuscript therefore requires effect magnitude and uncertainty to remain visible where appropriate.

## 13. Reproducibility versus replication and validity

PASS.

The chapter explicitly adopts the NASEM terminology:

- reproducibility: consistent computational results using the same input data, computational steps/methods/code, and conditions of analysis;
- replication: a new study aimed at the same scientific question with newly obtained data.

It correctly states that a computation may reproducibly reproduce a confounded design, biased sample, coding defect, or misleading metric.

Thus reproducibility is not promoted into validity, causal identification, or generalization.

## 14. Benchmark performance versus mechanism evidence

PASS.

A benchmark superiority result is treated as performance evidence under the benchmark protocol.

It is not treated as sufficient identification of the mechanism responsible for the difference.

The chapter requires targeted interventions/ablations or other designs that separate the candidate mechanism from alternative changes before stronger mechanism claims are made.

## 15. Falsification and revision conditions

PASS.

The chapter treats falsifiability as a property of the experimental argument:

the design should state what result would count against, revise, or narrow the claim.

It does not require every scientific statement to be reduced to one null-hypothesis significance test.

## 16. Downstream handoff

PASS.

ATLAS-CH-REPLAY-001 may inherit:

- the experiment-argument object;
- estimand/metric distinction;
- intervention/comparison structure;
- variation-source decomposition;
- selection/reporting rule;
- reproducibility-versus-validity boundary;
- exact claim scope.

Replay can then add source, environment, parameter, seed, and output identity.

The dependency direction remains one-way.

Replay does not retroactively authorize the Experiment chapter.

## 17. Integrity

PASS subject to repository merge gate.

The Chapter Ledger records ATLAS-CH-EXPERIMENT-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-EXPERIMENT-LOCK-001`.

The bibliography contains all manuscript citation keys.

The witness contains an explicit `## Claim boundary`.

No governed figure is registered, which is appropriate because the exact finite witness is clearer as a table and arithmetic reconstruction than as a decorative diagram.

The audited manuscript/specification/derivation/witness contain no intentional tab or C0-control syntax.

Repository validation is the final merge gate for this audit branch.

## 18. Final disposition

AUDIT-021 passes with one formal notation repair.

The repaired chapter now supplies a dependency-safe experimental grammar:

**claim -> estimand -> intervention/comparison -> nuisance control -> effect/uncertainty -> selection rule -> bounded interpretation.**

That is sufficient for Replayable Evidence Objects to inherit an explicit experimental object without confusing replayability with validity.
