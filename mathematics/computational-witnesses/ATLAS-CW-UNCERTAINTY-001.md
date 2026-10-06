# ATLAS-CW-UNCERTAINTY-001 — Finite Uncertainty Witnesses

Chapter: ATLAS-CH-UNCERTAINTY-001
Witness class: exact finite probability replay

## W1. Same predictive entropy, opposite decomposition

### Model A

Theta is fixed.

Y ~ Bernoulli(1/2).

Therefore:

\[
H(Y)=1,
\]

\[
E[H(Y\mid Theta)]=1,
\]

\[
I(Y;Theta)=0.
\]

### Model B

Theta ~ Bernoulli(1/2).

Y=Theta.

Marginally Y ~ Bernoulli(1/2), hence:

\[
H(Y)=1.
\]

Conditionally Y is deterministic, hence:

\[
E[H(Y\mid Theta)]=0,
\]

\[
I(Y;Theta)=1.
\]

Same predictive law; different decomposition.

## W2. Two calibrated predictors with different Brier risk

Let X be a or b with probability 1/2 each.

\[
P(Y=1\mid a)=0.9,
\qquad
P(Y=1\mid b)=0.1.
\]

Predictor S0 outputs 0.5 everywhere.

Since the marginal positive rate is 0.5, S0 is calibrated.

Predictor S1 outputs 0.9 on a and 0.1 on b.

S1 is also calibrated.

Brier risk:

\[
R(S0)=0.25,
\]

\[
R(S1)=0.09.
\]

Therefore calibration does not determine sharpness or Brier performance.

## W3. Split-conformal rank witness

Let n=4 and alpha=0.2.

\[
k=\lceil(n+1)(1-\alpha)\rceil=4.
\]

Under exchangeability and no ties, the future score rank among five scores is uniform.

The future score is covered exactly for ranks 1 through 4.

Thus

\[
P(\text{coverage})=4/5=0.8.
\]

The witness establishes marginal rank coverage only.

## W4. Selective risk/coverage witness

Take five equally weighted examples with error indicators

\[
(0,0,0,1,1).
\]

Accept all five:

\[
coverage=1,
\qquad
risk=2/5.
\]

Accept only the first three:

\[
coverage=3/5,
\qquad
risk=0.
\]

Risk falls because the evaluated/accepted population changes.

## W5. Minimal exact replay

The following arithmetic can be checked directly:

    from fractions import Fraction
    from math import ceil

    # Calibration/sharpness witness
    brier_constant = Fraction(1, 4)
    brier_sharp = Fraction(9, 100)
    assert brier_sharp < brier_constant

    # Conformal rank witness
    n = 4
    alpha = Fraction(1, 5)
    k = ceil((n + 1) * (1 - alpha))
    assert k == 4
    assert Fraction(k, n + 1) == Fraction(4, 5)

    # Selective prediction witness
    errors = [0, 0, 0, 1, 1]
    full_risk = Fraction(sum(errors), len(errors))
    accepted = errors[:3]
    selective_risk = Fraction(sum(accepted), len(accepted))
    coverage = Fraction(len(accepted), len(errors))
    assert full_risk == Fraction(2, 5)
    assert selective_risk == 0
    assert coverage == Fraction(3, 5)

## Claim boundary

This witness verifies only the exact finite probability identities and counterexamples stated above. It does not establish population calibration from a finite sample, exact Bayesian inference, ensemble posterior semantics, conformal validity without exchangeability, conditional conformal coverage, or distribution-shift robustness.
