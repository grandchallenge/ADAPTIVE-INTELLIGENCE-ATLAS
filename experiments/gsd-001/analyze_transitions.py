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
    parser.add_argument("--family", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path(args.run_root)
    summaries: list[CheckpointSummary] = []
    for path in sorted(root.glob("*/summary.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        family = data.get("families", {}).get(args.family)
        if family is None:
            continue
        summaries.append(
            CheckpointSummary(
                revision=data["revision"],
                step=int(data["step"]),
                state=family["state"],
                mean_margin=float(family["mean_margin"]),
                ci_low=float(family["ci95"][0]),
                ci_high=float(family["ci95"][1]),
                n=int(family["n"]),
            )
        )

    result = {
        "family": args.family,
        "checkpoint_count": len(summaries),
        "transitions": detect_candidate_transitions(summaries),
        "claim_boundary": "candidate transitions only; WP03 validation required",
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
