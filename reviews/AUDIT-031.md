# AUDIT-031 — The External-Memory Thesis

## Disposition

**PASS AFTER THREE FORMAL PRECISION REPAIRS**

ATLAS-CH-EXTMEM-001 remains at `draft-v0.1`.

The chapter correctly develops a hybrid knowledge-placement thesis spanning parametric state and explicit external memory while preserving retrieval, continual-learning, provenance, freshness, access-control, and systems-cost boundaries.

AUDIT-031 found three in-scope precision defects:

1. the placement descriptor bundled latency and availability into one coordinate. These are now separated as `L` for latency and `H` for availability/failure tolerance;
2. the reader-facing text risked blurring external memory as a locus with persistence as a lifetime property. The repaired specification, derivation, manuscript, and tranche receipt now state explicitly that external locus and persistence are distinct; EXTMEM-001 focuses on persistent external records when that lifetime is deliberately chosen;
3. the versioned-store witness introduced version 2 without explicitly changing version 1 from current to superseded. The repaired witness now records the transition explicitly so there is exactly one current A version under the witness policy.

No exact witness value, source identity, prerequisite identity, placement conclusion, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  `c775a398062736c372f13f65dd2bb7349c2796c7`;
- implementation PR:
  #122;
- audit issue:
  #123;
- chapter:
  `ATLAS-CH-EXTMEM-001`.

## 1. Hard prerequisites

PASS.

### Retrieval

- manuscript blob:
  `a4cf5482885ae61ec5751168187365afd1866f3a`;
- AUDIT-027 blob:
  `71b9c41a343acb1e00c2fd572d1b28bd16eed078`;
- source-lock blob:
  `beee17eb3f727d0eb78083f5bd7afdd1028382a2`.

### Continual Learning

- manuscript blob:
  `0e9d13767e63ea4464ccaa61ce58809e38332d6c`;
- AUDIT-024 blob:
  `40da1dba9274d9e5b23104051b736bdcc13468a8`;
- source-lock blob:
  `51cf1617f6d888f968dcbc4892abd8655b388f3a`.

No Context Compilation or Polity manuscript is used as hidden prerequisite authority.

## 2. External primary examples

PASS.

The source lock identifies:

- Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*;
- Khandelwal et al. (2020), *Generalization through Memorization: Nearest Neighbor Language Models*;
- Borgeaud et al. (2022), *Improving language models by retrieving from trillions of tokens*;
- Meng et al. (2022), *Locating and Editing Factual Associations in GPT*.

These sources are used as representative examples of explicit non-parametric memory and direct parametric factual editing.

The chapter does not infer universal superiority for either architecture.

## 3. Placement descriptor

PASS AFTER REPAIR.

The final descriptor is:

`Place(k)=(V,P,S,D,R,L,H,A,G)`

for:

- volatility;
- provenance/audit need;
- sharing scope;
- deletion/supersession need;
- retrievability;
- latency;
- availability/failure tolerance;
- access-control/privacy;
- generalization/compression value.

No universal scalar placement score is defined.

## 4. External locus versus persistence

PASS AFTER REPAIR.

The chapter now states explicitly that:

- external memory describes locus;
- persistence describes lifetime;
- EXTMEM-001 specifically studies persistent external records when that lifetime is chosen.

This preserves the inherited Memory Taxonomy distinction.

## 5. Parametric state

PASS.

The chapter represents parametric behavior as:

`f_theta(q)`.

It does not claim that semantic facts map one-to-one to individual parameters.

It treats fact-to-weight editing as representation- and method-dependent.

## 6. External state

PASS.

External records carry explicit fields such as:

- key;
- value;
- source;
- version;
- status;
- metadata.

The chapter keeps storage semantics distinct from retrieval semantics.

## 7. Storage versus use

PASS.

The chapter explicitly rejects:

`correct_storage => correct_use`.

It lists independent failure modes including:

- stale index;
- wrong query;
- bad ranking/filter;
- access denial;
- stale cache;
- context omission.

This correctly inherits RETRIEVAL-001.

## 8. Exact parametric witness

PASS.

For:

`f_theta(A)=theta_1+theta_2`;

`f_theta(B)=theta_1-theta_2`,

initial targets:

`A=2,B=0`

give uniquely:

