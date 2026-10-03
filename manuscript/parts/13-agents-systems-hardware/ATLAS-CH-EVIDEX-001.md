# Evidence Exchange and Zero-Context Work
<!-- ATLAS-CH-EVIDEX-001 -->

**Epistemic status:** provenance standards plus Atlas synthesis, bounded GCL project evidence, and exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-EVIDEX-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-EVIDEX-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-EVIDEX-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-EVIDEX-001.yaml

A result that is useful to its author can still be useless to everyone else.

The missing ingredient is often not intelligence.

It is transfer.

A proof sketch may depend on a source version that was never named.

An experiment may depend on a hidden environment choice.

A contributor may say "this works" without stating the exact claim, the domain on which it was tested, or the assumptions it used.

A second actor can receive the same words and reconstruct a different task.

At that point the problem is no longer only epistemic and no longer only coordinative.

It is an evidence-exchange problem.

The Atlas needs a way to move candidate evidence between actors while preserving enough identity, scope, provenance, and replay information that a later reader can determine what was actually done.

That is the subject of this chapter.

## 1. Evidence must survive handoff

The Evidence chapter gave us a claim-support packet

K = (q, tau, S, Omega, N, D).

The Coordination chapter gave us actors, channels, event identities, causal order, retries, and transaction boundaries.

Neither object by itself tells us how to package a bounded scientific or mathematical task for another actor.

That requires an interface.

The interface has two directions.

A dispatch says:

this is the exact obligation;

these are the facts you may import;

these are the sources and tools you may use;

these are the failure conditions;

this is the return grammar;

this is where the result must go.

A return says:

this is the dispatch I answered;

this is my strongest exact conclusion;

this is my support;

this is my provenance;

this is how to test or falsify it;

this is what remains unresolved.

Evidence exchange begins when both directions are explicit.

## 2. The dispatch packet

Write a dispatch as

D = (delta, Q, B, Sigma, C, Lambda, Gamma, rho).

Here delta is a stable dispatch identity.

Q is the exact bounded obligation.

B is the bootstrap: definitions, protected facts, and immutable imported-source identities.

Sigma is the allowed source and tool policy.

C is the context and independence class.

Lambda is the set of resource bounds, rejection conditions, and legitimate stop conditions.

Gamma is the exact return grammar.

rho is the durable return route.

This object is intentionally stricter than an ordinary instruction.

An ordinary instruction can rely on shared context.

A dispatch intended for independent work should not.

## 3. What zero-context actually means

"Zero context" can be misunderstood.

It does not mean the worker knows no mathematics.

It does not mean the worker has never seen the topic.

It does not mean the worker is statistically independent from every other actor.

It means the task itself should not depend on hidden conversational state.

Fix a declared class of eligible actors A.

Let H be hidden session history.

Zero-context sufficiency constrains the **authorized task contract**, not the worker's psychology.

Write

Contract_A(D,H)

for the obligation, premises, permissions, source policy, stop conditions, and return requirements that the protocol authorizes when D is accompanied by hidden history H.

Then require

Contract_A(D,H1)
=
Contract_A(D,H2)

for admissible hidden histories H1 and H2.

The exact obligation must be the same.

The imported facts must be the same.

The permitted sources must be the same.

The return grammar must be the same.

The stop conditions must be the same.

A worker can bring background knowledge and can still misunderstand an instruction.

What it cannot be authorized to obtain from hidden history is the missing half of the assignment.

## 4. Hidden context and explicit prerequisites

There is nothing wrong with prerequisites.

Science depends on them.

The problem is invisible prerequisites.

Compare two instructions.

First:

"Use the convergence theorem we discussed yesterday."

Second:

"Use Theorem T from source S at immutable version h, under hypotheses H1 through H4."

The second instruction can still be wrong.

It can name the wrong theorem.

Its hypotheses may not match.

But the dependency is inspectable.

The first instruction delegates part of the task definition to shared memory.

That works until the worker changes, the session ends, the conversation is unavailable, or two participants remember different versions.

Zero-context work therefore does not eliminate context.

It compiles relevant context into an explicit packet.

## 5. A dispatch is a boundary object

A good dispatch has to satisfy two constituencies.

The sender needs confidence that the worker is solving the intended problem.

The worker needs enough information to know what is allowed and what a valid return looks like.

This is why a dispatch should include excluded assumptions as well as imported facts.

Suppose a source proves a theorem for finite groups.

The target problem concerns compact groups.

