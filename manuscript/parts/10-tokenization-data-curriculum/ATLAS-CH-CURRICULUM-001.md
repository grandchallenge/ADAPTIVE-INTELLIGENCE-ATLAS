# Curriculum Learning

**Epistemic status:** established curriculum-learning literature + audited Data/Optimization prerequisites + Atlas state-aware synthesis.

A curriculum is often summarized as “show easy examples first, then harder ones.”

That description captures one historical intuition, but it is too narrow for a mathematical atlas.

The deeper object is a controller over training experience.

It decides, explicitly or implicitly, what the learner sees next.

Sometimes the controller is fixed before training begins. Sometimes it reacts to measurements of the learner. Sometimes it changes only the probability of sampling different regions of the same corpus. Sometimes it removes examples from the eligible set. Sometimes it uses a nominal difficulty score. Sometimes it uses a signal called learning progress.

These mechanisms are not equivalent.

The central lesson of this chapter is:

> **Curriculum learning is a control problem over the effective training distribution. A useful curriculum must be defined by its available experiences, observations, state, actions, and update rule. Static difficulty order is one special case, not the definition.**

The source tradition begins with curriculum learning as an organized presentation of examples [@BengioEtAl2009Curriculum], extends to automatic syllabus selection driven by learning-progress signals [@GravesEtAl2017Curriculum], and includes competence-based scheduling that couples example difficulty to a model-training schedule [@PlataniosEtAl2019Curriculum].

The audited Data chapter supplies the data-distribution and evidence semantics.

The audited First-Order Optimization chapter supplies the optimizer-state and training-recipe boundary.

## 1. The question is not merely “easy or hard?”

Suppose a dataset contains two kinds of examples.

One kind has a lower declared difficulty score than the other.

A fixed easy-to-hard syllabus can sort them and move through that ordering.

But what if the learner has already exhausted what the easy region can teach?

What if the learner is not yet ready for the nominally hard region?

What if two learners at the same training step occupy different states because of initialization, stochastic gradients, routing, or earlier examples?

Then “difficulty” alone is not enough to specify the useful next experience.

A curriculum must answer a stronger question:

> Given the learner information that the controller is allowed to observe, what training experience distribution should be used next?

That is a policy question.

## 2. Three states, not one

At training step \(t\), keep at least three categories separate.

### 2.1 Model state

Let

\[
\theta_t
\]

denote model parameters or another declared model state.

### 2.2 Optimizer state

Let

\[
u_t
\]

denote optimizer state: momentum, adaptive moments, schedules, or other quantities required by the optimizer.

The audited Optimization chapter already established that optimizer motion is not determined by the raw gradient alone.

### 2.3 Curriculum state

Let

\[
c_t
\]

denote controller state.

It can contain:

- syllabus position;
- current competence threshold;
- sampling weights;
- region statistics;
- progress estimates;
- counters;
- eligibility masks;
- controller-bandit state.

These coordinates are not model parameters merely because they evolve during training.

The complete controller need not observe all of \(\theta_t\) or \(u_t\).

Instead declare an observation

\[
z_t
=
\Omega(\theta_t,u_t,c_t,H_t),
\]

where \(H_t\) is whatever training/evaluation history is available to the controller.

The observation function matters.

A controller that sees only aggregate loss has a different information contract from one that sees per-domain validation, gradients, probes, or held-out competence tests.

## 3. Curriculum as a policy

Let \(\mathcal X\) be the available experience space.

A curriculum action \(a_t\) can mean many things:

- choose one example;
- choose a bucket;
- choose a domain;
- choose a task;
- set sampling weights;
- set an eligibility threshold;
- select a replay source;
- choose a stochastic syllabus arm.

Write the curriculum policy as

\[
\pi_t(a\mid z_t,c_t).
\]

Then a sampling kernel produces a training experience

\[
x_t\sim Q(\cdot\mid a_t).
\]

The learner updates through

\[
(\theta_{t+1},u_{t+1})
=
\mathcal T_{\rm train}(\theta_t,u_t,x_t).
\]

The controller may update separately. Let \(f_t\) denote the declared post-update feedback visible to the controller, such as a loss or evaluation score. Then

\[
c_{t+1}
=
\mathcal T_{\rm curr}(c_t,z_t,a_t,x_t,f_t).
\]

This decomposition matters because a curriculum is not the optimizer.

It changes which training evidence reaches the optimizer.

## 4. Open loop and closed loop

The simplest curriculum is open loop.

A deterministic syllabus is

\[
a_t=\sigma(t).
\]

It can be sophisticated.

It can increase difficulty gradually, cycle domains, interleave tasks, or follow a handcrafted sequence.

It is still open loop if the next action does not depend on current learner observations.

A stochastic open-loop curriculum can use

