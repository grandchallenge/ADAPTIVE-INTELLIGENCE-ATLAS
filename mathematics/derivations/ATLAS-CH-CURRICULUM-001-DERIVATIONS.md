# Derivations — ATLAS-CH-CURRICULUM-001

## Scope

This packet supports the formal distinctions and finite witness used by Curriculum Learning.

It does not prove that any curriculum improves a real neural network.

It does not identify a mechanism of learning from loss, accuracy, or another behavioral metric.

## 1. Learner and curriculum state are separate

Write learner optimization state as

\[
y_t=(\theta_t,u_t),
\]

where \(\theta_t\) is model state and \(u_t\) is optimizer state.

Write curriculum state separately as \(c_t\).

A declared observable is

\[
z_t=\Omega(y_t,c_t,H_t),
\]

where \(H_t\) is the retained training/evaluation history available to the controller.

The curriculum chooses

\[
a_t\sim\pi_t(\cdot\mid z_t,c_t).
\]

Then a data-selection kernel chooses

\[
x_t\sim Q(\cdot\mid a_t).
\]

The learner updates through

\[
y_{t+1}
=
\mathcal T_{\rm train}(y_t,x_t).
\]

The controller state updates through

\[
c_{t+1}
=
\mathcal T_{\rm curr}(c_t,z_t,a_t,x_t,\ell_t).
\]

This decomposition prevents three different objects from being collapsed:

\[
\text{learner state}
\neq
\text{controller state}
\neq
\text{controller observation}.
\]

## 2. Open-loop schedule

An open-loop deterministic curriculum is a sequence

\[
a_t=\sigma(t).
\]

More generally, an open-loop stochastic curriculum can use

\[
a_t\sim\pi_t(a),
\]

where the distribution may depend on time but not on the current learner observation.

Open-loop does not mean uniform or random.

A highly structured easy-to-hard syllabus can still be open-loop.

## 3. Closed-loop curriculum

A closed-loop curriculum uses

\[
a_t\sim\pi_t(a\mid z_t,c_t).
\]

The distinguishing feature is feedback.

The policy may react to declared evidence about current training state.

The feedback can be poor, delayed, noisy, or misleading; closed-loop is a structural classification, not a quality guarantee.

## 4. Difficulty is a declared score

Let

\[
d:\mathcal X\to\mathbb R.
\]

A curriculum may order examples by \(d\), but the score itself is produced by a declared rule.

If two learners have different states, the same sample can produce different gradients, losses, or learning effects even when \(d(x)\) is fixed.

Therefore static difficulty order does not determine state-dependent utility without additional assumptions.

## 5. Competence schedule

Let \(q_t\) be a nondecreasing scalar schedule.

Define the eligible set

\[
\mathcal X_t
=
\{x:d(x)\le q_t\}.
\]

This formalizes one competence-style curriculum.

The name “competence” does not alter the mathematics: \(q_t\) is a controller variable, and \(\mathcal X_t\) is an eligibility set.

Any claim that \(q_t\) equals actual learner competence needs separate evidence.

## 6. Learning-progress signal

For a region \(r\), evaluation metric \(m_t(r)\), and lag \(w\),

\[
LP_t(r)
=
m_t(r)-m_{t-w}(r).
\]

This is a finite-difference observation.

Changing \(w\) changes the signal.

If \(m_t\) is noisy, \(LP_t\) is noisy.

If performance saturates, \(LP_t\) can approach zero even when retained capability remains high.

If performance temporarily drops while representations reorganize, signed progress can be negative without proving destructive learning.

Thus:

\[
LP_t
\]

is a controller signal, not a mechanism theorem.

## 7. Sample selection and reweighting

Let the retained corpus be \(\mathcal D\) with base measure \(\mu\).

A reweighting controller produces a new probability measure

