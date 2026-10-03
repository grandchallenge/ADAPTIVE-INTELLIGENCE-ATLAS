# Experiments as Arguments
<!-- ATLAS-CH-EXPERIMENT-001 -->

**Epistemic status:** Atlas synthesis of established experimental-design, causal-inference, statistical-reporting, reproducibility, and machine-learning experimental-method sources, with one exact finite computational witness.  
**Specification:** manuscript/specifications/ATLAS-CH-EXPERIMENT-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-EXPERIMENT-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-EXPERIMENT-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-EXPERIMENT-001.yaml

A machine-learning experiment can be expensive, carefully logged, repeated across seeds, and still fail to answer the question its authors think it answers.

That is not because experiments are useless.

It is because **a run is not yet an argument**.

A run produces observations.

An argument explains why those observations bear on a particular claim.

The distinction is easy to lose when the object on the screen is a single number: accuracy, loss, reward, latency, FLOPs, energy, perplexity, exact-match rate.

Numbers look decisive.

But before a number can carry evidentiary force, we must ask what was changed, what stayed fixed, what population or task family the comparison refers to, what randomness was sampled, what nuisance variables moved at the same time, what selection process chose the reported result, and what claim the result is actually allowed to support.

This chapter develops experiments as **structured claim-support objects**.

The governing idea is:

> an experiment is a designed contrast whose evidentiary force comes from the relation among the claim, the estimand, the intervention, the comparison, the variation model, and the scope.

The chapter does not propose one universal statistical recipe.

Different scientific questions need different designs.

What must remain stable is the logical discipline connecting design to claim.

## 1. From metric to argument

Suppose two systems are evaluated and one obtains score 82 while the other obtains score 79.

What has been established?

At minimum, under the exact evaluation protocol that produced those numbers, one recorded outcome is larger than the other.

That statement may be useful.

But many stronger statements do not follow automatically.

It does not yet establish:

- that the architectural difference caused the improvement;
- that the improvement persists across datasets;
- that the improvement persists across seeds;
- that the effect is practically important;
- that a named mechanism explains the difference;
- that the result generalizes outside the benchmark;
- that the experiment would survive a fresh implementation;
- that the comparison was selected before seeing the results.

The Evidence chapter already supplied the Atlas rule that support must retain its scope.

EXPERIMENT-001 specializes that rule for empirical and computational comparisons.

We will write an experiment-argument object as

`E = (q, theta, U, A, Z, Y, g, V, rho, Omega)`.

The notation is deliberately compact.

It forces ten questions into view.

- `q`: What bounded claim is under examination?
- `theta`: What quantity is the experiment meant to estimate?
- `U`: What units, tasks, datasets, or population does the design concern?
- `A`: What intervention or assignment rule creates the comparison?
- `Z`: What nuisance variables, blocks, or controlled conditions matter?
- `Y`: What outcome is measured?
- `g`: What estimator or comparison rule converts observations into a contrast?
- `V`: What sources of variation or uncertainty are represented?
- `rho`: What stopping, tuning, selection, and reporting rule generated the reported result?
- `Omega`: What scope is the conclusion allowed to inhabit?

This tuple is an Atlas synthesis.

It is not an externally standardized definition of experiment.

Its purpose is diagnostic: if a load-bearing field is missing, the argument may be weaker than the prose suggests.

## 2. An intervention is not an observation

The NIST engineering-statistics handbook begins from deliberate variation of factors and observation of responses, and treats nuisance factors, blocking, randomization, and replication as central design concerns [@NISTDOEHandbook].

That intervention logic matters because observational association and intervention answer different questions.

Suppose high-capacity models obtain higher scores than low-capacity models in a collection of published results.

That is an association.

Perhaps capacity helps.

Perhaps the high-capacity models were also trained on more data, tuned more aggressively, evaluated later in the field's history, or implemented by teams with more compute.

The observation does not identify which difference produced the outcome.

A designed intervention attempts to break that ambiguity.

Change the factor of interest while holding relevant alternatives fixed, balancing them, randomizing them, or modeling them explicitly.

