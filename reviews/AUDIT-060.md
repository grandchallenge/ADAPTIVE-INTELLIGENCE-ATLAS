# AUDIT-060 — Coupling-Phase Spectroscopy

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-CPS-001 remains at draft-v0.1.

The audit found no mathematical, dependency, source-scope, provenance, witness, protocol, citation, or repository defect requiring repair.

The current project-level scientific boundary remains:

\[
\boxed{
\text{one confirmed GSD behavioural transition}
+
\text{CPS optimizer-state lane artifact-blocked}
}
\]

with no public GSD CPS signal disposition authorized.

## Audited implementation

- implementation issue: #239
- implementation PR: #240
- exact validated implementation head: c2a6330cdc68d741ccc7c12477113e253d13a90d
- implementation GitHub Actions run: 37533936696
- implementation merge / audited protected baseline: 7ca2ee93f1f2bc60ffadc696f2893ac0c29fed4c
- audit issue: #241
- audit branch: audit/a241
- chapter: ATLAS-CH-CPS-001

Protected implementation artifact identities:

- specification: 05d1d186cce4f911790f8cd0a9bb25556bc56484
- derivation packet: 1ced647197f9af6567736e5edbccfefd7f200d5e
- computational witness: aafd136691e45b675ea05dc268f15f86302ba625
- reader manuscript: c07337d1bdf013ad5ac5a2caa69c4efbb45eea50
- source lock: 372dd928a77cf30e2e9b903239e4a49a5d479b79
- Chapter Ledger: dcc92835850f1f4fd33ba598e94097c6be55dc1a
- Source Register: 546eba7a627a71af4d27430e16c379457aa15ead
- transaction receipt: be766d28d50a22036a2f9ed780f60811b34d116b

## 1. Hard prerequisite identity

PASS.

OPTDYN-001 is bound exactly:

- manuscript: 59b03c10b7f4b917cc8a0cb4d6893e12c1993c8c;
- source lock: 0b0cb1dd109a7708bd2a5238116bd225c69fb185;
- AUDIT-002: 4671995f0cd7465a5df2bb60431244f482e5e3c9.

The chapter inherits augmented-state, local-Jacobian, non-normal transient, and time-varying-product mathematics from this audited prerequisite.

No downstream chapter is used as hidden mathematical authority.

## 2. October 6 public GCL refresh

PASS.

The source lock does not repeat the October 2 OPTDYN source-gap statement as current fact.

It records a fresh October 6 organization search and binds current public GSD state at:

grandchallenge/GSD@ebd4681e1815a3d7f0285cc4ce2bc090b38fae8c.

The exact project files are:

- research programme: 6a898efbdbe23eb6e947cd1c12f4a4b8fcee631f;
- work-package index: c7af5b65f6496ff4a3c8533f4bb6ee8721467385;
- campaign state: bc5ef87989fbeb094b0ffe5b348d06fe409397dc;
- WP03R transition receipt: 01acb64e536f13bd689d20a74608a7170900d0e3;
- WP04 artifact receipt: 9e999395fd14d1e8ac1b0ea5a209a1da66abab06.

These identities match the transaction receipt.

## 3. GSD behavioural-transition scope

PASS.

The bound WP03R receipt establishes one robust OLMo2-1B behavioural transition for truthy_answer/surprising_truth under the frozen GSD protocol.

The transition is localized between steps 2000 and 3000, with step 2000 GENERALIZING and steps 3000/4000 PATTERN_MATCHING.

The source explicitly blocks promotion to:

- optimizer cause;
- mechanism identity/change;
- persistence state;
- capacity-allocation explanation;
- architecture-level conclusion.

The CPS chapter preserves all of those firewalls.

## 4. GSD-WP04 scope

PASS.

The GSD research programme defines WP04 as CPS transition-local dynamics.

Its question is whether optimizer-state structure predicts or explains confirmed transitions.

Its declared scientific exit grammar is:

- PREDICTIVE_SIGNAL;
- DESCRIPTIVE_ONLY;
- NO_SIGNAL.

The Atlas chapter accurately imports that grammar without claiming any of those outcomes has been reached.

## 5. Artifact-block disposition

PASS.

The bound WP04 artifact receipt records exact public revisions:

- stage1-step2000-tokens5B;
- stage1-step3000-tokens7B;
- stage1-step4000-tokens9B.

It records that those revisions expose model/config/tokenizer artifacts but not:

- optimizer state;
- trainer state;
- scheduler state;
- gradient artifact;
- update-direction artifact.

The receipt explicitly says:

BLOCKED_EXTERNAL_ARTIFACT_ABSENT

and explicitly distinguishes this from a negative CPS result.

The chapter preserves that distinction exactly.

## 6. No false signal disposition

PASS.

The chapter does not infer:

\[
\mathrm{PREDICTIVE\_SIGNAL},
\]

\[
\mathrm{DESCRIPTIVE\_ONLY},
\]

or:

\[
\mathrm{NO\_SIGNAL}
\]

from the blocked GSD lane.

The current project-level disposition remains an evidence-availability block.

## 7. Momentum Jacobian family

PASS.

With:

\[
\eta=\frac1{10},
\qquad
\beta=\frac9{10},
\]

the inherited momentum Jacobian is correctly specialized to:

\[
J(h)
=
\begin{pmatrix}
1-\frac h{10}&-\frac9{100}\\
h&\frac9{10}
\end{pmatrix}.
\]

No parameterization mismatch with OPTDYN-001 was found.

## 8. Determinant identity

PASS.

Direct expansion gives:

\[
\det J(h)
=
\left(1-\frac h{10}\right)\frac9{10}
+
\frac{9h}{100}
=
\frac9{10}.
\]

Therefore:

