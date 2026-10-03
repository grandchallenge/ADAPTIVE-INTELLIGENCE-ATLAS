# AUDIT-025 — Formal Methods and Machine-Checkable Claims

## Disposition

**PASS AFTER TWO SUBSTANTIVE REPAIRS**

ATLAS-CH-FORMAL-001 remains at `draft-v0.1`.

The chapter correctly separates formal specification, proof/checking, implementation conformance, environment assumptions, replayability, and institutional authority.

AUDIT-025 found two substantive defects and repaired both in the source artifacts:

1. the source lock treated Lean's mutable `latest` documentation endpoint plus an observed version/date as a load-bearing source identity. The endpoint changed version during the audit session. The mutable reference was removed from the load-bearing source set, manuscript citations, and bibliography; the immutable 2015 Lean system-description paper remains sufficient for the kernel-architecture claim;
2. the draft represented requirement, specification, model, proof, checker, implementation, and world as one linear chain. That wrongly suggested untyped relations such as checker-to-implementation. The chapter now uses an object set with typed obligations: `Formalizes`, `Interprets`, `Checks`, `Conforms`, and `AssumptionsHold`.

No invariant proof, Hoare-contract statement, exact witness arithmetic, testing boundary, trusted-kernel claim, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  `ea4b586d2b2c4a2e664345613ec7300c5e18ffda`;
- implementation PR:
  #107;
- audit issue:
  #108;
- duplicate audit issue:
  #109, closed as duplicate after a connector retry partially succeeded;
- chapter:
  `ATLAS-CH-FORMAL-001`.

## 1. Hard prerequisite

PASS.

The source lock binds:

- REPLAY manuscript blob:
  `4d95568d12ec0b27bcace910d8573f4a22e8b161`;
- REPLAY source-lock blob:
  `b373efe80e4ced13c7e060e5036d0012d2e17686`;
- joint keystone audit `AUDIT-003` blob:
  `9723fcb3dfa0111829b98f1c9bb416a13dbd714e`.

The chapter preserves REPLAY-001's central boundary:

replayability, truth, formal proof, certification, and institutional authority are distinct states.

## 2. External source identities

PASS AFTER PROVENANCE REPAIR.

Load-bearing sources are now stable bibliographic objects:

- Hoare (1969), axiomatic program reasoning;
- Milner (1979), LCF machine-assisted proof architecture;
- de Moura et al. (2015), Lean theorem-prover system description;
- Lamport (2002), TLA+ specification and model-checking framework.

The mutable Lean `latest` documentation URL is no longer used as load-bearing authority.

This repair is required by the inherited replay/source-identity discipline.

## 3. Formal support graph

PASS AFTER FORMAL REPAIR.

The chapter now uses the object set

`F=(R,S,M,P,K,I,W)`

for:

- intended requirement;
- formal specification/property;
- model/semantics;
- proof/check support object;
- checker/kernel;
- implementation;
- deployed world.

The relations are typed:

`Formalizes(S,R)`;

`Interprets(M,S)`;

`Checks(K,P,S,M)`;

`Conforms(I,M)`;

`AssumptionsHold(W,M)`.

A machine check may establish the declared `Checks` relation without establishing specification adequacy, implementation conformance, or environmental assumptions.

This is materially stronger and clearer than the original linear chain.

## 4. Requirement versus formal specification

PASS.

The chapter correctly states that a formal theorem can be valid while the formalized predicate fails to capture the intended requirement.

The semantic bridge from requirement to specification remains an explicit review obligation.

## 5. Hoare-style contract scope

PASS.

The manuscript uses

`{P} C {Q}`

under partial-correctness semantics:

if `P` holds and `C` terminates, `Q` holds afterward.

The assignment example

`{Even(x)} x:=x+2 {Even(x)}`

is correct.

The chapter does not silently promote partial correctness into a termination theorem.

## 6. Inductive invariant

PASS.

For:

- `Init(x): x=0`;
- `Next(x,x'): x'=x+2`;
- `Inv(x): Even(x)`;

the initialization obligation holds because zero is even.

The preservation obligation holds because

`x=2k => x+2=2(k+1)`.

Induction over finite reachability therefore proves every specified reachable state is even.

The equivalent closed form

`x_n=2n`

is also correct.

## 7. Testing versus proof

PASS.

The finite test prefix

`0->2->4->6`

establishes those concrete implementation executions only.

It does not establish the universal invariant over the infinite specified transition system.

