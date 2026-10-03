# AUDIT-024 — Continual Learning and Forgetting

## Disposition

**PASS AFTER TWO EVALUATION-GRAMMAR REPAIRS**

ATLAS-CH-CONTINUAL-001 remains at `draft-v0.1`.

The chapter correctly treats continual learning as sequential behavioral retention under changing training evidence and keeps replay, consolidation/EWC, episodic gradient constraints, and parameter isolation as distinct mechanisms.

AUDIT-024 found two in-scope defects in the evaluation grammar:

1. `F_avg` and cross-context `F_max` were written without stating that the sequence must contain at least two contexts and that cross-context score aggregation requires commensurate score scales or an explicit normalization;
2. the chapter described the performance record as lower-triangular while also discussing forward transfer. The lower triangle is sufficient for retention/forgetting, but forward transfer requires evaluation of not-yet-trained contexts plus a declared untrained/reference baseline.

Both defects are repaired in the specification, derivation packet, and manuscript.

No source identity, EWC equation, GEM constraint sign, exact witness arithmetic, mechanism boundary, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  `b726917e1b40d37ce0f0459035ef9b7e07e0fa6b`;
- implementation PR:
  #105;
- audit issue:
  #106;
- chapter:
  `ATLAS-CH-CONTINUAL-001`.

## 1. Hard prerequisites

PASS.

The source lock binds exactly:

- MEMTAX manuscript blob:
  `de0cc5225e84748311f4a36e7a81f1978414aa6e`;
- AUDIT-019 blob:
  `68bb06442a7f1f6137b24bf6e7fc583977053ded`;
- OPTBASE manuscript blob:
  `42df47c50c2d6d26da65a58b230040e2663f901f`;
- AUDIT-012 blob:
  `28929ba6b4a16a3cef4a871fd9253d76e8a93634`.

The chapter consumes memory-role/locus discipline and first-order optimization machinery only within those audited scopes.

No External Memory or Context Compilation manuscript is used as hidden prerequisite authority.

## 2. External source identities and roles

PASS.

The source lock identifies:

- McCloskey and Cohen (1989), catastrophic sequential interference;
- Kirkpatrick et al. (2017), Elastic Weight Consolidation;
- Rebuffi et al. (2017), iCaRL/exemplar-based class-incremental learning;
- Lopez-Paz and Ranzato (2017), GEM and transfer-aware continual evaluation;
- Mallya and Lazebnik (2018), PackNet parameter isolation;
- van de Ven, Tuytelaars, and Tolias (2022), task/domain/class incremental scenarios.

The source roles are bounded.

No source is promoted into a universal best continual-learning method or an exact zero-forgetting guarantee.

## 3. Performance-through-time object

PASS AFTER REPAIR.

For encountered contexts, the chapter uses

`R_{i,j}`

for performance on context `j` after training through context `i`.

The lower-triangular encountered-context record is sufficient for acquisition and retention analysis.

If a protocol evaluates future contexts `j>i`, those entries may complete a full matrix for forward-transfer analysis.

A forward-transfer claim additionally requires a declared untrained/reference baseline.

The chapter no longer implies that forward transfer can be recovered from the lower triangle alone.

## 4. Forgetting summaries

PASS AFTER REPAIR.

For `T>=2` and earlier context `j<T`:

`B_j=max_{k=j,...,T-1}R_{k,j}`.

Atlas endpoint forgetting is

`F_j=max(0,B_j-R_{T,j})`.

The chapter also defines

`F_avg=(1/(T-1))sum_{j<T}F_j`

and

`F_max=max_{j<T}F_j`.

The repaired chapter now states that cross-context aggregation is meaningful only when scores share a commensurate scale or an explicit normalization.

Otherwise the per-context `F_j` values remain the correct report.

These metrics are labeled Atlas summaries rather than universal standards.

## 5. Catastrophic-forgetting boundary

PASS.

The manuscript does not label every performance decline catastrophic.

It requires a declared protocol and magnitude/severity context, while accurately attributing the catastrophic-interference terminology to McCloskey and Cohen and the catastrophic-forgetting terminology used in the later literature.

## 6. Incremental-learning scenarios

PASS.

The task-, domain-, and class-incremental distinctions are used to expose different inference contracts.

In particular, task-specific routing is not treated as equally available in class-incremental evaluation.

The manuscript therefore does not compare results across these regimes as though evaluator context information were identical.

## 7. Replay/rehearsal

PASS.

Replay is defined as reintroducing prior evidence into later optimization.

The chapter correctly separates:

- the training use called replay;
- the storage locus/lifetime/addressability of the remembered information.

It also states that bounded or biased replay does not imply exact retention.

## 8. EWC equation and scope

PASS.

The chapter uses

`L_EWC(theta)=L_B(theta)+(lambda/2)sum_i F_i(theta_i-theta^*_{A,i})^2`.

This matches the cited EWC form.

The Fisher diagonal is described as a local/tractable approximation used to weight parameter importance.

The manuscript explicitly rejects:

`EWC = exact behavioral retention guarantee`.

## 9. Exact quadratic witness

PASS.

The witness uses

`L_A(w)=(1/2)(w+1)^2`

and

`L_B(w)=(1/2)(w-1)^2`.

Independent exact replay confirms:

- Task A optimum `w=-1`: `(L_A,L_B)=(0,2)`;
- Task B optimum `w=1`: `(L_A,L_B)=(2,0)`;
- sequential B-only optimization therefore raises old-task loss from `0` to `2`.

For

`J_lambda=L_B+(lambda/2)(w+1)^2`,

the exact minimizer is

`w_lambda=(1-lambda)/(1+lambda)`.

At that point:

`L_A=2/(1+lambda)^2`;

`L_B=2lambda^2/(1+lambda)^2`.

At `lambda=1`:

`w=0`;

`L_A=L_B=1/2`.

The witness Claim boundary is correct.

## 10. Replay/EWC coincidence

PASS.

Equal-weight exact rehearsal in the toy minimizes

`L_A+L_B=w^2+1`

and therefore also yields `w=0`.

The chapter explicitly states why this is a special coincidence:

the old task loss is itself exactly the quadratic used as the chosen retention penalty.

It does not infer general replay/EWC equivalence.

## 11. GEM gradient constraint

PASS.

Let `g_j` be the remembered-task gradient and `g_tilde` the proposed update gradient.

For update

`theta' = theta-eta g_tilde`,

the first-order remembered-loss change is

`-eta g_j^T g_tilde`.

Thus

`g_j^T g_tilde>=0`

is the correct linearized non-increase condition.

The manuscript keeps this as a local/first-order statement over remembered losses, consistent with the cited GEM formulation, and does not promote it into a finite-step global retention theorem.

## 12. Parameter isolation

PASS.

The scalar contrast introduces two task-selected parameters:

`w_A=-1`,
`w_B=1`.

Both task losses can then be zero.

The manuscript correctly accounts for the changed resource/inference contract:

- extra capacity;
- task-conditioned routing.

It explicitly refuses to transfer this result directly to class-incremental evaluation without task identity.

## 13. Stability-plasticity interpretation

PASS.

The exact scalar family shows:

- `lambda=0`: maximal adaptation to B and old loss `2`;
- `lambda=1`: balanced toy compromise `1/2,1/2`;
- large `lambda`: increased retention of A and worse fit to B.

The chapter labels this a local capacity-conflict witness rather than a universal theorem that all continual learning reduces to one scalar tradeoff.

## 14. Capacity and memory accounting

PASS.

The chapter requires resource costs to remain visible, including exemplars, generated replay, importance statistics, task-specific heads/masks, and reserved parameters.

Zero forgetting obtained by unlimited model duplication is therefore not silently compared with fixed-capacity methods as though the resource contracts matched.

## 15. Memory-taxonomy compatibility

PASS.

Replay is a training use, not a storage locus.

Consolidation does not automatically make parameters a semantic database.

Parameter isolation is not external memory.

These distinctions preserve MEMTAX-001.

## 16. Downstream handoff

PASS.

ATLAS-CH-EXTMEM-001 may inherit:

- replay as access to retained records;
- parameter consolidation as a distinct retention mechanism;
- parameter-isolation capacity/routing costs;
- behavioral forgetting metrics;
- the distinction between stored evidence and protected weights.

It must independently establish the external-memory thesis.

## 17. Integrity

PASS subject to audit merge validation.

The Chapter Ledger records CONTINUAL-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-CONTINUAL-LOCK-001`.

The bibliography closes all six manuscript citation keys.

The witness contains an explicit `## Claim boundary`.

No governed figure is required for this tranche; the exact one-dimensional tradeoff is clearer in equations and exact rational outputs.

## 18. Final disposition

AUDIT-024 passes after two evaluation-grammar repairs.

The durable continual-learning layer is:

**sequential context stream -> performance-through-time record -> measured interference/transfer -> protection mechanism -> retained capability under explicit memory, capacity, routing, and evaluation contracts.**
