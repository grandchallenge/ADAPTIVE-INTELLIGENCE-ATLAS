# ATLAS-CW-SHIFT-001 — Exact Changed-Law and Robustness Witnesses

## Claim boundary

This witness certifies only the exact finite changed-law, importance-weight, benign-marginal-shift, conditional-shift, and adversarial-risk identities stated below. It does not prove universal distribution-shift correction, calibration transfer, conformal transfer, or adversarial robustness beyond the declared finite objects and perturbation set.

## Purpose

Replay four exact separations:
1. source calibration can fail under deployment covariate shift with predictor unchanged;
2. a substantial marginal shift can leave task risk unchanged;
3. conditional shift is not fixed by covariate importance weights;
4. clean risk and adversarial risk can differ maximally.

## Python replay

```python
from fractions import Fraction as F

# Witness A: calibration under P, failure under Q.
P = {"a": F(1,2), "b": F(1,2)}
Q = {"a": F(3,4), "b": F(1,4)}
y = {"a": F(1), "b": F(0)}
score = {"a": F(1,2), "b": F(1,2)}

p_event = sum(P[x]*y[x] for x in P)
q_event = sum(Q[x]*y[x] for x in Q)
assert p_event == F(1,2)
assert q_event == F(3,4)
assert abs(p_event-F(1,2)) == 0
assert abs(q_event-F(1,2)) == F(1,4)

brier_P = sum(P[x]*(score[x]-y[x])**2 for x in P)
brier_Q = sum(Q[x]*(score[x]-y[x])**2 for x in Q)
assert brier_P == brier_Q == F(1,4)

w = {x: Q[x]/P[x] for x in P}
assert w == {"a": F(3,2), "b": F(1,2)}
assert sum(P[x]*w[x] for x in P) == 1
assert sum(P[x]*w[x]*y[x] for x in P) == q_event

# Witness B: marginal shift without task failure.
P2 = {"u": F(1,2), "v": F(1,2)}
Q2 = {"u": F(9,10), "v": F(1,10)}
y2 = {"u": 0, "v": 1}
f2 = {"u": 0, "v": 1}
tv = F(1,2)*sum(abs(P2[x]-Q2[x]) for x in P2)
assert tv == F(2,5)
risk_P2 = sum(P2[x]*(f2[x] != y2[x]) for x in P2)
risk_Q2 = sum(Q2[x]*(f2[x] != y2[x]) for x in Q2)
assert risk_P2 == risk_Q2 == 0

# Conditional shift with unchanged X marginal.
Q3 = dict(P2)
y3 = {"u": 1, "v": 0}
risk_Q3 = sum(Q3[x]*(f2[x] != y3[x]) for x in Q3)
assert risk_Q3 == 1
assert {x: Q3[x]/P2[x] for x in P2} == {"u": F(1), "v": F(1)}

# Adversarial separation.
points = [-1, 1]
label = {-1: 0, 1: 1}
pred = {-1: 0, 1: 1}
clean = sum(F(1,2)*(pred[x] != label[x]) for x in points)
assert clean == 0
adv = sum(
    F(1,2)*max(pred[xp] != label[x] for xp in points)
    for x in points
)
assert adv == 1

print("SHIFT_EXACT_WITNESS_OK")
```

## Expected output

```text
SHIFT_EXACT_WITNESS_OK
```

## Frozen exact values

- source event rate at score 1/2: 1/2;
- target event rate at score 1/2: 3/4;
- target calibration gap: 1/4;
- source and target Brier risk in Witness A: 1/4;
- importance weights: w(a)=3/2, w(b)=1/2;
- marginal total variation in Witness B: 2/5;
- source and target 0/1 risk in Witness B: 0;
- conditional-shift target risk in control: 1;
- clean risk in adversarial witness: 0;
- adversarial risk for the declared perturbation set: 1.

## Interpretation

These are exact finite identities, not asymptotic or empirical claims. They demonstrate non-equivalence among calibration, ordinary target risk, marginal shift magnitude, conditional shift, and adversarial risk.
