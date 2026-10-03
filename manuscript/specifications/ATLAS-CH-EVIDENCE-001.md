# Chapter Specification — ATLAS-CH-EVIDENCE-001

## Identity

**Title:** Claims, Evidence, and Computational Witnesses  
**Part:** Orientation  
**Status:** specification-ready.  
**Epistemic class:** Atlas documentary synthesis.

## Chapter contract

Give the Atlas a precise grammar for saying what is claimed, what supports the claim, what scope binds that support, and what stronger conclusion the support does not license.

The chapter must preserve the canonical Atlas epistemic vocabulary while making its internal logic visible to a reader.

It is not a universal theory of scientific knowledge. It is the evidence contract used by this monograph.

## Dependency contract

Hard prerequisite:

- ATLAS-CH-MAP-001 — How to Read a Mathematical Atlas.

Exact project-internal sources are bound in:

sources/source-locks/ATLAS-CH-EVIDENCE-001.yaml

No downstream chapter may be used as prerequisite authority.

## Reader outcome

A reader should be able to:

1. distinguish the exact wording of a claim from the object used to support it;
2. distinguish definition, established result, Atlas derivation, computational witness, observation, interpretation, public project evidence, programme context, conjecture, open problem, and institutional status;
3. state the scope and hypotheses under which a support route is relevant;
4. explain why evidence support is not automatically logical entailment;
5. explain why the Atlas classes are not a one-dimensional ranking from weak to strong;
6. state what a computational witness establishes and what it does not;
7. distinguish observation from a causal or mechanistic interpretation;
8. distinguish exact public project evidence from remembered programme context;
9. recognize promotion errors caused by prose, figures, CI, review, or repetition;
10. identify what a downstream chapter is entitled to assume.

## Formal documentary object

Use the claim-support packet

K = (q, τ, S, Ω, N, D)

where:

- q is the exact claim;
- τ is the declared Atlas epistemic class;
- S is the set of support objects or support routes;
- Ω is the scope, hypotheses, domain, run, dataset, or version boundary;
- N is the explicit set of stronger conclusions not licensed;
- D is the downstream permission: what later chapters may consume without silently strengthening q.

Use the notation

S ↝[Ω, τ] q

for documentary support.

This arrow is deliberately not logical entailment. When a proof relation exists, it must be named separately.

## Central distinction

The chapter must make the following separation durable:

claim ≠ evidence ≠ interpretation ≠ institutional status.

A single source object may support several differently scoped claims. A single claim may require several support routes. Neither fact implies that evidence classes admit a total order.

## Canonical epistemic vocabulary

Explain all reader-facing classes in governance/EPISTEMIC_STATUS.yaml:

- Definition;
- Established Result;
- Atlas Derivation;
- Computational Witness;
- Observation;
- Interpretation;
- GCL Public Project Evidence;
- GCL Programme;
- Conjecture;
- Open Problem;
- Institutional Status.

Do not invent a replacement taxonomy.

## Computational witness

Include one small exact finite witness contrasting a bounded computational statement with a universal theorem.

Preferred example:

- enumerate integers n from -10 through 10;
- verify exactly that n(n-1) is even for those 21 values;
- state that the finite witness proves only the finite enumerated claim;
- give the separate elementary proof of the universal statement for all integers.

This example is pedagogical. It is not offered as a new mathematical result.

## Required counterexamples and failure boundaries

Include at least:

1. exact finite computation improperly promoted to an infinite theorem;
2. repeatable observation improperly promoted to a universal mechanism;
3. proof of a narrower formal statement improperly promoted to a broader prose claim;
4. precise source identity with insufficient authority for the claim;
5. successful CI, audit, review, or institutional acceptance improperly promoted to mathematical truth.

Also state:

- a definition may be useful without asserting external existence;
- a conjecture may be precise without being established;
- an open problem may have a proposed route without having a solution.

## Figure decision

No governed figure is required for v0.1.

The claim-support packet, epistemic table, and counterexample table are the core visual structures. A decorative hierarchy would be actively misleading because the epistemic classes are not a scalar ladder.

## Documentary packet

Create:

mathematics/derivations/ATLAS-CH-EVIDENCE-001-DOCUMENTARY.md

It must reconstruct the chapter's evidence rules from exact pinned governance objects and record the nonpromotion consequences.

## Computational witness record

Create:

mathematics/computational-witnesses/ATLAS-CW-EVIDENCE-001.md

It must include the exact finite claim, deterministic replay procedure, result, separate universal proof, and explicit claim boundary.

## Downstream handoff

Direct consumers may assume the evidence grammar without rebuilding it:

- ATLAS-CH-DATA-001;
- ATLAS-CH-MECHDIAG-001;
- ATLAS-CH-EVIDEX-001;
- ATLAS-CH-EXPERIMENT-001.

They may not treat the grammar itself as external scientific authority.

## Acceptance

The draft must:

- preserve all canonical epistemic labels and promotion rules;
- distinguish documentary support from logical entailment;
- define the six-field claim-support packet;
- reject a scalar hierarchy of evidence classes;
- include the exact finite computational-witness contrast;
- include all required promotion counterexamples;
- preserve project-evidence versus programme-context boundaries;
- preserve institutional-status versus mathematical-truth boundaries;
- provide explicit downstream permissions;
- remain monograph prose rather than repository instructions.
