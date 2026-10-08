# EDITORIAL-DIRECT-RETURN-SMOKE-001 — production live intake

Date: 2026-10-08. Parent editorial campaign #314. No mathematical or editorial review claim.

- Protected main prior to smoke: `35555ce031d68c26a3d53f8981e0443ad39b811d`; PR #356 merged successfully to this exact commit, containing `.github/workflows/atlas-direct-editorial-returns.yml`, projector source and 15 local tests.
- Protected-main `validate` success read back after merge.
- The code review under separate agent role `ADVERSARIAL_CHECK` is PR #356 review ID `5456674812`, role pass `ATLAS-OPS-PROJECTION-356-ADV-001`. Authentication is transport; this is not a distinct-person requirement.
- Canary issue [#359](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/359) was expressly created as `TEST_ONLY`, with `ASSIGNMENT_ID: ATLAS-PROJECTION-CANARY-001`. Organisation Issue Fields set `GCL Campaign=ATLAS-EDITORIAL-REVIEW-001`, `GCL State=AVAILABLE`. Temporary project item `PVTI_lADOB9Ao_c4Blwurzg_ZfUs` was added to Project #2.
- Authenticated synthetic `RESULT/1` posted as issue comment ID `6060064035`, with `github_actor: fyremael`, `agent_role: QA_AUTOMATION`, `agent_run_id: ATLAS-PROJECTION-CANARY-001-SMOKE`, exact reviewed head `35555ce031d68c26a3d53f8981e0443ad39b811d` and `status: completed`. It explicitly declared that it was not an editorial contribution.
- Production [GitHub Actions run 37778482191](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/37778482191) on `issue_comment` at exact main head completed `SUCCESS`.
- Fresh GitHub REST Issue Fields readback showed `GCL State=RETURNED` (previously AVAILABLE) and campaign unchanged. Therefore automated projector write authority is proven in the production runner.
- Canary issue #359 was subsequently **closed**, and temporary Project #2 item **deleted**, to avoid polluting genuine agent job counts. No protected source, mathematical claim, figure or public release mutation was part of the canary.
- Nine earlier real RESULT/1 records #326–#334 remain RETURNED. These are evidence contributions; substantive agent-role review completeness must be judged independently of the GitHub login. Other available jobs remain available.

**Disposition:** `PASS` for live Atlas direct-return operational projection. This is not editorial acceptance, not an agent-claim mechanism, and does not authorize v0.1.1 publication. Exact main head and run must be rebound for any future state assertions.
