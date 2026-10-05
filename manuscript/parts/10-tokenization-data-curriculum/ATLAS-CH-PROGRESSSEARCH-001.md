# Learning Progress as a Search Operator
<!-- ATLAS-CH-PROGRESSSEARCH-001 -->

**Epistemic status:** audited Curriculum prerequisite + primary learning-progress/search sources + Atlas synthesis + exact finite witnesses  
**Specification:** manuscript/specifications/ATLAS-CH-PROGRESSSEARCH-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-PROGRESSSEARCH-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-PROGRESSSEARCH-001.md

A curriculum controller asks what the learner should see next.

A search controller asks a stronger question:

> Which part of experience space should be investigated next, including regions we have not yet characterized?

That extra phrase changes the problem.

Learning progress can rank known regions. Search must also decide when to leave them.

## 1. The inherited progress signal

The audited Curriculum chapter already defines an oriented progress signal

\[
LP_t(r)=\eta_r[m_t(r)-m_{t-w}(r)],
\]

with an explicit metric, lag, orientation, noise boundary, and observation scope.

PROGRESSSEARCH keeps all of those restrictions.

A large positive value means only that the declared metric moved in the declared favorable direction over the chosen window.

It does not prove a mechanism was acquired.

## 2. From curriculum control to search

Curriculum control can operate over a known menu of examples, buckets, domains, or distributions.

Search becomes explicit when the controller must also decide which regions deserve measurement, refinement, or generation.

Let the experience space be \(\mathcal E\). It may be finite, partitioned, or continuously parameterized.

Define the search state

\[
\mathfrak S_t=(\mathcal E,z_t,h_t,\widehat{LP}_t,u_t,g_t,\Phi_t,H,B_t).
\]

The new pieces are not cosmetic:

- \(h_t\): what the search process has already tried;
- \(u_t\): coverage or uncertainty;
- \(g_t\): declared generalization-state evidence;
- \(\Phi_t\): the search objective or ordering rule;
- \(H\): the horizon used for value/credit;
- \(B_t\): remaining budget.

The search operator is

\[
r_t\sim\mathcal S_t(\cdot\mid\mathfrak S_t).
\]

## 3. Why progress is attractive

Progress is different from raw performance.

A region with high performance but no remaining improvement may be saturated.

A region with low performance and no improvement may be presently unlearnable, badly measured, or simply unexplored.

A region with moderate performance and rapid improvement may be a productive frontier.

This intuition appears in progress-sensitive intrinsic-motivation systems and competence-progress goal exploration [@OudeyerKaplanHafner2007IntrinsicMotivation] [@BaranesOudeyer2013GoalExploration].

Portelas et al. make the search interpretation explicit in a continuously parameterized environment space, using absolute learning progress inside a surrogate teacher/bandit problem [@PortelasEtAl2020TeacherAlgorithms].

The Atlas adopts the structural idea without importing a universal optimality claim.

## 4. Search needs exploration

If the controller only chooses the largest progress estimate among regions it has already measured, an unseen region can remain unseen forever.

That is exploitation, not complete search.

Search therefore needs a declared rule for unobserved or uncertain regions.

Possible rules include:

- forced coverage;
- random exploration;
- optimism/uncertainty bonuses;
- posterior sampling;
- novelty or diversity constraints;
- hierarchical refinement of promising regions.

No one rule is privileged by definition.

## 5. Exact exploration witness

Use two regions A and B.

A has been measured and gives progress 1.

B is unobserved but, when sampled in the toy system, gives progress 3.

An exploit-only policy restricted to observed regions chooses A twice:

\[
1+1=2.
\]

A coverage-first policy samples B once, observes 3, then selects B again:

\[
3+3=6.
\]

Therefore:

\[
\boxed{
\text{greedy over observed regions}
\not\Rightarrow
\text{discovery of a better unobserved region}
}.
\]

The result is finite and exact.

It does not say that forced coverage is always best.

## 6. Generalization-state evidence is not one scalar

The GSD boundary distinguishes evidence about:

- acquisition;
- persistence;
- accessibility;
- behavioral expression.

Write

\[
g_t(r)=\bigl(g_t^{acq},g_t^{pers},g_t^{access},g_t^{expr}\bigr)(r).
\]

These coordinates can disagree.

A capability can appear acquired but fail persistence checks.

It can persist but become inaccessible to one readout.

It can be accessible but not behaviorally expressed under the tested distribution.

Search may use these observations, but it must not silently collapse them into a mechanism label.

## 7. Heterogeneous evidence needs an ordering rule

Progress, uncertainty, persistence evidence, cost, and novelty do not necessarily share units.

