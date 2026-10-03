# ATLAS-CW-EXPLORE-001 — Two-Step Value of Information Witness

**Chapter:** ATLAS-CH-EXPLORE-001  
**Witness class:** exact finite rational computation  
**Purpose:** show that an action with lower immediate expected reward can have higher finite-horizon value because its observation changes the next decision.

## Model

Latent parameter:

`theta in {0,1}`.

Prior:

`P(theta=1)=2/5`,
`P(theta=0)=3/5`.

Known action `S`:

- deterministic reward `1/2`;
- no information about `theta`.

Unknown action `U`:

- reward `theta`;
- one observation reveals `theta` exactly.

Horizon: two actions.

## Exact derivation

Immediate expected values:

`E[r(S)]=1/2`.

`E[r(U)]=2/5`.

Thus `U` has lower immediate expected reward by

`1/2-2/5=1/10`.

If `S` is chosen first, the belief does not change, so `S` is again optimal at step 2:

`V(S-first)=1`.

If `U` is chosen first:

- with probability `2/5`, observe 1 and choose `U` at step 2 for reward 1;
- with probability `3/5`, observe 0 and choose `S` at step 2 for reward `1/2`.

Expected step-2 reward:

`(2/5)(1)+(3/5)(1/2)=7/10`.

Total:

`V(U-first)=2/5+7/10=11/10`.

Future decision value of the observation:

`7/10-1/2=1/5`.

Net advantage after paying the immediate exploration cost:

`1/5-1/10=1/10`.

## Information gain

Pulling `U` reveals `theta` exactly.

With base-2 logarithms,

`IG(U)=h_2(2/5)>0`.

Pulling `S` leaves the posterior unchanged:

`IG(S)=0`.

The information gain is measured in bits.

The value of information is measured here in reward units.

They are not the same quantity.

## Exact replay

```python
from fractions import Fraction

p = Fraction(2, 5)
safe = Fraction(1, 2)
unknown_now = p

safe_total = safe + safe
future_after_unknown = p * 1 + (1 - p) * safe
unknown_total = unknown_now + future_after_unknown
exploration_cost = safe - unknown_now
value_of_information = future_after_unknown - safe
net_advantage = unknown_total - safe_total

print(f"safe_total={safe_total}")
print(f"unknown_total={unknown_total}")
print(f"exploration_cost={exploration_cost}")
print(f"value_of_information={value_of_information}")
print(f"net_advantage={net_advantage}")
```

Expected output:

```text
safe_total=1
unknown_total=11/10
exploration_cost=1/10
value_of_information=1/5
net_advantage=1/10
```

## Claim boundary

This witness proves only the exact two-step Bayesian decision statement above.

It does not prove that exploration is always beneficial, that information gain alone determines optimal exploration, that any named exploration algorithm must choose `U` in an analogous model, or that an informative action satisfies an independently declared constraint.
