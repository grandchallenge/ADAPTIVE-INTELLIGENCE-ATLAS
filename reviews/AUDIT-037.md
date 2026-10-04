# AUDIT-037 — Curriculum Learning

## Disposition

**PASS AFTER THREE FORMAL/OBSERVABILITY REPAIRS**

ATLAS-CH-CURRICULUM-001 remains at draft-v0.1.

The implementation correctly establishes the curriculum-controller object, the open-loop/closed-loop distinction, the difficulty/competence claim firewall, the selection-versus-reweighting distinction, the GSD mechanism-inference boundary, and the finite state-dependent action-separation witness.

AUDIT-037 found three in-scope precision defects:

1. the curriculum-state transition used an undeclared feedback symbol;
2. the generic learning-progress formula did not directly encode whether the underlying metric was higher-is-better or lower-is-better;
3. the finite state-aware witness implicitly assumed full toy-state observability and repeatable experience-type actions without declaring those assumptions.

All three defects were repaired on the audit branch.

No prerequisite edge, external-source authority, bibliography identity, finite witness arithmetic, Chapter Ledger status, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  4c28148b2e9d09bf5f5ea3241e49141aeaa33d7f;
- implementation PR:
  #146;
- implementation issue:
  #145;
- audit issue:
  #147;
- chapter:
  ATLAS-CH-CURRICULUM-001.

Merged implementation artifact blobs before audit repair:

- specification:
  884515f44c13097f9d15463bb7cc652a8bf7168e;
- derivation packet:
  c89197a887dd6ac99827413ab60d1e4afc873da1;
- computational witness:
  1c68636266449d9957c420d3ea3b7952e956b214;
- manuscript:
  d81e621620e3a7c0d4844247f29a0d3498740465;
- source lock:
  6d4baa8ddcaf82a2f58dad09c884fdbc716af35c.

Repaired audit-head artifact blobs:

- specification:
  51531d7ffee7715e6152b84deef7e66374d674f3;
- derivation packet:
  06eb06b048b589d681038655b8157edf676981af;
- computational witness:
  9046b19870b1c11d1d070fd6e4f5484f464a2774;
- manuscript:
  c6f65a46034125c601322e984e378d41735586ef;
- source lock:
  2901f709c380dc5516017b33ce475899c6560d81.

## 1. Hard prerequisites

PASS.

The source lock binds exactly to the audited prerequisites at protected baseline c1122f3b6a6cb0170e77f5fe340a7bec402618ce.

### Data Quality, Mixtures, and Contamination

- manuscript blob:
  e4cb245419ad3601aa82ac33129660673ab1622c;
- AUDIT-030 blob:
  740b1340ac969bd330a995b9dca2129f4317a541;
- source-lock blob:
  701f5504e77342fad29fb4c54eb2926a0c4c90b9.

### First-Order Optimization

- manuscript blob:
  42df47c50c2d6d26da65a58b230040e2663f901f;
- AUDIT-012 blob:
  28929ba6b4a16a3cef4a871fd9253d76e8a93634;
- source-lock blob:
  fa610d3d763cc1a7e76ee4b83e85ce2c965c2825.

The project-local GSD agenda is bound separately at blob:

0f31202a928d8e2cb5e3290d84b32344033c2f19.

It is used only as research-context authority for the non-monotone mechanism-inference boundary, not as a hidden hard prerequisite.

## 2. External source scope

PASS.

The source lock uses:

- Bengio et al. (2009), Curriculum Learning, for the curriculum-learning formulation and continuation-method interpretation;
- Graves et al. (2017), Automated Curriculum Learning for Neural Networks, for automated stochastic syllabus selection from learning-progress signals in the paper's experiments;
- Platanios et al. (2019), Competence-based Curriculum Learning for Neural Machine Translation, for difficulty/competence-based scheduling in NMT.

Their empirical outcomes remain source-specific.

The Atlas does not infer universal easy-to-hard optimality, universal curriculum gains, or a universal learning-progress objective.

## 3. Bibliography closure

PASS.

Canonical bibliography blob:

f9872769b6a013bf9dfd57e4cf080206fe32b95a.

The declared keys resolve:

- BengioEtAl2009Curriculum;
- GravesEtAl2017Curriculum;
- PlataniosEtAl2019Curriculum.

## 4. Curriculum control object

PASS AFTER REPAIR.

The chapter separates:

- model state \(\theta_t\);
- optimizer state \(u_t\);
- curriculum state \(c_t\);
- controller observation \(z_t\);
- curriculum action \(a_t\);
- selected training experience \(x_t\);
- post-update feedback \(f_t\).

