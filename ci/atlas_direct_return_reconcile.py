#!/usr/bin/env python3
"""Replay missed Atlas direct-editorial RESULT/1 events from durable comments."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "ci"))

from atlas_direct_return_projector import REPO, evaluate  # noqa: E402


def reconcile(issue: dict, fields: list[dict], comments: list[dict]) -> dict:
    if issue.get("state") != "open":
        return {"project": False, "reason": "not_open_issue"}

    ordered = sorted(
        comments,
        key=lambda c: (str(c.get("created_at") or ""), int(c.get("id") or 0)),
    )
    examined = 0
    rejected: list[dict] = []

    for comment in ordered:
        body = comment.get("body")
        if not isinstance(body, str) or not body.startswith("RESULT/1\n"):
            continue
        examined += 1
        result = evaluate(
            {
                "action": "created",
                "repository": {"full_name": REPO},
                "issue": issue,
                "comment": comment,
            },
            fields,
        )
        if result.get("project") is True:
            return {
                **result,
                "replayed": True,
                "examined_result_comments": examined,
            }
        rejected.append(
            {"comment_id": comment.get("id"), "reason": result.get("reason")}
        )

    return {
        "project": False,
        "reason": "no_conforming_result",
        "examined_result_comments": examined,
        "rejected": rejected,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue", type=Path, required=True)
    parser.add_argument("--issue-fields", type=Path, required=True)
    parser.add_argument("--comments", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    result = reconcile(
        json.loads(args.issue.read_text(encoding="utf-8")),
        json.loads(args.issue_fields.read_text(encoding="utf-8")),
        json.loads(args.comments.read_text(encoding="utf-8")),
    )
    args.output.write_text(json.dumps(result, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
