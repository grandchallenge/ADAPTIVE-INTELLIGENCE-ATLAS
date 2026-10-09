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


## 10. Advancement needs its own guard

Receipt and replay are evidence-state transitions.

Programme advancement is a different act.

For one finite model, define five Boolean conditions:

- `I(e)`: exact identity and provenance are valid;
- `S(e)`: the structural return contract is valid;
- `R(e)`: the required replay or check has completed;
- `A(e)`: adjudication supports the bounded claim;
- `D(e)`: the programme has issued an explicit advancement disposition.

Then define:

`G_adv(e)=I(e) S(e) R(e) A(e) D(e)`.

This is a deliberately strict finite witness.

It is not presented as the only possible research-governance formula.

## 11. A missing programme disposition keeps the gate closed

Evaluate:

`b=(1,1,1,1,0)`.

Then:

`G_adv(b)=0`.

The evidence may be well identified.

Its structure may be valid.

Replay may have succeeded.

Adjudication may even support the bounded claim.

The successor is still not authorized under this witness because programme disposition is absent.

This is exactly the distinction encoded by the public GCL Frontier Advancement Gate.

## 12. A complete witness vector opens the finite gate

Now evaluate:

`b'=(1,1,1,1,1)`.

Then:

`G_adv(b')=1`.

The arithmetic is trivial.

The semantic point is not.

A transition becomes legal because every declared condition is satisfied, not because the underlying prose sounds persuasive.

## 13. A missing required check also keeps the gate closed

Take:

`b_R=(1,1,0,1,1)`.

Then:

`G_adv(b_R)=0`.

A strong result statement cannot substitute for a required check that the governing process explicitly declared mandatory.

This is one value of machine-readable workflow state:

> missing conditions remain visible as missing conditions.

## 14. Advancement can be canonically idempotent too

Let:

`K_adv`

be the canonical set of evidence identities that have received the relevant advancement effect.

For identity `m`:

`K_adv union {m} union {m}=K_adv union {m}`.

So repeated exact application of the same advancement effect need not create a second canonical promotion.

The history may still record both attempts.

This matters whenever delivery, CI, merge automation, or network retries can repeat an otherwise valid event.

## 15. Idempotence is scoped, not magical

The word **idempotent** is easy to overuse.

This chapter means something narrow:

> a declared canonical mutation keyed by stable identity does not multiply its canonical effect when the exact same event is replayed.

It does not mean:

- two independent reviews must reach the same judgment;
- rerunning a stochastic experiment must return identical measurements;
- policy changes have no effect;
- a new result identity should be discarded.

Idempotence is a property of a specified operation.

## 16. Different evidence under one dispatch is not a retry

Return:

`r_A=(17,A)`

and later:

`r_B=(17,B)`.

Because:

`A != B`,

these are different immutable result identities.

The second object may:

- conflict with the first;
- strengthen it;
- supersede it under an explicit policy;
- address a different subclaim.

The transport layer should preserve that distinction instead of silently replacing one object by dispatch key.

## 17. Conflict is a scientific relation, not an intake shortcut

Suppose two preserved returns disagree.

The state machine should first preserve both identities.

Only then should adjudication decide the semantic relation.

This ordering matters:

`preserve -> compare -> adjudicate`

is different from:

`receive second -> overwrite first`.

The first route retains the evidence needed to understand disagreement.

## 18. Actor roles are not actor independence

Research workflows often name roles:

- contributor;
- reviewer;
- adjudicator;
- certifier.

Those labels are useful.

They do not prove independence.

Two differently named actors can share:

- information;
- incentives;
- training data;
- organizational control;
- hidden communication.

The chapter therefore treats independence as a governed relation, not a typography choice.

## 19. A narrow separation-of-duty predicate

Suppose one policy requires only that the producer and reviewer identities differ.

Define:

`Sep(a_prod,a_rev)=1{a_prod != a_rev}`.

