# Context Compilation
<!-- ATLAS-CH-CONTEXTCOMP-001 -->

**Epistemic status:** audited External-Memory Thesis + Atlas-owned finite context-compilation formalism and exact witness.  
**Specification:** manuscript/specifications/ATLAS-CH-CONTEXTCOMP-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-CONTEXTCOMP-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-CONTEXTCOMP-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-CONTEXTCOMP-001.yaml

A memory system can contain the right information and still hand the model the wrong working context.

The record can exist.

Retrieval can find it.

The ranker can score it highly.

The final prompt can still be stale, unauthorized, over budget, missing a mandatory record, stripped of provenance, or badly assembled.

This chapter treats that assembly step as a first-class transformation.

The governing claim is:

\[
\boxed{
\text{a model context is a compiled working set, not merely a prefix of retrieved text.}
}
\]

The word compiled matters because context construction has inputs, constraints, policy, failure modes, and a replayable output.

## 1. The external-memory handoff

The External-Memory Thesis established a hybrid architecture:

- some structure remains parametric;
- some information remains explicit and retrievable;
- external records can carry source, version, status, and supersession metadata;
- freshness is a policy question;
- correct storage is distinct from successful retrieval and use.

CONTEXTCOMP starts after retrieval has already produced candidates.

Its question is narrower:

> which candidate records should actually become the bounded working context of this invocation, and in what serialized form?

## 2. The pipeline

Write:

\[
M
\xrightarrow{\mathrm{retrieve}}
R_q
\xrightarrow{\mathrm{compile}_{\Pi,B}}
K_q
\xrightarrow{\mathrm{invoke}}
y.
\]

Here:

- \(M\) is external memory;
- \(R_q\) is the retrieved candidate set for query/invocation \(q\);
- \(\Pi\) is compilation policy;
- \(B\) is context budget;
- \(K_q\) is the compiled ordered working context;
- \(y\) is downstream model behavior.

Every arrow has different obligations.

## 3. Storage is not retrieval

A correct current record can be present in memory and never retrieved.

That is a retrieval failure.

It is not a compilation failure.

The compiler cannot select a candidate it never receives.

This distinction is inherited from EXTMEM-001 and its Retrieval prerequisite.

## 4. Retrieval is not compilation

A retriever may return:

- stale versions;
- duplicate keys;
- unauthorized records;
- many more records than the model budget permits;
- records whose metadata makes them mandatory;
- records useful for ranking but invalid under the current invocation policy.

The candidate set is therefore an input to compilation.

It is not yet the context.

## 5. Ranking is one signal, not the whole contract

A retrieval rank can express one notion of relevance or similarity.

It does not automatically encode:

- current version;
- authorization;
- mandatory policy;
- provenance requirements;
- atomic serialization cost;
- conflict state.

This chapter's exact witness makes that distinction literal.

The top-ranked policy record is stale.

The current mandatory policy ranks third.

A rank-only prefix fails.

## 6. Candidate records

Represent a candidate record as

\[
r_i=
(k_i,v_i,\sigma_i,p_i,a_i,m_i,\rho_i,c_i,u_i,t_i).
\]

The fields are:

- logical key;
- version;
- status;
- provenance/source;
- authorization;
- mandatory flag;
- retrieval rank;
- compiled cost;
- declared compiler utility;
- type.

This is a chapter-local formal object.

It is not proposed as a universal context format.

## 7. Compiled cost includes metadata

Suppose the payload itself costs

\[
d_i
\]

units.

Suppose required metadata costs

\[
h_i.
\]

Then the actual compiled cost is

\[
c_i=d_i+h_i.
\]

If the system budgets only the payload while still requiring provenance in the prompt, its budget calculation is wrong.

The resource accounting must describe the object actually serialized.

## 8. Provenance is not decoration

The External-Memory Thesis made source/version identity explicit.

Context compilation should not throw that information away casually.

For the finite formalism, serialize each included record with an envelope:

\[
E(r_i)
=
[\mathrm{id},\mathrm{key},\mathrm{version},\mathrm{source},\mathrm{status},\mathrm{payload}].
\]

The envelope lets the working context say not only what was included, but which version and source were included.

That does not prove the source is true.

It preserves identity.

## 9. Authorization comes before optimization

Suppose a retrieved record is highly ranked and appears highly useful.

If the invocation is not authorized to use it, the compiler must exclude it.

Authorization is therefore modeled as a hard admissibility filter:

\[
a_i=1.
\]

It is not a utility bonus.

The compiler cannot trade privacy or authority against a few extra utility points.

## 10. Freshness comes before optional utility

Suppose two records share logical key policy:

- version 1 is superseded;
- version 2 is current.

