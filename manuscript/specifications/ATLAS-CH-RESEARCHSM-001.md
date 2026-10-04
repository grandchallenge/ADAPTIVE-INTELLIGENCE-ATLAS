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
