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

# Explicit complete finite potential-outcome population:
# identity, stratum, Y(0), Y(1), for all 20 distinct units.
population = tuple(
    [(f"easy-{i}", "easy", 10, 11) for i in range(10)]
    + [(f"hard-{i}", "hard", 0, 1) for i in range(10)]
)
assert len(population) == len({unit[0] for unit in population}) == 20
assert all(y1 - y0 == 1 for _, _, y0, y1 in population)
ate = sum((y1 - y0 for _, _, y0, y1 in population), 0) / len(population)
assert ate == 1

# The one easy and nine hard treated units are specified by unique IDs.
treated_ids = {"easy-0"} | {f"hard-{i}" for i in range(9)}
treated_units = [u for u in population if u[0] in treated_ids]
control_units = [u for u in population if u[0] not in treated_ids]
assert len(treated_units) == len(control_units) == 10
assert sum(s == "easy" for _, s, _, _ in treated_units) == 1
assert sum(s == "hard" for _, s, _, _ in treated_units) == 9
assert sum(s == "easy" for _, s, _, _ in control_units) == 9
assert sum(s == "hard" for _, s, _, _ in control_units) == 1

treated = [y1 for _, _, _, y1 in treated_units]
control = [y0 for _, _, y0, _ in control_units]
naive = Fraction(sum(treated), len(treated)) - Fraction(sum(control), len(control))

# For each stratum, both intervention arms are observed.
def observed_stratum_contrast(stratum):
    yt = [y1 for _, s, _, y1 in treated_units if s == stratum]
    yc = [y0 for _, s, y0, _ in control_units if s == stratum]
    assert yt and yc
    return Fraction(sum(yt), len(yt)) - Fraction(sum(yc), len(yc))

easy = observed_stratum_contrast("easy")
hard = observed_stratum_contrast("hard")
standardized = (easy + hard) / 2
assert (naive, easy, hard, standardized) == (-7, 1, 1, 1)

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

The replay enumerates all 20 distinct units and *both* potential
outcomes for each unit, not merely four reported group means. The treatment
assignment is then formed by immutable unit IDs. Assertions check every
unit-level treatment effect, stratum counts, the observed contrasts, and the
standardized contrast. This construction is a finite counterexample, not an
identification theorem for observational data.

## Interpretation

The aggregate comparison says treatment is worse by 7.

The controlled within-stratum comparison says treatment is better by 1 in both strata.

The reversal is produced entirely by assignment imbalance across the nuisance stratum.

## Claim boundary

This witness proves only the exact finite statement encoded above:

**for this 20-unit deterministic table and assignment, the uncontrolled aggregate contrast is -7 while both within-stratum contrasts and the equal-stratum standardized contrast are +1.**

It does not prove that stratification always identifies causal effects, that all observational comparisons can be repaired by blocking, that every Simpson-type reversal has this mechanism, or that randomized experiments are automatically valid in every other respect.
