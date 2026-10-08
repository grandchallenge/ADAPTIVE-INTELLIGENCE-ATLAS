# Uncertainty and Calibration
<!-- ATLAS-CH-UNCERTAINTY-001 -->

**Epistemic status:** established probability/statistics + source-scoped uncertainty methods + Atlas synthesis.

Specification: manuscript/specifications/ATLAS-CH-UNCERTAINTY-001.md
Derivation packet: mathematics/derivations/ATLAS-CH-UNCERTAINTY-001-DERIVATIONS.md
Computational witness: mathematics/computational-witnesses/ATLAS-CW-UNCERTAINTY-001.md
Source lock: sources/source-locks/ATLAS-CH-UNCERTAINTY-001.yaml

A model can be wrong in more than one way.

It can be:

- uncertain because the outcome itself is noisy;
- uncertain because several models or parameter settings remain plausible;
- confident but systematically miscalibrated;
- calibrated but uninformative;
- uncertain in a Bayesian approximation;
- covered by a conformal set without assigning calibrated probabilities;
- accurate on accepted examples only because it abstains on the rest.

These are not synonyms.

This chapter develops a vocabulary for keeping them separate.

The governing principle is:

> A useful uncertainty statement must name the random object, the conditioning information, the estimator or diagnostic, and the guarantee.

## 1. Probability is not yet calibration

Suppose a classifier emits a score

\[
S\in[0,1]
\]

for a binary outcome

\[
Y\in\{0,1\}.
\]

A probability-like number can be read as a claim.

If the model says

\[
S=0.8,
\]

the calibration question is not whether the model is correct on this one example.

It is whether examples receiving score 0.8 are positive about 80 percent of the time under the relevant distribution.

Population calibration can be written as

\[
E[Y\mid S]=S
\]

almost surely.

At an atomic score value,

\[
P(Y=1\mid S=s)=s.
\]

This is a property of the joint law of predictions and outcomes.

It is not a property of the numerical range [0,1] alone.

## 2. Confidence is not calibration

A model can emit scores close to one and still be badly calibrated.

Likewise, a model can be calibrated while rarely producing extreme probabilities.

Guo et al. study confidence calibration in modern neural networks and evaluate post-processing methods including temperature scaling [@GuoPleissSunWeinberger2017Calibration].

The source-scoped lesson is not that temperature scaling universally solves uncertainty.

It is that probability calibration is measurable, can fail in trained neural networks, and can be altered by a post-hoc map without changing the predicted class ordering.

## 3. Calibration is not accuracy

Accuracy asks how often a decision rule is correct.

Calibration asks whether stated probabilities match conditional frequencies.

A classifier can improve one without necessarily improving the other.

Temperature scaling is a useful example: changing logits by a positive scalar temperature does not change the argmax class, yet it can change probability calibration.

This is why uncertainty work should keep:

- decisions;
- scores;
- probability claims;
- losses

as separate objects.

## 4. Calibration is not sharpness

Consider a population with

\[
P(X=a)=P(X=b)=1/2
\]

and

\[
P(Y=1\mid X=a)=0.9,
\qquad
P(Y=1\mid X=b)=0.1.
\]

The marginal positive rate is 0.5.

A constant predictor

\[
S_0=0.5
\]

is calibrated.

So is the predictor

\[
S_1(a)=0.9,
\qquad
S_1(b)=0.1.
\]

But they do not contain the same information.

For the constant predictor,

\[
E[(Y-S_0)^2]=0.25.
\]

For the sharper conditional predictor,

\[
E[(Y-S_1)^2]=0.09.
\]

Both are calibrated.

Only one distinguishes the two covariate regimes.

Therefore:

\[
\boxed{
\text{calibration}
\not\Rightarrow
\text{sharpness or informativeness}.
}
\]

## 5. Proper scoring and calibration are related but distinct

Log loss and Brier score reward probabilistic predictions using the realized outcome.

They are not merely calibration errors.

A predictor can have good calibration and poor resolution.

A predictor can have better proper-score risk while both predictors are calibrated.

The previous exact witness demonstrates this with Brier risk.

The Atlas therefore uses proper scores, calibration diagnostics, and discrimination metrics as distinct evaluation axes.

## 6. Empirical calibration is an estimate

Population calibration is a property of a distribution.

A reliability diagram is a finite-sample diagnostic.

Expected calibration error is a finite-sample, bin-dependent summary.

A common form is

\[
ECE
=
\sum_j
\frac{|B_j|}{n}
\left|
acc(B_j)-conf(B_j)
\right|.
\]

Change the bins and the numerical ECE can change.

Therefore a small empirical ECE is not itself a theorem that

\[
E[Y\mid S]=S
\]

in the deployment population.

## 7. One word, several uncertainty objects

Suppose a model defines a predictive law

