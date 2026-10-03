# AGENTS-001 — From Models to Agents

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- baseline: 1ab13b87c02f90630dbd37be7e4a15ee83643c80;
- issue: #72;
- hard prerequisite:
  - ATLAS-CH-THESIS-001 at draft-v0.1;
  - AUDIT-004 PASS.

## Objective

Establish the single-agent transition object consumed by the later Coordination family.

## Central object

A = (M, C, X, O, Γ, U, B, σ).

The model is a proposal component inside a loop that also includes controller state, observation, execution, update, budget/authority state, and stopping.

## Representative mechanisms

Primary literature is source-locked for ReAct, Toolformer, Tree of Thoughts, and Reflexion.

These are examples of mechanisms, not a universal agent taxonomy.

## Bounded delegation

Delegation packet:

D = (g', A', R', Q', σ').

Default invariants:

A' subseteq A;

R' <= R.

The chapter proves authority non-expansion along delegation paths under the declared set model and a simple induction bound for explicitly allocated resources in a finite delegation tree.

## Computational witness

ATLAS-CW-AGENTS-001 exhaustively checks a hidden-bit environment.

A fixed answer rule scores:

- 1/2 without informative interaction;
- 2/2 with one authorized QUERY and budget one;
- 1/2 when authority is removed;
- 1/2 when budget is zero.

This isolates interaction structure without changing model weights.

## Figure decision

No governed figure is added in v0.1.

A state-machine plate is deferred until Coordination Architectures adds shared state and multi-agent topology.

## Durable objects

The branch contains:

- sources/source-locks/ATLAS-CH-AGENTS-001.yaml;
- manuscript/specifications/ATLAS-CH-AGENTS-001.md;
- mathematics/derivations/ATLAS-CH-AGENTS-001-DERIVATIONS.md;
- mathematics/computational-witnesses/ATLAS-CW-AGENTS-001.md;
- manuscript/parts/13-agents-systems-hardware/ATLAS-CH-AGENTS-001.md;
- Chapter Ledger promotion to draft-v0.1;
- Source Register entry.

## Next step after merge

Run a bounded post-draft audit of sources, formal loop semantics, authority and resource invariants, witness scope, termination surfaces, and the handoff to ATLAS-CH-COORD-001.
