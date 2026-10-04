# AUDIT-035 — Research as a State Machine

## Disposition

**PASS AFTER THREE COMPLETENESS REPAIRS**

ATLAS-CH-RESEARCHSM-001 remains at `draft-v0.1`.

The implementation baseline had the correct prerequisite/source lock, bounded-work-package object, research-state product, duplicate relation, and canonical-idempotence core. However, its manuscript and finite witness stopped before several obligations required by the chapter's own specification.

AUDIT-035 repaired three in-scope completeness defects:

1. the manuscript stopped immediately after the duplicate/retry witness and omitted guarded advancement, actor-separation boundaries, certification, safety-versus-liveness, typed recovery, public GCL lifecycle mapping, failure modes, and the GOVADAPT handoff;
2. the computational witness covered only evidence-set cardinality and omitted the required five-factor advancement gate, exact repeated advancement effect, same-actor separation counterexample, and safety-without-liveness execution;
3. the derivation packet stopped at basic safety invariants and omitted explicit advancement state, certification guard, receipt/promotion separation, liveness counterexample, recovery classes, and the pinned public workflow mapping.

The repaired chapter now satisfies its declared specification without changing prerequisite identities or public-source authority boundaries.

## Audited baseline

- implementation merge:
  `a796eb3ae822c3bf998b27de94db7213646d2c59`;
- implementation PR:
  #137;
- audit issue:
  #138;
- chapter:
  `ATLAS-CH-RESEARCHSM-001`.

## 1. Hard prerequisites

PASS.

### Replayable Evidence Objects

- manuscript blob:
  `4d95568d12ec0b27bcace910d8573f4a22e8b161`;
- AUDIT-003 blob:
  `9723fcb3dfa0111829b98f1c9bb416a13dbd714e`;
- source-lock blob:
  `b373efe80e4ced13c7e060e5036d0012d2e17686`.

### Formal Methods and Machine-Checkable Claims

- manuscript blob:
  `c3e8933a773e0f34a6d38ab23a056fd84408ccbf`;
- AUDIT-025 blob:
  `3250d8411cfeeec470e4124d8022303f30aaf1f5`;
- source-lock blob:
  `74d3bf0420152d5a9e4a3545974ee2f448cb5481`.

No Governed Adaptation chapter is used as hidden prerequisite authority.

## 2. Public GCL case-study evidence

PASS.

The source lock binds exactly to `grandchallenge/MATH-PROGRAMME@fdd7a3fe3df7b2d699753347080c1cbc2127e02d`.

Verified public blobs:

- lifecycle controller:
  `91dca167b4b9c2dd15be41fb1996211752120f27`;
- Frontier Advancement Gate:
  `4145981b5ba85527c49b83a3440b0632db9924ca`;
- Controlled Epistemic Interface:
  `33164987c3f5484863ab31606034060e72b7148a`.

The chapter uses these as concrete operational examples, not universal workflow laws.

## 3. Bounded work package

PASS.

The chapter defines:

`W=(id,Q,B,S,D,R,A,Z)`

for stable identity, bounded question, bootstrap facts, allowed sources, required deliverables, durable return route, granted authority, and stop/non-authority conditions.

This is correctly presented as an Atlas research-state object rather than an externally established universal schema.

## 4. Product research state

PASS.

The chapter uses:

`x=(q,E,U,J,P,C,L)`

for execution phase, immutable evidence identities, replay/check state, adjudication, programme disposition, certification, and append-only history.

Programme disposition and certification are deliberately separate coordinates.

## 5. Canonical state versus history

PASS.

The canonical projection omits retry-log multiplicity while history remains append-only.

For stable event key `k`:

`Canon(F_k(F_k(x)))=Canon(F_k(x))`.

The chapter correctly scopes idempotence to canonical effect rather than requiring identical history.

## 6. Duplicate versus conflict

PASS.

Return identity is:

`r=(d,h)`

for dispatch identity `d` and immutable result identity `h`.

Exact duplicates require both coordinates to match.

Thus:

- `(17,A)` repeated is an exact retry;
- `(17,B)` with `B!=A` is distinct evidence, not a duplicate.

The chapter correctly preserves both identities before adjudicating their semantic relation.

## 7. Exact evidence-set witness

PASS.

Starting from empty evidence:

`E_1={(17,A)}`

has cardinality 1.

Exact retry gives:

`E_2=E_1 union {(17,A)}=E_1`.

So:

`|E_2|=1`.

Adding distinct result:

`(17,B)`

gives cardinality 2.

## 8. Advancement guard

PASS AFTER REPAIR.

The repaired chapter defines the finite witness:

`G_adv(e)=I(e)S(e)R(e)A(e)D(e)`

for identity/provenance, structure, required replay/check, supporting adjudication, and explicit programme disposition.

This is explicitly scoped as one strict finite model rather than a universal research-governance formula.

## 9. Exact advancement vectors

PASS AFTER REPAIR.

The finite witness now includes:

`(1,1,1,1,0) -> 0`;

`(1,1,1,1,1) -> 1`;

`(1,1,0,1,1) -> 0`.

