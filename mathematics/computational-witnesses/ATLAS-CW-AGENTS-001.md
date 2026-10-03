# ATLAS-CW-AGENTS-001 — Interaction Changes the Available Information

**Chapter:** ATLAS-CH-AGENTS-001  
**Witness class:** exact finite deterministic computation  
**Purpose:** isolate the structural difference between a one-shot model call and an agent loop with an authorized information-gathering action.

## Environment

The hidden environment state is s in {0,1}.

Before any tool action, both states produce the same observation:

UNKNOWN.

The task is to return the hidden bit exactly.

## Model component

Use the same deterministic answer operator in every condition:

- if internal state contains an observed bit, return that bit;
- otherwise return 0.

No model weights or answer rule change across conditions.

## Conditions

### Condition A — one-shot model

The model receives only UNKNOWN and returns 0.

Results:

- s=0 -> correct;
- s=1 -> incorrect.

Score: 1/2.

### Condition B — agent with QUERY authority and budget 1

The controller first executes QUERY.

QUERY returns the exact hidden bit.

The update rule stores the returned bit.

The answer operator is then called on the updated state.

Results:

- s=0 -> QUERY returns 0 -> answer 0 -> correct;
- s=1 -> QUERY returns 1 -> answer 1 -> correct.

Score: 2/2.

### Condition C — same agent, QUERY not authorized

The controller cannot execute QUERY.

The answer operator receives no bit and returns 0.

Score: 1/2.

### Condition D — same agent, budget 0

QUERY is authorized in principle but cannot be executed because its cost is one.

The answer operator receives no bit and returns 0.

Score: 1/2.

## Replay procedure

    def answer(memory):
        return memory["bit"] if "bit" in memory else 0

    def run(secret, query_authorized, budget):
        memory = {}
        if query_authorized and budget >= 1:
            memory["bit"] = secret
            budget -= 1
        return answer(memory)

    for authorized, budget in [(False, 0), (True, 1), (False, 1), (True, 0)]:
        score = sum(run(s, authorized, budget) == s for s in (0, 1))
        print(authorized, budget, score)

Expected output:

    False 0 1
    True 1 2
    False 1 1
    True 0 1

## Exact argument

Before QUERY, the observation is identical for s=0 and s=1.

Any deterministic one-shot answer rule based only on that identical observation must emit the same answer in both cases.

Since the two correct answers differ, such a rule cannot be correct on both states.

One authorized query makes the states distinguishable.

The subsequent answer therefore can be correct on both.

## What changed

The model answer rule did not change.

What changed was:

- the available action set;
- the remaining budget;
- the observation returned by the environment;
- persistent state available to the later model call.

The witness therefore isolates the architectural contribution of the interaction loop.

## Claim boundary

This witness establishes the exact four-condition result for the declared two-state toy system.

It does not show that tool use improves arbitrary tasks, that language-model agents are reliable, that more autonomy is desirable, or that a particular commercial agent framework is superior.

It demonstrates only that an authorized information-gathering transition can change what is computable by a fixed downstream answer rule because it changes the information available to later decisions.
