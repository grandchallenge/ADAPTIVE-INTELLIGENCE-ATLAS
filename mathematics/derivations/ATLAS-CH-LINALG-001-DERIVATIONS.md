# ATLAS-CH-LINALG-001 — Derivation Packet

## D1. Matrix as linear-map representation

Given bases for finite-dimensional spaces, a linear map

[
T:V	o W
]

is represented by a matrix (A). A basis change changes the coordinate matrix but need not change the underlying map.

## D2. Orthogonal projection

If (Qinmathbb R^{n	imes k}) has orthonormal columns,

[
Q^	op Q=I,
]

then

[
P=QQ^	op
]

satisfies

[
P^2=P,
qquad
P^	op=P.
]

Hence (P) is the orthogonal projector onto (operatorname{col}(Q)).

## D3. Singular-value decomposition

For

[
Ainmathbb R^{m	imes n},
]

the SVD is

[
A=USigma V^	op.
]

The induced Euclidean operator norm is

[
|A|_2=sigma_{max}(A).
]

For the non-normal witness

[
A=
egin{pmatrix}
1&1\
0&1
end{pmatrix},
]

the eigenvalues are both (1), while the singular values are

[
sigma_1=rac{1+sqrt5}{2},
qquad
sigma_2=rac{sqrt5-1}{2}.
]

Thus eigenvalue magnitude and one-step Euclidean amplification answer different questions.

## D4. Low-rank approximation

For singular values

[
sigma_1gecdotsgesigma_r>0,
]

the best rank-(k) approximation in induced (2)-norm has error

[
sigma_{k+1}.
]

For the witness matrix above, the best rank-one approximation error is

[
rac{sqrt5-1}{2}.
]

## D5. Conditioning

For nonsingular

[
D=
egin{pmatrix}
1&0\
0&1/100
end{pmatrix},
]

[
kappa_2(D)
=
rac{sigma_{max}(D)}{sigma_{min}(D)}
=
100.
]

A relative perturbation aligned with the weak singular direction can therefore be amplified by a factor governed by this conditioning.

## D6. Pseudoinverse

For

[
A=USigma V^	op,
]

the Moore-Penrose pseudoinverse is

[
A^+=VSigma^+U^	op,
]

with nonzero singular values inverted.

For least squares,

[
x_star=A^+b
]

is the minimum-norm least-squares solution when the standard finite-dimensional conditions apply.

## Claim boundary

This packet establishes standard finite-dimensional identities and one exact witness. It does not claim that spectral structure alone determines neural training behavior.
