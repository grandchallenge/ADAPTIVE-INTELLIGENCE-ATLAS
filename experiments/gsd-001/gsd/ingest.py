from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .checkpoints import parse_checkpoint_revision
from .scoring import classify_margins


def iter_logprob_outputs(root: Path) -> Iterable[tuple[str, str, Path]]:
    """Yield family, task, path for GDsuite log-probability JSON outputs."""
    for path in sorted(root.rglob("*.json")):
        rel = path.relative_to(root)
        if len(rel.parts) < 2:
            continue
        if path.name.endswith("_summary.json") or path.name.endswith("_full.json"):
            continue
        family = rel.parts[0]
        task = "/".join(rel.with_suffix("").parts[1:])
        yield family, task, path


def ingest_checkpoint(upstream_root: Path, revision: str) -> tuple[list[dict], dict]:
    parsed = parse_checkpoint_revision(revision)
    step = parsed.step if parsed else -1
    rows_out: list[dict] = []

    for family, task, path in iter_logprob_outputs(upstream_root):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            continue
        for index, row in enumerate(data):
            required = {
                "correct_log_prob",
                "incorrect_log_prob",
                "correct_avg_prob",
                "incorrect_avg_prob",
            }
            if not required.issubset(row):
                continue
            rows_out.append({
                "revision": revision,
                "step": step,
                "family": family,
                "task": task,
                "row_index": index,
                "seed": row.get("seed"),
                "sum_margin": float(row["correct_log_prob"]) - float(row["incorrect_log_prob"]),
                "avg_token_prob_margin": float(row["correct_avg_prob"]) - float(row["incorrect_avg_prob"]),
                "upstream_hard_generalizes": float(row["correct_avg_prob"]) > float(row["incorrect_avg_prob"]),
            })

    summaries: dict[str, dict] = {}
    for family in sorted({r["family"] for r in rows_out}):
        margins = [r["sum_margin"] for r in rows_out if r["family"] == family]
        summaries[family] = classify_margins(margins)

    return rows_out, {
        "revision": revision,
        "step": step,
        "families": summaries,
        "source": "locked_upstream_gdsuite",
    }
