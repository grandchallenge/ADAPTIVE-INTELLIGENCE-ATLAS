# ATLAS-CW-FORMAL-001 — Inductive Invariant versus Finite Testing

**Chapter:** ATLAS-CH-FORMAL-001  
**Witness class:** exact infinite-state specification + finite implementation counterexample  
**Purpose:** distinguish universal proof, finite tests, and implementation/specification conformance.

## Formal specification

State:

`x in N`.

Initial state:

`x_0=0`.

Specified transition:

`SpecStep(x)=x+2`.

Invariant:

`Even(x)`.

## Inductive proof

Base:

`x_0=0=2*0` is even.

Preservation:

assume

`x=2k`.

Then

`SpecStep(x)=2k+2=2(k+1)`,

which is even.

Therefore every state reachable from zero by finitely many specified transitions is even.

Equivalent closed form:

`x_n=2n`.

## Finite test suite

Test only:

`0 -> 2`,
`2 -> 4`,
`4 -> 6`.

All observed states satisfy the invariant.

Those successful tests establish the tested prefix.

They do not prove the infinite universal invariant by themselves.

## Divergent implementation

Define

`ImplStep(x)=x+2` for `x<6`;

`ImplStep(x)=x+1` for `x>=6`.

Starting from zero:

`0 -> 2 -> 4 -> 6 -> 7`.

The finite test suite still passes.

At state `6`, implementation and specification diverge:

`SpecStep(6)=8`.

`ImplStep(6)=7`.

The implementation then violates the invariant because `7` is odd.

## Exact replay

```python
def spec_step(x: int) -> int:
    return x + 2

def impl_step(x: int) -> int:
    return x + 2 if x < 6 else x + 1

def even(x: int) -> bool:
    return x % 2 == 0

x = 0
tested = []
for _ in range(3):
    y = impl_step(x)
    tested.append((x, y, even(y)))
    x = y

next_impl = impl_step(x)
next_spec = spec_step(x)

print("tested=", tested)
print("state_after_tests=", x)
print("next_spec=", next_spec)
print("next_impl=", next_impl)
print("impl_invariant=", even(next_impl))
```

Expected output:

```text
tested= [(0, 2, True), (2, 4, True), (4, 6, True)]
state_after_tests= 6
next_spec= 8
next_impl= 7
impl_invariant= False
```

## What is proved

The mathematical induction proves:

`forall n in N, x_n=2n`

for the declared specification.

Therefore all specified reachable states are even.

## What is only tested

The executable replay establishes three concrete implementation transitions and the subsequent counterexample.

It does not machine-check the induction theorem.

## Claim boundary

This witness proves the declared invariant for the mathematical specification by an explicit induction argument and exhibits an exact implementation counterexample after a finite passing prefix.

It does not prove that all formal systems have this structure, that a proof assistant is infallible, that testing is epistemically weak in every finite-domain setting, or that an arbitrary implementation conforms to a proved specification.
