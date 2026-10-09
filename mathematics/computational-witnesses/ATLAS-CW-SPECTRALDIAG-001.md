# ATLAS-CW-SPECTRALDIAG-001 — Exact Spectral Diagnostic Separations

## Claim boundary
This witness certifies only the finite exact identities below. It does not establish a universal spectral diagnostic, a learned Koopman approximation theorem, or a mechanistic interpretation of any spectral signature.

## Python replay

```python
from fractions import Fraction as F

# W1: equal eigenvalues, unequal finite response.
D = ((F(1,2),F(0)),(F(0),F(1,2)))
N = ((F(1,2),F(2)),(F(0),F(1,2)))
e2 = (F(0),F(1))

mv = lambda A,x: tuple(sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A)))
n2 = lambda x: sum(v*v for v in x)

assert n2(mv(D,e2)) == F(1,4)
assert n2(mv(N,e2)) == F(17,4)

# W2: same eigenvalue and singular-value multisets, different fixed-interface response.
A = ((F(2),F(0)),(F(0),F(1,2)))
B = ((F(1,2),F(0)),(F(0),F(2)))
e1 = (F(1),F(0))
assert n2(mv(A,e1)) == F(4)
assert n2(mv(B,e1)) == F(1,4)
assert F(2)-F(1,2) == F(3,2)

# W3: same local Jacobian at zero, different nonlinear value at 1/2.
x = F(1,2)
Fmap = lambda x: F(1,2)*x
Gmap = lambda x: F(1,2)*x + x*x
assert Fmap(x) == F(1,4)
assert Gmap(x) == F(1,2)
# For polynomials of degree at most 2, the symmetric difference at zero
# equals the exact analytic first derivative there (quadratic terms cancel).
def first_derivative_zero(p):
    return (p(F(1)) - p(F(-1))) / 2

JF0 = first_derivative_zero(Fmap)
JG0 = first_derivative_zero(Gmap)
assert JF0 == JG0 == F(1,2)

# W4: identical Hessian spectrum 2I, different gradients at origin.
# For quadratic polynomials, central first and second differences with
# unit steps exactly recover the derivatives/Hessian at the origin.
f = lambda x,y: x*x + y*y
g = lambda x,y: x*x + y*y + x

def grad_zero(q):
    return ((q(F(1),F(0)) - q(F(-1),F(0))) / 2,
            (q(F(0),F(1)) - q(F(0),F(-1))) / 2)

def hessian_zero(q):
    q00 = q(F(0),F(0))
    xx = q(F(1),F(0)) - 2*q00 + q(F(-1),F(0))
    yy = q(F(0),F(1)) - 2*q00 + q(F(0),F(-1))
    xy = (q(F(1),F(1)) - q(F(1),F(-1))
          - q(F(-1),F(1)) + q(F(-1),F(-1))) / 4
    return ((xx,xy),(xy,yy))

grad_f_0 = grad_zero(f)
grad_g_0 = grad_zero(g)
assert grad_f_0 == (F(0),F(0))
assert grad_g_0 == (F(1),F(0))
assert hessian_zero(f) == hessian_zero(g) == ((F(2),F(0)),(F(0),F(2)))

# W5: two-state Koopman swap matrix U has eigenvalues +/-1.
U = ((F(0),F(1)),(F(1),F(0)))
# U^2=I certifies eigenvalues lie in roots of lambda^2-1; trace=0, determinant=-1 gives {1,-1}.
U2 = tuple(tuple(sum(U[i][k]*U[k][j] for k in range(2)) for j in range(2)) for i in range(2))
assert U2 == ((F(1),F(0)),(F(0),F(1)))
traceU = U[0][0] + U[1][1]
detU = U[0][0]*U[1][1] - U[0][1]*U[1][0]
assert traceU == 0
assert detU == -1

print('SPECTRALDIAG_EXACT_WITNESS_OK')
```

The W3–W4 replay now computes the stated local derivatives instead of
assuming their values. Symmetric finite differences are exact **here because
the displayed maps are polynomials of degree at most two**; they are not a
general exact-derivative procedure for arbitrary learned functions.

## Expected output

```text
SPECTRALDIAG_EXACT_WITNESS_OK
```

## Frozen exact values
- equal-eigenvalue control: ||D e2||^2=1/4, ||N e2||^2=17/4;
- equal-spectrum/interface control: ||A e1||^2=4, ||B e1||^2=1/4;
- interface-response change with zero eigenvalue/singular-value multiset drift: 3/2 in norm;
- local-Jacobian control: F'(0)=G'(0)=1/2, but F(1/2)=1/4 and G(1/2)=1/2;
- Hessian control: both Hessian spectra {2,2}, gradients at origin (0,0) versus (1,0);
- Koopman swap: U^2=I, trace(U)=0, det(U)=-1, hence eigenvalues {1,-1}.

## Interpretation
These controls show that operator spectra, interface behavior, local nonlinear behavior, optimization stationarity, and mechanistic significance are different objects. The finite identities are exact; empirical spectral estimation requires additional error analysis.
