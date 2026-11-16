# OWI-DS-002 — Native LambdaBeam 28-op expressions to exact ExeDec source-language gate

**Parent:** OWI-DS-002 #483. **Provenance:** Original independently authored LambdaBeam NeurIPS 2023 source at Git commit 61986dc1a6d8cc9521fb17e3152f7f085b5d7c95. Exact ExeDec source tasks at google-deepmind/exedec commit ef046ce2cc3fcd024e32f5dfe00e69700dac82ed.

The original pretrained model has 28 indexed operation-specific LSTM/init weight heads, confirmed against its actual 40.75MB original checkpoint in protected PR #501. ExeDec's DSL has 38 legal instantiated fixed-lambda operations. Direct weight import into the exact ExeDec 38-op model was rejected; **native original 28-op program generation followed by a strictly verified adapter** is a legitimate next route.

## Exact native-expression subgrammar

The new Python translator is an allowlist and static syntax compiler. It never calls Python eval, exec, pickle.load, torch.load or arbitrary code and does not require running an unverified model. It parses with stdlib ast.parse in expression mode, then recursively reduces under fixed input, type, AST-size, recursion-depth and target source-size caps. There is no acceptance based solely on observationally matching examples.

Admitted native root operators: Head, Last, Take, Drop, Minimum, Maximum, Reverse, Sort, Sum, Map, Filter, Count, ZipWith, with public ExeDec bounded integer/list inputs and strict source compiler type rules. Native higher-order lambdas must normalize by **capture-safe immediate beta substitution** to the fixed ExeDec library: ten unary transforms, four predicates and five binary operators. This includes commuted simple unary/binary forms and immediately applied nested lambdas that normalize to one fixed operator. It does **not** support arbitrary closure-dependent lambdas, learned recursive functions, source Python arithmetic syntax not emitted by LambdaBeam, direct scalar arithmetic expressions, conditional branching, extra keywords, unsupported constants, unbound names, attribute access, unsafe Python calls, unrestricted beta reductions or unconstrained source generation.

## Explicit semantic mismatch exclusions

- Access: original LambdaBeam uses Python negative indexing: Access(-1,[1,2]) returns 2. Exact ExeDec rejects a negative index, returns None. Reject all native Access until a separately verified nonnegative-index proof is admitted.
- Scanl1: original constructs its first result from xs[0] and fails on an empty list, while ExeDec returns []. Reject all native Scanl1 until an explicit nonempty-list proof or separately authorized semantic adapter is available.

For this deliberately restricted grammar, **32 of 38** ExeDec atomic operator variants are statically representable with native operator-class expressions; one Access and five Scanl1 variants are excluded. The gate separately executes original hash-locked published operator implementations and the protected exact ExeDec interpreter on bounded sample inputs, comparing successes and undefined cases. These are finite source-semantic checks, not a complete mathematical equivalence proof. Discrepancies fail exact-head CI and preserve negative records.

## Original 1,200 source tasks and future genuine trained candidates

The workflow reads all 1,200 published source reference programs across six hash-pinned ExeDec JSONL splits **only for retrospective structural coverage auditing**: count how many reference solutions have no excluded operators. Source references are not fed to a model or the participant-view candidate translator. Do not misreport reference-grammar eligibility as synthesis success or a hidden holdout. Every published source row is public.

A fail-closed candidate interface consumes records containing only split, index and native_expression. It projects only the public I/O task, translates the original native expression through the strict grammar, independently verifies all public examples using exact ExeDec, and only **after a candidate exists** calls the reference-based independent evaluator with 16 generated valid fresh inputs. Malformed, unsupported and noncompatible programs retain negative results rather than being silently rewritten. This interface makes future genuine native pretrained 28-head beam outputs testable while excluding source targets from search. It does **not itself attest** that a submitted receipt originated from the trained checkpoint.

## Resource, exact-head replay and custody

The workflow fetches only pinned upstream Python source paths via Git partial+sparse checkout, avoiding redundant download of the already hash-verified 40.75MB model checkpoint. It verifies seven pinned model/source blobs and eight original enumeration/operation load-bearing blobs before executing upstream native operators. No trained LambdaBeam inference occurs in this tranche; neither full fair search compute nor neural-model behavior is measured.

Original trained neural inference, source-syntax translation coverage on actual trained beams, task-independent transfer calibration, full-resource accounting, C1 chosen-run JVP, D intervention-predictive self-model, and scientific certification remain open. A translated candidate is a candidate, not a universal equivalence proof.
