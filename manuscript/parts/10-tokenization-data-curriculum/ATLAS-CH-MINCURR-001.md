# Minimal Curricula and Reasoning Bases
<!-- ATLAS-CH-MINCURR-001 -->

**Epistemic status:** audited Progress Search and Residual substrates + classical teaching/machine-teaching authority + Atlas-owned exact finite minimality witness.  
**Specification:** manuscript/specifications/ATLAS-CH-MINCURR-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-MINCURR-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-MINCURR-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-MINCURR-001.yaml

A curriculum can be useful without being minimal.

An experience can produce rapid learning progress without belonging to the smallest basis needed for a declared capability.

A later capability can be expressed without proving that an early mechanism survived.

Those are three different problems.

This chapter separates them.

The central question is:

> what is the smallest admissible early basis from which the capability we care about can be reconstructed?

The answer is always relative to a declaration.

## 1. Progress search is not yet minimality

Learning Progress as a Search Operator supplied a controller for where to look next.

It can use:

- learning-progress estimates;
- exploration;
- coverage state;
- delayed credit;
- finite horizons;
- generalization-state evidence.

That controller can find useful experience.

But it does not answer:

> which experiences are strictly necessary and jointly sufficient for the target capability?

That is the new question.

## 2. The Residual supplies the right discipline

The Residual already established that minimality is not meaningful in the abstract.

One must declare:

- the capability;
- admissible transformations;
- admissible descriptor class;
- reconstruction class.

MINCURR applies the same discipline to early experience and reasoning bases.

A “minimal curriculum” means minimal relative to a target and a reconstruction contract.

## 3. The smallest exact witness

Let:

\[
Q=\{q_1,q_2\}.
\]

Consider four possible capability hypotheses:

\[
H=\{h_{00},h_{01},h_{10},h_{11}\}.
\]

Each hypothesis is completely described by two outputs.

For example:

\[
h_{10}(q_1)=1,
\qquad
h_{10}(q_2)=0.
\]

Choose target:

\[
h^\star=h_{11}.
\]

The target capability therefore answers both probes with one.

## 4. A declared reconstruction rule

Use target-consistent labeled experiences:

\[
e_1=(q_1,1),
\]

\[
e_2=(q_2,1).
\]

For a finite set \(T\) of labeled experiences, first restrict it to the target probe family:

\[
T_Q=\{(q,y)\in T:q\in Q\}.
\]

Define the **target-relative** version space by

\[
V_H(T)=\{h\in H:\forall(q,y)\in T_Q,\ h(q)=y\}.
\]

An auxiliary experience with probe outside \(Q\) imposes no constraint on this reconstructor. This is a declared target-identification convention, not a claim that the experience is useless for learning other capabilities.

The reconstructor succeeds only when:

\[
|V_H(T)|=1.
\]

This is a very simple learner.

That simplicity is useful because the minimality proof can be exact.

## 5. Two examples are sufficient

Take:

\[
T^\star=\{e_1,e_2\}.
\]

The first example says:

\[
q_1\mapsto1.
\]

That removes:

\[
h_{00},h_{01}.
\]

The second says:

\[
q_2\mapsto1.
\]

Together the two examples leave only:

\[
\boxed{
V_H(T^\star)=\{h_{11}\}.
}
\]

The target is reconstructed exactly.

## 6. No strict smaller set works

With no examples:

\[
|V_H(\varnothing)|=4.
\]

With only \(e_1\):

\[
V_H(\{e_1\})
=
\{h_{10},h_{11}\}.
\]

With only \(e_2\):

\[
V_H(\{e_2\})
=
\{h_{01},h_{11}\}.
\]

Neither singleton identifies the target.

Therefore:

\[
\boxed{
|T^\star|=2
}
\]

is the exact minimum for this declared problem.

## 7. This is teaching-set minimality

Goldman and Kearns formalized teaching complexity through the size of sets that uniquely identify a target concept within a concept class [@GoldmanKearns1995Teaching].

The Atlas witness is a tiny exact instance of that idea.

The point is not that every curriculum problem is a teaching-dimension problem.