If the dispatch lists only the finite-group theorem and says "generalize it," an actor may quietly assume the missing extension.

A better dispatch says:

finite-group theorem available;

compact-group extension unavailable;

do not import it.

The exclusion is not negative prose.

It defines the search space.

## 6. Source policy is part of the mathematics

Two actors can receive the same mathematical question and still be solving different assignments if one is allowed to search external literature and the other is restricted to a protected packet.

This is why Sigma belongs in the dispatch.

Possible source policies include:

protected packet only;

primary sources allowed;

public sources allowed;

repository-local sources only;

no external source use;

tools allowed but internet disallowed.

These are not administrative details.

They change what evidence can be introduced.

A zero-context dispatch must therefore tell the worker not only what the problem is, but what evidence universe it is allowed to draw from.

## 7. Context class is not a certificate of independence

Suppose a dispatch says

C = independent_blind.

That can mean the worker is not shown selected prior returns.

This may reduce anchoring or copying.

It may improve adversarial value.

But the label is weaker than the word independent sometimes suggests.

Two workers can use the same foundation model.

They can share training data.

They can share organizational assumptions.

They can unknowingly reproduce the same error.

They can even be the same model in separate sessions.

So an independence label should be read as an information-flow constraint.

What information was withheld?

What information remained available?

What provenance does the worker actually have?

That is more useful than pretending one adjective proves methodological independence.

## 8. The return object

Now write a return as

R = (delta, chi, K, Pi, V, Delta).

The first field, delta, links the return to the dispatch.

chi is the declared disposition.

K is the claim-support packet from the Evidence chapter.

Pi is provenance.

V contains verification and falsification hooks.

Delta is the unresolved residual or next bounded obligation.

This structure matters because a return is not merely an answer.

It is a candidate evidence object.

A phrase such as

PROVED

or

COUNTEREXAMPLE

inside chi does not make itself true.

The disposition tells the reviewer what the contributor claims to have returned.

Review remains a separate operation.

## 9. Provenance asks how an object came to exist

The W3C PROV family gives us a useful conceptual separation.

There are entities.

There are activities.

There are agents.

Entities can be generated by activities.

Activities can use entities.

Agents can bear responsibility for activities or generated objects.

Entities can derive from other entities.

This is exactly the kind of separation evidence exchange needs.

A return can therefore carry provenance like:

which input objects were used;

which actor or execution identity produced the return;

which procedure transformed the inputs;

which output entity was generated;

which derivation links connect the result to its sources.

The Atlas does not need to reproduce the entire PROV specification to benefit from the distinction.

The key lesson is that payload and lineage are different objects.

## 10. Provenance is not truth

A false result can have excellent provenance.

Imagine an arithmetic script that reads the exact intended file, runs under the exact pinned interpreter, records the exact command, and deterministically prints the wrong number because the code contains a bug.

Every provenance field can be correct.

The scientific claim can still fail.

This is an important boundary.

Provenance lets us ask:

where did this result come from?

It does not answer:

is this result true?

The second question requires verification, proof, replication, adjudication, or some other evidence operation.

Good provenance makes those operations easier.

It does not replace them.

## 11. Identity has layers

Evidence exchange often uses identifiers.

Not all identifiers answer the same question.

A filename answers:

what human-facing path or label was used?

A commit-and-path pair answers:

which repository version and file path?

A content hash answers:

which bytes?

A DOI may answer:

which scholarly object or version?

A bibliographic record answers:

which published source is intended?

These identities can reinforce one another.

They can also diverge.

Two files can have the same name and different bytes.

Two archives can contain identical bytes under different bibliographic descriptions.

A hash can identify bytes perfectly while saying nothing about what those bytes are supposed to mean.

So source locking should be designed around the failure mode.

If version drift matters, identify the version.

If bibliographic confusion matters, identify the work.

If byte identity matters, fingerprint the bytes.

## 12. A tiny ambiguity with an exact answer

The chapter's witness uses two source versions.

Both are called

inputs.txt.

Version one contains:

a=2

b=3.

Version two contains:

a=2

b=4.

The declared procedure is to add a and b.

The returned evidence bytes say:

result=5.

Now consider a handoff that records only

source_path=inputs.txt.

There are two candidate sources.

Replay version one and we obtain 5.

Replay version two and we obtain 6.

The returned result bytes alone do not tell us which source was used.

The provenance reconstruction is ambiguous.

Now add the exact SHA-256 of version one.

