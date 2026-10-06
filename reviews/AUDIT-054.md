# AUDIT-054 — Uncertainty and Calibration

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-UNCERTAINTY-001 remains at draft-v0.1.

The audit found no mathematical, epistemic, source-scope, dependency, citation, or documentary defect requiring repair.

No publication, theorem certification, or release promotion is implied.

## Audited baseline

- implementation merge: 8dfb5a09bebf4c15d8257bb74d9b3657688b2d8b
- implementation PR: #216
- implementation issue: #215
- audit issue: #217
- chapter: ATLAS-CH-UNCERTAINTY-001

Merged implementation artifact blobs:

- specification: efa855b00af94780f08f9267ed6357ec847374c9
- derivation packet: 997cba9eb0c8f48d06c1155c5e17f7db74c964ae
- computational witness: 01f8fff254fb0a458935c716ce07da389a4a33ef
- manuscript: e6714d0505a96e2bfdc431b4ec60d50b0044efa6
- source lock: b9f38d496efe2d704b759510cf171d5a3e83a2c8
- Chapter Ledger: 4c854cfd4f7e19db3399d78c95cb90a99a4da9eb
- Source Register: ae7b98bb7b758631c202f004c444180dcfbb5401
- bibliography: afafee05f9fd71932e067e34a061e970c1685f90
- transaction receipt: 1d501e5016a9bca664de71c62d3e0993194fd1a6

## 1. Hard prerequisite identity

PASS.

The source lock binds exactly to the protected baseline 1fa80bdae8e5219cc7e90b481914b66e3af8c3aa.

Probability, Information, and Statistical Structure:

- manuscript: 0fca10cbc7476c5b729ee15dfad0dec563665821
- source lock: ea5a1b0db3aadf052fc0b749d7e813bb0ca5d43c
- AUDIT-004: 948f76b3f86d27fa4830efc30d8ef0135134256e

No downstream Distribution Shift chapter is used as hidden prerequisite authority.

## 2. External source scope

PASS.

The source lock uses:

- Guo et al. for neural-network confidence calibration and temperature-scaling experiments;
- Gal and Ghahramani for the specific approximate-Bayesian interpretation of dropout developed in that paper;
- Kendall and Gal for the paper's aleatoric/epistemic decomposition in Bayesian deep-learning vision models;
- Lakshminarayanan et al. for deep-ensemble predictive-uncertainty experiments;
- Vovk, Gammerman, and Shafer for foundational conformal-prediction validity;
- Lei et al. for full/split conformal regression and finite-sample marginal coverage;
- Geifman and El-Yaniv for selective-classification risk/coverage control.

The chapter does not promote paper-scoped empirical claims into universal theorems.

The source lock explicitly blocks:

- deep ensemble = exact posterior;
- MC dropout = exact posterior sampling;
- conformal coverage = calibration;
- selective risk = calibration;
- in-distribution guarantee = distribution-shift guarantee.

## 3. Population calibration definition

PASS.

For binary Y and probabilistic score S, the chapter uses

\[
E[Y\mid S]=S
\]

almost surely.

At score atoms with positive probability this becomes

\[
P(Y=1\mid S=s)=s.
\]

This is a correct probability-calibration object.

The chapter does not confuse score range [0,1] with calibration.

## 4. Calibration versus accuracy

PASS.

The chapter correctly distinguishes:

- class decision;
- probability score;
- calibration property;
- proper score/loss.

Temperature scaling is used only as a source-scoped example that can change probability calibration while preserving argmax ordering for positive temperature.

No universal effectiveness claim is made.

## 5. Calibration versus sharpness witness

PASS.

The population is:

\[
P(X=a)=P(X=b)=1/2,
\]

\[
P(Y=1\mid a)=0.9,
\qquad
P(Y=1\mid b)=0.1.
\]

The marginal positive rate is 0.5.

Constant predictor:

\[
S_0=0.5
\]

is calibrated.

Conditional predictor:

\[
S_1(a)=0.9,
\qquad
S_1(b)=0.1
\]

is also calibrated.

Independent exact replay gives:

\[
E[(Y-S_0)^2]=1/4=0.25,
\]

\[
E[(Y-S_1)^2]=9/100=0.09.
\]

Thus the counterexample correctly proves that calibration does not determine sharpness/informativeness or Brier risk.

## 6. Predictive entropy decomposition

PASS.

The chapter uses

\[
H(Y)
=
E[H(Y\mid\Theta)]
+
I(Y;\Theta).
\]

This is the standard mutual-information identity under the declared latent-variable model.

The chapter explicitly marks the aleatoric/epistemic interpretation as model-relative.

## 7. Same-predictive-law counterexample

PASS.

### Model A

Theta is fixed and

\[
Y\sim Bernoulli(1/2).
\]

Therefore:

\[
H(Y)=1,
\qquad
E[H(Y\mid\Theta)]=1,
\qquad
I(Y;\Theta)=0.
\]

### Model B

\[
\Theta\sim Bernoulli(1/2),
\qquad
Y=\Theta.
\]

Marginally Y is again Bernoulli(1/2), so

\[
H(Y)=1.
\]

But conditional on Theta, Y is deterministic:

\[
E[H(Y\mid\Theta)]=0,
\qquad
I(Y;\Theta)=1.
\]

