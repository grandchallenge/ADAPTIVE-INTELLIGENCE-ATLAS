# Chapter Specification — ATLAS-CH-SHIFT-001

## Identity

**Title:** Distribution Shift and Robustness  
**Part:** Diagnostics, Robustness, and Compression  
**Status target:** draft-v0.1  
**Implementation issue:** #263  
**Protected baseline:** 01a4c2c7d526df385bb8b2ab58046c3c476e3629

## Hard prerequisite

ATLAS-CH-UNCERTAINTY-001 / AUDIT-054.

SHIFT may inherit population calibration definitions, distinct predictive-uncertainty objects, conformal coverage and exchangeability boundaries, selective risk/coverage semantics, exact finite uncertainty witnesses, and the rule that guarantees are scoped to their stated law and assumptions. SHIFT must independently establish all claims under changed deployment law Q.

## New primary source scope

- Sugiyama, Krauledat, and Müller (2007): covariate shift and importance-weighted correction/model selection.
- Madry, Makelov, Schmidt, Tsipras, and Vladu (2018): adversarial robustness through robust optimization over a declared perturbation set.

The exact finite shift and robustness witnesses in this chapter are Atlas-owned.

## Chapter contract

Every distribution-shift statement must type at least: source law P; deployment law Q; prediction rule f or probabilistic predictor s; loss/metric; which marginal or conditional changes; and support/absolute-continuity assumptions if reweighting is used.

The chapter distinguishes covariate shift, label/prior shift, concept/conditional shift, average-case deployment-law shift, adversarial perturbation, and structural/mechanism shift. These are not synonyms.

## Covariate shift

For joint laws P and Q on (X,Y), covariate shift means

\[
P_X \neq Q_X,\qquad P(Y\mid X)=Q(Y\mid X)
\]

on the relevant support.

For loss L,

\[
R_Q(f)=\mathbb E_Q[L(f(X),Y)].
\]

If Q_X is absolutely continuous with respect to P_X, with

\[
w(x)=\frac{dQ_X}{dP_X}(x),
\]

then

\[
R_Q(f)=\mathbb E_P[w(X)L(f(X),Y)].
\]

No density-ratio correction is asserted where Q_X puts mass outside the support of P_X.

## Concept/conditional shift

Concept/conditional shift changes P(Y|X) to a different Q(Y|X), possibly with P_X=Q_X. Importance weighting of X alone does not in general correct conditional shift.

## Exact witness A — calibration can fail under pure covariate shift

Let X in {a,b}, with Y=1 at a and Y=0 at b under both P and Q. Let

\[
P_X(a)=P_X(b)=1/2,
\]

and

\[
Q_X(a)=3/4,\qquad Q_X(b)=1/4.
\]

Use the unchanged probabilistic predictor

\[
s(a)=s(b)=1/2.
\]

Under P,

\[
\mathbb E_P[Y\mid s(X)=1/2]=1/2,
\]

so the sole score level is perfectly population calibrated. Under Q,

\[
\mathbb E_Q[Y\mid s(X)=1/2]=3/4,
\]

while the predictor still outputs 1/2. Therefore the calibration gap is

\[
\boxed{1/4}.
\]

This is pure covariate shift: the conditional law Y|X is unchanged.

### Brier-risk control

For either label,

\[
(1/2-Y)^2=1/4.
\]

Hence

\[
R_P^{\rm Brier}=R_Q^{\rm Brier}=1/4.
\]

So calibration can degrade while this predictive risk remains unchanged.

## Exact witness B — marginal shift need not cause task failure

Let X in {u,v}, with Y=0 at u and Y=1 at v. Use deterministic predictor f(u)=0, f(v)=1. Let

\[
P_X(u)=P_X(v)=1/2,
\]

and

\[
Q_X(u)=9/10,\qquad Q_X(v)=1/10.
\]

Then P_X differs from Q_X, with total variation distance

\[
\operatorname{TV}(P_X,Q_X)=2/5.
\]

But P(Y|X)=Q(Y|X), and the predictor remains perfect:

\[
\boxed{R_P^{0/1}(f)=R_Q^{0/1}(f)=0}.
\]

Therefore a detected marginal shift does not imply performance failure.

## Exact importance-weight identity

For Witness A,

\[
w(a)=3/2,\qquad w(b)=1/2.
\]

For any function g(X,Y),

\[
\mathbb E_Q[g]=\mathbb E_P[w(X)g]
\]

because the conditional law is unchanged and both target points lie in source support. The chapter must not generalize this identity to conditional shift.

## Support failure control

If P_X(a)=1 but Q_X(b)>0, then P_X(b)=0, so an ordinary ratio Q_X(b)/P_X(b) is unavailable. Importance weighting cannot reconstruct target behavior on target-only support without extra structure.

## Adversarial robustness

Given perturbation sets Delta(x), define adversarial risk

\[
R_{\rm adv}(f)=\mathbb E_{(X,Y)\sim P}\left[\sup_{x'\in\Delta(X)}L(f(x'),Y)\right].
\]

This is a worst-case local objective, not the same object as ordinary deployment-law risk R_Q.

## Exact adversarial separation witness

Let X in {-1,+1}, Y=1[X=+1], and predictor f(-1)=0, f(+1)=1. Clean risk is zero. Declare

\[
\Delta(-1)=\Delta(+1)=\{-1,+1\}.
\]

For each clean point, the adversary may present the opposite input while the original label is retained. Then worst-case 0/1 loss equals one at both source points, so

\[
\boxed{R_{\rm adv}(f)=1}
\]

while

\[
\boxed{R_P(f)=0}.
\]

Average-case clean risk and adversarial risk are distinct.

## Robust optimization

A robust objective has the schematic form

\[
\min_\theta \mathbb E_P\left[\sup_{\delta\in\Delta(X)}L(f_\theta(X+\delta),Y)\right].
\]

Every claim must specify Delta, loss, and data law. No robustness claim is universal over unspecified perturbations.

## Structural sensitivity

Structural shift changes a declared component of the system or data-generating mechanism, such as graph/topology, routing/capacity rule, tokenizer, measurement process, intervention mechanism, or feature-generation mechanism. Changed output statistics may be evidence of changed behavior but do not identify which structural mechanism changed.

## Metric firewall

Keep separate population calibration, marginal conformal coverage, selective risk, ordinary predictive risk under P, ordinary predictive risk under Q, adversarial/worst-case risk, and structural sensitivity. No one is an automatic surrogate for another.

## Required non-implications

- shift detected does not imply task risk increased;
- P-calibration does not imply Q-calibration;
- P-coverage does not imply Q-coverage;
- low R_Q does not imply low adversarial risk;
- low adversarial risk for one perturbation set does not imply low adversarial risk for another;
- changed predictive statistics do not imply an identified structural cause.

## Reader outcomes

A reader should be able to name P and Q before changed-law claims; distinguish covariate and conditional shift; reproduce both finite shifted-law witnesses; state the importance-weight identity and support condition; distinguish deployment-law risk from adversarial risk; reproduce the adversarial separation; and keep calibration, coverage, selective risk, predictive risk, adversarial risk, and structural sensitivity separate.

## Required artifacts

Source lock; bibliography entries; specification; derivation packet; exact computational witness; reader manuscript; Chapter Ledger promotion; Source Register entry; transaction receipt; mandatory post-draft audit.

## References

- [@SugiyamaKrauledatMuller2007Covariate]
- [@MadryEtAl2018Adversarial]
