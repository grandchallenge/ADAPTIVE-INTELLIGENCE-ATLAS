# ATLAS-CW-GEOM-001 — Constrained Geometry Witness

**Chapter:** \`ATLAS-CH-GEOM-001\`  
**System:** Wolfram Language 15.0.1 for Linux x86 (64-bit), July 2 2026  
**System ID:** Linux-x86-64  
**Figure source:** \`figures/wolfram/ATLAS-FIG-MANIFOLD-001.wl\`

## Purpose

Render one explicit sphere example showing:

- the admissible manifold;
- the tangent plane;
- a legal tangent vector;
- the exponential-map endpoint;
- the normalized-retraction endpoint.

## Parameters

\[
x=(0,0,1),
\qquad
v=(0.8,0,0).
\]

The tangent condition is exact:

\[
x^\top v=0.
\]

## Endpoints

The exponential-map endpoint is

\[
\operatorname{Exp}_x(v)
=
\cos(0.8)x
+
\sin(0.8)\frac{v}{0.8}.
\]

The normalized-retraction endpoint is

\[
R_x(v)
=
\frac{x+v}{\|x+v\|}.
\]

Both endpoints have unit norm; they are distinct finite moves.

## Rendered witness

\`figures/masters/ATLAS-FIG-MANIFOLD-001.png\`

The corresponding figure manifest records the literal and nonliteral semantics.

## Claim boundary

The witness illustrates exact sphere geometry for one chosen point and tangent vector. The extent of the tangent-plane patch, perspective, opacity, and label placement are schematic. The figure does not establish that a neural representation is empirically spherical.