\[
p(y\mid x,D).
\]

Possible uncertainty summaries include:

- predictive variance;
- predictive entropy;
- posterior variance over parameters;
- disagreement among models;
- mutual information between predictions and latent model variables;
- width of a prediction interval;
- conformal set size;
- probability of abstention;
- selective risk.

These quantities answer different questions.

A chapter that simply plots an “uncertainty score” without defining the underlying object has not yet specified the claim.

## 8. Predictive entropy

For a discrete predictive law,

\[
H(Y\mid x,D)
=
-\sum_y
p(y\mid x,D)
\log p(y\mid x,D).
\]

Entropy summarizes uncertainty in the predictive distribution.

It does not say where that uncertainty came from.

This matters because the same predictive distribution can arise from very different latent structures.

## 9. Aleatoric and epistemic uncertainty

Kendall and Gal use a two-way distinction in Bayesian deep-learning models for computer vision [@KendallGal2017Uncertainty]:

- aleatoric uncertainty: uncertainty associated with noise inherent in observations or the conditional data model;
- epistemic uncertainty: uncertainty associated with the model and its parameters.

This distinction is useful.

It is not an exhaustive ontology of every uncertainty that can arise in an adaptive system.

Numerical approximation, distribution shift, misspecification, measurement failure, hidden interventions, and unknown unknowns can require other descriptions.

The Atlas therefore treats aleatoric/epistemic language as model-relative.

## 10. Entropy decomposition

Let Theta denote a latent model variable.

Then

\[
I(Y;\Theta)
=
H(Y)-H(Y\mid\Theta).
\]

Equivalently,

\[
H(Y)
=
E_\Theta[H(Y\mid\Theta)]
+
I(Y;\Theta).
\]

In a declared Bayesian predictive model, this can motivate a decomposition into:

- expected conditional uncertainty;
- model-dependent information gain or epistemic component.

The identity is exact.

The interpretation depends on what Theta means.

## 11. Same entropy, opposite decomposition

Consider two models.

### Model A

Theta is fixed.

\[
Y\sim Bernoulli(1/2).
\]

Then

\[
H(Y)=1\text{ bit},
\]

\[
E[H(Y\mid\Theta)]=1,
\]

\[
I(Y;\Theta)=0.
\]

### Model B

\[
\Theta\sim Bernoulli(1/2),
\]

and

\[
Y=\Theta.
\]

Marginally,

\[
Y\sim Bernoulli(1/2).
\]

So again,

\[
H(Y)=1\text{ bit}.
\]

But now conditioning on Theta makes Y deterministic:

\[
E[H(Y\mid\Theta)]=0,
\]

\[
I(Y;\Theta)=1\text{ bit}.
\]

The predictive distribution is identical.

The decomposition is opposite.

Therefore:

\[
\boxed{
\text{predictive entropy alone}
\not\Rightarrow
\text{epistemic uncertainty}.
}
\]

## 12. Reducibility is relative to the information set

The phrase “epistemic uncertainty can be reduced with more data” requires a model and a data-acquisition regime.

More observations of the same kind may reduce parameter uncertainty.

They may fail to resolve:

- structural misspecification;
- unobserved confounding;
- systematic measurement bias;
- an unidentifiable parameterization;
- a changed environment.

So reducibility is not an intrinsic label attached to a scalar variance.

It is relative to the model, observations, and interventions that are possible.

## 13. Bayesian uncertainty

A Bayesian model places a distribution over uncertain quantities and updates it using data.

For parameters Theta,

\[
p(\Theta\mid D)
\propto
p(D\mid\Theta)p(\Theta).
\]

The posterior predictive is

\[
p(y\mid x,D)
=
\int
p(y\mid x,\Theta)
p(\Theta\mid D)
d\Theta.
\]

This is a precise probabilistic object.

A practical neural-network approximation may only approximate it.

The distinction between target and approximation should remain visible.

## 14. Dropout as an approximate Bayesian construction

Gal and Ghahramani develop a theoretical framework relating dropout training in neural networks to approximate Bayesian inference in deep Gaussian-process models [@GalGhahramani2016DropoutBayes].

Within that framework, repeated stochastic forward passes can be used to estimate predictive quantities.

The Atlas preserves two boundaries.

First:

\[
\text{MC dropout}
\neq
\text{exact posterior sampling}.
\]

Second:

\[
\text{dropout used in a network}
\not\Rightarrow
\text{all Bayesian guarantees}.
\]

The interpretation comes from the cited approximation framework, not from randomness alone.

## 15. Deep ensembles

Lakshminarayanan, Pritzel, and Blundell study independently trained neural networks as a simple and scalable method for predictive uncertainty estimation [@LakshminarayananPritzelBlundell2017DeepEnsembles].

Given predictive distributions