\[
a_t\sim\pi_t(a).
\]

Randomness does not make a curriculum adaptive.

A closed-loop curriculum uses feedback:

\[
a_t\sim\pi_t(a\mid z_t,c_t).
\]

Now the same training step \(t\) can produce different curriculum actions for two learners with different observed states.

This distinction is more fundamental than “easy first.”

## 5. Difficulty is a score, not an essence

Let

\[
d:\mathcal X\to\mathbb R
\]

be a declared difficulty score.

Examples of possible scoring rules include:

- sequence length;
- rarity;
- number of compositional steps;
- reference-model loss;
- teacher-model confidence;
- structural depth;
- human difficulty labels;
- corruption level.

Each score embeds assumptions.

A long example can be easy for one model and hard for another.

A sample with high loss can be informative, mislabeled, out-of-distribution, adversarial, or merely underfit.

Therefore:

\[
\boxed{
\text{declared difficulty score}
\neq
\text{intrinsic universal difficulty}
}
\]

Bengio et al. introduced curriculum learning around meaningful organization of examples and explored a continuation-method interpretation [@BengioEtAl2009Curriculum].

The Atlas keeps that historical role while refusing to turn “easy” into an observer-independent property.

## 6. Competence schedules

A competence-based curriculum can couple the difficulty score to a threshold.

Let

\[
q_t
\]

be a schedule and define the eligible set

\[
\mathcal X_t
=
\{x\in\mathcal X:d(x)\le q_t\}.
\]

As \(q_t\) grows, more examples become eligible.

Platanios et al. use estimated example difficulty and model competence in a curriculum framework for neural machine translation [@PlataniosEtAl2019Curriculum].

The Atlas uses that work as a representative mechanism.

It does not infer:

\[
q_t
=
\text{true competence}.
\]

The controller variable is a scheduling construct.

Any stronger claim about actual competence needs its own measurement contract.

## 7. Automated curricula and learning progress

Graves et al. show one way to automate curriculum construction: use signals derived from learning progress as reward for a nonstationary bandit that selects a stochastic syllabus [@GravesEtAl2017Curriculum].

This introduces an important architectural shift.

The curriculum is no longer merely an ordered list.

It becomes a controller that receives a reward-like signal and reallocates training attention.

A generic finite-difference progress signal for region \(r\) must also state which metric direction counts as improvement. Let \(\eta_r\in\{+1,-1\}\). Define

\[
LP_t(r)
=
\eta_r\left[m_t(r)-m_{t-w}(r)\right],
\]

where \(m_t(r)\) is a declared metric, \(w\) is a declared lag, \(\eta_r=+1\) for higher-is-better metrics, and \(\eta_r=-1\) for lower-is-better metrics.

This signal has a measurement contract.

It depends on:

- the metric;
- the window;
- evaluation noise;
- sampling frequency;
- smoothing;
- region definition;
- whether higher or lower is better.

A different window can reverse which region appears to have the highest current progress.

## 8. Learning progress is not a mechanism readout

Suppose validation accuracy rises quickly on one region.

That is evidence about the declared behavioral metric.

It does not by itself prove:

- which internal feature was acquired;
- whether the capability will persist;
- whether it is accessible under distribution shift;
- whether the model used the intended mechanism;
- whether later training will erase or mask it.

For curriculum design, the practical consequence is simple.

A progress metric can be useful as a controller signal without being a complete scientific explanation.

That distinction lets us use feedback without overclaiming what feedback means.

## 9. Selection is not the same as reweighting

The audited Data chapter separates the retained corpus from the effective training measure.

Curriculum learning operates on that interface.

Suppose the corpus is \(\mathcal D\) with base sampling measure \(\mu\).

A reweighting curriculum can define

