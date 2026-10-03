# Regret
<!-- ATLAS-CH-REGRET-001 -->

**Epistemic status:** established bandit-regret theory + audited exploration prerequisite + Atlas synthesis + exact finite witnesses.  
**Specification:** manuscript/specifications/ATLAS-CH-REGRET-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-REGRET-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-REGRET-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-REGRET-001.yaml

Regret measures the price of not acting like a comparator.

That sentence is useful only if the comparator is named.

A regret number does not belong to an algorithm by itself.

It belongs to a complete evaluation contract:

- environment;
- horizon;
- policy;
- reward or loss convention;
- comparator;
- expectation or prior convention.

Change the comparator and the regret can change while the learner does exactly the same thing.

Change the prior and a Bayes-optimal policy can stop being desirable.

Change cumulative interaction cost into final recommendation quality and the preferred algorithm can change again.

The governing rule of this chapter is:

> regret is a relational quantity, not an intrinsic property of a trajectory.

That rule is the difference between using regret theory and merely quoting a rate.

## 1. From exploration to opportunity cost

The Exploration chapter established the central learning-while-acting tension.

An exploratory action may sacrifice immediate reward to gain information that improves later decisions.

Regret asks a complementary question:

> how much reward was lost relative to a declared comparator over the interaction?

This makes regret especially natural for bandits.

If the learner samples an arm that is not truly best, it pays an opportunity cost.

If that sample reveals useful information, the cost may be worthwhile.

Regret does not say whether the information was worthwhile by itself.

It records the reward shortfall relative to the benchmark.

## 2. The stochastic-bandit object

Let environment `theta` define arm means

`mu_theta(a)`

for actions

`a in A`.

Let

`mu_theta^*=max_a mu_theta(a)`.

Define the gap

`Delta_theta(a)=mu_theta^*-mu_theta(a)`.

Let `Pi` be the declared admissible policy class. A policy `pi in Pi` chooses actions

`A_1,...,A_T`

and observes rewards

`Y_1,...,Y_T`.

Under the stationary stochastic-bandit convention,

`E[Y_t | H_{t-1},A_t]
=
mu_theta(A_t)`.

This small structure is enough to expose several regret notions that are often collapsed.

## 3. Pathwise reward shortfall is random

Define the pathwise mean-benchmark regret

`R_T^path(theta)
=
T mu_theta^*
-
sum_t Y_t`.

The comparator term uses the expected reward of the best fixed arm.

The learner term uses realized rewards.

So `R_T^path` is random.

It can even be negative.

A learner pulling a suboptimal arm can get lucky enough that its realized reward exceeds

`T mu_theta^*`.

That does not make the chosen arm optimal.

It means reward noise beat the mean benchmark on that path.

## 4. Expected or pseudo-regret

A standard stochastic-bandit quantity is

`bar R_T(pi,theta)
=
E_theta^pi[
sum_t Delta_theta(A_t)
]`.

This quantity depends on which arms the learner chooses, not on favorable or unfavorable reward noise after conditioning on those choices.

Bubeck and Cesa-Bianchi develop stochastic and adversarial bandit regret in this comparator-relative framework [@BubeckCesaBianchi2012].

Lattimore and Szepesvári give a comprehensive modern treatment across stochastic, adversarial, Bayesian, minimax, and pure-exploration settings [@LattimoreSzepesvari2020].

Terminology varies across subliteratures.

The Atlas therefore writes the formula before attaching the name.

## 5. Why expected pathwise regret equals pseudo-regret here

Under the declared stochastic-bandit model,

`E[Y_t]
=
E[mu_theta(A_t)]`.

Therefore

`E[R_T^path(theta)]
=
T mu_theta^*
-
sum_t E[Y_t]`

`=
E[
sum_t
(mu_theta^*-mu_theta(A_t))
]`

`=
bar R_T(pi,theta)`.

The equality is useful.

The objects remain different.

One is a random pathwise shortfall.

The other is its expected gap accumulation under the declared model.

## 6. Pull counts expose the cost of exploration

Let

`N_a(T)`

be the number of times arm `a` is selected by time `T`.

Then

`bar R_T(pi,theta)
=
sum_a
Delta_theta(a)
E[N_a(T)]`.

This formula turns regret into an accounting identity.

Each suboptimal arm contributes:

`gap x expected number of pulls`.

A learning policy must sample uncertain arms enough to discover which are suboptimal.

Regret theory asks how efficiently that information cost can be paid.

## 7. Exact witness: same policy, different pathwise regret

Take two Bernoulli arms:

`mu(A)=1/4`,
`mu(B)=3/4`.

Suppose the learner always pulls A for two rounds.

The pseudo-regret is exactly

`2(3/4-1/4)=1`.

