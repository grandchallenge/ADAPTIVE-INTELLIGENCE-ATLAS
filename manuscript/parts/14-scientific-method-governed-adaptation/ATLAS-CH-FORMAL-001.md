# Formal Methods and Machine-Checkable Claims
<!-- ATLAS-CH-FORMAL-001 -->

**Epistemic status:** established formal-methods foundations + audited replay/provenance prerequisite + Atlas synthesis + exact state-machine witness.  
**Specification:** manuscript/specifications/ATLAS-CH-FORMAL-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-FORMAL-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-FORMAL-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-FORMAL-001.yaml

Formal methods are powerful because they force us to say exactly what is being claimed.

They are also easy to overstate because a machine can check the wrong formal statement perfectly.

The central problem is therefore not only:

> can this theorem be checked?

It is also:

> what object was formalized, what semantics does it use, what does the proof actually range over, what trusted machinery checks it, and how is the formal result connected back to the intended system?

The governing distinction of this chapter is:

> machine-checked correctness is always correctness of a declared formal object under a declared trust base.

The semantic bridges around that object remain part of the scientific argument.

## 1. The formal support graph

Use the Atlas object set

`F=(R,S,M,P,K,I,W)`.

Here:

- `R`: intended requirement;
- `S`: formal specification/property;
- `M`: formal model and semantics;
- `P`: proof object, derivation, certificate, or model-checking result;
- `K`: trusted checker/kernel and surrounding trust base;
- `I`: implementation;
- `W`: deployed world or environment.

These objects should not be arranged as one untyped implication chain.

Instead, use typed obligations:

`Formalizes(S,R)`

asks whether the formal statement captures the intended requirement.

`Interprets(M,S)`

binds the statement to its formal semantics/model.

`Checks(K,P,S,M)`

records that checker `K` accepts support object `P` for the declared formal claim.

`Conforms(I,M)`

asks whether the implementation refines or conforms to the formal model strongly enough for the property being transferred.

`AssumptionsHold(W,M)`

asks whether the deployed world satisfies the environmental assumptions used by the model.

This graph prevents a common collapse.

A proof checker may establish `Checks`.

It does not automatically establish `Formalizes`, `Conforms`, or `AssumptionsHold`.

## 2. Formal specification is not human intent

Suppose the intended requirement is:

> the controller must never issue an unsafe command.

A formal specification might encode:

`forall reachable s, command(s) in SafeSet`.

That may be precise.

But perhaps the formalization omitted:

- a sensor failure mode;
- an actuator delay;
- an environmental transition;
- a unit conversion;
- an emergency override.

The theorem can be completely correct relative to its formal world and still fail to establish the real intended requirement.

This is not a defect peculiar to theorem provers.

It is the ordinary scientific problem of model adequacy expressed sharply.

Formalization moves ambiguity into explicit definitions.

It does not make interpretation disappear.

## 3. Hoare logic: contracts as proof objects

Hoare's axiomatic account of programming introduced reasoning in the form

`{P} C {Q}`

for command `C`, precondition `P`, and postcondition `Q` [@Hoare1969].

Under partial-correctness semantics, the triple means:

if `P` holds before execution and `C` terminates, then `Q` holds afterward.

For

`x := x+2`,

a useful triple is

`{Even(x)} x:=x+2 {Even(x)}`.

If

`x=2k`,

then after the assignment

`x'=2k+2=2(k+1)`.

The postcondition follows.

This small example contains the essential formal-methods pattern:

- state a contract;
- define semantics;
- prove the transition preserves the contract.

## 4. Invariants turn local preservation into global claims

Consider a transition system with:

- initial predicate `Init(x)`;
- next-state relation `Next(x,x')`;
- invariant candidate `Inv(x)`.

To prove that every reachable state satisfies `Inv`, establish:

1. initialization:
   `Init(x) => Inv(x)`;
2. preservation:
   `Inv(x) and Next(x,x') => Inv(x')`.

Then induction over the reachability derivation gives the global invariant.

This is different from observing many successful executions.

The proof quantifies over every reachable state admitted by the formal transition system.

## 5. Exact witness: an infinite-state counter

Let

`x_0=0`

and

`x_{n+1}=x_n+2`.

The claimed invariant is

`Even(x_n)`.

The base case is immediate:

`0=2*0`.

For the inductive step, if

`x_n=2k`,

then

`x_{n+1}=2k+2=2(k+1)`.

Therefore

`x_n=2n`

for every natural number `n`.

Every reachable specified state is even.

