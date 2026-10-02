# ATLAS-CW-OPTDYN-001 — Optimizer-State Dynamics Witness

**Chapter:** `ATLAS-CH-OPTDYN-001`  
**System:** Wolfram Language 15.0.1 for Linux x86 (64-bit), July 2 2026  
**System ID:** Linux-x86-64  
**Norm:** spectral/operator (2)-norm  
**Figure source:** `figures/wolfram/ATLAS-FIG-OPTDYN-001.wl`

## Purpose

Exhibit a stable momentum recurrence whose **augmented optimizer-state Jacobian** is non-normal and displays finite-horizon amplification.

## Quadratic and optimizer

[
L(	heta)=rac12	heta^2,
qquad
eta=rac1{10},
qquad
eta=rac9{10}.
]

With state (z=(	heta,v)),

[
z_{t+1}=Jz_t,
]

where

[
J=
egin{pmatrix}
0.9&-0.09\
1&0.9
end{pmatrix}.
]

## Eigenvalue check

Wolfram returns

[
lambda_pm=0.9pm0.3i.
]

Hence

[
|lambda_pm|=sqrt{0.9}<1.
]

The linear recurrence is asymptotically stable.

## Non-normal finite-horizon check

Wolfram evaluates

[
|J|_2
=
1.507152555478529ldots
]

and, over (k=0,ldots,30),

[
max_k|J^k|_2
=
2.610090585959495ldots
]

at

[
k=4.
]

Thus asymptotic spectral stability coexists with substantial short-horizon gain.

## Symbolic checks

For general (h,eta,eta), the recurrence Jacobian is

[
J=
egin{pmatrix}
1-eta h&-etaeta\
h&eta
end{pmatrix},
]

with characteristic polynomial

[
lambda^2-(1+eta-eta h)lambda+eta.
]

Wolfram also returns a generically nonzero matrix for

[
J^	op J-JJ^	op,
]

confirming that the augmented update is not normally diagonalizable in general.

## Rendered witness

`figures/masters/ATLAS-FIG-OPTDYN-001.png`

Committed PNG Git blob:

`fa8e5231cb6451c026a0ccd7beecdfcff330c98d`.

## Claim boundary

The witness establishes the mechanism for one exact scalar-quadratic momentum system. It does not establish that a real neural-training trajectory follows a constant Jacobian, nor that every observed loss spike is caused by non-normal optimizer-state amplification.