Then:

`Sep(A,A)=0`

and:

`Sep(A,B)=1`.

This proves identity separation only.

It does not prove epistemic independence.

## 20. Same-actor review can fail a declared gate

If the governing policy requires:

`Sep=1`,

then a review by the same actor who produced the artifact does not satisfy that particular condition.

This is a policy statement, not a universal moral claim about self-review.

Self-review can still be valuable.

It simply does not substitute for a distinct-actor condition when such a condition has been explicitly required.

## 21. Certification is another state change

Certification should not be hidden inside words such as accepted, merged, green, or adjudicated.

Let certification state be coordinate:

`C`.

A certification transition has its own exact target, support requirements, and authority predicate.

For example:

`G_cert(o)=T(o) S_cert(o) H(o)`,

where:

- `T(o)` binds the exact target revision;
- `S_cert(o)` binds the required support state;
- `H(o)` binds the governing authority conditions.

A positive programme disposition does not automatically set certification state.

## 22. Exact target identity matters

A review of revision:

`r_1`

does not automatically certify later revision:

`r_2`.

If `r_2` changes the load-bearing artifact, the target identity has changed.

The state machine should bind evidence, replay, adjudication, and certification to the exact object they support.

This prevents stale evidence from leaking across revisions.

## 23. Forge, Solve, and Cert can be understood as authority compartments

The public GCL lifecycle controller records:

`MATHFORGE_TO_MATHSOLVE_TO_MATHCERT`

as an authority boundary.

At the level needed here:

- Forge fixes source/problem identity;
- Solve performs bounded work, evidence preservation, replay, and adjudication;
- Cert performs a distinct certification function.

The chapter does not claim this three-part split is universally optimal.

It uses the public workflow as one concrete example of authority compartmentalization.

## 24. Frontier advancement is not contributor authority

The public Frontier Advancement Gate makes one boundary explicit:

a contributor may return a next residual.

That residual is evidence.

It is not programme scheduling authority.

The programme separately chooses a disposition such as advance, independently verify, formalize, adversarially attack, source-block, refute, or close without successor.

This distinction prevents a useful contributor from silently becoming the scheduler of protected research state.

## 25. Independent-intelligence intake is an authority boundary

The public Controlled Epistemic Interface describes a narrow crossing:

`dispatch -> bounded contribution -> immutable intake -> separate adjudication -> protected route`.

Its compact boundary is:

`receive != believe != admit != certify`.

That is a state-machine statement.

Every verb denotes a different possible transition.

## 26. Zero-context is a work-context property

A bounded dispatch can be designed so that a contributor need not absorb the repository's local framing before attempting the task.

This can reduce one kind of institutional-context coupling.

It does not prove statistical independence, cryptographic independence, absence of shared pretraining, or absence of common mathematical culture.

The source itself makes this boundary explicit.

## 27. Fail closed means preserve protected state

Suppose a transition guard fails.

The default protected behavior in this chapter is:

> do not perform the protected canonical mutation.

That does not mean nothing happens.

The system may still append a failure receipt, capture diagnostics, open a repair issue, preserve a candidate artifact, or retry an allowed check.

Fail-closed promotion and active recovery are compatible.

## 28. Safety is not liveness

This distinction is essential.

A system can preserve every safety invariant and still make no progress.

Consider a state in which evidence identities remain correct, duplicate retries do not multiply effects, invalid transitions are blocked, certification remains protected, and the advancement disposition stays false forever.

No declared safety rule is violated.

Yet the claim never advances.

Safety answers:

> what bad transitions are forbidden?

Liveness answers:

> what good transition eventually occurs?

They need separate arguments.

## 29. A finite safety-without-liveness witness

Let the machine be in an adjudicated state with:

`D(e)=0`.

Suppose the only future event available is an exact retry that leaves:

`D(e)=0`.

Every retry is canonically idempotent.

Every protected invariant remains true.

