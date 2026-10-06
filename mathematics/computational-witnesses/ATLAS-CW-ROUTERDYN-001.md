# ATLAS-CW-ROUTERDYN-001 — Router Dynamics Witnesses

## Purpose

This exact finite packet checks three independent separations:

1. stable expert loads can hide total token-route churn;
2. zero preferred-route churn can coexist with nonzero router-probability drift;
3. two local maps can have identical one-step eigenvalue multisets while failing to commute.

## Exact replay

\`\`\`python
import math

# Witness A: load balance versus churn.
r0 = [0, 0, 1, 1]
r1 = [1, 1, 0, 0]

def loads(routes, experts=2):
    return [sum(x == e for x in routes) for e in range(experts)]

load0 = loads(r0)
load1 = loads(r1)
route_churn = sum(a != b for a, b in zip(r0, r1)) / len(r0)
load_drift = sum(abs(a - b) for a, b in zip(load0, load1)) / (2 * len(r0))

assert load0 == [2, 2]
assert load1 == [2, 2]
assert route_churn == 1.0
assert load_drift == 0.0

T_swap = [[0.0, 1.0], [1.0, 0.0]]
T_stable = [[1.0, 0.0], [0.0, 1.0]]

# Both 2x2 matrices are orthogonal, hence both singular spectra are (1, 1).
def gram(M):
    return [
        [sum(M[k][i] * M[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]

assert gram(T_swap) == [[1.0, 0.0], [0.0, 1.0]]
assert gram(T_stable) == [[1.0, 0.0], [0.0, 1.0]]

# Witness B: probability drift without preferred-route churn.
P0 = [[0.6, 0.4], [0.4, 0.6]]
P1 = [[0.9, 0.1], [0.1, 0.9]]

def top1(row):
    return max(range(len(row)), key=row.__getitem__)

routes0 = [top1(row) for row in P0]
routes1 = [top1(row) for row in P1]
prob_drift = sum(
    sum(abs(a - b) for a, b in zip(x, y))
    for x, y in zip(P0, P1)
) / (2 * len(P0))

assert routes0 == routes1 == [0, 1]
assert abs(prob_drift - 0.3) < 1e-12

# Witness C: noncommuting local maps.
J0 = [[1, 1], [0, 1]]
J1 = [[1, 0], [1, 1]]

def mm(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]

A = mm(J1, J0)
B = mm(J0, J1)
C = [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]
fro = math.sqrt(sum(x * x for row in C for x in row))

assert A == [[1, 1], [1, 2]]
assert B == [[2, 1], [1, 1]]
assert C == [[-1, 0], [0, 1]]
assert abs(fro - math.sqrt(2)) < 1e-12

print("ROUTERDYN witness: PASS")
\`\`\`

Expected output:

\`\`\`text
ROUTERDYN witness: PASS
\`\`\`

## Exact values

- initial and final accepted loads: \((2,2)\);
- load drift: \(0\);
- route churn: \(1\);
- stable and swap transition matrices both have singular values \((1,1)\);
- probability drift with unchanged preferred routes: \(0.3\);
- commutator Frobenius norm: \(\sqrt2\).

## Claim boundary

These witnesses prove only the declared finite separations.

They do not establish that churn is harmful, that any one spectrum is the correct router diagnostic, or that a nonzero commutator identifies a causal mechanism.
