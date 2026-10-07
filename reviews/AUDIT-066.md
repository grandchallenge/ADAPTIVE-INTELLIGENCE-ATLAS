# AUDIT-066 — Distribution Shift and Robustness

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-SHIFT-001 remains at draft-v0.1.

The audit found no mathematical, dependency, source-scope, provenance, witness, bibliography, protocol, or repository defect requiring repair.

## Audited implementation

- implementation issue: #263
- implementation PR: #264
- exact validated implementation head: 98eeee1ed12d9ed513617ce33ee96d663f6706a5
- implementation GitHub Actions run: 37551352063
- implementation merge / audited protected baseline: af551d732d83c6751051c864206df4bb153e5a3f
- audit issue: #265
- audit branch: audit/a265
- chapter: ATLAS-CH-SHIFT-001

Protected implementation artifact identities:

- specification: b0d7a0a85e56c065b8977ba523b75601366ffc6f
- derivation packet: b12d6ef827f8095c8599c7dcc610e223ae2c769d
- computational witness: 4bf2a0b95d8e1ade101b00c9aa15afb4ee1dd77b
- reader manuscript: 064b7f05068eb212eacbb64228e51b6069d2728f
- source lock: 5c96c8b3efc459308db680dada19ebc767209634
- bibliography: ed8976909306cde1ef6a92de5383c1cd61600484
- Chapter Ledger: 94ae4b045410a8fe1e2dce84d160b78a0f163629
- Source Register: 540d7ff9a0e0e2668ca5444a4a42456b22c94d4a
- transaction receipt: 62a0f5405b0837b1a199d968b0d7a6308f5fefe9

## 1. Hard prerequisite

PASS.

UNCERTAINTY-001 is bound exactly:

- manuscript e6714d0505a96e2bfdc431b4ec60d50b0044efa6;
- source lock b9f38d496efe2d704b759510cf171d5a3e83a2c8;
- AUDIT-054 132a0df9a603ec88811312d193971100549648a4.

SHIFT preserves the prerequisite boundary: calibration, coverage, selective risk, and uncertainty diagnostics are scoped to the law and assumptions under which they were established. No source-law guarantee is silently promoted to a changed deployment law.

## 2. New source scope

PASS.

The chapter adds only:

- Sugiyama, Krauledat, and Müller (2007), *Covariate Shift Adaptation by Importance Weighted Cross Validation*;
- Madry, Makelov, Schmidt, Tsipras, and Vladu (2018), *Towards Deep Learning Models Resistant to Adversarial Attacks*.

Their use is narrow:

- covariate shift with changed input marginal and invariant conditional output law, plus importance-weighted correction/model-selection claims under stated assumptions;
- adversarial robustness formulated through robust optimization against a declared perturbation/adversary class.

Neither source is used as authority for the Atlas-owned finite calibration, benign-shift, support-failure, conditional-shift, or adversarial-separation witnesses.

## 3. Bibliography integrity

PASS.

The bibliography contains the keys:

- SugiyamaKrauledatMuller2007Covariate;
- MadryEtAl2018Adversarial.

The manuscript and source lock reference those exact keys. No unrelated bibliography change is introduced.

## 4. Source and deployment laws

PASS.

The chapter explicitly separates source law P from deployment law Q and writes source and deployment risk as different expectations. Changed-law claims therefore bind to a declared probability law rather than only to a fixed model artifact.

## 5. Covariate versus conditional shift

PASS.

Covariate shift is typed as a changed X-marginal with invariant conditional Y|X. Conditional/concept shift is typed as a changed conditional law. The chapter explicitly blocks the inference that X-density-ratio weighting repairs conditional shift.

## 6. Importance-weight identity

PASS.

Under covariate shift and Q_X absolutely continuous with respect to P_X, the chapter derives

\[
R_Q(f)=\mathbb E_P[w(X)L(f(X),Y)],
\qquad
w=\frac{dQ_X}{dP_X}.
\]

The support/absolute-continuity assumption is stated as part of the claim rather than as an implementation detail.

## 7. Support-failure boundary

PASS.

The chapter correctly rejects ordinary density-ratio correction when Q assigns positive mass to source-zero support. It does not claim reweighting can synthesize evidence for target-only support without additional assumptions.

