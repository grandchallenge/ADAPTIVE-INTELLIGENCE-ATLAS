# ATLAS-CH-EXTMEM-001 — Formal and Derivation Packet

## 1. Placement is an architectural relation

Let `K` be a set of knowledge items or knowledge classes.

A placement architecture assigns each item to one or more loci:

`ell(k) subseteq {parametric, external}`.

The relation may be hybrid.

The chapter does not assume a total binary partition because the same information can be represented redundantly in both parameters and external records.

## 2. Placement descriptor

For item `k`, use:

`Place(k)=(V,P,S,D,R,L,A,G)`.

Coordinates represent:

- volatility/update frequency `V`;
- provenance/audit need `P`;
- sharing scope `S`;
- deletion/supersession need `D`;
- explicit retrievability/addressability `R`;
- latency/availability constraints `L`;
- access-control/privacy requirements `A`;
- value of parametric compression/generalization `G`.

No canonical addition or scalarization is defined.

Any policy that reduces these coordinates to one score must declare its weighting and operating assumptions.

## 3. Parametric state

A parametric component is represented by:

`theta in Theta`.

Its behavior is:

`f_theta(q)`

for query `q`.

A fact update is implemented by some state transformation:

`U_param(theta,e)=theta'`

where `e` denotes the intended edit.

The mapping from semantic fact edit to parameter update is representation- and method-dependent.

## 4. External state

An external memory consists of records:

`m=(key,value,source,version,status,metadata)`.

A versioned write produces a new record or state:

`U_ext(M,e)=M'`.

A current read is not merely:

`key -> value`.

It must specify version/freshness policy.

Write:

`read(M,key,pi_fresh)`.

## 5. Retrieval is distinct from storage

Even if the correct record exists in `M`, a system can fail because:

- the query is wrong;
- the filter excludes it;
- ranking misses it;
- the index is stale;
- the caller lacks access;
- context compilation omits it.

Therefore:

`correct_storage !=> correct_use`.

This is inherited from RETRIEVAL-001.

## 6. Forgetting is distinct from parameter movement

CONTINUAL-001 established that forgetting is behavioral under an evaluation protocol.

Therefore the existence of an external update path does not imply that parametric learning stops.

Stable skills, procedures, representations, and reusable structure may still require parameter updates.

External memory changes the placement of selected knowledge.

It does not replace learning.

## 7. Exact parametric witness

Define two queries:

`Q={A,B}`.

Let:

`theta=(theta_1,theta_2)`.

Define:

`f_theta(A)=theta_1+theta_2`;

`f_theta(B)=theta_1-theta_2`.

Initial targets:

`y_A=2`;

`y_B=0`.

Solve:

`theta_1+theta_2=2`;

`theta_1-theta_2=0`.

Adding equations:

`2 theta_1=2`.

So:

`theta_1=1`.

Then:

`theta_2=1`.

Hence:

`theta=(1,1)`.

## 8. Update only A

Change the desired facts to:

`y'_A=4`;

`y'_B=0`.

Solve:

`theta'_1+theta'_2=4`;

`theta'_1-theta'_2=0`.

Thus:

`theta'_1=2`;

`theta'_2=2`.

Hence:

`theta'=(2,2)`.

Both coordinates change.

The parameter displacement is:

`Delta theta=(1,1)`.

For this representation:

`||Delta theta||_0=2`.

This count is representation-specific and is not a universal measure of edit difficulty.

## 9. Naive coordinate-local edit

Suppose only `theta_1` changes:

`theta_naive=(2,1)`.

Then:

`f_theta_naive(A)=3`;

`f_theta_naive(B)=1`.

So the edit:

- fails to reach new target `A=4`;
- alters the unrelated target `B=0`.

This is an exact interference witness for this chosen parameterization.

It is not a theorem about all neural representations.

## 10. External-memory witness

Initial records:

`M_1[A]=(value=2,source=s_A1,version=1,status=current)`;

`M_1[B]=(value=0,source=s_B1,version=1,status=current)`.

Update A by adding:

`r_A2=(key=A,value=4,source=s_A2,version=2,status=current,supersedes=1)`.

Mark old A record superseded or select the highest admissible version under the read policy.

B remains unchanged.

Then:

`read(M_2,A,latest)=4`;

`read(M_2,B,latest)=0`.

The changed logical record set is:

`{A}`.

## 11. Record-local update

Let:

`KeysChanged(M_1,M_2)
=
{k : current(M_1,k) != current(M_2,k)}`.

For the witness:

`KeysChanged(M_1,M_2)={A}`.

Thus:

`|KeysChanged|=1`.

This record-locality property is exact for the chosen store representation.

