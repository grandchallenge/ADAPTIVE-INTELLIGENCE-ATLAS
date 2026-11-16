# OWI-DS-002 — Pinned original LambdaBeam trained-checkpoint compatibility gate

**Programme:** [OWI-DS-002 #483](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/483). **Proposed disposition:** a safe structural checkpoint audit only; actual retained model-state evidence and admission still require exact-head CI.

## Questions answered and not answered

The protected GCL #500 comparator executes the independent NeurIPS-2023 LambdaBeam *original bottom-up enumeration* algorithm but does not use the trained LambdaBeam neural model. This is an explicit open scientific obligation, not a minor nomenclature issue.

At pinned public upstream LambdaBeam commit 61986dc1a6d8cc9521fb17e3152f7f085b5d7c95, the original DeepCoder domain defines 28 classes in its get_operations() list, and the published evaluation configuration enables use_op_specific_lstm=True. The DeepCoderModel constructs an op-indexed LSTM for every operation, plus op-specific initialization modules. The source-locked 2024 ExeDec benchmark requires 38 fixed-lambda instantiated legal operators: ten first-order, ten Map variants, eight Filter/Count predicate variants, five ZipWith variants, five Scanl1 variants. The original trained checkpoint has not yet been structurally read back in this document's proposed state.

The fixed-lambda adapter from #500 uses those 38 legal atoms with exact ExeDec execution semantics and disables LambdaBeam's arbitrary free-lambda search. The original 28-op *trained model* does not automatically acquire ten correctly trained additional operator heads, nor does a shared human-readable primitive name prove identity of its learned parameters. This gate checks actual original checkpoint layout, not just source-code implications.

## Safe exact-evidence protocol

Original source and binary model/checkpoint are obtained from the original repository and exact commit. Require the original checkpoint's Git blob SHA1 identity 91ab03f94972f4f523dfaa771a45ea28583f519f and exact byte length 40,750,571. Additionally verify seven original source Git blobs: declared DSL operations, DeepCoderModel, op-init, arg selector, trained model runner, checkpoint writer, and published evaluation config.

**Do not execute untrusted checkpoint pickle bytes.** The new gate reads the original PyTorch ZIP envelope, extracts bounded data.pkl *as bytes* and uses stdlib pickletools.genops to **parse data opcodes only**. It does not call pickle.load or torch.load, instantiate the neural model or import model-specific Python classes from checkpoint. It enumerates literal named model tensor keys for two independent index families: op_specific_lstm.(index).* and init.op_specific_mod.(index).*; both must span the exact 28 original source operations without gaps. A malformed/ambiguous or differently structured checkpoint fails closed as **evidentiary inconclusive**, not as evidence of incompatibility. This is static metadata analysis: it does not verify tensor shape consistency, runtime loadability, semantics of learned representations, or trained model quality.

The exact ExeDec DSL operation count is computed from the protected source-locked interpreter grammar, not guessed or copied from a narrative. A matched original 28-head checkpoint in a 38-atom exact DSL has a **structural parameter-map deficit**, which bars direct unmodified pretrained checkpoint reuse. Mapping non-identical lambda families to original heads is an engineering/model adaptation operation that must be declared and evaluated. Different original operator names/index assignments also prevent an unreviewed bare state_dict transposition.

## Legitimate continuation paths

A **native restricted trained search** could load original weights in the original 28-op model and constrain the original generated expression grammar, then translate only legal fixed-lambda ExeDec terms to source-locked executable programs. This requires a mechanically checked DSL translation including nontrivial nested lambdas, semantic validation, and a post-search private evaluator. Alternatively, a **38-operation retrained or fine-tuned neural model** can initialize new/changed operation-specific parameters and train with exact ExeDec source tasks plus independent held-out controls; its compute and corpus contamination must be included in the comparison. Neither route is validated by a structural audit.

An index/weight count mismatch *rejects drop-in checkpoint reuse*; it does not prove pretrained transfer impossible, an insurmountable semantic incompatibility, or poor downstream accuracy. A model-weight audit is not an executed neural experiment, a C1 chosen-run derivative, a causal D self-model or an equal-total-compute A/B/C/D study. Preserve issue #483 open until these research obligations are actually discharged.