The point is that “minimal examples” becomes mathematically meaningful only after the target class and learner semantics are fixed.

## 8. Machine teaching makes the optimization direction explicit

Ordinary learning asks what the learner can infer from given data.

Machine teaching reverses the direction:

> given the learner and target, what training set should a teacher provide?

Zhu frames machine teaching as finding an optimal training set for a specified learning algorithm and target [@Zhu2015MachineTeaching].

MINCURR uses that inverse-design perspective without claiming that real neural learning is identical to the finite witness.

## 9. Minimality is conditional

Suppose we already knew the target belonged to:

\[
\{h_{10},h_{11}\}.
\]

Then one example:

\[
(q_2,1)
\]

would suffice.

The minimum has changed because the side information changed.

So:

\[
\boxed{
\text{minimality is relative to the declared hypothesis/capability problem}.
}
\]

## 10. Capability identity can be weaker than model identity

The finite witness uniquely identifies one hypothesis.

Real systems often do not require that.

Suppose two internal systems behave identically on the entire declared probe family.

Then capability reconstruction can succeed even if internal states differ.

This is the Residual connection.

A curriculum can be minimal for:

\[
\text{capability equivalence}
\]

without being sufficient to reconstruct the whole model.

## 11. Now add a high-progress distractor

Introduce an auxiliary experience:

\[
e_3=(z,1),
\]

where:

\[
z\notin Q.
\]

This auxiliary region is outside the declared target capability family.

Freeze progress scores:

\[
p(e_1)=1,
\]

\[
p(e_2)=1,
\]

\[
p(e_3)=5.
\]

So \(e_3\) is the most attractive region under a pure current-progress score.

## 12. But it tells us nothing about the target class

Because \(z\) is outside the target probe family:

\[
V_H(\{e_3\})=H.
\]

Therefore:

\[
|V_H(\{e_3\})|=4.
\]

The auxiliary experience leaves target ambiguity unchanged.

By contrast, either \(e_1\) or \(e_2\) cuts the target version space from four hypotheses to two.

## 13. Search value and basis value can disagree

We therefore have:

\[
p(e_3)>p(e_1),p(e_2),
\]

but:

\[
e_3\notin T^\star.
\]

So:

\[
\boxed{
\text{highest current learning progress}
\not\Rightarrow
\text{membership in a minimal reconstructive basis}.
}
\]

This does not make progress useless.

It says the two objectives are different.

## 14. Search asks where to learn next

A progress-search controller can ask:

> where is the learner currently changing fastest?

A minimal-basis analysis asks:

> what information or operation is necessary to reconstruct the declared target capability?

These questions can agree.

They do not have to.

## 15. Minimal set is not optimal sequence

The witness has one two-example set:

\[
\{e_1,e_2\}.
\]

Under the declared order-insensitive reconstructor, both orders:

\[
(e_1,e_2)
\]

and:

\[
(e_2,e_1)
\]

work.

Thus:

\[
\boxed{
\text{minimal set}
\not\Rightarrow
\text{unique optimal sequence}.
}
\]

Sequence optimization requires learner dynamics.

## 16. Why reasoning bases are harder than teaching sets

A teaching set is observable.

A reasoning basis is partly mechanistic.

We might want to say that broad capability was built from a small early collection of:

- operations;
- circuits;
- heuristics;
- primitives;
- subroutines.

But that claim requires more than showing that a small dataset was sufficient.

It requires evidence about what was acquired and what survived.

## 17. Four distinct questions

For a candidate early mechanism \(m\), ask separately:

1. was it acquired?
2. did it persist?
3. is it still accessible?
4. is it behaviorally expressed?

Those are different propositions.

## 18. Acquisition

Acquisition means we have evidence that mechanism \(m\) existed or was used during an early learning interval.

Possible evidence can include:

- a local mechanistic probe;
- a causal intervention;
- a decodable representation;
- a training-local behavior.

This is time-local evidence.

It does not tell us what happens later.

## 19. Persistence

Persistence means the same declared mechanism remains later.

That immediately raises an identity problem:

> what counts as “the same” mechanism?

Possible identity criteria include:

