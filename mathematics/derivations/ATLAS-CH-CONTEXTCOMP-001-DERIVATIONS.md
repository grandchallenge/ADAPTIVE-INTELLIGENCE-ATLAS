# ATLAS-CH-CONTEXTCOMP-001 — Derivation Packet

## Scope

This packet formalizes a finite provenance-aware context compiler.

It begins with an already retrieved candidate set.

It does not prove retrieval quality, semantic truth, downstream answer correctness, or universal prompt optimality.

## D1. Candidate records

Let

\[
R=\{r_1,\ldots,r_n\}.
\]

Each record carries:

\[
r_i=(k_i,v_i,\sigma_i,p_i,a_i,m_i,\rho_i,c_i,u_i,t_i).
\]

Interpretation:

- \(k_i\): logical key;
- \(v_i\): version;
- \(\sigma_i\): status;
- \(p_i\): provenance/source identity;
- \(a_i\): authorization;
- \(m_i\): mandatory flag;
- \(\rho_i\): retrieval rank;
- \(c_i\): compiled cost;
- \(u_i\): declared compiler utility;
- \(t_i\): record type.

The compiler treats \(c_i\) as the cost of the complete serialized record envelope.

## D2. Authorization filter

Define

\[
A(R)=\{r_i\in R:a_i=1\}.
\]

This is a hard filter.

No amount of utility compensates for

\[
a_i=0.
\]

Thus authorization is not part of the optional objective.

## D3. Freshness/version filter

Let the declared policy be latest-current.

For every logical key \(k\), retain the unique authorized record marked current.

Superseded versions are excluded.

If more than one authorized record for the same key is marked current and the policy contains no conflict-resolution rule, return

\[
\mathrm{VERSION\_CONFLICT}.
\]

Call the surviving set

\[
F(A(R)).
\]

This stage uses record metadata, not retrieval rank.

## D4. Mandatory set

Define

\[
M=
\{r_i\in F(A(R)):m_i=1\}.
\]

The mandatory cost is

\[
C_M=
\sum_{r_i\in M}c_i.
\]

For budget \(B\), a necessary feasibility condition is

\[
C_M\le B.
\]

If

\[
C_M>B,
\]

the compiler returns

\[
\mathrm{MANDATORY\_OVERFLOW}.
\]

It does not silently omit or truncate a mandatory atomic record.

## D5. Optional selection

Let

\[
O=F(A(R))\setminus M.
\]

Residual budget is

\[
B'=B-C_M.
\]

The optional selection problem is:

\[
\max_{S\subseteq O}
\sum_{r_i\in S}u_i
\]

subject to

\[
\sum_{r_i\in S}c_i\le B'.
\]

This is a finite subset-selection problem.

The chapter does not claim a particular production algorithm for large \(n\).

The finite witness is solved exactly by enumeration.

## D6. Deterministic tie-breaking

If two feasible optional sets have equal utility:

1. choose lower total cost;
2. if cost also ties, choose the lexicographically smallest sorted list of stable record IDs.

This defines a deterministic compiler result for finite input.

It is a policy choice.

It is not a theorem about the best prompt order or best model behavior.

## D7. Serialization function

Let

\[
S_{\rm final}=M\cup S^\star.
\]

Define type precedence

\[
\text{policy}
\prec
\text{evidence}
\prec
\text{detail}
\prec
\text{background}.
\]

Within each type, order by stable record ID.

For each record define the serialized envelope

\[
E(r_i)
=
[\mathrm{id},\mathrm{key},\mathrm{version},\mathrm{source},\mathrm{status},\mathrm{payload}].
\]

Then

\[
K=
\mathrm{serialize}(S_{\rm final})
\]

is the compiled working context.

## D8. Exact finite witness

Set

\[
B=8.
\]

Use records:

\[
r_{p1}:
(c,u,\rho,\sigma,m)
=
(3,9,1,\mathrm{superseded},0),
\]

\[
r_f:
(c,u,\rho,\sigma,m)
=
(4,7,2,\mathrm{current},0),
\]

