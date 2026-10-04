# Chapter Specification — ATLAS-CH-RESEARCHSM-001

## Identity

- Stable ID: `ATLAS-CH-RESEARCHSM-001`
- Title: **Research as a State Machine**
- Part: `ATLAS-PART-GOV`
- Status target: `draft-v0.1`
- Hard prerequisites: `ATLAS-CH-REPLAY-001`, `ATLAS-CH-FORMAL-001`
- Baseline: `889193744d0ae1bdd6ae6bd0d6328becbc5b3eaf`

## Contract

Develop Forge -> Solve -> Cert, bounded work packages, actor roles, idempotent retry, guarded transitions, failure states, and explicit authority changes as a research lifecycle.

## Opening obstruction

"The research task is done" is not a machine state. It may mean that a return arrived, was preserved, replayed, adjudicated, incorporated, used to authorize a successor, or separately certified. Those are different events.

## Bounded work package

Define

`W=(id,Q,B,S,D,R,A,Z)`

for stable identity, bounded question, bootstrap facts, allowed sources, required deliverables, durable return route, granted authority, and stop/non-authority conditions.

## Research state

Use

`x=(q,E,U,J,P,C,L)`

where:

- `q`: execution/transport phase;
- `E`: preserved immutable evidence objects;
- `U`: replay/check state;
- `J`: adjudication state;
- `P`: programme disposition;
- `C`: certification state;
- `L`: append-only history.

Representative execution phases are

`READY, LAUNCHED, RETURNED, CAPTURED, REPLAYED, ADJUDICATED`.

Programme disposition and certification are separate coordinates rather than one total linear ladder.

## Guarded transition

Each event `e` has a typed target, actor, guard `g_e(x)`, and partial transition `delta_e(x)`.

The transition is legal only when `g_e(x)=1`.

A successful computation does not bypass a missing guard.

## Canonical state versus history

Let `Canon(x)` omit retry-log multiplicity. A retry keyed by stable identity `k` is canonically idempotent when

`Canon(F_k(F_k(x)))=Canon(F_k(x))`.

The append-only history may still record both attempts. Idempotence therefore constrains the canonical effect, not the existence of an audit trail.

## Duplicate versus conflict

A duplicate return has the same dispatch identity and immutable result identity. It must not create a second canonical evidence effect.

A return with the same dispatch identity but a different immutable result identity is additional or conflicting evidence, not a duplicate, and must not silently replace the first object.

## Advancement guard

For evidence `e`, use the finite witness guard

`G_adv(e)=I(e) and S(e) and R(e) and A(e) and D(e)`

for valid identity/provenance, structural validity, required replay/check, supporting adjudication, and explicit programme disposition.

A contributor-supplied next residual does not itself set `D=1`.

## Separate certification transition

Certification is represented as a distinct state coordinate and transition. Its guard binds the exact target revision, the required support state, and the authority predicate defined by the governing policy.

Where a policy requires actor separation, that requirement is represented as an explicit predicate. Different actor labels alone are not sufficient evidence of independence.

## Finite witness requirements

Use one dispatch with one immutable result identity. The first arrival adds one canonical evidence object; an identical retry leaves the canonical evidence set unchanged while adding a history record.

Evaluate the five-factor advancement predicate on

`b=(1,1,1,1,0)`

and

`b'=(1,1,1,1,1)`.

The conjunction is respectively `0` and `1`. A repeated application at `b'` must leave the canonical advancement effect unchanged.

Also introduce a second result identity under the same dispatch and show that it is retained as a distinct evidence object rather than treated as the identical retry.

## Counterexamples and invariants

The manuscript must include these finite failures:

1. a structurally valid return with a missing required check does not satisfy the five-factor advancement predicate;
2. when the governing policy requires producer/reviewer separation, a same-actor review does not satisfy that declared predicate;
3. a fail-closed machine can preserve every safety invariant while remaining blocked, so safety does not imply liveness.

Required invariants:

- receipt alone does not change claim status;
- duplicate delivery does not duplicate the canonical advancement effect;
- different immutable result identities are never silently replaced;
- a transition with a false required guard is not taken;
- certification remains a separate state change.

## Failure and recovery

A failed transition preserves the last protected canonical state unless an explicit transition authorizes replacement. Recovery distinguishes retry, new evidence, supersession, implementation repair, and policy change.

## Public case-study boundary

The pinned public GCL artifacts supply one concrete lifecycle example with durable returns, replay/adjudication, fail-closed advancement, and separate successor selection. They are examples rather than universal workflow laws.

## Downstream handoff

After audit, `ATLAS-CH-GOVADAPT-001` may inherit the bounded work-package object, typed research state, canonical/history separation, idempotent retry, duplicate/conflict distinction, guarded advancement/certification, failure/recovery discipline, and finite witness.

## Completion

Source lock, formal packet, exact witness, manuscript, ledger/register updates, tranche receipt, green validation, implementation merge, bounded audit, audit repair/merge, closure verification, frontier recomputation, and controller reset are required.
