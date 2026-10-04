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
