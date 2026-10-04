# ATLAS-CW-EXTMEM-001 — Parametric Edit versus Versioned External Record

**Chapter:** ATLAS-CH-EXTMEM-001  
**Witness class:** exact finite deterministic computation  
**Purpose:** compare one representation-specific parameter update with one versioned external-memory update, including a stale-read failure mode.

## Parametric representation

Let:

`f_theta(A)=theta_1+theta_2`

`f_theta(B)=theta_1-theta_2`.

Initial targets:

`A=2`

`B=0`.

Unique solution:

`theta=(1,1)`.

## Updated target

Change only A:

`A=4`

while preserving:

`B=0`.

The new equations are:

`theta'_1+theta'_2=4`

`theta'_1-theta'_2=0`.

Unique solution:

`theta'=(2,2)`.

Therefore:

`Delta theta=(1,1)`.

Both coordinates change.

## Naive one-coordinate edit

Use:

`theta_naive=(2,1)`.

Then:

`f_theta_naive(A)=3`

`f_theta_naive(B)=1`.

So the naive local parameter edit neither completes the A update nor preserves B.

This is a property of this chosen parameterization only.

## Versioned external store

Initial current records:

`A -> (2,s_A1,v1)`

`B -> (0,s_B1,v1)`.

Update only A by changing version state explicitly:

`A,v1 -> (2,s_A1,v1,status=superseded)`

`A,v2 -> (4,s_A2,v2,status=current,supersedes=v1)`.

Keep B unchanged and current.

Latest-version reads now give:

`A=4`

`B=0`.

Only logical key A changes.

The store retains source/version metadata for both A versions.

## Stale-read counterexample

A consumer pinned to snapshot v1 still observes:

`A=2`.

The authoritative latest store observes:

`A=4`.

Therefore the external representation supports local record mutation and explicit provenance, but it does not guarantee fresh reads.

## Exact table

| Quantity | Initial | Updated |
|---|---:|---:|
| parametric theta_1 | 1 | 2 |
| parametric theta_2 | 1 | 2 |
| f(A) | 2 | 4 |
| f(B) | 0 | 0 |
| current external A | 2 | 4 |
| current external B | 0 | 0 |
| external keys changed | 0 | 1 |
| stale-snapshot A after update | n/a | 2 |

## Claim boundary

This witness proves only the exact representation-specific statements above.

It does not prove that external memory requires fewer machine operations, that parameter editing is generally non-local, that external memory is more accurate or secure, that explicit memory should contain every fact, or that stale-read risk is unique to external systems.
