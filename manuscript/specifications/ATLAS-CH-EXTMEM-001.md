# Chapter Specification — ATLAS-CH-EXTMEM-001

## Identity

- Stable ID: `ATLAS-CH-EXTMEM-001`
- Title: **The External-Memory Thesis**
- Part: `ATLAS-PART-MEM`
- Status target: `draft-v0.1`
- Hard prerequisites:
  - `ATLAS-CH-RETRIEVAL-001`
  - `ATLAS-CH-CONTINUAL-001`
- Implementation issue: #122
- Baseline: `7604f00fe257ade14adf01718bda0b8f9aa8feb9`

## Contract

Argue and test which knowledge should leave parameters and enter persistent shared memory.

## Governing thesis

The placement question is not:

> parameters or external memory?

It is:

> which information should be compressed into model behavior, and which information should remain explicit, addressable, versioned, and retrievable?

The expected architecture is usually hybrid.

## Placement descriptor

For a knowledge item or class `k`, use:

`Place(k)=(V,P,S,D,R,L,A,G)`

where:

- `V`: volatility/update frequency;
- `P`: provenance/audit requirement;
- `S`: sharing/synchronization scope;
- `D`: deletion/supersession requirement;
- `R`: addressability/retrievability;
- `L`: latency/availability constraint;
- `A`: access-control/privacy constraint;
- `G`: value of compression/generalization into parameters.

No universal scalar score over these coordinates is assumed.

## External-memory-favoring pressures

External placement becomes attractive when knowledge is:

- frequently updated;
- individually addressable;
- provenance-critical;
- shared across agents/processes;
- subject to deletion or supersession;
- too large or sparse to justify parametric absorption;
- useful only in a subset of contexts;
- naturally represented as records/documents/tuples.

These are pressures, not a theorem of optimality.

## Parametric-favoring pressures

Parametric placement becomes attractive when knowledge is:

- stable;
- needed with very low retrieval latency;
- diffuse across many examples;
- useful primarily through generalization/compression rather than record identity;
- difficult to retrieve by an explicit key/query;
- robustly encoded as reusable features or procedures.

Again, these are pressures, not a universal rule.

## Hybrid placement

A hybrid system can:

- keep general linguistic/computational structure in parameters;
- keep mutable facts and records external;
- retrieve only the working subset required by the current task;
- optionally consolidate repeated/stable external evidence into parameters later.

Externalization and consolidation are different operations.

## Exact witness

Define a parametric representation for two facts:

`f_theta(A)=theta_1+theta_2`

`f_theta(B)=theta_1-theta_2`.

Initial targets:

`A=2`

`B=0`.

The unique parameter solution is:

`theta=(1,1)`.

Now update only fact A:

`A:2 -> 4`

while preserving:

`B=0`.

The new unique parameter solution is:

`theta'=(2,2)`.

Both parameter coordinates change.

A naive one-coordinate edit `theta_1:1->2` with `theta_2=1` yields:

`A=3`

`B=1`,

so it neither completes the requested update nor preserves B.

This demonstrates update coupling only for this chosen representation.

## External record representation

Use a versioned exact-key store:

`M_1[A]=(2,source=s_A1,version=1)`

`M_1[B]=(0,source=s_B1,version=1)`.

Update A by appending/superseding:

`M_2[A]=(4,source=s_A2,version=2,supersedes=1)`.

B remains:

`M_2[B]=M_1[B]`.

Latest-version reads give:

`read(M_2,A)=4`

`read(M_2,B)=0`.

The update is record-local in this representation, and the old/new source identities remain explicit.

## Stale-read counterexample

A consumer pinned to snapshot `M_1` still reads:

`read(M_1,A)=2`.

Therefore externalization does not make information automatically fresh.

A correct external-memory system needs explicit freshness/version semantics.

## Provenance boundary

The versioned store has a direct mapping from each current fact record to its source metadata.

The toy parameter vector `theta` does not itself contain a per-fact source record.

This does not prove that parametric systems cannot maintain provenance in auxiliary metadata.

It proves only that provenance is explicit in the chosen external representation and absent from the bare parameter vector.

## Retrieval boundary

Correct storage does not imply correct use.

Failure can arise from:

- missed retrieval;
- stale snapshot;
- wrong ranking/filter;
- poisoned record;
- unauthorized record;
- missing context compilation.

External memory moves some failure modes out of weight updates and into memory/retrieval infrastructure.

It does not remove failure.

## Continual-learning boundary

Parameter updates can interfere with earlier behavior.

Replay, consolidation, episodic constraints, and parameter isolation are mechanisms for controlling that interference.

External memory offers another architectural move:

- do not encode every mutable fact as a weight update in the first place.

That move does not eliminate the need for continual learning of skills, representations, or stable structure.

## Shared-memory boundary

One store can serve multiple agents or model instances.

Shared visibility requires:

- access policy;
- synchronization/version semantics;
- provenance;
- deletion/supersession rules.

Shared memory is not equivalent to unrestricted global access.

## Downstream handoff

`ATLAS-CH-CONTEXTCOMP-001` may inherit:

- external versus parametric placement criteria;
- freshness/version requirements;
- retrieval/use separation;
- provenance-preserving record semantics.

`ATLAS-CH-POLITY-001` may inherit:

- shared-memory scope;
- synchronization/access-control requirements;
- distinction between common memory and private model state.

Neither downstream chapter may treat external memory as automatically correct, fresh, complete, or safe.
