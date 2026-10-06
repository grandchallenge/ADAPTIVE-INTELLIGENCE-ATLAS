# ATLAS-CW-RPO-001 — Relative-Position Operator Witness

## Purpose

This exact finite witness verifies:

1. Fourier diagonalization of two four-position cyclic relative-position operators;
2. the DC component;
3. identical singular-value multisets with different labeled frequency profiles;
4. different DC-only approximation errors across heads.

## Exact replay

\`\`\`python
import cmath
import math

L = 4

kappa_A = [1.0, 0.5, 0.0, 0.5]
kappa_B = [1.0, -0.5, 0.0, -0.5]

def eigenvalues(kappa):
    out = []
    for k in range(L):
        z = sum(
            kappa[d] * cmath.exp(2j * math.pi * k * d / L)
            for d in range(L)
        )
        out.append(z)
    return out

lam_A = eigenvalues(kappa_A)
lam_B = eigenvalues(kappa_B)

def clean(z):
    r = 0.0 if abs(z.real) < 1e-12 else z.real
    i = 0.0 if abs(z.imag) < 1e-12 else z.imag
    return complex(r, i)

lam_A = [clean(z) for z in lam_A]
lam_B = [clean(z) for z in lam_B]

assert lam_A == [2+0j, 1+0j, 0j, 1+0j]
assert lam_B == [0j, 1+0j, 2+0j, 1+0j]

sv_A = sorted((abs(z) for z in lam_A), reverse=True)
sv_B = sorted((abs(z) for z in lam_B), reverse=True)

assert sv_A == [2.0, 1.0, 1.0, 0.0]
assert sv_B == [2.0, 1.0, 1.0, 0.0]

energy_A = sum(abs(z) ** 2 for z in lam_A)
energy_B = sum(abs(z) ** 2 for z in lam_B)

q_A = [abs(z) ** 2 / energy_A for z in lam_A]
q_B = [abs(z) ** 2 / energy_B for z in lam_B]

assert all(abs(a-b) < 1e-12 for a, b in zip(q_A, [2/3, 1/6, 0, 1/6]))
assert all(abs(a-b) < 1e-12 for a, b in zip(q_B, [0, 1/6, 2/3, 1/6]))

dc_A = lam_A[0]
dc_B = lam_B[0]

assert dc_A == 2+0j
assert dc_B == 0j

fro_dc_error_A = math.sqrt(sum(abs(lam_A[k])**2 for k in range(1, L)))
fro_dc_error_B = math.sqrt(sum(abs(lam_B[k])**2 for k in range(1, L)))

op_dc_error_A = max(abs(lam_A[k]) for k in range(1, L))
op_dc_error_B = max(abs(lam_B[k]) for k in range(1, L))

assert abs(fro_dc_error_A - math.sqrt(2)) < 1e-12
assert abs(fro_dc_error_B - math.sqrt(6)) < 1e-12
assert op_dc_error_A == 1.0
assert op_dc_error_B == 2.0

print("RPO witness: PASS")
\`\`\`

Expected output:

\`\`\`text
RPO witness: PASS
\`\`\`

## Exact values

Head A:

- kernel: \((1,\tfrac12,0,\tfrac12)\);
- eigenvalues: \((2,1,0,1)\);
- mode-energy profile: \((2/3,1/6,0,1/6)\);
- DC eigenvalue: \(2\);
- DC-only Frobenius error: \(\sqrt2\);
- DC-only operator-norm error: \(1\).

Head B:

- kernel: \((1,-\tfrac12,0,-\tfrac12)\);
- eigenvalues: \((0,1,2,1)\);
- mode-energy profile: \((0,1/6,2/3,1/6)\);
- DC eigenvalue: \(0\);
- DC-only Frobenius error: \(\sqrt6\);
- DC-only operator-norm error: \(2\).

Both heads have the same unordered singular-value multiset:

\[
(2,1,1,0).
\]

## Claim boundary

The witness proves only these finite cyclic-operator facts.

It does not establish task-level head specialization, realistic periodic sequence boundaries, or universal usefulness of Fourier truncation.
