# Replayable Evidence Objects
<!-- ATLAS-CH-REPLAY-001 -->

**Epistemic status:** methodological synthesis grounded in reproducibility and provenance literature, exact GCL lifecycle records, and an executable Atlas replay package.  
**Primary figure:** \`ATLAS-FIG-REPLAY-001\`  
**Documentary packet:** \`mathematics/derivations/ATLAS-CH-REPLAY-001-DERIVATIONS.md\`  
**Computational witness:** \`mathematics/computational-witnesses/ATLAS-CW-REPLAY-001.md\`

## 1. A result should be reconstructable

A scientific result is often presented as a sentence:

> We found \(X\).

But the sentence is the end of a path.

Before the claim came:

- a source;
- a definition of the object;
- a method;
- code or derivation;
- an execution environment;
- an observation;
- an interpretation;
- some form of review.

If those links are lost, the claim may remain readable while the reason for believing it becomes opaque.

This chapter treats documentary provenance as part of the scientific object.

Its central distinction is:

\[
\boxed{
\text{replayability is a property of the evidence path}.
}
\]

Truth, verification, certification, and authority are separate properties.

They may depend on replay.

They are not created by replay.

## 2. The chain of custody

The useful allegory is a **chain of custody**.

An exhibit is useful only if its identity and transformation history remain traceable.

The correspondence is:

- evidence label ↔ stable artifact identity;
- custody record ↔ provenance chain;
- laboratory procedure ↔ replay method;
- analyst conclusion ↔ interpretation;
- formal disposition ↔ review or certification state.

The limit is essential.

Scientific truth is not determined by legal procedure.

Institutional acceptance is not mathematical truth.

A correct theorem can exist before any institution recognizes it.

A perfectly documented computation can still be wrong.

The allegory teaches traceability only.

## 3. Reproducibility, replication, and Atlas replay

Terminology matters because similar words carry different expectations.

The National Academies distinguishes **reproducibility** from **replicability**. Reproducibility concerns obtaining consistent computational results using the same data, computational steps, methods, code, and analysis conditions. Replicability concerns obtaining consistent results in a new study with new data [@NASEM2019Reproducibility].

The Atlas uses **replay** more narrowly:

> an identity-bound reconstruction of a specified evidence path.

Replay may be internal or external.

Replay may be deterministic or stochastic.

Replay can be exact at the byte level or approximate at a result level, provided the contract states which.

The term is local to the Atlas/GCL context.

It is not proposed as a replacement for broader scientific terminology.

## 4. A provisional evidence object

The Atlas uses

\[
\boxed{
E=(C,S,M,A,O,I,R)
}
\]

as an explanatory model.

The fields are:

\[
C
=
\text{claim identity and exact wording},
\]

\[
S
=
\text{source identities},
\]

\[
M
=
\text{method, derivation, code, or proof object},
\]

\[
A
=
\text{execution environment and artifact identities},
\]

\[
O
=
\text{observations or outputs},
\]

\[
I
=
\text{interpretation and claim boundary},
\]

\[
R
=
\text{review, replay, adjudication, or certification records}.
\]

The tuple is not a universal schema.

It is a checklist against a recurrent failure:

> “We reproduced it” without saying what “it” was.

## 5. Why claim identity comes first

Suppose two files contain the same output:

\[
86.
\]

One claim might be:

> this candidate has score 86 under evaluator \(E\).

Another might be:

> 86 is globally optimal.

The bytes are identical.

The claims are not.

The first may be supported by replaying an evaluator on an exact candidate.

The second requires a different argument entirely.

Therefore the evidence object begins with

\[
C,
\]

the exact claim.

A replay object without claim identity is a pile of artifacts waiting for someone to overinterpret it.

## 6. Source identity

A source should be identified strongly enough that another actor can recover the same object.

A mutable URL is often insufficient.

A branch name can move.

A “latest” tag can change.

A webpage can be edited.

A dataset can be refreshed.

Stronger identities include:

- immutable commit SHA;
- Git blob identity;
- content digest;
- DOI plus exact version where applicable;
- archived source snapshot;
- source manifest binding multiple objects.

Content addressing does not prove correctness.

It answers a narrower question:

> Are these the bytes we named?

That narrow answer is foundational.

## 7. Method identity

The method field \(M\) may contain very different kinds of support:

- a hand derivation;
- executable code;
- a proof assistant term;
- an experimental protocol;
- a finite search;
- a numerical solver;
- a statistical analysis;
- a symbolic computation.

The important point is not that every method becomes code.

It is that the method remains inspectable enough for its support role.

Sandve et al. give practical rules for reproducible computational research, including recording how results were produced and preserving exact intermediate and external information where needed [@SandveEtAl2013].

The Atlas extends that documentary instinct across computational and mathematical work.

## 8. Environment identity

A program is not executed in a vacuum.

Results may depend on:

- language version;
- library versions;
- compiler;
- architecture;
- precision;
- accelerator runtime;
- operating system;
- deterministic or nondeterministic kernels;
- external services;
- data state.

The necessary level of pinning depends on the claim.

A pure exact-integer computation may need little.

A floating-point distributed training run may need much more.

The goal is not maximal metadata for its own sake.

It is sufficient identity for the evidence path being claimed.

## 9. The tiny replay package

This chapter contains an actual executable witness.

The program

\`mathematics/computational-witnesses/replay_examples/deterministic_fraction_sum.py\`

computes

\[
\frac13+\frac16+\frac12
\]

using exact rational arithmetic.

The expected output is

\[
\boxed{\texttt{1/1}}.
\]

The program SHA-256 is

\`e6e841bfe975f283ab948c4f7f9bbbf5ba488d267fda36edc1b270d5dcd062c1\`.

The expected-output SHA-256 is

\`3117b181de4d46b7ff8adb4c78adec272c019160d4adf27a901e90ec114e1845\`.

The identity manifest records:

- code path;
- code hash;
- expected-output path;
- output hash;
- invocation;
- environment class;
- arithmetic model;
- claim boundary.

Atlas CI executes the program and compares the output byte-for-byte.

The mathematics is deliberately trivial.

The evidence mechanism is the object under study.

## 10. What successful replay establishes

For the tiny witness, successful replay establishes:

1. the committed program has the declared hash;
2. the expected output has the declared hash;
3. the program executes successfully in the CI environment;
4. its standard output matches the locked expected bytes.

That is a real result.

It does **not** establish:

- that every Atlas claim is reproducible;
- that the code implements some unstated theorem;
- that the program is independently reviewed;
- that the result is formally verified;
- that the result is certified.

A replay result should say exactly what passed.

## 11. A perfectly replayable wrong program

Imagine the program:

\[
\texttt{print("2+2=5")}.
\]

Its source can be hashed.

Its environment can be pinned.

Its output can replay perfectly forever.

It remains mathematically wrong.

This is the most important counterexample in the chapter.

Replay can establish faithful reconstruction of a computation.

It cannot turn a false computation into a true claim.

## 12. A correct argument that is not replayable enough

Now take the opposite case.

A mathematician writes a correct argument on paper, but the crucial source is cited only as:

> “the recent lemma from that preprint.”

The reasoning may be mathematically correct.

The documentary path may still be too weak for another actor to reconstruct efficiently.

Non-replayability does not imply falsehood.

It implies a provenance deficit.

This distinction prevents the Atlas from confusing documentation quality with truth.

## 13. Mutable dependencies

Suppose a replay instruction says:

> download \`model/latest\` and run the script.

Today, \`model/latest\` resolves to bytes \(A\).

Tomorrow, it resolves to bytes \(B\).

The name did not change.

The object did.

A replay instruction tied only to the mutable name has lost identity.

Pinning an immutable revision repairs the identity problem.

It still does not prove that the pinned artifact is the **right** artifact for the claim.

Identity and semantics remain separate.

## 14. Seed is not environment

For a stochastic experiment, a random seed is valuable.

It is not always sufficient.

A seeded computation can still differ because of:

- PRNG implementation;
- library changes;
- accelerator nondeterminism;
- thread scheduling;
- reduction order;
- mixed precision;
- compiler transformations;
- external data drift.

Therefore

\[
\boxed{
\text{seed}+\text{code}
\neq
\text{complete replay identity}
}
\]

in general.

The environment record should match the sensitivity of the evidence.

## 15. Byte identity is not semantic identity

Consider a program that checks a property for every integer

\[
1\le n\le100.
\]

Suppose:

- the code hash matches;
- the environment matches;
- the output hash matches;
- a second actor replays it successfully.

Now suppose the manuscript says:

> the property holds for every positive integer.

The replay is exact.

The claim is unsupported.

The failed object is the semantic bridge between observation \(O\) and interpretation \(I\).

That is why an evidence object must bind both.

## 16. Formal proof of the wrong statement

Formal verification is a powerful support route.

Suppose a proof assistant verifies a theorem

\[
T'.
\]

If the intended human claim was

\[
T,
\]

and the bridge

\[
T\leftrightarrow T'
\]

has not been established, then the formal proof does not automatically settle \(T\).

The kernel can be perfectly correct about the formal object while the human interpretation is wrong.

Formal verification therefore strengthens one part of the evidence path.

It does not abolish semantic review.

## 17. Finite verification generalized too far

A program may exhaustively check all cases in a finite set.

That can be an exact finite result.

If prose silently extends it to an infinite domain, the result has changed class.

For example,

\[
P(n)\text{ verified for }1\le n\le10^6
\]

does not entail

\[
\forall n\in\mathbb N,\;P(n).
\]

Exact finite verification is strong evidence for the finite statement.

It is not a continuum or universal proof unless an additional theorem supplies the bridge.

## 18. Internal replay is not independent reproduction

Suppose the same author:

- writes the code;
- runs the code;
- reruns the code;
- confirms the same output.

That is useful regression evidence.

It is not independent reproduction.

Independence changes epistemic value only when the relevant independence is real and documented.

Questions include:

- Did the second actor reuse the same implementation?
- Did they use the same hidden assumptions?
- Did they reconstruct the mathematics independently?
- Did they share the same data-generation error?
- Was the evaluation oracle independently derived?

“Independent” is itself a claim that needs provenance.

## 19. Provenance as a graph

W3C PROV provides a general model of entities, activities, agents, and derivation relations [@W3CPROVDM2013].

The Atlas specializes the idea into a scientific support path:

\[
\text{source}
\to
\text{method}
\to
\text{execution}
\to
\text{observation}
\to
\text{interpretation}
\to
\text{claim}.
\]

Review and authority transitions are separate.

![An exact declared graph with a solid evidence path from Source through Method, Execution, Observation, Interpretation, and Claim, followed by dashed separate transitions through Review or replay, Adjudication, and Certification.](../../figures/masters/ATLAS-FIG-REPLAY-001.png)

Every node and directed edge in the figure is declared in the figure manifest.

The layout is presentation.

The separation of edge classes is content.

## 20. Evidence edges versus authority edges

This distinction is worth making explicit.

An evidence edge says something like:

> this observation was produced by this execution.

An interpretation edge says:

> this observation supports this bounded claim under this reasoning.

A review edge says:

> this actor checked this aspect of the evidence path.

A certification edge says:

> under this institution’s rules, this exact revision reached this authority state.

These are different relations.

Collapsing them into one arrow marked “verified” destroys information.

## 21. Current GCL technical-writing doctrine

The current GCL technical-writing reference states a programme principle:

> technical communication is part of the research instrument.

Its writing invariants include:

- object identity;
- claim identity;
- bounded evidence;
- visible limitations;
- provenance;
- review specificity;
- authority separation;
- public inheritance;
- analogy discipline;
- fail-closed promotion.

The exact source is pinned in this chapter’s source lock to

\`grandchallenge/MATH-PROGRAMME@9c09521f0f7b1b7bbb2830b42f097f227f209d7d\`.

The Atlas uses that doctrine as a concrete institutional example.

It does not claim that every scientific organization must use GCL’s exact workflow.

## 22. Forge, Solve, Cert as role separation

GCL uses a Forge → Solve → Cert separation.

At a high level:

- **Forge** fixes source identity and problem/evidence context;
- **Solve** performs bounded mathematical or computational work and adjudication;
- **Cert** performs separate certification work under its own authority.

The value is not the names.

The value is that evidence production, problem solving, and certification are not silently treated as one operation.

This reduces one common failure mode:

> the actor that produced a result implicitly promotes it to whatever authority level is convenient.

Role separation makes that promotion explicit.

## 23. The current OPENMATH lifecycle

The source-locked current OPENMATH controller records:

\[
\texttt{READY}
\to
\texttt{LAUNCHED}
\to
\texttt{RETURNED}
\to
\texttt{CAPTURED}
\to
\texttt{REPLAYED}
\to
\texttt{ADJUDICATED}
\to
\texttt{ADVANCED}.
\]

Its durable substrate is GitHub task and evidence state.

Its return grammar is

\[
\texttt{GCL-CONTRIBUTION-RESULT/1}.
\]

Its authority boundary is recorded as

\[
\texttt{MATHFORGE\_TO\_MATHSOLVE\_TO\_MATHCERT}.
\]

Most importantly for this chapter, the controller explicitly prohibits itself from:

- claiming mathematical correctness not established by Solve adjudication;
- performing MATHCERT certification.

That is documentary evidence of authority separation, not merely a slogan.

## 24. Replay evidence can exist while certification remains false

A current source-locked MATHCERT OPENMATH intake contains:

- source authority;
- source lock;
- statement identity;
- evaluator contract;
- proof receipt;
- search receipt;
- replay receipt;
- candidate byte identity;
- independent-executor requirements.

It also records:

\[
\boxed{
\texttt{certification\_effect:false}.
}
\]

This is a particularly useful example because it blocks an easy conceptual collapse.

The presence of replay evidence does not itself create certification.

A certification transition is another event with another authority basis.

## 25. Fail closed

Suppose a replay requires:

- exact source identity;
- exact candidate identity;
- exact method identity;
- exact expected output.

If any of those identities disagree, the correct response is not to “approximately continue” while preserving the same status.

The support path has changed.

GCL’s current writing and OPENMATH doctrine uses a fail-closed pattern: identity or provenance mismatches block the applicable promotion.

That does not mean every scientific workflow must stop on every mismatch.

It means a workflow should not silently preserve an authority state whose prerequisites no longer hold.

## 26. Evidence object versus archive

An archive stores artifacts.

An evidence object stores relationships among artifacts and claims.

The difference is important.

A directory containing:

- \`result.csv\`;
- \`final.py\`;
- \`notes.md\`;
- \`plot.png\`

may be an archive.

It becomes stronger evidence when we can answer:

- Which code produced the CSV?
- Which source revision did the code use?
- Which rows support which claim?
- Which figure came from which data?
- What interpretation was applied?
- What review checked that interpretation?
- What version was actually certified?

Evidence is structured provenance plus bounded meaning.

## 27. The evidence object as a reconstruction test

The chapter’s acceptance test is simple:

> Can another competent actor reconstruct why we believe this, and can they see exactly what that reconstruction does not establish?

This is stronger than asking:

> Are all the files present?

It asks for an intelligible support path.

For a computational result, another actor should be able to reconstruct the computation.

For a derivation, another actor should be able to reconstruct the mathematical steps.

For a literature-dependent claim, another actor should be able to recover the exact source.

For an institutional status, another actor should be able to identify the exact authority record.

## 28. Five distinctions to keep visible

### 28.1 Replay versus truth

Replay means the evidence path can be reconstructed under its stated conditions.

It does not make a false method true.

### 28.2 Replay versus replication

Replay may reuse the same source, data, and method.

Replication asks a different question and may use new data or an independently rebuilt method [@NASEM2019Reproducibility].

### 28.3 Replay versus formal verification

Formal verification checks a formal statement under a formal trust base.

Replay reconstructs an evidence path.

Either may support the other.

They are not synonyms.

### 28.4 Replay versus certification

Certification is a governed disposition under some authority model.

Replay can be an input to certification.

It is not certification by implication.

### 28.5 Certification versus truth

Institutional certification is a status granted under defined rules.

It does not redefine mathematical truth.

The Atlas must keep epistemic and institutional categories separate even when they interact.

## 29. What a durable evidence object should make inspectable

A mature evidence object should make it possible to inspect:

- exact claim;
- source identities;
- source revisions;
- code or derivation identity;
- environment;
- input identities;
- output identities;
- figure/data lineage;
- assumptions;
- limitations;
- negative evidence;
- replay status;
- review scope;
- independence claims;
- adjudication state;
- certification state;
- supersession history.

Not every result needs every field.

But a missing field should be a conscious absence, not an accidental one.

## 30. Atlas connections

**Experiments as Arguments.**  
A controlled experiment becomes stronger when its exact support path can be replayed.

**Formal Methods.**  
Formal proofs can enter the evidence graph as machine-checkable support objects without collapsing the semantic bridge.

**Research as a State Machine.**  
Replay, adjudication, and certification become explicit state transitions.

**Governed Adaptation.**  
A system that changes itself needs provenance strong enough to know which evidence applies to which revision.

**Memory.**  
Institutional memory becomes more useful when it stores not only conclusions but also support paths.

The recurring Atlas shift is:

\[
\boxed{
\text{research result}
\longrightarrow
\text{replayable evidence object}.
}
\]

## 31. Closing view

A claim is easier to trust when the path behind it remains visible.

But visibility is not truth.

A replayable wrong program is still wrong.

A correct theorem with poor provenance can still be correct.

A formally verified narrow statement can still be misinterpreted.

A successful replay can still await independent review.

A result can be well supported and still uncertified.

The chain-of-custody allegory is only an allegory.

The evidence object is the object.

And the final test remains:

> Can another competent actor reconstruct why we believe this, and can they see exactly what that reconstruction does not establish?

## References used in this chapter

- [@NASEM2019Reproducibility]
- [@SandveEtAl2013]
- [@W3CPROVDM2013]

See \`sources/source-locks/ATLAS-CH-REPLAY-001.yaml\` for exact source identities, current GCL lifecycle records, and claim scope.
