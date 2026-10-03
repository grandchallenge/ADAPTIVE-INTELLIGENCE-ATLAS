# ATLAS-CH-EVIDENCE-001 — Documentary Reconstruction

## Purpose

This packet records the exact project-local objects from which the chapter Claims, Evidence, and Computational Witnesses is reconstructed.

It is a documentary derivation, not an external theorem about scientific epistemology.

## 1. Canonical vocabulary

The baseline object governance/EPISTEMIC_STATUS.yaml defines eleven reader-facing classes:

1. Definition.
2. Established Result.
3. Atlas Derivation.
4. Computational Witness.
5. Observation.
6. Interpretation.
7. GCL Public Project Evidence.
8. GCL Programme.
9. Conjecture.
10. Open Problem.
11. Institutional Status.

The source also supplies a promotion rule for each class.

Consequently, the chapter may explain and compose these classes, but it may not replace them with a new ungoverned taxonomy.

## 2. Claim-support packet

The chapter introduces the Atlas documentary object

K = (q, τ, S, Ω, N, D).

This object is a synthesis of fields already demanded separately by the source-lock, witness, composition, and epistemic standards.

q — claim identity:
The composition protocol and source-lock standard require load-bearing claims to be identifiable rather than inferred from presentation.

τ — epistemic class:
EPISTEMIC_STATUS.yaml provides the canonical label and promotion rule.

S — support route:
The composition protocol recognizes derivation, source-locked result, proof object, exact reconstruction, computational witness, empirical observation, and project evidence as distinct routes.

Ω — scope:
The epistemic and witness standards require preservation of hypotheses, run, environment, dataset, domain, numerical convention, or version where material.

N — non-entailments:
The witness and source-lock standards explicitly prohibit several silent promotions. Recording these as a field makes the boundary reader-visible rather than implicit.

D — downstream permission:
The dependency graph and ledger define what later chapters may assume from a hard prerequisite.

The six-field packet therefore packages existing doctrine into one reader-facing object. It does not create a new external evidentiary standard.

## 3. Documentary support is not logical entailment

The chapter writes

S ↝[Ω, τ] q

for support.

This symbol is intentionally weaker and more general than a proof relation.

Examples:

- a source-locked theorem can justify a theorem statement only with its hypotheses preserved;
- a computational witness can establish an exact finite result without proving a universal generalization;
- an empirical run can establish what was observed under that run without proving a universal mechanism;
- a governance record can establish review state without establishing mathematical truth.

Therefore the Atlas must name a proof, derivation, witness, observation, interpretation, or institutional record according to the role it actually plays.

## 4. No scalar evidence ladder

The eleven epistemic classes are not ordered by one scalar strength.

Reason:

- Definition creates terminology rather than evidentiary support.
- Open Problem records unresolved status rather than weak evidence.
- Institutional Status records authority state rather than mathematical truth.
- Interpretation is a relation to underlying evidence rather than a substitute for it.
- GCL Programme records research context rather than a lower-confidence implementation claim.
- Computational Witness and Observation answer different questions from Established Result.

Thus a single ranking would collapse distinct semantic axes.

The manuscript may discuss stronger or weaker support for a particular claim, but it must not present the canonical classes themselves as a universal total order.

## 5. Promotion rule

A promotion changes the claim-support packet in a way that strengthens what the reader may infer.

Presentation changes alone do not supply that support.

Examples of nonpromotion:

- adding a polished figure does not turn an observation into a theorem;
- rerunning exact code does not turn a finite check into a continuum proof;
- merging a pull request does not turn programme context into public scientific validation;
- review or audit does not erase the original scope and hypotheses;
- a precise citation does not grant the cited object authority outside its domain.

A legitimate promotion requires support appropriate to the stronger claim and must update the recorded class and scope.

## 6. Counterexample matrix

### Exact computation versus theorem

Finite enumeration over n in [-10,10] may prove the finite enumerated proposition. It does not by itself prove the corresponding proposition for every integer.

### Repeatable observation versus mechanism

Repeatedly observing a behavior in one experimental family can establish repeated observation within that family. It does not alone identify the causal mechanism or prevalence outside the tested scope.

### Narrow proof versus broad prose

A correct proof of statement A does not establish prose statement B when B contains an unstated stronger quantifier, domain, or assumption.

### Precise identity versus adequate authority

A perfectly pinned source can still be the wrong authority for a claim. Identity answers which object was consumed; authority answers what that object can support.

### Institutional state versus truth

Green CI, successful replay, audit PASS, merge, acceptance, or certification are institutional or procedural facts. Their mathematical meaning is limited to the exact authority and checks recorded.

## 7. Computational witness role

The exact finite witness in ATLAS-CW-EVIDENCE-001 is deliberately elementary.

Its value is semantic rather than mathematical novelty.

It places the following two statements side by side:

A. For each integer n from -10 through 10, n(n-1) is even.
B. For every integer n, n(n-1) is even.

Exact enumeration is sufficient for A because A has a finite declared domain.

B requires a general argument. The elementary proof uses the fact that consecutive integers have opposite parity.

The same computed values may illustrate B, but they do not prove B.

## 8. Dependency handoff

The chapter's direct consumers are recorded in the Atlas architecture:

- Data Quality, Mixtures, and Contamination;
- Mechanistic Diagnostics;
- Evidence Extraction and Claim Discipline;
- Experiments as Arguments.

Those chapters may inherit:

- the canonical epistemic labels;
- the claim-support packet;
- the documentary support arrow;
- the nonpromotion rules;
- the distinction between exact public evidence and programme context;
- the distinction between institutional status and mathematical truth.

They must supply their own domain-specific evidence.

## 9. Source identity summary

All source identities and authority scopes are fixed in:

sources/source-locks/ATLAS-CH-EVIDENCE-001.yaml

The lock pins the baseline commit and exact Git blob SHA-1 for every load-bearing project-internal source used by this chapter.

## Claim boundary

This packet establishes faithful reconstruction of the Atlas evidence grammar at the pinned baseline.

It does not establish that the grammar is complete, uniquely correct, or universally optimal for science or mathematics.