The implementation originally wrote the controller update with an undeclared \(\ell_t\).

The repaired artifacts define \(f_t\) explicitly as controller-visible post-update feedback and use

\[
c_{t+1}
=
\mathcal T_{\rm curr}(c_t,z_t,a_t,x_t,f_t).
\]

The learner transition and curriculum-state transition remain distinct.

## 5. Open-loop versus closed-loop curriculum

PASS.

An open-loop deterministic syllabus is represented as:

\[
a_t=\sigma(t).
\]

An open-loop stochastic curriculum may depend on time but not current learner observation.

A closed-loop curriculum uses:

\[
a_t\sim\pi_t(a\mid z_t,c_t).
\]

The chapter correctly states that randomness alone does not make a curriculum adaptive.

## 6. Difficulty semantics

PASS.

Difficulty is a declared score:

\[
d:\mathcal X\to\mathbb R.
\]

The manuscript explicitly rejects the inference:

\[
\text{difficulty score}
=
\text{intrinsic universal difficulty}.
\]

It notes that score interpretation can depend on learner, representation, objective, preprocessing, and training stage.

## 7. Competence schedule

PASS.

A competence-style curriculum may define:

\[
\mathcal X_t
=
\{x:d(x)\le q_t\}.
\]

The chapter correctly treats \(q_t\) as a controller/scheduling variable.

Naming the variable "competence" does not prove actual learner competence.

## 8. Learning-progress orientation

PASS AFTER REPAIR.

The implementation used:

\[
LP_t(r)=m_t(r)-m_{t-w}(r)
\]

while separately saying that the sign convention had to be declared.

That left the generic displayed formula directionally ambiguous for lower-is-better metrics such as loss.

The repaired chapter defines an orientation variable:

\[
\eta_r\in\{+1,-1\},
\]

and uses:

\[
LP_t(r)
=
\eta_r
\left[
m_t(r)-m_{t-w}(r)
\right].
\]

The convention is:

- \(\eta_r=+1\) for higher-is-better metrics;
- \(\eta_r=-1\) for lower-is-better metrics.

The progress signal remains explicitly dependent on metric, window, orientation, noise, and observation scope.

## 9. Progress-versus-mechanism boundary

PASS.

The chapter retains the project-local GSD rule:

> Do not infer monotone mechanism improvement from smooth loss, more training, or endpoint benchmarks.

A progress metric is therefore permitted as a curriculum-control signal without being promoted into proof of:

- acquisition;
- persistence;
- accessibility;
- internal representation change;
- mechanism identity.

## 10. Selection versus mixture reweighting

PASS.

For retained corpus \(\mathcal D\) and base measure \(\mu\), the chapter defines reweighting as:

