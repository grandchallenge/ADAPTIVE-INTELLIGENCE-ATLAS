# Chapter Specification — ATLAS-CH-CONTEXTCOMP-001

## Identity

**Title:** Context Compilation  
**Part:** Memory Beyond Weights  
**Status target:** draft-v0.1  
**Implementation issue:** #235  
**Protected baseline:** b00d6020b809145a99689418db13ff6d6561a659

## Hard prerequisite

ATLAS-CH-EXTMEM-001 / AUDIT-031.

Exact prerequisite identities and the claim boundary are frozen in:

sources/source-locks/ATLAS-CH-CONTEXTCOMP-001.yaml

No new external source authority is required for the core formal chapter.

## Chapter contract

Treat a model invocation context as a compiled working set, not as an unexamined prefix of retrieved text.

The chapter must define a bounded transformation

\[
\text{retrieved candidate records}
\longrightarrow
\text{ordered working context}
\]

under explicit:

- freshness/version policy;
- authorization policy;
- mandatory-record constraints;
- provenance-preserving atomic record semantics;
- context budget;
- selection objective;
- deterministic tie-breaking;
- serialization order.

It must preserve the separation:

\[
\text{storage}
\neq
\text{retrieval}
\neq
\text{ranking}
\neq
\text{compilation}
\neq
\text{model use}.
\]

## Inherited EXTMEM boundary

The chapter may assume:

- hybrid parametric/external placement;
- versioned records;
- explicit freshness policy;
- provenance-preserving record semantics;
- retrieval success distinct from storage correctness;
- authorization distinct from retrievability;
- shared memory not automatically fresh or consistent.

The chapter must independently define how retrieved records become bounded working context.

## Candidate record object

A candidate record is

\[
r_i=
(k_i,v_i,\sigma_i,p_i,a_i,m_i,\rho_i,c_i,u_i,t_i),
\]

where:

- \(k_i\): logical key;
- \(v_i\): version;
- \(\sigma_i\): status, such as current or superseded;
- \(p_i\): source/provenance identity;
- \(a_i\in\{0,1\}\): authorization predicate;
- \(m_i\in\{0,1\}\): mandatory flag;
- \(\rho_i\): retrieval rank;
- \(c_i\in\mathbb N\): compiled cost;
- \(u_i\): declared compiler utility score;
- \(t_i\): record type.

The compiled cost includes both payload and provenance envelope.

The utility score is compiler policy input.

It is not identified with truth, relevance, model accuracy, causal importance, or downstream task value.

## Compiler stages

For candidate multiset \(R\) and budget \(B\):

### 1. Authorization filter

Discard every record with

\[
a_i=0.
\]

Authorization is a hard admissibility condition, not a utility bonus.

### 2. Freshness/version filter

Apply the declared version policy.

For a latest-current policy, superseded records are removed and the current record for each logical key is retained.

If the policy leaves an unresolved conflict, compilation must fail explicitly.

### 3. Mandatory set

Let

\[
M=\{r_i:m_i=1\}.
\]

If

\[
\sum_{r_i\in M}c_i>B,
\]

return an explicit mandatory-overflow failure.

Do not silently truncate mandatory atomic records.

### 4. Optional selection

Let \(O\) be the remaining current authorized records.

Select

\[
S^\star
\subseteq O
\]

to maximize

\[
\sum_{r_i\in S^\star}u_i
\]

subject to

\[
\sum_{r_i\in S^\star}c_i
\le
B-\sum_{r_i\in M}c_i.
\]

Records are atomic.

For ties:

1. prefer lower total cost;
2. then choose the lexicographically smallest sorted list of stable record IDs.

This tie-break is Atlas policy for determinism, not a universal standard.

### 5. Serialization

Serialize

\[
M\cup S^\star
\]

using declared type precedence and stable record IDs.

For the finite witness use:

\[
\text{policy}
\prec
\text{evidence}
\prec
\text{detail}
\prec
\text{background}.
\]

The serialized form must retain at least:

- record ID;
- logical key;
- version;
- source;
- status;
- payload.

## Exact budget-8 witness

Use budget

\[
B=8.
\]

Candidate records:

| ID | key | version/status | rank | cost | utility | mandatory | type |
|---|---|---|---:|---:|---:|---|---|
| \(r_{p1}\) | policy | v1 superseded | 1 | 3 | 9 | no | policy |
| \(r_f\) | task_fact | v1 current | 2 | 4 | 7 | no | evidence |
| \(r_{p2}\) | policy | v2 current | 3 | 4 | 8 | yes | policy |
| \(r_b\) | background | v1 current | 4 | 2 | 3 | no | background |
| \(r_d\) | detail | v1 current | 5 | 3 | 5 | no | detail |

All are authorized.

\(r_{p2}\) supersedes \(r_{p1}\).

### Freshness step

Remove

\[
r_{p1}.
\]

### Mandatory step

Include

\[
r_{p2}
\]

at cost \(4\), leaving residual budget

\[
8-4=4.
\]

### Optional optimization

Remaining options are:

\[
r_f:(c,u)=(4,7),
\]

\[
r_b:(c,u)=(2,3),
\]

\[
r_d:(c,u)=(3,5).
\]

The pair \(r_b+r_d\) costs \(5\) and is infeasible.

Therefore the unique maximum-utility optional set is

\[
\{r_f\}.
\]

The compiled set is

\[
\boxed{
\{r_{p2},r_f\}
}
\]

with total cost

\[
4+4=8
\]

and declared utility

\[
8+7=15.
\]

Serialized order is:

1. current policy record \(r_{p2}\);
2. task evidence record \(r_f\).

Both retain source/version metadata.

## Naive rank-prefix control

