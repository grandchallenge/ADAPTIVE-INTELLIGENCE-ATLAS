# ATLAS-CW-CPS-001 — Exact Coupling-Phase Spectroscopy Witness

**Chapter:** ATLAS-CH-CPS-001  
**Purpose:** exact replay of a finite augmented-state spectroscopy toy and its discovery/freeze/heldout prediction protocol.

## W1. Momentum Jacobian family

Use:

\[
J(h)
=
\begin{pmatrix}
1-\frac h{10} & -\frac9{100}\\
h & \frac9{10}
\end{pmatrix}.
\]

This is the fixed-\(\eta=1/10,\beta=9/10\) scalar-quadratic momentum Jacobian inherited from OPTDYN.

## W2. Exact determinant and trace

For every \(h\):

\[
\boxed{
\det J(h)=\frac9{10}.
}
\]

Also:

\[
\boxed{
\operatorname{tr}J(h)
=
\frac{19}{10}-\frac h{10}.
}
\]

Define:

\[
\kappa(J)
=
1+\det J-\operatorname{tr}J.
\]

Hence:

\[
\boxed{
\kappa(J(h))=\frac h{10}.
}
\]

## W3. Four synthetic windows

Use:

| window | role | \(h\) | \(\kappa\) | synthetic next-window label |
|---|---|---:|---:|---:|
| d0 | discovery | 2 | \(1/5\) | 0 |
| d1 | discovery | 8 | \(4/5\) | 1 |
| h0 | heldout | 3 | \(3/10\) | 0 |
| h1 | heldout | 7 | \(7/10\) | 1 |

These labels are synthetic.

They are not GSD observations.

## W4. Discovery freeze

Using discovery windows only:

\[
\frac15<\frac12<\frac45.
\]

Freeze:

\[
\tau=\frac12.
\]

Predict:

\[
\widehat Y
=
\mathbf 1\{\kappa>\tau\}.
\]

No heldout label participates in threshold selection.

## W5. Heldout replay

For h0:

\[
\frac3{10}<\frac12
\]

so:

\[
\widehat Y=0.
\]

For h1:

\[
\frac7{10}>\frac12
\]

so:

\[
\widehat Y=1.
\]

Therefore:

\[
\boxed{
(\widehat Y_{h0},\widehat Y_{h1})
=
(0,1).
}
\]

The synthetic heldout labels are recovered exactly.

## W6. Spectral-radius control

The four exact traces are:

\[
\operatorname{tr}J(2)=\frac{17}{10},
\]

\[
\operatorname{tr}J(3)=\frac85,
\]

\[
\operatorname{tr}J(7)=\frac65,
\]

\[
\operatorname{tr}J(8)=\frac{11}{10}.
\]

Their characteristic discriminants are:

\[
\Delta_2=-\frac{71}{100},
\]

\[
\Delta_3=-\frac{26}{25},
\]

\[
\Delta_7=-\frac{54}{25},
\]

\[
\Delta_8=-\frac{239}{100}.
\]

All are negative.

Therefore each matrix has a complex-conjugate eigenvalue pair.

Since:

\[
\det J=\frac9{10},
\]

the modulus of each eigenvalue is:

\[
\sqrt{\frac9{10}}.
\]

Hence:

\[
\boxed{
\rho(J(2))
=
\rho(J(3))
=
\rho(J(7))
=
\rho(J(8))
=
\sqrt{\frac9{10}}.
}
\]

A spectral-radius-only rule therefore cannot distinguish the four toy windows.

## W7. Exact matrix contrast

For discovery no-transition window:

\[
J(2)
=
\begin{pmatrix}
\frac45&-\frac9{100}\\
2&\frac9{10}
\end{pmatrix}.
\]

For discovery transition window:

\[
J(8)
=
\begin{pmatrix}
\frac15&-\frac9{100}\\
8&\frac9{10}
\end{pmatrix}.
\]

They share the same determinant and spectral radius.

They do not share the same trace or coupling coordinate.

This is the finite reason the toy calls for a multi-coordinate spectroscopy view rather than one universal scalar.

## W8. Real GSD boundary

The exact public GSD source lock records:

- one confirmed OLMo2-1B behavioural transition;
- a current GSD-WP04 CPS lane;
- no optimizer/trainer/scheduler/gradient/update-direction artifacts at the exact public transition-local revisions;
- current disposition BLOCKED_EXTERNAL_ARTIFACT_ABSENT.

Therefore this computational witness must not be interpreted as a replay of the GSD transition.

It is only a protocol witness.

## W9. Minimal exact replay code

    from fractions import Fraction as F

    def matrix(h):
        return (
            (F(1) - F(h, 10), -F(9, 100)),
            (F(h), F(9, 10)),
        )

    def trace(M):
        return M[0][0] + M[1][1]

    def det(M):
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]

    def kappa(M):
        return F(1) + det(M) - trace(M)

    expected_discriminants = {
        2: -F(71, 100),
        3: -F(26, 25),
        7: -F(54, 25),
        8: -F(239, 100),
    }

    for h in (2, 3, 7, 8):
        M = matrix(h)
        assert det(M) == F(9, 10)
        assert kappa(M) == F(h, 10)

        disc = trace(M) ** 2 - F(18, 5)
        assert disc == expected_discriminants[h]
        assert disc < 0

    discovery = [
        (2, 0),
        (8, 1),
    ]

    heldout = [
        (3, 0),
        (7, 1),
    ]

    tau = F(1, 2)

    assert kappa(matrix(discovery[0][0])) < tau
    assert kappa(matrix(discovery[1][0])) > tau

    predictions = [
        int(kappa(matrix(h)) > tau)
        for h, _ in heldout
    ]

    labels = [label for _, label in heldout]

    assert predictions == labels == [0, 1]

## W10. Protocol disposition

The replay code validates:

- exact matrix construction;
- determinant identity;
- coupling-coordinate identity;
- negative discriminants;
- discovery-only threshold placement;
- heldout toy predictions.

It does not produce a scientific GSD-WP04 signal disposition.

The public GSD-WP04 disposition remains:

\[
\boxed{
\mathrm{BLOCKED\_EXTERNAL\_ARTIFACT\_ABSENT}.
}
\]

## Claim boundary

This witness establishes only exact properties of the declared scalar-quadratic momentum family and a synthetic discovery/freeze/heldout prediction protocol.

It does not establish:

- that \(\kappa\) predicts real neural-training transitions;
- that the GSD behavioural transition is caused by optimizer state;
- that a CPS signal exists in the public GSD transition window;
- that missing optimizer artifacts imply no CPS signal;
- that equal spectral radius implies equivalent local dynamics;
- that one local Jacobian globally models stochastic nonlinear training;
- that two correctly classified synthetic heldout windows constitute empirical validation.
