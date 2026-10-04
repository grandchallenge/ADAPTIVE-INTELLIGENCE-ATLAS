# ATLAS-CH-RESEARCHSM-001 — Formal and Derivation Packet

## 1. Bounded work package

Let

`W=(id,Q,B,S,D,R,A,Z)`.

The coordinates are stable identity, bounded question, bootstrap facts, allowed sources, required deliverables, durable return route, granted authority, and stop/non-authority conditions.

A work package is operationally bounded when those coordinates are sufficient to decide whether a candidate return is in scope.

## 2. Product research state

Define

`x=(q,E,U,J,P,C,L)`.

Here:

- `q` is the execution/transport phase;
- `E` is a finite map or set of immutable evidence identities;
- `U` is replay/check state;
- `J` is adjudication state;
- `P` is programme disposition;
- `C` is certification state;
- `L` is append-only history.

Representative execution phases are

`READY,LAUNCHED,RETURNED,CAPTURED,REPLAYED,ADJUDICATED`.

The product representation matters because programme disposition and certification need not occur as one total chain.

## 3. Typed events and guards

Let an event be

`e=(k,t,o,a,p)`

for stable event key, event type, target object identity, actor identity, and payload identity.

For each event type `t`, define a guard

`g_t(x,e) in {0,1}`

and partial transition

`delta_t(x,e)`.

The transition is admitted only if

`g_t(x,e)=1`.

## 4. Canonical projection

Let

`Canon(x)=(q,E,U,J,P,C)`

and retain `L` as append-only attempt history.

This separation permits a retry to be visible in history without multiplying its canonical effect.

## 5. Canonical idempotence

For an event with stable key `k`, let `F_k` be its guarded mutator.

Define canonical idempotence by

`Canon(F_k(F_k(x)))=Canon(F_k(x))`.

This is weaker than requiring the entire state including append-only history to be identical.

If the second attempt appends a history record, then generally

`L(F_k(F_k(x))) != L(F_k(x))`

while the canonical research state remains unchanged.

## 6. Duplicate return relation

Let a preserved return identity be

`r=(d,h)`

for dispatch/work-package identity `d` and immutable result digest `h`.

Define exact duplicate relation

`(d,h) ~dup (d',h')`

iff

`d=d'`
and
`h=h'`.

If `d=d'` but `h!=h'`, the returns are not duplicates.

A correct intake therefore behaves as a set insertion on exact identities rather than replacement by dispatch key alone.

## 7. Finite advancement predicate

For a candidate evidence object `e`, define Boolean predicates:

- `I(e)`: identity and provenance valid;
- `S(e)`: structural contract valid;
- `R(e)`: required replay/check condition satisfied;
- `A(e)`: adjudication supports the bounded claim;
- `D(e)`: programme disposition permits advancement.

Define

`G_adv(e)=I(e) S(e) R(e) A(e) D(e)`

with Boolean multiplication.

Every factor is necessary in this declared witness model.

## 8. Separate certification coordinate

Certification is modeled by `C`, not by overloading `P`.

A certification event has its own target-identity and policy predicates. Where the governing policy requires actor separation, that requirement is an explicit predicate rather than an inference from different labels.

## 9. Exact witness setup

Take one dispatch `d=17` and first immutable result identity `h=A`.

Let the initial canonical evidence set be empty:

`E_0=empty`.

History begins with a launch record.

## 10. First return

The first return identity is `r_A=(17,A)`.

Canonical capture is set insertion:

`E_1=E_0 union {r_A}={r_A}`.

Hence `|E_1|=1`.

## 11. Exact retry

Apply the identical return again.

Because set insertion is idempotent,

`E_2=E_1 union {r_A}=E_1`.

Thus `|E_2|=1`.

The attempt history may contain two arrival events while canonical evidence count remains one.

## 12. Boolean gate

For `G=b1*b2*b3*b4*b5`, the input `(1,1,1,1,0)` gives `G=0`, while `(1,1,1,1,1)` gives `G=1`.

## 13. Idempotent union

For a singleton `S={m}`, set union satisfies `S union S = S`. The finite witness uses this identity to ensure that an exact retry has one canonical effect.

## 14. Distinct result identity

For `r_A=(17,A)` and `r_B=(17,B)` with `A!=B`, the duplicate relation is false. Both identities therefore remain present in the evidence set `{r_A,r_B}`.

## 15. Missing-condition counterexample

For the same Boolean product, `(1,1,0,1,1)` gives `G=0`. A positive claim in the returned prose cannot change that arithmetic: a declared required condition that is false keeps the transition closed.

## 16. Safety invariants

The finite construction supports four invariants:

1. exact retry does not increase canonical evidence cardinality;
2. exact repeated canonical incorporation does not increase the incorporated-key cardinality;
3. a false required Boolean condition blocks the associated transition;
4. distinct immutable result identities remain distinct evidence objects.

These are safety properties: they rule out declared bad state changes.


## 17. Advancement as a separate canonical effect

Let `K_adv` be the set of evidence identities whose bounded claim has received an explicit programme advancement disposition.

For candidate evidence `e`, define:

`Advance(K_adv,e)=
K_adv union {id(e)}`

only when:

`G_adv(e)=1`.

If the guard is false, the canonical advancement set is unchanged.

Thus for:

`b=(1,1,1,1,0)`,

we have:

`G_adv(b)=0`

and no advancement mutation occurs.

For:

`b'=(1,1,1,1,1)`,

we have:

`G_adv(b')=1`

and the identity is inserted once.

## 18. Idempotent advancement

