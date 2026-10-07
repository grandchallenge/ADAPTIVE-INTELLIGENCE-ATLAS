# Distribution Shift and Robustness
<!-- ATLAS-CH-SHIFT-001 -->

**Epistemic status:** audited Uncertainty substrate + primary covariate-shift and adversarial-robust-optimization sources + Atlas-owned exact finite witnesses.  
**Specification:** manuscript/specifications/ATLAS-CH-SHIFT-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-SHIFT-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-SHIFT-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-SHIFT-001.yaml

A model can remain numerically unchanged while the world in which it is evaluated changes.

That forces a discipline:

\[
\boxed{\text{name the source law and deployment law before claiming robustness under shift.}}
\]

## 1. Source law is not deployment law

Let P be the law under which a guarantee, diagnostic, or empirical estimate was established. Let Q be the deployment law. For predictor f and loss L,

\[
R_P(f)=\mathbb E_P[L(f(X),Y)],
\]

\[
R_Q(f)=\mathbb E_Q[L(f(X),Y)].
\]

These are different mathematical objects unless P=Q or a bridge is proved.

The Uncertainty chapter established that calibration, conformal coverage, selective risk, predictive entropy, and other uncertainty objects are assumption-scoped. SHIFT adds the changed-law layer.

## 2. Distribution shift is not one phenomenon

### Covariate shift

\[
P_X\neq Q_X,\qquad P(Y\mid X)=Q(Y\mid X).
\]

Sugiyama, Krauledat, and Müller study this setting and importance-weighted correction/model-selection methods [@SugiyamaKrauledatMuller2007Covariate].

### Label/prior shift

The class prior changes while an appropriate class-conditional mechanism is held fixed.

### Concept or conditional shift

\[
P(Y\mid X)\neq Q(Y\mid X).
\]

Changing only X-weights cannot generally repair this.

### Structural shift

A mechanism, topology, measurement process, routing rule, tokenizer, feature generator, or other declared system component changes. Structural shift is not identified merely because output statistics changed.

## 3. Covariate shift permits a change of measure

If

\[
P(Y\mid X)=Q(Y\mid X)
\]

and

\[
Q_X\ll P_X,
\]

define

\[
w(x)=\frac{dQ_X}{dP_X}(x).
\]

Then

\[
R_Q(f)=\mathbb E_P[w(X)L(f(X),Y)].
\]

This is not extrapolation. It requires the relevant target support to lie within source support.

## 4. Target-only support is a real boundary

If some region has P_X(x)=0 and Q_X(x)>0, the ordinary importance ratio is unavailable there. No finite reweighting of observed source examples creates evidence about a target-only region. Extra modeling assumptions may permit extrapolation, but they must be declared.

## 5. Exact witness: calibration can fail under pure covariate shift

Let X have two states a and b. Outcomes are deterministic:

\[
Y(a)=1,\qquad Y(b)=0.
\]

Under the source law,

\[
P_X(a)=P_X(b)=1/2.
\]

Under deployment,

\[
Q_X(a)=3/4,\qquad Q_X(b)=1/4.
\]

Nothing about Y|X changed.

Use the same predictor before and after deployment:

\[
s(a)=s(b)=1/2.
\]

Under P, the event frequency among all points receiving score 1/2 is 1/2, so the sole score level is perfectly calibrated.

Under Q, the event frequency is 3/4 while the predictor still emits 1/2. The deployment calibration gap is

\[
\boxed{1/4}.
\]

The model did not change. The conditional outcome mechanism did not change. Only the covariate mixture changed.

## 6. Calibration failure need not mean every risk changed

For the same predictor,

\[
(1/2-Y)^2=1/4
\]

for either label. Thus Brier risk is

\[
\boxed{1/4}
\]

under both P and Q.

So calibration deterioration and generic predictive-risk deterioration are not the same statement.

## 7. Exact importance weights

For that shift,

\[
w(a)=\frac{3/4}{1/2}=\frac32,
\]

\[
w(b)=\frac{1/4}{1/2}=\frac12.
\]

And

\[
\frac12\frac32+\frac12\frac12=1.
\]

The reweighted source event rate is

\[
\frac12\frac32=\frac34,
\]

which exactly recovers the deployment event rate.

## 8. A detected marginal shift need not be a performance failure

Let X in {u,v}, with Y(u)=0 and Y(v)=1. Use exact predictor f(u)=0, f(v)=1.

Let

\[
P_X=(1/2,1/2)
\]

and

\[
Q_X=(9/10,1/10).
\]

The marginal laws differ substantially:

\[
\operatorname{TV}(P_X,Q_X)=2/5.
\]

Yet the predictor is right on every input under both laws. Therefore

\[
\boxed{R_P^{0/1}=R_Q^{0/1}=0}.
\]

A shift detector can be correct that the input marginal changed while a task-failure alarm would be wrong.

## 9. Concept shift is different

Keep the same X-marginal, but reverse the conditional labels under deployment. Then

\[
P_X=Q_X
\]

while

\[
P(Y\mid X)\neq Q(Y\mid X).
\]