The resulting contrast can then bear more directly on the intended claim.

Randomization is one important mechanism for doing this, but it is not magic.

It addresses assignment-related confounding under the design.

It does not automatically repair:

- bad measurement;
- coding defects;
- selective reporting;
- inappropriate outcomes;
- protocol drift;
- hidden preprocessing;
- nonrepresentative sampling;
- generalization beyond the study scope.

Experimental control is therefore specific.

One must always ask: **what source of ambiguity did this design actually remove?**

## 3. Hypothesis versus estimand

A hypothesis is often verbal:

> the intervention improves performance.

The phrase "improves performance" is not yet a mathematical object.

Improve what?

Over which population?

By what aggregation?

Under which resource budget?

Relative to what alternative?

An **estimand** makes the target explicit.

In a simple finite causal setting, imagine units indexed by `i=1,...,n`.

Each unit has two potential outcomes:

- `Y_i(1)`: the outcome under treatment;
- `Y_i(0)`: the outcome under control.

The finite-population average treatment effect is

`Delta = (1/n) sum_i [Y_i(1)-Y_i(0)]`.

Rubin's treatment-effect framework made the benefits of randomization and carefully controlled nonrandomized comparisons explicit in this language of treatment effects and assignment [@Rubin1974Causal].

The difficult point is immediate.

For a particular unit, we observe only the outcome corresponding to the treatment actually assigned.

The other outcome is counterfactual.

So an experiment does not merely "measure the effect."

It constructs a design under which observed contrasts can support claims about an otherwise unobserved comparison.

This is why an estimand is not the same thing as a metric.

Accuracy can be a metric.

"The average change in accuracy caused by replacing component X with Y under a fixed training and evaluation protocol" is an estimand.

The difference is not stylistic.

It determines what the experiment is trying to learn.

## 4. Baselines are comparators; ablations are interventions

Machine-learning papers often use the words **baseline** and **ablation** as if they were interchangeable.

They are not.

A baseline is any comparator.

An ablation is a structured intervention on a component of a reference system.

If a model `S` contains component `c`, an ablation might compare `S` against `S_{-c}`, where the component is removed or replaced.

The intended mechanism claim is something like:

> the presence of component c contributes to the observed behavior.

But the validity of that interpretation depends on what else changes.

Removing a component might also change:

- parameter count;
- compute;
- activation scale;
- optimization stability;
- training time;
- receptive field;
- memory footprint;
- initialization;
- interface shape.

If those effects are not controlled, the ablation is not a pure intervention on one semantic mechanism.

It is a compound intervention.

This does not make the experiment worthless.

It changes the claim.

A compound ablation can show that one system configuration differs from another.

It may not isolate why.

The useful rule is:

> an ablation supports mechanism evidence only to the degree that the intervention isolates the candidate mechanism from relevant alternative changes.

## 5. The confounding trap

A comparison can be numerically exact and logically wrong for the intended question.

Consider two nuisance strata: easy and hard.

Every easy unit has potential outcomes

- control: 10;
- treatment: 11.

Every hard unit has

- control: 0;
- treatment: 1.

Treatment helps every unit by exactly 1.

So the exact finite-population average treatment effect is +1.

Now assign units badly.

The treatment group receives:

- 1 easy unit;
- 9 hard units.

The control group receives:

- 9 easy units;
- 1 hard unit.

The treatment mean is

`(11 + 9*1)/10 = 2`.

The control mean is

`(9*10 + 0)/10 = 9`.

The naive aggregate contrast is therefore

`2 - 9 = -7`.

The aggregate says treatment is worse.

But within the easy stratum,

`11 - 10 = +1`.

Within the hard stratum,

`1 - 0 = +1`.

If we compare treatment and control within strata and then standardize with equal stratum weights, the contrast is +1.

The exact computational witness for this chapter reproduces those values.

Nothing probabilistic is hiding in the example.

The sign reversal is caused entirely by imbalance in the nuisance variable.

This is a minimal model of confounding.

NIST's blocking guidance describes the corresponding design idea: nuisance factors can be held constant within blocks so that the factor of interest can be compared without mixing the block effect into the contrast [@NISTDOEHandbook].

