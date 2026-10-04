# Chapter Specification — ATLAS-CH-CURRICULUM-001

## Identity

**Title:** Curriculum Learning  
**Part:** Tokenization, Data, and Curriculum  
**Status:** specification-ready.  
**Epistemic class:** established curriculum-learning literature + audited Data/Optimization prerequisites + Atlas state-aware synthesis.

## Chapter contract

Study training-example ordering, difficulty, competence, automatic syllabus construction, and state-aware data selection without assuming monotone training progress.

The chapter must make the curriculum controller explicit enough to distinguish:

- what data are available;
- what the controller observes;
- what action the controller takes;
- how that action changes the effective training distribution;
- what learner state changes;
- what quantity is called progress;
- what remains unobserved.

The chapter must not equate a useful training signal with a mechanism-level explanation.

## Dependency contract

Hard prerequisites:

- ATLAS-CH-DATA-001;
- ATLAS-CH-OPTBASE-001.

May assume from DATA:

- dataset lineage;
- raw versus filtered/effective distributions;
- mixture weights;
- exact/near duplicate semantics;
- synthetic provenance;
- contamination/evaluation boundaries;
- the requirement to declare the counting and sampling measure.

May assume from OPTBASE:

- parameter state;
- optimizer state;
- stochastic-gradient semantics;
- schedules and warmup as training-recipe objects;
- clipping/adaptive updates;
- the distinction between optimization mechanics and architecture claims.

May use the project-local AGENDA-GSD-001 only as explicitly source-locked research context.

Must not assume:

- that lower nominal difficulty is always the best next sample;
- that competence is directly observed;
- that loss decrease proves durable acquisition;
- that curriculum benefit is separable from compute, exposure count, mixture weight, or optimizer schedule without a controlled comparison;
- that learning progress is a mechanism-level observable;
- that every curriculum should be monotone in difficulty;
- that the later Learning Progress as a Search Operator chapter has already supplied a search theory.

## Curriculum control object

Let the available experience set be \(\mathcal X\).

At training step \(t\), keep separate:

- model parameters \(\theta_t\);
- optimizer state \(u_t\);
- curriculum/controller state \(c_t\);
- training history \(H_t\);
- declared observation
  \[
  z_t=\Omega(\theta_t,u_t,c_t,H_t);
  \]
- curriculum action \(a_t\), such as choosing an example, domain, bucket, eligibility set, or sampling distribution;
- selected training experience \(x_t\sim Q(\cdot\mid a_t)\);
- declared post-update feedback \(f_t\), such as a loss, score, or other controller-visible measurement.

A curriculum policy is

\[
\pi_t(a\mid z_t,c_t).
\]

The training transition is

\[
(\theta_{t+1},u_{t+1})
=
\mathcal T_{\rm train}(\theta_t,u_t,x_t).
\]

The curriculum-state update is separately

\[
c_{t+1}
=
\mathcal T_{\rm curr}(c_t,z_t,a_t,x_t,f_t).
\]

The policy, learner transition, and controller-state transition are distinct objects.

## Open-loop versus closed-loop curricula

An open-loop schedule may be written

\[
\pi_t(a),
\]

or as a deterministic sequence \(a_t=\sigma(t)\).

It does not condition on current learner observations.

A closed-loop curriculum uses

\[
\pi_t(a\mid z_t,c_t).
\]

Two curricula can have the same nominal difficulty ordering and still differ because one adapts to learner state and the other does not.

## Difficulty

A difficulty score is a declared map

\[
d:\mathcal X\to\mathbb R.
\]

It may be based on length, rarity, teacher score, loss under a reference model, structural complexity, or another declared feature.

The chapter must state:

\[
\text{difficulty score}
\neq
\text{intrinsic universal difficulty}.
\]

Difficulty can depend on the learner, representation, objective, data preprocessing, and training stage.

## Competence schedule

A competence-based curriculum may define a scalar schedule \(q_t\) and eligibility set

\[
\mathcal X_t
=
\{x\in\mathcal X:d(x)\le q_t\}.
\]

This is a scheduling mechanism.

The chapter must not infer from the name “competence” that the learner has been proved competent on all examples below the threshold.

## Learning progress

For a declared evaluation region \(r\), metric \(m_t(r)\), lag/window \(w\), and orientation \(\eta_r\in\{+1,-1\}\), define

\[
LP_t(r)
=
\eta_r\left[m_t(r)-m_{t-w}(r)\right],
\]

where \(\eta_r=+1\) for a higher-is-better metric and \(\eta_r=-1\) for a lower-is-better metric.

Alternative signals are permitted, but their metric, window, orientation, noise handling, and observation scope must be declared.

The chapter must state:

\[
LP_t(r)
\neq
\text{direct observation of an internal learning mechanism}.
\]

## Sample selection versus mixture reweighting

Selecting a strict subset of examples and assigning a new probability distribution over an unchanged retained corpus are distinct interventions.

A selector may change support.

A reweighting policy may preserve support but alter probability mass.

Both can alter the effective training measure inherited from DATA.

## Fixed finite separation witness

Use two training actions:

- \(E\): nominally easy;
- \(H\): nominally hard.

Declare static difficulty:

\[
d(E)=1,
\qquad
d(H)=2.
\]

Learner state is

\[
s=(e,h)\in\{0,1,2\}^2.
\]

