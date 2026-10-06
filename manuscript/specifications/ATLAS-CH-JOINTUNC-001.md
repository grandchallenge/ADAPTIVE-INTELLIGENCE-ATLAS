# Chapter Specification — ATLAS-CH-JOINTUNC-001

## Identity

**Title:** Joint Uncertainty Propagation  
**Part:** Decision-Making Under Uncertainty  
**Status target:** draft-v0.1  
**Implementation issue:** #243  
**Protected baseline:** c6b690725a0c89dd1746015d3e688c50553e0f28

## Hard prerequisites

### ATLAS-CH-RLBASE-001 / AUDIT-017

The chapter may inherit:

- controlled stochastic state/action/transition/reward/policy/value objects;
- Bellman expectation language;
- model-based versus model-free distinctions;
- partial observability / belief-state semantics;
- the explicit statement that transition, reward, observation, and future-value uncertainties interact and are not solved by RLBASE.

### ATLAS-CH-INFO-001 / AUDIT-004

The chapter may inherit:

- declared probability-model discipline;
- joint and conditional probability;
- expectation;
- statistical dependence;
- the distinction between information/dependence and causality;
- concentration/sufficiency boundaries.

Exact prerequisite identities and claim boundaries are frozen in:

sources/source-locks/ATLAS-CH-JOINTUNC-001.yaml

## Chapter contract

Treat transition, reward, observation, and future-value uncertainty jointly rather than by adding separate error bars as if independence had already been proved.

The chapter must distinguish:

1. uncertainty coordinates;
2. marginal variances;
3. covariance/dependence structure;
4. propagated uncertainty of a declared decision functional;
5. exact affine propagation;
6. local first-order propagation for nonlinear functions;
7. statistical dependence;
8. causal attribution.

The chapter must not collapse all eight into one generic scalar.

## Local uncertainty vector

Define a declared local coordinate vector:

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

Interpret the coordinates as:

- \(\varepsilon_R\): reward-model / reward-realization error;
- \(\varepsilon_T\): transition-model / transition-effect error;
- \(\varepsilon_O\): observation / belief-state error;
- \(\varepsilon_V\): future-value error before discounting.

These are local scalarized coordinates chosen for a declared decision functional.

They are not universal latent variables.

## Covariance matrix

Let:

\[
\Sigma
=
\operatorname{Cov}(\varepsilon).
\]

Then:

\[
\Sigma_{ii}
=
\operatorname{Var}(\varepsilon_i),
\]

and for \(i\neq j\),

\[
\Sigma_{ij}
=
\operatorname{Cov}(\varepsilon_i,\varepsilon_j).
\]

The diagonal does not determine the full propagated uncertainty unless the cross-covariances are known to vanish for the declared functional.

## Exact affine decision-error model

Use the exact local affine functional:

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

Its sensitivity vector is:

\[
a=
\begin{pmatrix}
1\\1\\1\\1/2
\end{pmatrix}.
\]

The factor \(1/2\) is a toy discount-like weight for the future-value coordinate.

The first three coefficients equal one because the witness uses normalized local coordinates.

This is a finite local witness, not a universal Bellman uncertainty formula.

## Exact joint propagation identity

For centered or non-centered \(\varepsilon\),

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
2\sum_{i<j}a_i a_j
\operatorname{Cov}(\varepsilon_i,\varepsilon_j).
\]

This identity is exact.

The diagonal-only approximation is:

\[
V_{\rm diag}
=
\sum_i a_i^2\operatorname{Var}(\varepsilon_i).
\]

It is exact only when the weighted covariance correction vanishes.

## Marginal-variance contract

For all three exact witness cases use:

\[
\operatorname{Var}(\varepsilon_R)
=
\operatorname{Var}(\varepsilon_T)
=
\operatorname{Var}(\varepsilon_O)
=
\operatorname{Var}(\varepsilon_V)
=
1.
\]

Therefore:

\[
\boxed{
V_{\rm diag}
=
1+1+1+\frac14
=
\frac{13}{4}.
}
\]

All three cases share the same marginal variances.

Only their dependence structure changes.

## Positive common-shock witness

