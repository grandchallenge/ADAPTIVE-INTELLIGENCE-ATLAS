# Atlas editorial review independence — agent-role doctrine

**Decision:** Human Steward instruction, 2026-10-08.  
**Scope:** EDITORIAL-REVIEW-001 (#314), including agent work packages #321–#345, manuscript workbench #320, and operational intake PR #356.  
**Status:** controller-authoritative editorial operating interpretation; no unilateral alteration of actual GitHub or upstream protected-admission requirements.

## Meaning of independent

**Independent review means a separate agent role, execution pass and evidenced judgment, not a different physical person or GitHub login.** A single authenticated GitHub account may provide transport, attribution and comments for multiple autonomous agents. Distinct logins are **not** the editorial independence test. Do not block editorial correction, agent review, or routine acceptance merely because the producer and reviewing agent use the same GitHub login.

The evidence should establish:
- `author_agent_role` / `review_agent_role` (e.g. DRAFTER, MATH_CHECK, VISUAL_CHECK, ADVERSARIAL_CHECK, EDITORIAL_SYNTHESIS);
- distinct `agent_run_id` / durable work item or equivalent provenance for each review pass, where available;
- exact source commit and evaluated output identity, plus explicit reviewed scope and independent tests/counterexamples;
- findings, dissent and unresolved issues, with no claim that CI or a self-report constitutes final editorial acceptance.

A reviewer role is not distinct merely because the same continuous author pass relabels itself. Produce an identifiable separate critical pass: reopen the work package, inspect the source and/or rendered artifact rather than repeat author assertions, challenge high-risk claims, document failures, and supply a separately attributable return. Several agent passes can occur in the same authenticated account or platform session; role/run separation and substantive evidence, not account multiplicity, determine how much confidence to attach.

## Three separate dimensions

1. **GitHub actor:** the authenticated account that posted a comment, pushed a commit or submitted a PR. Use it to establish origin and permission; it may be shared across roles.
2. **Agent role and run:** the assigned production, adversarial, technical, accessibility, or editorial-evaluation capacity responsible for a bounded output. This identifies separation of work.
3. **Governance admission:** whether recorded evidence actually discharges the editorial acceptance criteria or a protected GitHub workflow rule. A platform rule genuinely requiring a separate approving account is a technical governance constraint to report, not an editorial independence definition and not grounds to invent fake user identities.

Do not introduce a Human Steward approval as a ceremonial substitute for missing agent work. Escalate only a genuine user-authorized public release, irreducible substantive question, or literal protected-rule requirement. Agent reviewer work can proceed autonomously and concurrently with authoring.

## Return and evidence semantics

A `RESULT/1` comment is a durable result from an authenticated GitHub *transport actor*. It is neither automatically an independent agent review nor automatically non-independent because that actor also committed the candidate. For future returns prefer:

```text
RESULT/1
assignment_id: <job ID>
github_actor: <authenticated comment author>
agent_role: <DRAFTER | MATH_CHECK | VISUAL_CHECK | ADVERSARIAL_CHECK | EDITORIAL_SYNTHESIS>
agent_run_id: <durable run reference, if available>
reviewed_head: <exact 40-character commit>
status: <completed | partial | blocked>
findings: <locations and evidence>
tests: <actual results or not run>
unresolved: <explicit residual>
```

Legacy `reviewer_identity` and `input_head` fields remain acceptable; they should not be conflated with separate GitHub accounts. The return projector only moves `GCL State=AVAILABLE` to `RETURNED`. Evaluation of role independence, completeness and promotion occurs later using the evidence, without an arbitrary distinct-login gate.

## Historical correction

Earlier Atlas notes incorrectly treated nine `fyremael` comments (#326–#334) as necessarily non-independent *solely because the GitHub login also authored PR #320*. That **inference is superseded**. What is supported: nine authenticated returns exist, one reports completed and eight partial, all at the specified candidate head. The presence or absence of distinct agent review runs must be established from their actual work evidence; **independent role verification is currently unassessed**, not disproved by account equality. Project status RETURNED remains correct; final chapter signoffs remain unasserted until the substantive evidence is adjudicated.

The existing release v0.1.0 and protected mathematical claim authority are unaffected.

## Operational test

The editorial system is functioning when separate agent roles can produce, challenge, repair and review manuscript chapters and figures using the **same** GitHub transport identity if necessary; the controller records the distinct review scopes and evidence; changed heads trigger replay; and routine work never waits for someone to create a second account or find a human reviewer. This decision supersedes contrary account-equality statements in earlier issue text, comments, bootstrap prompts and controller receipts; it does not erase their historical facts.