But:

`eventually(advanced(e))`

is false on this execution.

That is enough to show:

> fail-closed safety alone does not guarantee progress.

## 30. Recovery needs typed classes

After a failure or block, "try again" is too vague.

At least five different operations should be distinguished.

### Retry

The same event/evidence identity is attempted again.

### New evidence

A different immutable result identity arrives.

### Supersession

A governed relation explicitly marks one artifact as replacing another for a declared purpose.

### Implementation repair

Tooling or workflow code changes while protected evidence identity remains intact.

### Policy change

The governing guard or authority rule itself changes through an authorized route.

These operations have different provenance and authority meanings.

## 31. Recoverable tooling failure is not scientific refutation

A CI outage, rate limit, parser defect, or transient connector failure does not by itself falsify the research claim.

Likewise, a mathematical refutation is not a tooling failure.

The state machine should type these failures differently.

This prevents infrastructure noise from silently becoming epistemic judgment.

## 32. Protected repair requires replay

If implementation code changes after a failed run, old execution evidence should not be relabeled as evidence for the repaired implementation.

The repaired artifact needs fresh replay at its new exact identity when the governing process requires it.

This is the operational form of:

> repair, then re-evaluate the repaired object.

## 33. Public lifecycle case study

The pinned GCL lifecycle controller records the concrete sequence:

`READY -> LAUNCHED -> RETURNED -> CAPTURED -> REPLAYED -> ADJUDICATED -> ADVANCED`.

It also records durable GitHub evidence, protected merges, allowed and prohibited actions, fail-closed behavior on identity/provenance mismatch, and event-driven advancement plus a recovery poll.

This is evidence that one real workflow can be encoded as a state machine.

It is not proof that every research programme should use the same states.

## 34. The case study also exposes authority limits

The same controller explicitly prohibits actions such as claiming mathematical correctness not established by Solve adjudication, MATHCERT certification, topology redesign, and direct protected-main pushes.

That is important.

A controller's permissions are part of its semantics.

Automation should be described not only by what it can do, but also by what it is forbidden to do.

## 35. State machines make authority inspectable

An informal workflow often hides authority in convention.

A typed transition machine can make authority explicit through event type, actor, target, guard, and permitted mutation.

This does not make governance automatically correct.

It makes the governance claim inspectable.

## 36. The machine does not prove the science

Suppose every lifecycle transition is valid.

That establishes workflow conformance.

It does not establish mathematical truth, novelty, completeness of review, absence of omitted premises, correctness of every human judgment, or adequacy of the governance policy.

Formal workflow correctness and scientific correctness remain different claims.

## 37. Machine state should not collapse scientific uncertainty

A programme may legitimately store unresolved status, conflicting evidence, source-blocked status, conditional support, falsification under one assumption, or an open question under another.

A state machine should preserve those distinctions.

Governance is not improved by forcing every question into a binary accepted/rejected flag.

## 38. Bounded work packages protect handoff quality

A work package is strongest when a new contributor can determine the exact target, premises, allowed sources, required output, return route, authority boundary, and stop condition.

That is why the bounded package belongs inside the state-machine chapter.

It is the unit on which safe delegation operates.

## 39. Independent actors need bounded interfaces too

Actor separation is useful only if the transferred work is well defined.

Otherwise two nominally independent contributors may solve different problems while appearing to review one another.

Stable identities and bounded work packages give the separation predicate something concrete to refer to.

## 40. Idempotence enables automation under retries

Distributed automation is rarely exactly-once at the transport layer.

Events can be delivered twice, retried after timeout, replayed after a crash, or awakened by multiple triggers.

Canonical idempotence allows those operational duplicates without multiplying protected effects.

That is one reason stable identity is not administrative decoration.

## 41. History should remain append-only where possible

An append-only history preserves failed attempts, retries, repairs, policy changes, and supersession events.

Canonical state can still expose the current protected interpretation.