A controller may use a scalarization, lexicographic rule, constrained optimization, or multi-objective policy.

But that rule is part of the algorithm.

Writing

\[
\Phi_t(\widehat{LP},u,g,c,B,H)
\]

does not itself justify adding the arguments numerically.

## 8. Immediate progress can be the wrong horizon

Learning progress is often measured locally in time.

Search value can be delayed.

Consider a two-step toy system.

Action G gives immediate progress 2 but moves to a state with no second-step gain.

Action I gives immediate progress 0 but unlocks a second-step action X worth 5.

Immediate greed chooses G and obtains total return 2.

The path I,X obtains 5.

Thus:

\[
\boxed{
\text{max immediate progress}
\not\Rightarrow
\text{max finite-horizon return}
}.
\]

## 9. Credit assignment is separate from search

Suppose an experience chosen now is followed by several updates before a later validation gain appears.

Which earlier experience gets credit?

A declared H-step return can be written

\[
G_t^{(H)}=\sum_{k=0}^{H-1}\gamma^k r_{t+k}.
\]

But that is only a temporal aggregation rule.

It does not prove causal attribution.

If several data regions, optimizer updates, or interventions occur in between, the attribution method must be stated separately.

## 10. Absolute learning progress needs care

Some systems use

\[
|LP_t(r)|
\]

rather than signed progress.

This can be useful when any strong change signals a region worth revisiting.

But magnitude is not direction.

A large absolute change may reflect improvement, forgetting, degradation, noise, or nonstationarity.

Therefore:

\[
\boxed{|LP|\neq\text{beneficial learning}.}
\]

## 11. Search changes the training intervention

A search controller can change:

- which regions are sampled;
- how often they are sampled;
- which regions are never sampled;
- how much controller computation is spent;
- the order and dependence structure of training experience.

That means search can change the effective training distribution.

A fair experiment must still inherit the Curriculum comparison obligations for training dose, optimizer schedule, exposure, stopping rule, and controller overhead.

## 12. Search can overfit its metric

A controller may repeatedly select regions that look productive only because the progress estimate is noisy or easy to game.

A search policy can therefore overfit its own feedback channel.

Useful checks include:

- held-out evaluation;
- alternate windows;
- persistence checks;
- delayed reevaluation;
- cross-region validation;
- robustness to progress-estimator noise.

These checks reduce ambiguity but do not turn the signal into a mechanism oracle.

## 13. Search does not mean permanent novelty

Exploration is not synonymous with choosing something new at every step.

Once a productive region is found, exploitation can be rational.

Likewise, revisiting an old region can be rational when forgetting or transfer changes its value.

The correct balance depends on the declared objective and horizon.

## 14. Search over generated experience

The experience space need not be a fixed dataset.

A region can parameterize:

- a simulator;
- a synthetic-data generator;
- a task template;
- a goal distribution;
- a transformation family;
- a problem generator.

In that case, the search operator chooses conditions under which new experience is produced.

This makes the support itself adaptive.

The provenance of generated experience must therefore remain explicit.

## 15. What search has not yet solved

Even a good progress-search operator does not answer:

- what the smallest sufficient curriculum is;
- which learned mechanisms are transferable;
- which reasoning operations form a reconstructive basis;
- whether the same basis works across model scales;
- whether early mechanisms remain latent after later training.

Those are downstream questions.

## 16. Handoff to Minimal Curricula and Reasoning Bases

ATLAS-CH-MINCURR-001 may now assume:

- explicit experience-space search;
- progress estimates with their observation contract;
- an exploration/coverage state;
- delayed-credit and finite-horizon semantics;
- generalization-state evidence as a non-oracular vector;
- exact examples where exploit-only and immediate-greedy choice fail.

MINCURR must add a criterion of minimality and reconstructability.

Finding a high-progress region is not the same as finding a minimal transferable basis.

## 17. Durable lesson

Learning progress can do more than order a syllabus.

It can become feedback for where to look next.

But once progress becomes a search signal, the missing pieces become unavoidable:

\[
\text{search}
=
\text{progress signal}
+
\text{exploration}
+
\text{credit}
+
\text{horizon}
+
\text{budget}
+
\text{declared evidence semantics}.
\]

The point is not to worship learning progress.

The point is to turn it into a governed search signal whose limits are visible.

## References used in this chapter

- [@OudeyerKaplanHafner2007IntrinsicMotivation]
- [@BaranesOudeyer2013GoalExploration]
- [@PortelasEtAl2020TeacherAlgorithms]

Exact source authority, prerequisite identities, and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-PROGRESSSEARCH-001.yaml