But the pathwise mean-benchmark regret is

`3/2-(Y_1+Y_2)`.

If both rewards are zero, regret is

`3/2`.

If exactly one is one, regret is

`1/2`.

If both rewards are one, regret is

`-1/2`.

The same policy in the same environment can therefore produce different pathwise regret values.

The exact expectation is still

`1`.

## 8. Negative pathwise regret is not paradoxical

The best arm is best in expectation.

It is not guaranteed to dominate every realized sample path.

This is the same reason a fair or unfavorable gamble can win on one trial.

So a negative pathwise value does not refute the comparator.

It exposes the difference between:

- stochastic performance on one path;
- expected performance under the environment.

A report should say which one it is using.

## 9. Bayesian regret adds a prior

Let `nu` be a prior over environments.

Define Bayesian regret:

`BR_T(pi,nu)
=
E_{theta~nu}[
bar R_T(pi,theta)
]`.

Now the evaluation weights environments by prior probability.

A policy can be excellent under the prior while weak on rare environments.

That may be rational if the prior is part of the intended decision problem.

It is not a worst-case statement.

The prior belongs in the claim.

## 10. Worst-case regret removes prior weighting

For environment class `Theta`, define

`W_T(pi,Theta)
=
sup_{theta in Theta}
bar R_T(pi,theta)`.

This asks:

> how bad can the policy be over the declared class?

Rare environments do not receive less weight.

They receive the same worst-case attention as common ones.

The environment class is therefore just as important as the prior was in the Bayesian case.

A worst-case guarantee without the class is incomplete.

## 11. Minimax regret chooses the best worst-case policy

Define

`R_T^*(Theta,Pi)
=
inf_{pi in Pi}
sup_{theta in Theta}
bar R_T(pi,theta)`.

The policy is chosen to minimize its worst environment-specific expected regret.

This is a different optimization problem from minimizing

`BR_T(pi,nu)`.

The distinction is not philosophical.

It changes optimal policies in the smallest possible examples.

## 12. Exact Bayes/minimax witness

Consider one decision and two possible environments.

Under environment `+`:

- A pays 1;
- B pays 0.

Under environment `-`:

- A pays 0;
- B pays 1.

Let the policy choose A with probability `q`.

Then

`R(q,+)=1-q`

and

`R(q,-)=q`.

Worst-case regret is

`max(1-q,q)`.

The minimax choice is

`q=1/2`

with regret

`1/2`.

Now put prior mass

`9/10`

on `+`.

Bayesian regret is

`9/10(1-q)+1/10 q`.

It is minimized at

`q=1`.

The Bayes-optimal regret is

`1/10`.

But that policy has worst-case regret

`1`.

The criterion changed.

So did the optimal policy.

## 13. Bayes performance is bounded by worst-case performance

For a fixed policy and a prior supported on `Theta`,

`BR_T(pi,nu)
<=
W_T(pi,Theta)`.

An average over a set cannot exceed the set's supremum.

Taking the best policy over the same declared class `Pi` on each side gives

`inf_{pi in Pi} BR_T(pi,nu)
<=
R_T^*(Theta,Pi)`.

This inequality does not say that the optimizing policies coincide.

The exact witness shows that they need not.

## 14. Minimax is not prior-free truth

A minimax policy protects against the worst environment in its declared class.

That does not make the class itself uniquely correct.

A class can be:

- too broad;
- too narrow;
- misspecified;
- computationally convenient rather than realistic.

Minimax analysis removes a prior.

It does not remove modeling assumptions.

## 15. Comparator class is part of regret

Regret can be defined against many comparators.

Examples include:

- best fixed action;
- best stationary policy;
- best policy in a hypothesis class;
- best action sequence with at most `S` switches;
- best dynamic action sequence;
- clairvoyant oracle subject to constraints.

A stronger comparator generally makes the benchmark harder to match.

Two regret numbers against different comparator classes are not the same quantity.

## 16. Exact comparator witness

Consider reward table:

| round | A | B |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 0 | 1 |

The learner chooses A twice and earns 1.

Against the best fixed arm:

- A earns 1;
- B earns 1.

Regret is

`0`.

Against an unrestricted per-round comparator:

- choose A on round 1;
- choose B on round 2.

Comparator reward is 2.

Regret is

`1`.

Same learner.

Same reward table.

Different comparator.

Different regret.

## 17. The comparator can be too strong to be useful

Suppose a learner must act causally, without future observations.

Now compare it with a clairvoyant sequence that sees all future rewards.

The resulting regret may measure a genuine gap.

But the comparator has access to information the learner never could.

That may be appropriate for one theorem and misleading for another engineering claim.

A regret analysis should state what information the comparator is allowed to use.

## 18. Cumulative regret measures interaction cost