\[
p_m(y\mid x),
\qquad
m=1,\dots,M,
\]

an ensemble mixture is

\[
\bar p(y\mid x)
=
\frac1M
\sum_{m=1}^M
p_m(y\mid x).
\]

This is an exact mixture identity.

It does not imply that the members are samples from

\[
p(\Theta\mid D).
\]

Ensemble disagreement can be useful empirically without becoming posterior variance by definition.

## 16. Ensemble spread and epistemic uncertainty

It is tempting to call all disagreement epistemic uncertainty.

That is too fast.

Ensemble spread can depend on:

- initialization;
- optimization path;
- training-data resampling;
- architecture diversity;
- explicit priors;
- regularization;
- stochastic training;
- mode coverage.

The generated ensemble determines what its spread means.

The Atlas therefore says:

> ensemble disagreement is an empirical uncertainty diagnostic whose epistemic interpretation must be justified by the ensemble construction.

## 17. Prediction sets are another object

Sometimes the output is not a probability.

It is a set

\[
C(x)
\]

constructed to contain the future response with a target frequency.

Conformal prediction provides a framework for this kind of set-valued prediction [@VovkGammermanShafer2005Conformal; @LeiEtAl2018ConformalRegression].

Its signature guarantee is coverage under stated exchangeability/randomness assumptions.

That is different from probability calibration.

## 18. Split conformal rank logic

Suppose we have

\[
n
\]

calibration nonconformity scores and one future score.

For target miscoverage \(0<\alpha<1\), the finite-sample rank correction uses

\[
k
=
\left\lceil
(n+1)(1-\alpha)
\right\rceil.
\]

The threshold is the \(k\)-th smallest calibration score **when \(1\le k\le n\)**. If \(k=n+1\), there is no such order statistic in the \(n\) calibration scores; the standard nonrandomized convention sets the threshold to \(+\infty\) (and hence uses an unrestricted prediction set for that score rule). This occurs when \(\alpha<1/(n+1)\). For example, with \(n=4\) and \(\alpha=0.1\), one obtains \(k=5\), not a fifth calibration observation.

Under exchangeability, the future score has a symmetric rank among the

\[
n+1
\]

scores.

This rank symmetry is the core of the finite-sample marginal-coverage logic.

## 19. Exact conformal rank witness

Take

\[
n=4,
\qquad
\alpha=0.2.
\]

Then

\[
k
=
\lceil5(0.8)\rceil
=
4.
\]

Assume no ties.

The future score's rank is uniform over

\[
1,2,3,4,5.
\]

The future point is covered unless its score is the unique largest score.

Hence

\[
P(Y_{new}\in C(X_{new}))
=
\frac45
=
0.8.
\]

This is an exact finite rank argument.

It is marginal.

It is not arbitrary conditional coverage.

## 20. Coverage is not calibration

Calibration concerns statements such as

\[
P(Y=1\mid S=s)=s.
\]

Conformal coverage concerns

\[
P(Y\in C(X))
\ge
1-\alpha
\]

under the construction's assumptions.

A set can have the target marginal coverage without supplying calibrated class probabilities.

A calibrated probability model does not automatically produce a conformal finite-sample coverage theorem.

These are distinct guarantees.

## 21. Distribution-free does not mean assumption-free

The phrase “distribution-free” can be misleading when detached from the sampling assumptions.

Conformal validity does not require a parametric family for the outcome distribution.

It does require the symmetry/exchangeability conditions used by the theorem.

A deployment process with:

- temporal drift;
- feedback;
- covariate shift;
- intervention;
- adaptive selection

can violate the assumptions that justified the original coverage statement.

This boundary passes directly to the downstream Shift chapter.

## 22. Conditional coverage is stronger

Marginal coverage averages over the input distribution.

A stronger statement would require coverage within every relevant subgroup or condition.

Generic finite-sample conformal validity does not automatically give arbitrary exact conditional coverage.

The Atlas will not rewrite a marginal theorem as a subgroup theorem.

## 23. Abstention is another control surface

A model need not predict on every example.

Let

\[
A(X)\in\{0,1\}
\]

indicate acceptance.

Coverage is

\[
c
=
P(A(X)=1).
\]

For loss L, selective risk is

\[
R_{sel}
=
E[L\mid A(X)=1].
\]

Selective classification studies this risk-coverage tradeoff; Geifman and El-Yaniv develop a deep-network construction in this setting [@GeifmanElYaniv2017Selective].

## 24. Exact risk-coverage witness

Suppose five equally weighted examples have error indicators

\[
(0,0,0,1,1).
\]

If we accept all five,

\[
c=1,
\]

and

\[
R_{sel}
=
\frac25.
\]

If we accept only the first three,

\[
c=\frac35,
\]

and

\[
R_{sel}=0.
\]