Thus identical predictive law and entropy can correspond to opposite decomposition.

The chapter correctly concludes only that predictive entropy alone cannot identify the decomposition.

## 8. Aleatoric/epistemic taxonomy boundary

PASS.

The chapter treats the Kendall-Gal two-way taxonomy as useful but not exhaustive.

It explicitly leaves room for:

- numerical uncertainty;
- misspecification;
- distribution shift;
- measurement failure;
- hidden interventions;
- other model-dependent uncertainty sources.

No exhaustive ontology is claimed.

## 9. MC-dropout boundary

PASS.

The chapter treats MC dropout only under the cited Gal-Ghahramani approximate-Bayesian framework.

It does not call arbitrary dropout masks exact posterior samples.

It does not infer universal calibration or Bayesian guarantees from dropout usage alone.

## 10. Deep-ensemble boundary

PASS.

For predictive distributions p_m, the chapter defines the mixture

\[
\bar p
=
\frac1M\sum_m p_m.
\]

This mixture identity is correct.

It does not imply that ensemble members are posterior draws.

The manuscript correctly describes disagreement as an empirical diagnostic whose epistemic interpretation depends on ensemble construction.

## 11. Conformal rank construction

PASS.

For n calibration scores and target miscoverage alpha, the chapter uses

\[
k=\lceil(n+1)(1-\alpha)\rceil.
\]

It explicitly states the exchangeability assumption and the usual finite-sample convention.

It does not rewrite distribution-free as assumption-free.

## 12. Exact conformal witness

PASS.

For

\[
n=4,
\qquad
\alpha=0.2,
\]

independent replay gives

\[
k=\lceil5(0.8)\rceil=4.
\]

Under exchangeability and no ties, the future score rank is uniform on five positions.

Coverage occurs for ranks 1 through 4, hence

\[
P(\text{covered})=4/5=0.8.
\]

The chapter correctly labels this as marginal rank coverage.

It does not claim arbitrary exact conditional coverage.

## 13. Conformal coverage versus calibration

PASS.

The chapter keeps separate:

\[
Y\in C(X)
\]

coverage events and

\[
E[Y\mid S]=S
\]

probability calibration.

No implication between them is asserted without extra structure.

Conformal sets are not called Bayesian credible regions.

## 14. Selective prediction definition

PASS.

For acceptance A and loss L, the chapter defines:

\[
c=P(A=1),
\]

and when c>0,

\[
R_{sel}=E[L\mid A=1].
\]

The equivalent ratio form

\[
R_{sel}=\frac{E[LA]}{E[A]}
\]

is correct.

## 15. Exact selective risk/coverage witness

PASS.

For errors

\[
(0,0,0,1,1),
\]

accepting all five yields:

\[
coverage=1,
\qquad
risk=2/5.
\]

Accepting the first three yields:

\[
coverage=3/5,
\qquad
risk=0.
\]

The chapter correctly states that lower selective risk is conditional on a smaller accepted population.

It does not infer probability calibration from abstention.

## 16. Empirical calibration metric boundary

PASS.

The chapter presents binned ECE as an empirical summary and explicitly records its dependence on finite samples, aggregation, and binning.

It does not define population calibration through ECE.

Proper scoring rules are kept separate from calibration summaries.

## 17. Decision boundary

PASS.

The chapter does not infer a policy directly from entropy or uncertainty.

It states that abstention, escalation, additional sensing, active learning, or other actions require a loss/utility rule.

Thus diagnostic uncertainty and decision policy remain distinct objects.

## 18. Distribution-shift handoff

PASS.

The chapter explicitly records:

- P-calibration does not imply Q-calibration;
- P-exchangeability does not imply Q-exchangeability;
- P risk/coverage estimates need not equal Q risk/coverage.

The direct consumer ATLAS-CH-SHIFT-001 must independently establish changed-law guarantees.

This is the correct forward boundary.

## 19. Bibliography and citation resolution

PASS.

Seven new bibliography keys are registered:

- GuoPleissSunWeinberger2017Calibration
- GalGhahramani2016DropoutBayes
- KendallGal2017Uncertainty
- LakshminarayananPritzelBlundell2017DeepEnsembles
- VovkGammermanShafer2005Conformal
- LeiEtAl2018ConformalRegression
- GeifmanElYaniv2017Selective

All reader-facing citations resolve under canonical validation.

## 20. Repository integrity

PASS subject to audit-PR validation.

At the implementation merge:

- Chapter Ledger: 4c854cfd4f7e19db3399d78c95cb90a99a4da9eb
- Source Register: ae7b98bb7b758631c202f004c444180dcfbb5401
- bibliography: afafee05f9fd71932e067e34a061e970c1685f90
- chapter status: draft-v0.1
- hard dependency unchanged
- no governed figure introduced

Implementation exact head 845a5e62b7b2e2a40d01683f98954f3ff9dcbc12 passed:

- canonical Linux validation;
- GitHub Actions validation.

## Final disposition

AUDIT-054 passes with no repair.

The durable UNCERTAINTY layer is:

**probability calibration + explicit sharpness distinction + model-relative entropy decomposition + source-scoped Bayesian/ensemble approximations + exchangeability-bounded conformal coverage + explicit selective risk/coverage + hard distribution-shift handoff.**
