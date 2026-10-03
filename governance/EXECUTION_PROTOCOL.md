# Atlas Execution Protocol

## Transaction mode

For long-form Atlas production, bounded work should be executed as repository transactions rather than conversational micro-steps.

A transaction SHOULD encompass, where applicable:

1. source and dependency reads;
2. mathematical or editorial audit;
3. all repairs found within the bounded scope;
4. provenance updates;
5. pull-request creation or update;
6. repository-wide validation;
7. merge on green validation;
8. issue closure;
9. instantiation of the next dependency-legal tranche.

Operational rules:

- Do not emit progress-only conversational checkpoints between these steps.
- Batch connector operations where possible.
- Stop only for a genuine external blocker, failed validation requiring substantive human judgment, or an explicit governance gate.
- CI or API latency is not itself a reason to hand control back to the Human Steward.
- Preserve every repair and disposition in the repository rather than in chat-only state.

This protocol exists to prevent artificial interruption of long governed research runs while preserving boundedness, auditability, and human control.