The lesson is not "always stratify."

The lesson is:

> aggregate differences answer aggregate questions. If treatment assignment changes the mixture of nuisance conditions, the aggregate contrast may not estimate the treatment effect you intended.

## 6. Controls do not all play the same role

The word **control** can refer to several distinct devices.

A control group may represent the no-treatment alternative.

A baseline model may represent the incumbent method.

A placebo-like condition may preserve everything except the hypothesized active mechanism.

A negative control may be chosen because no effect is expected.

A positive control may verify that the measurement system can detect a known effect.

A blocked design may control nuisance variation by comparing like with like.

These are not synonyms.

The useful question is not "does the experiment have a control?"

It is:

> which alternative explanation is this control designed to eliminate?

A good control has a job.

If its job is not stated, the reader cannot tell what ambiguity it resolves.

## 7. Counterfactuals are the missing half of the comparison

Whenever we claim that an intervention **caused** an outcome, we are implicitly comparing what happened with what would have happened otherwise.

That "otherwise" is counterfactual.

In randomized experiments, the design uses other assigned units to estimate the missing alternative.

In matched or blocked observational studies, the design attempts to build a credible comparison class.

In simulations, the counterfactual may be directly computable because the same synthetic state can be rerun under two interventions.

In machine-learning ablations, the counterfactual may be "the same training/evaluation process without this component."

But the phrase **the same** is doing work.

If the counterfactual run changes multiple factors, the claimed mechanism becomes ambiguous.

A counterfactual therefore requires an invariance contract:

which parts of the world are intended to remain fixed while the intervention changes?

The stronger the causal interpretation, the more carefully that contract must be defended.

## 8. Seeds: useful, narrow, often overinterpreted

Random seeds are important in modern machine learning because many pipelines contain stochastic elements:

- parameter initialization;
- minibatch ordering;
- dropout masks;
- augmentation;
- environment trajectories;
- randomized search;
- sampling.

Henderson et al. documented how nondeterminism, algorithmic variance, baseline choice, and reporting practice complicate interpretation in deep reinforcement learning [@HendersonEtAl2018].

The general lesson is broader than RL, but the scope must remain explicit.

Suppose an outcome can be written schematically as

`Y = F(a, d, s, h, e)`

with

- algorithm `a`;
- data `d`;
- seed `s`;
- hyperparameter/search choice `h`;
- environment and implementation `e`.

If we vary only `s`, we learn about run-to-run variation conditional on `a,d,h,e`.

That can be valuable.

But it does not automatically estimate:

- uncertainty across datasets;
- shift in the target population;
- variability across independent implementations;
- sensitivity to preprocessing;
- uncertainty induced by hyperparameter search;
- uncertainty about the scientific mechanism.

"Five seeds" is therefore not a universal unit of experimental reliability.

It is a statement about one coordinate of variation.

The experiment should say what that coordinate represents.

## 9. Selection rules are part of the experiment

Suppose we train 100 configurations and report the best one.

The reported score is not the observation from a prespecified configuration.

It is the maximum of a search process.

If each observed score is

`X_j = mu_j + epsilon_j`,

and the selected run is

`j* = argmax_j X_j`,

then the reported statistic is

`max_j X_j`.

That selection changes its interpretation.

The same principle applies when we choose:

- the best seed;
- the best checkpoint;
- the best prompt;
- the best benchmark subset;
- the best hyperparameter sweep;
- the best architecture after many failed variants.

Selection is not forbidden.

Hidden selection is the problem.

The Atlas therefore places stopping, tuning, selection, and reporting inside the experiment object as `rho`.

If `rho` changes after observing outcomes, the experimental argument changes too.

## 10. Effect size is not statistical significance

A statistically significant result can be tiny.

A practically important effect can fail a significance threshold in a small or noisy study.

The American Statistical Association's statement on p-values explicitly separates p-values from effect size and practical importance, and warns against making scientific conclusions depend only on threshold crossing [@WassersteinLazar2016].

For the Atlas, this yields a simple discipline.