\[
\boxed{\det J(h)=9/10}
\]

for the entire declared toy family.

## 9. Trace and coupling coordinate

PASS.

\[
\operatorname{tr}J(h)
=
\frac{19}{10}-\frac h{10}.
\]

The chapter defines:

\[
\kappa(J)
=
1+\det J-\operatorname{tr}J.
\]

Therefore:

\[
\kappa(J(h))
=
1+\frac9{10}
-
\left(
\frac{19}{10}-\frac h{10}
\right)
=
\boxed{\frac h{10}}.
\]

The chapter explicitly states that \(\kappa\) is a toy matrix-derived coordinate, not a universal CPS diagnostic.

## 10. Discovery windows

PASS.

The two discovery windows are:

\[
h=2,\quad \kappa=1/5,\quad Y=0,
\]

and:

\[
h=8,\quad \kappa=4/5,\quad Y=1.
\]

The frozen threshold:

\[
\tau=1/2
\]

lies strictly between the two discovery scores.

No heldout label is required to choose it.

## 11. Heldout toy prediction

PASS.

Heldout windows are:

\[
h=3,\quad \kappa=3/10,\quad Y=0,
\]

and:

\[
h=7,\quad \kappa=7/10,\quad Y=1.
\]

The frozen predictor:

\[
\widehat Y
=
\mathbf 1\{\kappa>1/2\}
\]

returns exactly:

\[
(0,1).
\]

This is correctly scoped as a synthetic protocol witness only.

## 12. Discriminants

PASS.

The exact characteristic discriminants are:

\[
\Delta_2=-71/100,
\]

\[
\Delta_3=-26/25,
\]

\[
\Delta_7=-54/25,
\]

\[
\Delta_8=-239/100.
\]

All are negative.

Independent exact replay agrees.

## 13. Equal spectral-radius control

PASS.

All four matrices have:

\[
\det J=9/10
\]

and complex-conjugate eigenvalues.

Therefore:

\[
|\lambda|^2=9/10
\]

for each conjugate pair, giving:

\[
\boxed{
\rho(J(2))
=
\rho(J(3))
=
\rho(J(7))
=
\rho(J(8))
=
\sqrt{9/10}.
}
\]

Thus spectral radius is identical across all four toy windows.

The chapter correctly uses this only to show that spectral radius alone cannot implement the toy classifier.

## 14. Same spectral radius boundary

PASS.

The chapter does not infer equivalent dynamics from equal spectral radius.

It explicitly notes that the matrices differ in trace, coupling coordinate, and directional action.

This is consistent with the audited OPTDYN/non-normality substrate.

## 15. Discovery/freeze/heldout protocol

PASS.

The chapter requires:

1. behavioral target lock independently of CPS;
2. discovery-only probe/layer/horizon/lead/threshold selection;
3. complete probe freeze;
4. pre-transition feature computation using only information available at or before checkpoint \(t\);
5. heldout transition evaluation;
6. declared controls.

This blocks post hoc selection from being relabeled as prediction.

## 16. Retrospective versus predictive evidence

PASS.

The chapter correctly distinguishes:

\[
\text{retrospective alignment}
\]

from:

\[
\text{heldout prediction}.
\]

Retrospective best-layer or best-statistic selection is restricted to DESCRIPTIVE_ONLY unless a new frozen heldout test succeeds.

## 17. Predictive versus causal evidence

PASS.

The chapter explicitly rejects:

\[
\text{heldout prediction}
\Rightarrow
\text{causal optimizer-state mechanism}.
\]

Causal promotion requires a controlled optimizer-state/update intervention or another declared causal design.

No current GSD source is promoted past its supported evidence level.

## 18. Evidence ladder

PASS.

The chapter separates:

- C0 behavioral transition;
- C1 local diagnostic movement;
- C2 heldout prediction;
- C3 intervention sensitivity;
- C4 mechanism-specific support.

The ladder is epistemic organization, not a claim that every CPS programme will reach every level.

## 19. Artifact completeness

PASS.

The chapter requires exact identity for the state required by the chosen probe.

It does not silently substitute a weaker statistic when optimizer artifacts are absent.

This is consistent with the current WP04 block.

## 20. One-transition boundary

PASS.

The chapter explicitly states that one confirmed transition cannot establish a general heldout predictor.

It may support:

- artifact-readiness work;
- a descriptive case study if artifacts become available.

General prediction requires separate discovery and heldout transition windows.

## 21. Scale boundary

PASS.

The public confirmed transition is OLMo2 1B.

The manuscript does not promote a future 1B CPS result to:

- OLMo3 7B;
- OLMo3 32B;
- other model families;
- other optimizers;
- downstream post-training transfer.

Scale transfer requires independent evidence.

## 22. Transaction-receipt provenance

PASS.

Every implementation artifact identity in governance/tranches/CPS-001.md matches the exact protected implementation merge.

Every bound GSD project-source blob also matches the source lock.

No provenance repair is required.

## 23. Repository integrity

PASS subject to audit-PR validation.

At the audited implementation merge:

- CPS status is draft-v0.1;
- canonical specification/manuscript/derivation/source-lock/witness paths are populated;
- the hard dependency remains OPTDYN-001 only;
- the CPS source lock is registered;
- no governed figure is introduced;
- no new bibliography key is required;
- implementation exact head passed GitHub Actions run 37533936696;
- protected implementation merge passed canonical repository validation.

## Final disposition

AUDIT-060 passes with no repair.

The durable CPS boundary is:

**a confirmed behavioural transition can motivate optimizer-state spectroscopy, but descriptive alignment, heldout prediction, causal mechanism evidence, and artifact availability remain separate evidentiary objects. Current public GSD-WP04 is artifact-blocked, not scientifically negative.**