The accepted predictions are perfect.

But forty percent of the population has been rejected.

The improvement is real and conditional on lower coverage.

## 25. Abstention is not calibration

A selective classifier can reject difficult cases using:

- confidence;
- margin;
- entropy;
- an auxiliary selector;
- a calibrated risk predictor;
- another uncertainty score.

Whatever the mechanism, low selective risk does not prove the underlying probabilities are calibrated.

Conversely, a calibrated predictor need not know which examples to reject to achieve a desired risk-coverage curve.

The objects remain separate.

## 26. Uncertainty and decisions

Uncertainty matters because decisions have asymmetric costs.

A probability estimate may feed:

- abstention;
- escalation to a human;
- additional sensing;
- active learning;
- a larger conformal set;
- a safer controller;
- deferred execution.

But the correct action depends on a loss or utility model.

High entropy does not mathematically imply “abstain.”

That policy requires a decision rule.

## 27. Calibration can be local or global in different senses

A single scalar calibration metric can hide structure.

A model may appear calibrated overall while failing on:

- a demographic subgroup;
- a rare class;
- a region of feature space;
- long-context examples;
- high-loss examples;
- a shifted domain.

The fix is not to call calibration useless.

It is to state the conditioning structure being tested.

## 28. The model can be calibrated for the wrong world

Suppose calibration is established under distribution P.

Deployment occurs under distribution Q.

Even if the scoring function is unchanged,

\[
P(Y=1\mid S=s)
\]

and

\[
Q(Y=1\mid S=s)
\]

need not agree.

Therefore:

\[
\boxed{
P\text{-calibration}
\not\Rightarrow
Q\text{-calibration}.
}
\]

The same caution applies to:

- ensemble diagnostics;
- conformal coverage;
- selective-risk estimates;
- abstention thresholds.

## 29. The uncertainty interface

A downstream component should be able to ask:

1. What is random?
2. What is conditioned on?
3. Is the output a probability, variance, entropy, set, interval, or decision?
4. Is the quantity predictive or parameter/model-level?
5. Is the method Bayesian, approximately Bayesian, ensemble-based, conformal, or purely empirical?
6. What distributional assumptions support the guarantee?
7. Is the guarantee marginal or conditional?
8. Is abstention changing the evaluated population?
9. Was calibration measured or proved?
10. Does deployment match the law under which the statement was established?

This is the chapter's practical contract.

## 30. Handoff to Distribution Shift and Robustness

The direct consumer is

ATLAS-CH-SHIFT-001.

SHIFT may inherit:

- population calibration definitions;
- the calibration-versus-sharpness witness;
- the predictive entropy decomposition;
- the same-entropy/opposite-decomposition counterexample;
- source-scoped MC-dropout and ensemble semantics;
- conformal rank coverage and its exchangeability boundary;
- selective coverage and selective risk.

SHIFT must independently establish what survives when the data law changes.

In particular it must not assume:

\[
\text{i.i.d. calibration}
\Rightarrow
\text{shifted calibration},
\]

or

\[
\text{exchangeable conformal coverage}
\Rightarrow
\text{coverage under arbitrary drift}.
\]

## 31. Failure modes

The most common category errors are:

- calling confidence calibration “uncertainty estimation” without saying what is uncertain;
- calling predictive entropy epistemic uncertainty;
- treating ensemble members as posterior samples by definition;
- treating stochastic dropout passes as exact Bayesian posterior samples;
- treating a conformal set as a Bayesian credible region;
- treating marginal coverage as arbitrary conditional coverage;
- treating low ECE as population calibration;
- treating low selective risk as unchanged-population accuracy;
- treating abstention as calibration;
- transporting an in-distribution guarantee into a shifted environment without revalidation.

## 32. Closing view

Uncertainty is not one number.

The Atlas uses a family of objects:

\[
\boxed{
\begin{array}{l}
\text{probability calibration},\\
\text{predictive entropy},\\
\text{model/posterior uncertainty},\\
\text{aleatoric uncertainty},\\
\text{ensemble disagreement},\\
\text{conformal coverage},\\
\text{selective risk and coverage}.
\end{array}
}
\]

Each object comes with its own assumptions and its own question.

The durable rule is:

> Before using an uncertainty estimate, name what it estimates and name the guarantee it actually carries.

## References used in this chapter

- [@GuoPleissSunWeinberger2017Calibration]
- [@GalGhahramani2016DropoutBayes]
- [@KendallGal2017Uncertainty]
- [@LakshminarayananPritzelBlundell2017DeepEnsembles]
- [@VovkGammermanShafer2005Conformal]
- [@LeiEtAl2018ConformalRegression]
- [@GeifmanElYaniv2017Selective]

Exact provenance and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-UNCERTAINTY-001.yaml