When an experiment supports a quantitative claim, report the quantity of interest.

Do not replace it with the fact that some test crossed a threshold.

Depending on the design, useful objects may include:

- mean difference;
- relative change;
- risk difference;
- odds ratio;
- standardized difference;
- confidence or credible interval;
- predictive interval;
- distributional comparison;
- task-level effect distribution.

The correct object depends on the estimand.

The principle does not.

**Magnitude and uncertainty should remain visible.**

A p-value may be part of the argument.

It cannot stand in for the argument.

## 11. Benchmark score versus mechanism evidence

Suppose a new architecture beats a baseline on five benchmarks.

That is evidence about comparative performance under those benchmark protocols.

It is not automatically evidence for the proposed explanation.

A model may improve because of:

- the claimed architectural mechanism;
- increased compute;
- parameter count;
- better optimization;
- hidden regularization;
- preprocessing;
- data leakage;
- implementation quality;
- changed training duration;
- favorable hyperparameter search.

Mechanism evidence requires a design that separates the proposed mechanism from plausible alternatives.

This is why a chapter about experiments must treat ablations, controls, and counterfactuals as structural objects rather than publication rituals.

A benchmark answers:

> what happened under this benchmark protocol?

A mechanism experiment asks:

> what change caused or mediated the difference?

Those are related questions.

They are not the same question.

## 12. Reproducibility is valuable and not sufficient

The National Academies report adopts a useful terminology [@NASEM2019Reproducibility].

In that report:

- **reproducibility** means obtaining consistent computational results using the same input data, code or methods, and analysis conditions;
- **replicability** means obtaining consistent results across studies aimed at the same scientific question using newly obtained data.

The distinction matters because reproducibility is often mistaken for validity.

A perfectly reproducible pipeline can reproduce a flawed analysis exactly.

It can reproduce:

- a confounded comparison;
- a data leak;
- a coding bug;
- a biased sample;
- a misleading metric;
- a selectively chosen result.

Reproducibility answers an identity-and-reexecution question:

> can the computation be reconstructed and obtain consistent results?

Validity asks whether the design and reasoning support the claim.

Replication asks whether a fresh study aimed at the same scientific question yields consistent findings, subject to its own uncertainty and design.

Generalization asks whether the result survives beyond the original context.

These are different evidentiary axes.

No one axis should silently substitute for the others.

## 13. Falsifiability belongs in the design

A claim becomes experimentally useful when the design makes clear what result would count against it.

That does not require reducing every scientific claim to one null-hypothesis test.

It does require a rejection, revision, or failure condition.

For example:

- if a claimed component matters, an isolated ablation should change the target outcome in a declared direction or range;
- if a scaling law is claimed, specified deviations should count against the proposed law;
- if a mechanism is claimed to improve stability, instability metrics should be defined before observing the candidate;
- if two methods are claimed equivalent, a tolerance and comparison domain should be stated.

A design that cannot lose is not a strong experimental argument.

A useful experiment risks changing our mind.

## 14. Repetition, replication, and robustness

Running the same code twice is not the same as repeating a randomized study.

Running more seeds is not the same as collecting new data.

Testing more benchmarks is not automatically the same as replication.

Using another implementation is not automatically the same as generalization.

The words matter because they describe different sources of variation.

A mature experimental report should say which axes were varied.

For example:

- same code, same data, same seed: deterministic replay check;
- same code and data, different seeds: stochastic execution variation;
- same method, new dataset sampled from same frame: replication-like evidence;
- new implementation, same intended method: implementation robustness;
- shifted population or domain: external generalization;
- altered nuisance conditions: robustness or stress testing.

The more precisely these are named, the less likely one form of evidence is to be mistaken for another.

## 15. The experiment table

A practical way to force the argument into view is to write the experiment as a table before running it.