The source-perfect predictor now has target error one. The covariate density ratio is identically one, so X-reweighting does nothing.

This is why distribution shift is too coarse a diagnosis.

## 10. Calibration, coverage, and selective risk each have their own transfer problem

A guarantee under P can depend on exchangeability, score distribution, subgroup mixture, acceptance threshold, calibration level sets, or loss distribution. Changing P to Q can disturb these in different ways.

Therefore:

\[
P\text{-calibration}\not\Rightarrow Q\text{-calibration},
\]

\[
P\text{-coverage}\not\Rightarrow Q\text{-coverage},
\]

and

\[
P\text{-selective-risk control}\not\Rightarrow Q\text{-selective-risk control}.
\]

Each transfer needs its own assumptions.

## 11. Adversarial robustness asks a different question

Average-case target risk is

\[
R_Q(f)=\mathbb E_Q[L(f(X),Y)].
\]

Adversarial risk instead has the form

\[
R_{\rm adv}(f)=\mathbb E_P\left[\sup_{x'\in\Delta(X)}L(f(x'),Y)\right].
\]

Madry et al. study adversarial robustness through robust optimization against a specified perturbation/adversary class [@MadryEtAl2018Adversarial].

The supremum is the important difference. A deployment distribution and a worst-case perturbation set are not interchangeable objects.

## 12. Exact adversarial separation

Take X in {-1,+1}, with labels matching sign, and a perfect predictor. Clean risk is zero.

Declare

\[
\Delta(-1)=\Delta(+1)=\{-1,+1\}.
\]

For either original example, the adversary can choose the opposite input while the original label is retained. Thus worst-case loss is one at every source point:

\[
\boxed{R_{\rm adv}=1}.
\]

So R_P=0 can coexist with R_adv=1.

## 13. Robustness is perturbation-set relative

If instead Delta(x)={x}, adversarial risk equals clean risk. The model did not change; only the allowed perturbation set changed. Therefore “robust” is incomplete without the threat/perturbation model.

## 14. Robust optimization

A robust-training objective is schematically

\[
\min_\theta\mathbb E_P\left[\sup_{\delta\in\Delta(X)}L(f_\theta(X+\delta),Y)\right].
\]

The objective is meaningful only with a declared data law, perturbation set, loss, and optimization approximation. Robustness to one perturbation family is not automatically robustness to another.

## 15. Structural sensitivity is not an adversarial synonym

Suppose a system component changes: tokenizer, routing topology, communication graph, measurement process, sensor transform, feature-generation mechanism, or intervention policy.

A structural-sensitivity analysis must name that component and compare behavior across the change. A change in predictive statistics can signal changed behavior but cannot by itself identify which mechanism changed.

## 16. Average-case shift is not worst-case shift

A law Q assigns probability mass. An adversarial set Delta(x) specifies possible worst-case alternatives around a point.

One integrates:

\[
\mathbb E_Q[\cdot].
\]

The other maximizes:

\[
\sup_{\delta\in\Delta(x)}[\cdot].
\]

Neither operation silently replaces the other.

## 17. Shift magnitude is metric-relative

Even “large shift” requires a discrepancy: total variation, KL divergence, Wasserstein distance, feature discrepancy, calibration change, risk change, or structural edit magnitude. These can rank changes differently.

The benign marginal-shift witness has nonzero total variation but zero task-risk change.

## 18. Support overlap determines what reweighting can say

Importance weighting is strongest when target mass is represented in source support. Poor overlap creates large weights and unstable estimation. Zero overlap creates a literal support failure for ordinary density-ratio correction.

The support condition is therefore part of the claim.

## 19. The unchanged model can still face a changed theorem

When deployment law changes, model parameters, architecture, scoring rule, threshold, and code may all remain fixed. Yet the guarantee can change because its probability law changed.

Governance must bind guarantees to laws, not only model artifacts.

## 20. Metric firewall

SHIFT keeps separate calibration, conformal/marginal coverage, selective risk, source predictive risk, deployment predictive risk, adversarial risk, and structural sensitivity. Every experiment must state which object it measured.

## 21. What SHIFT does not license

It does not license:

- shift detected implies model failed;
- source calibration implies deployment calibration;
- good target-average risk implies adversarial robustness;
- changed outputs imply an identified structural cause.

## 22. Operational checklist

For every deployment-shift claim:
1. name P;
2. name Q;
3. name the changed marginal, conditional, or mechanism;
4. name the metric;
5. check support;
6. state average-case versus worst-case semantics;
7. separate detection from performance;
8. separate predictive failure from causal diagnosis;
9. replay an exact or empirical witness;
10. state what remains unproved.

## 23. Durable rule

\[
\boxed{\text{robustness is always relative to a law, metric, and perturbation/mechanism class.}}
\]

A detected change is evidence of change. It is not by itself evidence of task failure, calibration failure, adversarial vulnerability, or structural cause.

## References used in this chapter

- [@SugiyamaKrauledatMuller2007Covariate]
- [@MadryEtAl2018Adversarial]
