# Chapter Specification — ATLAS-CH-SYNTHESIS-001

## Identity

**Title:** Beyond the Monolithic Model  
**Part:** Scientific Method, Evidence, and Governed Adaptation  
**Status target:** draft-v0.1  
**Implementation issue:** #276  
**Protected baseline:** 4c038e50f91e152e8139fc0dd412587d02f620fb

## Hard prerequisites

### ATLAS-CH-FRONTIER-001 / AUDIT-043

May inherit the programme taxonomy, exact status grammar, bounded proof/experiment obligations, and the rule that frontier questions are not results.

### ATLAS-CH-POLITY-001 / AUDIT-048

May inherit the polity object, private/shared-state separation, capability/authority distinction, candidate-validation-commit decomposition, exact specialization witness, and heterogeneous cost bookkeeping.

Exact identities are frozen in:

sources/source-locks/ATLAS-CH-SYNTHESIS-001.yaml

## Typed synthesis object

Define

[
Sigma=(X,D,M,T,C,E,A,G,Q,K).
]

The fields are:

- (X): model/representation and private state;
- (D): dynamics/update laws;
- (M): persistent/shared memory;
- (T): tools/external services;
- (C): coordination/routing/composition;
- (E): evidence/validation;
- (A): adaptation mechanisms;
- (G): governance/authority;
- (Q): task contract;
- (K): heterogeneous cost/resource vector.

These are typed objects. They are not assumed to live in one vector space or share one optimizer, timescale, or authority model.

## Exact composition witness

Tasks:

[
Q={alpha,eta}.
]

Specialists:

[
A_alpha(alpha)=1,quad A_alpha(eta)=0,
]

[
A_eta(alpha)=0,quad A_eta(eta)=1.
]

Router:

[
R(alpha)=A_alpha,qquad R(eta)=A_eta.
]

Candidate:

[
c=(q,y,s).
]

Validator:

[
V(c)=1
]

iff (y=1) and (s) is the declared routed specialist for (q).

Governance:

[
G(c,V)=	ext{commit}
]

iff (V(c)=1).

Committed record:

[
m=(q,y,s,sigma=mathrm{validated}).
]

Shared memory is a persistent map keyed by (q).

System success for task (q) requires:

1. answer (y=1);
2. correct specialist source;
3. validator acceptance;
4. authorized commit;
5. durable validated memory record;
6. later recall of the committed answer.

## Full composition result

Under the declared composition:

- task accuracy = (2/2);
- validated commit coverage = (2/2);
- persistent recall coverage = (2/2);
- unauthorized commits = (0).

## Ablation 1 — broken router

Use:

[
R'(alpha)=A_alpha,qquad R'(eta)=A_alpha.
]

Then beta receives candidate answer (0), validation rejects it, and:

- task accuracy = (1/2);
- validated commit coverage = (1/2).

Thus component count alone does not determine system capability.

## Ablation 2 — remove validator, keep governance

Candidate production can remain correct on both tasks, but the unchanged governance rule requires positive validation evidence.

With no validator evidence:

- transient answer accuracy may remain (2/2);
- authorized commit coverage = (0/2).

Thus answer capability and durable governed state are distinct.

## Ablation 3 — remove shared memory

Answers, validation, and authorization may all succeed transiently.

Without persistent memory:

- persistent recall coverage = (0/2).

Thus immediate success does not imply durable shared state.

## Ablation 4 — remove governance gate

Introduce rejected candidate:

[
c_{mathrm{bad}}=(eta,1,A_alpha).
]

The validator rejects it because the source is wrong.

With governance enforced, it cannot commit.

If commit bypasses governance, the rejected candidate can be written.

Thus:

[
oxed{
	ext{correct-looking content}

otRightarrow
	ext{authorized state transition}.
}
]

## Status grammar

The chapter must preserve FRONTIER's exact categories:

- AUDIT_BOUND_SUBSTRATE
- DRAFT_SUBSTRATE
- BOUNDED_EVIDENCE
- ARCHITECTURE_STAGE
- OPEN_PROOF_OBLIGATION
- OPEN_EXPERIMENT_OBLIGATION
- CONJECTURAL_CONNECTION

No open programme item may be promoted merely because SYNTHESIS discusses it.

## Capability versus architecture claim

The finite witness proves only that one declared composition has a system-level property not shared by its broken ablations.

It does not prove:

- distributed systems are always superior;
- monolithic models are obsolete;
- more agents/components improve intelligence;
- one architecture is universally optimal.

## Cost boundary

Retain the polity cost vector:

[
K=(c_{mathrm{coord}},c_{mathrm{mem}},c_{mathrm{tool}},c_{mathrm{human}},c_{mathrm{val}}).
]

Do not scalarize unlike costs without a declared objective/conversion.

## Reader outcomes

A reader should be able to:

1. state the typed synthesis object;
2. distinguish capability, authority, evidence, governance, and cost;
3. replay the full two-task composition witness;
4. replay each ablation and identify which system contract fails;
5. preserve FRONTIER status categories;
6. explain why the witness does not establish a universal architecture;
7. identify open proof/experiment obligations as still open.

## Required artifacts

- source lock;
- specification;
- derivation packet;
- exact computational witness;
- reader manuscript;
- Chapter Ledger promotion;
- Source Register entry;
- transaction receipt;
- mandatory post-draft audit.

## References used in this chapter

No new external academic authority is added.

Programme-status authority is inherited through audited ATLAS-CH-FRONTIER-001.

System-composition authority is inherited through audited ATLAS-CH-POLITY-001.

Exact prerequisite identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-SYNTHESIS-001.yaml
