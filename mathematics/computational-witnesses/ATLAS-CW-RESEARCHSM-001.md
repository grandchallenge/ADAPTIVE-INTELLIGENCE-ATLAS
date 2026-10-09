# ATLAS-CW-RESEARCHSM-001 — Finite Research-State Witness

## Evidence identity

Fix dispatch `d=17` and result identity `r_A=(17,A)`. With `E_0=empty`, first capture gives `E_1={r_A}`, so `|E_1|=1`.

## Exact retry

Receiving the same identity again gives `E_2=E_1 union {r_A}=E_1`, so `|E_2|=1`. Attempt history may still record both arrivals.

## Distinct result

Let `r_B=(17,B)` with `B!=A`. This is not an exact duplicate of `r_A`. Preserving both gives `E_3={r_A,r_B}`, so `|E_3|=2`.

## Advancement gate

Use:

`G_adv(b)=b1*b2*b3*b4*b5`.

For:

`b=(1,1,1,1,0)`,

we obtain:

`G_adv(b)=0`.

For:

`b'=(1,1,1,1,1)`,

we obtain:

`G_adv(b')=1`.

A missing required replay/check example is:

`b_R=(1,1,0,1,1)`,

which also gives:

`G_adv(b_R)=0`.

## Idempotent advancement

Let `K_adv` be the canonical set of advanced evidence identities.

If `m` is already admitted under a true guard, then:

`(K_adv union {m}) union {m}=K_adv union {m}`.

Thus repeating the same exact advancement event does not multiply the canonical advancement effect.

History may still record the repeated attempt.

## Actor-separation counterexample

For a policy that requires producer/reviewer identity separation, define:

`Sep(a_prod,a_rev)=1{a_prod != a_rev}`.

Then:

`Sep(A,A)=0`.

So a same-actor review fails that declared separation predicate.

For distinct identities:

`Sep(A,B)=1`.

This establishes identity separation only; it does not prove stronger independence.

## Safety without liveness

Take a blocked state in which:

- all evidence identities are preserved;
- every invalid guarded transition remains blocked;
- no duplicate canonical effect occurs;
- certification remains unchanged;
- advancement disposition stays false forever.

If the only repeated future event is an idempotent retry, all listed safety invariants continue to hold while the evidence identity never enters `K_adv`.

Therefore the finite execution is safe under the declared invariants but not live with respect to eventual advancement.

## Executable canonical/history and exhaustive-guard replay

The following Python replay makes the state distinction testable. Canonical
evidence and advancement are immutable sets of exact identities; history
records attempts separately. The five-bit gate is checked for **all 32 Boolean
vectors**, not only the three displayed examples. The model uses a declared
identity-only separation policy; actor labels and different GitHub transports
are **not** a general independence certificate.

```python
from itertools import product

d = 17
r_A, r_B = (d, "A"), (d, "B")
assert r_A != r_B and r_A[0] == r_B[0]

def capture(evidence, history, result_identity):
    return (
        evidence | frozenset((result_identity,)),
        history + (("capture", result_identity),),
    )

def advance(advanced, history, result_identity, conditions):
    assert len(conditions) == 5
    approved = all(conditions)
    return (
        advanced | frozenset((result_identity,)) if approved else advanced,
        history + (("advance_attempt", result_identity, tuple(conditions)),),
    )

evidence, capture_history = frozenset(), tuple()
evidence, capture_history = capture(evidence, capture_history, r_A)
assert evidence == frozenset((r_A,)) and len(capture_history) == 1
after_first = evidence
evidence, capture_history = capture(evidence, capture_history, r_A)
assert evidence == after_first and len(capture_history) == 2
evidence, capture_history = capture(evidence, capture_history, r_B)
assert evidence == frozenset((r_A, r_B))
assert len(evidence) == 2 and len(capture_history) == 3

def gate(bits):
    assert len(bits) == 5 and all(b in (0, 1) for b in bits)
    return int(all(bits))

assert gate((1, 1, 1, 1, 0)) == 0
assert gate((1, 1, 1, 1, 1)) == 1
assert gate((1, 1, 0, 1, 1)) == 0

all_guards = tuple(product((0, 1), repeat=5))
assert len(all_guards) == 32
assert sum(gate(bits) for bits in all_guards) == 1
for bits in all_guards:
    first, first_history = advance(frozenset(), (), r_A, bits)
    second, second_history = advance(first, first_history, r_A, bits)
    assert first == second
    assert first == (frozenset((r_A,)) if all(bits) else frozenset())
    assert len(first_history) == 1 and len(second_history) == 2

# This identity-only separation policy is *one possible declared policy*.
separated = lambda prod, review: int(prod != review)
assert separated("A", "A") == 0
assert separated("A", "B") == 1

# A safe but non-live infinite trace: repeated blocked attempts never
# advance r_A, even though each attempt remains durable in history.
blocked = (1, 1, 0, 1, 1)
advanced, history = frozenset(), tuple()
for attempt in range(1, 101):
    advanced, history = advance(advanced, history, r_A, blocked)
    assert r_A not in advanced
    assert len(history) == attempt
assert advanced == frozenset()
# For *every* future repetition of the fixed blocked event, the same
# all-false mutation branch preserves this empty canonical set.
assert gate(blocked) == 0

print("RESEARCHSM_CANONICAL_GATES_REPLAY_OK")
```

Expected output:

```text
RESEARCHSM_CANONICAL_GATES_REPLAY_OK
```

The 100 attempted blocked events are an executable finite prefix. The
non-liveness conclusion additionally follows by induction because every
further identical blocked transition leaves the canonical advanced set
unchanged. This demonstration does not establish fairness assumptions or
liveness properties for deployed controllers.

## Claim boundary

This witness proves only the exact finite identity, Boolean-guard, actor-identity-separation, idempotence, and safety/liveness statements above.

It does not prove that the five-factor gate is universally correct; that distinct actors are epistemically independent; that workflow conformance proves mathematical truth; that blocked work should always advance; or that one lifecycle should govern all research programmes.
