# AUDIT-038 — Governed Adaptation

## Disposition

**PASS AFTER THREE PRECISION REPAIRS**

ATLAS-CH-GOVADAPT-001 remains at draft-v0.1.

The implementation correctly separates execution, promotion, recovery, and certification authority; binds validation to exact revision identity; distinguishes stored rollback artifacts from governed recoverability; imports the Optionality correction-capacity object without collapsing it into action count; and preserves the safety-versus-liveness boundary.

AUDIT-038 found three in-scope defects:

1. the Corrigibility bibliography/source-lock author order did not match the primary-source ordering;
2. the finite witness wrote the inherited correction-capacity object on candidate labels A/B rather than on the post-revision operative states x_A/x_B required by the inherited Optionality type;
3. equal immediate utility was stated without explicitly binding both candidate gains to one common protected reference state.

All three defects were repaired on the audit branch.

No prerequisite edge, authority boundary, witness arithmetic, ledger status, source-register entry, or downstream dependency required reversal.

## Audited baseline

- implementation issue: #149;
- implementation PR: #150;
- implementation merge: `c0db4e60ba1fb9d3f2d7ac4469ca40bb5a761784`;
- audit issue: #151;
- chapter: `ATLAS-CH-GOVADAPT-001`.

Merged implementation artifact blobs:

- specification: `66d8d6f1070ae198038523f46b8a3fb278c1eb3d`;
- derivation packet: `f3f62873ff6aee7934274bcb1454111398ec116d`;
- computational witness: `cfa35c11b741c32b6a234e3f83d67ffbf513538d`;
- manuscript: `73b0c80d4da9faea7c55bfe19cbc02669746839a`;
- source lock: `0728797d97234b449b5880aa2f15e5e4f13a4cc3`;
- bibliography: `a72d8a776bde1e5a35dec92c5158acf494b71f1e`.

Repaired audit-head artifact blobs:

- specification: `76b00e42bc730fd6fd464d7d6a11286e79390483`;
- derivation packet: `4db7196e6489bd42c46e0e9d591658f6fb334442`;
- computational witness: `bb795024e92af0e6c992f1874ebaf2f35abe8fa2`;
- manuscript: `5d7d87a1918edebc2487359a5dfea15cfa157b47`;
- source lock: `a94b5addea0b2615df1bc7546d561c42d4734dff`;
- bibliography: `6eb9b6107c0c30f77729fb300310df36dafcebb6`;
- tranche receipt: `8b20210b7a2a3457bcd9bcfdbb3fe0e4c9503b41`;
- Chapter Ledger: `37ce6b27fc673d43f536e37d9292976e23b91996`;
- Source Register: `39d264abc643e162e35ba4bb9f283045aa5e597c`.

## 1. Hard prerequisites

PASS.

The source lock binds the exact audited prerequisites at protected baseline `ae2ce726fa4f24fc52289a1f2e6bbbaff9232d11`.

### Optionality and Correction Capacity

- manuscript blob: `a202d82ad9f2242fd17117cf6faa6eaa30227369`;
- AUDIT-034 blob: `43abd668155904debaf7687a05e93a0ea7d60fa5`;
- source-lock blob: `631afbcc9bfa1a2382ef109d701d523cafbbf0d1`.

### Research as a State Machine

- manuscript blob: `fca394ca7fe69561730ea5b13076974f22fe73e9`;
- AUDIT-035 blob: `8251b54ffb5644a41d7404d0e33e717f384d5c12`;
- source-lock blob: `c507c236fb8993b1e5e4df400c92ce490ff42dde`.

No downstream Frontier manuscript is used as hidden prerequisite authority.

## 2. External source scope

PASS AFTER BIBLIOGRAPHIC REPAIR.

The source lock uses:

- Soares, Fallenstein, Yudkowsky, and Armstrong (2015), *Corrigibility*;
- Orseau and Armstrong (2016), *Safely Interruptible Agents*;
- Hadfield-Menell, Dragan, Abbeel, and Russell (2017), *The Off-Switch Game*.

The implementation bibliography had the last two Corrigibility authors in the wrong order. The audit repair aligns the bibliography and source lock with the primary-source ordering.

External authority remains bounded to corrective-intervention/corrigibility, interruptibility in the cited RL setting, and off-switch incentive analysis.

The chapter does not infer a complete theory of alignment or a universal governance theorem from those sources.

## 3. Governed state

PASS.

The chapter uses:

[
g=(r,x,E,A,P,C,L)
]

for exact revision identity, operative state, evidence, authority relation, promotion state, certification state, and history.

