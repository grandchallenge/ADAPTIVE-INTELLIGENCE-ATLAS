# ATLAS-CW-MEMTAX-001 — One Store, Three Memory Access Contracts

**Chapter:** ATLAS-CH-MEMTAX-001  
**Witness class:** exact finite deterministic computation

## Store

Use three immutable records:

A:
- id = A
- vector = (1,0)
- time = 1
- value = red

B:
- id = B
- vector = (0,1)
- time = 2
- value = blue

C:
- id = C
- vector = (1,1)
- time = 3
- value = green

The records do not change during the witness.

## Read 1 — exact key

Query:

id = B.

Result:

blue.

This is exact-address/key-value access.

## Read 2 — associative nearest key

Query vector:

q=(4/5,1/5).

Squared distances:

to A:
2/25;

to B:
32/25;

to C:
17/25.

The unique nearest record is A.

Result:

red.

This is associative/content-based access over the same stored records.

## Read 3 — episodic/recency filter

Query:

time >= 2.

Result set:

[B,C].

Latest result:

C -> green.

This is event/time-oriented access over the same stored records.

## Replay procedure

    from fractions import Fraction

    records = [
        ("A", (Fraction(1), Fraction(0)), 1, "red"),
        ("B", (Fraction(0), Fraction(1)), 2, "blue"),
        ("C", (Fraction(1), Fraction(1)), 3, "green"),
    ]

    exact = next(r for r in records if r[0] == "B")

    q = (Fraction(4, 5), Fraction(1, 5))

    def d2(v):
        return sum((a-b)**2 for a, b in zip(q, v))

    nearest = min(records, key=lambda r: d2(r[1]))
    recent = [r for r in records if r[2] >= 2]
    latest = max(recent, key=lambda r: r[2])

    print("exact=" + exact[3])
    print("distances=" + ",".join(str(d2(r[1])) for r in records))
    print("nearest=" + nearest[0] + ":" + nearest[3])
    print("recent=" + ",".join(r[0] for r in recent))
    print("latest=" + latest[0] + ":" + latest[3])

Expected output:

    exact=blue
    distances=2/25,32/25,17/25
    nearest=A:red
    recent=B,C
    latest=C:green

## What the witness establishes

The physical/logical stored records are identical in all three cases.

Changing only the read contract produces:
- exact-key behavior;
- associative behavior;
- episodic/recency behavior.

Therefore memory role depends partly on access semantics and cannot be inferred solely from bytes at rest.

## Claim boundary

The witness proves only the exact reads and distances for the declared three-record store.

It does not show that these three access modes exhaust machine memory, that Euclidean distance is a generally correct similarity metric, that recency identifies relevance, or that an external record is trustworthy merely because it is retrievable.
