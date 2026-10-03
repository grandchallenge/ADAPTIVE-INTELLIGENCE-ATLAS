# ATLAS-CH-FORMAL-001 — Formal and Derivation Packet

## 1. Purpose

This packet separates the formal objects that are often collapsed into the sentence:

> "the system is formally verified."

The chapter uses the object set

`F=(R,S,M,P,K,I,W)`

for intended requirement, formal specification, formal model/semantics, support object, checker/kernel, implementation, and deployed world.

These objects do not form one linear implication chain.

The load-bearing relations are typed:

`Formalizes(S,R)`,
`Interprets(M,S)`,
`Checks(K,P,S,M)`,
`Conforms(I,M)`,
`AssumptionsHold(W,M)`.

A proof/check can establish the formal relation represented by `Checks` without thereby establishing semantic adequacy, implementation conformance, or environmental assumption validity.

## 2. Requirement versus specification

Let `R` be an informal requirement such as:

> the counter never enters an odd state.

Let `S` be the formal predicate:

`forall x, Reachable(x) -> Even(x)`.

Even if `S` is proved, there remains a semantic question:

does `S` capture the intended requirement?

Possible mismatches include:

- wrong state variable;
- wrong notion of reachability;
- omitted initialization condition;
- omitted environment transition;
- too-weak safety predicate;
- wrong units or domain.

Formal proof increases precision.

It does not automatically establish specification adequacy.

## 3. Hoare contracts

A Hoare triple is written

`{P} C {Q}`.

Under partial-correctness semantics, it states:

if `P` holds before command `C` and `C` terminates, then `Q` holds afterward.

For assignment

`x := x+2`,

consider the triple

`{Even(x)} x:=x+2 {Even(x)}`.

If

`x=2k`,

then after assignment

`x'=2k+2=2(k+1)`.

Therefore the postcondition holds.

This single-step contract is the preservation lemma used in the transition-system invariant.

## 4. Transition system

Define:

- state space `X=N`;
- initial predicate `Init(x) := (x=0)`;
- transition relation `Next(x,x') := (x'=x+2)`;
- invariant `Inv(x) := Even(x)`.

Define reachability inductively:

1. if `Init(x)`, then `Reachable(x)`;
2. if `Reachable(x)` and `Next(x,x')`, then `Reachable(x')`.

## 5. Inductive invariant theorem

To prove

`forall x, Reachable(x) -> Inv(x)`,

it is sufficient to establish:

### Base obligation

`Init(x) -> Inv(x)`.

Since the only initial state is `0` and `0=2*0`, the base holds.

### Preservation obligation

`Inv(x) and Next(x,x') -> Inv(x')`.

Assume `x=2k`.

By `Next`,

`x'=x+2=2k+2=2(k+1)`.

Therefore `x'` is even.

By induction on the reachability derivation, every reachable state satisfies the invariant.

This theorem is universal over all finitely reachable states of the declared transition system.

## 6. Closed-form reachable states

The deterministic transition system also admits the exact form

`x_n=2n`

for every `n in N`.

Proof by induction:

- `n=0`: `x_0=0=2*0`;
- if `x_n=2n`, then
  `x_{n+1}=x_n+2=2n+2=2(n+1)`.

Thus every reachable state is even.

The closed-form proof and the invariant proof support the same property by different derivations.

## 7. Finite testing

Suppose tests execute only:

`0->2`,
`2->4`,
`4->6`.

All observed states are even.

This establishes exactly that the tested executions satisfy the invariant.

It does not establish

`forall n in N, Even(x_n)`

unless an additional theorem connects the finite test set to all possible executions.

Testing is a powerful counterexample search.

Passing tests do not create universal quantification.

## 8. A divergent implementation

Define executable step function

`impl(x)=
  x+2, if x<6;
  x+1, if x>=6.`

Starting from zero:

`0 -> 2 -> 4 -> 6 -> 7 -> 8 -> 9 -> ...`

