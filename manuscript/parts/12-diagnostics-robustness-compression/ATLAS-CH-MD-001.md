# Reading Internal Representations
<!-- ATLAS-CH-MECHDIAG-001 -->

**Epistemic status:** Audited prerequisites + primary sources + Atlas synthesis + exact finite witness  
**Specification:** manuscript/specifications/ATLAS-CH-MECHDIAG-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-MECHDIAG-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-MECHDIAG-001.md

A representation can contain information without the output map using it. The chapter therefore separates readability from functional dependence.

## Exact witness

Take (xin{-1,+1}), (h(x)=(x,x)), and (F(h)=h_1).

Both coordinates recover (x) perfectly. Setting the second coordinate to zero leaves (F) unchanged, while setting the first to zero changes the result.

Thus perfect decodability does not imply functional use.

## Diagnostic record

A strong component claim should bind

[
D=(B,S,T,M,R),
]

where (B) is the target behavior, (S) the selected components, (T) the tested transformation family, (M) the metric, and (R) the reference rule.

Starting from the reference state (h(-x)=(-x,-x)), replacing coordinate 1 with its value from (h(x)) restores output (x). Replacing coordinate 2 does not. The comparison separates the used coordinate from the equally predictive spectator.

## Null results and redundancy

A zero single-component effect is not an absence proof. For binary coordinates with

[
F(h_1,h_2)=max(h_1,h_2),
]

at state ((1,1)), setting either coordinate alone to zero leaves the output unchanged. Either coordinate can still support the result.

Therefore a null one-component result does not establish that no relevant representation exists.
