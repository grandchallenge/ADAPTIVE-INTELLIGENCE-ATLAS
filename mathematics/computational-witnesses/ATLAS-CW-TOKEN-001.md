# ATLAS-CW-TOKEN-001 — Tokenization Boundary Witnesses

## Purpose

This finite replay checks four distinctions:

1. byte length can differ from Unicode codepoint length;
2. normalization can change both counts;
3. one unigram vocabulary can admit multiple valid segmentations;
4. token count and idealized code length need not order sequences the same way.

## Exact replay

```python
import unicodedata
import math

nfc = "é"
nfd = unicodedata.normalize("NFD", nfc)

assert len(nfc) == 1
assert len(nfc.encode("utf-8")) == 2
assert len(nfd) == 2
assert len(nfd.encode("utf-8")) == 3

p = {"ab": 1/2, "a": 1/4, "b": 1/4}
segmentations = [
    ["ab", "ab"],
    ["a", "b", "ab"],
    ["ab", "a", "b"],
    ["a", "b", "a", "b"],
]

weights = []
for s in segmentations:
    w = 1.0
    for piece in s:
        w *= p[piece]
    weights.append(w)

expected = [1/4, 1/32, 1/32, 1/256]
assert all(abs(a-b) < 1e-15 for a, b in zip(weights, expected))

Z = sum(weights)
assert abs(Z - 81/256) < 1e-15

q = [w/Z for w in weights]
expected_q = [64/81, 8/81, 8/81, 1/81]
assert all(abs(a-b) < 1e-15 for a, b in zip(q, expected_q))

# Token count and code length can disagree.
len_A = 2
bits_A = -2 * math.log2(1/16)
len_B = 3
bits_B = -3 * math.log2(1/2)

assert len_A < len_B
assert bits_A == 8
assert bits_B == 3
assert bits_A > bits_B

# Toy fertility.
F_A = 5 / 2
F_B = 2 / 2
assert F_A == 2.5
assert F_B == 1.0

print("TOKEN witness: PASS")
```

Expected output:

```text
TOKEN witness: PASS
```

## Exact values

- NFC `é`: 1 codepoint, 2 UTF-8 bytes;
- decomposed `e` + combining acute: 2 codepoints, 3 UTF-8 bytes;
- unigram segmentation weights: \((1/4,1/32,1/32,1/256)\);
- normalized segmentation probabilities: \((64/81,8/81,8/81,1/81)\);
- two-token toy sequence code length: 8 bits under the declared model;
- three-token toy sequence code length: 3 bits;
- toy fertility values: 2.5 versus 1.0.

## Claim boundary

These witnesses prove only the declared finite separations. They do not establish tokenizer quality, multilingual fairness, morphological adequacy, or downstream model performance.
