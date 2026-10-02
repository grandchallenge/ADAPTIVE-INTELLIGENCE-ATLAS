# ATLAS-CH-NONNORMAL-001 — Derivation Packet

**Status:** first-pass derivations  
**Norm convention:** spectral/operator (2)-norm unless explicitly stated otherwise  
**Source lock:** `sources/source-locks/ATLAS-CH-NONNORMAL-001.yaml`

## D1. Exact powers of a stable non-normal matrix

Consider

[
A=
egin{pmatrix}
a & K\
0 & a
end{pmatrix}
=
aI+KN,
qquad
N=
egin{pmatrix}
0&1\
0&0
end{pmatrix},
]

with (N^2=0).

For integer (nge1),

[
A^n
=
(aI+KN)^n
=
a^n I+n a^{n-1}KN
]

because all terms containing (N^j) with (jge2) vanish. Therefore

[
oxed{
A^n=
egin{pmatrix}
a^n & nKa^{n-1}\
0 & a^n
end{pmatrix}.
}
]

The only eigenvalue is (a), with algebraic multiplicity two, so

[
ho(A)=|a|.
]

For (|a|<1), (A^n	o0) asymptotically. The off-diagonal term can nevertheless become large over finite (n).

## D2. Exact spectral norm of the power

Write

[
B=
egin{pmatrix}
p&q\
0&p
end{pmatrix},
]

where

[
p=a^n,qquad q=nKa^{n-1}.
]

Then

[
B^	op B
=
egin{pmatrix}
p^2 & pq\
pq & p^2+q^2
end{pmatrix}.
]

Its eigenvalues are

[
lambda_{pm}
=
rac{
2p^2+q^2
pm
|q|sqrt{4p^2+q^2}
}{2}.
]

Hence

[
oxed{
|A^n|_2
=
sqrt{
rac{
2a^{2n}
+n^2K^2a^{2n-2}
+
|nKa^{n-1}|
sqrt{
4a^{2n}
+n^2K^2a^{2n-2}
}
}{2}
}.
}
]

This formula exhibits the finite-horizon competition directly: (a^n) decays, while the polynomial factor (n) can initially dominate.

## D3. Concrete Atlas witness

Set

[
a=rac45,qquad K=4.
]

Then every eigenvalue has magnitude (0.8<1). The matched normal comparison is

[
N_0=rac45 I,
]

which has exactly the same eigenvalue multiset.

For the normal matrix,

[
|N_0^n|_2=(4/5)^n.
]

For the non-normal matrix, Wolfram evaluation over (n=0,ldots,40) gives the peak

[
oxed{
max_{0le nle40}|A^n|_2
=
8.2124290544ldots
quad	ext{at }n=4.
}
]

Thus the two matrices have the same eigenvalues while their finite-horizon gains differ by more than an order of magnitude.

This does not contradict asymptotic stability: (|A^n|_2	o0).

## D4. Exact pseudospectrum of the 2x2 Jordan-like example

For complex (z), let

[
delta=z-a,
qquad
r=|delta|.
]

Then

[
zI-A
=
egin{pmatrix}
delta & -K\
0 & delta
end{pmatrix}.
]

The squared singular values depend only on (r):

[
sigma_{pm}^2
=
rac{
2r^2+K^2
pm
Ksqrt{K^2+4r^2}
}{2},
qquad K>0.
]

The (2)-norm (arepsilon)-pseudospectrum is

[
Lambda_arepsilon(A)
=
{z:sigma_{min}(zI-A)learepsilon}.
]

On the boundary, set (sigma_{min}=arepsilon). Because the product of the singular values is

[
sigma_{max}sigma_{min}=|det(zI-A)|=r^2,
]

we have

[
sigma_{max}=rac{r^2}{arepsilon}.
]

Also,

[
sigma_{max}^2+sigma_{min}^2
=
2r^2+K^2.
]

Substituting,

[
rac{r^4}{arepsilon^2}+arepsilon^2
=
2r^2+K^2.
]

Multiply by (arepsilon^2):

[
r^4-2arepsilon^2r^2+arepsilon^4-K^2arepsilon^2=0,
]

so

[
(r^2-arepsilon^2)^2=K^2arepsilon^2.
]

Because (sigma_{max}gesigma_{min}) implies (r^2gearepsilon^2), the admissible branch is

[
oxed{
r^2=arepsilon(arepsilon+K).
}
]

Therefore

[
oxed{
Lambda_arepsilon(A)
=
left{
z:
|z-a|
le
sqrt{arepsilon(arepsilon+K)}
ight}.
}
]

For the normal comparison (N_0=aI),

[
oxed{
Lambda_arepsilon(N_0)
=
{z:|z-a|learepsilon}.
}
]

The same eigenvalue point therefore sits inside radically different pseudospectral neighborhoods.

## D5. Resolvent interpretation

Outside the spectrum,

[
|(zI-A)^{-1}|_2
=
rac{1}{sigma_{min}(zI-A)}.
]

Thus broad pseudospectral contours are exactly regions of large resolvent norm. This is not decorative spectral plotting: it measures sensitivity of the inverse problem associated with (zI-A).

The equivalent perturbation characterization,

[
zinLambda_arepsilon(A)
iff
zinsigma(A+E)
	ext{ for some }|E|_2learepsilon,
]

is source-backed by the canonical pseudospectra literature and should be cited rather than reproved in full generality.

## D6. What the example proves

It proves, constructively, that:

1. (ho(A)<1) does not imply monotone decay of (|A^n|_2);
2. identical eigenvalue sets do not determine finite-horizon gain;
3. non-normal eigenstructure can broaden the pseudospectrum substantially;
4. the phenomenon is already visible in dimension two.

It does **not** prove that:

- every non-normal matrix has large transient growth;
- transient growth implies nonlinear divergence;
- a neural optimizer showing a spike is necessarily governed by this mechanism;
- eigenvalues are useless.

## D7. Computational verification

Wolfram Language 15.0.1 verified:

[
A^n=
egin{pmatrix}
a^n & nKa^{n-1}\
0&a^n
end{pmatrix}
]

symbolically.

For (a=4/5,K=4), it independently evaluated the finite-horizon (2)-norm and found the peak above at (n=4).

It also verified by substitution that the pseudospectral boundary

[
r^2=arepsilon(arepsilon+K)
]

makes the exact smallest-singular-value expression equal to (arepsilon^2).

The rendered witness is:

`figures/masters/ATLAS-FIG-PSPECTRUM-001.png`.

## Source boundary

- Matrix-analysis baseline: `NONNORMAL-HORN-JOHNSON-2012`.
- Canonical pseudospectra framework: `NONNORMAL-TREFETHEN-EMBREE-2005`.
- Primary pseudospectra/transient-growth application: `NONNORMAL-REDDY-SCHMID-HENNINGSON-1993`.
- Historical broad motivation: `NONNORMAL-TREFETHEN-TREFETHEN-REDDY-DRISCOLL-1993`.

The 2x2 derivation itself is an Atlas-owned worked example.
