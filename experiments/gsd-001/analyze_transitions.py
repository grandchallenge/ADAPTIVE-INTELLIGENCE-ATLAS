from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from gsd.transitions import CheckpointSummary, detect_candidate_transitions


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_root")
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--task", help="Exact task key, e.g. flipped_answer/sst2")
    target.add_argument("--family", help="Descriptive family aggregate")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path(args.run_root)
    summaries: list[CheckpointSummary] = []
    section = "tasks" if args.task else "families"
    key = args.task or args.family

    for path in sorted(root.glob("*/summary.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        selected = data.get(section, {}).get(key)
        if selected is None:
            continue
        summaries.append(
            CheckpointSummary(
                revision=data["revision"],
                step=int(data["step"]),
                state=selected["state"],
                mean_margin=float(selected["mean_margin"]),
                ci_low=float(selected["ci95"][0]),
                ci_high=float(selected["ci95"][1]),
                n=int(selected["n"]),
            )
        )

    result = {
        "target_type": "task" if args.task else "family_aggregate",
        "target": key,
        "checkpoint_count": len(summaries),
        "transitions": detect_candidate_transitions(summaries),
        "claim_boundary": (
            "candidate transitions only; WP03 validation required. "
            "Task-level catalogues are primary."
        ),
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
