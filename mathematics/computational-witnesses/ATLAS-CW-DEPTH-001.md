# ATLAS-CW-DEPTH-001 — Depth as Approximation Time

**Chapter:** ATLAS-CH-DEPTH-001  
**Witness class:** exact deterministic contraction computation

## Recurrence

Start at

x_0=0

and iterate

x_{k+1}=(x_k+2)/2.

The unique fixed point of this affine contraction is

x*=2.

## Closed form

Subtract the fixed point:

x_{k+1}-2
=
(1/2)(x_k-2).

Therefore

x_k-2
=
-2^{1-k}

and

x_k
=
2(1-2^{-k}).

The exact error is

e_k
=
|x_k-2|
=
2^{1-k}.

## Exact table

k=0:
x_k=0,
e_k=2.

k=1:
x_k=1,
e_k=1.

k=2:
x_k=3/2,
e_k=1/2.

k=3:
x_k=7/4,
e_k=1/4.

k=4:
x_k=15/8,
e_k=1/8.

k=5:
x_k=31/16,
e_k=1/16.

## Tolerance-driven stopping

For epsilon in (0,2), stop at the smallest integer k satisfying

e_k <= epsilon.

Since

e_k=2^{1-k},

the exact stopping depth is

tau(epsilon)
=
ceil(log_2(2/epsilon)).

For dyadic tolerances:

epsilon=1/2 -> tau=2;

epsilon=1/4 -> tau=3;

epsilon=1/16 -> tau=5.

## Replay procedure

    from fractions import Fraction

    x = Fraction(0, 1)
    target = Fraction(2, 1)

    for k in range(6):
        print(k, x, abs(target - x))
        x = (x + target) / 2

Expected output:

    0 0 2
    1 1 1
    2 3/2 1/2
    3 7/4 1/4
    4 15/8 1/8
    5 31/16 1/16

## What the witness establishes

The same transformation can be run for a fixed number of steps or until a declared tolerance is met.

The recurrence is unchanged.

The stopping policy changes the realized depth.

This is one exact example of depth acting as computational approximation time.

## Claim boundary

The witness proves only the stated scalar recurrence, closed form, error formula, and dyadic stopping depths.

It does not show that arbitrary deep networks are contractions, that learned halting scores are calibrated numerical error estimates, that more depth always improves a task, or that adaptive depth necessarily reduces wall-clock time.