Within the finite candidate set, only one source matches.

Replay reproduces 5.

Nothing about the arithmetic became more intelligent.

The handoff became better identified.

## 13. Hashes solve one problem, not every problem

It is tempting to turn that witness into a slogan:

hash everything.

That would be too strong.

A hash is excellent for byte identity.

It does not tell us:

whether the source is authoritative;

whether the source corresponds to the bibliographic work we intended;

whether a PDF scan omitted a page;

whether an executable is safe;

whether a dataset was collected correctly;

whether a theorem's hypotheses match our use.

A strong evidence object can therefore need both content identity and semantic identity.

The source lock says what the object is.

The fingerprint says which bytes were inspected.

The authority field says what role the source is permitted to play.

These are separate claims.

## 14. FAIRness and exchangeability

The FAIR principles were written for scientific data management and stewardship, but several of their ideas apply naturally to evidence exchange.

Objects benefit from persistent identifiers.

Metadata should be rich enough to describe the object.

Metadata should explicitly identify the data or object it describes.

Objects should carry qualified references to related objects.

Reusable objects should carry detailed provenance.

The principles also explicitly extend beyond conventional data to algorithms, tools, and workflows.

This is useful for an Atlas concerned with machine-assisted research.

But FAIRness is not a truth metric.

A beautifully described, permanently identified, interoperable object can still be wrong.

FAIR improves the conditions for discovery and reuse.

Epistemic status remains separate.

## 15. Return grammars force useful omissions into view

Free-form prose is flexible.

That is both its strength and its weakness.

A contributor can return three pages of sophisticated reasoning and forget to say the exact theorem being claimed.

A return grammar reduces that ambiguity.

A useful grammar asks for:

the strongest exact statement;

the derivation or support;

assumptions beyond the bootstrap;

verification or falsification hooks;

the claim boundary;

the next residual.

These fields create friction.

That friction is useful.

It forces the contributor to distinguish what was shown from what merely seems plausible.

It also makes machine intake easier because important evidence fields have stable locations.

## 16. The return route matters

Suppose a worker produces a perfect result in a private transient chat.

A later reviewer never sees it.

Did the programme receive evidence?

Operationally, perhaps someone read it.

Durably, perhaps not.

When downstream review depends on a return, the transport should create a persistent identity.

That could be:

a versioned file;

an issue comment;

an append-only journal event;

a database record;

an object-store artifact;

another durable evidence surface.

The exact technology is secondary.

The requirement is that a later actor can identify the same return object.

Durability is therefore part of the evidence chain when later inspection matters.

## 17. Receipt is not acceptance

Evidence workflows become confused when arrival is treated as validation.

The Atlas distinguishes four states.

Receipt:

the return reached the declared surface.

Acceptance:

an intake or reviewer determined that it satisfies the structural or substantive contract required at that stage.

Promotion:

a stronger project object incorporates or relies on some claim from the return.

Certification:

a separate process confers whatever formal or institutional status certification means.

These are not synonyms.

A structurally valid counterexample can be accepted even though it defeats the hoped-for theorem.

A returned proof can be received and rejected.

An accepted proof can still require formal replay before promotion.

A promoted theorem can still lack machine-checked certification.

The state changes must remain explicit.

## 18. Structural validity is weaker than mathematical validity

A return can satisfy every field in the grammar.

The dispatch ID can match.

The provenance can be complete.

The claim boundary can be explicit.

The code can run.

The theorem can still be false.

Structural intake answers:

is this object well formed enough to review?

Mathematical or scientific adjudication answers:

does the evidence support the claim?

Those are different layers.

This distinction prevents a parser from accidentally becoming a theorem prover.

## 19. Replayability is graded

A result is not simply replayable or non-replayable.

We can pin different amounts of the execution.

Level one might identify the source and algorithm.

Level two might add exact code and parameters.

Level three might add package versions, random seeds, and expected outputs.

Level four might add environment/container identity and hardware-sensitive details.

Different claims require different levels.

A symbolic proof may care little about GPU model.

A floating-point kernel benchmark may care a great deal.

So a return should pin what is material to the claim, not maximize metadata without purpose.

The later Replayable Evidence Objects chapter develops this in more detail.

## 20. Zero-context work is compiled context

There is a useful way to think about the entire exercise.

A zero-context packet is not context-free.

It is context that has been compiled.

The sender begins with a large working context:

papers;

repository state;

conversation history;

prior failed attempts;

