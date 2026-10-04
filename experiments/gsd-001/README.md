# GSD-001 — Tranche A

This directory executes GSD-WP00 through GSD-WP03.

## Locked external inputs

- arXiv:2609.33150v1
- Jiaxin-Wen/GDsuite at commit e3f5de327cd90a579e50a89f04fa167c584b799f
- jiaxin-wen/generalization-dynamics-evals
- allenai/OLMo-2-0425-1B-early-training

The GCL runner verifies the load-bearing GDsuite files by Git blob SHA-1 before use.
Hugging Face model and dataset revisions are resolved to exact repository SHAs and written
into each run manifest.

## Local WP00 tests

    python -m pip install -r experiments/gsd-001/requirements-ci.txt
    PYTHONPATH=experiments/gsd-001 pytest -q experiments/gsd-001/tests

These tests require neither a GPU nor a model download.

## Prepare the locked upstream runner

On the accelerator host:

    git clone https://github.com/Jiaxin-Wen/GDsuite.git
    cd GDsuite
    git checkout e3f5de327cd90a579e50a89f04fa167c584b799f
    cd ..

The GCL runner will fail closed if README.md, config.yaml, or run_eval.py do not match
the locked Git blob identities.

## Install accelerator dependencies

    python -m pip install -r experiments/gsd-001/requirements.txt

## One-checkpoint smoke test

    python experiments/gsd-001/run_sweep.py \
      --upstream-dir ./GDsuite \
      --revision stage1-step20000-tokens42B \
      --families intuitive_answer \
      --n-seeds 1 \
      --max-eval 16 \
      --output-dir runs/gsd-smoke

On GPUs without BF16 support, the runner derives an FP16 copy of the locked upstream
config and records that precision override. Any transition discovered under the FP16
override must be replayed under BF16 before promotion.

## WP01 checkpoint sweep

    python experiments/gsd-001/run_sweep.py \
      --upstream-dir ./GDsuite \
      --auto-revisions \
      --n-seeds 2 \
      --max-eval 256 \
      --output-dir runs/olmo2-1b-early

WP01 does not close until at least 20 exact revisions complete.

Each revision emits:

- upstream/ — unchanged GDsuite outputs
- items.jsonl — GCL per-item soft margins
- summary.json — bootstrap state summaries
- manifest.json — exact source, model, dataset, precision, and environment identities

## WP02 transition catalogue

Run one family at a time:

    python experiments/gsd-001/analyze_transitions.py \
      runs/olmo2-1b-early \
      --family successive_answer \
      --output runs/olmo2-1b-early/successive-transitions.json

A catalogue entry is only CANDIDATE_TRANSITION.

## WP03 promotion rule

A candidate transition must survive:

1. soft-margin confidence rather than hard accuracy alone;
2. prompt-variant attack;
3. token-boundary audit;
4. stable-control check;
5. independent replay or flanking-checkpoint support.

Only then may it receive CONFIRMED_TRANSITION.

## Claim boundary

This tranche cannot establish a mechanism, capacity-allocation explanation, optimizer
effect, architecture effect, or post-training consequence. Negative results are retained.
