# AUDIT-014 — Claims, Evidence, and Computational Witnesses

## Disposition

**PASS WITH ONE DOCUMENTARY REPAIR**

ATLAS-CH-EVIDENCE-001 remains at draft-v0.1.

The chapter faithfully reconstructs the Atlas project-local evidence grammar from exact baseline objects and keeps claim, support, interpretation, and institutional status separate.

The audit made one bounded repair: direct downstream consumers were named by chapter title in the documentary reconstruction. Their stable ATLAS-CH-* identities are now explicit in both the reconstruction packet and reader-facing handoff. The manuscript also states explicitly that the canonical epistemic classes do not form a scalar ladder.

No mathematical claim or source-lock identity required repair.

## Audited baseline

- EVIDENCE-001 merge:
  95f71ecc4baafba19bad76fd8d67f7b5efbe4ebe;
- source-lock baseline:
  a3361157cd98647ab3450a2a9786242af9930291;
- audit issue:
  #70;
- chapter:
  ATLAS-CH-EVIDENCE-001.

## 1. Exact documentary pins

PASS.

Every source-lock Git blob was independently re-fetched from the pinned baseline.

Matches:

- governance/EPISTEMIC_STATUS.yaml:
  c64f7376bf21447d73c277ba3758be7490bcdaf8;
- governance/CHAPTER_COMPOSITION_PROTOCOL.md:
  52f1d77e80e516cea179550f966383b0b06900af;
- governance/COMPUTATIONAL_WITNESS_STANDARD.md:
  1d9c71c5e720ebe421ebb4943f97541635a4bd76;
- governance/SOURCE_LOCK_STANDARD.md:
  df1384f164133a58d430af9934b1609ea2dbc857;
- governance/ATLAS_EDITORIAL_PROFILE.md:
  4e54b0bebd39dd4432e7caf8238456dac8b9cebf;
- governance/CHAPTER_LEDGER.yaml:
  1b4320b3ecc44d2120753d583b8f12cfee3a610b;
- governance/ATLAS_MAP.md:
  03b9475696f3f3b75806b3ebe44dd84780f01439;
- audited MAP prerequisite manuscript:
  c14d9f1e4e9a105a5cf2c5083f8b8ca83182a43b;
- reviews/AUDIT-013.md:
  a5db63d67b64bdea18d538253d900aecc67e8d1c.

The source lock contains all nine identities and scoped authority statements.

## 2. Canonical epistemic vocabulary

PASS.

The manuscript includes all eleven canonical reader-facing classes:

1. Definition;
2. Established Result;
3. Atlas Derivation;
4. Computational Witness;
5. Observation;
6. Interpretation;
7. GCL Public Project Evidence;
8. GCL Programme;
9. Conjecture;
10. Open Problem;
11. Institutional Status.

No replacement taxonomy is introduced.

## 3. Claim-support packet

PASS.

The chapter defines:

K = (q, τ, S, Ω, N, D),

with explicit fields for claim identity, epistemic class, support route, scope, non-entailments, and downstream permission.

The packet is correctly presented as an Atlas documentary synthesis rather than a universal external standard.

## 4. Support versus entailment

PASS.

The notation S ↝[Ω, τ] q is explicitly described as documentary support and explicitly denied the semantics of logical entailment.

Proof, finite computation, observation, project evidence, and institutional record remain different support roles.

## 5. No scalar evidence ladder

PASS.

The manuscript explains why Definition, Open Problem, Interpretation, Programme context, Computational Witness, Observation, and Institutional Status do not form weaker or stronger versions of one proposition.

The audit added the explicit sentence:

The classes do not form a scalar ladder.

This prevents a hierarchy graphic or later summary from silently changing the taxonomy into a confidence score.

## 6. Computational witness

PASS.

ATLAS-CW-EVIDENCE-001 uses exact integer arithmetic on all 21 integers from -10 through 10.

Its expected replay output is:

count=21
all_even=True

The witness establishes only the finite enumerated proposition.

The universal statement that n(n-1) is even for every integer n is established separately from the parity of consecutive integers.

Thus:

exact finite verification ≠ universal proof.

## 7. Observation versus interpretation

PASS.

The manuscript treats observation as scoped record and interpretation as a reasoned reading that remains separable from the evidence.

It explicitly warns that multiple mechanisms may produce the same observable.

## 8. Public evidence versus programme context

PASS.

Exact public GCL project evidence requires an inspectable identity and may assert only what that object supports.

Programme context can motivate research without being promoted into a public implementation or completed-result claim.

## 9. Source identity versus source authority

PASS.

The chapter preserves the canonical source-lock distinction:

identity answers which object was consumed;

authority answers what that object is allowed to support.

A precisely pinned but inappropriate source is not treated as adequate evidence.

## 10. Institutional status versus mathematical truth

PASS.

CI, replay, review, audit, merge, adjudication, acceptance, and certification are described as procedural or institutional facts whose force is bounded by their exact authority and checks.

No generic truth operator is inferred from process state.

## 11. Downstream handoff

PASS AFTER DOCUMENTARY REPAIR.

The four direct consumers are now named by stable identity:

- ATLAS-CH-DATA-001;
- ATLAS-CH-MECHDIAG-001;
- ATLAS-CH-EVIDEX-001;
- ATLAS-CH-EXPERIMENT-001.

They inherit the evidence grammar, not domain evidence they have not produced.

## 12. Dependency direction

PASS.

No downstream chapter is used as prerequisite authority.

The hard prerequisite remains audited ATLAS-CH-MAP-001.

## 13. Integrity

PASS.

The manuscript, documentary packet, and computational witness contain no hidden C0 control characters or tabs.

The Chapter Ledger records ATLAS-CH-EVIDENCE-001 at draft-v0.1.

The Source Register contains ATLAS-SRC-EVIDENCE-LOCK-001.

The witness contains an explicit Claim boundary.

No governed figure is registered, consistent with the tranche decision that a hierarchy graphic would be semantically misleading.

## 14. Final disposition

AUDIT-014 passes with the stable-identity documentary repair described above.

The Orientation layer now supplies both:

- a reading contract from ATLAS-CH-MAP-001; and
- an evidence contract from ATLAS-CH-EVIDENCE-001.

Downstream chapters may now state not merely what they claim, but what kind of support is carrying each claim and where that support stops.
