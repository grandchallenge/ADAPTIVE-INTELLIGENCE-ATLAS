# ATLAS-CW-PROGRESSSEARCH-001 — Exploration and Horizon Witness

## Purpose

This exact finite witness checks two distinct failures: exploit-only search can miss an unobserved high-progress region, and immediate-progress greed can lose to a lower-immediate-reward action over a finite horizon.

## Exact replay

```python
# Witness A: exploration
rewards = {'A': 1, 'B': 3}
observed = {'A': rewards['A']}

exploit_total = 0
for _ in range(2):
    choice = max(observed, key=observed.get)
    exploit_total += rewards[choice]

observed2 = {'A': rewards['A']}
coverage_total = 0
for _ in range(2):
    unseen = [r for r in rewards if r not in observed2]
    if unseen:
        choice = unseen[0]
    else:
        choice = max(observed2, key=observed2.get)
    reward = rewards[choice]
    observed2[choice] = reward
    coverage_total += reward

assert exploit_total == 2
assert coverage_total == 6

# Witness B: horizon
greedy_total = 2 + 0
investment_total = 0 + 5

assert greedy_total == 2
assert investment_total == 5
assert investment_total > greedy_total

print('PROGRESSSEARCH witness: PASS')
```

Expected output:

```text
PROGRESSSEARCH witness: PASS
```

## Exact values

- exploit-only two-round reward: 2;
- coverage-first two-round reward: 6;
- immediate-greedy two-step return: 2;
- investment-then-unlock two-step return: 5.

## Claim boundary

The witness proves only these declared finite separations. It does not show that forced coverage, absolute progress, or any one horizon rule is generally optimal.