# Chapter Specification — ATLAS-CH-MECHDIAG-001

## Identity

**Title:** Mechanistic Intervention  
**Part:** Diagnostics, Robustness, and Compression  
**Status:** specification-ready.  
**Epistemic class:** audited Evidence and Transformer prerequisites + primary interpretability sources + Atlas synthesis.

## Contract

Develop a disciplined ladder from observational probes to controlled internal tests. The chapter must distinguish information that is readable from information that is functionally used, and must state the scope of every component-level claim.

## Hard prerequisites

- ATLAS-CH-EVIDENCE-001
- ATLAS-CH-TRANSFORMER-001

Exact prerequisite identities are locked in:

`sources/source-locks/ATLAS-CH-MECHDIAG-001.yaml`.

## Required distinctions

The chapter must keep separate:

- probe accuracy and functional dependence;
- correlation and component-level explanation;
- single-component masking and redundancy-aware tests;
- arbitrary replacement and reference-state substitution;
- local restoration and global uniqueness;
- activation-level localization and parameter editing;
- readable, inaccessible-under-a-test, and genuinely absent information;
- circuit faithfulness, completeness, and minimality.

## Diagnostic record

Every strong component claim should identify

\[
D=(B,S,T,M,R),
\]

where (B) is the target behavior, (S) the selected components, (T) the tested transformations, (M) the metric, and (R) the reference rule.

## Exact witness

Use

\[
x\in\{-1,+1\},\qquad h(x)=(x,x),\qquad F(h)=h_1.
\]

Both coordinates recover (x) perfectly, but only the first affects the output map. The witness must verify both zero-setting and clean/reference substitution.

## Failure boundaries

- perfect decodability != functional use;
- a null one-component test != absence of representation;
- a successful local restoration != unique global mechanism;
- one replacement rule != replacement-invariant evidence;
- a component label != a basis-independent feature identity;
- a spectral correlate != a mechanistic explanation.

## Sources

- [@ElazarEtAl2021Amnesic]
- [@MengEtAl2022FactualAssociations]
- [@WangEtAl2023Interpretability]

## Downstream handoff

Direct consumer:

- ATLAS-CH-SPECTRALDIAG-001.

SPECTRALDIAG may inherit the diagnostic record, the readability/function distinction, redundancy warnings, and the exact finite witness. It must independently establish any spectral diagnostic claim.
