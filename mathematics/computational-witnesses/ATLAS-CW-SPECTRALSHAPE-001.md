# ATLAS-CW-SPECTRALSHAPE-001 — Exact Spectral-Shaping Witness

**Chapter:** ATLAS-CH-SPECTRALSHAPE-001

## W1. Conditioning witness

Use

\[
G=\operatorname{diag}(4,1).
\]

Its singular values are \((4,1)\), so:

\[
\kappa_2(G)=4.
\]

### Scalar normalization

\[
G_{\rm scale}
=
\operatorname{diag}(1,1/4),
\qquad
\kappa_2=4.
\]

### Upper clipping

\[
G_{\rm clip}
=
\operatorname{diag}(2,1),
\qquad
\kappa_2=2.
\]

### Polar flattening

\[
G_{\rm polar}=I_2,
\qquad
\kappa_2=1.
\]

### Explicit non-flat target

\[
G_\tau
=
\operatorname{diag}(3,2),
\qquad
\kappa_2=\frac32.
\]

## W2. Non-normal control

Use

\[
A=
\begin{pmatrix}
1/2&2\\
0&1/2
\end{pmatrix},
\qquad
N=\frac12I_2.
\]

Both have eigenvalues \(\{1/2,1/2\}\).

For

\[
e_2=(0,1)^\top,
\]

\[
Ae_2=(2,1/2)^\top,
\qquad
\|Ae_2\|_2^2=\frac{17}{4},
\]

while

\[
Ne_2=(0,1/2)^\top,
\qquad
\|Ne_2\|_2^2=\frac14.
\]

At

\[
\varepsilon=\frac14,
\]

the inherited exact non-normal pseudospectral-radius formula gives

\[
r_A
=
\sqrt{
\varepsilon(\varepsilon+2)
}
=
\frac34.
\]

For the normal scalar matrix,

\[
r_N=\varepsilon=\frac14.
\]

## W3. Minimal exact replay code

    from fractions import Fraction as F

    spectra = {
        "original": (F(4), F(1)),
        "scale": (F(1), F(1,4)),
        "clip": (F(2), F(1)),
        "polar": (F(1), F(1)),
        "target": (F(3), F(2)),
    }

    def kappa(s):
        return max(s) / min(s)

    assert kappa(spectra["original"]) == F(4)
    assert kappa(spectra["scale"]) == F(4)
    assert kappa(spectra["clip"]) == F(2)
    assert kappa(spectra["polar"]) == F(1)
    assert kappa(spectra["target"]) == F(3,2)

    A = ((F(1,2),F(2)),(F(0),F(1,2)))
    N = ((F(1,2),F(0)),(F(0),F(1,2)))
    e2 = (F(0),F(1))

    def matvec(M,x):
        return tuple(sum(M[i][j]*x[j] for j in range(len(x)))
                     for i in range(len(M)))

    def norm2(x):
        return sum(v*v for v in x)

    assert matvec(A,e2) == (F(2),F(1,2))
    assert matvec(N,e2) == (F(0),F(1,2))
    assert norm2(matvec(A,e2)) == F(17,4)
    assert norm2(matvec(N,e2)) == F(1,4)

    eps = F(1,4)
    rA2 = eps * (eps + F(2))
    rN2 = eps * eps

    assert rA2 == F(9,16)
    assert rN2 == F(1,16)

    print("SPECTRALSHAPE_EXACT_WITNESS_OK")

## Claim boundary

This witness proves only the finite singular-value maps, condition numbers, probe responses, and pseudospectral-radius identities stated above.

It does not prove that any target spectrum is universally optimal, that better instantaneous conditioning implies faster nonlinear optimization, or that shaping an update matrix controls optimizer-state dynamics or downstream task quality.
