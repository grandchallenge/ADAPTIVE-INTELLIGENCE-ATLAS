# From Readability to Functional Evidence

**Epistemic status:** audited prerequisites + exact finite witness + source-scoped synthesis

A representation may carry a quantity that is easy to read without the declared output map depending on that quantity. The chapter therefore separates readout success from functional dependence.

## Exact finite separation

For x in {-1,+1}, let h(x)=(x,x) and F(h)=h_1. Both coordinates recover x exactly. Removing the second coordinate leaves F unchanged, while removing the first changes the output. Starting from h(-x), replacing coordinate 1 with its clean value restores x; replacing coordinate 2 does not.

This proves a finite separation between perfect readability and use by the declared output map.

## Diagnostic record

A strong component-level result should state the target behavior B, selected component set S, tested transformation T, metric M, and reference rule R:

D=(B,S,T,M,R).

The same observed effect can support different interpretations if any of these fields changes.

## Redundancy boundary

A null one-component result does not prove that no relevant representation exists. Redundant coordinates can each support the same output while neither is individually necessary under a single removal test.

## Downstream handoff

ATLAS-CH-SPECTRALDIAG-001 may inherit the readability/function distinction, the diagnostic record, the redundancy warning, and the exact witness. Any proposed spectral signature still requires its own functional evidence.

## References used in this chapter

Primary references and exact prerequisite identities are recorded in:

sources/source-locks/ATLAS-CH-MECHDIAG-001.yaml
