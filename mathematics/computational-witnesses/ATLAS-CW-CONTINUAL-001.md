# ATLAS-CW-CONTINUAL-001 — Two Conflicting Tasks in One Shared Parameter

**Chapter:** ATLAS-CH-CONTINUAL-001  
**Witness class:** exact scalar optimization  
**Purpose:** make sequential interference and the retention/adaptation tradeoff exact.

## Task losses

Task A:

`L_A(w)=(1/2)(w+1)^2`.

Task B:

`L_B(w)=(1/2)(w-1)^2`.

The unique task optima are

`w_A^*=-1`

and

`w_B^*=1`.

No single scalar `w` makes both losses zero.

## Sequential training without protection

After Task A:

`w=-1`,
`L_A=0`.

After training Task B to its own optimum:

`w=1`,
`L_B=0`,
`L_A=2`.

Exact old-task loss increase:

`2`.

## Quadratic retention penalty

Take scalar importance `F=1`.

Define

`J_lambda(w)
=
L_B(w)
+
(lambda/2)(w+1)^2`.

The exact minimizer is

`w_lambda=(1-lambda)/(1+lambda)`.

At that point:

`L_A(w_lambda)=2/(1+lambda)^2`.

`L_B(w_lambda)=2lambda^2/(1+lambda)^2`.

For `lambda=1`:

`w=0`,
`L_A=1/2`,
`L_B=1/2`.

Thus the old-task loss is reduced from `2` to `1/2`, but exact adaptation to Task B is sacrificed.

## Equal-weight replay in this toy

Exact equal-weight rehearsal minimizes

`L_A(w)+L_B(w)`.

Since

`L_A(w)+L_B(w)=w^2+1`,

the minimizer is also

`w=0`.

This equality with the `lambda=1,F=1` retention objective is special to the chosen quadratic witness.

Replay and EWC are not generally equivalent.

## Parameter isolation contrast

Allow two task-selected parameters.

Choose

`w_A=-1`

for Task A and

`w_B=1`

for Task B.

Then each task can attain zero loss under the correct selector.

This uses more capacity and assumes task-conditioned routing.

## Exact replay

```python
from fractions import Fraction

def losses(w):
    la = Fraction(1,2) * (w + 1) ** 2
    lb = Fraction(1,2) * (w - 1) ** 2
    return la, lb

# Sequential task optima.
print("A optimum:", losses(Fraction(-1,1)))
print("B optimum:", losses(Fraction(1,1)))

# lambda = 1 retention/replay coincidence.
w = Fraction(0,1)
print("lambda1:", losses(w))

# A few exact lambda values.
for lam in (Fraction(0,1), Fraction(1,1), Fraction(3,1)):
    wlam = (1 - lam) / (1 + lam)
    la, lb = losses(wlam)
    print(lam, wlam, la, lb)
```

Expected exact outputs include:

```text
A optimum: (0, 2)
B optimum: (2, 0)
lambda1: (1/2, 1/2)
0 1 2 0
1 0 1/2 1/2
3 -1/2 1/8 9/8
```

## Claim boundary

This witness proves only the exact scalar statements above.

It does not prove that EWC, replay, GEM, or parameter isolation is universally superior; that real neural-network task losses are quadratic; that the Fisher diagonal is an exact importance oracle; or that a task-selected two-parameter solution transfers to class-incremental evaluation without task identity.