A rank-only prefix that ignores freshness and mandatory semantics sees:

1. \(r_{p1}\), cost 3;
2. \(r_f\), cost 4;
3. \(r_{p2}\), cost 4.

Under budget \(8\), it includes the first two records at total cost \(7\).

The next record cannot fit.

Therefore the rank-prefix result is

\[
\{r_{p1},r_f\}.
\]

It contains a superseded policy and omits the mandatory current policy.

If the procedure tries to use the final one budget unit by cutting \(r_{p2}\), it violates the atomic provenance-envelope rule.

Thus:

\[
\boxed{
\text{retrieval rank alone}
\not\Rightarrow
\text{valid compiled context}.
}
\]

## Mandatory-overflow control

If the same current mandatory policy has cost \(4\) but the context budget is

\[
B=3,
\]

then

\[
c(M)=4>B.
\]

The correct compiler output is an explicit failure:

\[
\boxed{
\mathrm{MANDATORY\_OVERFLOW}.
}
\]

It is not a truncated policy record and not a silent omission.

## Provenance preservation

For an included record \(r_i\), define its serialized envelope schematically as

\[
E(r_i)
=
[\mathrm{id},\mathrm{key},\mathrm{version},\mathrm{source},\mathrm{status},\mathrm{payload}].
\]

The finite formalism treats \(E(r_i)\) as atomic.

Compilation preserves the ability to identify which source/version was placed into the working context.

It does not establish that the source is true.

## Context validity predicate

For declared policy \(\Pi\), budget \(B\), and compiled sequence \(K\), define

\[
\mathrm{Valid}_\Pi(K;R,B)
\]

to require:

1. every serialized record is authorized;
2. every serialized logical key satisfies the freshness/version rule;
3. every mandatory current authorized record is present;
4. total compiled cost is at most \(B\);
5. no atomic record is partially serialized;
6. every record retains required provenance metadata;
7. serialization order satisfies the declared precedence/tie-break policy.

This is a compiler-validity predicate.

It is not a model-answer correctness predicate.

## Stage separation

The chapter must maintain:

\[
M
\xrightarrow{\mathrm{retrieve}}
R_q
\xrightarrow{\mathrm{compile}_{\Pi,B}}
K_q
\xrightarrow{\mathrm{invoke}}
y.
\]

A failure at each stage means something different.

### Memory failure

The authoritative record is wrong, missing, stale, or unauthorized.

### Retrieval failure

The relevant record is not returned.

### Ranking failure

Useful candidates are ordered poorly.

### Compilation failure

Freshness, authorization, mandatory, atomicity, provenance, budget, or ordering policy is violated.

### Model-use failure

The model receives a valid compiled context but still ignores, misreads, or misuses it.

The chapter must not collapse these stages.

## Context budget semantics

The budget \(B\) is an abstract compiled-cost budget.

It can represent tokens, bytes, slots, or another declared resource.

No claim is made that all production context windows have identical accounting.

If provenance headers consume resources, those resources belong in \(c_i\).

## Ordering boundary

Serialization order is part of the compiled context object.

The chapter may define deterministic ordering.

It may not assert, without additional evidence, that a particular order universally improves model performance.

## Conflict boundary

If two authorized records for the same logical key are both marked current and the declared freshness policy does not resolve them, the compiler returns an explicit conflict.

It must not choose by retrieval rank unless that behavior is itself part of the declared version policy.

## Utility boundary

The optimization problem

\[
\max \sum u_i
\]

is exact relative to declared \(u_i\).

The chapter must explicitly reject:

\[
u_i
=
\text{true model usefulness}
\]

as an assumed identity.

A production system can learn, estimate, or hand-specify utility scores, but that is a separate evidence problem.

## Required non-implications

The reader manuscript must explicitly reject:

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
\text{fits token budget}
\not\Rightarrow
\text{provenance or authorization valid}.
\]

## Practical compilation ledger

A real compilation event should be able to record:

- invocation/query ID;
- compiler policy/version;
- context budget;
- candidate record IDs;
- candidate versions/statuses;
- authorization decisions;
- records rejected by freshness policy;
- mandatory set;
- selected set;
- excluded feasible records;
- total compiled cost;
- serialization order;
- provenance/source IDs;
- explicit failure code when compilation aborts.

This makes context construction replayable.

## Reader outcomes

A reader should be able to:

1. distinguish retrieval from context compilation;
2. define an atomic provenance-aware record;
3. state hard filters versus optimization criteria;
4. identify mandatory-overflow and unresolved-conflict failures;
5. reproduce the budget-8 witness;
6. explain why rank-prefix truncation fails;
7. distinguish compiler utility from downstream model usefulness;
8. define compiler validity separately from answer correctness;
9. state why provenance metadata consumes budget;
10. design a replayable compilation ledger.

## Required artifacts

- specification;
- derivation packet;
- exact computational witness;
- reader manuscript;
- source lock;
- Chapter Ledger promotion;
- Source Register entry;
- transaction receipt;
- mandatory post-draft audit.

## Downstream handoff

CONTEXTCOMP should provide reusable language for:

- agent working-memory construction;
- retrieval-augmented invocation pipelines;
- shared-memory systems;
- governed tool use;
- evidence assembly;
- context/token compression;
- research-system dispatch.

Downstream chapters may inherit:

- explicit stage separation;
- context-budget accounting;
- mandatory/freshness/authorization filters;
- provenance-preserving atomic record semantics;
- replayable compilation ledgers.

They may not inherit a theorem that compiler validity guarantees downstream model correctness.

## References used in this chapter

External authority is inherited through ATLAS-CH-EXTMEM-001 / AUDIT-031.

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-CONTEXTCOMP-001.yaml
