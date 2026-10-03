# FORMAL-001 — Formal Methods and Machine-Checkable Claims

## Identity

- chapter: `ATLAS-CH-FORMAL-001`
- issue: #107
- baseline: `c257c8400a329cb127ac322cf8bfb70d4693b10c`
- branch: `work/formal-001`

Prerequisite identities:

- REPLAY manuscript `4d95568d12ec0b27bcace910d8573f4a22e8b161`
- REPLAY source lock `b373efe80e4ced13c7e060e5036d0012d2e17686`
- AUDIT-003 `9723fcb3dfa0111829b98f1c9bb416a13dbd714e`

## Core

The chapter separates intended requirement, formal specification, model, checked support object, checker, implementation, and environment.

Exact witness:

- specification starts at 0 and adds 2;
- induction establishes evenness for all specified reachable states;
- an implementation agrees on `0->2->4->6` and then maps `6->7`;
- therefore finite passing tests, specification proof, and implementation conformance are distinct.

## Durable artifacts

Source lock, specification, derivation packet, witness, manuscript, ledger promotion, source register, and bibliography are present.

## Remaining gates

Validate, merge, audit, validate audit, merge, verify closure, recompute frontier, reset controller.