\[
\mu_t'(x)
=
\frac{w_t(x)\mu(x)}
{\sum_{x'}w_t(x')\mu(x')}.
\]

It separately defines support-changing selection through a subset \(S_t\subseteq\mathcal D\).

The chapter notes that positive reweighting may preserve support while selection may change it.

The two interventions are not treated as definitionally identical.

## 11. Finite witness observation contract

PASS AFTER REPAIR.

The finite witness uses state:

\[
s=(e,h)\in\{0,1,2\}^2.
\]

The implementation called the policy state-aware but did not explicitly say how the controller observed this state.

The repaired specification, derivation, computational witness, manuscript, and source lock now declare:

\[
z=s.
\]

Thus the exact toy controller has full state observability.

The chapter explicitly states that this is stronger than the partial observations normally available in real training systems.

## 12. Finite witness action semantics

PASS AFTER REPAIR.

The two-step state-aware path uses:

\[
H,H.
\]

The implementation did not explicitly state whether \(H\) was a repeatable experience type or a unique without-replacement record.

The repaired artifacts define \(E\) and \(H\) as repeatable experience types.

Therefore repeated selection is legal by construction.

No empirical conclusion about repeated hard examples is inferred.

## 13. Exact witness transition rules

PASS.

State:

\[
s=(e,h)\in\{0,1,2\}^2.
\]

Nominal difficulty:

\[
d(E)=1<2=d(H).
\]

Aggregate toy score:

\[
M(e,h)=e+h.
\]

Easy transition:

\[
T_E(e,h)
=
(\min(2,e+1),h).
\]

Hard transition:

\[
T_H(e,h)
=
\begin{cases}
(e,\min(2,h+1)),&e\ge1,\\
(e,h),&e=0.
\end{cases}
\]

Progress:

\[
R(s,a)
=
M(T_a(s))-M(s).
\]

These equations are internally consistent.

## 14. Exact action reversal

PASS.

At:

\[
s_A=(0,0),
\]

the exact rewards are:

\[
R(s_A,E)=1,
\qquad
R(s_A,H)=0.
\]

Thus \(E\) is the unique one-step progress maximizer.

At:

\[
s_B=(2,0),
\]

the exact rewards are:

\[
R(s_B,E)=0,
\qquad
R(s_B,H)=1.
\]

Thus \(H\) is the unique one-step progress maximizer.

No single state-independent deterministic first action is progress-optimal for both states.

The static nominal ranking does not change.

## 15. Exhaustive witness table

PASS.

Independent replay confirms:

| State | \(R(E)\) | \(R(H)\) |
| --- | ---: | ---: |
| \((0,0)\) | 1 | 0 |
| \((0,1)\) | 1 | 0 |
| \((0,2)\) | 1 | 0 |
| \((1,0)\) | 1 | 1 |
| \((1,1)\) | 1 | 1 |
| \((1,2)\) | 1 | 0 |
| \((2,0)\) | 0 | 1 |
| \((2,1)\) | 0 | 1 |
| \((2,2)\) | 0 | 0 |

The witness correctly exposes ties and saturation in addition to the two unique-maximizer states.

## 16. Equal-transition-budget replay

PASS.

From:

\[
s_B=(2,0),
\]

fixed easy-then-hard produces:

\[
(2,0)\xrightarrow{E}(2,0)\xrightarrow{H}(2,1),
\]

with cumulative toy progress:

\[
1.
\]

The full-state immediate-progress policy produces:

\[
(2,0)\xrightarrow{H}(2,1)\xrightarrow{H}(2,2),
\]

with cumulative toy progress:

\[
2.
\]

Both execute exactly two learner transitions.

The chapter explicitly does not claim equal controller overhead or wall-clock cost.

## 17. Greedy progress versus long-horizon value

PASS.

The derivation defines one-step greedy action selection but explicitly denies the general identity between greedy immediate progress and long-horizon optimal curriculum control.

The later PROGRESSSEARCH chapter therefore retains responsibility for:

- exploration;
- experience-space search;
- long-horizon objective;
- uncertainty;
- credit assignment;
- stopping rules.

## 18. Dose and recipe confounding

PASS.

The manuscript requires curriculum comparisons to declare or control, as appropriate:

- optimizer-update count;
- tokens/examples processed;
- repeated exposure;
- batch size;
- optimizer;
- learning-rate schedule;
- initialization/seeds;
- controller cost;
- data support;
- sampling weights;
- stopping/tuning procedure.

The chapter does not attribute every endpoint difference to curriculum order.

## 19. Bibliographic/source integrity

PASS.

Source identities remain unchanged after audit repair.

No source claim was strengthened beyond the locked authority.

The source lock retains the three external papers and the audited internal prerequisite identities.

## 20. Mathematical/document integrity

PASS.

A targeted post-repair scan found:

- balanced display-math delimiters in all witness-bearing artifacts;
- no remaining use of the undeclared \(\ell_t\);
- explicit \(\eta_r\) orientation in the specification, derivation, and manuscript;
- explicit full-state observability and repeatable-action assumptions in all finite-witness artifacts.

## 21. Repository integrity

PASS subject to audit-PR validation.

At the repaired audit head:

- bibliography blob:
  f9872769b6a013bf9dfd57e4cf080206fe32b95a;
- Chapter Ledger blob:
  b48b155f74003eb87e89a18dc684d750e5ab8d2c;
- Source Register blob:
  15bb46c2d5865e03f6f8098d354194046a47a3ec.

The Chapter Ledger retains CURRICULUM-001 at draft-v0.1.

The Source Register retains ATLAS-SRC-CURRICULUM-LOCK-001.

The manuscript retains the required epistemic marker, references section, and source-lock path.

No governed figure is required.

## 22. Downstream handoff

PASS.

PROGRESSSEARCH may inherit:

- curriculum action/observation semantics;
- open-loop versus closed-loop distinction;
- oriented finite-difference progress signals;
- support/reweighting distinction;
- the finite state-dependent action-separation witness;
- the distinction between controller feedback and mechanism evidence.

It must independently define long-horizon search, exploration, uncertainty, credit assignment, and stopping.

## Final disposition

AUDIT-037 passes after three repairs.

The durable curriculum layer is:

**declared training experience space + separate learner/optimizer/controller state + explicit controller observation + open/closed-loop policy semantics + oriented progress measurements + bounded state-aware witness + strict separation between controller feedback and mechanism claims.**