The first three transitions agree with the formal specification.

A finite test suite covering only those transitions passes.

At state `6`, the implementation transition differs:

formal specification:

`6 -> 8`;

implementation:

`6 -> 7`.

The invariant then fails.

This gives three simultaneously true statements:

1. the specification theorem is correct;
2. the finite tested prefix passes;
3. the implementation does not conform to the specification.

## 9. Proof of specification is not proof of implementation

Let

`SpecStep(x)=x+2`.

A proof of

`Even(x) -> Even(SpecStep(x))`

does not prove

`Even(x) -> Even(ImplStep(x))`

unless conformance

`ImplStep(x)=SpecStep(x)`

or another sufficient relation is established.

The missing object is the implementation/specification bridge.

Possible support routes include:

- refinement proof;
- verified compilation;
- code extraction from the formal model;
- executable contracts;
- equivalence proof;
- restricted conformance testing.

Each route carries its own assumptions.

## 10. Tests can refute universal claims

Although passing finite tests do not generally prove a universal property over an infinite domain, one failing test is enough to refute a universal claim when the test instance lies inside the quantified domain.

For the implementation above:

`x=6`

is a concrete counterexample to

`forall reachable x, Even(x)`.

Thus testing and proof are asymmetric:

- universal proof can establish all cases under its formal assumptions;
- one concrete counterexample can refute a universal statement;
- finitely many successes usually establish only those cases.

## 11. Finite exhaustive checking

If a model has a genuinely finite state space and every reachable state is exhaustively explored, then finite checking may establish a universal property over that finite model.

The support claim must include:

- finite model identity;
- transition semantics;
- exploration completeness;
- property checked;
- tool assumptions.

This is stronger than sample testing.

It remains a claim about the model being checked.

## 12. Model checking

A state-based formal specification often separates:

- initial-state predicate `Init`;
- next-state relation `Next`;
- safety property `Safe`;
- liveness/fairness conditions where relevant.

TLA+ provides one specification framework for this style.

A model checker such as TLC can explore reachable states for a model within its executable/finite constraints.

The important Atlas boundary is:

`model checked`

does not automatically imply

`deployed implementation verified`.

A conformance/refinement bridge remains necessary.

## 13. LCF-style trust architecture

Milner's LCF architecture introduced a crucial trust pattern:

- many proof procedures may be complex;
- theorem construction is mediated through a small trusted core;
- only values created through trusted inference primitives inhabit the theorem type.

This reduces the trusted computing base relative to trusting every tactic/search procedure.

It does not reduce trust to zero.

The kernel implementation and logical foundation remain trusted.

## 14. Lean trust architecture

The Lean system description and current official reference describe a theorem prover based on dependent type theory with a small trusted kernel.

In simplified terms:

1. a user writes declarations/theorem statements;
2. elaboration resolves syntax, implicits, coercions, notation, type classes, and metavariables;
3. tactics/automation construct proof terms;
4. the kernel checks the fully elaborated terms against the type theory and environment.

If automation generates an invalid proof term, kernel checking should reject it, assuming the kernel and surrounding trusted base behave correctly.

Thus automation can be large without all automation belonging to the trusted logical core.

## 15. Proof term versus theorem meaning

In propositions-as-types style systems, a proof term inhabits the proposition/type representing the theorem.

Kernel acceptance establishes:

- the term is well-typed under the formal environment;
- imported definitions/axioms have the meanings assigned inside that environment.

Kernel acceptance does not independently establish:

- that the formal proposition was the theorem the human meant;
- that imported axioms are appropriate for the application;
- that an implementation satisfies the model represented by the theorem;
- that physical measurements satisfy the formal assumptions.

## 16. Trust base accounting

A formal result should expose its trust base.

Depending on the support route, this may include:

- logic/type theory;
- axioms;
- kernel/checker implementation;
- parser/elaborator boundaries if not independently rechecked;
- library definitions/theorems;
- compiler/runtime;
- SAT/SMT solver if certificates are not independently checked;
- hardware;
- external oracle data;
- semantic formalization.

"Machine checked" is therefore incomplete without saying **what was checked by what**.

## 17. Executable checker versus proof object

An executable checker consumes a candidate object and decides whether it satisfies a defined relation.

A proof object encodes a derivation that a checker/kernel validates.

These can coincide in certificate-based systems, but they are not identical notions.

Examples:

- a primality certificate checked by a small verifier;
- a SAT unsat proof checked by a proof checker;
- a Lean proof term checked by the Lean kernel;
- a finite witness checked by repository CI.

The strength of the result depends on the statement the checker actually enforces.

## 18. Static types are formal but scoped

A type checker proves some property of the program representation under the language's type system.

For example, a well-typed expression may guarantee absence of certain classes of misuse.

That does not mean every semantic program requirement has been proved.

Type checking is a formal support route with a bounded claim class.

## 19. Contracts and runtime assertions

An executable assertion

`assert x % 2 == 0`

can detect a violation on an executed path.

If every transition is instrumented and every deployment path is observed, the evidence may be strong operationally.

It still differs from a static invariant proof.

A runtime assertion usually establishes:

- this execution reached or did not reach a violating state.

It does not automatically quantify over unexecuted futures.

## 20. Property-based testing

Property-based testing samples/generated inputs from a declared strategy and checks a property.

It can find counterexamples with high efficiency.

A successful campaign supports the tested/sample distribution.

It is not a universal proof unless the generator is exhaustive over a finite domain or another theorem supplies completeness.

## 21. SMT/SAT-backed verification

Automated solvers can discharge formal obligations.

The trust story depends on architecture.

Possible cases include:

- trust the solver directly;
- obtain a certificate/proof trace and check it independently;
- reconstruct a proof inside a proof assistant;
- use an untrusted tactic that produces a kernel-checked term.

Therefore "SMT proved it" is not yet a complete trust statement.

## 22. Specification bugs are formal bugs

A theorem can be exactly correct and operationally useless because the specification omitted the important property.

Examples:

- prove array indices are in bounds but omit confidentiality;
- prove message integrity but omit freshness;
- prove no deadlock in an abstract model that omitted a blocking subsystem;
- prove arithmetic safety for units interpreted incorrectly.

Formalization moves ambiguity.

It does not abolish the need to choose the right property.

## 23. Strong theorem, weak environment bridge

Suppose a controller is proved safe assuming sensor error

`|e|<=epsilon`.

The theorem may be perfectly machine checked.

If the deployed sensor can violate the bound, the theorem's assumptions do not hold in the world.

The failure is not in the proof.

It is in the bridge from environment `W` to formal assumptions `M/S`.

Formal certification must preserve that boundary.

## 24. Replay and formal proof are complementary

REPLAY-001 asks:

> can another competent actor reconstruct the support path?

FORMAL-001 asks:

> does a declared formal derivation establish a declared formal property under a declared trust base?

A formal proof can be poorly replayable if versions/dependencies are not pinned.

A replayable artifact can be mathematically wrong.

Combining both support routes is stronger than confusing either with the other.

## 25. Formal certification versus institutional certification

A phrase such as "formally certified" may refer to:

- proof assistant acceptance;
- certificate verification;
- verified implementation;
- compliance certification;
- institutional approval.

These are distinct authority/evidence states.

The Atlas reserves explicit terminology for the actual state attained.

A Lean theorem check is not, by itself, a GCL or regulatory certification transition.

## 26. Downstream interface

RESEARCHSM-001 may consume:

- transition systems;
- inductive invariants;
- machine-checkable transition predicates;
- trusted-kernel discipline;
- specification/implementation bridges;
- replay-versus-proof distinction;
- authority separation.

It must independently define its governed research-state transitions, actors, promotion gates, and idempotence rules.
