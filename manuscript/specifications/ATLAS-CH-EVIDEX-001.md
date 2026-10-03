# Chapter Specification — ATLAS-CH-EVIDEX-001

## Identity

**Title:** Evidence Exchange and Zero-Context Work  
**Part:** Agents, Systems, and Hardware  
**Status:** specification-ready.  
**Epistemic class:** provenance standards plus Atlas synthesis and bounded GCL project evidence.

## Chapter contract

Explain how candidate evidence can move between actors without relying on hidden conversational state.

The chapter begins with the audited Evidence claim-support packet and the audited Coordination layer, then adds explicit dispatch, return, provenance, replay, and synthesis contracts.

## Dependency contract

Hard prerequisites:

- ATLAS-CH-COORD-001 — Coordination Architectures;
- ATLAS-CH-EVIDENCE-001 — Claims, Evidence, and Computational Witnesses.

The Coordination prerequisite supplies actor/event identity, channels, causal ordering, retry/deduplication, and transaction boundaries.

The Evidence prerequisite supplies the claim-support packet

K = (q, tau, S, Omega, N, D),

where a claim is separated from its support, scope, non-claims, epistemic class, and downstream permission.

No Replayable Evidence Objects, Formal Methods, or Research State Machine chapter may be used as hidden prerequisite authority.

## Reader outcome

A reader should be able to:

1. explain why a useful answer is not yet an exchangeable evidence object;
2. define a bounded dispatch packet;
3. define zero-context sufficiency relative to a declared actor class;
4. distinguish hidden context from explicitly imported prerequisites;
5. define a return object linked to its dispatch;
6. separate provenance from truth and authority;
7. explain source locking and immutable version identity;
8. distinguish receipt, acceptance, promotion, and certification;
9. explain independent/blind work as an information-flow constraint rather than proof of independence;
10. state how synthesis may combine returns without silently strengthening them.

## Formal spine

### Dispatch packet

Use

D = (delta, Q, B, Sigma, C, Lambda, Gamma, rho),

where:

- delta is a stable dispatch identity;
- Q is the exact bounded obligation;
- B is the complete bootstrap: definitions, protected facts, and immutable imported sources;
- Sigma is the allowed source/tool policy;
- C is the context and independence class;
- Lambda is the resource, rejection, and stop-condition set;
- Gamma is the exact return grammar;
- rho is the durable return route.

### Zero-context sufficiency

For a declared eligible actor class A, a dispatch is zero-context sufficient when every correctness-relevant task fact is either:

- present in D; or
- referenced by an immutable identity in B;

and the obligation, permissions, and return contract do not change with hidden session history.

Equivalently, for admissible hidden histories H1 and H2,

Interpret(D, H1) = Interpret(D, H2).

This is a task-interface property, not a claim that the actor has no background knowledge.

### Return object

Use

R = (delta, chi, K, Pi, V, Delta),

where:

- delta links the return to its dispatch;
- chi is the declared disposition;
- K is the Evidence claim-support packet;
- Pi is provenance: actor/source/tool/environment identity and derivation history as applicable;
- V is verification/falsification hooks;
- Delta is unresolved residual, limitation, or next bounded obligation.

A return is candidate evidence until a downstream review operation promotes some of its claims.

## Provenance model

Use W3C PROV at the conceptual level:

- entities are data/evidence objects;
- activities transform or generate entities;
- agents bear responsibility or attribution;
- derivation links outputs to inputs.

The Atlas exchange tuple is not claimed to be a serialization of PROV-DM.

## Reusability

Use FAIR only for bounded principles relevant here:

- persistent identifiers;
- rich metadata;
- qualified references;
- provenance;
- reusable description of data, algorithms, tools, and workflows.

FAIRness is not treated as scientific validity.

## Exact computational witness

Create mathematics/computational-witnesses/ATLAS-CW-EVIDEX-001.md.

Use two source versions with the same human pathname:

version v1 bytes:

    a=2
    b=3

SHA-256:

    b64a71cff6737624915d32f719c1c6957c60cfb0b286eb9d0b5d3741f26b1265

version v2 bytes:

    a=2
    b=4

SHA-256:

    c572528f7b0e700de0fd7bf2f3b7144a68f671ee0ed4b9d47943d9b489fe9844

Returned evidence bytes are:

    result=5

with SHA-256:

    ccdc6ccf3d8b13ef2de8739e91bacbe75d8f29b5c5a4dba8da5ac49881617d2f

Handoff A names only the mutable/human path "inputs.txt". Two source candidates remain.

Handoff B names the exact v1 SHA-256. One source candidate remains, and replay of the declared addition recomputes 5.

The witness establishes source-identity disambiguation, not truth of arbitrary evidence.

## GCL bounded project evidence

Use exact public MATHSOLVE artifacts only as examples of one implementation:

- CEI zero-context dispatch template;
- RESULT/1 grammar;
- independent_blind ZERO_CONTEXT adversarial packet.

The chapter may extract structural lessons from these artifacts but must not present GCL protocol names as universal scientific standards.

## Exchange invariants

The chapter must make explicit:

1. dispatch identity survives return;
2. source identity is version-specific where version changes matter;
3. return grammar preserves claim boundary;
4. return disposition is not self-certifying;
5. durable transport is part of the evidence chain when later actors must inspect the return;
6. replay instructions identify enough input/procedure/environment state to attempt reproduction;
7. synthesis takes intersections of compatible scope unless new support justifies expansion.

## Failure boundaries

Include:

- mutable URL/path without version identity;
- source hash without bibliographic/semantic identity;
- evidence payload detached from provenance;
- return detached from dispatch;
- hidden assumptions in chat history;
- ambiguous allowed-source policy;
- result grammar that omits limitations;
- private or ephemeral return transport;
- duplicate returns without stable identity;
- "independent" label without declared information-flow provenance;
- replay recipe that omits environment-sensitive choices;
- synthesis that silently widens domain or epistemic status.

## Figure decision

No governed figure is required for v0.1.

The dispatch/return tuples, provenance chain, and exact ambiguity witness carry the semantics directly.

## Downstream handoff

ATLAS-CH-REPLAY-001 may assume:

- stable dispatch/return identity;
- immutable source identity;
- provenance versus truth separation;
- replay hooks;
- claim-boundary preservation.

It must add environment pinning, exact artifact capture, and executable replay semantics.

ATLAS-CH-RESEARCHSM-001 may later consume:

- bounded work-package semantics;
- durable return routes;
- promotion boundaries;
- independent/blind context declarations.

It must add programme-level state transitions and governance.

## Acceptance

The draft must:

- preserve the audited Evidence and Coordination boundaries;
- define D and R exactly;
- define zero-context sufficiency relative to an actor class;
- distinguish imported prerequisites from hidden context;
- develop provenance without equating it to truth;
- include the exact source-identity witness;
- distinguish receipt, acceptance, promotion, and certification;
- explain independent/blind work as an information-flow condition;
- include the bounded GCL implementation example;
- state downstream handoffs by stable ID;
- remain mathematical systems/scientific-method prose rather than a repository manual.