governance boundaries;

current theorem frontier.

Only part of that context is necessary for one bounded task.

The dispatch compiler extracts:

definitions;

protected facts;

forbidden imports;

source identities;

success criteria;

return grammar;

stop conditions.

The worker receives the minimal sufficient task interface rather than the sender's entire history.

This is an information-design problem.

Too little context produces ambiguity.

Too much context can leak prior answers, waste attention, or defeat blindness.

## 21. Why excluded assumptions are first-class

Imported facts tell the worker what is available.

Excluded assumptions tell the worker what must still be earned.

This is especially important in theorem work.

Suppose a source states convergence but leaves the topology implicit.

If a downstream theorem needs convergence in a stronger topology, the missing strength is the problem.

A dispatch that merely says

prove convergence

may invite the worker to restate the source.

A dispatch that says

source-level convergence is imported;

strong-topology convergence is not imported;

show the smallest additional estimate needed

defines a much sharper task.

Zero-context work is strongest when the boundary between granted and ungranted knowledge is explicit.

## 22. Falsification conditions make returns cheaper to judge

A work packet should not only say what success looks like.

It should say what would make a contribution unusable.

Examples:

uses a forbidden source;

requires an unstated assumption;

changes the theorem domain;

depends on an unpinned artifact;

exceeds the search budget;

returns only numerical evidence where proof is required.

These conditions improve efficiency.

They allow both worker and reviewer to stop early when the task contract has been violated.

This is the evidence-exchange analogue of an API rejecting an invalid input rather than producing an ambiguous output.

## 23. GCL as a bounded implementation example

The public MATHSOLVE repository contains a concrete implementation of this style.

Its zero-context dispatch template requires an exact bounded obligation, definitions, imported facts, excluded assumptions, permitted contribution types, falsification conditions, resource bounds, a return contract, and an authority boundary.

Its RESULT/1 grammar requires fields for the strongest exact statement, derivation, assumptions, verification or falsification hooks, claim boundary, and next residual.

A public Yang-Mills work packet marks itself

ZERO_CONTEXT

and

independent_blind,

restricts the worker to a protected packet, states explicit success criteria, and demands one structured result.

These are useful because they are not hypothetical.

They show how the abstract exchange object can be instantiated in a real research workflow.

They remain project evidence.

The Atlas does not claim that every research programme should use the same field names or protocol.

## 24. A return must point backward before synthesis can point forward

The dispatch ID delta is not administrative decoration.

It is the primary backward edge.

A return should tell us which obligation it answers.

Without that link, a result can be mathematically interesting and operationally orphaned.

The same is true of source identities.

Evidence should point backward to what generated it before a synthesis step points forward to new claims.

This creates a directed provenance structure:

sources and protected facts;

dispatch;

actor activity;

return;

review;

promotion.

Each edge can be inspected.

That is far safer than a narrative chain in which conclusions gradually detach from their inputs.

## 25. Synthesis is a new reasoning step

Suppose two independent returns arrive.

One proves a statement for domain Omega_1.

Another proves a related statement for Omega_2.

A controller cannot simply paste the prose together and declare a theorem on a larger domain.

For the special pointwise form

for every x in Omega_i, q(x),

two valid returns do justify q on Omega_1 union Omega_2.

That simple rule does **not** generalize automatically.

A global property, uniqueness statement, convergence mode, coupled hypothesis, or domain-dependent definition may require a new composition theorem.

Synthesis therefore has its own burden.

Are the proposition schemas identical?

Are the definitions aligned?

Do the hypotheses match?

Are the source versions compatible?

Does one argument depend on an assumption excluded by the other?

What logical rule licenses the combined domain?

The return objects make these questions visible.

They do not answer them automatically.

Synthesis is itself an evidence-producing activity.

## 26. Stronger prose requires stronger support

Evidence exchange should be monotone in a specific sense.

Passing through more hands must not strengthen a claim unless some new evidence or argument justifies the strengthening.

A contributor returns:

"I verified the property for n<=100."

A coordinator summarizes:

"the property appears robust."

A final report writes:

"the property holds."

The last sentence is stronger.

No new evidence appeared.

This is a promotion failure.

The Evidence chapter already gave us N, the set of stronger conclusions not licensed.

Evidence exchange preserves that field precisely to prevent confidence from increasing merely because an object travelled through a workflow.

## 27. Conflict is an admissible output

Independent work is valuable partly because returns may disagree.

