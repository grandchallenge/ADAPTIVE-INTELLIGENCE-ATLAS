# ATLAS-CW-POLITY-001 — Two-Specialist Composition Witness

## Purpose

This exact finite witness shows that a composed system can solve a task set that no individual specialist in the system solves alone, while also showing that the gain depends on the routing rule.

## System

Use two tasks, alpha and beta.

- Specialist A_alpha returns 1 on alpha and 0 on beta.
- Specialist A_beta returns 0 on alpha and 1 on beta.

Under a uniform task distribution, each specialist is correct on exactly one of two tasks.

## Correct composition

The router sends alpha to A_alpha and beta to A_beta.

The resulting system is correct on both tasks.

## Broken composition

A broken router sends both tasks to A_alpha.

The resulting system is again correct on only one of two tasks.

Thus the component set alone does not determine system capability; the composition law matters.

## Exact replay

```python
tasks = ('alpha', 'beta')

def a_alpha(q):
    return 1 if q == 'alpha' else 0

def a_beta(q):
    return 1 if q == 'beta' else 0

def good_router(q):
    return a_alpha if q == 'alpha' else a_beta

def bad_router(q):
    return a_alpha

def accuracy(system):
    return sum(system(q) == 1 for q in tasks) / len(tasks)

assert accuracy(a_alpha) == 0.5
assert accuracy(a_beta) == 0.5
assert accuracy(lambda q: good_router(q)(q)) == 1.0
assert accuracy(lambda q: bad_router(q)(q)) == 0.5

print('POLITY witness: PASS')
```

Expected output:

```text
POLITY witness: PASS
```

## Claim boundary

The witness proves only this finite composition result. It does not establish that adding agents increases capability, that the router is always correct, or that validators, memory, humans, tools, or governance guarantee correctness.