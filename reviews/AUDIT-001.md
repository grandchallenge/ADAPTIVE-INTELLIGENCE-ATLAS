# AUDIT-001 — Geometry + Non-normality v0.1

## Disposition

**PASS WITH BOUNDED REPAIRS APPLIED**

No blocking mathematical defect was found in the two v0.1 chapter drafts.

Audited baseline:

`44cbe4cacb8394744d919e5556633b8f0d815929`

Target chapters:

- `ATLAS-CH-GEOM-001`;
- `ATLAS-CH-NONNORMAL-001`.

## 1. Mathematical audit

### Geometry

Rechecked:

- sphere tangent-space derivation;
- normalized-retraction first derivative;
- sphere exponential-map formula;
- SLERP unit-norm identity;
- antipodal nonuniqueness boundary;
- Stiefel tangent-space differentiation;
- Stiefel/Grassmann quotient distinction.

Independent Wolfram check under the recorded 15.0.1 runtime returned:

- SLERP norm-squared identity: exactly (1);
- (x^	op v=0) for the figure witness;
- (|operatorname{Exp}_x(v)|^2=1);
- (|R_x(v)|^2=1);
- (|operatorname{Exp}_x(v)-R_x(v)|approx0.125177186605) for (x=(0,0,1)), (v=(4/5,0,0)).

This confirms the figure shows two distinct, legal finite endpoints rather than duplicate renderings.

### Non-normality

Rechecked:

- exact binomial/Jordan power formula;
- squared singular-value formula for the upper-triangular (2	imes2) family;
- matched normal comparison;
- finite-horizon peak for (a=4/5,K=4);
- exact (2)-norm pseudospectral boundary
  [
  |z-a|^2=arepsilon(arepsilon+K).
  ]

No mathematical correction was required.

## 2. Source/claim alignment

Bibliographic metadata was independently checked against publisher/primary or authoritative records before the original source locks were committed.

The audit found no instance where:

- a historical source was being used as the sole authority for a general mathematical fact;
- a GCL interpretation was presented as an externally established theorem;
- a fluid-mechanical application was generalized into a claim about neural training;
- a computational witness was promoted to proof.

The source-lock claim boundaries remain appropriate.

## 3. Figure audit

### Defect A — pseudospectral levels were not self-identifying

The original right-hand panel distinguished normal and non-normal contours by solid/dashed line style but did not identify the (arepsilon) levels.

**Repair:** label each non-normal contour with its epsilon level and add explicit panel titles.

This improves self-decoding and remains usable without color.

New rendered blob:

`cf87cec053f71b22ce25adfd12224fd601a49f9e`.

Previous KEYSTONE-002 blob retained in the historical tranche receipt:

`b8901f7ef153598e7b6fe60756ef14f808798734`.

### Defect B — manifold plate under-labelled its tangent object

The original geometry plate did not explicitly label the tangent plane.

**Repair:** add (T_xS^2) label and a descriptive panel title.

New rendered blob:

`39c6a40522b4d65c8ef34a0c4f6a36119dceab66`.

Previous KEYSTONE-002 blob retained in the historical tranche receipt:

`aded6f0764e04dd17457a71a32cb4a1ae5d42a84`.

### Defect C — manuscript image alternatives were object IDs only

**Repair:** replace ID-only Markdown alt text with content descriptions that state the mathematical comparison.

## 4. Convention audit

The non-normality chapter uses the closed definition

[
Lambda_arepsilon(A)
=
{z:sigma_{min}(zI-A)learepsilon}.
]

Some literature uses an open inequality convention.

**Repair:** state explicitly that the Atlas uses the closed convention in this chapter.

## 5. Provenance audit

Rerendering changed PNG identities.

**Repair:** update active figure manifests and computational-witness receipts to the new Git blob identities.

The historical KEYSTONE-002 receipt is intentionally **not** rewritten; it remains an accurate receipt for the state that merged.

This preserves the distinction between historical state and current active artifact identity.

## 6. Citation closure

All citation keys in the two manuscript drafts resolve to `sources/bibliography.bib`.

Resolved keys:

- `Lee2018Riemannian`;
- `AbsilMahonySepulchre2008`;
- `EdelmanAriasSmith1998`;
- `Shoemake1985`;
- `HornJohnson2012`;
- `TrefethenEmbree2005`;
- `ReddySchmidHenningson1993`;
- `TrefethenEtAl1993`.

**Durable repair:** Atlas CI now checks manuscript citation keys against the canonical bibliography.

## 7. Allegory audit

### Cartographer and mountain

PASS.

The mapping is structurally faithful for ambient space, admissible state space, tangent space, geodesic, and retraction. The manuscript explicitly states that general manifolds need not be visible embedded surfaces and that a retraction is not a physical projection.

### Aligned harbor currents

PASS.

The analogy is bounded to modal geometry and transient amplification. The manuscript explicitly rejects literal identification with fluid dynamics.

## 8. Epistemic audit

The chapters maintain the intended separation among:

- standard sourced mathematics;
- Atlas-owned derivation;
- Wolfram computational witness;
- interpretation for adaptive systems;
- future GCL research questions.

No statement was found that should be promoted to a stronger epistemic label.

## 9. Remaining non-blocking editorial work

For later publication passes:

- harmonize typography and equation numbering once the manuscript build system exists;
- add formal Definition/Result/Computational Witness callout styling;
- consider a second geometry plate comparing chord distance with geodesic distance;
- consider a second non-normality plate showing a diagonalizable non-normal family so the chapter does not visually rely only on a defective Jordan example.

These are enrichment opportunities, not defects in the current v0.1 drafts.

## 10. Audit conclusion

The pair is fit to remain at `draft-v0.1` and to serve as the mathematical style reference for the next keystone pair.

The next substantive target is:

- `ATLAS-CH-ATTNOP-001` — Attention as an Operator;
- `ATLAS-CH-OPTDYN-001` — Optimizer-State Dynamics.
