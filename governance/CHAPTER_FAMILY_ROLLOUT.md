# Chapter-Family Rollout After the Six Keystones

**Status:** historical dependency-driven drafting plan — execution complete
**Original baseline:** six audited keystones at `draft-v0.1`
**Original remaining chapters:** 74
**Current protected phase:** 80/80 chapter nodes at `draft-v0.1`; architecture frontier exhausted; global synthesis active.

This document is retained as the execution rationale for chapter-family drafting. Its family sequencing describes how the corpus was built. Current chapter lifecycle state is governed by `governance/CHAPTER_LEDGER.yaml`; active transaction state is governed by `governance/ACTIVE_TRANSACTION.yaml` on the controller branch.

## Principle

Draft by **dependency closure and conceptual leverage**, not by table-of-contents order alone.

The six keystones proved the local authoring grammar. They do not erase their undrafted prerequisites.

At the synthesis baseline, the highest-reach undrafted nodes are:

| Chapter ID | Current downstream descendants |
|---|---:|
| `ATLAS-CH-THESIS-001` | 79 |
| `ATLAS-CH-OBJECTS-001` | 68 |
| `ATLAS-CH-LINALG-001` | 63 |
| `ATLAS-CH-DYN-001` | 48 |
| `ATLAS-CH-INFO-001` | 28 |
| `ATLAS-CH-ARCHHIST-001` | 28 |
| `ATLAS-CH-TRANSFORMER-001` | 20 |
| `ATLAS-CH-REP-001` | 19 |
| `ATLAS-CH-NUMERICS-001` | 17 |
| `ATLAS-CH-OPTBASE-001` | 17 |

These counts measure graph reach, not intellectual importance.

## Family 0 — Orientation and load-bearing mathematical spine

This family comes first even though several downstream keystones already exist.

Primary targets:

- `ATLAS-CH-THESIS-001`;
- `ATLAS-CH-MAP-001`;
- `ATLAS-CH-OBJECTS-001`;
- `ATLAS-CH-EVIDENCE-001`;
- `ATLAS-CH-LINALG-001`;
- `ATLAS-CH-DYN-001`;
- `ATLAS-CH-INFO-001`;
- `ATLAS-CH-NUMERICS-001`;
- `ATLAS-CH-LOCALGLOBAL-001`.

Goal:

- remove hidden prerequisites from later families;
- freeze state/operator/object language before it proliferates;
- establish evidence classes before the Atlas accumulates many synthesis claims;
- supply the dynamics and numerical-analysis language consumed by later chapters.

The existing keystones are valid style anchors, not substitutes for these prerequisites.

## Family 1 — Geometric representation and architecture

Enter after the Family 0 mathematical notation stabilizes.

Primary targets:

- `ATLAS-CH-REP-001`;
- `ATLAS-CH-ARCHHIST-001`;
- `ATLAS-CH-TRANSFORMER-001`;
- `ATLAS-CH-DEPTH-001`;
- `ATLAS-CH-NORMREP-001`;
- `ATLAS-CH-QUOTIENT-001`;
- `ATLAS-CH-RESIDUAL-001`.

Then expand through the remaining representation and architecture descendants.

Goal:

connect the Geometry keystone to learned representations, normalized states, quotient structure, architecture history, and the Transformer substrate consumed by later attention, sparse-compute, systems, and memory chapters.

## Family 2 — Optimization and numerical computation

Primary targets:

- `ATLAS-CH-OPTBASE-001`;
- `ATLAS-CH-SPECTRALSHAPE-001`;
- `ATLAS-CH-MANOPT-001`;
- `ATLAS-CH-SECOND-001`;
- `ATLAS-CH-TRANSPORT-001`;
- `ATLAS-CH-NETNUM-001`;
- `ATLAS-CH-BOUNDARYPROBE-001`;
- `ATLAS-CH-COMPOSE-001`;
- `ATLAS-CH-NEURALKRYLOV-001`;
- `ATLAS-CH-ADAPTDEPTH-001`.

Goal:

