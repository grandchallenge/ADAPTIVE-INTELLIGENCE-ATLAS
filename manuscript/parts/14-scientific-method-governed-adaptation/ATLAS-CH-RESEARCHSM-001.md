# Research as a State Machine
<!-- ATLAS-CH-RESEARCHSM-001 -->

**Epistemic status:** audited Replay/Formal prerequisites + public GCL workflow case study + Atlas synthesis + exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-RESEARCHSM-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-RESEARCHSM-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-RESEARCHSM-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-RESEARCHSM-001.yaml

A sentence such as "the research task is done" hides too much.

A result can arrive without being preserved. A preserved artifact can remain unchecked. A successful replay can reconstruct a computation without deciding the surrounding claim. A bounded review can support a result without settling every later use of it.

This chapter replaces those ambiguities with explicit objects and transitions.

## 1. From evidence objects to research state

The Replayable Evidence chapter established that source identity, execution, observation, interpretation, review, and certification are different relations.

The Formal Methods chapter established that a transition system is useful only when its state, transition relation, invariants, and model boundary are explicit.

Research workflows need both ideas.

Evidence objects tell us what moves through the workflow.

A state machine tells us which changes are permitted, what each change means, and which facts remain unchanged when a transition fails.

The object of this chapter is therefore not a task list.

It is a typed lifecycle for evidence-bearing research objects.

## 2. A bounded work package

Let

`W=(id,Q,B,S,D,R,A,Z)`.

The coordinates record:

- stable work-package identity;
- bounded question or obligation;
- explicit bootstrap facts;
- allowed source universe;
- required deliverables;
- durable return route;
- authority granted to the worker;
- stop conditions and explicit non-authorities.

The point of this tuple is not administrative completeness.

It is semantic closure.

A competent contributor should be able to decide, from the package itself, what problem is being attempted, which premises are authorized, what a valid return must contain, and what the return is not allowed to decide.

## 3. The research state is a product

Represent the live research state as

`x=(q,E,U,J,P,C,L)`.

Here:

- `q` records execution or transport phase;
- `E` contains preserved immutable evidence identities;
- `U` records replay or checking state;
- `J` records adjudication;
- `P` records programme disposition;
- `C` records certification state;
- `L` is append-only history.

A representative transport path is:

`READY -> LAUNCHED -> RETURNED -> CAPTURED -> REPLAYED -> ADJUDICATED`.

That path is useful.

It is not the whole machine.

Programme disposition and certification are separate coordinates because neither is merely another name for successful transport.

## 4. State change requires a declared condition

For each event type, define a condition `g_e(x)` and a partial state update `delta_e(x)`.

The update is applied only when the declared condition holds.

A return can arrive without satisfying its schema. A schema-valid return can fail replay. A replayed result can fail adjudication. A positively adjudicated result can still await a separate programme decision.

The state machine keeps these cases separate.

## 5. Forge, Solve, and Cert are roles

The public GCL workflow uses Forge, Solve, and Cert as a separation of work.

At the level needed here:

- Forge fixes problem and source identity;
- Solve performs bounded mathematical or computational work and adjudication;
- Cert performs a separate certification function.

The names are project-specific. The structural lesson is that evidence production, adjudication, and later certification need not be one operation.

## 6. Receipt is not incorporation

Suppose a durable return reaches its declared route.

That establishes receipt.

It does not automatically establish structural validity, replay success, scientific correctness, programme incorporation, successor selection, or certification.

The earlier evidence chapters stated this boundary conceptually.

The state-machine view makes it operational: each distinction occupies a different coordinate or transition.

## 7. Idempotence belongs to canonical effect

A retryable research system needs two views of state.

The first is canonical state: which evidence objects and dispositions currently count.

The second is history: what attempts, retries, failures, and recoveries occurred.

Let `Canon(x)` omit retry-log multiplicity.

For a stable event key `k`, canonical idempotence means

`Canon(F_k(F_k(x)))=Canon(F_k(x))`.

The history may still record both attempts.

This distinction matters.

If the entire history had to be identical after retry, the system would have to hide the fact that a retry occurred.

If canonical state were allowed to multiply with every retry, the same evidence could acquire multiple effects merely because transport repeated.

Neither behavior is desirable.

## 8. Duplicate is an identity relation

A return is not a duplicate merely because it belongs to the same work package.

Use the exact return identity

`r=(d,h)`

for dispatch identity `d` and immutable result identity `h`.

Two returns are exact duplicates only when both coordinates agree.

If the dispatch is the same but the result identity differs, the programme has two evidence objects.

It may later decide that one supersedes, refutes, strengthens, or merely differs from the other.

But that semantic decision must not be smuggled into transport by treating every second return as "the same thing."

## 9. Exact finite retry witness

Take dispatch

`d=17`

and result identity

`r_A=(17,A)`.

The first capture creates the singleton evidence set

`E_1={r_A}`.

Receive the identical result again.

Set union gives

`E_2=E_1 union {r_A}=E_1`.

Therefore canonical evidence count remains

`1`.

Now introduce

`r_B=(17,B)`

with

`B!=A`.

Then

`E_3={r_A,r_B}`

has cardinality

`2`.

The witness therefore separates retry from genuinely distinct evidence using only stable identity and finite set arithmetic.
