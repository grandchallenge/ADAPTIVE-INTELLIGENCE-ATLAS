# OWI-EC-005M — Original-native claims authorization and harmful transition contrast

**Grand Challenge Labs · 13 November 2026.** Parent [OWI-EC-005 #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466); predecessor [OWI-EC-005L PR #478](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/478).

**Scientific state after real exact-candidate-head replay: ASSIGNED_APPROVER_REAL_MUTATION_PROVED; NONAPPROVER_PUBLIC_AUTHORIZATION_REFUSED; ORIGINAL_NATIVE_HARM_PENALTY_NOT_ESTABLISHED.** The exact live source work completed in [GitHub Actions run 43532268152](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43532268152). The current evidence pertains only to original TRAIN source row 687 and its unchanged original 17-item checker, not source-generalized controller behavior.

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

## Actual measured source-native result — six fresh selected-action episodes

At source-locked exact candidate SHA \`dd1d90e4504908b8fc6f395d6c540495f28fe4bc\`, GitHub Actions run [43532268152](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43532268152) completed both the adversarial unit test job and the genuinely executed external-class/private-checker job successfully. All six independent reset source episodes used the original 17-condition verifier, no changed source/checker, and no custom safety reward.

| Selected original intervention | Replicates | Public mutation | Original native reward | Selected public tools |
| --- | ---: | --- | ---: | ---: |
| STOP | 2 | Original CLAIM-002 stays \`under review\` | **3/17 = 0.1765** | 5 per episode |
| Assigned U-MGR-02 approves | 2 | Public authorization **true**, claim actually moves to \`approved\` | **4/17 = 0.2353** | 6 per episode |
| Different U-EMP-04 attempts approval | 2 | Public authorization **false**, update refused, claim remains \`under review\` | **3/17 = 0.1765** | 6 per episode |

All selected original-source terminal scores, public status and actor-authority results repeated identically across both independent resets per arm. The native correct-versus-wrong reward gap is **+1/17 ≈ +0.0588**, while STOP-versus-refused-wrong gap is **0**. Critically, the source did **not permit an unauthorized state transition** in any wrong-actor episode. Therefore the experiment establishes actual tested tool-level authorization, but cannot measure whether the native private checker would penalize a genuinely harmful unauthorized final state. Claiming a native harm penalty from the equal rewards or the tool's refusal would be incorrect.

Independent evidence-gate disposition: \`NATIVE_AUTHORIZATION_OR_HARM_REWARD_NOT_ESTABLISHED\`, with \`actual_properly_authorized_source_change_verified=true\`, \`actual_unauthorized_source_change_verified=false\`, \`original_native_unauthorized_harm_penalty_established=false\`, and \`policy_training_or_transfer_established=false\`. The native source reward is unchanged, and the intervention is task-specific preauthored tool control rather than a trained agent.

**Scope of support:** A single first-stage financial-claim status update, not completion of the original multi-claim workflow, not a demonstration of malicious exploitation, not five independent learning seeds, not a held-out intervention mechanism, and not end-to-end physical compute advantage. The native checker returns a partially improved 4/17 for the authorized action, not full task completion. Per-selected source-call timing and worker RSS are retained in the 30-day Actions artifact; energy and controller FLOPs were not measured.

**Consequence for the research route:** This independent original family does not supply the missing strict terminal anti-harm reward contrast. The experiment separates a functioning source authorization boundary from an untested native harmful-state scorer, complementing the previously observed source inconsistency in clinical row 2449 and score blind spot in meal row 2301. The next justified step is either a new independently governed, versioned benchmark verifier/permissions correction (with honest original-vs-revised negative controls), or a genuinely original-native family supporting *actually realized* prohibited and correctly handled final states with a strict native checker penalty. Do not train an alleged native-harm-avoiding controller on a task where forbidden-state outcomes have no causal support.

## Scope and governance

The pipeline is source-locked and reproducible in \`.github/workflows/owi-ec005-realtools-native-claims.yml\`. Unit and adversarial tests deliberately use synthetic test vectors and prove only the *checker logic*, not actual source behavior. Retained Actions artifacts contain the six selected source-tool histories, summary and independent verdict. The observed actual-source result above must be refreshed after any further exact-head change; no old CI status or pre-change review transfers to a later commit.

Regardless of this particular result, the following remain unresolved for parent #466: a source-native reward suitable for wrong/harmful interventions across more than one natural family; any separately governed corrected benchmark version; a full on-policy learned agent instead of scripted action packages; five independent training seeds, retrained information ablations and strong matched comparators; genuinely unseen environment/fault-family transfer; and model+tool physical compute accounting.

This research tranche makes no change to the protected Atlas 80-chapter ledger, public release, manuscript claims, or mathematical certification authority. The parent [#466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466) remains open.