connect Geometry, Non-normality, Optimizer-State Dynamics, and Boundary Contracts into one numerical-dynamical family before GCL-specific optimizer programmes become load-bearing examples.

## Family 3 — Attention, position, sparse computation, and routing

Build around the existing Attention keystone once the Transformer and optimization substrate is explicit.

Primary targets include:

- `ATLAS-CH-ATTNAPPROX-001`;
- `ATLAS-CH-POSGEOM-001`;
- `ATLAS-CH-RPO-001`;
- remaining positional/RoPE descendants;
- `ATLAS-CH-SPARSE-001`;
- `ATLAS-CH-MOE-001`;
- `ATLAS-CH-ROUTERDYN-001`;
- `ATLAS-CH-REGRETROUTE-001`.

Goal:

unify operator language across attention, position, routing, and conditional computation while keeping standard Transformer mathematics distinct from GCL RPO/SPLICE programme evidence.

## Family 4 — Memory, data, curriculum, and decision

Run as two coupled subfamilies with a synthesis checkpoint.

Memory/data targets include:

- `ATLAS-CH-MEMTAX-001`;
- `ATLAS-CH-RETRIEVAL-001`;
- `ATLAS-CH-CONTINUAL-001`;
- `ATLAS-CH-EXTMEM-001`;
- `ATLAS-CH-CONTEXTCOMP-001`;
- tokenizer/data/curriculum descendants.

Decision targets include:

- `ATLAS-CH-RLBASE-001`;
- `ATLAS-CH-EXPLORE-001`;
- uncertainty/robustness descendants;
- optionality/regret descendants.

Goal:

make the allocation problem among weights, context, memory, experience, and action explicit, and provide a standard substrate for minimal-curriculum and learning-progress questions.

## Family 5 — Agents, polity, hardware, and systems

Primary spine:

- `ATLAS-CH-AGENTS-001`;
- `ATLAS-CH-COORD-001`;
- `ATLAS-CH-EVIDEX-001`;
- remaining polity/distributed-intelligence descendants;
- hardware and systems chapters.

Goal:

move from single-model computation to coordinated systems whose behavior depends on communication, persistent memory, tools, evidence exchange, and physical machine constraints.

Hardware chapters may be drafted earlier when another family needs a concrete systems explanation, but they should not become undocumented prerequisites.

## Family 6 — Diagnostics, experiments, formal methods, and governance

Use the Replayable Evidence keystone as the evidentiary style anchor.

Primary spine:

- mechanistic and spectral diagnostic chapters;
- `ATLAS-CH-EXPERIMENT-001`;
- `ATLAS-CH-FORMAL-001`;
- `ATLAS-CH-RESEARCHSM-001`;
- `ATLAS-CH-GOVADAPT-001`.

Goal:

make diagnosis, experiment, replay, formal support, adjudication, certification, and governed adaptation distinct objects before the final synthesis depends on them.

## Family 7 — Frontier and global synthesis

Do not draft these to completion until the preceding dependency cones are mature:

- `ATLAS-CH-FRONTIER-001`;
- `ATLAS-CH-SYNTHESIS-001`;
- explicit frontier-programme chapters whose prerequisites are then mature.

Goal:

synthesize rather than preview.

The final argument should be earned by the dependency graph.

## Family execution rhythm

For each family:

1. recompute the dependency cone;
2. identify the smallest dependency-closed tranche;
3. source-lock the family;
4. update or write chapter specifications where needed;
5. draft two to five representative chapters;
6. build figures and computational witnesses concurrently with prose;
7. audit the representative tranche;
8. freeze family-local notation and cross-links;
9. draft the remaining family chapters;
10. run a family synthesis pass.

Do not draft an entire family blindly in parallel. Representative chapters are probes for notation, figure semantics, and hidden prerequisites.

## Global synthesis cadence

Run global synthesis after:

- Family 0;
- Family 2;
- the Family 4/5 boundary;
- Family 6;
- immediately before release candidate.

The Atlas should become more coherent as it grows, not merely longer.