If the declared policy is latest-current, version 1 is removed before optional selection.

This remains true even if version 1 has:

- better retrieval rank;
- higher declared utility;
- lower compiled cost.

A validity constraint is not a soft preference.

## 11. Unresolved conflict is a failure state

Now suppose two authorized records for the same logical key are both marked current.

If the version policy does not say which wins, the compiler should not silently guess.

It should return:

\[
\mathrm{VERSION\_CONFLICT}.
\]

Choosing the higher retrieval rank would be a new policy.

If that policy is desired, it must be declared.

## 12. Mandatory records

Some records are not optional under a particular invocation contract.

Examples can include:

- current governing policy;
- task instruction;
- safety constraint;
- required schema;
- experiment identity.

Let

\[
M
\]

be the mandatory set.

Its total cost is

\[
C_M=
\sum_{r_i\in M}c_i.
\]

This cost is paid before optional context is selected.

## 13. Mandatory overflow

If

\[
C_M>B,
\]

no atomic context can both:

- contain every mandatory record;
- fit the budget.

The correct output is explicit failure:

\[
\boxed{
\mathrm{MANDATORY\_OVERFLOW}.
}
\]

The compiler should not make a mandatory rule half-visible merely to keep the invocation running.

## 14. Optional selection

After authorization, freshness, conflict resolution, and mandatory inclusion, let \(O\) be the optional records.

Residual budget is:

\[
B'=B-C_M.
\]

This chapter uses the finite objective:

\[
\max_{S\subseteq O}
\sum_{r_i\in S}u_i
\]

subject to:

\[
\sum_{r_i\in S}c_i\le B'.
\]

This is a declared compiler objective.

It is not a definition of true context usefulness.

## 15. Utility is policy input

The score

\[
u_i
\]

can come from:

- a heuristic;
- a learned scorer;
- a human rule;
- a task-specific policy.

The finite chapter does not care where it came from.

It only proves which subset is optimal relative to those declared scores.

Therefore:

\[
\boxed{
\text{utility-optimal under }\Pi
\not\Rightarrow
\text{universally optimal context}.
}
\]

## 16. Determinism

If several feasible subsets have equal utility, the compiler needs a tie-break if exact replay matters.

This chapter uses:

1. lower total cost;
2. lexicographically smaller stable record-ID list.

The choice is arbitrary but explicit.

Determinism turns the same inputs into the same compiled result.

## 17. Serialization is part of compilation

A selected set is unordered.

A model context is ordered.

Therefore compilation is not finished when subset selection ends.

The finite policy uses:

\[
\text{policy}
\prec
\text{evidence}
\prec
\text{detail}
\prec
\text{background}.
\]

Within a type, stable record IDs break ties.

No empirical claim is made that this order is universally best for language models.

It is simply part of the declared context object.

## 18. The exact budget-8 witness

Use context budget:

\[
B=8.
\]

The retrieved candidates are:

| ID | key | status/version | rank | cost | utility | mandatory |
|---|---|---|---:|---:|---:|---|
| \(r_{p1}\) | policy | superseded v1 | 1 | 3 | 9 | no |
| \(r_f\) | task_fact | current v1 | 2 | 4 | 7 | no |
| \(r_{p2}\) | policy | current v2 | 3 | 4 | 8 | yes |
| \(r_b\) | background | current v1 | 4 | 2 | 3 | no |
| \(r_d\) | detail | current v1 | 5 | 3 | 5 | no |

All records are authorized.

The current policy v2 supersedes v1.

## 19. Freshness removes the rank-1 policy

The latest-current policy excludes:

\[
r_{p1}.
\]

That record had retrieval rank \(1\).

It also had declared utility \(9\).

Neither fact can override its superseded status under this policy.

Remaining records:

\[
r_f,r_{p2},r_b,r_d.
\]

## 20. Mandatory policy consumes half the budget

The current policy v2 is mandatory.

Its cost is:

\[
4.
\]

Residual budget:

\[
8-4=4.
\]

The optional candidates are:

\[
r_f:(4,7),
\]

\[
r_b:(2,3),
\]

\[
r_d:(3,5).
\]

Each pair denotes:

\[
(\text{cost},\text{utility}).
\]

## 21. Exhaustive finite selection

Under residual budget \(4\), feasible optional subsets are:

\[
\varnothing,
\]

\[
\{r_f\},
\]

\[
\{r_b\},
\]

\[
\{r_d\}.
\]

Their utilities are:

\[
0,7,3,5.
\]

Every two-record optional subset costs more than \(4\).

Therefore the unique optimum is:

\[
\boxed{
S^\star=\{r_f\}.
}
\]

## 22. The compiled set

