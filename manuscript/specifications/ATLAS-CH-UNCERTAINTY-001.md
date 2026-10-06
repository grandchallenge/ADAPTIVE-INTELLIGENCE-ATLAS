# Chapter Specification — ATLAS-CH-UNCERTAINTY-001

## Identity

Title: Uncertainty and Calibration
Part: Diagnostics, Robustness, and Compression
Status: specification-ready.
Epistemic class: established probability/statistics + source-scoped ML methods + Atlas synthesis.

## Chapter contract

Develop aleatoric/epistemic uncertainty, ensembles, Bayesian approximations, conformal prediction, calibration, and abstention without collapsing their distinct mathematical objects or guarantees.

## Hard prerequisite

ATLAS-CH-INFO-001 / AUDIT-004.

Exact prerequisite identities and external claim boundaries are locked in:

sources/source-locks/ATLAS-CH-UNCERTAINTY-001.yaml

## Reader outcome

A reader should be able to:

1. distinguish predictive uncertainty from uncertainty about model parameters or hypotheses;
2. define binary probability calibration and explain why calibration is not sharpness or accuracy;
3. distinguish predictive entropy from an aleatoric/epistemic decomposition;
4. explain what MC dropout and deep ensembles estimate in their cited frameworks without calling them exact posteriors;
5. state the finite-sample marginal-coverage meaning of conformal prediction under exchangeability;
6. distinguish conformal coverage from probability calibration and conditional coverage;
7. define selective coverage and selective risk;
8. explain how abstention changes the evaluated population;
9. identify which guarantees fail or require re-establishment under distribution shift.

## Formal spine

For binary outcomes Y in {0,1}, let a score S in [0,1] represent a claimed probability of Y=1.

A calibrated score satisfies

\[
P(Y=1\mid S=s)=s
\]

for score values with positive probability, or the corresponding conditional-expectation statement

\[
E[Y\mid S]=S
\]

almost surely.

Calibration does not imply that S is informative about X, sharp, or highly accurate.

## Predictive uncertainty

Given a predictive distribution p(y|x,D), one uncertainty summary is predictive entropy

\[
H(Y\mid x,D).
\]

This summary alone does not identify why the predictive distribution is uncertain.

For a latent model variable Theta,

\[
H(Y\mid x,D)
=
E_{Theta\mid D}[H(Y\mid x,Theta)]
+
I(Y;Theta\mid x,D).
\]

In a declared Bayesian model, the first term can represent expected conditional/noise uncertainty and the mutual-information term can represent model-dependent epistemic uncertainty.

This decomposition is model-relative.

## Exact witness A — same predictive entropy, different decomposition

Model A:

- Theta is fixed;
- Y is Bernoulli(1/2).

Then

\[
H(Y)=1\text{ bit},
\qquad
E[H(Y\mid Theta)]=1,
\qquad
I(Y;Theta)=0.
\]

Model B:

- Theta is Bernoulli(1/2);
- Y=Theta deterministically.

Then the predictive law is still Bernoulli(1/2), so

\[
H(Y)=1\text{ bit},
\]

but

\[
E[H(Y\mid Theta)]=0,
\qquad
I(Y;Theta)=1\text{ bit}.
\]

Thus the same predictive distribution and predictive entropy do not identify the uncertainty decomposition.

## Exact witness B — calibration is not sharpness

Let X be equally likely to be a or b, with

\[
P(Y=1\mid X=a)=0.9,
\qquad
P(Y=1\mid X=b)=0.1.
\]

The marginal positive rate is 0.5.

Predictor S0 always outputs 0.5.

It is calibrated because

\[
P(Y=1\mid S0=0.5)=0.5.
\]

Predictor S1 outputs 0.9 on a and 0.1 on b.

It is also calibrated.

But their Brier risks differ:

\[
E[(Y-S0)^2]=0.25,
\]

while

\[
E[(Y-S1)^2]=0.09.
\]

Both are calibrated; S1 is more informative/sharp for this distribution.

## Bayesian approximations and ensembles

The chapter may discuss:

- MC dropout under the Gal-Ghahramani approximate-Bayesian framework;
- aleatoric/epistemic modeling under the Kendall-Gal paper's declared setting;
- deep ensembles as independently trained predictive models whose empirical spread/mixture can support predictive-uncertainty estimation.

