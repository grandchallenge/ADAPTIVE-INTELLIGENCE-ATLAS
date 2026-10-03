# ATLAS-CH-EVIDEX-001 — Formal and Documentary Packet

## Purpose

This packet defines the Atlas evidence-exchange interface and proves the exact source-identity witness.

It is built only from the audited Evidence and Coordination prerequisites plus provenance/reusability standards and bounded public GCL project evidence.

## 1. Starting point: claim-support packet

ATLAS-CH-EVIDENCE-001 supplies

K = (q, tau, S, Omega, N, D).

The fields separate:

- q — exact claim;
- tau — epistemic class;
- S — support objects/routes;
- Omega — scope, hypotheses, domain, run, dataset, version, or other boundary;
- N — stronger conclusions not licensed;
- D — downstream permission.

Evidence exchange must transport this packet without silently modifying its meaning.

## 2. Coordination substrate

ATLAS-CH-COORD-001 supplies actor identity, event identity, communication channels, causal ordering, retry/deduplication semantics, and transaction boundaries.

Evidence exchange adds a semantic constraint:

the channel may transport a return correctly while the return itself remains weak, false, ambiguous, or unsupported.

Transport correctness is therefore weaker than evidence quality.

## 3. Dispatch packet

Define

D = (delta, Q, B, Sigma, C, Lambda, Gamma, rho).

delta — stable dispatch identity.

Q — exact bounded obligation.

B — complete bootstrap consisting of definitions, protected facts, and immutable imported-source identities.

Sigma — source/tool policy.

C — context and independence class.

Lambda — resource, rejection, and stop-condition set.

Gamma — exact return grammar.

rho — durable return route.

The dispatch is an interface contract between sender and worker.

It should be sufficient to determine what work is authorized without recovering hidden chat history.

## 4. Zero-context sufficiency

Fix a declared actor class A.

Let H denote hidden conversational/session history not included in the dispatch.

Let Contract_A(D,H) denote the **authorized task contract** for an eligible actor class A when D is accompanied by hidden session history H.

The function is normative, not psychological: it records what premises, permissions, sources, success criteria, stop conditions, and return requirements the protocol authorizes.

D is zero-context sufficient for A when

Contract_A(D,H1)
=
Contract_A(D,H2)

for every pair of admissible hidden histories H1,H2.

The equality requires:

- same obligation Q;
- same imported facts B;
- same source/tool permissions Sigma;
- same context/independence declaration C;
- same stop/rejection conditions Lambda;
- same return grammar Gamma;
- same return route rho.

An actor may still misunderstand D or bring background knowledge. Zero-context sufficiency says only that hidden history is not an authorized source of correctness-relevant task state.

## 5. Hidden context versus imported prerequisite

An imported prerequisite is acceptable when the dispatch names it by a stable identity and states the role it may play.

Hidden context is a fact whose use changes the task but is available only through side-channel memory or prior conversation.

Thus:

"Use theorem T at commit/hash h under hypotheses H"

is an explicit import.

"Use the theorem we discussed yesterday"

is a hidden-context dependency unless the earlier object is identified durably.

The distinction is not stylistic.

It determines whether another actor can reconstruct the same obligation.

## 6. Return object

Define

R = (delta, chi, K, Pi, V, Delta).

delta — dispatch identity.

chi — declared disposition or return class.

K — claim-support packet from the Evidence chapter.

Pi — provenance record.

V — verification/falsification hooks.

Delta — unresolved residual, limitation, or next bounded obligation.

The return object is candidate evidence.

Its disposition chi is a statement by the contributor, not a certification event.

## 7. Provenance

At the conceptual level, the W3C PROV model distinguishes:

- entities;
- activities;
- agents;
- derivations;
- generation/use relations;
- responsibility/attribution.

For evidence exchange, these distinctions motivate a provenance record

Pi = (E_in, A_run, G_actor, E_out, links),

where:

E_in identifies input entities;

A_run identifies the activity/process;

G_actor identifies the responsible actor or execution identity;

E_out identifies the returned entity;

