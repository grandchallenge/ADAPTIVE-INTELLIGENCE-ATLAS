# Joint Uncertainty Propagation
<!-- ATLAS-CH-JOINTUNC-001 -->

**Epistemic status:** audited RL/control and information-theory substrate + Atlas-owned exact covariance propagation and finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-JOINTUNC-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-JOINTUNC-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-JOINTUNC-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-JOINTUNC-001.yaml

A sequential decision can be uncertain in several places at once.

The reward can be uncertain.

The transition can be uncertain.

The observation can be uncertain.

The continuation value can be uncertain.

If those uncertainties move together, adding four separate error bars as if they were independent can be wrong in either direction.

The governing principle is:

\[
\boxed{
\text{joint uncertainty requires the joint law, not only the marginals.}
}
\]

This chapter formalizes that principle in the smallest exact setting that exposes the issue.

## 1. The controlled-system handoff

Reinforcement Learning and Control separated:

- state;
- action;
- transition kernel;
- reward;
- policy;
- return;
- value;
- learned model;
- observation structure.

It also stated a boundary:

transition, reward, observation, and future-value uncertainty can interact.

RLBASE did not solve that interaction.

JOINTUNC starts there.

## 2. Information-theoretic discipline

Probability, Information, and Statistical Structure supplied another discipline:

uncertainty quantities are defined only relative to a declared probability model.

Dependence is also model-relative.

A covariance or mutual information does not become causal direction merely because it is nonzero.

JOINTUNC inherits that firewall.

## 3. Four local coordinates

Write a declared local error vector:

\[
\varepsilon
=
\begin{pmatrix}
\varepsilon_R\\
\varepsilon_T\\
\varepsilon_O\\
\varepsilon_V
\end{pmatrix}.
\]

Interpret the coordinates as local scalarized uncertainty in:

- reward;
- transition effect;
- observation or belief state;
- future value.

These are not universal latent variables.

They are coordinates chosen for a declared local decision calculation.

## 4. Marginals are not enough

Suppose we know:

\[
\operatorname{Var}(\varepsilon_R),
\quad
\operatorname{Var}(\varepsilon_T),
\quad
\operatorname{Var}(\varepsilon_O),
\quad
\operatorname{Var}(\varepsilon_V).
\]

That is not yet a full joint uncertainty description.

We also need the cross-covariances collected in:

\[
\Sigma
=
\operatorname{Cov}(\varepsilon).
\]

The diagonal records marginal variances.

The off-diagonal entries record pairwise covariance.

## 5. A declared local decision-error functional

Use the exact affine witness:

\[
\boxed{
\delta
=
\varepsilon_R
+
\varepsilon_T
+
\varepsilon_O
+
\frac12\varepsilon_V.
}
\]

The sensitivity vector is:

\[
a=
\begin{pmatrix}
1\\1\\1\\1/2
\end{pmatrix}.
\]

The factor \(1/2\) plays a discount-like role for the future-value coordinate.

The first three coefficients are normalized to one.

This is a toy local functional, not a universal Bellman uncertainty equation.

## 6. Exact affine propagation

For any finite-second-moment error vector:

\[
\boxed{
\operatorname{Var}(a^\top\varepsilon)
=
a^\top\Sigma a.
}
\]

Expanded:

\[
\operatorname{Var}(a^\top\varepsilon)
=
\sum_i a_i^2\operatorname{Var}(\varepsilon_i)
+
2\sum_{i<j}
a_i a_j
\operatorname{Cov}(\varepsilon_i,\varepsilon_j).
\]

The covariance terms are not optional decoration.

They are part of the exact variance.

## 7. The naive diagonal calculation

Give every coordinate unit marginal variance:

\[
\operatorname{Var}(\varepsilon_i)=1.
\]

Then the diagonal-only sum is:

\[
1+1+1+\frac14
=
\boxed{\frac{13}{4}}.
\]

If the weighted covariance terms vanish, this is exact.

If they do not, it is not.

