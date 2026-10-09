# Claims, Evidence, and Computational Witnesses
<!-- ATLAS-CH-EVIDENCE-001 -->

**Epistemic status:** Atlas documentary synthesis with one exact finite computational witness.  
**Specification:** manuscript/specifications/ATLAS-CH-EVIDENCE-001.md  
**Documentary packet:** mathematics/derivations/ATLAS-CH-EVIDENCE-001-DOCUMENTARY.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-EVIDENCE-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-EVIDENCE-001.yaml

A mathematical atlas does not merely contain statements. It tells the reader why some statements may be used as foundations, why others are observations, why still others are proposals, and where the boundary between them lies.

That distinction matters because polished exposition can make unlike things look deceptively similar. A theorem and a numerical plot may occupy adjacent pages. A conjecture may be written in notation as crisp as a proved result. A project record may contain exact hashes and still say nothing about whether the mathematics is true. A computational witness may be exact down to the last bit and still establish only a finite claim.

The first discipline of evidence is therefore separation.

A claim is one object. Its support is another. The interpretation placed on that support is another. The institutional state attached to the work is another.

The Atlas will often connect these objects. It must not fuse them.

## 1. Start with the exact claim

Before asking whether evidence is strong, ask what the evidence is supposed to support.

Compare:

- this matrix has spectral norm greater than one;
- this optimizer can amplify perturbations in this toy system;
- this training run exhibited a transient spike;
- non-normality caused the spike;
- non-normal transient amplification is prevalent in frontier training.

These statements are not interchangeable. They differ in object, quantifier, domain, and ambition. A calculation sufficient for the first may merely illustrate the second. An experiment relevant to the third may be suggestive but insufficient for the fourth. None automatically establishes the fifth.

Evidence becomes intelligible only after the claim is made precise enough to fail.

For that reason the Atlas treats claim identity as part of the scientific object, not as decorative prose wrapped around a result.

## 2. The claim-support packet

The chapter will use a compact documentary object:

\[
K=(q,\tau,S,\Omega,N,D).
\]

Its fields are:

q — the exact claim.

τ — the declared epistemic class.

S — the support objects or support routes.

Ω — the scope: hypotheses, domain, dataset, run, environment, version, numerical convention, or other boundary that controls where the support applies.

N — explicit non-entailments: stronger conclusions the support does not license.

D — downstream permission: what a later chapter may consume without silently strengthening the claim.

We write

\[
S \mathrel{\rightsquigarrow}_{\Omega,\tau}q.
\]

This means that \(S\) supports \(q\) within the declared scope \(\Omega\)
and epistemic class \(\tau\). This is a scoped evidentiary judgment, not a
logical entailment.

The arrow is intentionally not a symbol for logical entailment.

Sometimes the support route is a proof, and then a genuine logical relation can be stated. Sometimes it is a finite computation, an empirical observation, a source-locked public artifact, or a review record. These objects can support claims without all functioning as proofs.

The notation exists to prevent a common category error: treating every reason for belief as though it were the same kind of mathematical implication.

## 3. Eleven labels, not eleven rungs

The Atlas uses eleven canonical reader-facing epistemic classes.

| Class | What it records | What it does not create by itself |
|---|---|---|
| Definition | A stipulated mathematical or documentary object | External existence or empirical truth |
| Established Result | A result supported by appropriate external scholarly or formal authority | Permission to drop the source hypotheses |
| Atlas Derivation | A derivation carried out in this book from stated assumptions | External attribution or independent validation |
| Computational Witness | A reproducible symbolic, numerical, finite-search, simulation, graphical, or replay object | Proof or certification merely by being exact or reproducible |
| Observation | What was empirically or computationally observed under stated conditions | Universal mechanism or prevalence |
| Interpretation | A reasoned reading of results, observations, or witnesses | Replacement for the underlying evidence |
| GCL Public Project Evidence | A claim grounded in an exact public GCL artifact | Authority beyond what that artifact actually contains |
| GCL Programme | A research direction, hypothesis, remembered programme term, or planned construction | Public implementation or completed result |
| Conjecture | A substantive proposed claim not yet sufficiently proved | Established result |
| Open Problem | A precise unresolved question or target | Existence of a solution |
| Institutional Status | A governed state such as reviewed, accepted, superseded, adjudicated, or certified | Mathematical truth by status alone |

It is tempting to place these classes on a ladder from weak to strong. That would be a mistake.

A definition is not weak evidence; it is not evidence of that kind at all. An open problem is not a low-confidence theorem. Institutional status records a relation to an authority process, not a probability that a mathematical sentence is true. Interpretation sits on top of evidence without replacing it. Programme context can be valuable for choosing research directions while remaining deliberately barred from public implementation claims.

The vocabulary is therefore closer to a set of typed roles than to a single confidence score. The classes do not form a scalar ladder.

