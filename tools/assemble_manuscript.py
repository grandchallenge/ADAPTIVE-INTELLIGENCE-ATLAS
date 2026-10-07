#!/usr/bin/env python3
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "governance" / "CHAPTER_LEDGER.yaml"


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def source_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return "UNKNOWN"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Assemble the canonical Atlas manuscript from CHAPTER_LEDGER order."
    )
    parser.add_argument("--output", default="build/atlas-manuscript.md")
    parser.add_argument("--manifest", default="build/atlas-manifest.json")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the assembly and write only to explicitly supplied paths.",
    )
    args = parser.parse_args()

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    chapters = ledger.get("chapters", [])
    if len(chapters) != ledger.get("chapter_count"):
        raise SystemExit("ledger chapter_count mismatch")

    paths = [c.get("manuscript_path") for c in chapters]
    if any(not p for p in paths):
        raise SystemExit("ledger chapter missing manuscript_path")
    if len(paths) != len(set(paths)):
        raise SystemExit("duplicate canonical manuscript path")
    if any(not p.startswith("manuscript/parts/") for p in paths):
        raise SystemExit("canonical manuscript path outside manuscript/parts")

    commit = source_commit()
    assembled = [
        "# A Mathematical Atlas of Adaptive Intelligence",
        "",
        "> Non-promotional working assembly generated from the protected Chapter Ledger.",
        f"> Source commit: `{commit}`",
        f"> Canonical chapters: {len(chapters)}",
        "",
    ]
    manifest_chapters = []

    for index, chapter in enumerate(chapters, start=1):
        rel = chapter["manuscript_path"]
        path = ROOT / rel
        if not path.is_file():
            raise SystemExit(f"missing canonical manuscript: {rel}")
        raw = path.read_bytes()
        text = raw.decode("utf-8").rstrip() + "\n"
        assembled.extend(
            [
                "",
                f"<!-- ATLAS_CHAPTER {index:02d} {chapter['id']} {rel} -->",
                "",
                text.rstrip(),
                "",
            ]
        )
        manifest_chapters.append(
            {
                "index": index,
                "id": chapter["id"],
                "part_id": chapter["part_id"],
                "status": chapter["status"],
                "path": rel,
                "git_blob_sha1": git_blob_sha1(raw),
            }
        )

    out_path = ROOT / args.output if not Path(args.output).is_absolute() else Path(args.output)
    manifest_path = ROOT / args.manifest if not Path(args.manifest).is_absolute() else Path(args.manifest)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    body = "\n".join(assembled).rstrip() + "\n"
    out_path.write_text(body, encoding="utf-8", newline="\n")
    manifest = {
        "schema_version": "1.0.0",
        "artifact_class": "non-promotional-working-assembly",
        "atlas_id": ledger.get("atlas_id"),
        "source_commit": commit,
        "chapter_count": len(chapters),
        "chapters": manifest_chapters,
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n"
    )

    marker_count = body.count("<!-- ATLAS_CHAPTER ")
    if marker_count != len(chapters):
        raise SystemExit(
            f"assembly marker count {marker_count} != chapter count {len(chapters)}"
        )

    print(
        f"OK: assembled {len(chapters)} canonical chapters from ledger order; "
        f"output={out_path}; manifest={manifest_path}; source_commit={commit}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