## 8. Positive common-shock dependence

Let \(U,W\) be independent centered Rademacher variables.

Set:

\[
\varepsilon_R=U,
\]

\[
\varepsilon_T=U,
\]

\[
\varepsilon_O=U,
\]

\[
\varepsilon_V=W.
\]

The first three uncertainties share one common shock.

Their covariance matrix is:

\[
\Sigma_+
=
\begin{pmatrix}
1&1&1&0\\
1&1&1&0\\
1&1&1&0\\
0&0&0&1
\end{pmatrix}.
\]

## 9. Positive dependence amplifies uncertainty

Now:

\[
\delta_+
=
3U+\frac12W.
\]

Since \(U\) and \(W\) are independent:

\[
\operatorname{Var}(\delta_+)
=
9+\frac14
=
\boxed{\frac{37}{4}}.
\]

The diagonal-only value was:

\[
\frac{13}{4}.
\]

Difference:

\[
\boxed{6}.
\]

Ignoring positive covariance has substantially understated the propagated variance.

## 10. Cancellation dependence

Now keep the same marginal variances but reverse the observation coordinate:

\[
\varepsilon_R=U,
\]

\[
\varepsilon_T=U,
\]

\[
\varepsilon_O=-U,
\]

\[
\varepsilon_V=W.
\]

Then:

\[
\Sigma_-
=
\begin{pmatrix}
1&1&-1&0\\
1&1&-1&0\\
-1&-1&1&0\\
0&0&0&1
\end{pmatrix}.
\]

## 11. Dependence can also cancel

The propagated error is now:

\[
\delta_-
=
U+\frac12W.
\]

Therefore:

\[
\operatorname{Var}(\delta_-)
=
1+\frac14
=
\boxed{\frac54}.
\]

The diagonal-only value was still:

\[
\frac{13}{4}.
\]

Difference:

\[
\boxed{-2}.
\]

Ignoring covariance has now overstated the propagated variance.

## 12. Independence control

Let:

\[
U_R,U_T,U_O,U_V
\]

be mutually independent centered Rademacher variables.

Set each uncertainty coordinate equal to its own independent variable.

Then:

\[
\Sigma_0=I_4.
\]

Therefore:

\[
\operatorname{Var}(\delta_0)
=
1+1+1+\frac14
=
\boxed{\frac{13}{4}}.
\]

The diagonal calculation is exact.

## 13. One set of marginals, three different results

All three cases have the same marginal variance vector:

\[
(1,1,1,1).
\]

Their propagated variances are:

\[
\boxed{
\frac{37}{4},
\qquad
\frac54,
\qquad
\frac{13}{4}.
}
\]

Therefore:

\[
\boxed{
\text{same marginal variances}
\not\Rightarrow
\text{same propagated uncertainty}.
}
\]

## 14. The difference is dependence structure

The three experiments did not change the marginal error sizes.

They changed only how the error coordinates move together.

That is the central point.

If the uncertainty object is joint, its propagation should be joint.

## 15. Independence is stronger than required

The covariance correction vanishes when the relevant weighted cross-covariances vanish.

Full independence guarantees that.

But full independence is not necessary.

Thus:

\[
\boxed{
\text{uncorrelated}
\not\Rightarrow
\text{independent}.
}
\]

The variance calculation needs second moments.

A claim of independence needs more.

## 16. Propagation depends on the decision functional

Suppose we keep the same covariance matrix but change the decision quantity.

Use sensitivity vector \(b\) instead of \(a\).

Then:

\[
\operatorname{Var}(b^\top\varepsilon)
=
b^\top\Sigma b.
\]

Different decision functionals can therefore assign different importance to the same covariance structure.

There is no universal propagated-uncertainty scalar independent of the quantity being propagated.

## 17. Reward uncertainty remains a distinct object

Reward uncertainty can mean several things:

- random reward realization;
- measurement noise;
- learned reward-model error;
- reward misspecification.

Those are not identical.

