# Atlas direct-editorial return projector

Operational component for issue #314 and organization Project #2. This feature is an issue-comment event handler on the Atlas repository, separate from the protected MATHSOLVE reservation controller.

## Event contract

When a new comment begins with `RESULT/1` on an open Atlas issue labeled `gcl-pickup:direct-editorial`, the checker evaluates the authenticated commenter, exact `assignment_id`, syntactic `input_head`, `status` (completed / partial / blocked), the issue's own bounded assignment identity, and its organization Issue Fields. Only `GCL Campaign=ATLAS-EDITORIAL-REVIEW-001` and `GCL State=AVAILABLE` can transition.

A matching result moves the organization Issue Field `GCL State` from `AVAILABLE` to `RETURNED`, adds `gcl-state:returned`, removes `gcl-state:available`, and reads the state back. A repeat event is idempotent; an unrelated, malformed, spoofed or blocked issue receives no mutation. There is no protected approval, merge, claim, certification or independent-review claim. In particular the result's self-reported `status: completed` is **not** a chapter approval.

The workflow uses `issue_comment.created` and the default-branch workflow, plus ordinary `GITHUB_TOKEN` Issues write permission. It does not use a privileged repository secret or execute code from an untrusted comment. Do not add arbitrary comment data to shell commands.

## Limitations and governance

- The Project's RETURNED view is a discovery projection, not adjudication.
- The projector currently **does not capture** a protected result record or adjudicate completeness/quality. Source comments remain durable evidence, and a later Atlas editorial intake must evaluate them.
- The authenticated commenter may be the author of the candidate PR; that is a legitimate contribution but not independent review.
- Captured input head identity is checked for SHA-1 syntax, not compared against the *latest* PR head. Stale reviews still count as *returned evidence*, but cannot be used as exact-head acceptance.
- If an issue is `BLOCKED`, `RESERVED`, or already `RETURNED`, the projector does not reset it.
- Public `atlas-v0.1.0` and protected `main` mathematical authority remain unchanged.
- Deployment requires normal protected PR review/merge. Before merge, only the historical nine-result manual reconciliation is active.

## Validation

`python3 -m unittest discover -s tests -p test_atlas_direct_return_projector.py -v` tests standard, partial, actor mismatch, wrong assignment, other campaign, unrelated issue, bad head, duplicate, blocked, wrong status, and figure-title fallback.
