# ATLAS-CH-UNCERTAINTY-001 — Derivation Packet

## Scope

This packet establishes the exact finite probability identities and counterexamples used by Uncertainty and Calibration.

It does not prove universal calibration, Bayesian correctness, conformal validity under shift, or selective-risk guarantees beyond the stated assumptions.

## D1. Binary calibration

Let Y in {0,1} and S in [0,1].

Population calibration means

\[
E[Y\mid S]=S
\]

almost surely.

For an atom s with positive probability, this reduces to

\[
P(Y=1\mid S=s)=s.
\]

The property is conditional on the score, not on every covariate value.

## D2. Calibration does not imply sharpness

Let X in {a,b} with equal probability and

\[
P(Y=1\mid a)=0.9,\qquad P(Y=1\mid b)=0.1.
\]

The marginal positive rate is

\[
P(Y=1)=\frac12(0.9)+\frac12(0.1)=0.5.
\]

Define the constant score

\[
S_0=0.5.
\]

Then

\[
P(Y=1\mid S_0=0.5)=0.5,
\]

so S0 is calibrated.

Define

\[
S_1(a)=0.9,\qquad S_1(b)=0.1.
\]

Then

\[
P(Y=1\mid S_1=0.9)=0.9
\]

and

\[
P(Y=1\mid S_1=0.1)=0.1.
\]

So S1 is also calibrated.

For Bernoulli Y with conditional probability p,

\[
E[(Y-p)^2\mid p]=p(1-p).
\]

Therefore

\[
E[(Y-S_1)^2]
=
\frac12(0.9)(0.1)+\frac12(0.1)(0.9)
=
0.09.
\]

For the constant score,

\[
E[(Y-0.5)^2]
=
Var(Y)
=
0.25.
\]

Thus calibration alone does not determine sharpness or Brier risk.

## D3. Entropy decomposition

For latent model variable Theta,

\[
I(Y;Theta)
=
H(Y)-H(Y\mid Theta).
\]

Averaging conditional entropy over Theta gives

\[
H(Y)
=
E[H(Y\mid Theta)]
+
I(Y;Theta).
\]

The interpretation of the terms depends on the declared probabilistic model.

## D4. Same predictive law, purely conditional/noise uncertainty

Let Theta be deterministic and

\[
Y\sim Bernoulli(1/2).
\]

Then

\[
H(Y)=1.
\]

Because conditioning on fixed Theta changes nothing,

\[
H(Y\mid Theta)=1.
\]

Therefore

\[
I(Y;Theta)=0.
\]

## D5. Same predictive law, purely latent/model uncertainty

Let

\[
Theta\sim Bernoulli(1/2)
\]

and set

\[
Y=Theta.
\]

Marginally,

\[
Y\sim Bernoulli(1/2),
\]

so

\[
H(Y)=1.
\]

But conditional on Theta, Y is deterministic:

\[
H(Y\mid Theta)=0.
\]

Hence

\[
I(Y;Theta)=1.
\]

The predictive distribution and predictive entropy are identical to D4, while the decomposition is opposite.

## D6. Predictive entropy is not an uncertainty ontology

D4 and D5 prove by counterexample:

\[
H(Y)\text{ alone}
\not\Rightarrow
\text{aleatoric/epistemic decomposition}.
\]

Any decomposition requires additional latent/model structure.

## D7. Ensemble mixture

For ensemble predictive distributions p_m(y|x), a simple mixture is

\[
\bar p(y|x)=\frac1M\sum_{m=1}^M p_m(y|x).
\]

This identity defines the mixture.

It does not imply that the p_m are posterior draws.

The empirical dispersion of ensemble predictions is therefore an estimator/diagnostic whose probabilistic interpretation depends on how the ensemble was generated.

## D8. MC dropout boundary

Under the cited Gal-Ghahramani framework, stochastic dropout forward passes are connected to a particular approximate-Bayesian inference construction.

The Atlas may compute Monte Carlo averages of stochastic predictions.

It must not infer that arbitrary dropout masks are exact posterior samples.

## D9. Split-conformal rank correction

For n calibration scores and target miscoverage (0<\alpha<1), define

\[
k=\lceil(n+1)(1-\alpha)\rceil.
\]

When (1\le k\le n), use the (k\)-th order statistic of calibration scores as threshold. When (k=n+1), the calibration sample has no (k\)-th order statistic. The standard nonrandomized convention uses the threshold (+\infty); this case occurs for \(\alpha<1/(n+1)\). For example, \(n=4\), \(\alpha=0.1\) gives \(k=\lceil5(0.9)\rceil=5\), so the threshold is \(+\infty\) rather than an undefined fifth calibration value.

Under exchangeability, the future score's rank among n+1 scores is symmetric.

Ignoring ties for the exact finite witness, the rank is uniform.

## D10. Exact n=4 conformal witness

Take n=4 and alpha=0.2.

Then

\[
k=\lceil5(0.8)\rceil=4.
\]

The future score is covered unless it is rank 5, the unique largest score.

Therefore

\[
P(\text{covered})
=
P(\text{rank}\le4)
=
4/5.
\]

This is a marginal rank statement.

It is not a conditional-coverage theorem.

## D11. Coverage is not calibration

Conformal coverage concerns events of the form

\[
Y\in C(X).
\]

Probability calibration concerns

\[
E[Y\mid S]=S
\]

for a probabilistic score.

Neither equation implies the other without extra structure.

## D12. Selective prediction

Let acceptance A in {0,1}, loss L, and

\[
c=P(A=1)>0.
\]

Selective risk is

\[
R_{sel}=E[L\mid A=1].
\]

Equivalently,

\[
R_{sel}=\frac{E[LA]}{E[A]}.
\]

This quantity changes when the acceptance rule changes.

## D13. Exact selective witness

For five equally weighted examples with errors

\[
e=(0,0,0,1,1),
\]

accept all:

\[
c=1,\qquad R_{sel}=2/5.
\]

Accept only the first three:

\[
c=3/5,\qquad R_{sel}=0.
\]

The lower risk is conditional on a smaller accepted population.

## D14. Empirical calibration metrics

If a sample is partitioned into bins B_j, one common empirical calibration summary has the form

\[
ECE
=
\sum_j \frac{|B_j|}{n}
\left|
acc(B_j)-conf(B_j)
\right|.
\]

Changing bins can change ECE without changing the underlying predictor or data.

Therefore ECE is a bin-dependent estimator/summary, not the definition of population calibration.

## D15. Shift boundary

Suppose a property is proved under law P and deployment uses Q.

The P-based identity may remain algebraically true as a definition, but a P-probabilistic guarantee does not automatically become a Q-guarantee.

In particular:

- P-calibration need not imply Q-calibration;
- P-exchangeability does not imply Q-exchangeability;
- P-risk/coverage estimates need not equal Q-risk/coverage.

The downstream Shift chapter owns those changed-law questions.

## Durable propositions

1. Calibration is a conditional-frequency/conditional-expectation property of predicted probabilities.
2. Calibration alone does not determine sharpness or predictive usefulness.
3. Predictive entropy alone cannot identify aleatoric versus epistemic uncertainty.
4. Aleatoric/epistemic decomposition is model-relative.
5. Ensemble mixtures do not make ensemble members posterior samples by definition.
6. MC dropout carries only the approximate-Bayesian semantics established by its framework.
7. Conformal prediction gives a marginal coverage statement under its exchangeability assumptions.
8. Conformal coverage is not probability calibration.
9. Selective prediction trades coverage against risk on accepted examples.
10. Distribution-relative guarantees must be re-established under distribution shift.