The chapter also correctly states the asymmetric point:

one concrete counterexample inside the quantified domain can refute a universal claim.

## 8. Implementation/specification counterexample

PASS.

The implementation

`ImplStep(x)=x+2` for `x<6`;

`ImplStep(x)=x+1` for `x>=6`

agrees with the tested prefix and then maps

`6->7`.

The specification maps

`6->8`.

Thus:

- the specification proof is valid;
- the finite implementation tests pass;
- the implementation fails conformance;
- the implementation invariant fails at state 7.

The witness Claim boundary is correct.

## 9. Exhaustive finite checking

PASS.

The chapter distinguishes finite sampling from exhaustive exploration of a genuinely finite model.

A universal result over a finite model requires:

- exact model identity;
- transition semantics;
- complete reachable-state exploration;
- declared property;
- checker/tool assumptions.

The result is not promoted beyond that model without an additional bridge.

## 10. Model checking

PASS.

TLA+/TLC is used as a distinct formal-support route for state-based specifications.

The chapter does not identify a model-checking result with arbitrary deployed implementation correctness.

The implementation/model relation remains explicit.

## 11. LCF and trusted-kernel architecture

PASS.

The chapter accurately uses Milner's LCF architecture for the principle that complex proof-producing procedures can be placed outside a smaller trusted theorem-construction/checking core.

It also states that a reduced trust base is not a zero trust base.

## 12. Lean boundary

PASS.

The immutable Lean system-description source supports:

- dependent-type-theory foundation;
- interactive/automated theorem proving;
- small trusted kernel;
- fully specified proof objects/terms checked within the formal environment.

The manuscript does not claim:

- every theorem is axiom-free;
- every imported theorem is semantically appropriate;
- kernel checking proves human-intent adequacy;
- proof-assistant acceptance is institutional certification.

No Lean code artifact is required for this tranche because no FORMAL-001-specific Lean toolchain lock was declared.

## 13. Trust-base accounting

PASS.

The chapter keeps visible, where applicable:

- logic/type theory;
- axioms;
- checker/kernel implementation;
- imported definitions/libraries;
- solvers/certificates;
- compiler/runtime/hardware;
- external assumptions;
- semantic formalization.

Thus "machine checked" is not treated as an assumption-free status.

## 14. Replay versus formal proof

PASS.

REPLAY-001 and FORMAL-001 are complementary:

- replay asks whether the support path can be reconstructed under exact identity;
- formal proof asks whether a declared formal support object establishes a declared formal property under a declared checker/trust base.

The chapter correctly allows:

- replayable but unproved;
- proved but poorly replayable;
- both;
- neither.

## 15. Machine-checkable support classes

PASS.

The manuscript distinguishes, without treating them as equivalent:

- static typing;
- runtime contracts/assertions;
- property-based testing;
- exhaustive finite checking;
- model checking;
- SAT/SMT-assisted verification;
- proof-assistant theorem checking.

The chapter does not claim one universal hierarchy across all support purposes.

## 16. Formal versus institutional certification

PASS.

A machine-checked theorem, verified implementation property, checked certificate, compliance certificate, and governed institutional promotion are kept distinct.

This preserves the inherited authority-separation doctrine.

## 17. Integrity

PASS subject to audit merge validation.

The Chapter Ledger records FORMAL-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-FORMAL-LOCK-001`.

The bibliography closes all load-bearing manuscript citation keys:

- `Hoare1969`;
- `Milner1979LCF`;
- `DeMouraEtAl2015Lean`;
- `Lamport2002SpecifyingSystems`.

The stale `LeanReference2026` key is absent.

The exact witness contains an explicit Claim boundary.

## 18. Downstream handoff

PASS.

ATLAS-CH-RESEARCHSM-001 may inherit:

- typed formal-support relations;
- transition-system semantics;
- inductive invariants;
- safety/liveness distinction;
- trust-base accounting;
- replay/proof separation;
- implementation/model bridge discipline;
- authority separation.

It must independently define the research lifecycle, work-package states, actor roles, idempotence, promotion gates, failure states, and authority transitions.

## 19. Final disposition

AUDIT-025 passes after the two repairs above.

The durable formal-methods layer is:

**intended requirement --formalization--> formal specification/model; support object --checked-by--> trusted checker; implementation --conforms/refines--> model; world --satisfies assumptions--> model, with each bridge separately evidenced and replay-bound.**