Add the mandatory current policy:

\[
\boxed{
S_{\rm final}
=
\{r_{p2},r_f\}.
}
\]

Total cost:

\[
4+4=8.
\]

Total declared utility:

\[
8+7=15.
\]

The serialized context places:

1. current policy v2;
2. task evidence.

Both retain provenance metadata.

## 23. What the witness actually proves

It proves an exact finite statement about a declared compiler.

It proves:

- which candidate is stale;
- which record is mandatory;
- which optional subsets fit;
- which feasible set maximizes declared utility;
- which records are serialized;
- exact cost;
- exact declared utility.

It does not prove that a language model will answer correctly.

## 24. The naive rank-prefix control

Now ignore freshness and mandatory semantics.

Take candidates by retrieval rank until the next record does not fit.

First:

\[
r_{p1}
\]

costs \(3\).

Then:

\[
r_f
\]

costs \(4\).

Cumulative cost:

\[
7.
\]

The next candidate is current mandatory policy v2 with cost \(4\).

It cannot fit.

The rank-prefix result is:

\[
\boxed{
\{r_{p1},r_f\}.
}
\]

## 25. Why the rank prefix is invalid

It contains:

\[
r_{p1},
\]

which is superseded.

It omits:

\[
r_{p2},
\]

which is current and mandatory.

Therefore the result fails the declared compiler contract twice.

This is an exact counterexample to:

\[
\boxed{
\text{high retrieval rank}
\Rightarrow
\text{valid working context}.
}
\]

## 26. Truncating the policy is not a repair

After the rank prefix, one budget unit remains.

The current policy record costs \(4\).

If the compiler cuts the record into a one-unit fragment, it no longer has the declared atomic object.

The fragment can lose:

- record ID;
- version;
- source;
- status;
- payload.

A valid compiler must revise selection or fail.

It must not pretend a record fragment is the full provenance-aware record.

## 27. Atomicity is policy-relative

This chapter treats records as atomic.

That is a modeling choice.

A different system could define safe sub-record segmentation.

If it does, the segments need their own:

- identity;
- provenance;
- ordering;
- truncation semantics;
- validity rules.

The chapter's non-implication is therefore bounded:

> arbitrary token-level truncation is not authorized by this atomic-record formalism.

It does not prove that no principled segmentation scheme can exist.

## 28. Compiler validity

Define:

\[
\mathrm{Valid}_{\Pi}(K;R,B).
\]

The predicate requires:

1. authorization;
2. freshness/version validity;
3. mandatory inclusion;
4. budget compliance;
5. atomicity;
6. required provenance;
7. declared serialization order.

The witness context satisfies all seven.

The rank-prefix control does not.

## 29. Valid context is not correct answer

A model can receive a compiler-valid context and still fail.

It can:

- ignore the evidence;
- misread a version;
- invent unsupported content;
- follow the wrong record;
- fail for reasons unrelated to memory.

Thus:

\[
\boxed{
\mathrm{Valid}_{\Pi}(K)
\not\Rightarrow
\mathrm{CorrectAnswer}.
}
\]

The compiler certifies its transformation.

It does not certify the model.

## 30. Stored is not retrieved

This chapter keeps several non-implications visible:

\[
\text{stored}
\not\Rightarrow
\text{retrieved}.
\]

A record can exist but never enter the candidate set.

## 31. Retrieved is not included

Likewise:

\[
\text{retrieved}
\not\Rightarrow
\text{included}.
\]

A record can be excluded because it is:

- stale;
- unauthorized;
- optional but over budget;
- lower utility under the declared policy;
- in conflict.

## 32. Included is not used

And:

\[
\text{included}
\not\Rightarrow
\text{used by model}.
\]

The context can contain the right evidence while the model ignores it.

This stage separation prevents one success metric from being misreported as another.

## 33. Budget is an abstract resource

This chapter writes:

\[
B
\]

as a compiled-context budget.

It can represent:

- tokens;
- bytes;
- slots;
- another declared resource.

The accounting must be explicit.

The chapter does not assume all model APIs count context identically.

## 34. Prompt construction becomes replayable

A compiled context should have a receipt.

Record:

- query/invocation ID;
- compiler policy version;
- context budget;
- candidates;
- versions/statuses;
- authorization decisions;
- freshness exclusions;
- mandatory records;
- selected optional records;
- total cost;
- serialization order;
- source identities;
- explicit failure code.

Now context construction can be replayed.

That is stronger than saying:

> we put the most relevant things in the prompt.

## 35. Replay does not validate retrieval quality

Suppose the compiler receipt replays perfectly.

The retriever may still have omitted the most useful record.

Replayability tells us what the compiler did with its inputs.

