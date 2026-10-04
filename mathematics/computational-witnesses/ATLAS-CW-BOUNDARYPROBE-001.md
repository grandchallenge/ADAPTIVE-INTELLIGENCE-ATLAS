# ATLAS-CW-BOUNDARYPROBE-001 — Exact Local Sensitivity and Power-Iteration Witness

**Chapter:** ATLAS-CH-BOUNDARYPROBE-001  
**Witness class:** exact finite symbolic/rational computation  
**Purpose:** verify JVP/VJP identities, local nonlinear remainder, singular-gain semantics, and both successful and failed power iteration on one explicit nonlinear component.

## Component

`F(x1,x2)=(x1^2+x2, x1+2x2)`.

Operating point:

`x0=(1,1)`.

Then:

`F(x0)=(2,3)`.

Jacobian:

`J=[[2,1],[1,2]]`.

## Singular structure

`J^T J=[[5,4],[4,5]]`.

Its eigenvalues are:

`9,1`.

Therefore the singular values of `J` are:

`3,1`.

Hence:

`||J||_2=3`.

## JVP

Take:

`v=(1,1)`.

Then:

`Jv=(3,3)`.

The Euclidean gain is exactly:

`3`.

For scalar `epsilon`:

`F(x0+epsilon v)-F(x0)
=
epsilon(3,3)+(epsilon^2,0)`.

Thus the first-order term is exactly the JVP and the remainder is explicitly nonlinear.

## VJP

Take:

`w=(1,2)`.

Then:

`J^T w=(4,5)`.

The pairing identity gives:

`w^T(Jv)=9`

and

`(J^T w)^T v=9`.

## Power iteration: mixed start

Let:

`A=J^T J`.

Start:

`z0=(1,0)`.

Then:

`A z0=(5,4)`;

`A^2 z0=(41,40)`.

Rayleigh quotients:

`rho1=365/41`;

`rho2=29525/3281`.

Both approach the dominant eigenvalue:

`9`.

The corresponding singular-value estimates are:

`sqrt(365/41)`;

`sqrt(29525/3281)`;

approaching `3`.

## Power iteration: missed dominant direction

Start instead with:

`zbad=(1,-1)`.

Then:

`A zbad=zbad`.

The Rayleigh quotient remains exactly:

`1`.

The inferred singular value remains:

`1`.

The true operator norm remains:

`3`.

Thus one finite power-iteration run is not a certified upper bound on the local operator norm.

## Exact replay

```python
from fractions import Fraction

J = (
    (Fraction(2), Fraction(1)),
    (Fraction(1), Fraction(2)),
)

def mv(A, x):
    return tuple(sum(a*b for a, b in zip(row, x)) for row in A)

def transpose(A):
    return tuple(zip(*A))

def mm(A, B):
    BT = transpose(B)
    return tuple(tuple(sum(a*b for a,b in zip(row,col)) for col in BT) for row in A)

def dot(x, y):
    return sum(a*b for a,b in zip(x,y))

def rayleigh(A, x):
    Ax = mv(A,x)
    return dot(x,Ax) / dot(x,x)

JT = transpose(J)
A = mm(JT, J)

v = (Fraction(1), Fraction(1))
w = (Fraction(1), Fraction(2))

jvp = mv(J, v)
vjp = mv(JT, w)

u1 = mv(A, (Fraction(1), Fraction(0)))
u2 = mv(A, u1)
rho1 = rayleigh(A, u1)
rho2 = rayleigh(A, u2)

zbad = (Fraction(1), Fraction(-1))
bad_next = mv(A, zbad)
rho_bad = rayleigh(A, zbad)

print("A=", A)
print("jvp=", jvp)
print("vjp=", vjp)
print("pairings=", dot(w,jvp), dot(vjp,v))
print("u1=", u1, "rho1=", rho1)
print("u2=", u2, "rho2=", rho2)
print("bad_next=", bad_next, "rho_bad=", rho_bad)
```

Expected exact output:

```text
A= ((Fraction(5, 1), Fraction(4, 1)), (Fraction(4, 1), Fraction(5, 1)))
jvp= (Fraction(3, 1), Fraction(3, 1))
vjp= (Fraction(4, 1), Fraction(5, 1))
pairings= 9 9
u1= (Fraction(5, 1), Fraction(4, 1)) rho1= 365/41
u2= (Fraction(41, 1), Fraction(40, 1)) rho2= 29525/3281
bad_next= (Fraction(1, 1), Fraction(-1, 1)) rho_bad= 1
```

## Claim boundary

This witness proves only the exact local and finite computations above.

It does not establish a global Lipschitz constant for the nonlinear map, a certified spectral-norm upper bound from finite power iteration, semantic interface compatibility, causal attribution, global numerical stability, or downstream system correctness.
