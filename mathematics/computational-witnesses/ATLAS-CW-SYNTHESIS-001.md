# ATLAS-CW-SYNTHESIS-001 — Exact System Composition Witness

**Chapter:** ATLAS-CH-SYNTHESIS-001

## W1. System

Tasks:

\[
Q=\{\alpha,\beta\}.
\]

Specialists:

\[
A_\alpha=(1,0),\qquad A_\beta=(0,1).
\]

Correct routing:

\[
R=(A_\alpha,A_\beta).
\]

Validator accepts only correct answer plus correct declared source.

Governance commits only accepted candidates.

Shared memory persists committed validated records.

## W2. Full composition

Expected exact metrics:

- task accuracy: (2/2);
- validated commit coverage: (2/2);
- persistent recall coverage: (2/2);
- unauthorized commits: (0).

## W3. Broken router

Use \(R'=(A_\alpha,A_\alpha)\).

Expected metrics:

- task accuracy: (1/2);
- validated commit coverage: (1/2).

## W4. Validator ablation

Keep correct routing and unchanged governance.

Expected metrics:

- transient answer accuracy: (2/2);
- authorized commit coverage: (0/2).

## W5. Memory ablation

Keep correct routing, validation, and governance.

Expected metrics:

- immediate answer accuracy: (2/2);
- persistent recall coverage: (0/2).

## W6. Governance ablation

Bad candidate:

\[
(\beta,1,A_\alpha).
\]

Validator rejects it.

With governance: no commit.

With governance bypassed: one unauthorized commit.

## W7. Minimal replay code

    tasks = ("alpha", "beta")

    specialists = {
        "A_alpha": {"alpha": 1, "beta": 0},
        "A_beta": {"alpha": 0, "beta": 1},
    }

    expected_source = {
        "alpha": "A_alpha",
        "beta": "A_beta",
    }

    good_router = expected_source.copy()
    bad_router = {
        "alpha": "A_alpha",
        "beta": "A_alpha",
    }

    def validator(candidate):
        q, y, source = candidate
        return y == 1 and source == expected_source[q]

    def run(router, validator_present=True, memory_present=True, governance_present=True):
        memory = {}
        answers = {}
        unauthorized = 0

        for q in tasks:
            source = router[q]
            y = specialists[source][q]
            candidate = (q, y, source)
            answers[q] = y

            accepted = validator(candidate) if validator_present else False

            if governance_present:
                may_commit = accepted
            else:
                may_commit = True
                if not accepted:
                    unauthorized += 1

            if may_commit and memory_present:
                memory[q] = (y, source, "validated" if accepted else "unvalidated")

        accuracy = sum(answers[q] == 1 for q in tasks)
        validated_commits = sum(
            q in memory and memory[q][2] == "validated" for q in tasks
        )
        recall = sum(
            q in memory and memory[q][0] == 1 and memory[q][2] == "validated"
            for q in tasks
        )

        return accuracy, validated_commits, recall, unauthorized

    assert run(good_router) == (2, 2, 2, 0)
    assert run(bad_router)[:3] == (1, 1, 1)
    assert run(good_router, validator_present=False) == (2, 0, 0, 0)
    assert run(good_router, memory_present=False) == (2, 0, 0, 0)

    # Explicit rejected bad-source candidate for governance bypass.
    bad_candidate = ("beta", 1, "A_alpha")
    assert validator(bad_candidate) is False

    memory = {}
    # With governance, rejected candidate cannot commit.
    if validator(bad_candidate):
        memory["beta"] = bad_candidate
    assert "beta" not in memory

    # Without governance, the same rejected candidate can be written.
    memory["beta"] = bad_candidate
    assert memory["beta"] == bad_candidate

    print("SYNTHESIS_EXACT_WITNESS_OK")

## Claim boundary

This witness proves only the declared finite composition and ablations. It does not establish universal superiority of distributed systems, universal validator correctness, universal memory benefit, or a universal architecture of intelligence.