links record generation, use, and derivation relations.

The Atlas tuple is not claimed to be a complete PROV-DM serialization.

## 8. Provenance is not truth

Suppose an agent derives an incorrect lemma from an exact source-locked input.

The provenance can be flawless:

- exact source;
- exact actor;
- exact timestamp;
- exact code;
- exact return.

The lemma can still be false.

Therefore:

good provenance
does not imply
correct claim.

Provenance improves inspectability and attribution.

It does not replace verification.

## 9. Durable identity

A human-readable path or title can be useful but may be mutable or ambiguous.

Version-sensitive evidence should therefore carry a stable object/version identity.

Examples include:

- content hashes;
- immutable repository commits plus paths;
- versioned DOIs;
- archived object identifiers;
- source-lock fingerprints.

A hash answers a byte-identity question.

Bibliographic identity answers a semantic/source question.

Strong evidence exchange often needs both.

A hash alone does not tell us what an object means or whether it is authoritative.

## 10. Exact source-identity witness

Use two source versions with the same human pathname:

inputs.txt, version v1:

a=2
b=3

SHA-256:

b64a71cff6737624915d32f719c1c6957c60cfb0b286eb9d0b5d3741f26b1265

inputs.txt, version v2:

a=2
b=4

SHA-256:

c572528f7b0e700de0fd7bf2f3b7144a68f671ee0ed4b9d47943d9b489fe9844

Returned evidence bytes:

result=5

SHA-256:

ccdc6ccf3d8b13ef2de8739e91bacbe75d8f29b5c5a4dba8da5ac49881617d2f

Suppose the declared procedure is:

parse a and b;
return a+b.

### Handoff A

The return identifies only:

source_path = inputs.txt.

Two source candidates satisfy that path label:

v1 and v2.

Therefore provenance reconstruction is ambiguous.

If v1 is replayed, the procedure returns 5.

If v2 is replayed, the procedure returns 6.

The evidence bytes "result=5" do not determine which source version was used.

### Handoff B

The return includes:

source_sha256 =
b64a71cff6737624915d32f719c1c6957c60cfb0b286eb9d0b5d3741f26b1265.

Exactly one of the two candidate source versions matches.

Replay of the declared addition yields 5.

Thus Handoff B supports deterministic source-version reconstruction within the finite candidate set.

This proves an identity property, not the universal correctness of content hashes or replay systems.

## 11. Reusability and FAIR

FAIR principles support several design choices relevant to evidence exchange:

- persistent identifiers;
- rich metadata;
- explicit identifier-to-metadata association;
- qualified references among data;
- detailed provenance;
- reusable descriptions of data, algorithms, tools, and workflows.

The Atlas uses those ideas narrowly.

A FAIR object can still contain a wrong result.

FAIRness improves findability and reuse conditions, not truth by itself.

## 12. Return grammar

A strict return grammar can preserve evidence boundaries.

A useful grammar should force the contributor to state:

- dispatch identity;
- disposition;
- strongest exact statement;
- derivation/support;
- assumptions beyond bootstrap;
- verification/falsification hooks;
- claim boundary;
- unresolved residual.

The grammar does not make the claim correct.

It makes omissions more visible and makes independent review easier.

## 13. Durable return route

If downstream actors must inspect the result, transport must leave a durable identity.

A return route rho can be:

- a versioned file;
- an issue/comment identity;
- an object store record;
- a database row with stable key;
- another persistent append-only surface.

An ephemeral private message can be operationally useful.

It is insufficient as the only evidence surface when later audit depends on it.

The durability requirement is task-relative.

Not every informal conversation needs archival treatment.

## 14. Independent and blind work

Let I denote the information set available to a contributor.

An independent_blind assignment attempts to constrain I so that the worker does not see selected prior returns or solution paths.

This is an information-flow condition.

It does not imply:

- different model weights;
- different training data;
- different organization;
- statistical independence;
- independent certification.

Therefore the return should state actual provenance and context class rather than infer independence from a label alone.

## 15. Receipt, acceptance, promotion, certification