The finite witness deliberately compresses them into one local scalar only after the modeling choice is declared.

## 18. Transition uncertainty remains distinct too

Transition uncertainty can include:

- inherent next-state randomness;
- learned transition-model uncertainty;
- local approximation error;
- uncertainty in a transition-sensitive summary.

The chapter does not silently equate those notions.

## 19. Observation uncertainty is not transition uncertainty

In a partially observed system, latent-state dynamics and observation generation are separate stochastic mechanisms.

An observation can be noisy even when the latent transition is known.

A transition can be uncertain even when observation is perfect.

They can also be dependent.

This is why the observation coordinate remains explicit.

## 20. Future-value uncertainty is downstream but not redundant

Future-value uncertainty can reflect:

- uncertain next state;
- value-function estimation error;
- function approximation;
- finite data;
- model error.

It is not automatically absorbed by the transition coordinate.

A declared calculation must say which uncertainty is represented where.

## 21. Expected value is not uncertainty

RLBASE established value as expected future return under declared conditions.

That expectation is not an uncertainty estimate.

Two actions can have equal expected value and different propagated uncertainty.

Two actions can also have equal propagated variance and different expected value.

Therefore:

\[
\boxed{
\text{expected value}
\neq
\text{uncertainty}.
}
\]

## 22. A risk rule must be declared

A decision system may intentionally combine expectation and uncertainty.

For example, it may penalize variance.

That is a new decision rule.

It should not be smuggled into the meaning of value.

The utility or risk criterion must be declared explicitly.

## 23. Variance is useful but incomplete

Variance is a second-moment summary.

Two distributions can share mean and variance while differing in:

- tail probability;
- skewness;
- support;
- multimodality;
- catastrophic-event probability.

Therefore:

\[
\boxed{
\text{same variance}
\not\Rightarrow
\text{same risk distribution}.
}
\]

## 24. Nonlinear decision maps

Real decision functionals are often nonlinear.

Let:

\[
F(x)
\]

be differentiable at a nominal state \(x\).

For perturbation \(\varepsilon\):

\[
F(x+\varepsilon)-F(x)
=
\nabla F(x)^\top\varepsilon
+
R.
\]

The remainder \(R\) matters.

## 25. The exact remainder identity

The variance is exactly:

\[
\operatorname{Var}
\left(
F(x+\varepsilon)-F(x)
\right)
=
\nabla F(x)^\top
\Sigma
\nabla F(x)
+
\operatorname{Var}(R)
+
2\operatorname{Cov}
\left(
\nabla F(x)^\top\varepsilon,
R
\right).
\]

Only the first term is the familiar linearized propagation term.

## 26. First-order propagation is local

If the remainder contributions are controlled, then:

\[
\operatorname{Var}
\left(
F(x+\varepsilon)-F(x)
\right)
\approx
\nabla F(x)^\top
\Sigma
\nabla F(x).
\]

This is a local approximation.

It is not a license to propagate one covariance matrix globally through an arbitrary nonlinear agent.

## 27. When the local approximation can fail

The first-order picture can fail when:

- perturbations are not small;
- curvature is large;
- thresholds or discontinuities matter;
- policies switch;
- state visitation changes;
- tail events dominate;
- the covariance itself changes across the perturbed region.

A global theorem needs additional arguments.

## 28. Sequential propagation is harder than one step

For:

\[
x_{t+1}=F_t(x_t,\eta_t),
\]

later uncertainty depends on:

- local sensitivities;
- cross-time dependence;
- state-dependent noise;
- policy feedback;
- changing distributions;
- changing approximators.

The exact affine witness is a building block.

It does not solve the full recursion.

## 29. Why naive independent summation is dangerous

The positive common-shock witness gave:

\[
\frac{37}{4}
\]

while naive summation gave:

\[
\frac{13}{4}.
\]

The cancellation witness gave:

\[
\frac54
\]

while naive summation again gave:

\[
\frac{13}{4}.
\]

So the naive rule is not merely slightly noisy.

