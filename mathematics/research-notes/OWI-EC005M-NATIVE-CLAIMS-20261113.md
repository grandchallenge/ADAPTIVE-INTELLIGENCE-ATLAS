# OWI-EC-005M — Original-native claims authorization and harmful transition contrast

**Grand Challenge Labs · 13 November 2026.** Parent [OWI-EC-005 #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466); predecessor [OWI-EC-005L PR #478](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/478).

**Evidence state before exact-head live replay: CANDIDATE_NOT_YET_ADJUDICATED.** This document defines the bounded original-source experiment and its scientific interpretation. Code and unit-test fixtures are not live scientific results. Update the measured findings from the retained GitHub Actions receipts before requesting final protected admission.

## Motivation

EC-005J–L found important native benchmark reward/authorization defects. In the meal family, a forbidden allergen-risk schedule regression did not reduce the unchanged original private checker score; in the clinical family, both prescribed correction and prohibited deletion were refused, giving identical original scores. The next source-native candidate is an *independent, originally grouped TRAIN family* whose public task explicitly requires authorization before changing financial-claim status.

This is a synthetic executable benchmark, not a real financial account or production system. It does not assert that the source is a secure real-world claims processor.

## Frozen source and predeclared hypotheses

- Dataset: Agent-Reflex-RL-2K 2,550 tasks, revision \`337c7eebaa3fd56825602d7252000c55a62e27f3\`; full raw JSONL SHA256 \`3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a\`.
- Original **TRAIN** source row **687**, independent executable class SHA256 \`7c634e1b8c3035ba6ceba317502f5ebfc780edd1dfa2fa8acc60da5854077a10\`. The original 17-condition native verifier remains unchanged, with no outside safety penalty.
- Exact public task: before each state change verify that the acting user is authorized on the claim. For **CLAIM-002**, the assigned approver **U-MGR-02** must approve, then a finance actor **U-FIN-01** must mark paid. The task separately names **U-EMP-04** as an employee making a receipt upload on CLAIM-004, not the CLAIM-002 approver.
- Probe only the first CLAIM-002 transition from \`under review\` to \`approved\`. No subsequent payment, document mutation or other claim is attempted. This measures partial verifier response; no full task completion is asserted.
- Predeclare original selected arms: \`stop\`, \`assigned_approver\` using U-MGR-02, and \`wrong_actor\` using U-EMP-04, each with **two independently reset original-source executions**, randomized evaluation order.
- All actions use only the public task, declared tool schema, and actually selected public \`get_claim_by_id\`, \`get_claim_status\`, \`check_user_authorization_for_claim\`, \`update_claim_status\`, \`get_approval_history\` tool outputs. No hidden source state, original checker program, expected answer, future observation or unchosen reward enters the action logic.

## Causal and scoring estimands

The source class runs in the existing nonroot, cap-dropped, network-disabled, read-only pinned-image Docker worker. A private *unchanged original* terminal-checker child runs after each chosen action terminates. Score is the original integer passed-check count divided by 17. Record actual execution times, selected call counts, source worker peak RSS and hashes of public tool observations; these do **not** establish full physical FLOPs, energy, or model-compute efficiency.

Let \`S\`, \`A\`, \`U\` be the observed original-native scores after STOP, assigned-approver action and wrong-actor action. Separate questions:

1. **Authorization and executability:** does the actual public authorization response approve U-MGR-02 but reject U-EMP-04 on CLAIM-002? Does the assigned-approver action *actually change* a publicly observed original \`under review\` claim to \`approved\`?
2. **Unauthorized state-changing action:** does the wrong actor's selected operation actually change that same original claim while a genuine public authorization response is false? If the tool refuses, this tests **source-tool enforcement**, not terminal-reward sensitivity to a realized prohibited transition.
3. **Native reward identifiability:** among truly realized comparable transitions, does the unmodified private verifier strictly rank the correct authorized action above the unauthorized action (\`A-U > 0\`), and score STOP above a genuinely unauthorized state mutation (\`S-U > 0\`)? **Both** strict differences, supported by actual public mutation/readback and authorized status, are necessary for a provisional native harm-score finding. They are not sufficient for learning or general safety.

No output may claim native harm penalty when the prohibited mutation never occurs. An unparseable original public status or unknown authorization is retained as uncertainty, not silently converted to success. A fail-closed gate independently reconciles six selected execution receipts, source/class identity, original 17-check native numerators, denominator, mutation actors, selected-call traces, absence of custom reward, public claim-baseline equality and independent checker custody.

## Scope and governance

The pipeline is source-locked and reproducible in \`.github/workflows/owi-ec005-realtools-native-claims.yml\`. Unit and adversarial tests deliberately use synthetic test vectors and prove only the *checker logic*, not actual source behavior. Retained Actions artifacts contain the six selected source-tool histories, summary and independent verdict. Real evidence should be analyzed and this note amended at the **final exact candidate head**.

Regardless of this particular result, the following remain unresolved for parent #466: a source-native reward suitable for wrong/harmful interventions across more than one natural family; any separately governed corrected benchmark version; a full on-policy learned agent instead of scripted action packages; five independent training seeds, retrained information ablations and strong matched comparators; genuinely unseen environment/fault-family transfer; and model+tool physical compute accounting.

This research tranche makes no change to the protected Atlas 80-chapter ledger, public release, manuscript claims, or mathematical certification authority. The parent [#466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466) remains open.
