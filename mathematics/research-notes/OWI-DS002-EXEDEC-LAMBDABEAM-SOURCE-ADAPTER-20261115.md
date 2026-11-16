# OWI-DS-002 — Original LambdaBeam enumeration on exact ExeDec source DSL

Parent #483. Scientific engineering tranche: an independently authored **external published program search algorithm** (the unmodified NeurIPS 2023 LambdaBeam auxiliary bottom-up enumeration routine), not the separately published **trained neural LambdaBeam policy**, and not a claim of contemporary state-of-the-art strong solver superiority.

## Source lock and semantic bridge

Original external repository ellisk42/LambdaBeam is pinned to Git commit 61986dc1a6d8cc9521fb17e3152f7f085b5d7c95. Eight load-bearing upstream code files are checked by exact Git blob hash before import. The original upstream baseline search code and algorithm are not edited or forked. Its only configuration difference is disabling general free-variable lambda generation: the immutable 2024 ExeDec DeepCoder DSL provides a fixed, complete list of legal higher-order lambda tokens; all are compiled into typed atomic operations instead.

The GCL-domain adapter is necessarily new and must not be described as upstream work. It maps every legal ExeDec operation/lambda from the protected #493 source-concordance-tested interpreter to the original upstream OperationBase API. Every proposal is evaluated with exact ExeDec intermediate-value integer/list bounds and undefined-operation behavior. Candidate search sees **only public input/output examples**; source target programs, evaluator-only novel inputs, reference outputs and any C1/D privileged information are not supplied. Any proposed expression is extracted into typed ExeDec straight-line code and independently checked with the original #493 admission verifier, including 16 fresh evaluator inputs.

The external algorithm itself is independently authored, and the exact semantic adapter is locally authored. This distinction matters: the result cannot be called an independently validated full external ExeDec system until the adapter's input/type/semantics/instrumentation and actual source replay are reviewed. The source corpus is published and reference solutions are visible upstream; procedural source projection does not give a cryptographically blind holdout.

## Study and resource accounting

The exact-head CI runs the original published source on the same source-pinned ExeDec 12 tasks (indices 0 and 17 in each of six structural splits), each with five seeded randomized operation orders. An ExeDec-exact protected GCL register-search baseline #498 runs on the **same GitHub Actions runner and task/seed pairs**, with 1.5 seconds per-case configured wall cap and maximum 15,000 search attempts; the search engines differ materially in cost/grammar search strategy and object allocation. The external code weights expressions, while GCL counts attempted register successors, so 15,000 attempted values and 15,000 attempted successors do not establish equal computational work. All positive, negative, inconclusive and unmatched cases are retained.

A further 54 distinct published source tasks, nine fresh indices per each of six structural splits, are evaluated with one new seed. No trained neural checkpoint is loaded; no GPU claim, no hidden reward and no intervention feedback enters either search.

Each trial records exact immutable external source ID, ExeDec split Git blob, task index/seed and public projection digest; original search value-exploration count, CPU/wall, executable candidate or explicit none, separate independent checker verdict, and process peak RSS. Run jobs and artifact digest are evidence. An externally sourced algorithm may still perform poorly or terminate without candidates; CI must not hide that.

## Scientific boundaries and next work

An outcome-only external program-search baseline with exact ExeDec semantics is a valuable step toward stronger comparison, but NOT the trained neural LambdaBeam method, complete DSL verification on arbitrary programs, a global solver advantage, or a full equal-total-compute A/B/C/D study. In particular, original free-variable lambda generation is disabled for semantic compatibility. C1 requires a separately admitted smooth fixed-shape chosen-run JVP interface, charged derivatives and shuffled/surrogate controls; D requires genuine held-out causal intervention prediction. Both scientific goals remain open after this engineering phase.