Candidate revisions remain bound to an exact parent and exact candidate result identity.

## 4. Authority separation

PASS.

The chapter distinguishes proposal, execution, promotion, recovery, and certification authority.

No automatic implication among those authority relations is asserted.

In particular, successful execution does not imply promotion or certification.

## 5. Exact-target evidence

PASS.

For evidence object (e), the chapter uses exact target binding:

[
Binds(e,r)
iff
target(e)=r.
]

Evidence targeting revision (r_1) is not exact-target validation for materially changed revision (r_2).

The chapter therefore requires fresh replay after identity-changing repair.

## 6. Correction-capacity type

PASS AFTER REPAIR.

OPTIONALITY defines correction feasibility/capacity on states.

The implementation witness used shorthand such as:

[
CC_{h,0}(A;b).
]

That treated candidate labels as if they were the state argument of the inherited object.

The repaired artifacts explicitly define post-revision operative states (x_A) and (x_B), and use:

[
CC_{h,0}(x_A;b)=1,
qquad
CC_{h,0}(x_B;b)=1/2.
]

This restores the inherited type.

## 7. Common utility baseline

PASS AFTER REPAIR.

The implementation stated:

[
Delta U(A)=Delta U(B)=1
]

without explicitly naming the common reference.

The repaired formal packet and witness introduce protected reference state (x_0) and define:

[
Delta U(q)=U(x_q)-U(x_0).
]

Thus both candidate gains are measured against the same state.

## 8. Finite witness arithmetic

PASS.

Hidden future condition:

[
Theta={N,D},
qquad
b(N)=b(D)=1/2.
]

For (x_A):

[
C_{h,0}(x_A,N)=1,
qquad
C_{h,0}(x_A,D)=1.
]

Therefore:

[
CC_{h,0}(x_A;b)=1.
]

For (x_B):

[
C_{h,0}(x_B,N)=1,
qquad
C_{h,0}(x_B,D)=0.
]

Therefore:

[
CC_{h,0}(x_B;b)=1/2.
]

The immediate utility increments remain tied at 1 from the same protected reference state.

## 9. Utility-only versus correction-aware gate

PASS.

The utility threshold admits both candidates because their immediate increments tie.

A declared correction-capacity floor (kappa=1) admits (x_A) and rejects (x_B).

The chapter correctly limits this to the declared finite witness and does not promote (kappa=1) into a universal policy.

## 10. Rollback artifact versus recoverability

PASS.

The chapter distinguishes stored restoration material from existence of an authorized, bounded, target-reaching recovery path.

It explicitly notes that authority, external state, dependency compatibility, and horizon can block actual recovery even when old bytes exist.

## 11. Raw option labels versus functional correction paths

PASS.

The witness allows both candidate states to expose the same two command labels while only one has an authorized target-reaching recovery path.

Thus raw action count does not establish correction capacity.

This is consistent with the audited Optionality prerequisite.

## 12. Safety versus liveness

PASS.

The chapter gives a fail-closed execution that can preserve an invariant indefinitely while promoting nothing.

It therefore preserves:

[
	ext{safety}

otRightarrow
	ext{liveness}.
]

## 13. Governance conformance versus substantive correctness

PASS.

The manuscript explicitly confines process conformance to what the declared authority/evidence gate establishes.

It does not treat successful governance execution as proof of scientific truth, universal safety, or complete empirical correctness.

## 14. Governing-policy boundary

PASS.

Authority over operative state does not automatically include authority over the authority relation itself.

Policy change is treated as a distinct transition class governed by its own authority.

## 15. Repository integrity

PASS subject to audit-PR validation.

- Chapter Ledger keeps `ATLAS-CH-GOVADAPT-001` at `draft-v0.1`;
- Source Register contains `ATLAS-SRC-GOVADAPT-LOCK-001`;
- all declared bibliography keys resolve;
- manuscript contains the required epistemic marker, references section, and source-lock path;
- no governed figure is required.

## 16. Downstream handoff

PASS.

`ATLAS-CH-FRONTIER-001` may inherit:

- governed adaptation as a typed transition;
- authority separation;
- exact-target evidence rebinding;
- authorized recovery-path semantics;
- correction-capacity-aware admissibility;
- equal-immediate-value finite separation;
- safety/liveness separation.

FRONTIER must independently determine research-frontier priority.

## Final disposition

AUDIT-038 passes after three repairs.

The durable governed-adaptation layer is:

**exact revision identity + typed authority + exact-target evidence + authorized recovery paths + correction-capacity-aware admissibility + explicit safety/liveness separation, without promoting process conformance into substantive truth.**