This is a universal statement over an infinite family of executions/states.

## 6. Three tests are not that theorem

Now test only:

`0 -> 2`,
`2 -> 4`,
`4 -> 6`.

All pass.

These tests establish exactly those executions.

They do not, by themselves, establish the universal invariant.

The difference is logical, not rhetorical.

A finite list of successful examples has the shape:

`P(x_1),...,P(x_m)`.

The invariant theorem has the shape:

`forall x in Reachable, P(x)`.

The quantifier changed.

An additional theorem is needed to bridge them.

## 7. A passing implementation can still be wrong

Define an implementation:

`ImplStep(x)=x+2` when `x<6`;

`ImplStep(x)=x+1` when `x>=6`.

Starting from zero:

`0 -> 2 -> 4 -> 6`.

The three tests pass.

The next transition is:

`6 -> 7`.

The invariant fails.

At exactly the same state, the specification says:

`6 -> 8`.

So three facts coexist:

1. the formal invariant proof is correct for the specification;
2. the tested implementation prefix passes;
3. the implementation does not conform to the specification.

This is the chapter's central exact counterexample.

## 8. Proof of specification is not proof of implementation

Suppose we prove:

`Even(x) -> Even(SpecStep(x))`.

That theorem says nothing directly about `ImplStep`.

To transfer the property, we need a bridge such as:

`ImplStep(x)=SpecStep(x)`

or a refinement relation strong enough to preserve the property.

Possible routes include:

- verified compilation;
- refinement proofs;
- equivalence proofs;
- code extraction;
- executable contracts;
- verified interpreters;
- constrained conformance testing.

Each route adds assumptions.

Formal methods do not remove bridges.

They make them inspectable.

## 9. Tests and proofs are complementary

Testing is not a weak version of proof.

It is a different support route.

Tests are excellent for:

- finding concrete counterexamples;
- exercising real implementations;
- regression checking;
- exposing integration failures;
- validating environment assumptions.

Proof is excellent for:

- universal claims over a formal domain;
- invariant preservation;
- exact algebraic properties;
- eliminating untested cases inside the formal model.

One failing test can refute a universal claim immediately.

Many successful tests usually do not establish the universal claim.

The asymmetry matters.

## 10. Exhaustive finite checking is stronger than sampling

Suppose a state space is genuinely finite.

If every reachable state is enumerated and every transition is checked, then a finite computation can establish a universal property over that finite model.

That is not the same as sampling.

The support route depends on:

- the exact finite model;
- transition semantics;
- completeness of exploration;
- property checked;
- correctness of the checker.

The word **finite** does not weaken the result.

It defines the result's domain.

## 11. Model checking

State-machine formal methods often write a system as:

- initial-state predicate;
- transition relation;
- safety properties;
- liveness/fairness assumptions where needed.

TLA+ is one mature framework for this style, and Lamport's *Specifying Systems* develops specification, safety/liveness reasoning, composition, and TLC model checking [@Lamport2002SpecifyingSystems].

A model checker can explore all reachable states of a finite model.

That can be an exact result about the model.

It is still not automatically a proof about arbitrary deployed code.

The implementation/model bridge remains separate.

## 12. The model can be the wrong model

Imagine a distributed protocol model with perfect channels.

The safety theorem may hold.

The deployed system may lose, duplicate, or reorder messages in ways omitted from the formal model.

The theorem is not thereby false.

Its assumptions are simply not the deployment assumptions.

This distinction is essential:

> a correct theorem with an inadequate model is still a correct theorem about the inadequate model.

Formal verification therefore strengthens the need for explicit model identity.

## 13. Trusted kernels

Proof assistants introduce another architectural distinction.

Robin Milner's LCF work established the influential pattern of a small trusted proof core surrounded by more complex proof-producing machinery [@Milner1979LCF].

The intuition is simple.

Tactics and automation may be sophisticated and buggy.

If they can only produce theorem objects through a small trusted interface, then bugs in automation should fail to manufacture accepted false theorems unless they compromise the trusted core or exploit assumptions already present in the logic.

This reduces the trusted computing base.

It does not eliminate trust.

## 14. Lean as a proof-assistant example

Lean is an interactive theorem prover based on dependent type theory with a small trusted kernel [@DeMouraEtAl2015Lean].

Its architecture separates convenient proof construction from final checking.

A user may rely on:

- notation;
- elaboration;
- type-class inference;
- tactics;
- automation;
- libraries.

The final elaborated object is checked by the kernel against the formal environment.