If evidence identity `m` is already in `K_adv`, repeated guarded incorporation gives:

`(K_adv union {m}) union {m}
=
K_adv union {m}`.

Therefore the canonical advancement effect is idempotent under exact identity.

The history may still append another attempted transition record.

This is the same canonical/history separation used for evidence capture.

## 19. Missing replay/check blocks advancement

Take:

`b_R=(1,1,0,1,1)`.

Then:

`G_adv(b_R)=0`.

All other witness conditions may be positive, but the declared required replay/check factor is false.

Therefore the transition remains closed.

This proves only the semantics of the declared conjunctive guard.

It does not claim that every scientific workflow must use these five exact factors.

## 20. Separation-of-duty predicate

Suppose a governing policy requires producer/reviewer identity separation for a particular review transition.

Define the narrow predicate:

`Sep(a_prod,a_rev)
=
1{a_prod != a_rev}`.

Then:

`Sep(A,A)=0`

and:

`Sep(A,B)=1`

for distinct actor identities A and B.

This predicate establishes only actor-identity separation.

It does not establish statistical, epistemic, cryptographic, organizational, or causal independence.

Those stronger notions require separate evidence.

## 21. Certification guard

Let a certification event target immutable revision `o`.

A schematic certification guard can be written:

`G_cert(o)
=
T(o) S_cert(o) H(o)`,

where:

- `T(o)` binds the exact target identity/revision;
- `S_cert(o)` represents the required support state;
- `H(o)` is the authority/policy predicate, including any required separation-of-duty condition.

Certification changes coordinate `C` only when the declared certification guard holds.

A positive programme disposition `P` does not by itself set `C`.

## 22. Receipt does not change claim status

Let claim-status coordinate `P` initially equal `P_0`.

A receipt/capture transition may change:

- execution phase `q`;
- evidence set `E`;
- history `L`.

It need not change `P`.

Thus one legal capture transition can satisfy:

`P_after=P_before`.

Receipt and claim promotion are therefore distinct state changes.

## 23. Safety does not imply liveness

Consider a finite state:

`x_block=(ADJUDICATED,E,U,J,P_pending,C_none,L)`

with all protected evidence intact and with advancement guard false only because:

`D(e)=0`.

Assume the only enabled future event is an idempotent retry that leaves `D(e)=0`.

Then every safety invariant from Section 16 is preserved forever:

- no duplicate canonical evidence effect;
- no invalid guarded transition;
- no silent replacement;
- no unauthorized certification.

But the liveness property:

`eventually(id(e) in K_adv)`

is false on this execution.

Therefore fail-closed safety does not imply progress.

A separate liveness assumption or enabled authority transition is required.

## 24. Failure-state preservation

For a guarded transition `delta_t` with false guard:

`g_t(x,e)=0`,

define the protected canonical outcome as:

`Canon(x_after)=Canon(x_before)`

unless the governing process explicitly defines a different failure transition.

History may append a failure record.

This is a fail-closed mutation rule, not a statement that the external world is unchanged.

## 25. Recovery classes are not interchangeable

After a failed or blocked transition, distinguish at least:

1. **retry** — same stable event/evidence identity, same intended canonical effect;
2. **new evidence** — different immutable result identity;
3. **supersession** — explicit governed relation marking one object as replacing another for a declared purpose;
4. **implementation repair** — workflow/tooling repair that does not silently alter protected evidence identity;
5. **policy change** — authorized change to the governing transition/guard itself.

Treating these as one generic "try again" operation would erase provenance and authority distinctions.

## 26. Public GCL lifecycle case study

The pinned public lifecycle controller records the concrete path:

`READY -> LAUNCHED -> RETURNED -> CAPTURED -> REPLAYED -> ADJUDICATED -> ADVANCED`.

It also records:

- a MATHFORGE-to-MATHSOLVE-to-MATHCERT authority boundary;
- protected GitHub state;
- allowed and prohibited actions;
- fail-closed behavior on identity/provenance mismatch.

The Atlas does not infer that this path is universal.

It is one operational instance of the product-state and guarded-transition ideas.

## 27. Frontier advancement is separate from contributor suggestion

The pinned Frontier Advancement Gate states that a completed RESULT/1 and a contributor-supplied next residual do not themselves authorize a successor.

In the Atlas notation, this is precisely why:

`D(e)`

is not set by contributor output alone.

Frontier advancement requires a protected programme disposition.

## 28. Controlled independent-intelligence intake

The pinned Controlled Epistemic Interface documents a bounded path:

`dispatch -> independent contribution -> immutable intake -> adjudication -> governed protected route`.

Its explicit boundary is:

`receive != believe != admit != certify`.

The Atlas uses this as a case study for state/authority separation.

It does not infer that distinct actors are independent merely because their labels differ.

## 29. Model boundary

The research-state machine certifies only the properties encoded by its state variables, guards, transition rules, and evidence identities.

Even perfect workflow conformance does not establish:

- mathematical truth of every admitted claim;
- completeness of the review;
- novelty;
- absence of shared prior information among actors;
- correctness of an omitted premise;
- correctness of the governance policy itself.

Those are separate claims.

## 30. Downstream interface

`ATLAS-CH-GOVADAPT-001` may consume:

- bounded work-package semantics;
- product research state;
- canonical/history separation;
- exact-identity retry idempotence;
- duplicate/conflict distinction;
- guarded promotion and certification;
- explicit actor-separation predicates;
- fail-closed safety versus liveness separation;
- recovery classes.

It must independently define how an adaptive system is permitted to alter its own behavior, policy, or authority while preserving optionality and correction capacity.