\[
r_{p2}:
(c,u,\rho,\sigma,m)
=
(4,8,3,\mathrm{current},1),
\]

\[
r_b:
(c,u,\rho,\sigma,m)
=
(2,3,4,\mathrm{current},0),
\]

\[
r_d:
(c,u,\rho,\sigma,m)
=
(3,5,5,\mathrm{current},0).
\]

All are authorized.

\(r_{p1}\) and \(r_{p2}\) share logical key policy.

\(r_{p2}\) supersedes \(r_{p1}\).

## D9. Freshness step

The latest-current policy removes

\[
r_{p1}.
\]

Thus the current authorized set is

\[
R'=
\{r_f,r_{p2},r_b,r_d\}.
\]

## D10. Mandatory step

The mandatory set is

\[
M=\{r_{p2}\}.
\]

Its cost is

\[
C_M=4.
\]

Residual budget is

\[
B'=8-4=4.
\]

Optional set is

\[
O=\{r_f,r_b,r_d\}.
\]

## D11. Exhaustive feasible-set comparison

All subsets of \(O\):

### Empty set

\[
c=0,\qquad u=0.
\]

### \(\{r_f\}\)

\[
c=4,\qquad u=7.
\]

Feasible.

### \(\{r_b\}\)

\[
c=2,\qquad u=3.
\]

Feasible.

### \(\{r_d\}\)

\[
c=3,\qquad u=5.
\]

Feasible.

### \(\{r_f,r_b\}\)

\[
c=6>4.
\]

Infeasible.

### \(\{r_f,r_d\}\)

\[
c=7>4.
\]

Infeasible.

### \(\{r_b,r_d\}\)

\[
c=5>4.
\]

Infeasible.

### \(\{r_f,r_b,r_d\}\)

\[
c=9>4.
\]

Infeasible.

Among feasible optional sets, maximum utility is

\[
7,
\]

uniquely attained by

\[
S^\star=\{r_f\}.
\]

Therefore

\[
S_{\rm final}
=
\{r_{p2},r_f\}.
\]

Total cost:

\[
4+4=8.
\]

Total declared utility:

\[
8+7=15.
\]

## D12. Serialized result

Type precedence places policy before evidence.

Thus:

\[
K=
(E(r_{p2}),E(r_f)).
\]

The compiled context contains:

- current policy v2;
- source identity for policy v2;
- task fact;
- source identity for the task fact.

The superseded policy v1 is absent.

## D13. Validity of the compiled result

For the declared policy:

### Authorization

Both records are authorized.

### Freshness

Policy key uses current v2.

### Mandatory inclusion

\(r_{p2}\) is present.

### Budget

\[
c(r_{p2})+c(r_f)=8\le8.
\]

### Atomicity

Both complete record envelopes are included.

### Provenance

Both source identities remain serialized.

### Ordering

Policy precedes evidence.

Therefore

\[
\boxed{
\mathrm{Valid}_{\Pi}(K;R,8)=1.
}
\]

## D14. Rank-prefix control

Sort the raw retrieved candidates by rank:

\[
r_{p1},r_f,r_{p2},r_b,r_d.
\]

A naive prefix under budget \(8\):

- include \(r_{p1}\), cumulative cost \(3\);
- include \(r_f\), cumulative cost \(7\);
- \(r_{p2}\) would raise cost to \(11\), so stop.

The result is:

\[
K_{\rm rank}
=
(E(r_{p1}),E(r_f)).
\]

It fails freshness because \(r_{p1}\) is superseded.

It fails mandatory inclusion because \(r_{p2}\) is absent.

Therefore

\[
\boxed{
\mathrm{Valid}_{\Pi}(K_{\rm rank};R,8)=0.
}
\]

## D15. Why one-unit truncation does not repair the rank prefix

After selecting \(r_{p1}\) and \(r_f\), one unit remains.

The current mandatory policy costs

\[
c(r_{p2})=4.
\]

Under atomic-record semantics, a one-unit fragment is not \(E(r_{p2})\).

It can omit:

- record identity;
- version;
- source;
- status;
- payload.

Therefore truncating the record violates the declared compilation object.

The compiler must reconsider the selected set rather than slicing the mandatory record.

## D16. Mandatory-overflow theorem for this compiler

Let mandatory set \(M\) have total compiled cost \(C_M\).

If

\[
C_M>B,
\]

no context satisfying both:

1. all mandatory records included atomically;
2. total cost at most \(B\),

exists.

Proof:

Any valid context has cost at least \(C_M\).

If \(C_M>B\), that contradicts the budget condition.

Therefore explicit failure is correct.

For the witness current policy:

\[
C_M=4.
\]

At budget

\[
B=3,
\]

no valid compiled context exists.

## D17. Retrieval rank is not freshness

In the witness:

\[
\rho(r_{p1})=1,
\]

while

\[
\rho(r_{p2})=3.
\]

Yet \(r_{p1}\) is superseded and \(r_{p2}\) is current.

Therefore the exact candidate set gives a counterexample to:

\[
\text{better retrieval rank}
\Rightarrow
\text{fresher version}.
\]

No statistical claim is needed.

## D18. Candidate utility is not truth

The superseded record has declared utility

\[
u(r_{p1})=9,
\]

higher than current policy utility

\[
u(r_{p2})=8.
\]

Freshness filtering removes it before optimization.

Thus hard validity constraints dominate optional utility.

This is intentional.

The compiler does not buy freshness violations with utility points.

## D19. Provenance consumes budget

Suppose record payload cost is \(d_i\) and required provenance-envelope cost is \(h_i\).

Then define

\[
c_i=d_i+h_i.
\]

If a system instead budgets only \(d_i\), it can overstate how many complete provenance-preserving records fit.

Therefore the context budget must match the serialization object actually delivered.

## D20. Compiler validity does not imply answer correctness

Let

\[
K
\]

satisfy every compiler constraint.

A downstream model can still:

- ignore a record;
- misinterpret it;
- hallucinate;
- choose the wrong source;
- fail the task for unrelated reasons.

Thus:

\[
\boxed{
\mathrm{Valid}_\Pi(K)
\not\Rightarrow
\mathrm{CorrectAnswer}.
}
\]

The compiler certifies only its own declared transformation.

## D21. Storage, retrieval, compilation, use

The pipeline is:

\[
M
\xrightarrow{\mathrm{retrieve}}
R_q
\xrightarrow{\mathrm{compile}_{\Pi,B}}
K_q
\xrightarrow{\mathrm{model}}
y.
\]

The arrows have different obligations.

A correct record in \(M\) can be missed by retrieval.

A retrieved record can be rejected by the compiler.

A valid compiled record can be ignored by the model.

Therefore no arrow can be silently identified with the next.

## D22. Replayability object

A compilation receipt can be defined as:

\[
\mathcal L
=
(q,\Pi,B,R_q,A,F,M,S^\star,K,\mathrm{status}),
\]

where the record contains:

- invocation/query identifier;
- compiler policy/version;
- budget;
- candidate IDs;
- authorization decisions;
- freshness/version decisions;
- mandatory set;
- optional selected set;
- serialized order;
- explicit status or failure code.

This is sufficient to replay the finite decision given the same record metadata and payload costs.

It does not prove the retrieved candidate set was ideal.

## D23. Durable propositions

1. Retrieval produces candidates; compilation produces bounded ordered working context.
2. Authorization and freshness are hard admissibility constraints in the declared compiler.
3. Mandatory records create a feasibility condition before optional optimization.
4. Provenance-preserving records are atomic in the finite formalism.
5. The exact budget-8 compiler selects current policy v2 plus task evidence at total cost 8 and declared utility 15.
6. Rank-prefix truncation selects superseded policy v1 plus evidence and is invalid under the same policy.
7. Mandatory overflow admits no valid context under atomic inclusion.
8. Retrieval rank does not imply freshness.
9. Compiler utility does not equal truth or universal model usefulness.
10. Compiler validity does not imply downstream answer correctness.