The two views answer different questions.

Canonical state asks:

> what counts now?

History asks:

> how did we get here?

## 42. A practical research-state ledger

Before accepting a protected state change, record:

| Field | Question |
|---|---|
| work identity | Which exact bounded package is this? |
| target | Which exact artifact/revision is affected? |
| event type | Receipt, replay, adjudication, promotion, certification, or other? |
| actor | Who/what is attempting the transition? |
| evidence identity | Which immutable result is involved? |
| guard | Which conditions must be true? |
| authority | Who is permitted to perform this mutation? |
| canonical effect | What protected state changes? |
| history effect | What attempt/receipt is appended? |
| retry key | How are exact repeats recognized? |
| conflict rule | What happens to a different result under the same dispatch? |
| failure class | Tooling, evidence, policy, authority, or science? |
| recovery | Retry, repair, new evidence, supersession, or policy change? |
| certification | Is this a separate transition? |
| frontier effect | Who may authorize a successor? |

This ledger turns vague workflow verbs into inspectable state transitions.

## 43. Failure modes

### Done-as-one-state

Receipt, replay, adjudication, promotion, and certification are collapsed into one label.

### Retry-multiplies-authority

The same immutable result gains multiple effects because transport repeated.

### Dispatch-key-overwrite

A different result under the same work package silently replaces prior evidence.

### Replay-equals-truth

A successful execution is treated as proof of the surrounding scientific claim.

### Reviewer-label-equals-independence

Different role names are treated as evidence of independent judgment.

### Contributor-equals-scheduler

A suggested next residual is treated as authorization to advance the research frontier.

### Safe-equals-live

Fail-closed preservation is treated as proof the programme will eventually make progress.

### Repair-reuses-stale-evidence

A changed implementation is promoted using evidence bound to an older revision.

## 44. What the finite witness establishes

The companion witness proves only these exact finite facts:

- first capture of `(17,A)` creates one canonical evidence identity;
- exact retry leaves the evidence count at one;
- distinct result `(17,B)` raises the preserved count to two;
- advancement vector `(1,1,1,1,0)` evaluates to zero;
- advancement vector `(1,1,1,1,1)` evaluates to one;
- missing-check vector `(1,1,0,1,1)` evaluates to zero;
- repeated exact advancement has one canonical set-insertion effect;
- same-actor separation predicate `Sep(A,A)` evaluates to zero;
- a fail-closed execution can preserve all declared safety invariants while never reaching advancement.

It does not prove that the five-factor gate is universal or that identity-separated actors are epistemically independent.

## 45. Downstream handoff

**Governed Adaptation — ATLAS-CH-GOVADAPT-001** may now assume bounded work packages, product research state, canonical/history separation, exact-identity idempotent retry, duplicate/conflict distinction, guarded programme advancement, separate certification state, explicit actor-separation predicates, fail-closed safety versus liveness, typed recovery operations, and exact-target evidence binding.

It must independently answer the harder question:

> when a system is allowed to modify its own behavior, policy, tools, memory, or authority, which state-machine invariants and correction-capacity constraints must survive that adaptation?

## References used in this chapter

- Atlas prerequisite: *Replayable Evidence Objects* (`ATLAS-CH-REPLAY-001`) and its audited source lock.
- Atlas prerequisite: *Formal Methods and Machine-Checkable Claims* (`ATLAS-CH-FORMAL-001`) and `AUDIT-025`.
- GCL public lifecycle controller: repository `grandchallenge/MATH-PROGRAMME`, at immutable commit `fdd7a3fe3df7b2d699753347080c1cbc2127e02d`; source path `governance/openmath_unattended_lifecycle_controller.json`.
- GCL public Frontier Advancement Gate at the same protected commit.
- GCL public Controlled Epistemic Interface at the same protected commit.

Exact source identities, blob hashes, and authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-RESEARCHSM-001.yaml
