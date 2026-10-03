# Chapter Specification — ATLAS-CH-CONTINUAL-001

## Identity

- Stable ID: `ATLAS-CH-CONTINUAL-001`
- Title: **Continual Learning and Forgetting**
- Part: `ATLAS-PART-MEM`
- Status target: `draft-v0.1`
- Hard prerequisites: `ATLAS-CH-MEMTAX-001`, `ATLAS-CH-OPTBASE-001`
- Implementation issue: #105
- Baseline: `8a08c5db5322f027dd9214618f21ed88ce9255c0`

## Contract

Study replay, consolidation, EWC, parameter isolation, and forgetting under sequential learning.

## Evaluation object

For contexts `1,...,T`, let `R_{i,j}` be performance on context `j` after training through context `i`.

For a sequence with `T>=2`, and for `j<T`, define

`B_j=max_{k=j,...,T-1} R_{k,j}`

and Atlas endpoint forgetting

`F_j=max(0,B_j-R_{T,j})`.

Also record:

`F_avg=(1/(T-1)) sum_{j<T} F_j`

and

`F_max=max_{j<T} F_j`.

These are declared Atlas summaries, not universal metric definitions. Aggregate across contexts only when scores are commensurate or a normalization is declared; otherwise retain the per-context values. Preserve positive backward transfer separately when relevant.

## Required distinctions

- performance loss versus parameter movement;
- severe forgetting versus ordinary evaluation variation;
- replay versus consolidation;
- EWC versus exact retention;
- replay versus gradient constraints;
- parameter isolation versus external memory;
- average versus worst-context forgetting;
- task-, domain-, and class-incremental evaluation.

## Mechanism families

Replay/rehearsal reintroduces prior examples, experiences, or generated substitutes into later learning.

EWC uses

`L_EWC(theta)=L_B(theta)+(lambda/2) sum_i F_i(theta_i-theta^*_{A,i})^2`

with diagonal importance weights motivated in the cited source by a Fisher-based local approximation.

GEM uses episodic memory together with gradient constraints.

PackNet-style isolation freezes or reserves parameter subsets and trades interference reduction against capacity/routing requirements.

## Exact witness

Use one scalar parameter `w`.

`L_A(w)=(1/2)(w+1)^2`

`L_B(w)=(1/2)(w-1)^2`

Task A optimum:

`w_A^*=-1`, old loss `0`.

Task B alone:

`w=1`, new loss `0`, old loss `2`.

For `F=1`, define

`J_lambda(w)=L_B(w)+(lambda/2)(w+1)^2`.

Then

`w_lambda=(1-lambda)/(1+lambda)`

`L_A(w_lambda)=2/(1+lambda)^2`

`L_B(w_lambda)=2 lambda^2/(1+lambda)^2`.

At `lambda=1`:

`w=0`, `L_A=L_B=1/2`.

Equal-weight exact replay of both quadratic objectives also yields `w=0` in this toy. State explicitly that this equality is special to the chosen quadratic witness; replay and EWC are different mechanisms in general.

With two isolated task-selected parameters, `w_A=-1` and `w_B=1` can each achieve zero loss, at the cost of extra capacity and routing.

## Source roles

Use:

- McCloskey–Cohen for sequential catastrophic interference;
- Kirkpatrick et al. for EWC;
- Rebuffi et al. for exemplar-based class-incremental learning;
- Lopez-Paz–Ranzato for GEM and continual performance/transfer evaluation;
- Mallya–Lazebnik for parameter isolation;
- van de Ven et al. for task/domain/class-incremental scenarios.

## Downstream handoff

`ATLAS-CH-EXTMEM-001` may inherit the distinctions among replay, weight consolidation, and parameter isolation, plus explicit memory/capacity accounting.

It must independently argue what should leave parameters and enter persistent shared memory.

## Completion

Source lock, derivation packet, witness, manuscript, ledger/register/bibliography updates, tranche receipt, green validation, implementation merge, bounded audit, audit merge, frontier recomputation, and controller reset are all required.
