# OWI-DS002 — Explicit semantics adapter for native 28-head LambdaBeam Access/Scanl1

**Parent:** OWI-DS-002 #483. This is a disclosed, bounded engineering correction. The exact upstream LambdaBeam original source revision is 61986dc1a6d8cc9521fb17e3152f7f085b5d7c95. The source-pinned ExeDec interpreter and published dataset are from google-deepmind/exedec ef046ce2cc3fcd024e32f5dfe00e69700dac82ed. The actual original pretrained 28-head checkpoint was separately audited under PR #501. The previous PR #503 admitted a source-concordant restricted 32-of-38 atom translator and identified two incompatible original operations: Access negative-index behavior and Scanl1 on empty lists.

## Explicit original/adapted boundary

This change does NOT declare unmodified original LambdaBeam equivalent to ExeDec. It adds a specifically named semantic mode explicit_exedec_adapter. Legacy translation and original native execution defaults remain fail-closed on Access and Scanl1. Opting into the new mode admits both syntactic classes **only when the runtime operation methods used to generate and replay those expressions are the separately checked ExeDec-compatible subclasses**.

The original upstream Python operation source remains unchanged, and original published source files must pass exact Git checks before import. Two in-memory subclasses override the behavior of only the relevant native operations:

- Access: original LambdaBeam uses Python list indexing; a negative index such as -1 is accepted. Exact ExeDec rejects negative and out-of-range indices. The adapter adds the exact bounds guard, delegates valid cases to the original operation, and checks the bounded result.
- Scanl1: original LambdaBeam initializes the prefix list from xs[0], so empty input is undefined. Exact ExeDec defines an empty Scanl1 result as the empty list. The adapter returns [] on empty inputs and delegates nonempty cases to original source implementation. Crucially, it also independently enforces the exact ExeDec <=50 integer and <=5 list prefix bound, rather than the original native source's wider -256..255 / <=20 bound.

The wrapper preserves the ORIGINAL 28-operation ordering, repr operator names, arities, bound-variable shape, weights and operation names for indexed learned-head selection. The original 28-head checkpoint's weights have NOT been loaded or tested and nothing proves the trained guidance remains valid after these two explicit semantic changes. Changing the semantics is precisely a declared runtime adaptation that might affect trained beam search.

## Semantic checks and claim scope

The explicit mode extends the native AST translator's legal ExeDec atomic names from 32 to all 38 fixed-lambda variants: nine previously admitted first-order operations, the Access first-order operation, ten Map unary tokens, four Filter predicate tokens, four Count predicate tokens, five ZipWith binary tokens, and five Scanl1 binary tokens. The existing strict original mode is unaffected.

The exact-head workflow runs original source native operation code after verifying seven model and eight enumeration/operation Git blob identities. It compares adapted original source operation method results against the independently implemented source-locked ExeDec interpreter, over the prior 518-case matrix plus 49 Access and 35 Scanl1 matrix cases and targeted edge sets. All fixed 38 atomic variants must execute under both semantics and agree, including empty Scanl1, negative Access, and exact-bound overflow. Expected upstream semantic divergences must also be detected before accepting the adapted correction. This finite matrix is *not a proof of universal semantic equivalence* and does not cover all unrestricted native lambda expressions, arbitrary deep programs or learned model behavior.

## Retrospective published reference coverage

The preceding strict original runtime source audit established that 438/1200 source targets did not use Access or Scanl1, with 762 excluded by their presence. The adapted runtime now supports the full set of **source DSL operator names** in 1200/1200 published source programs, but this is solely a syntactic name-level gate. It does NOT establish full nested expression translatability from the 28-head original neural model, a model success rate, independent blind holdout, equal resource accounting, or safe trained checkpoint transfer. Reference programs are accessed only for retrospective diagnostic coverage and never during participant candidate search.

## Resource and governance

The workflow uses Git sparse/partial checkout of original source without re-downloading the already pinned 40.75MB pretrained checkpoint. The existing source-locked ExeDec verifier retains the only authority for candidate bounded execution agreement. A following separate research tranche must actually run pretrained 28-head beam inference against a controlled task set and pass candidate receipts to the newly adapted semantics mode, or retrain/fine-tune, with evaluation and training resource ledgers. Neither C1 chosen-run JVP nor D causal intervention-predictive model is run by this compatibility adapter.

Do not claim original-model unchanged inference, pretrained baseline performance, universal equivalence, formal proof, or end-to-end reflective-cognition success from the existence of a runtime adapter.