## 8. Exact calibration-failure witness

PASS.

For X in {a,b}, deterministic labels Y(a)=1, Y(b)=0, constant score 1/2, source marginal (1/2,1/2), and deployment marginal (3/4,1/4):

- source event rate at the sole score level is 1/2;
- deployment event rate at the same score level is 3/4;
- source calibration gap is 0;
- deployment calibration gap is 1/4.

The predictor is unchanged and Y|X is unchanged. This is therefore an exact pure-covariate-shift calibration failure.

Independent audit replay agrees.

## 9. Brier-risk control

PASS.

For the same witness, squared error is 1/4 for either label under the constant 1/2 score. Hence source and deployment Brier risk both equal 1/4.

The chapter therefore correctly demonstrates that calibration degradation need not imply a change in this predictive-risk metric.

## 10. Exact importance weights

PASS.

The finite weights are:

\[
w(a)=3/2,
\qquad
w(b)=1/2.
\]

Their source expectation is one, and the reweighted source event rate is 3/4, exactly matching the target event rate.

## 11. Benign marginal-shift control

PASS.

For the perfect two-point predictor with source X-marginal (1/2,1/2) and deployment marginal (9/10,1/10):

\[
\operatorname{TV}(P_X,Q_X)=2/5,
\]

while source and target 0/1 risks both equal zero.

Thus a correctly detected marginal shift does not itself establish task failure.

## 12. Conditional-shift control

PASS.

With unchanged X-marginal but reversed deterministic labels under Q, the source-perfect predictor has target risk one while the X-density ratio is identically one.

This exactly demonstrates that covariate reweighting does not generally repair conditional shift.

## 13. Adversarial clean/worst-case separation

PASS.

The exact two-point classifier has clean risk zero. Under the declared perturbation set allowing either input while the original label is retained, worst-case adversarial risk is one.

Thus clean average-case risk and adversarial risk are distinct objects.

## 14. Perturbation-set dependence

PASS.

The chapter states that if the perturbation set is reduced to the identity-only set, adversarial risk returns to clean risk. Robustness is therefore correctly treated as relative to a declared threat/perturbation set.

## 15. Average-case versus worst-case firewall

PASS.

The manuscript distinguishes an expectation under a deployment law Q from a supremum over a perturbation set. It does not identify ordinary distribution shift with adversarial robustness.

## 16. Calibration, coverage, and selective-risk firewall

PASS.

The chapter preserves the inherited separation among:

- population calibration;
- conformal/marginal coverage;
- selective risk;
- source predictive risk;
- deployment predictive risk;
- adversarial risk;
- structural sensitivity.

No one metric is promoted as a universal robustness surrogate.

## 17. Structural-sensitivity boundary

PASS.

Structural shift is tied to an explicitly changed component or mechanism such as topology, routing/capacity, tokenizer, measurement process, or feature-generation rule. Changed predictive statistics alone are not treated as causal identification of the changed mechanism.

## 18. Transaction-receipt provenance

PASS.

Every implementation artifact identity recorded in governance/tranches/SHIFT-001.md matches the protected implementation merge. The protected receipt itself is blob 62a0f5405b0837b1a199d968b0d7a6308f5fefe9.

The only pre-merge repairs were repository-protocol repairs to the manuscript reference heading and witness claim-boundary marker; the receipt was explicitly rebound to their repaired blob identities before validation and merge.

## 19. Repository integrity

PASS subject to audit-PR validation.

At the audited implementation merge:

- SHIFT status is draft-v0.1;
- canonical specification/manuscript/derivation/source-lock/witness paths are populated;
- hard dependency remains UNCERTAINTY-001;
- the SHIFT source lock is registered;
- both new bibliography keys resolve;
- no governed figure is introduced;
- exact implementation head passed GitHub Actions run 37551352063;
- protected implementation merge passed canonical repository validation;
- independent audit replay returned SHIFT_AUDIT_WITNESS_OK.

## Final disposition

AUDIT-066 passes with no repair.

The durable SHIFT rule is:

**robustness is always relative to a declared law, metric, and perturbation or mechanism class. A detected distributional change is evidence of change, but is not by itself evidence of task failure, calibration failure, adversarial vulnerability, or structural cause.**
