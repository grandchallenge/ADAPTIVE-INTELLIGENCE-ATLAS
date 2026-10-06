# ATLAS-CW-CONTEXTCOMP-001 — Exact Context Compilation Witness

**Chapter:** ATLAS-CH-CONTEXTCOMP-001  
**Purpose:** exact replay of freshness-aware bounded compilation, rank-prefix failure, provenance-preserving atomicity, and mandatory overflow.

## W1. Budget

Use compiled-context budget

\[
B=8.
\]

Compiled costs include payload plus required provenance envelope.

## W2. Candidate records

The retrieved candidate set is:

| ID | key | status/version | rank | cost | utility | mandatory | authorized | type |
|---|---|---|---:|---:|---:|---|---|---|
| r_policy_v1 | policy | superseded v1 | 1 | 3 | 9 | no | yes | policy |
| r_fact | task_fact | current v1 | 2 | 4 | 7 | no | yes | evidence |
| r_policy_v2 | policy | current v2 | 3 | 4 | 8 | yes | yes | policy |
| r_background | background | current v1 | 4 | 2 | 3 | no | yes | background |
| r_detail | detail | current v1 | 5 | 3 | 5 | no | yes | detail |

The source identities are:

- r_policy_v1 -> src_policy_v1;
- r_fact -> src_fact;
- r_policy_v2 -> src_policy_v2;
- r_background -> src_background;
- r_detail -> src_detail.

The current policy v2 supersedes policy v1.

## W3. Freshness filter

The declared latest-current policy removes:

\[
r_{\rm policy\_v1}.
\]

Survivors:

\[
r_{\rm fact},
r_{\rm policy\_v2},
r_{\rm background},
r_{\rm detail}.
\]

## W4. Mandatory inclusion

The current policy v2 is mandatory.

Its cost is:

\[
4.
\]

Residual budget:

\[
8-4=4.
\]

## W5. Optional feasible sets

Optional candidates:

\[
r_{\rm fact}:(4,7),
\]

\[
r_{\rm background}:(2,3),
\]

\[
r_{\rm detail}:(3,5).
\]

Here each pair is:

\[
(\text{cost},\text{declared utility}).
\]

Feasible subsets under residual budget \(4\):

- empty: \((0,0)\);
- fact: \((4,7)\);
- background: \((2,3)\);
- detail: \((3,5)\).

Every two-record optional subset costs at least \(5\) and is infeasible.

Thus the unique maximum-utility optional selection is:

\[
\boxed{
\{r_{\rm fact}\}.
}
\]

## W6. Final compiled set

Add the mandatory policy:

\[
\boxed{
S_{\rm final}
=
\{r_{\rm policy\_v2},r_{\rm fact}\}.
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

## W7. Serialization

Declared type precedence is:

\[
\text{policy}
\prec
\text{evidence}
\prec
\text{detail}
\prec
\text{background}.
\]

Therefore serialized context is:

1. r_policy_v2;
2. r_fact.

Each record preserves an envelope:

\[
[\mathrm{id},\mathrm{key},\mathrm{version},\mathrm{source},\mathrm{status},\mathrm{payload}].
\]

The compiled context therefore retains:

- current policy identity;
- current policy version;
- current policy source;
- task-fact identity;
- task-fact source.

## W8. Validity checks

### Authorization

Both included records are authorized.

### Freshness

The policy record is current v2.

### Mandatory inclusion

r_policy_v2 is included.

### Budget

\[
8\le8.
\]

### Atomicity

No record is split.

### Provenance

Source metadata is retained.

### Ordering

Policy precedes evidence.

Thus:

\[
\boxed{
\mathrm{Valid}_{\Pi}(K)=1.
}
\]

## W9. Naive rank-prefix control

Sort raw candidates by retrieval rank:

1. r_policy_v1, cost 3;
2. r_fact, cost 4;
3. r_policy_v2, cost 4;
4. r_background, cost 2;
5. r_detail, cost 3.

A naive rank-prefix budget fill:

- includes r_policy_v1, cumulative cost 3;
- includes r_fact, cumulative cost 7;
- cannot include r_policy_v2 because total would be 11.

Result:

\[
\{r_{\rm policy\_v1},r_{\rm fact}\}.
\]

This fails:

- freshness: policy v1 is superseded;
- mandatory inclusion: current policy v2 is absent.

Therefore:

\[
\boxed{
\mathrm{Valid}_{\Pi}(K_{\rm rank})=0.
}
\]

## W10. Why truncation does not repair it

After the naive rank prefix, one budget unit remains.

Current mandatory policy v2 costs four units.

Under atomic provenance-aware record semantics, one unit is not a valid serialized policy record.

Partial truncation can omit the very metadata needed to identify:

- record;
- version;
- source;
- status;
- payload.

Therefore the compiler must reconsider selection.

It may not repair the invalid prefix by slicing the mandatory record.

## W11. Mandatory-overflow control

Set:

\[
B=3.
\]

The current mandatory policy still costs:

\[
4.
\]

Therefore:

\[
C_M=4>3.
\]

No atomic context can both include the mandatory policy and fit the budget.

Correct compiler status:

\[
\boxed{
\mathrm{MANDATORY\_OVERFLOW}.
}
\]

## W12. Exact replay code

    records = [
        {
            "id": "r_policy_v1",
            "key": "policy",
            "version": 1,
            "status": "superseded",
            "rank": 1,
            "cost": 3,
            "utility": 9,
            "mandatory": False,
            "authorized": True,
            "type": "policy",
        },
        {
            "id": "r_fact",
            "key": "task_fact",
            "version": 1,
            "status": "current",
            "rank": 2,
            "cost": 4,
            "utility": 7,
            "mandatory": False,
            "authorized": True,
            "type": "evidence",
        },
        {
            "id": "r_policy_v2",
            "key": "policy",
            "version": 2,
            "status": "current",
            "rank": 3,
            "cost": 4,
            "utility": 8,
            "mandatory": True,
            "authorized": True,
            "type": "policy",
        },
        {
            "id": "r_background",
            "key": "background",
            "version": 1,
            "status": "current",
            "rank": 4,
            "cost": 2,
            "utility": 3,
            "mandatory": False,
            "authorized": True,
            "type": "background",
        },
        {
            "id": "r_detail",
            "key": "detail",
            "version": 1,
            "status": "current",
            "rank": 5,
            "cost": 3,
            "utility": 5,
            "mandatory": False,
            "authorized": True,
            "type": "detail",
        },
    ]

    budget = 8

    current = [
        r for r in records
        if r["authorized"] and r["status"] == "current"
    ]

    mandatory = [r for r in current if r["mandatory"]]
    optional = [r for r in current if not r["mandatory"]]

    mandatory_cost = sum(r["cost"] for r in mandatory)
    assert mandatory_cost == 4

    residual = budget - mandatory_cost
    assert residual == 4

    feasible = []
    for mask in range(1 << len(optional)):
        subset = [
            optional[i]
            for i in range(len(optional))
            if mask & (1 << i)
        ]
        cost = sum(r["cost"] for r in subset)
        utility = sum(r["utility"] for r in subset)
        if cost <= residual:
            feasible.append((utility, cost, tuple(sorted(r["id"] for r in subset)), subset))

    best = min(feasible, key=lambda x: (-x[0], x[1], x[2]))
    best_ids = {r["id"] for r in best[3]}

    assert best_ids == {"r_fact"}

    final_ids = {r["id"] for r in mandatory} | best_ids
    assert final_ids == {"r_policy_v2", "r_fact"}

    final_cost = sum(r["cost"] for r in current if r["id"] in final_ids)
    final_utility = sum(r["utility"] for r in current if r["id"] in final_ids)

    assert final_cost == 8
    assert final_utility == 15

    ranked = sorted(records, key=lambda r: r["rank"])
    used = 0
    prefix = []

    for r in ranked:
        if used + r["cost"] <= budget:
            prefix.append(r)
            used += r["cost"]
        else:
            break

    assert [r["id"] for r in prefix] == ["r_policy_v1", "r_fact"]
    assert "r_policy_v2" not in {r["id"] for r in prefix}

    assert 4 > 3

## Claim boundary

This witness establishes only properties of the declared finite compiler and candidate set.

It establishes:

- exact freshness filtering;
- exact mandatory cost;
- exact feasible optional subsets;
- exact selected set;
- exact total cost and declared utility;
- exact rank-prefix failure;
- exact mandatory-overflow condition.

It does not establish:

- that the declared utility scores equal true usefulness;
- that this compiler is universally optimal;
- that retrieval rank is generally poor;
- that any particular serialization order improves a model;
- that a valid compiled context produces a correct answer;
- that token-level truncation is always invalid outside the declared atomic-record policy;
- that all production context compilers should use this exact objective.