This is the key trust pattern:

> automation may be large while the final logical checker remains small.

## 15. Small trusted core does not mean no trust

Even a small kernel has assumptions.

A formal result can depend on:

- the type theory or logic;
- explicit axioms;
- the kernel implementation;
- imported definitions;
- library theorems;
- parser/elaborator behavior if not independently reconstructed;
- compiler/runtime/hardware when executing extracted code;
- external certificates or oracles.

So "Lean checked it" is meaningful but incomplete.

A mature statement says:

- which theorem;
- under which imports/axioms;
- in which toolchain;
- checked by which kernel;
- with what semantic bridge to the intended claim.

## 16. Proof terms versus theorem meaning

In a propositions-as-types setting, a proof term inhabits the proposition representing the theorem.

Kernel acceptance therefore establishes a precise syntactic-semantic fact inside the formal environment.

But theorem meaning still depends on the chosen definitions.

If a theorem formalizes:

`Safe := x<100`

while the intended policy meant:

`Safe := x<=10`,

the kernel may correctly prove the wrong policy.

Machine checking is strongest when formal statement identity is preserved alongside the proof.

This directly inherits the claim-identity discipline from REPLAY-001.

## 17. Replayable proof is stronger than an unpinned proof artifact

REPLAY-001 established that source, method, environment, output, and interpretation should be identity-bound.

Formal proof benefits from exactly the same discipline.

A proof artifact can depend on:

- theorem prover version;
- library revision;
- imported modules;
- generated code;
- solver version;
- external certificate format.

If those dependencies float, another actor may not be able to reconstruct the check.

Thus:

`formal proof`

and

`replayable formal proof`

are distinct documentary states.

## 18. Replay is not proof

The converse is equally important.

A program can reproduce the same wrong output forever.

A checker can replay a finite search exactly.

A build can remain byte-for-byte stable.

None of those facts automatically imply a theorem.

REPLAY-001 already established this boundary.

FORMAL-001 adds the complementary rule:

> proof and replay are orthogonal support dimensions.

A result can be:

- replayable but unproved;
- proved but poorly replayable;
- both;
- neither.

## 19. Executable checkers and proof objects

Not every machine-checkable result uses a proof assistant.

Some systems use compact certificates.

A producer may perform expensive search.

A smaller checker verifies the returned certificate.

Examples can include:

- SAT/SMT proof traces;
- primality certificates;
- optimization certificates;
- typed intermediate representations;
- proof-carrying code.

The epistemic advantage is architectural:

the producer can be less trusted if the checker fully validates the support object.

But the checker still validates only its declared relation.

## 20. Static types are formal claims with bounded scope

A type checker proves something.

What it proves depends on the type system.

A well-typed program may guarantee:

- certain operations receive values of the right form;
- some memory or effect discipline;
- absence of certain representation errors.

It does not automatically prove:

- business correctness;
- security policy;
- termination;
- liveness;
- numerical accuracy.

A formal mechanism should always be paired with its actual claim class.

## 21. Runtime contracts are path-local evidence

A runtime assertion such as

`assert even(x)`

can detect a violation on an executed path.

If the assertion never fires across many tests, that is useful evidence.

But unless all possible executions are covered or an additional theorem gives completeness, the assertion history remains execution-local.

This is another example of the quantifier discipline:

observed paths are not automatically all paths.

## 22. Property-based testing is still testing

Property-based testing can generate large numbers of structured inputs.

It often finds counterexamples that humans would not write manually.

This is valuable.

But if generation samples an infinite or enormous domain, passing campaigns remain sampling evidence.

If the generator is exhaustive over a finite domain, the claim class changes.

The difference should be stated, not implied.

## 23. SMT and SAT trust paths

Automated solvers are common inside formal methods.

There are several trust architectures:

- trust the solver directly;
- ask the solver to emit a proof trace;
- independently check the trace;
- reconstruct the result in a proof assistant;
- let an untrusted tactic invoke the solver and produce a kernel-checked term.

The phrase

> the solver proved it

does not tell us which architecture was used.

The trust path belongs in the evidence record.

## 24. Formal proof can expose missing requirements

One practical benefit of formalization is that it forces vague language into explicit predicates and transitions.

That process often reveals that the requirement itself was incomplete.

Questions emerge:

- What exactly counts as failure?
- Which state variables matter?
- Is liveness required or only safety?
- Is termination required?
- Which environment actions are possible?
- What fairness assumption is being made?

Formal methods therefore have value even before a theorem is completed.

They refine the question.