Within a particular role, support can certainly be better or worse. A proof can be correct or defective. An experiment can be well or poorly controlled. A source can be primary or remote. But those judgments do not turn the role taxonomy itself into one scalar order.

## 4. Definition is not discovery

Definitions are unusually powerful because they let a subject become precise.

Suppose the Atlas defines a boundary contract, a replayable evidence object, or a Residual. The definition can be exact and useful immediately. It can support derivations about any object satisfying the definition.

What it cannot do is establish that the defined object occurs in nature, in a deployed system, or in a frontier model.

This sounds obvious when stated explicitly. It is easy to forget when a definition is elegant.

A name gives a phenomenon a handle. It does not give the phenomenon empirical prevalence.

## 5. Established results and Atlas derivations

An established result enters the Atlas from an appropriate external scholarly or formal source. The source matters, but so do its hypotheses.

If a theorem holds for compact operators, smooth manifolds, convex objectives, independent samples, finite state spaces, or asymptotic limits, those conditions are part of the object being imported. Citation does not dissolve them.

An Atlas derivation is different. It is mathematics carried out in the book from declared assumptions or earlier results.

The distinction is not an insult to either class. It is provenance.

A correct Atlas derivation may be entirely rigorous. Its label tells the reader where the derivation was performed and where responsibility for the argument lies. If the same statement is later located in external literature, the source record can be enriched. The original derivation does not retroactively become someone else's result.

## 6. Computational witnesses

A computational witness is one of the Atlas's most useful evidence forms because many structures become visible only when symbolic, numerical, finite-search, graphical, simulation, or replay machinery is allowed to participate.

The rule is simple:

A witness must be as exact about its boundary as it is about its output.

Consider the elementary parity example recorded in ATLAS-CW-EVIDENCE-001.

We enumerate every integer from -10 through 10 and compute n(n-1) modulo 2 using exact integer arithmetic. Every residue is zero.

That computation establishes a complete finite statement:

for each of those 21 integers, n(n-1) is even.

It does not prove the universal statement:

for every integer n, n(n-1) is even.

The universal statement has a separate proof. Two consecutive integers have opposite parity, so one is even, and their product is even.

The witness and the proof agree on the tested values. They do different logical work.

This is the central discipline of computational evidence. Exactness protects the computation from one class of doubt. Reproducibility protects the reconstruction route from another. Neither property silently enlarges the domain of the claim.

### What a witness can be excellent at

A computational witness can:

- verify a finite family exhaustively;
- expose a counterexample;
- check an algebraic identity at a declared set of exact inputs;
- evaluate a numerical quantity under a stated convention;
- reconstruct an artifact from pinned sources;
- make geometry visible;
- replay a deterministic procedure;
- falsify a proposed universal statement with one valid counterexample.

### What a witness cannot acquire by presentation

A witness does not become a theorem because the plot is attractive.

It does not become independent replication because another process reran the same internal pipeline.

It does not become certification because CI is green.

It does not become causal explanation because the observed pattern matches an intuition.

The support route remains what it is.

## 7. Observation is not interpretation

An observation records what happened under stated conditions.

For example:

- a loss curve rose sharply at a particular step;
- one intervention reduced a measured quantity;
- a router changed assignments under a perturbation;
- an ablation changed test accuracy on a declared benchmark;
- a diagnostic statistic concentrated in a particular layer.

Interpretation asks what the observation means.

Perhaps the spike reflects transient amplification. Perhaps the intervention removed a mechanism. Perhaps the router statistic indicates specialization. These can be good interpretations. They are still interpretations.

The distinction is especially important when several mechanisms can produce similar observables.

A useful discipline is to ask whether another mechanism could produce the same observation. If yes, the observation may constrain the explanation without identifying it.

This is why later diagnostic chapters will need interventions, substitutions, controls, counterfactuals, and competing explanations. The evidence grammar comes first so those chapters can state exactly which inferential step each experiment supplies.

## 8. Public project evidence and programme context

Research programmes develop language faster than every idea becomes a stable public artifact.

The Atlas therefore separates two project-local classes.

GCL Public Project Evidence refers to an exact public object: a repository file, commit, artifact, result, or other inspectable object whose identity can be locked.

GCL Programme refers to a research direction, remembered term, planned construction, hypothesis, or context that is not being asserted as exact public evidence.

The distinction protects both.

Public evidence should not be weakened by mixing it with recollection. Programme context should not be forced into false certainty merely to make the prose sound complete.

A programme idea can motivate a chapter, suggest an experiment, or identify a useful open problem. It simply cannot be laundered into a statement that an implementation or result exists publicly when no exact public object has been bound.

## 9. Conjecture and open problem

A conjecture and an open problem are related but different.

A conjecture says: here is a substantive statement we suspect may be true.

An open problem says: here is an unresolved question or target.

A good research programme often contains both.

For example, one may conjecture that a certain invariant controls transfer, while the corresponding open problem asks for necessary and sufficient conditions under which reconstruction succeeds.