Thus a missing programme disposition or required check keeps the declared transition closed.

## 10. Idempotent advancement

PASS AFTER REPAIR.

Let `K_adv` be the canonical set of identities receiving the declared advancement effect.

Then:

`(K_adv union {m}) union {m}=K_adv union {m}`.

Repeated exact advancement therefore has one canonical set-insertion effect while history may record repeated attempts.

## 11. Actor-separation boundary

PASS AFTER REPAIR.

For a policy that requires producer/reviewer identity separation:

`Sep(a_prod,a_rev)=1{a_prod!=a_rev}`.

Therefore:

`Sep(A,A)=0`;

`Sep(A,B)=1`.

The chapter correctly states that distinct actor identities prove only identity separation, not statistical, epistemic, cryptographic, organizational, or causal independence.

## 12. Certification separation

PASS AFTER REPAIR.

Certification remains coordinate `C`.

A schematic certification guard binds:

- exact target identity/revision;
- required support state;
- authority/policy predicate.

A positive programme disposition does not itself set certification state.

## 13. Exact-target discipline

PASS.

The manuscript explicitly rejects stale evidence transfer from one load-bearing revision to a changed revision.

Review, replay, adjudication, and certification must remain bound to the exact object they support.

## 14. Receipt versus claim status

PASS.

The chapter explicitly permits receipt/capture to change execution/evidence/history while leaving programme disposition unchanged.

Thus receipt is not promotion.

## 15. Frontier-advancement authority

PASS.

The pinned Frontier Advancement Gate states that contributor-supplied next residuals are evidence, not scheduling authority.

The chapter maps this to the separate programme-disposition factor `D(e)`.

## 16. Controlled independent-intelligence intake

PASS.

The pinned interface supports the operational sequence:

`dispatch -> bounded contribution -> immutable intake -> separate adjudication -> protected route`.

The manuscript retains the source's boundary:

`receive != believe != admit != certify`.

It does not promote zero-context work into a claim of statistical or epistemic independence.

## 17. Forge/Solve/Cert boundary

PASS.

The public controller records the authority boundary:

`MATHFORGE_TO_MATHSOLVE_TO_MATHCERT`.

The chapter uses it as a concrete compartmentalization example.

It does not claim the three-part split is universally optimal or that Solve adjudication is MATHCERT certification.

## 18. Fail-closed mutation

PASS AFTER REPAIR.

When a required transition guard is false, the protected canonical mutation does not occur.

The chapter correctly allows diagnostics, failure receipts, candidate preservation, and permitted repair actions to proceed separately.

Fail-closed promotion is therefore not confused with operational paralysis.

## 19. Safety versus liveness

PASS AFTER REPAIR.

The repaired witness includes a blocked adjudicated state where all safety invariants remain preserved while `D(e)=0` forever and only idempotent retries occur.

The eventual-advancement property is false on that execution.

Therefore:

> safety does not imply liveness.

A separate progress assumption or enabled authority transition is required.

## 20. Recovery classes

PASS AFTER REPAIR.

The final chapter distinguishes:

- exact retry;
- new evidence;
- explicit supersession;
- implementation/tooling repair;
- authorized policy change.

These are not collapsed into one generic retry operation.

## 21. Tooling failure versus scientific failure

PASS.

The manuscript distinguishes CI/rate-limit/parser/connector failures from mathematical refutation.

Infrastructure failure does not silently become epistemic judgment.

## 22. Repair and replay

PASS.

The chapter states that a changed implementation must not inherit stale execution evidence merely by relabeling it.

Where the governing process requires replay, the repaired exact object must be freshly re-evaluated.

## 23. Workflow conformance versus scientific truth

PASS.

The chapter explicitly denies that a valid lifecycle proves:

- mathematical truth;
- novelty;
- completeness of review;
- correctness of omitted premises;
- adequacy of governance.

This preserves the Formal Methods model boundary.

## 24. Integrity

PASS subject to audit-PR validation.

The Chapter Ledger records RESEARCHSM-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-RESEARCHSM-LOCK-001`.

The computational witness is bound at:

`mathematics/computational-witnesses/ATLAS-CW-RESEARCHSM-001.md`.

The manuscript has the required epistemic marker, references section, and source-lock path.

No unresolved bibliography citation keys are present.

No governed figure is required.

## 25. Downstream handoff

PASS AFTER REPAIR.

GOVADAPT-001 may inherit:

- bounded work packages;
- typed product research state;
- canonical/history separation;
- exact-identity idempotence;
- duplicate/conflict distinction;
- guarded promotion;
- separate certification;
- actor-separation predicates;
- safety/liveness separation;
- typed recovery;
- exact-target evidence binding.

It must independently define self-modification/adaptation authority and correction-capacity preservation.

## 26. Final disposition

AUDIT-035 passes after the three completeness repairs above.

The durable research-state layer is:

**bounded work identity + immutable evidence + guarded typed transitions + exact-target authority + canonical idempotence + append-only history + separate adjudication/promotion/certification, with fail-closed safety kept distinct from eventual progress.**
