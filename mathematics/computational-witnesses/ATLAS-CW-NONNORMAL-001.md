# ATLAS-CW-NONNORMAL-001 — Non-normal Transient-Growth Witness

**Chapter:** `ATLAS-CH-NONNORMAL-001`  
**System:** Wolfram Language 15.0.1 for Linux x86 (64-bit), July 2 2026  
**System ID:** Linux-x86-64  
**MaxExtraPrecision:** 50  
**Norm:** spectral/operator (2)-norm  
**Figure source:** `figures/wolfram/ATLAS-FIG-PSPECTRUM-001.wl`

## Matrix

[
A=
egin{pmatrix}
4/5&4\
0&4/5
end{pmatrix},
qquad
N_0=(4/5)I.
]

## Symbolic power check

Wolfram returned, for integer (nge1),

[
A^n
=
egin{pmatrix}
(5/4)^{-n}&4^n5^{1-n}n\
0&(5/4)^{-n}
end{pmatrix},
]

which simplifies to

[
egin{pmatrix}
(4/5)^n&4n(4/5)^{n-1}\
0&(4/5)^n
end{pmatrix}.
]

## Singular-value check

For

[
B=
egin{pmatrix}
p&q\0&p
end{pmatrix},
]

Wolfram returned the squared singular values

[
rac{2p^2+q^2mp |q|sqrt{4p^2+q^2}}{2}.
]

## Finite-horizon check

Over (n=0,ldots,40), Wolfram returned

[
max|A^n|_2
=
8.212429054411118
]

at

[
n=4.
]

## Pseudospectral-boundary check

For the exact smallest-singular-value formula, substituting

[
r^2=arepsilon(arepsilon+K)
]

simplified the residual

[
sigma_{min}^2-arepsilon^2
]

to exactly (0).

## Rendered witness

`figures/masters/ATLAS-FIG-PSPECTRUM-001.png`

Committed PNG Git blob:

`b8901f7ef153598e7b6fe60756ef14f808798734`.

## Claim boundary

This witness establishes the exact finite-dimensional example and its rendering. It does not infer the prevalence or cause of transient instability in any learned system.