\[
\mu_t'(x)
=
\frac{w_t(x)\mu(x)}
{\sum_{x'}w_t(x')\mu(x')}.
\]

If every weight stays positive, the support is unchanged even though probability mass moves.

A selector can instead choose

\[
S_t\subseteq\mathcal D
\]

and sample only from \(S_t\).

Now support changes.

This distinction matters for:

- exposure;
- contamination accounting;
- rare domains;
- replay;
- fairness of comparisons;
- target-distribution interpretation.

“Curriculum changed the data” is too vague.

We should say how.

## 10. A finite state-aware separation

The smallest useful witness needs no neural network.

Let the learner state be

\[
s=(e,h)\in\{0,1,2\}^2.
\]

Interpret the coordinates only as toy learning levels.

For this exact witness, the curriculum controller observes the entire toy state:

\[
z=s.
\]

This full-observability assumption is deliberately stronger than the partial measurements available in most real training systems. The actions \(E\) and \(H\) denote repeatable experience types, so the same type may be selected on successive updates.

There are two actions:

\[
E=\text{nominally easy},
\qquad
H=\text{nominally hard}.
\]

Static difficulty is

\[
d(E)=1,
\qquad
d(H)=2.
\]

The easy update is

\[
T_E(e,h)
=
(\min(2,e+1),h).
\]

The hard update is

\[
T_H(e,h)
=
\begin{cases}
(e,\min(2,h+1)),&e\ge1,\\
(e,h),&e=0.
\end{cases}
\]

The hard coordinate has one toy prerequisite: \(e\ge1\).

Define

\[
M(e,h)=e+h
\]

and one-step progress

\[
R(s,a)
=
M(T_a(s))-M(s).
\]

Now compare two learner states.

### 10.1 Learner A

At

\[
s_A=(0,0),
\]

easy gives

\[
R(s_A,E)=1.
\]

Hard gives

\[
R(s_A,H)=0.
\]

Easy is uniquely progress-maximizing.

### 10.2 Learner B

At

\[
s_B=(2,0),
\]

the easy coordinate is saturated.

Therefore

\[
R(s_B,E)=0.
\]

Hard is available and gives

\[
R(s_B,H)=1.
\]

Hard is uniquely progress-maximizing.

The nominal ranking

\[
d(E)<d(H)
\]

is identical for both learners.

The useful next action is not.

Therefore:

\[
\boxed{
\text{static difficulty order}
\not\Rightarrow
\text{state-uniform next-action optimality}
}
\]

in this finite system.

That is the chapter’s exact theorem-grade witness.

## 11. What the witness does not say

The witness does not say that real training contains an “easy coordinate” and a “hard coordinate.”

It does not say that hard examples require a simple prerequisite.

It does not say that immediate progress is the correct objective.

It does not say that a neural model at high performance on easy data is permanently saturated.

It establishes one logical point only:

> If training utility depends on learner state, a state-independent ranking can fail to choose the same useful next experience for all learner states.

That is enough to justify treating state-aware curriculum control as a distinct object.

## 12. Equal-budget two-step replay

Start from

\[
s_B=(2,0).
\]

Give both curricula exactly two learner transitions.

A fixed easy-then-hard syllabus does:

\[
(2,0)
\xrightarrow{E}
(2,0)
\xrightarrow{H}
(2,1).
\]

Toy progress is

\[
1.
\]

A state-aware immediate-progress policy does:

\[
(2,0)
\xrightarrow{H}
(2,1)
\xrightarrow{H}
(2,2).
\]

Toy progress is

\[
2.
\]

The comparison is intentionally bounded.

Both execute two learner updates.

The witness does not account for controller computation, evaluation overhead, measurement latency, or partial-state estimation. Its repeated \(H,H\) action is legal only because the witness explicitly defines \(H\) as a repeatable experience type.

## 13. Why immediate progress is not enough

A tempting rule is:

> Always train on the region with the largest current learning progress.

That rule can be useful.

It is not automatically optimal.

An action with small immediate gain may unlock a later region.

A region with zero observed progress may already be mastered and need occasional rehearsal.

A region with high progress may be noisy and temporarily flattering the metric.

A region may need exploration before its learning potential can be estimated.

These long-horizon questions belong partly to the later Learning Progress as a Search Operator chapter.

CURRICULUM-001 defines the controller interface that chapter will consume.

It does not pre-solve search.

## 14. Curriculum versus training dose

Suppose two experiments end at the same wall-clock time, but one sees more tokens.

Or they see the same number of examples, but one repeats easy examples more often.

Or they see the same corpus, but one uses a different learning-rate schedule.

Then “curriculum effect” is not yet isolated.

A credible comparison should declare or control, as appropriate:

- optimizer-update count;
- examples or tokens processed;
- repeated exposure;
- batch size;
- optimizer;
- learning-rate schedule;
- model initialization;
- seeds;
- controller evaluation cost;
- data support;
- sampling weights;
- stopping rule;
- tuning procedure.

The required controls depend on the claim.

The principle is inherited from the Atlas evidence discipline:

> attribute only what the experiment isolates.

## 15. Curriculum and mixture optimization

Curriculum learning can look like time-dependent mixture optimization.

The overlap is real.

If a curriculum chooses domain weights \(w_t\), it changes the effective sampling distribution.

But the concepts are not identical.

Mixture optimization can seek a fixed or slowly varying distribution without an easy-to-hard semantics.

Curriculum learning can change support, ordering, eligibility, or task structure.

The useful abstraction is not a label.

It is the explicit policy over experiences.

## 16. Stochastic syllabi

A curriculum can be stochastic.

For example,

\[
a_t\sim\pi_t(a\mid z_t,c_t).
\]

Stochasticity can support:

- exploration;
- robustness to noisy progress estimates;
- coverage;
- softened eligibility;
- bandit-style allocation.

But stochasticity itself proves nothing about exploration quality.

A random controller can be worse than a deterministic one.

The exploration objective and feedback model must be declared.

## 17. When loss is a bad difficulty proxy

Current loss is attractive because it is already available.

But high loss can mean many things.

An example may be:

- genuinely complex;
- mislabeled;
- out-of-distribution;
- rare;
- adversarial;
- corrupted;
- already memorized but evaluated under noise;
- incompatible with the current objective.

Likewise low loss can mean:

- mastered;
- trivial;
- duplicated;
- leaked;
- overrepresented.

Therefore a loss-based curriculum must say what interpretation it assumes.

The Data chapter’s lineage and duplication semantics are directly relevant here.

## 18. The fixed lesson plan and the teacher reading the room

The chapter’s pedagogical analogy is a teacher with two possible modes.

The fixed lesson plan is open loop.

It says:

> Lesson 1, then lesson 2, then lesson 3.

The adaptive teacher reads declared evidence about the class and may alter the next exercise.

That is closed loop.

The analogy is useful because it exposes the information path.

It fails if we pretend the teacher sees “understanding” directly.

A machine-learning controller sees measurements.

The quality of those measurements is part of the system.

## 19. Failure modes

### 19.1 Easy-to-hard as dogma

A curriculum can be useful without monotone difficulty.

A learner may need rehearsal, interleaving, or revisiting prerequisite regions.

### 19.2 Competence by naming

A variable called competence is still a variable.

The name does not prove that it measures actual competence.

### 19.3 Progress as mechanism

A rising metric is not a direct scan of internal learning.

### 19.4 Greedy progress as global policy

One-step gain need not maximize long-horizon capability.

### 19.5 Hidden dose changes

If one curriculum trains longer or sees more useful examples, ordering may not be the only causal difference.

### 19.6 Controller overfitting

A closed-loop curriculum can optimize its own progress metric rather than the true downstream objective.

### 19.7 Support drift

Aggressive selection can stop exposing the learner to important regions.

### 19.8 Noise chasing

A controller can repeatedly select regions whose progress estimates are noisy rather than genuinely useful.

### 19.9 Endpoint-only interpretation

An endpoint improvement does not explain when, how, or why the capability emerged.

### 19.10 Ignoring controller cost

A curriculum can reduce learner updates while increasing measurement, scheduling, or data-pipeline cost.

## 20. What later chapters may assume

Learning Progress as a Search Operator may assume:

- a curriculum action space exists;
- open-loop and closed-loop controllers are distinct;
- progress signals have explicit measurement contracts;
- data selection changes the effective training measure;
- learner state and curriculum state are separate;
- static difficulty order need not be state-uniformly optimal;
- curriculum feedback is evidence for control, not automatically evidence for mechanism.

It must independently add:

- experience-space search;
- exploration;
- long-horizon objectives;
- credit assignment;
- uncertainty over progress estimates;
- search stopping rules.

Minimal Curricula and Reasoning Bases remains further downstream.

It may not inherit a claim that the smallest curriculum is the one with the highest short-term progress.

## 21. Epistemic status

Established external literature:

- curriculum learning as organized training-example presentation and continuation-style motivation [@BengioEtAl2009Curriculum];
- automated stochastic syllabus selection using learning-progress signals in the reported settings [@GravesEtAl2017Curriculum];
- difficulty/competence-based scheduling for NMT in the reported setting [@PlataniosEtAl2019Curriculum].

Audited Atlas prerequisites:

- data lineage, sampling measure, mixture semantics, contamination boundaries;
- optimizer and schedule mechanics.

Atlas-owned synthesis:

- curriculum as an explicit control object over the effective training distribution;
- the separation among model, optimizer, curriculum state, and curriculum observation;
- the exact finite state-dependent next-action witness;
- the claim firewall between progress signals and mechanism claims.

Computational witness:

- exact nine-state transition/progress table;
- unique action reversal between \((0,0)\) and \((2,0)\);
- equal-two-transition comparison from \((2,0)\).

Not established here:

- universal curriculum gains;
- universal easy-to-hard optimality;
- direct observability of competence;
- long-horizon optimality of greedy progress;
- mechanism identification from behavioral metrics;
- compute savings in deployed training systems.

## References used in this chapter

- [@BengioEtAl2009Curriculum] — foundational curriculum-learning formulation and continuation-method interpretation.
- [@GravesEtAl2017Curriculum] — automated curriculum/syllabus selection from learning-progress signals.
- [@PlataniosEtAl2019Curriculum] — competence-based curriculum scheduling for neural machine translation.

Exact provenance and authority boundaries are locked in:

sources/source-locks/ATLAS-CH-CURRICULUM-001.yaml