If one contributor proves q and another returns a counterexample to q under the same stated assumptions, the correct evidence state is not

two votes for the average.

It is conflict.

The next operation may be:

compare source locks;

compare hidden assumptions;

replay the counterexample;

check the proof step;

send an adversarial packet;

narrow the theorem.

A good exchange protocol preserves contradictions until they are resolved.

It does not smooth them away for the sake of a clean dashboard.

## 28. Duplicate delivery and evidence identity

Coordination systems can retry.

That means the same logical return may appear more than once.

Two comments can carry the same result.

The same payload can be reposted by different actors.

A worker can retry after an uncertain transport failure.

So evidence intake needs stable logical identity.

The dispatch identity helps.

A return identity can help further.

Payload equality alone is not enough because two independent actors can legitimately return identical text.

Conversely, small formatting changes do not necessarily create a new logical result.

This is the evidence analogue of the Coordination chapter's distinction between delivery and effect.

## 29. Evidence exchange and memory

Evidence objects often become memory.

A returned proof can enter an archive.

A source lock can enter persistent memory.

A failed attempt can become episodic memory for later search.

A promoted theorem can become semantic project memory.

This creates a new boundary.

Storing a return does not promote it.

Retrieving it later does not revalidate it.

Memory preserves access.

Evidence status must travel with the object.

That is why provenance and epistemic class are not optional metadata in long-lived research systems.

## 30. Evidence exchange and agents

Agentic systems make these issues more urgent because delegation can happen quickly.

A parent agent can spawn several workers.

Each can search, compute, or prove.

Returns can arrive concurrently.

A summarizer can merge them.

Without explicit exchange semantics, the system can lose:

which worker used which source;

which result was independent;

which assumptions were shared;

which claim was only numerical;

which return was superseded;

which failure was never resolved.

The danger is not only hallucination.

It is provenance collapse.

A coordinated system can become less epistemically legible as it becomes more capable.

The exchange layer exists to resist that collapse.

## 31. Minimal handoff, not maximal paperwork

The goal is not to wrap every thought in bureaucracy.

A tiny task can have a tiny dispatch.

What matters is sufficiency.

If the task is

compute SHA-256 of these exact bytes

then the packet can be short.

If the task is

close the missing theorem-grade convergence bridge in a source with known omitted proofs

then the packet must be richer.

The metadata burden should scale with the ambiguity and consequence of the claim.

This is another form of adaptive computation:

spend evidence-handling effort where the epistemic boundary requires it.

## 32. What Replay may assume

ATLAS-CH-REPLAY-001 may assume:

stable dispatch and return identities;

immutable source/version identities;

the distinction between provenance and truth;

verification/falsification hooks;

graded replayability;

claim-boundary preservation.

Its job is to go further:

pin environments;

capture executable artifacts;

record exact outputs;

build semantic bridges from bytes to claims;

make replay itself a governed evidence object.

It need not rediscover why a mutable pathname is insufficient.

## 33. What the Research State Machine may assume

ATLAS-CH-RESEARCHSM-001 may later assume:

bounded work packages;

durable return routes;

context and independence declarations;

receipt versus acceptance versus promotion;

explicit residuals.

Its task is to arrange those objects into programme-level state transitions.

This chapter supplies the objects that move.

The state-machine chapter supplies the lifecycle.

## 34. The boundary to remember

Evidence exchange is successful when a result can leave one actor without losing the conditions under which it means what it means.

That requires more than copying text.

The obligation must have an identity.

The imported facts must be explicit.

The source universe must be declared.

The return must point back to the dispatch.

The claim must carry its scope and non-claims.

The provenance must identify how the object came to be.

The replay hooks must say how another actor can challenge it.

And no workflow step may promote the claim merely because the object moved successfully.

A good evidence packet therefore behaves like a scientific interface.

It says what goes in.

It says what may be assumed.

It says what comes out.

It says what the output does not establish.

And it leaves enough of a trail that another actor can disagree with it for the right reasons.

That is the purpose of zero-context work.

Not to remove context.

To make the necessary context explicit, bounded, portable, and inspectable.

## References used in this chapter

Exact source identities and authority scopes are pinned in:

sources/source-locks/ATLAS-CH-EVIDEX-001.yaml

The external basis includes W3C PROV-DM and the FAIR Guiding Principles.

The bounded implementation examples are exact public MATHSOLVE artifacts at commit 1273b75457f42da62a8af4c69493d44d293d4567.
