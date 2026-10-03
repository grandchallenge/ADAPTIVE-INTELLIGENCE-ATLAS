# ATLAS-CW-COORD-001 — Lost Update Under Legal Interleavings

**Chapter:** ATLAS-CH-COORD-001  
**Witness class:** exact finite concurrency enumeration  
**Purpose:** show that shared state plus locally correct read-modify-write logic does not imply the intended joint effect without an atomicity or synchronization story.

## Initial state

x = 0.

Two actors, P and Q, each intend to increment x once.

Each non-atomic increment is decomposed into:

R_i — read x into actor-local r_i;

W_i — write r_i + 1 to x.

The only scheduling constraints are:

R_P before W_P;

R_Q before W_Q.

## Complete legal interleavings

There are six interleavings preserving the two actor-local orders.

1. R_P W_P R_Q W_Q -> x=2
2. R_P R_Q W_P W_Q -> x=1
3. R_P R_Q W_Q W_P -> x=1
4. R_Q W_Q R_P W_P -> x=2
5. R_Q R_P W_Q W_P -> x=1
6. R_Q R_P W_P W_Q -> x=1

Thus:

- 2 of 6 schedules preserve both increments;
- 4 of 6 schedules lose one update.

## Replay procedure

    from itertools import permutations

    ops = ("RP", "WP", "RQ", "WQ")

    def legal(order):
        return order.index("RP") < order.index("WP") and order.index("RQ") < order.index("WQ")

    def run(order):
        x = 0
        local = {}
        for op in order:
            if op == "RP":
                local["P"] = x
            elif op == "RQ":
                local["Q"] = x
            elif op == "WP":
                x = local["P"] + 1
            elif op == "WQ":
                x = local["Q"] + 1
        return x

    schedules = [p for p in permutations(ops) if legal(p)]
    results = [(p, run(p)) for p in schedules]
    print("schedules=" + str(len(results)))
    print("final_2=" + str(sum(v == 2 for _, v in results)))
    print("final_1=" + str(sum(v == 1 for _, v in results)))

Expected output:

    schedules=6
    final_2=2
    final_1=4

## Atomic comparison

If each increment is one atomic transition INC_i: x <- x+1, only the relative transaction order remains.

P then Q yields 2.

Q then P yields 2.

## Claim boundary

The witness establishes the exact schedule counts and final states for this declared two-actor toy model.

It does not prove that transactions are universally preferable, that all shared-state systems lose updates, that real runtimes sample these six schedules uniformly, or that one database isolation level is sufficient for every application.

It demonstrates only that local correctness of two read-modify-write operations is insufficient to guarantee their intended combined effect when the operations can interleave.