Precision does not demote either object. A conjecture can be mathematically sharp. An open problem can have a detailed attack plan. What remains forbidden is pretending that a plausible route is already a solution.

## 10. Institutional status is a different axis

The Atlas also records institutional states.

A result may be reviewed, audited, accepted, superseded, adjudicated, certified, or merged.

These states matter. They tell the reader what process the object has passed through and which authority made the decision.

But process state and mathematical truth are not synonyms.

Green CI may show that declared automated checks passed.

A documentary audit may show that source identities, scope statements, and manuscript claims agree.

A formal certificate may establish something much stronger if the certification authority and formal statement are themselves specified.

The error is not in having institutional status. The error is in allowing the status word to float free of the authority and checks that give it meaning.

The same discipline applies in reverse. A true mathematical argument can exist before any institution has reviewed it. Lack of institutional status is not a proof of falsehood.

## 11. Source identity is not source authority

A source lock answers two different questions:

1. Which exact object did the chapter consume?
2. What is that object authoritative for?

These fields must remain separate.

A commit hash can identify a README perfectly. That does not make the README a primary authority for a historical theorem.

A DOI can identify a paper perfectly. That does not make every sentence in later secondary commentary a theorem of that paper.

A source can therefore be perfectly pinned and still be insufficient for the claim being made.

This is why the Atlas rejects citation laundering. Precision of identity is necessary for reconstructability. Adequacy of authority is a separate judgment.

## 12. Promotion requires new support

Suppose a chapter begins with an Observation and later acquires a proof of a general theorem.

That is a legitimate promotion because the support changed.

Suppose instead that the observation is rewritten in more confident prose, placed in a polished figure, cited repeatedly, and merged after green CI.

Nothing epistemic has changed.

Presentation can reveal status. It cannot create status.

In the claim-support packet, a genuine promotion changes τ only when S and usually Ω change in a way that licenses the stronger q.

This yields a useful editorial test:

If the claim sounds stronger after revision, point to the new support object that justifies the stronger wording.

If no such object exists, the prose has outrun the evidence.

## 13. Five common promotion failures

### 13.1 Finite check to universal theorem

A finite exhaustive search proves a finite exhaustive claim.

It proves an infinite claim only when there is an additional argument reducing the infinite domain to the finite search.

Timeout is not a nonexistence proof. Large coverage is not an infinite quantifier.

### 13.2 Repeatable observation to universal mechanism

Repeated observation within one family improves confidence that the observation is stable in that family.

It does not alone prove that one mechanism caused it, that the mechanism is unique, or that the phenomenon is prevalent outside the tested regime.

### 13.3 Narrow proof to broad prose

A proof can be flawless and still fail to support the sentence written above it.

Typical causes include a wider domain, missing hypothesis, stronger quantifier, causal language, or an implicit approximation-to-exactness jump.

The cure is not to distrust proof. It is to align q with the theorem actually proved.

### 13.4 Precise citation to excessive authority

A source can be exact and still be the wrong kind of authority.

Source identity and source authority must both survive inspection.

### 13.5 Procedure to truth

CI, replay, review, audit, merge, adjudication, acceptance, and certification are procedural or institutional facts.

Each can support important claims about what was checked.

None may be treated as a generic truth operator.

## 14. What later chapters may now assume

Four architectural consumers depend directly on this chapter.

ATLAS-CH-DATA-001 — Data Quality, Mixtures, and Contamination may assume that empirical claims must retain dataset, mixture, benchmark, contamination, and run scope.

ATLAS-CH-MECHDIAG-001 — Mechanistic Diagnostics may assume the distinction between Observation and Interpretation and may require stronger interventions before promoting correlation to mechanism.

ATLAS-CH-EVIDEX-001 — Evidence Extraction and Claim Discipline may assume the claim-support packet and can refine it into operational extraction and adjudication procedures.

ATLAS-CH-EXPERIMENT-001 — Experiments as Arguments may assume that controls, ablations, counterfactuals, effect sizes, seeds, and reproducibility are support routes whose force depends on the exact claim and scope.

The handoff is deliberately modest.

Later chapters inherit the grammar. They do not inherit domain evidence they have not yet produced.

## 15. The durable habit

The strongest practical lesson of this chapter is a question sequence.

When encountering a technical statement, ask:

What exactly is the claim?

What class is it in?

What supports it?

Under what scope?

What stronger inference is not licensed?

What may a later chapter safely reuse?

If those questions can be answered, evidence becomes inspectable rather than atmospheric.

That is enough structure to let a large monograph combine theorem, derivation, computation, experiment, interpretation, programme, and governance without pretending they are the same thing.

## References used in this chapter

This chapter is a project-local documentary synthesis. Its load-bearing sources are exact Atlas governance and prerequisite objects pinned in:

sources/source-locks/ATLAS-CH-EVIDENCE-001.yaml

The chapter makes no claim that the Atlas taxonomy is a universal or uniquely correct theory of scientific epistemology.