- matched functional signature;
- aligned mechanistic subspace;
- matched causal intervention effect;
- reconstructive equivalence under a declared map.

The identity criterion must be declared.

## 20. Acquisition does not prove persistence

A mechanism can be:

- overwritten;
- transformed;
- replaced;
- absorbed into another computation.

Therefore:

\[
\boxed{
\text{acquisition}
\not\Rightarrow
\text{persistence}.
}
\]

Longitudinal evidence is required.

## 21. Accessibility

A mechanism can persist without being reachable through the current interface.

It may be inaccessible to:

- the current prompt;
- routing;
- the active policy;
- the current readout;
- the current controller.

Therefore:

\[
\boxed{
\text{persistence}
\not\Rightarrow
\text{accessibility}.
}
\]

Accessibility is interface-relative.

## 22. Expression

A mechanism can be accessible but not normally expressed.

Another route may dominate.

The context may suppress it.

A controller may avoid it.

So:

\[
\boxed{
\text{accessibility}
\not\Rightarrow
\text{expression in every context}.
}
\]

## 23. Later expression does not prove early persistence

Suppose a later model succeeds on the same behavior.

That could happen because:

- the original mechanism persisted;
- it was relearned;
- a different mechanism replaced it;
- a compensating route emerged.

Thus:

\[
\boxed{
\text{later behavioral success}
\not\Rightarrow
\text{persistence of a particular early mechanism}.
}
\]

## 24. This matters for developmental narratives

It is tempting to tell a story:

> the model learned primitive \(A\) early, primitive \(B\) later, and broad reasoning emerged by composing them.

That story may be correct.

But behavior alone does not establish it.

A mechanistic developmental claim needs evidence at each link.

## 25. A minimal reasoning basis must specify composition

Suppose candidate operations are:

\[
r_1,\dots,r_k.
\]

A claim that subset:

\[
R^\star
\]

is sufficient requires an admissible composition class:

\[
\mathfrak M.
\]

Otherwise “reconstructable from the basis” is underspecified.

This is exactly the lesson inherited from the Residual.

## 26. Strict-smaller failure is essential

A set can be sufficient without being minimal.

To establish relative minimality, one must attack strict smaller candidates.

The finite witness does this exhaustively.

In a larger system, exact enumeration may be impossible.

Then the burden shifts to:

- lower bounds;
- adversarial ablations;
- impossibility arguments;
- certified search.

## 27. High progress can be auxiliary

The \(e_3\) control illustrates a practical danger.

An auxiliary task can be:

- rapidly improving;
- informative for representation learning;
- useful for exploration;

yet not belong to the minimal basis for the declared target capability.

The correct conclusion is not that \(e_3\) is worthless.

It is that usefulness is objective-relative.

## 28. Low progress can still be necessary

The converse can also happen.

An experience region can show little current progress because the learner already handles it well.

Yet it may still encode a constraint that is necessary to identify or preserve the target capability.

Therefore progress magnitude alone is not a necessity test.

## 29. Minimal basis can change with capability scope

A basis sufficient for:

\[
\mathcal Q=\{q_1,q_2\}
\]

may fail when the target probe family expands.

If we add:

\[
q_3,
\]

new examples or operations may become necessary.

Therefore:

\[
\boxed{
\text{minimal for one probe family}
\not\Rightarrow
\text{minimal for a broader capability}.
}
\]

## 30. Minimal does not mean unique

Many systems can admit several distinct minimal bases of equal size.

A curriculum study should distinguish:

- minimum size;
- one minimizer;
- all minimizers;
- equivalence classes of minimizers.

The Atlas witness happens to be unique only because its declared target example language is tiny.

## 31. Operational versus semantic reconstruction

A basis may semantically contain enough information to reconstruct a capability.

That does not mean an allowed learner can efficiently use it.

So MINCURR inherits the RESIDUAL distinction:

\[
\text{semantic sufficiency}
\neq
\text{operational accessibility}.
\]

A claimed basis should say what reconstruction class is allowed.

## 32. A general machine-teaching formulation

Let:

- \(L\): declared learner;
- \(\theta^\star\): target;
- \(\mathcal E\): admissible experiences;
- \(c(T)\): curriculum cost.

