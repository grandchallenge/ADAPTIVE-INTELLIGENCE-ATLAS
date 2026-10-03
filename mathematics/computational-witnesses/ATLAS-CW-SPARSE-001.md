# ATLAS-CW-SPARSE-001 — Conditional Compute Does Not Determine Latency

**Chapter:** ATLAS-CH-SPARSE-001  
**Witness class:** exact finite deterministic resource accounting  
**Purpose:** show that input-dependent execution can reduce average arithmetic without reducing peak arithmetic, and that lower arithmetic does not imply lower latency without a hardware cost model.

## Systems

### Fixed baseline

Four blocks execute for every input.

Each block contributes 10 arithmetic units.

Assume the four-block path is fused into one launch.

Resource pair:

`C_fixed=(40,1)`.

Coordinates are:

- arithmetic units;
- launches.

### Conditional system

Paths:

- `x1 -> {1,4}`;
- `x2 -> {1,2,4}`;
- `x3 -> {1,4}`;
- `x4 -> {1,2,3,4}`.

Assume one router launch and one launch per active block.

Resource pairs:

- `x1: (20,3)`;
- `x2: (30,4)`;
- `x3: (20,3)`;
- `x4: (40,5)`.

Average:

`C_cond=(55/2,15/4)`.

## Arithmetic comparison

Average arithmetic reduction:

`1-(55/2)/40=5/16=31.25%`.

Peak conditional arithmetic:

`40`.

Therefore:

- average arithmetic decreases;
- peak arithmetic is unchanged.

## Hardware model A

Let

`T_A(F,K)=F`.

Then:

- fixed latency proxy: `40`;
- conditional average: `55/2=27.5`.

Conditional wins.

## Hardware model B

Let

`T_B(F,K)=F/10+10K`.

Then:

fixed:

`40/10+10=14`.

conditional average:

`(55/2)/10+10(15/4)`

`=11/4+150/4`

`=161/4=40.25`.

Fixed wins.

## Exact replay

```python
from fractions import Fraction

fixed = (Fraction(40), Fraction(1))
cond = [
    (Fraction(20), Fraction(3)),
    (Fraction(30), Fraction(4)),
    (Fraction(20), Fraction(3)),
    (Fraction(40), Fraction(5)),
]

avg_f = sum(x[0] for x in cond) / len(cond)
avg_k = sum(x[1] for x in cond) / len(cond)
peak_f = max(x[0] for x in cond)
reduction = 1 - avg_f / fixed[0]

def latency(pair, alpha, beta):
    f, k = pair
    return alpha*f + beta*k

fixed_A = latency(fixed, Fraction(1), Fraction(0))
cond_A = latency((avg_f, avg_k), Fraction(1), Fraction(0))

fixed_B = latency(fixed, Fraction(1,10), Fraction(10))
cond_B = latency((avg_f, avg_k), Fraction(1,10), Fraction(10))

print("avg_cond=", (avg_f, avg_k))
print("peak_flops=", peak_f)
print("reduction=", reduction)
print("model_A=", fixed_A, cond_A)
print("model_B=", fixed_B, cond_B)
```

Expected exact output:

```text
avg_cond= (Fraction(55, 2), Fraction(15, 4))
peak_flops= 40
reduction= 5/16
model_A= 40 55/2
model_B= 14 161/4
```

## Claim boundary

This witness proves only the finite resource calculations above.

It does not claim that real hardware latency is linear in arithmetic units and launch count; the two scalarizations are deliberately toy cost models used to prove non-identifiability of latency from arithmetic count alone. It does not establish a quality result, a universal routing advantage, or a particular speedup for SkipNet, DynamicViT, SACT, or any production accelerator.