Let \(U,W\) be independent centered Rademacher variables:

\[
P(U=1)=P(U=-1)=\frac12,
\]

and likewise for \(W\).

Set:

\[
\varepsilon_R=U,
\qquad
\varepsilon_T=U,
\qquad
\varepsilon_O=U,
\qquad
\varepsilon_V=W.
\]

Then:

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

The propagated error is:

\[
\delta_+
=
3U+\frac12W.
\]

Hence:

\[
\operatorname{Var}(\delta_+)
=
9+\frac14
=
\boxed{\frac{37}{4}}.
\]

The diagonal-only value remains:

\[
\frac{13}{4}.
\]

Thus:

\[
\boxed{
\frac{37}{4}
>
\frac{13}{4}.
}
\]

Ignoring positive dependence understates the propagated variance by:

\[
6.
\]

## Cancellation witness

Let \(U,W\) again be independent centered Rademacher variables.

Set:

\[
\varepsilon_R=U,
\qquad
\varepsilon_T=U,
\qquad
\varepsilon_O=-U,
\qquad
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

The propagated error is:

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

Again the diagonal-only value is:

\[
\frac{13}{4}.
\]

Thus:

\[
\boxed{
\frac54
<
\frac{13}{4}.
}
\]

Ignoring covariance can also overstate propagated uncertainty.

## Independence control

Let:

\[
U_R,U_T,U_O,U_V
\]

be mutually independent centered Rademacher variables.

Set:

\[
\varepsilon_i=U_i.
\]

Then:

\[
\Sigma_0=I_4.
\]

The propagated variance is:

\[
\operatorname{Var}
\left(
U_R+U_T+U_O+\frac12U_V
\right)
=
1+1+1+\frac14
=
\boxed{\frac{13}{4}}.
\]

Thus the diagonal sum is exact in the independence control.

## Independence versus zero covariance

The exact algebraic condition for the cross terms to vanish is:

\[
\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0
\]

for the relevant weighted pairs.

Full independence is sufficient but not necessary.

The manuscript must not state:

\[
\text{uncorrelated}
\iff
\text{independent}.
\]

## Why the witness is load-bearing

The three cases have identical marginal variances:

\[
(1,1,1,1).
\]

Yet their propagated variances are:

\[
\frac{37}{4},
\qquad
\frac54,
\qquad
\frac{13}{4}.
\]

Therefore marginal uncertainty alone does not determine propagated uncertainty.

The dependence structure matters.

## Decision-specific propagation

The chapter must not imply that one covariance matrix answers every decision question.

A different scalar decision functional has a different sensitivity vector.

For affine functional:

\[
\delta=a^\top\varepsilon,
\]

the propagated variance is:

\[
a^\top\Sigma a.
\]

Changing \(a\) changes which covariance terms matter.

Therefore:

\[
\boxed{
\text{uncertainty propagation is functional-relative}.
}
\]

## Nonlinear local propagation

Let a differentiable scalar decision functional be:

\[
F(x).
\]

For perturbation \(\varepsilon\),

\[
F(x+\varepsilon)
=
F(x)
+
\nabla F(x)^\top\varepsilon
+
R(x,\varepsilon).
\]

If the remainder is controlled on the perturbation regime of interest, first-order propagation gives:

\[
\boxed{
\operatorname{Var}
\left(
F(x+\varepsilon)-F(x)
\right)
\approx
\nabla F(x)^\top
\Sigma
\nabla F(x).
}
\]

This is a local approximation.

It is not an exact identity for arbitrary nonlinear \(F\).

## Remainder boundary

The chapter must state that first-order propagation can fail when:

- perturbations are large;
- curvature is large;
- discontinuities or threshold effects matter;
- the distribution has heavy tails not controlled by the approximation;
- the relevant sequential system changes regime;
- the local covariance itself changes materially across the perturbation region.

No global sequential-decision guarantee follows from a local gradient/covariance calculation alone.

## Sequential uncertainty boundary

A one-step local propagated variance is not automatically the uncertainty of a multi-step return.

Across time, uncertainty can be coupled through:

- state transitions;
- policy actions;
- observation updates;
- reward structure;
- value approximation;
- model adaptation.

A multi-step treatment requires the declared joint law or additional propagation assumptions.

The chapter may introduce the recursive problem but must not pretend the single-step witness solves it globally.

## Observation uncertainty

Observation uncertainty must not be silently merged into transition uncertainty.

In a partially observed system:

- environment state can be uncertain;
- observation generation can be uncertain;
- belief state can be uncertain;
- policy decisions can depend on that belief.

JOINTUNC keeps the observation coordinate explicit.

## Reward uncertainty

Reward uncertainty can arise from:

- stochastic reward realization;
- learned reward model;
- measurement noise;
- misspecified reward function.

These are not identical.

The chapter uses one local scalar \(\varepsilon_R\) only for the finite propagation witness.

## Transition uncertainty

Transition uncertainty can mean:

- aleatoric next-state randomness;
- epistemic transition-model uncertainty;
- local model approximation error;
- uncertainty in a scalar transition-sensitive summary.

The witness uses a declared local transition-effect coordinate.

It does not erase these distinctions globally.

## Future-value uncertainty

Future-value uncertainty can arise from:

- uncertain next state;
- uncertain value function;
- finite-data estimation;
- function approximation;
- model misspecification.

The coordinate \(\varepsilon_V\) represents a declared future-value error after the local problem has been scalarized.

## Dependence is not cause

If:

\[
\operatorname{Cov}(\varepsilon_R,\varepsilon_T)\neq0,
\]

the chapter may conclude statistical dependence in the declared joint model.

It may not conclude:

\[
\varepsilon_R
\to
\varepsilon_T
\]

causally.

The causal firewall from INFO remains active.

## Expected value versus uncertainty

Two actions can have the same expected return and different propagated uncertainty.

Conversely, two actions can have equal propagated variance and different expected return.

Therefore:

\[
\boxed{
\text{expected value}
\neq
\text{uncertainty}.
}
\]

A decision rule that trades them off must state that rule explicitly.

## Variance is not the full distribution

Equal variance does not imply equal:

- tail risk;
- skewness;
- multimodality;
- support;
- failure probability.

Variance is a second-moment summary.

The chapter must not present it as a complete uncertainty representation.

## Required exact replay

The computational witness must verify with exact rational arithmetic:

\[
V_{\rm diag}=\frac{13}{4},
\]

\[
V_+=\frac{37}{4},
\]

\[
V_-=\frac54,
\]

\[
V_0=\frac{13}{4}.
\]

It must verify:

\[
V_+-V_{\rm diag}=6,
\]

and:

\[
V_--V_{\rm diag}=-2.
\]

It must also verify all three covariance matrices are positive semidefinite.

## Required non-implications

The manuscript must explicitly reject:

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

## Reader outcomes

A reader should be able to:

1. explain why marginal error bars are insufficient under dependence;
2. derive \(\operatorname{Var}(a^\top\varepsilon)=a^\top\Sigma a\);
3. expand the covariance correction;
4. reproduce the \(37/4\), \(5/4\), and \(13/4\) witnesses exactly;
5. distinguish independence from zero covariance;
6. state why observation uncertainty should remain separate from transition uncertainty;
7. distinguish expected value from uncertainty;
8. state the local nonlinear propagation rule and its remainder boundary;
9. explain why covariance does not establish cause;
10. explain why variance is not the full decision-risk distribution.

## Required artifacts

- source lock;
- specification;
- derivation packet;
- exact computational witness;
- reader manuscript;
- Chapter Ledger promotion;
- Source Register entry;
- transaction receipt;
- mandatory post-draft audit.

## Downstream handoff

Later decision, robustness, and systems chapters may inherit:

- covariance-sensitive joint propagation;
- the distinction between marginal and joint uncertainty;
- functional-relative sensitivity vectors;
- the exact affine identity;
- local nonlinear propagation boundaries;
- dependence/causality separation.

They may not inherit a claim that second moments completely characterize risk or that local propagation solves multi-step uncertainty globally.

## References used in this chapter

No new external academic authority is added.

External definitions and decision/control substrate are inherited through audited RLBASE-001 and INFO-001.

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-JOINTUNC-001.yaml