It must not claim:

- dropout samples are exact posterior samples in arbitrary networks;
- ensemble members are posterior samples by definition;
- ensemble variance universally equals epistemic uncertainty;
- the aleatoric/epistemic two-way taxonomy is exhaustive.

## Conformal prediction

Let n calibration nonconformity scores and one future score be exchangeable.

For miscoverage alpha, split conformal uses the finite-sample rank correction

\[
k=\lceil (n+1)(1-\alpha)\rceil.
\]

The prediction set is formed so that the future score is accepted when it does not exceed the corresponding calibration quantile, with the usual convention if k>n.

The guarantee is marginal coverage under the stated exchangeability assumptions.

It is not:

- probability calibration;
- a posterior credible interval;
- arbitrary conditional coverage;
- a distribution-shift guarantee.

## Exact witness C — finite conformal rank

Take n=4 and alpha=0.2.

Then

\[
k=\lceil5(0.8)\rceil=4.
\]

Under exchangeability and no ties, the future score's rank among five scores is uniform on {1,2,3,4,5}.

The split-conformal set accepts exactly when the future score is not the unique largest score.

Therefore

\[
P(\text{covered})=4/5=0.8.
\]

With ties, the standard nonrandomized construction is conservative rather than anti-conservative under its assumptions.

## Selective prediction and abstention

Let A(x) in {0,1} be an acceptance rule.

Coverage is

\[
c=P(A(X)=1).
\]

For loss L, selective risk is

\[
R_{sel}
=
E[L\mid A(X)=1],
\]

when coverage is positive.

This is a conditional performance measure on accepted examples.

It is not a calibration statement.

## Exact witness D — risk/coverage tradeoff

For five ordered examples, suppose the error indicators are

\[
(0,0,0,1,1).
\]

Accepting all five gives

\[
c=1,
\qquad
R_{sel}=2/5.
\]

Accepting only the first three gives

\[
c=3/5,
\qquad
R_{sel}=0.
\]

The risk reduction is achieved by changing coverage.

Nothing in this witness says the underlying predicted probabilities are calibrated.

## Calibration metrics

Empirical diagnostics such as reliability diagrams and expected calibration error depend on finite samples, binning, and aggregation.

The chapter must distinguish:

- population calibration;
- empirical calibration estimates;
- bin-dependent calibration summaries;
- proper scoring rules such as Brier score or log loss.

A low empirical calibration error is not itself a theorem of population calibration.

## Distribution-shift boundary

All i.i.d./exchangeability, calibration, ensemble, Bayesian-approximation, and selective-risk claims are distribution-relative.

The downstream ATLAS-CH-SHIFT-001 chapter must separately analyze what happens when the deployment law differs from the law under which the guarantee or diagnostic was established.

## Failure boundaries

- uncertainty != entropy;
- entropy != epistemic uncertainty;
- confidence != calibration;
- calibration != accuracy;
- calibration != sharpness;
- deep ensemble != exact posterior;
- MC dropout != exact Bayesian inference in arbitrary architectures;
- conformal coverage != conditional coverage;
- conformal coverage != calibration;
- abstention != calibration;
- lower selective risk != unchanged coverage;
- in-distribution guarantee != distribution-shift guarantee.

## Downstream handoff

Direct consumer: ATLAS-CH-SHIFT-001.

SHIFT may inherit:

- the distinct uncertainty objects;
- calibration definitions;
- predictive-entropy decomposition witness;
- conformal exchangeability boundary;
- selective risk/coverage definitions.

SHIFT must independently establish every changed-distribution, robustness, covariate-shift, concept-drift, adversarial, or structural-sensitivity claim.

## Sources

- [@GuoPleissSunWeinberger2017Calibration]
- [@GalGhahramani2016DropoutBayes]
- [@KendallGal2017Uncertainty]
- [@LakshminarayananPritzelBlundell2017DeepEnsembles]
- [@VovkGammermanShafer2005Conformal]
- [@LeiEtAl2018ConformalRegression]
- [@GeifmanElYaniv2017Selective]

Exact source authority and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-UNCERTAINTY-001.yaml