## 25. Invariants are contracts over evolution

In adaptive systems, invariants are especially useful because the system changes over time.

Examples include:

- a resource bound is never exceeded;
- authority never escalates without a permitted transition;
- provenance is never discarded during promotion;
- a representation remains normalized;
- a safety region remains invariant;
- an evidence state cannot jump directly from unreviewed to certified.

This prepares the next chapter.

Research processes themselves can be modeled as governed transition systems.

## 26. Safety and liveness are different

A safety property says, roughly:

> something bad never happens.

An invariant is a common safety-property form.

A liveness property says:

> something good eventually happens.

A system can be perfectly safe by doing nothing forever.

Therefore a governance or research state machine often needs both:

- forbidden transitions must never occur;
- legitimate work must still be able to progress.

Formal verification should not hide this distinction under one word such as **correct**.

## 27. Formal certification is overloaded language

The word **certified** can mean several things:

- a theorem was machine checked;
- a proof certificate was checked;
- an implementation property was verified;
- a compliance body issued a certificate;
- an institution promoted an artifact into an authoritative state.

These are different events.

The Atlas reserves the stronger authority language for the actual governed transition.

A proof assistant accepting a theorem is not automatically institutional certification.

## 28. Machine-checked does not mean assumption-free

A theorem can use axioms.

A theorem can rely on imported propositions.

A model can assume fairness.

A verified controller can assume bounded disturbance.

A proof can be exact while its premises are conditional.

The appropriate statement is therefore:

> theorem T is machine checked under assumptions A in formal environment E.

Conditional correctness is still correctness.

Its assumptions must remain visible.

## 29. The trust-base ledger

For a machine-checkable claim, record:

| Field | Question |
|---|---|
| requirement | What human/system claim is intended? |
| formal statement | What exact proposition/property was encoded? |
| semantics | What model gives the symbols meaning? |
| proof/check | What derivation, trace, model-check run, or certificate supports it? |
| checker | What validates the support object? |
| axioms/imports | What is assumed rather than derived? |
| toolchain | What exact version/environment is needed to replay checking? |
| implementation bridge | Why does the deployed artifact satisfy the formal model? |
| environment bridge | Why do real conditions satisfy formal assumptions? |
| authority | What review/certification state was actually reached? |

This ledger is the formal-methods analogue of REPLAY-001's evidence object.

## 30. Failure modes

### Proof-of-the-wrong-specification

A theorem is valid but the formal predicate omits the real requirement.

### Model-equals-system

A finite/abstract model is treated as identical to deployment.

### Tests-equal-proof

A passing finite suite is promoted into a universal claim.

### Automation-equals-trust

A tactic or solver is trusted merely because it is sophisticated.

### Kernel-equals-no-assumptions

A small trusted kernel is treated as eliminating axioms and semantic assumptions.

### Type-safe-equals-correct

A bounded static property is promoted into total system correctness.

### Machine-checked-equals-certified

A proof check is treated as an institutional authority transition.

### Formal-equals-replayable

A theorem artifact is accepted without pinning toolchain, imports, or source identity.

## 31. Why the exact witness matters

The counter witness is deliberately simple because the distinction is conceptual.

The invariant proof covers every specified reachable state.

The finite tests cover three implementation transitions.

The implementation then diverges.

Nothing subtle is happening.

The point is that all three evidence statements can be true simultaneously.

That makes the boundary hard to evade:

> proof, testing, and conformance are different relations.

## 32. Downstream handoff

**Research as a State Machine — ATLAS-CH-RESEARCHSM-001** may now assume:

- transition-system semantics;
- inductive invariants;
- initial/preservation proof obligations;
- safety versus liveness distinction;
- machine-checking versus semantic adequacy;
- trusted-kernel/trust-base discipline;
- replay and formal proof as complementary support routes;
- authority transitions as separate from theorem checking.

The downstream chapter must independently formalize:

- Forge -> Solve -> Cert;
- bounded work packages;
- independent actors;
- idempotence;
- promotion gates;
- failure/rollback states;
- authority transitions.

## References used in this chapter

- Hoare, *An Axiomatic Basis for Computer Programming* [@Hoare1969].
- Milner, *LCF: A Way of Doing Proofs with a Machine* [@Milner1979LCF].
- de Moura et al., *The Lean Theorem Prover (System Description)* [@DeMouraEtAl2015Lean].
- Lamport, *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers* [@Lamport2002SpecifyingSystems].

Exact source identities and authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-FORMAL-001.yaml
