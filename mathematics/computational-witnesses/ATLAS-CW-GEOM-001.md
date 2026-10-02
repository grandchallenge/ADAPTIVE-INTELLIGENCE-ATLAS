# ATLAS-CW-GEOM-001 — Sphere Geometry Witness

**Chapter:** `ATLAS-CH-GEOM-001`  
**System:** Wolfram Language 15.0.1 for Linux x86 (64-bit), July 2 2026  
**System ID:** Linux-x86-64  
**MaxExtraPrecision:** 50  
**Figure source:** `figures/wolfram/ATLAS-FIG-MANIFOLD-001.wl`

## Purpose

Reconstruct the unit-sphere plate from explicit equations and confirm that the two finite updates shown are distinct:

[
operatorname{Exp}_x(v)
=
cos(|v|)x+sin(|v|)rac{v}{|v|},
]

[
R_x(v)=rac{x+v}{|x+v|}.
]

## Parameters

[
x=(0,0,1),qquad v=(0.8,0,0).
]

The tangent condition is exact:

[
x^	op v=0.
]

## Reconstruction

Run the source file in repository root. It exports:

`figures/masters/ATLAS-FIG-MANIFOLD-001.png`.

The committed PNG Git blob is:

`aded6f0764e04dd17457a71a32cb4a1ae5d42a84`.

## Claim boundary

This witness reconstructs an exact unit-sphere example. It verifies neither a general manifold theorem nor an empirical claim about neural representations.
