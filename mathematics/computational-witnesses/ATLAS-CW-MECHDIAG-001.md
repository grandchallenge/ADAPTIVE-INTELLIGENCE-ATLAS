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
print("MECHDIAG witness: PASS")
```

This finite example proves that perfect decodability can coexist with zero functional dependence on the decoded coordinate. It does not establish uniqueness of any global explanation.