| Field | Question |
|---|---|
| claim `q` | What proposition may change status? |
| estimand `theta` | What quantity is the experiment trying to learn? |
| units `U` | What population, tasks, examples, environments, or runs are sampled? |
| intervention `A` | What is deliberately changed or assigned? |
| nuisance `Z` | What else may affect the outcome? |
| outcome `Y` | What is measured and why is it relevant? |
| comparison `g` | How are observations converted into the target contrast? |
| variation `V` | Which uncertainty sources are sampled or estimated? |
| selection `rho` | How are stopping, tuning, and reporting determined? |
| scope `Omega` | Where may the conclusion be applied? |

This table is not a bureaucracy.

It is a compression of the experimental argument.

If the table cannot be completed, that is useful information before compute is spent.

## 16. Failure modes

Experiments fail in characteristic ways.

### Confounded comparison

The treatment groups differ in nuisance factors that also affect the outcome.

### Baseline asymmetry

One method receives more tuning, compute, data, or engineering effort.

### Hidden multiplicity

Many hypotheses or configurations are tried, but the report presents the selected result as if it were prespecified.

### Metric substitution

The measured metric drifts away from the actual scientific or engineering objective.

### Seed laundering

Seed variation is presented as if it covered data, population, or implementation uncertainty.

### Ablation overclaim

A compound system change is interpreted as evidence for one isolated mechanism.

### Reproducibility overclaim

Exact rerun is presented as evidence that the scientific conclusion is valid.

### Benchmark overclaim

Performance on a fixed benchmark is promoted into a universal capability or mechanism claim.

### Scope drift

A result established on one domain is written as if it held across a broader population.

These failures have one family resemblance:

**the claim becomes stronger than the design.**

## 17. Experiments in adaptive-intelligence research

Adaptive systems make experimental design unusually difficult because the object under study may itself change its behavior in response to:

- data order;
- feedback;
- memory;
- routing;
- learned state;
- tool outputs;
- environment dynamics;
- resource constraints.

A static A/B comparison may therefore hide path dependence.

For these systems, the unit of intervention may need to be:

- an episode;
- a trajectory;
- a task sequence;
- a training curriculum;
- a memory state;
- a coordination graph;
- a bounded agent policy.

The central discipline remains unchanged.

Name the unit.

Name the intervention.

Name the comparison.

Name the sources of variation.

Name the stopping rule.

Name the scope.

Then state only the claim that this design supports.

## 18. What this chapter establishes

This chapter does not certify any empirical architecture.

It establishes a reading and design grammar.

A downstream reader may now ask of any experiment:

1. What is the claim?
2. What is the estimand?
3. What creates the contrast?
4. What nuisance variables remain?
5. What kind of baseline or ablation is used?
6. Which randomness is sampled?
7. What effect magnitude is observed?
8. What uncertainty is represented?
9. How was the result selected?
10. What is reproducible?
11. What is replicated?
12. What mechanism, if any, is actually identified?
13. Where does the claim stop?

The exact confounding witness demonstrates why these questions matter.

A clean number can point in the wrong direction when the design mixes treatment with nuisance structure.

The cure is not statistical ornament.

It is experimental clarity.

## 19. Atlas handoff

**Replayable Evidence Objects — ATLAS-CH-REPLAY-001.**  
Replay may assume that an experiment has a declared claim, estimand, intervention/comparison structure, variation model, selection rule, and scope. Replay can then bind the exact data, code, environment, parameters, seeds, and outputs needed to reconstruct that experiment.

The dependency direction matters.

Replaying an experiment does not create its causal or scientific validity.

It preserves the experiment that was actually performed.

That preservation is powerful only when the experiment's argument was explicit in the first place.

## References used in this chapter

- NIST/SEMATECH e-Handbook of Statistical Methods, experimental-design sections [@NISTDOEHandbook].
- Rubin, *Estimating causal effects of treatments in randomized and nonrandomized studies* [@Rubin1974Causal].
- Wasserstein and Lazar, *The ASA Statement on p-Values: Context, Process, and Purpose* [@WassersteinLazar2016].
- National Academies of Sciences, Engineering, and Medicine, *Reproducibility and Replicability in Science* [@NASEM2019Reproducibility].
- Henderson et al., *Deep Reinforcement Learning That Matters* [@HendersonEtAl2018].

Exact source identities and authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-EXPERIMENT-001.yaml