`theta=(1,1)`.

Updating only A to 4 while preserving B=0 gives uniquely:

`theta'=(2,2)`.

Thus:

`Delta theta=(1,1)`.

Both coordinates change in this representation.

## 9. Naive local parameter edit

PASS.

Using:

`theta_naive=(2,1)`

gives:

`A=3,B=1`.

The chapter correctly scopes this as a representation-specific interference witness, not a theorem about parameter editing generally.

## 10. Versioned external witness

PASS AFTER REPAIR.

The updated A versions are now represented explicitly as:

`A,v1 -> (2,s_A1,v1,status=superseded)`;

`A,v2 -> (4,s_A2,v2,status=current,supersedes=v1)`.

B remains unchanged/current.

Latest-version reads give:

`A=4,B=0`.

Exactly one A version is current under this witness policy.

## 11. Record-locality boundary

PASS.

The external witness changes one logical key.

The chapter explicitly refuses to infer from this that external updates require fewer machine operations or lower wall-clock cost.

Replication, indexing, synchronization, and cache invalidation remain systems costs.

## 12. Provenance boundary

PASS.

The external representation stores source/version metadata directly.

The bare parameter vector does not itself contain a per-fact source field.

The chapter also states explicitly that a parametric system may keep auxiliary provenance externally.

Thus the claim is about representation visibility, not metaphysical impossibility.

## 13. Stale-read counterexample

PASS.

After authoritative A advances from 2 to 4:

- latest authoritative read returns 4;
- a consumer pinned to the old snapshot still returns 2.

Therefore:

`externalized != automatically fresh`.

Freshness/version semantics are required.

## 14. Shared-memory semantics

PASS.

The chapter distinguishes:

- one shared authoritative store;
- consumer-visible effective state;
- caches/snapshots;
- synchronization/version policy.

Shared storage is not promoted into automatic consistency.

## 15. Access control

PASS.

The chapter defines a distinct authorization predicate for reads/writes and states:

> retrievable does not mean authorized.

This is correctly separated from relevance/ranking.

## 16. Deletion and supersession

PASS.

External records can support explicit states such as superseded, revoked, deleted, or quarantined.

The chapter correctly notes that:

- replicas/caches/logs can complicate deletion;
- deleting a source record is not equivalent to erasing learned parametric behavior.

## 17. Consolidation

PASS.

Externalization and consolidation remain distinct operations.

The chapter allows:

- explicit evidence first;
- later parametric consolidation when stable/generalizable structure emerges.

It does not require a one-way migration out of parameters.

## 18. Replay boundary

PASS.

The manuscript correctly observes that external records can be used for replay during training without becoming the final runtime answer source.

Memory locus and memory role remain distinct.

## 19. Truth/authority boundary

PASS.

The chapter states that an explicit record can still be false, stale, poisoned, unsupported, or low-authority.

External memory increases inspectability; it does not create truth.

## 20. Integrity

PASS subject to audit-PR validation.

The Chapter Ledger records EXTMEM-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-EXTMEM-LOCK-001`.

The manuscript's only citation key, `LewisEtAl2020RAG`, is already closed in the repository bibliography.

The computational witness is bound at:

`mathematics/computational-witnesses/ATLAS-CW-EXTMEM-001.md`.

The witness contains an explicit Claim boundary.

No governed figure is required.

## 21. Downstream handoff: Context Compilation

PASS.

CONTEXTCOMP-001 may inherit:

- hybrid parametric/external placement;
- versioned records;
- freshness requirements;
- retrieval/use separation;
- provenance-preserving memory semantics.

It must independently define task-specific context assembly.

## 22. Downstream handoff: Polity

PASS.

POLITY-001 may inherit:

- shared memory as an explicit locus;
- version/synchronization requirements;
- access-control distinction;
- coexistence of shared memory with private parametric/working state.

It must independently define multi-agent governance and authority.

## 23. Final disposition

AUDIT-031 passes after the three repairs above.

The durable external-memory thesis is:

**keep stable, reusable, compressed structure in learned capability where appropriate; keep mutable, addressable, provenance-sensitive, shareable state explicit where appropriate; connect them through typed retrieval and freshness contracts; and treat the placement choice as a multi-dimensional systems decision rather than a universal slogan.**
