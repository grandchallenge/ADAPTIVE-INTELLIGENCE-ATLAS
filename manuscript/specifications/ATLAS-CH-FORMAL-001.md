# Chapter Specification — ATLAS-CH-FORMAL-001

## Identity

- Stable ID: `ATLAS-CH-FORMAL-001`
- Title: **Formal Methods and Machine-Checkable Claims**
- Part: `ATLAS-PART-GOV`
- Status target: `draft-v0.1`
- Hard prerequisite: `ATLAS-CH-REPLAY-001`
- Implementation issue: #107
- Baseline: `c257c8400a329cb127ac322cf8bfb70d4693b10c`

## Contract

Develop specifications, invariants, contracts, proof assistants, Lean, and the limits of formal certification.

## Opening obstruction

A machine can verify a theorem that is irrelevant to the intended claim.

A test suite can pass without proving a universal property.

A model checker can exhaust a bounded/abstract model without proving the deployed system.

A proof assistant can reject a false derivation while still depending on the correctness of the formal statement, axioms, definitions, and trusted kernel.

The chapter must therefore separate the objects being checked.

## Formal claim stack

Use the following Atlas stack:

`R -> S -> M -> P -> K -> I -> W`

where:

- `R`: natural-language requirement or intended claim;
- `S`: formal specification;
- `M`: formal model/semantics;
- `P`: proof object, derivation, model-checking result, or certificate;
- `K`: checker/kernel and trusted computing base;
- `I`: implementation or deployed artifact;
- `W`: real-world environment/phenomenon.

The arrows are obligations, not automatic equivalences.

A checked theorem at `S/M/P/K` does not by itself establish:

- that `S` captures `R`;
- that `I` implements `S`;
- that `W` satisfies the modeling assumptions.

## Specification versus requirement

A requirement is what the human/system intends.

A formal specification is a mathematical object intended to encode some part of that requirement.

The bridge

`R ~ S`

is semantic and must be reviewed.

Formal precision can expose ambiguity in `R`, but it cannot mechanically guarantee adequacy unless adequacy itself has been formalized against another trusted object.

## Hoare-style contracts

Use a Hoare triple

`{P} C {Q}`

as a compact program-contract object:

if precondition `P` holds and command `C` terminates under the adopted semantics, then postcondition `Q` holds.

The chapter must state the semantics and total/partial-correctness scope when needed.

Hoare logic is used to demonstrate formal contracts and inference, not as the only formal-methods framework.

## Invariants

For transition system

`(X, Init, Next)`

and predicate `Inv(x)`, an inductive invariant requires:

1. initialization:
   `Init(x) => Inv(x)`;
2. preservation:
   `Inv(x) and Next(x,x') => Inv(x')`.

Then every state reachable by finitely many `Next` steps from an initial state satisfies `Inv`.

This proof is universal over the declared transition system, not merely over tested traces.

## Testing versus proof

Finite tests establish concrete executions.

They can:

- find counterexamples;
- exercise code paths;
- check regressions;
- support conformance evidence.

They do not, without an additional theorem or exhaustive finite-domain argument, establish a universal property over an infinite state/input space.

## Model checking

Model checking explores states of a formal model under declared semantics.

For a finite state space, exhaustive exploration can establish a property for all reachable states of that model.

For bounded or abstract models, the claim must preserve the bound/abstraction.

A model-checking result is not automatically a proof that arbitrary deployed code implements the model.

## Proof assistants and the trusted kernel

Use the LCF/Lean architecture to explain a small trusted checker/kernel.

Automation, tactics, elaborators, search procedures, and external solvers may be large.

The final proof object/term is accepted only if the trusted kernel validates it under the formal environment.

This shifts trust rather than eliminating it.

The trust base still includes, as applicable:

- kernel implementation;
- logical axioms;
- definitions;
- imported libraries;
- compiler/runtime/hardware assumptions if execution is involved;
- semantic bridge from human claim to formal theorem.

## Lean boundary

Lean is used as the primary named proof-assistant example.

The chapter may state that Lean uses dependent type theory and a small trusted proof-checking kernel, supported by the 2015 system description and the versioned official reference.

Do not claim that:

- every Lean theorem is axiom-free;
- every imported theorem is mathematically appropriate for the intended application;
- kernel checking proves the adequacy of informal requirements;
- automation is trusted merely because it produced a term that the kernel accepts.

No Lean artifact is required in this tranche because the chapter's exact witness is language-independent and the repository does not yet declare a FORMAL-001-specific Lean toolchain lock.

## Exact witness

Specification:

- state `x in N`;
- initial state `x_0=0`;
- transition `x' = x+2`;
- invariant `Even(x)`.

Inductive proof:

- base: `0` is even;
- step: if `x=2k`, then `x+2=2(k+1)` is even.

Therefore every reachable specified state is even.

### Finite tests

Test the concrete transitions

`0->2`,
`2->4`,
`4->6`.

All pass the invariant.

These tests alone do not prove all reachable states of an infinite transition system are even.

### Divergent implementation

Define implementation step

`impl(x)=x+2` if `x<6`,
`impl(x)=x+1` if `x>=6`.

The tested prefix is identical:

`0,2,4,6`.

The next state is

`7`,

which violates `Even(x)`.

Thus:

- the inductive proof is valid for the formal specification;
- the finite tests pass for the implementation prefix;
- the implementation fails to conform to the specification at `x=6`.

This is the chapter's central exact counterexample.

## Machine-checkable claim classes

Distinguish:

- static type checking;
- executable assertions/contracts;
- property-based testing;
- bounded/exhaustive finite checking;
- model checking;
- SMT/SAT-backed verification;
- proof-assistant theorem checking.

The chapter need not survey every tool.

It must preserve the different support classes and trust assumptions.

## Formal certification boundary

The word `certified` is overloaded.

The manuscript must distinguish:

- machine-checked theorem;
- verified implementation property;
- proof-carrying/certificate-checked result;
- institutional certification or governed authority state.

A proof assistant accepting a theorem is not automatically an institutional certification event.

This inherits REPLAY-001's authority separation.

## Downstream handoff

`ATLAS-CH-RESEARCHSM-001` may inherit:

- requirement/specification/model/proof/kernel/implementation distinctions;
- invariants and transition-system reasoning;
- machine-checking versus semantic-adequacy boundary;
- trusted-kernel/trust-base discipline;
- the rule that formal proof and replay are complementary, non-equivalent support routes.

It must independently define the research state machine, promotion gates, bounded work packages, actor roles, and authority transitions.

## Completion

Source lock, formal packet, exact witness, manuscript, ledger/register/bibliography updates, tranche receipt, green validation, implementation merge, bounded audit, audit merge, frontier recomputation, and controller reset are required.