Cumulative regret asks how much opportunity cost was paid throughout learning.

That is natural when rewards during learning matter.

If every exploratory action costs money, time, safety margin, or service quality, the cost accumulates.

Bandit regret theory often focuses on this online objective.

A learner should learn while performing well.

## 19. Simple regret measures final recommendation quality

Pure-exploration problems often care about a different object.

After `T` samples, the learner recommends an arm

`hat a_T`.

Define simple regret:

`SR_T
=
mu^*
-
mu(hat a_T)`.

This ignores how much reward was lost while gathering information.

It asks only:

> how good is the final recommendation?

Lattimore and Szepesvári treat pure exploration as a distinct objective family from cumulative-regret minimization [@LattimoreSzepesvari2020].

## 20. Exact cumulative/simple witness

Suppose rewards are deterministic:

- A gives 1;
- B gives 0.

A learner:

1. pulls B once;
2. pulls A once;
3. recommends A.

Cumulative regret is

`1`.

The B pull paid one unit of opportunity cost.

Final simple regret is

`0`.

The recommendation is perfect.

So cumulative regret and final recommendation error are different objectives even in a trivial problem.

## 21. Exploration can raise cumulative regret and lower simple regret

This is not a contradiction.

Sampling a doubtful arm can be costly during interaction.

The information can improve the final choice.

That is exactly why pure exploration and online reward maximization require different algorithms and analyses.

The objective must be fixed before the experiment.

Otherwise a method can be declared good after the fact by selecting whichever regret notion flatters it.

## 22. Sublinear regret is an average guarantee

A common goal is

`bar R_T=o(T)`.

This means

`bar R_T/T -> 0`.

Average regret per round vanishes.

Cumulative regret need not vanish.

It need not even stay bounded.

For example,

`bar R_T=log T`

diverges as `T` grows while

`log T/T -> 0`.

So "sublinear regret" does not mean "no regret."

It means the cumulative cost grows more slowly than the horizon.

## 23. A good asymptotic rate can hide finite-horizon cost

Asymptotics answer what happens as the horizon becomes large.

Real systems operate at finite horizons.

An algorithm with excellent limiting behavior may have poor constants or long transients.

Another may be better for the actual deployment horizon and worse asymptotically.

A regret statement should therefore say whether it is:

- finite time;
- asymptotic order;
- asymptotic constant;
- lower bound;
- upper bound.

These are different claim classes.

## 24. Lai–Robbins: exploration has an asymptotic information price

Lai and Robbins established classical asymptotic efficiency results for adaptive allocation under regular parametric stochastic-bandit assumptions [@LaiRobbins1985].

The broad lesson is important:

a uniformly good learner cannot simply stop sampling every suboptimal arm immediately.

It must collect enough evidence to distinguish the true environment from alternatives in which that arm would be optimal.

That information requirement produces logarithmic-scale sampling costs in the classical setting.

The exact constants and regularity assumptions belong to that model class.

They are not universal bandit laws.

## 25. Finite-time analysis answers another question

Auer, Cesa-Bianchi, and Fischer gave finite-time stochastic-bandit analysis for upper-confidence methods [@AuerEtAl2002Bandit].

The important Atlas distinction is between:

- asymptotic efficiency;
- explicit finite-`T` control.

A theorem can be strong in one sense and weak in the other.

Do not silently replace one with the other.

## 26. Regret does not explain the policy mechanism

Two policies can have the same regret for different reasons.

One may explore deliberately.

Another may make estimation mistakes.

A third may be constrained from selecting the best action.

A fourth may be randomized for robustness or fairness.

Regret measures comparative reward performance.

It is not a mechanistic explanation of why actions occurred.

The Exploration chapter supplies those mechanism distinctions.

## 27. Regret and information are different units

Russo and Van Roy's information-directed sampling explicitly couples expected single-period regret with information acquisition [@RussoVanRoy2014].

That is useful precisely because the quantities differ.

Regret is measured in reward or loss units.

Information gain is measured in information units.

An information-ratio construction relates them.

It does not identify them.

## 28. Low regret does not imply safety

Imagine a thousand-round policy with excellent cumulative reward that takes one action capable of catastrophic failure.

If the reward objective does not encode the catastrophe at the right scale, low regret can coexist with unacceptable safety.

A safety guarantee requires:

- a constrained set;
- chance constraint;
- risk measure;
- reachability condition;
- conservative baseline;
- or another explicit safety object.

Regret alone does not create it.

## 29. Low regret does not imply calibration

A decision-maker can choose high-reward actions while maintaining badly calibrated probabilities.

If only the selected actions matter to reward, prediction quality away from those decisions may not affect regret.

Calibration therefore requires its own evaluation.

The same is true for uncertainty quality and causal identification.

