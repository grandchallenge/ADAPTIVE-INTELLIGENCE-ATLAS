# ATLAS-CW-NETNUM-001 — Scalar Residual/Euler Scheme Witness

**Chapter:** ATLAS-CH-NETNUM-001  
**Witness class:** exact symbolic and rational finite computation  
**Purpose:** distinguish residual-step syntax, finite-horizon refinement, numerical stability, map invertibility, and time reversibility on the smallest declared flow.

## Continuous reference problem

`x'=-x`,
`x(0)=1`.

Exact solution:

`x(t)=e^{-t}`.

Exact one-step map:

`Phi_h(x)=e^{-h}x`.

## Residual/Euler step

`Psi_h(x)=x-hx=(1-h)x`.

This is both an explicit-Euler step for the declared ODE and a scalar residual block.

## One-step local error

Starting from exact state `x`:

`Phi_h(x)-Psi_h(x)=[e^{-h}-(1-h)]x`.

Series:

`e^{-h}-(1-h)=h^2/2-h^3/6+h^4/24-...`.

The leading local error is quadratic in `h`.

## Stability

Euler amplification factor:

`R(-h)=1-h`.

Non-growth condition:

`|1-h|<=1`.

For real `h>=0`, the non-growth set is exactly:

`0<=h<=2`.

Strict decay requires:

`0<h<2`.

At `h=2`, the factor is `-1`, so magnitude is preserved rather than decayed.

At `h=3`:

- exact factor: `e^{-3}`;
- Euler factor: `-2`.

The continuous mode decays.

The discrete mode doubles in magnitude and alternates sign.

## Finite-horizon refinement

Fix `T=1`.

With `N` equal steps:

`h=1/N`,
`x_N=(1-1/N)^N`.

Exact finite values:

| N | h | Euler value |
|---:|---:|---:|
| 2 | 1/2 | 1/4 |
| 4 | 1/4 | 81/256 |
| 8 | 1/8 | 5764801/16777216 |

Exact continuous value:

`e^{-1}`.

Exact error expressions:

- `e^{-1}-1/4`;
- `e^{-1}-81/256`;
- `e^{-1}-5764801/16777216`.

Approximate values:

- `e^{-1} ≈ 0.3678794412`;
- `1/4 = 0.25`;
- `81/256 = 0.31640625`;
- `5764801/16777216 ≈ 0.3436089158`.

Absolute errors decrease across the declared finite sequence:

- approximately `0.1178794412`;
- approximately `0.0514731912`;
- approximately `0.0242705254`.

The finite table is not itself a proof of convergence for all `N`.

## Invertibility versus time reversibility

Take `h=1/2`.

Forward Euler:

`Psi_h(x)=(1/2)x`.

This map is invertible:

`Psi_h^{-1}(x)=2x`.

The same Euler formula with negative step is

`Psi_{-h}(x)=(3/2)x`.

Therefore

`Psi_{-h}(Psi_h(x))=(3/4)x`.

Since

`3/4 != 1`,

the method is not time reversible even though the forward map is invertible.

For comparison, the exact flow satisfies

`Phi_{-h}(Phi_h(x))=x`.

## Exact replay

```python
from fractions import Fraction
from math import exp

vals = {}
for N in (2, 4, 8):
    h = Fraction(1, N)
    xN = (1 - h) ** N
    vals[N] = xN

h = Fraction(1, 2)
forward = 1 - h
negative_step = 1 + h
round_trip = forward * negative_step
true_inverse = 1 / forward

print(vals)
print("round_trip=", round_trip)
print("true_inverse=", true_inverse)
print("unstable_factor_h3=", 1 - 3)
print("exact_T1=", exp(-1))
```

Expected exact rational outputs include:

```text
{2: Fraction(1, 4), 4: Fraction(81, 256), 8: Fraction(5764801, 16777216)}
round_trip= 3/4
true_inverse= 2
unstable_factor_h3= -2
```

## Claim boundary

This witness proves only the declared scalar finite calculations.

It does not prove that arbitrary residual networks converge to ODE solutions, that greater network depth reduces approximation error, that forward numerical stability guarantees training stability, or that an invertible neural architecture is a symmetric numerical integrator.