For this finite witness only, the controller observation is full state:

\[
z=s.
\]

Actions \(E\) and \(H\) select repeatable experience types rather than unique without-replacement records. These are explicit witness assumptions, not claims about real training systems.

Define total toy score

\[
M(e,h)=e+h.
\]

Easy transition:

\[
T_E(e,h)
=
(\min(2,e+1),h).
\]

Hard transition:

\[
T_H(e,h)
=
\begin{cases}
(e,\min(2,h+1)),&e\ge 1,\\
(e,h),&e=0.
\end{cases}
\]

Define one-step toy progress

\[
R(s,a)
=
M(T_a(s))-M(s).
\]

Then at

\[
s_A=(0,0),
\]

\[
R(s_A,E)=1,
\qquad
R(s_A,H)=0.
\]

At

\[
s_B=(2,0),
\]

\[
R(s_B,E)=0,
\qquad
R(s_B,H)=1.
\]

Therefore no state-independent first action chosen solely from the static ranking \(d(E)<d(H)\) is one-step progress-optimal for both \(s_A\) and \(s_B\).

The exact witness proves only this finite separation.

## Two-step witness

For learner state \(s_B=(2,0)\), compare equal two-update budgets.

Fixed easy-then-hard syllabus:

\[
E,H:
\qquad
(2,0)\to(2,0)\to(2,1),
\]

with cumulative progress \(1\).

A state-aware progress policy chooses \(H\) at \((2,0)\), then \(H\) again:

\[
H,H:
\qquad
(2,0)\to(2,1)\to(2,2),
\]

with cumulative progress \(2\).

This difference is generated entirely by the declared toy transition law.

It is not evidence that real neural networks should repeat “hard” examples.

## Principal pedagogical device

### Allegory: a teacher with a fixed lesson plan versus a teacher reading the room

A fixed lesson plan says what comes next before seeing the class.

A state-aware teacher observes declared evidence about what has already been learned and may choose a different next exercise.

The analogy maps to open-loop versus closed-loop curriculum control.

Limit:

A neural learner does not expose “understanding” directly. Its observable losses, accuracies, gradients, probes, or other measurements are partial signals. The allegory must not turn a metric into a claim about internal cognition.

## Literature roles

Use:

- Bengio et al. (2009) for the curriculum-learning formulation and continuation-method interpretation;
- Graves et al. (2017) for automated stochastic syllabus selection from learning-progress signals in their experiments;
- Platanios et al. (2019) for difficulty/competence-based curriculum scheduling in NMT.

Do not generalize their empirical outcomes beyond the reported settings.

## Generalization-state boundary

The project-local GSD agenda supplies one durable warning:

> Do not infer monotone mechanism improvement from smooth loss, more training, or endpoint benchmarks.

CURRICULUM-001 may use that warning to constrain interpretation.

It must not claim that a change in loss or accuracy identifies a hidden mechanism transition.

## Controlled-comparison obligations

A curriculum experiment should declare or control, as applicable:

- total optimizer updates;
- tokens/examples processed;
- duplicate/repeat exposure;
- wall-clock or resource budget;
- optimizer and learning-rate schedule;
- batch construction;
- model initialization and seeds;
- data support and sampling weights;
- evaluation timing;
- stopping rule;
- selection/tuning procedure.

A curriculum effect may otherwise be confounded with changed training dose or recipe.

## Failure boundaries

Include:

- easy-to-hard is not synonymous with curriculum learning;
- curriculum learning is not synonymous with self-paced learning;
- low loss is not intrinsic easiness;
- competence thresholds are not proof of competence;
- progress signals can be noisy, delayed, nonstationary, or saturated;
- maximizing immediate progress can sacrifice long-horizon value;
- a state-aware controller can overfit its own metric;
- a stochastic syllabus is not evidence of beneficial exploration by itself;
- curriculum selection can alter the effective data distribution and therefore the target being optimized;
- curriculum effects need not be monotone over training;
- endpoint gains do not establish mechanism change;
- state-aware selection is not automatically compute-efficient after controller overhead is counted.

## Downstream handoff

Direct consumer:

- ATLAS-CH-PROGRESSSEARCH-001.

That chapter may inherit:

- open-loop versus closed-loop curriculum semantics;
- declared progress signals;
- curriculum action and observation interfaces;
- the finite state-dependence separation;
- the distinction between progress signals and mechanism evidence.

It must independently define experience-space search, search objectives, exploration, credit assignment, and long-horizon search behavior.

## Sources

- [@BengioEtAl2009Curriculum]
- [@GravesEtAl2017Curriculum]
- [@PlataniosEtAl2019Curriculum]

Source lock:

sources/source-locks/ATLAS-CH-CURRICULUM-001.yaml

## Acceptance

The draft must:

- define a curriculum as an explicit policy/controller object;
- distinguish open-loop schedules from closed-loop state-aware policies;
- separate model, optimizer, and curriculum state;
- define difficulty and competence without ontological overclaim;
- define one explicit learning-progress signal and its measurement boundary;
- distinguish selection from mixture reweighting;
- derive the finite two-state separation witness exactly;
- keep source-specific empirical claims scoped;
- preserve the GSD non-monotonicity/mechanism boundary;
- include source lock, derivation packet, bounded computational witness, bibliography closure, ledger/register updates, tranche receipt, and post-draft audit.