Then a teaching problem can be written:

\[
\min_{T\subseteq\mathcal E} c(T)
\]

subject to:

\[
L(T)=\theta^\star.
\]

For capability-relative reconstruction, replace exact parameter identity by:

\[
B(L(T),q)=B^\star(q)
\quad
\forall q\in\mathcal Q.
\]

The objective must say which notion is intended.

## 33. Early mechanisms require a longitudinal protocol

To claim an early reasoning basis persists, a study should freeze:

- early acquisition criterion;
- mechanism identity criterion;
- later persistence probe;
- accessibility interface;
- behavioral probe family;
- causal test where mechanism claims are made.

Then it should evaluate each separately.

## 34. A useful empirical disposition grammar

A future MINCURR experiment can distinguish:

### MINIMAL_RECONSTRUCTIVE_BASIS

A candidate basis is sufficient and every admissible strict smaller candidate is ruled out.

### SUFFICIENT_NOT_MINIMAL

The candidate reconstructs the target but minimality has not been shown or a smaller basis exists.

### SEARCH_RELEVANT_NOT_BASIS

An experience region is useful/high-progress but not required for the declared reconstruction target.

### PERSISTENT_INACCESSIBLE

A mechanism satisfies the declared persistence criterion but fails the current accessibility criterion.

### BEHAVIOR_ONLY

Later behavior is present without evidence identifying a persistent early mechanism.

This grammar prevents several common promotions.

## 35. The exact witness in one line

For the finite target:

\[
h^\star=(1,1),
\]

we have:

\[
V_H(\{e_1,e_2\})=\{h^\star\},
\]

but:

\[
|V_H(T)|>1
\]

for every strict smaller:

\[
T\subsetneq\{e_1,e_2\}.
\]

Meanwhile:

\[
p(e_3)=5
\]

is maximal while:

\[
V_H(\{e_3\})=H.
\]

That is the chapter’s core separation.

## 36. Non-implications

MINCURR rejects:

\[
\text{highest progress}
\not\Rightarrow
\text{minimal-basis membership},
\]

\[
\text{minimal for one target}
\not\Rightarrow
\text{universal minimality},
\]

\[
\text{minimal set}
\not\Rightarrow
\text{optimal sequence},
\]

\[
\text{acquisition}
\not\Rightarrow
\text{persistence},
\]

\[
\text{persistence}
\not\Rightarrow
\text{accessibility},
\]

\[
\text{later behavior}
\not\Rightarrow
\text{early-mechanism persistence},
\]

and:

\[
\text{behavioral equivalence}
\not\Rightarrow
\text{mechanistic identity}.
\]

## 37. Atlas connections

**Learning Progress as a Search Operator.**  
Progress can guide experience search without solving minimality.

**The Residual.**  
Task-relative sufficiency and declared reconstruction classes provide the minimality language.

**Mechanistic diagnostics.**  
Mechanism persistence needs longitudinal identity and causal evidence.

**Generalization-state dynamics.**  
Later behavioral state is evidence about behavior, not automatic evidence about which early mechanism survived.

**Compression and intelligence probes.**  
A minimal reasoning basis is related to compact reconstructive structure but is not identical to compression ratio.

## 38. Closing view

The smallest useful curriculum is not simply the region where learning is happening fastest.

And the smallest early basis is not automatically the mechanism that later behavior uses.

Minimality is a reconstruction claim.

Persistence is a longitudinal claim.

Accessibility is an interface claim.

Behavior is an expression claim.

The exact finite witness makes the first distinction formal:

\[
\boxed{
T^\star=\{(q_1,1),(q_2,1)\}
}
\]

is minimal for the declared target, while the highest-progress auxiliary experience contributes nothing to target identification.

The broader research programme begins when the same discipline is applied to learned operations:

> identify the smallest reconstructive basis, then separately test whether it was acquired, whether it persisted, whether it remains accessible, and whether later capability actually uses it.

## References used in this chapter

- [@GoldmanKearns1995Teaching]
- [@Zhu2015MachineTeaching]

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-MINCURR-001.yaml