It can fail in either direction.

## 30. Covariance is not causality

Suppose reward and transition errors have positive covariance.

That says they co-vary under the declared joint law.

It does not tell us whether:

- reward error causes transition error;
- transition error causes reward error;
- a third variable drives both;
- the dependence is induced by conditioning or selection.

Therefore:

\[
\boxed{
\text{statistical dependence}
\not\Rightarrow
\text{causal direction}.
}
\]

## 31. Conditional structure matters

The relevant covariance can change after conditioning on:

- current state;
- action;
- observation;
- belief state;
- model version;
- policy.

A joint uncertainty analysis should say what is conditioned on.

One unconditional covariance matrix may be inappropriate for every local decision context.

## 32. Functional-relative uncertainty is an interface concept

Suppose a downstream system asks:

> how uncertain is this action-value comparison?

The upstream uncertainty representation should expose enough joint structure to answer that question.

A list of independent scalar error bars may not be a sufficient interface.

This is a systems consequence of the mathematics.

## 33. What JOINTUNC does not claim

It does not claim that:

\[
\text{variance}
=
\text{complete risk}.
\]

It does not claim that:

\[
\text{covariance}
=
\text{cause}.
\]

It does not claim that:

\[
\text{local linearization}
=
\text{global sequential theorem}.
\]

It does not claim that the four witness coordinates are canonical.

It does not claim real RL errors have the toy joint laws.

## 34. Non-implications

The chapter rejects:

\[
\text{same marginal variances}
\not\Rightarrow
\text{same propagated uncertainty},
\]

\[
\text{zero covariance}
\not\Rightarrow
\text{independence},
\]

\[
\text{statistical dependence}
\not\Rightarrow
\text{causal direction},
\]

\[
\text{local first-order variance}
\not\Rightarrow
\text{global sequential uncertainty},
\]

\[
\text{same variance}
\not\Rightarrow
\text{same risk distribution},
\]

and:

\[
\text{high uncertainty}
\not\Rightarrow
\text{low expected value}.
\]

## 35. Practical protocol

For a real decision system:

1. define the decision functional;
2. identify distinct uncertainty sources;
3. define the conditioning context;
4. estimate or bound the joint covariance/dependence structure;
5. propagate through the declared sensitivity map;
6. test whether a local linear approximation is adequate;
7. expose remainder or nonlinear risk when it is not;
8. report expectation separately from uncertainty;
9. retain dependence/causality separation;
10. preserve the full distribution when second moments are insufficient.

## 36. Atlas connections

**Reinforcement Learning and Control.**  
JOINTUNC extends the controlled stochastic substrate without changing Bellman semantics.

**Probability and Information.**  
Joint distributions and statistical dependence are the mathematical foundation of the uncertainty object.

**Uncertainty and Calibration.**  
Marginal predictive uncertainty can feed JOINTUNC, but calibration of individual predictors does not by itself specify cross-source dependence.

**Distribution Shift.**  
A covariance structure learned in one regime may change under shift.

**Agents and Systems.**  
Joint uncertainty becomes an interface requirement when one subsystem passes uncertainty to another.

## 37. Closing view

Uncertainty does not propagate source by source unless the joint structure permits it.

The exact witness makes that unavoidable.

With the same four marginal variances:

\[
(1,1,1,1),
\]

we obtained:

\[
\frac{37}{4},
\qquad
\frac54,
\qquad
\frac{13}{4}.
\]

Nothing changed except dependence.

The correct conclusion is:

\[
\boxed{
\text{propagate the joint uncertainty of the declared decision object, not an assumed independent sum of marginal errors.}
}
\]

And when the decision map is nonlinear, keep the local approximation boundary visible.

## References used in this chapter

No new external academic authority is added.

The controlled-decision substrate is inherited through audited ATLAS-CH-RLBASE-001.

The probability/information substrate is inherited through audited ATLAS-CH-INFO-001.

Exact prerequisite identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-JOINTUNC-001.yaml
