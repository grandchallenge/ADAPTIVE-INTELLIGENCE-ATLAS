# ATLAS-CH-EXPERIMENT-001 — Derivation and Argument Packet

## 1. Purpose

This packet makes precise the chapter's central claim:

**an experiment is not merely an execution; it is a structured inference from a design and observations to a bounded claim.**

The packet does not attempt a complete theory of experimental design or causal inference.

It defines the minimum structure the Atlas needs so later chapters can distinguish a metric from the argument that gives the metric evidentiary force.

## 2. Starting point from the Evidence chapter

The audited Evidence chapter separates:

- claim;
- epistemic class;
- support route;
- scope;
- non-entailments;
- downstream permission.

EXPERIMENT-001 adds experimental structure to that support route.

A result is therefore not promoted by being called an experiment.

The experiment must expose what was varied, what was compared, how observations were selected, and what claim boundary survives those choices.

## 3. Experiment-argument object

Define

`E = (q, theta, U, A, Z, Y, g, V, tau, Omega)`.

Interpretation:

- `q`: bounded proposition or quantitative claim;
- `theta`: estimand, the quantity the design means to learn about;
- `U`: units, population, dataset, tasks, or cases to which the design refers;
- `A`: intervention/assignment rule;
- `Z`: nuisance variables, blocks, covariates, and controlled conditions;
- `Y`: measured outcome;
- `g`: estimator, contrast, or comparison function;
- `V`: declared variation/uncertainty sources and summary;
- `tau`: stopping, selection, tuning, and reporting rule;
- `Omega`: interpretation scope.

The tuple is diagnostic.

It does not imply that every field is statistically independent, nor that every experiment must use randomized treatment assignment.

## 4. Hypothesis and estimand are different objects

A hypothesis can be qualitative:

`q: intervention A improves performance.`

An estimand must specify a quantity, for example

`theta = E[Y | do(A=1)] - E[Y | do(A=0)]`

under a causal model, or a finite contrast under a declared dataset and protocol.

A hypothesis without an estimand can hide the meaning of "improves."

An estimand without a claim boundary can hide the population or task scope.

The design must connect the two.

## 5. Finite potential-outcome formulation

For finite units `i=1,...,n`, let

- `Y_i(1)`: outcome unit `i` would have under treatment;
- `Y_i(0)`: outcome unit `i` would have under control.

Define the finite-population average treatment effect

`Delta = (1/n) sum_i (Y_i(1)-Y_i(0))`.

Under assignment `A_i in {0,1}`, the observed outcome is

`Y_i = A_i Y_i(1) + (1-A_i)Y_i(0)`.

Only one potential outcome is observed for each unit.

That missing counterfactual is the reason the assignment and comparison design matter.

Randomization can make treatment assignment independent of potential outcomes under the randomized design, supporting unbiased or design-based estimators under appropriate conditions.

Nonrandomized studies require additional structure such as matching, blocking, modeling, or substantive assumptions.

## 6. Baseline versus ablation

Let system `S` contain components `c_1,...,c_k`.

A **baseline comparison** is any contrast

`g(Y(S), Y(B))`

against comparator `B`.

An **ablation of component c_j** constructs a controlled variant

`S_{-j}`

or another targeted intervention on `c_j`, then compares

`g(Y(S), Y(S_{-j}))`.

The comparison becomes mechanism evidence only if the intervention is sufficiently isolated.

If removal of `c_j` also changes compute budget, parameter count, data exposure, optimization schedule, or interface semantics, the ablation estimates a compound intervention unless those changes are explicitly controlled or included in the estimand.

## 7. Nuisance variables and blocking

Suppose outcome depends on treatment `A` and nuisance stratum `Z`.

The naive aggregate contrast

`E[Y | A=1] - E[Y | A=0]`

mixes the treatment effect with differences in the distribution of `Z` across treatment groups.

A standardized contrast instead fixes weights `w_z`:

`Delta_std = sum_z w_z ( E[Y | A=1,Z=z] - E[Y | A=0,Z=z] )`.

If treatment and control groups have different stratum weights, the naive and standardized contrasts can differ in magnitude or sign.

This is the formal core of the computational witness below.

## 8. Exact confounding witness

There are 20 units:

- 10 easy units;
- 10 hard units.

Potential outcomes are homogeneous within each stratum:

| Stratum | Y(0) | Y(1) | Individual effect |
|---|---:|---:|---:|
| easy | 10 | 11 | +1 |
| hard | 0 | 1 | +1 |