## 30. Low regret does not imply fairness

A reward comparator may average across users or groups.

Low aggregate regret can coexist with severe distributional disparities.

Unless the reward or constraints encode the relevant fairness property, regret does not measure it.

This is not an objection to regret theory.

It is a reminder that objectives define what is optimized.

## 31. Low regret does not imply robustness

A policy can have low regret on the declared environment class and fail badly outside it.

Worst-case regret is only worst case over

`Theta`.

If distribution shift moves the world outside `Theta`, the theorem no longer applies automatically.

Robustness requires an uncertainty set, perturbation model, or other shift semantics.

## 32. Low regret does not imply recoverability

A policy can obtain nearly comparator-level reward while entering a state from which future correction is difficult.

If the comparator does not price that loss of future action freedom, regret will not record it.

This is the boundary needed by the next chapter.

Optionality is not a synonym for low regret.

## 33. Expected regret can ignore tail structure

A policy with rare enormous losses can have acceptable expected regret if those events are sufficiently rare or insufficiently penalized.

Applications sensitive to tails may need high-probability or risk-sensitive guarantees.

Expected regret should not be promoted into a tail-risk guarantee.

## 34. Bayesian regret can hide rare-environment failure

The exact Bayes/minimax witness already demonstrates this.

The prior assigns probability `1/10` to the environment where action A is wrong.

Bayes optimization chooses A deterministically.

That is optimal for the declared prior.

Its worst-case regret is still maximal.

Bayesian performance and robustness answer different questions.

## 35. Minimax regret can be conservative under a strong prior

The reverse tradeoff also exists.

If the prior is reliable and highly concentrated, a minimax policy may spend performance protecting against environments believed to be very unlikely.

Whether that is desirable depends on the application.

The mathematics cannot choose the governance stance.

It can expose the consequence of the stance.

## 36. A practical regret ledger

Before reading or reporting a regret result, record:

| Field | Question |
|---|---|
| horizon | Over how many decisions? |
| environment | Which fixed environment or environment class? |
| policy | Which policy class may the learner use? |
| reward/loss | What is accumulated? |
| comparator | Best fixed action, stationary policy, switching policy, oracle, or something else? |
| randomness | Pathwise, expected over rewards, or expected over policy randomization? |
| prior | Is there a Bayesian prior, and what is it? |
| criterion | Bayesian, worst-case, minimax, high-probability, or another notion? |
| terminal objective | Is simple/final recommendation regret also relevant? |
| constraints | What important properties are outside the regret objective? |

This ledger prevents rate notation from outrunning semantics.

## 37. What the exact witnesses establish

The companion witness establishes four finite facts.

First, in a two-round Bernoulli problem:

- pseudo-regret is `1`;
- pathwise regret can be `3/2`, `1/2`, or `-1/2`;
- expected pathwise regret is exactly `1`.

Second, in a one-step two-environment problem:

- minimax policy chooses A with probability `1/2`;
- minimax regret is `1/2`;
- under prior `9/10,1/10`, Bayes-optimal policy chooses A with probability `1`;
- Bayes regret is `1/10`;
- its worst-case regret is `1`.

Third, one realized trajectory has regret `0` against the best fixed action and `1` against a dynamic per-round comparator.

Fourth, an exploration sequence has cumulative regret `1` and simple regret `0`.

No asymptotic theorem is inferred from these finite calculations.

## 38. Downstream handoff

**Optionality and Correction Capacity — ATLAS-CH-OPTIONALITY-001** may now assume:

- environment-specific expected/pseudo-regret;
- pathwise versus expected-regret distinction;
- Bayesian regret;
- worst-case and minimax regret;
- comparator-class dependence;
- cumulative versus simple regret;
- sublinear-regret semantics;
- the negative result that low reward regret does not automatically preserve recoverability or future action freedom.

The downstream chapter must independently define optionality, viable future actions, correction capacity, recoverability, and uncertainty over future opportunities.

It may use regret as one evaluation coordinate.

It may not redefine regret to contain those properties by fiat.

## References used in this chapter

- Lai and Robbins, *Asymptotically Efficient Adaptive Allocation Rules* [@LaiRobbins1985].
- Bubeck and Cesa-Bianchi, *Regret Analysis of Stochastic and Nonstochastic Multi-Armed Bandit Problems* [@BubeckCesaBianchi2012].
- Lattimore and Szepesvári, *Bandit Algorithms* [@LattimoreSzepesvari2020].
- Auer, Cesa-Bianchi, and Fischer, *Finite-time Analysis of the Multiarmed Bandit Problem* [@AuerEtAl2002Bandit].
- Russo and Van Roy, *Learning to Optimize via Information-Directed Sampling* [@RussoVanRoy2014].

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-REGRET-001.yaml
