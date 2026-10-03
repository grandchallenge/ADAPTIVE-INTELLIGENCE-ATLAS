# ATLAS-CW-RETRIEVAL-001 — One Store, Multiple Retrieval Contracts

**Chapter:** ATLAS-CH-RETRIEVAL-001  
**Witness class:** exact finite deterministic computation  
**Purpose:** show that exact-key, symbolic, vector, and hybrid retrieval can return different valid results over one immutable record set, and that hybrid composition order is load-bearing.

## Store

Use records:

- `A=(id=A, kind=paper, year=2024, v=(1,0), value=alpha)`
- `B=(id=B, kind=paper, year=2022, v=(4/5,3/5), value=beta)`
- `C=(id=C, kind=note, year=2025, v=(24/25,1/25), value=gamma)`

Query vector:

`q=(19/20,1/20)`.

Distance:

squared Euclidean distance.

## Vector ranking

For A:

`d(q,A)^2=1/200`.

For B:

`d(q,B)^2=13/40`.

For C:

`d(q,C)^2=1/5000`.

Hence:

`C < A < B`

by distance.

Vector top-1:

`C`.

Vector top-2:

`{C,A}`.

## Exact-key access

Query:

`id=B`.

Result:

`B`.

The nearest vector record is irrelevant to this exact-address contract.

## Symbolic access

Predicate:

`year>=2024`.

Result set:

`{A,C}`.

No score order is implied by the predicate alone.

## Hybrid access: filter then rank

Predicate:

`kind=paper`.

Admissible set:

`{A,B}`.

Ranking by vector distance gives:

`A,B`.

Top-1 result:

`A`.

## Hybrid access: rank then filter

Rank full set top-1 first.

Top-1:

`C`.

Then apply `kind=paper`.

C is not a paper.

Result:

empty.

Therefore:

`FilterThenRank != RankThenFilter`.

## Exact replay

```python
from fractions import Fraction

records = {
    "A": {"kind": "paper", "year": 2024, "v": (Fraction(1), Fraction(0)), "value": "alpha"},
    "B": {"kind": "paper", "year": 2022, "v": (Fraction(4,5), Fraction(3,5)), "value": "beta"},
    "C": {"kind": "note",  "year": 2025, "v": (Fraction(24,25), Fraction(1,25)), "value": "gamma"},
}

q = (Fraction(19,20), Fraction(1,20))

def d2(a, b):
    return sum((x-y)**2 for x, y in zip(a, b))

dist = {k: d2(q, r["v"]) for k, r in records.items()}
ranking = sorted(records, key=lambda k: (dist[k], k))

key_result = records["B"]["value"]
symbolic = sorted(k for k, r in records.items() if r["year"] >= 2024)

papers = [k for k, r in records.items() if r["kind"] == "paper"]
filter_then_rank = min(papers, key=lambda k: (dist[k], k))

rank_then_filter_top1 = ranking[0]
rank_then_filter = (
    rank_then_filter_top1
    if records[rank_then_filter_top1]["kind"] == "paper"
    else None
)

print("dist=", dist)
print("ranking=", ranking)
print("key_B=", key_result)
print("year_ge_2024=", symbolic)
print("filter_then_rank=", filter_then_rank)
print("rank_then_filter=", rank_then_filter)
```

Expected exact output:

```text
dist= {'A': Fraction(1, 200), 'B': Fraction(13, 40), 'C': Fraction(1, 5000)}
ranking= ['C', 'A', 'B']
key_B= beta
year_ge_2024= ['A', 'C']
filter_then_rank= A
rank_then_filter= None
```

## Claim boundary

This witness proves only the exact finite results above.

It does not establish a universal superiority ordering among exact-key, symbolic, vector, or hybrid retrieval; it does not validate any learned embedding; it does not characterize HNSW recall; and it does not imply that the nearest or highest-ranked record is semantically correct, provenance-valid, or useful to a downstream model.
