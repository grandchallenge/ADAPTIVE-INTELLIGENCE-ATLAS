# ATLAS-CW-EXPERIMENT-001 — Confounded Aggregate versus Controlled Contrast

**Chapter:** ATLAS-CH-EXPERIMENT-001  
**Witness class:** exact deterministic finite computation  
**Purpose:** show that an uncontrolled aggregate comparison can reverse the sign of a treatment effect when assignment is confounded with a nuisance stratum.

## Finite population

There are 20 units.

Ten are in an easy stratum and ten are in a hard stratum.

Potential outcomes are:

| Stratum | Y(0) | Y(1) |
|---|---:|---:|
| easy | 10 | 11 |
| hard | 0 | 1 |

Every unit therefore has treatment effect +1.

The exact finite-population average treatment effect is +1.

## Observed assignment

Treatment group:

- 1 easy unit;
- 9 hard units.

Control group:

- 9 easy units;
- 1 hard unit.

## Exact arithmetic

Treatment mean:

`(11 + 9*1)/10 = 2`.

Control mean:

`(9*10 + 0)/10 = 9`.

Naive aggregate contrast:

`2 - 9 = -7`.

Within easy stratum:

`11 - 10 = +1`.

Within hard stratum:

`1 - 0 = +1`.

Equal-stratum standardized contrast:

`(1/2)(+1) + (1/2)(+1) = +1`.

## Minimal executable replay

```python
from fractions import Fraction

treated = [11] + [1] * 9
control = [10] * 9 + [0]

naive = Fraction(sum(treated), len(treated)) - Fraction(sum(control), len(control))
easy = Fraction(11 - 10, 1)
hard = Fraction(1 - 0, 1)
standardized = (easy + hard) / 2

print(f"naive={naive}")
print(f"easy={easy}")
print(f"hard={hard}")
print(f"standardized={standardized}")
```

Expected output:

```text
naive=-7
easy=1
hard=1
standardized=1
```

## Interpretation

The aggregate comparison says treatment is worse by 7.

The controlled within-stratum comparison says treatment is better by 1 in both strata.

The reversal is produced entirely by assignment imbalance across the nuisance stratum.

## Claim boundary

This witness proves only the exact finite statement encoded above:

**for this 20-unit deterministic table and assignment, the uncontrolled aggregate contrast is -7 while both within-stratum contrasts and the equal-stratum standardized contrast are +1.**

It does not prove that stratification always identifies causal effects, that all observational comparisons can be repaired by blocking, that every Simpson-type reversal has this mechanism, or that randomized experiments are automatically valid in every other respect.
