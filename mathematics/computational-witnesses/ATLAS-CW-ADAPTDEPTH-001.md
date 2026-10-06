# ATLAS-CW-ADAPTDEPTH-001 — Adaptive Error-Control Witnesses

**Chapter:** ATLAS-CH-ADAPTDEPTH-001  
**Witness class:** exact finite replay

## W1. Embedded Euler/Heun error witness

Consider

\[
y'(t)=t,
\qquad
y(0)=0.
\]

Exact solution:

\[
y(t)=t^2/2.
\]

For one step of length \(h\):

Euler gives

\[
y_E=0.
\]

Heun gives

\[
y_H=h^2/2.
\]

Therefore

\[
y_H=y(h)
\]

and

\[
\widehat e
=
|y_H-y_E|
=
h^2/2.
\]

For this witness the embedded difference is exactly the Euler one-step error.

## W2. Rejection and step shrinkage

Set

\[
\tau=1/8.
\]

At \(h=1\),

\[
\widehat e=1/2>1/8.
\]

Reject.

For low-order \(p=1\), use the idealized unit-safety update

\[
h_{\mathrm{new}}
=
h(\tau/\widehat e)^{1/2}.
\]

Then

\[
h_{\mathrm{new}}
=
1\sqrt{(1/8)/(1/2)}
=
1/2.
\]

At \(h=1/2\),

\[
\widehat e
=
(1/2)^2/2
=
1/8.
\]

The retry meets tolerance exactly.

## W3. Perfect error ranking can still fail as error control

Use

\[
x_{k+1}=(x_k+2)/2,
\qquad
x_0=0.
\]

True fixed-point error:

\[
E_k=2^{1-k}.
\]

Define halting score

\[
q_k=4^{-k}=E_k^2/4.
\]

Thus q is strictly monotone in E and ranks depth perfectly.

At \(k=2\),

\[
q_2=1/16,
\]

while

\[
E_2=1/2.
\]

Therefore treating

\[
q_k\le1/16
\]

as if it meant

\[
E_k\le1/16
\]

causes premature stopping.

## W4. Calibrated threshold when the mapping is known

The exact mapping is

\[
E_k=2\sqrt{q_k}.
\]

For desired error tolerance \(\varepsilon\), the correct score threshold is

\[
q_k\le(\varepsilon/2)^2.
\]

For

\[
\varepsilon=1/2,
\]

the threshold is

\[
q_k\le1/16,
\]

which first holds at \(k=2\), exactly where

\[
E_2=1/2.
\]

For

\[
\varepsilon=1/16,
\]

the score threshold is

\[
q_k\le1/1024.
\]

Since

\[
q_5=1/1024
\]

and

\[
E_5=1/16,
\]

the calibrated rule stops at the correct depth for the exact recurrence.

## W5. Minimal replay code

    from fractions import Fraction

    def embedded_error(h):
        # y'=t, y(0)=0
        euler = Fraction(0)
        heun = h*h/Fraction(2)
        exact = h*h/Fraction(2)
        assert heun == exact
        return abs(heun - euler)

    tol = Fraction(1, 8)
    assert embedded_error(Fraction(1)) == Fraction(1, 2)
    assert embedded_error(Fraction(1, 2)) == tol

    def true_error(k):
        return Fraction(2, 2**k)

    def halt_score(k):
        return Fraction(1, 4**k)

    assert true_error(2) == Fraction(1, 2)
    assert halt_score(2) == Fraction(1, 16)
    assert halt_score(2) == true_error(2)**2 / 4

    # Correct score threshold for epsilon = 1/16
    eps = Fraction(1, 16)
    q_threshold = eps*eps/Fraction(4)
    assert q_threshold == Fraction(1, 1024)
    assert halt_score(5) == q_threshold
    assert true_error(5) == eps

## Claim boundary

This witness verifies only the exact finite identities above.

It does not establish:

- that Euler/Heun differences are exact local errors for arbitrary ODEs;
- that an embedded estimator guarantees a global error bound without further hypotheses;
- that a learned halting score is related to task or numerical error;
- that perfect ranking implies calibrated magnitude;
- that adaptive step selection minimizes compute;
- that neural depth is a numerical time mesh unless a reference dynamics/discretization is declared.
