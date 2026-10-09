# ATLAS-CW-MECHDIAG-001 — Decodability versus Functional Use

Let x be either -1 or +1. Define h(x)=(x,x) and f(h)=h_1. Both coordinate readers recover x exactly. Setting h_2 to zero leaves f unchanged, while setting h_1 to zero changes f. Starting from h(-x), replacing coordinate 1 by its value from h(x) restores f=x; replacing coordinate 2 does not.

```python
for x in (-1, 1):
    h = (x, x)
    assert h[0] == x and h[1] == x
    assert (h[0], 0)[0] == x
    assert (0, h[1])[0] == 0
    ref = (-x, -x)
    assert (x, ref[1])[0] == x
    assert (ref[0], x)[0] == -x
# A different output map gives a redundancy control on the binary domain.
def g(h):
    return max(h)
assert g((1, 1)) == 1
assert g((0, 1)) == 1
assert g((1, 0)) == 1
assert g((0, 0)) == 0

print("MECHDIAG witness: PASS")
```

## Independent redundancy control

For the separate binary-domain map \(G(h_1,h_2)=\max(h_1,h_2)\), a baseline state \((1,1)\) has output 1; masking either coordinate individually retains output 1, while masking both gives 0. This proves that null single-coordinate interventions need not rule out a jointly relevant component set. It does not claim that every null ablation is due to redundancy.

## Claim boundary

This finite example proves that perfect decodability can coexist with zero functional dependence on the decoded coordinate. It does not establish uniqueness of any global explanation.
