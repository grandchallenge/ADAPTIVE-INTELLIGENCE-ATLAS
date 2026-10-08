#!/usr/bin/env python3
"""Untrusted Atlas RESULT/1 -> operational queue projection decision only.

No result content is adjudicated here. Protected claim/editorial/release
authority cannot be established by this projector.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

REPO = "grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS"
CAMPAIGN = "ATLAS-EDITORIAL-REVIEW-001"
MARKER = "RESULT/1\n"
DIRECT_LABEL = "gcl-pickup:direct-editorial"
SHA = re.compile(r"^[0-9a-f]{40}$")
LOGIN = re.compile(r"^([A-Za-z0-9][A-Za-z0-9-]{0,38})(?:\b|$)")
ASSIGNMENT = re.compile(r"^ASSIGNMENT_ID:[ \t]*([A-Z0-9-]+)[ \t]*$", re.M)
TITLE_PREFIX = re.compile(r"^([A-Z][A-Z0-9_-]+)\s+—\s+")
RETURN_FIELD = re.compile(r"^([a-z_]+):[ \t]*(.*)$", re.M)
STATES = {"completed", "partial", "blocked"}

def evaluate(event: dict, fields: list[dict]) -> dict:
    def skip(reason: str) -> dict:
        return {"project": False, "reason": reason}
    issue = event.get("issue") or {}
    actor = (event.get("comment") or {}).get("user") or {}
    comment = event.get("comment") or {}
    repo = (event.get("repository") or {}).get("full_name")
    if repo != REPO:
        return skip("wrong_repository")
    if event.get("action") != "created":
        return skip("not_created")
    if "pull_request" in issue or issue.get("state") != "open":
        return skip("not_open_issue")
    if DIRECT_LABEL not in {x.get("name") for x in issue.get("labels", [])}:
        return skip("not_direct_editorial")
    body = comment.get("body") or ""
    if not body.startswith(MARKER):
        return skip("not_result")
    if not comment.get("id") or not actor.get("login"):
        return skip("missing_authenticated_comment")
    field_map = {}
    for x in fields:
        value = x.get("single_select_option") or {}
        field_map[x.get("issue_field_name")] = value.get("name", x.get("value"))
    if field_map.get("GCL Campaign") != CAMPAIGN:
        return skip("not_atlas_campaign")
    if field_map.get("GCL State") == "RETURNED":
        return skip("already_returned")
    if field_map.get("GCL State") != "AVAILABLE":
        return skip("state_not_available")
    matches = dict(RETURN_FIELD.findall(body))
    if any(k not in matches for k in ("assignment_id", "status")):
        return skip("missing_required_return_field")
    if not (matches.get("github_actor") or matches.get("reviewer_identity")):
        return skip("missing_actor_attribution")
    if not (matches.get("reviewed_head") or matches.get("input_head")):
        return skip("missing_source_head")
    issue_body = issue.get("body") or ""
    source = ASSIGNMENT.search(issue_body)
    if source:
        required_assignment = source.group(1)
    else:
        prefix = TITLE_PREFIX.search(issue.get("title") or "")
        if not prefix:
            return skip("unknown_assignment")
        required_assignment = prefix.group(1)
    if matches["assignment_id"].strip() != required_assignment:
        return skip("wrong_assignment")
    # Bind the comment to the authenticated GitHub transport account.
    # This is NOT the test for independence of the review agent role.
    declared_actor = (matches.get("github_actor") or
                      matches.get("reviewer_identity") or "")
    claimed = LOGIN.match(declared_actor.strip())
    if not claimed or claimed.group(1).casefold() != actor["login"].casefold():
        return skip("authenticated_actor_mismatch")
    head = (matches.get("reviewed_head") or
            matches.get("input_head") or "").strip()
    if not SHA.fullmatch(head):
        return skip("invalid_source_head")
    status = matches["status"].strip()
    if status not in STATES:
        return skip("invalid_result_status")
    # Projection is a receipt, NOT a verdict; no inference of independent review.
    return {
        "project": True,
        "issue_number": issue["number"],
        "comment_id": comment["id"],
        "authenticated_actor": actor["login"],
        "agent_role": matches.get("agent_role") or "UNDECLARED",
        "agent_run_id": matches.get("agent_run_id") or "UNRECORDED",
        "assignment": required_assignment,
        "input_head": head,
        "self_reported_status": status,
        "state_to_write": "RETURNED",
        "editorial_accepted": False,
        "independent_review_approved": False,
    }

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", type=Path, required=True)
    parser.add_argument("--issue-fields", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = evaluate(json.loads(args.event.read_text()), json.loads(args.issue_fields.read_text()))
    args.output.write_text(json.dumps(result, sort_keys=True) + "\n")

if __name__ == "__main__":
    main()
