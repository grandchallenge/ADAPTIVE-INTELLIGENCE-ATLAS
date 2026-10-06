# ATLAS-CW-TRANSPORT-001 — Constrained Representation Transport Witness

**Chapter:** `ATLAS-CH-TRANSPORT-001`  
**Witness class:** exact finite-dimensional replay  
**Purpose:** verify the chapter's sphere-retraction, base-point tangent, and order-sensitive transport claims.

## W1. Retraction endpoint

Let

\[
u=(1,0),
\qquad
\xi=(0,1).
\]

The normalized retraction is

\[
R_u(\xi)
=
\frac{(1,1)}{\sqrt2}.
\]

Checks:

\[
\|R_u(\xi)\|_2^2=1.
\]

Its polar angle is \(\pi/4\).

The unit-speed sphere exponential endpoint for tangent vector \(\xi\) at unit time has polar angle \(1\).

Therefore the feasible retraction endpoint is not the exact exponential-map endpoint.

## W2. Tangent ownership after moving the base point

Set

\[
u_0=(1,0),
\qquad
v_0=(0,1).
\]

Initial tangent check:

\[
u_0^\top v_0=0.
\]

After moving to

\[
u_1=(1,1)/\sqrt2,
\]

the same ambient vector satisfies

\[
u_1^\top v_0=1/\sqrt2.
\]

So it is no longer tangent.

The orthogonal projection is

\[
P_{u_1}v_0
=
(-1/2,1/2).
\]

Check:

\[
u_1^\top P_{u_1}v_0=0.
\]

## W3. Two-stage order witness on \(S^2\)

Start with

\[
u_0=(1,0,0),
\]

and increments

\[
a=(0,1,0),
\qquad
b=(0,0,1).
\]

Use

\[
R_u(\xi)=\frac{u+\xi}{\|u+\xi\|}.
\]

### A then B

\[
u_a=(1,1,0)/\sqrt2,
\]

\[
u_{ab}
=
(1/2,1/2,1/\sqrt2).
\]

### B then A

\[
u_b=(1,0,1)/\sqrt2,
\]

\[
u_{ba}
=
(1/2,1/\sqrt2,1/2).
\]

Both endpoints have unit norm.

They are unequal.

The exact inner product is

\[
u_{ab}^\top u_{ba}
=
1/4+1/\sqrt2.
\]

## W4. Minimal replay code

```python
from sympy import Matrix, sqrt, simplify

def retract(u, xi):
    y = u + xi
    return simplify(y / sqrt((y.T * y)[0]))

u0 = Matrix([1, 0, 0])
a  = Matrix([0, 1, 0])
b  = Matrix([0, 0, 1])

ua = retract(u0, a)
uab = retract(ua, b)

ub = retract(u0, b)
uba = retract(ub, a)

assert simplify((uab.T * uab)[0]) == 1
assert simplify((uba.T * uba)[0]) == 1
assert uab != uba
assert simplify((uab.T * uba)[0]) == 1/sqrt(2) + 1/4

print(ua)
print(uab)
print(ub)
print(uba)
```

Expected exact values:

```text
ua  = Matrix([sqrt(2)/2, sqrt(2)/2, 0])
uab = Matrix([1/2, 1/2, sqrt(2)/2])
ub  = Matrix([sqrt(2)/2, 0, sqrt(2)/2])
uba = Matrix([1/2, sqrt(2)/2, 1/2])
```

## W5. What this witness establishes

It establishes only:

- normalized retraction preserves the unit-sphere constraint in the declared cases;
- the same ambient tangent coordinates need not remain tangent after the base point moves;
- ordered constrained updates can reach different feasible endpoints;
- the exact endpoint values above.

It does not establish:

- that a learned neural network follows these specific sphere retractions;
- that a retraction is parallel transport or vector transport;
- that any path is optimal;
- that the updates are exact ODE flows;
- that order effects have the same size in a trained network;
- that constraint preservation improves task performance.


## Claim boundary

This computational witness verifies only the exact finite-dimensional identities and comparisons stated above. It does not establish exact-flow semantics, geodesic or parallel transport, optimality, network-level stability, information preservation, or empirical model quality.