\[
\mu_t'(x)
=
\frac{w_t(x)\mu(x)}
{\sum_{x'\in\mathcal D}w_t(x')\mu(x')},
\]

for nonnegative weights \(w_t\), provided the denominator is positive.

Support can remain unchanged.

A selector may instead choose a subset

\[
S_t\subseteq\mathcal D
\]

and sample only from \(S_t\).

Then support can change.

The two interventions may coincide in limiting cases but are not definitionally identical.

## 8. Finite state-aware witness

### 8.1 State and actions

State:

\[
s=(e,h)\in\{0,1,2\}^2.
\]

Actions:

\[
\mathcal A=\{E,H\}.
\]

Static difficulty:

\[
d(E)=1<2=d(H).
\]

Toy aggregate score:

\[
M(e,h)=e+h.
\]

### 8.2 Transition rules

Easy action:

\[
T_E(e,h)
=
(\min(2,e+1),h).
\]

Hard action:

\[
T_H(e,h)
=
\begin{cases}
(e,\min(2,h+1)),&e\ge1,\\
(e,h),&e=0.
\end{cases}
\]

The prerequisite \(e\ge1\) is part of the toy model.

It is not asserted to represent neural training generally.

### 8.3 One-step progress reward

Define

\[
R(s,a)
=
M(T_a(s))-M(s).
\]

At

\[
s_A=(0,0),
\]

easy action gives

\[
T_E(s_A)=(1,0),
\]

so

\[
R(s_A,E)=1.
\]

Hard action is blocked:

\[
T_H(s_A)=(0,0),
\]

so

\[
R(s_A,H)=0.
\]

Therefore \(E\) is the unique one-step progress maximizer at \(s_A\).

At

\[
s_B=(2,0),
\]

easy is saturated:

\[
T_E(s_B)=(2,0),
\]

so

\[
R(s_B,E)=0.
\]

Hard is available:

\[
T_H(s_B)=(2,1),
\]

so

\[
R(s_B,H)=1.
\]

Therefore \(H\) is the unique one-step progress maximizer at \(s_B\).

### 8.4 Separation proposition

Suppose a first-action rule ignores state and chooses only from the fixed nominal ranking

\[
d(E)<d(H).
\]

If it always chooses \(E\) first, it is not progress-optimal at \(s_B\).

If it always chooses \(H\) first, it is not progress-optimal at \(s_A\).

Hence no state-independent deterministic first action is one-step progress-optimal for both states.

This is the exact separation.

It proves:

\[
\text{static nominal order}
\not\Rightarrow
\text{state-uniform next-action optimality}
\]

in this finite model.

It does not prove that a state-aware curriculum is globally optimal in general.

## 9. Equal-budget two-step comparison

Start from

\[
s_B=(2,0).
\]

Fixed easy-then-hard syllabus:

\[
E,H.
\]

Step 1:

\[
(2,0)\xrightarrow{E}(2,0).
\]

Step 2:

\[
(2,0)\xrightarrow{H}(2,1).
\]

Cumulative toy progress:

\[
M(2,1)-M(2,0)=1.
\]

A state-aware immediate-progress policy chooses \(H\) at the initial state.

After one step:

\[
(2,0)\xrightarrow{H}(2,1).
\]

At \((2,1)\),

\[
R((2,1),H)=1,
\]

while easy remains saturated:

\[
R((2,1),E)=0.
\]

So it chooses \(H\) again:

\[
(2,1)\xrightarrow{H}(2,2).
\]

Cumulative toy progress:

\[
M(2,2)-M(2,0)=2.
\]

The comparison uses equal numbers of training transitions.

It does not model unequal controller overhead.

## 10. Immediate progress is not long-horizon value

Define one-step greedy curriculum policy

\[
\pi_{\rm greedy}(s)
\in
\arg\max_a R(s,a).
\]

Nothing in the finite witness proves

\[
\pi_{\rm greedy}
=
\arg\max_\pi
\mathbb E[M(s_T)]
\]

for arbitrary horizons, transition systems, or stochastic environments.

A curriculum may need to choose an action with small immediate progress to unlock later states.

Therefore the later Learning Progress as a Search Operator chapter must independently handle long-horizon search and exploration.

## 11. Dose and recipe confounding

Suppose curriculum A processes \(N_A\) examples and curriculum B processes \(N_B\).

If

\[
N_A\neq N_B,
\]

an endpoint difference cannot be attributed solely to ordering without additional design or analysis.

The same applies to:

- optimizer updates;
- token count;
- batch size;
- learning-rate schedule;
- repeated examples;
- wall-clock/resource budget.

Curriculum is an intervention on training experience allocation. Its comparison contract must isolate that intervention as far as the claim requires.

## 12. Generalization-state boundary

The project-local GSD agenda requires separation among:

- acquisition;
- persistence;
- accessibility;
- behavioral expression.

A curriculum metric such as loss or benchmark accuracy observes only a declared behavioral/training surface.

Therefore:

\[
\text{metric change}
\not\Rightarrow
\text{identified mechanism transition}.
\]

This is an epistemic boundary, not a claim that mechanism changes never occur.

## 13. Claim boundary

The exact derivations establish:

- the open-loop/closed-loop structural distinction;
- one explicit learning-progress signal;
- support-changing selection versus support-preserving reweighting;
- the finite state-dependent next-action separation;
- the equal-transition-budget arithmetic of the toy witness.

They do not establish:

- universal superiority of curriculum learning;
- universal easy-to-hard optimality;
- reliable observability of competence;
- mechanism identification from learning progress;
- long-horizon optimality of greedy progress;
- compute savings in real systems.