Evidence exchange requires four distinct states.

Receipt:
the object arrived on the declared surface.

Acceptance:
a reviewer judges that it satisfies the intake contract.

Promotion:
some claim in the object is admitted into a stronger project state, theorem, report, or chapter.

Certification:
a separate process confers whatever formal/institutional status that certification means.

The implication chain does not reverse.

Receipt does not imply acceptance.

Acceptance does not imply promotion.

Promotion does not automatically imply independent certification.

## 16. Replayability

A return is replayable at a declared level only if another actor can identify enough of:

- inputs;
- versions;
- procedure/code;
- environment assumptions;
- random seeds where material;
- expected outputs/checks;
- acceptance predicates.

to attempt the same computation or verification.

Replayability is therefore graded by what has been pinned.

A source-only replay is weaker than an environment-pinned executable replay.

ATLAS-CH-REPLAY-001 strengthens this object further.

## 17. Duplicate returns

If retries can occur, a stable dispatch identity delta and stable return identity are necessary for deduplication.

Two syntactically distinct comments can describe one logical result.

Two identical payloads can come from different actors or source versions.

Therefore duplicate detection cannot safely rely on payload text alone.

The Coordination chapter's delivery/effect distinction applies directly.

## 18. Synthesis

Suppose two returns establish pointwise instances of the same proposition schema:

R1:
for every x in Omega1, q(x);

R2:
for every x in Omega2, q(x).

Then, with no additional assumptions,

for every x in Omega1 union Omega2, q(x)

follows directly.

But there is **no generic union/intersection rule for arbitrary claims**. Global properties, coupled hypotheses, uniqueness statements, convergence modes, or claims whose meaning changes with the domain require a separate composition argument.

A downstream consumer that needs two guarantees simultaneously at the same x may naturally restrict to Omega1 intersect Omega2, but that too must match the logical form of the claims.

The key rule is:

synthesis must state and justify the composition rule.

It may not silently replace local support by an unrestricted global claim.

## 19. Conflicting returns

Suppose one return claims q and another claims not-q under apparently identical assumptions.

The correct synthesis state is conflict, not majority vote.

Possible next actions include:

- compare source identities;
- compare hypotheses;
- replay both;
- inspect hidden assumptions;
- seek a counterexample;
- issue an adversarial audit.

Evidence exchange should preserve disagreement until a new adjudication operation resolves it.

## 20. GCL public implementation example

At public MATHSOLVE commit

1273b75457f42da62a8af4c69493d44d293d4567,

the CEI dispatch template requires:

- exact bounded target;
- complete definitions;
- imported facts;
- excluded assumptions;
- permitted contribution types;
- falsification/rejection conditions;
- resource bounds;
- exact return contract;
- authority boundary.

A public RESULT/1 grammar carries:

- dispatch identity;
- context class;
- source policy;
- strongest exact statement;
- derivation;
- assumptions;
- verification/falsification hooks;
- claim boundary;
- next residual.

A public Yang-Mills adversarial packet demonstrates a ZERO_CONTEXT, independent_blind assignment constrained to a protected packet.

These are exact project artifacts.

They demonstrate one working design.

They do not establish a universal evidence-exchange standard.

## 21. Downstream handoff

ATLAS-CH-REPLAY-001 may consume:

- D and R identities;
- immutable source/version identity;
- provenance versus truth separation;
- verification hooks;
- replayability levels;
- claim-boundary preservation.

It must add environment pinning, artifact capture, executable replay, and semantic bridges.

ATLAS-CH-RESEARCHSM-001 may later consume:

- bounded work packages;
- durable return surfaces;
- context/independence declarations;
- receipt/acceptance/promotion distinctions.

It must add programme-level state transitions and governance.

## Claim boundary

This packet defines an Atlas protocol for evidence exchange and proves the finite source-identity ambiguity witness.

It does not prove that provenance guarantees correctness, that zero-context work guarantees independent reasoning, that content hashing alone provides semantic identity, or that the GCL dispatch/result grammar is universally optimal.
