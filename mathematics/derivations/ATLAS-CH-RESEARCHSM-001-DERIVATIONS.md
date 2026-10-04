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