It does not imply lower wall-clock cost than a parameter edit.

## 12. Provenance visibility

Define:

`Prov(M,k,v)=source metadata attached to record (k,v)`.

Then:

`Prov(M_1,A,1)=s_A1`;

`Prov(M_2,A,2)=s_A2`.

The supersession edge preserves the update history.

The bare vector:

`theta=(1,1)`

does not itself contain a per-fact source field.

This proves a representation difference only.

A parametric system could maintain auxiliary provenance externally.

## 13. Stale-read counterexample

Let consumer `C` hold a snapshot pointer to:

`M_1`.

After the authoritative store becomes `M_2`:

`read(M_2,A,latest)=4`;

but:

`read(M_1,A,snapshot)=2`.

Therefore:

`externalized != automatically fresh`.

Freshness requires a policy connecting consumer-visible version state to authoritative version state.

## 14. Version acceptance

Let the authoritative current version for key `k` be:

`v^*(k)`.

Let consumer-observed version be:

`v_C(k)`.

A strict freshness condition is:

`v_C(k)=v^*(k)`.

A bounded-staleness condition may permit:

`age(v_C(k),v^*(k)) <= tau_stale`

under a declared version-age metric.

The chapter does not choose one universal freshness policy.

## 15. Deletion and supersession

External records can support explicit state transitions such as:

- current;
- superseded;
- revoked;
- deleted;
- quarantined.

A model parameter edit has different semantics.

Removing a fact from weights is not equivalent to deleting a keyed record unless a method proves the desired behavioral erasure.

Therefore deletion requirements are a placement pressure, not a guarantee.

## 16. Shared read semantics

Suppose agents `C_1,C_2` query one authoritative store.

If both use the same accepted version and retrieval contract:

`read_C1(M,k)=read_C2(M,k)`

for exact-key deterministic reads.

If one uses stale cache `M_1` while another uses `M_2`, the equality can fail.

Shared storage therefore requires synchronization semantics before it yields shared effective memory.

## 17. Access-control boundary

Let:

`allow(a,k,op)`

be an authorization predicate.

A valid read requires:

`allow(agent,k,read)=true`.

External addressability makes access control explicit at the memory layer.

It also creates an attack surface:

- unauthorized read;
- unauthorized write;
- record poisoning;
- index tampering;
- metadata leakage.

External memory is not automatically safer than parametric memory.

## 18. Placement pressure: volatility

If a fact changes often, repeated parameter updates may be operationally expensive or behaviorally risky.

A versioned record can represent each change directly.

This favors external placement only when retrieval/update infrastructure is acceptable.

## 19. Placement pressure: provenance

If each claim must carry source identity, timestamp, or authority metadata, explicit records provide a natural representation.

Parametric behavior can still be source-informed, but source-to-output attribution is not automatically recoverable from weights.

This favors explicit memory when per-item provenance is load-bearing.

## 20. Placement pressure: sharing

If many agents require one mutable fact, one authoritative shared record can reduce duplicated update operations.

But shared memory introduces consistency, availability, and access-control obligations.

Thus sharing pressure cuts both ways.

## 21. Placement pressure: compression/generalization

Some knowledge is valuable because many examples jointly induce a reusable feature or procedure.

Keeping every training example as an external record is not equivalent to learning that structure.

This favors parametric consolidation where generalization/compression is the desired behavior.

## 22. Placement pressure: latency

External reads incur retrieval/index/network/cache costs.

Parametric behavior can be available in the forward pass without explicit record fetches.

Thus low-latency ubiquitous structure can favor parametric placement.

No universal latency ordering is claimed because system architecture and hardware matter.

## 23. Hybrid consolidation

Consider an external record stream:

`e_1,e_2,...,e_n`.

A consolidation process may update parameters using selected evidence while retaining the records.

This creates two distinct operations:

- memory write/update;
- model learning/consolidation.

Conflating them hides important failure modes.

## 24. Placement decision record

A practical placement decision should record:

- item/class identity;
- volatility;
- provenance requirement;
- sharing scope;
- deletion/supersession requirement;
- retrieval/index availability;
- latency budget;
- access-control/privacy constraints;
- expected generalization/compression value;
- chosen locus;
- fallback behavior if retrieval fails;
- freshness policy;
- evidence supporting the decision.

## 25. Downstream interface

CONTEXTCOMP-001 may consume:

- external record/version semantics;
- freshness requirements;
- retrieval-versus-use separation;
- hybrid parametric/external placement.

POLITY-001 may consume:

- shared-memory scope;
- authoritative-version semantics;
- access-control and synchronization obligations.

Neither may infer that shared external memory is automatically consistent, complete, trustworthy, or universally preferable.