Therefore the exact finite-population treatment effect is

`Delta = 1`.

Observed assignment is deliberately imbalanced:

- treatment receives 1 easy and 9 hard units;
- control receives 9 easy and 1 hard unit.

Observed treatment mean:

`(1*11 + 9*1)/10 = 20/10 = 2`.

Observed control mean:

`(9*10 + 1*0)/10 = 90/10 = 9`.

Naive aggregate difference:

`2 - 9 = -7`.

Within easy stratum:

`11 - 10 = +1`.

Within hard stratum:

`1 - 0 = +1`.

With equal stratum weights:

`Delta_std = (1/2)(1) + (1/2)(1) = 1`.

The aggregate comparison has the wrong sign because treatment assignment is confounded with stratum difficulty.

The controlled comparison recovers +1 only because this finite construction makes the within-stratum outcomes homogeneous and fully observed across assigned units.

No general causal-identification theorem follows from the toy table.

## 9. Random seed as one coordinate of variation

Let an ML outcome be written schematically as

`Y = F(a, d, s, h, e)`

where:

- `a`: algorithm/intervention;
- `d`: dataset/sample;
- `s`: random seed;
- `h`: hyperparameter/search choice;
- `e`: environment/implementation conditions.

A seed sweep that holds `d,h,e` fixed samples variation in `s`.

It therefore estimates something like

`Var_s[Y | a,d,h,e]`.

It does not automatically estimate

`Var_d`, distribution shift, cross-implementation variability, or uncertainty over the target population.

Reporting "five seeds" is therefore incomplete unless the reader knows what is fixed and what is sampled.

## 10. Selection and stopping

Suppose `m` noisy candidate runs yield

`X_j = mu_j + epsilon_j`.

If the reporting rule chooses

`j* = argmax_j X_j`,

then the reported statistic is

`max_j X_j`,

not a prespecified single-run observation.

The search rule is part of `tau`.

This remains true whether the selection happens over:

- seeds;
- hyperparameters;
- checkpoints;
- datasets;
- prompts;
- benchmark subsets;
- architecture variants.

A fair comparison must expose enough of that selection process for the intended inference.

## 11. Effect size versus statistical significance

An effect estimate asks "how much?"

A p-value, under a specified null model and analysis, addresses compatibility of data with that model in a different way.

The ASA statement explicitly rejects interpreting statistical significance as the magnitude or practical importance of an effect.

Therefore the experimental argument should expose:

- effect estimate;
- uncertainty interval or other variation description when appropriate;
- sample/design assumptions;
- any inferential statistic;
- practical interpretation.

A threshold crossing cannot replace the effect estimate.

## 12. Reproducibility, replication, validity

Using the NASEM terminology adopted by this chapter:

- reproducibility reuses the same data and computational method to seek consistent computational results;
- replication conducts a new study aimed at the same scientific question using newly obtained data.

These answer different questions.

A reproducible computation can faithfully reproduce:

- a confounded design;
- a coding error;
- a biased sample;
- a poorly chosen metric.

Thus:

`reproducible(E) != valid(E)`.

Likewise, one failed replication does not mechanically falsify the original claim without examining design, uncertainty, and scope.

## 13. Benchmark performance versus mechanism evidence

Suppose system `S_1` scores higher than `S_0` on benchmark `B`.

That observation supports a bounded performance comparison under the benchmark protocol.

It does not by itself identify which component caused the difference.

Mechanism evidence requires a design that changes the candidate mechanism while controlling or modeling relevant alternative changes.

This is why ablations, factorial designs, targeted interventions, and counterfactual reasoning matter.

## 14. Falsifiability as design property

A useful experimental claim states what outcome would count against it.

For claim `q`, the design should identify a rejection or revision region `R` in the observable/estimated result space, or at least an explicit qualitative falsification condition.

This does not require every scientific proposition to be reduced to one null-hypothesis test.

It requires the experiment to expose how evidence can change the claim.

## 15. Downstream interface

ATLAS-CH-REPLAY-001 may consume the following without rebuilding them:

- experiment-argument object `E`;
- distinction between estimand, metric, and claim;
- explicit stopping/selection rule;
- variation-source decomposition;
- reproducibility-versus-validity boundary;
- requirement that exact computational outputs retain their experimental scope.

Replay adds stronger source/environment identity machinery.

It does not retroactively supply prerequisite authority to this chapter.