It does not prove the inputs were ideal.

That requires separate retrieval evidence.

## 36. Freshness and ranking answer different questions

Freshness asks:

> is this the version allowed by the invocation policy?

Ranking asks:

> how does the retrieval system order candidates under its scoring rule?

Those questions can disagree.

The exact witness deliberately makes them disagree.

Rank 1 is stale.

Rank 3 is current and mandatory.

The compiler resolves the conflict through policy, not wishful interpretation of the rank.

## 37. Provenance and relevance answer different questions

A record can be highly relevant and poorly sourced.

A record can be authoritative and irrelevant to the current task.

Compilation may need both dimensions.

This chapter preserves provenance metadata.

It does not define a universal method for scoring source quality.

## 38. Shared memory needs invocation-local compilation

External memory can be shared across agents or model instances.

Working context is typically invocation-local.

Therefore the same shared store can compile differently for:

- different tasks;
- different authorization scopes;
- different budgets;
- different freshness policies;
- different mandatory constraints.

Context is a view over memory, not memory itself.

## 39. Context compilation is not memory deletion

Excluding a record from one invocation does not remove it from external memory.

The compiler chooses a working set.

It does not mutate the source store unless a separate operation explicitly does so.

This is another reason memory and context need separate objects.

## 40. Context compilation is not model editing

A compiled prompt can change behavior without changing parameters.

That does not make prompt construction equivalent to parameter editing.

The state loci and update semantics differ.

EXTMEM-001 supplied that distinction.

CONTEXTCOMP keeps it visible.

## 41. Practical compiler protocol

For an invocation:

1. retrieve candidates;
2. record candidate identities and ranks;
3. apply authorization;
4. apply freshness/version rules;
5. detect unresolved conflicts;
6. identify mandatory records;
7. check mandatory feasibility;
8. compute complete compiled costs;
9. select optional records;
10. serialize deterministically;
11. emit context plus compilation receipt;
12. invoke the model.

If any hard constraint fails, emit an explicit compiler failure.

## 42. What this chapter does not claim

It does not claim that:

\[
\text{retrieval rank}
=
\text{truth}.
\]

It does not claim that:

\[
\text{declared utility}
=
\text{true model usefulness}.
\]

It does not claim that:

\[
\text{more context}
=
\text{better answer}.
\]

It does not claim that:

\[
\text{compiler-valid}
=
\text{answer-correct}.
\]

It does not claim that one universal record ordering is optimal.

## 43. Non-implications

The chapter rejects:

\[
\text{stored}
\not\Rightarrow
\text{retrieved},
\]

\[
\text{retrieved}
\not\Rightarrow
\text{included},
\]

\[
\text{high retrieval rank}
\not\Rightarrow
\text{fresh/current},
\]

\[
\text{compiled}
\not\Rightarrow
\text{used by model},
\]

\[
\text{compiler-valid}
\not\Rightarrow
\text{answer-correct},
\]

\[
\text{utility-optimal under }\Pi
\not\Rightarrow
\text{universally optimal context},
\]

and

\[
\text{fits budget}
\not\Rightarrow
\text{provenance or authorization valid}.
\]

## 44. Atlas connections

**Retrieval.**  
Retrieval supplies candidates; compilation determines the invocation working set.

**External Memory.**  
Context compilation consumes versioned provenance-aware records without collapsing memory into prompt text.

**Agents.**  
An agent can compile different working sets for different subgoals while sharing one persistent store.

**Evidence systems.**  
Compilation receipts can preserve which evidence objects were actually placed before a model.

**Context and token compression.**  
Compression can become one optional selection mechanism, but it remains constrained by freshness, authority, provenance, and mandatory content.

**Governed adaptation.**  
Changing compiler policy changes which external state enters model computation and therefore deserves versioned governance.

## 45. Closing view

The model context is small.

The memory can be large.

The job between them is not merely retrieval.

It is compilation.

A serious compiler knows:

- which records are current;
- which records are authorized;
- which records are mandatory;
- what provenance must survive;
- what the budget actually counts;
- which optional records fit;
- how ties are resolved;
- how the final sequence is serialized.

The exact witness is small because the principle is structural.

The highest-ranked record can be stale.

The mandatory record can rank lower.

A naive prefix can fit the budget and still be invalid.

The correct conclusion is:

\[
\boxed{
\text{context construction is a governed bounded transformation from candidate memory records to a replayable working set.}
}
\]

That transformation deserves its own mathematics, provenance, and failure semantics.

## References used in this chapter

External authority is inherited through the audited External-Memory Thesis, ATLAS-CH-EXTMEM-001 / AUDIT-031.

Exact source identities and authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-CONTEXTCOMP-001.yaml
