# Atlas Execution Protocol

## Transaction mode

Long-form Atlas work is executed as bounded repository transactions rather than conversational micro-steps.

A transaction SHOULD encompass, where applicable:

1. read the current checkpoint, ledger, dependencies, and source locks;
2. execute the bounded mathematical/editorial work;
3. repair every defect found within scope;
4. update provenance, witnesses, figures, and governance records;
5. open or update the pull request;
6. run repository-wide validation;
7. merge only on green validation;
8. close completed issues;
9. write the next durable checkpoint.

### Conversational rule

Do not emit progress-only conversational checkpoints between these steps.

Return control to the Human Steward only when:

- a genuine external blocker prevents further work;
- a failed validation requires substantive human judgment rather than repair;
- an explicit governance gate requires human approval;
- the bounded transaction is complete.

API latency, CI latency, connector pagination, or the need for another routine tool call are not blockers.

### Durable checkpoint

The current transaction state is stored on the fixed controller branch:

- branch: `state/atlas-controller`
- path: `governance/ACTIVE_TRANSACTION.yaml`

The controller branch is deliberately separate from manuscript branches and `main`, so checkpoints can be updated without opening a PR or perturbing a content branch.

That file is the recovery authority after a conversation interruption. On resume:

1. read it first;
2. verify its baseline/branch against GitHub;
3. continue from `next_action`;
4. do not reconstruct state from chat memory when the repository checkpoint is available.

### Checkpoint discipline

Update the checkpoint on `state/atlas-controller` whenever the transaction crosses a durable boundary:

- tranche instantiated;
- source lock complete;
- draft complete;
- PR opened;
- CI green;
- merged;
- audit instantiated;
- audit merged.

Each checkpoint must record:

- issue;
- chapter/tranche;
- branch;
- baseline commit;
- current state;
- next action;
- stop conditions;
- relevant PR when one exists.

### Batching

Connector operations SHOULD be batched through orchestration calls where possible. Independent reads SHOULD be parallelized. Sequential write chains SHOULD be completed inside one orchestration call when their outputs determine subsequent writes.

The objective is continuity without weakening boundedness, provenance, validation, or human control.
