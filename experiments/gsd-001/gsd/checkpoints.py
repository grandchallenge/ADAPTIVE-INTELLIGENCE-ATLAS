from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable

_REVISION_RE = re.compile(
    r"^stage1-step(?P<step>\\d+)(?:-tokens(?P<tokens>[0-9.]+)B)?$"
)


@dataclass(frozen=True, order=True)
class CheckpointRef:
    step: int
    revision: str
    tokens_b: float | None = None


def parse_checkpoint_revision(name: str) -> CheckpointRef | None:
    match = _REVISION_RE.match(name)
    if not match:
        return None
    tokens = match.group("tokens")
    return CheckpointRef(
        step=int(match.group("step")),
        revision=name,
        tokens_b=float(tokens) if tokens is not None else None,
    )


def normalize_refs(names: Iterable[str]) -> list[CheckpointRef]:
    parsed = [p for name in names if (p := parse_checkpoint_revision(name))]
    return sorted({p.revision: p for p in parsed}.values())


def list_hf_checkpoint_refs(repo_id: str) -> list[CheckpointRef]:
    from huggingface_hub import HfApi

    refs = HfApi().list_repo_refs(repo_id=repo_id, repo_type="model")
    names = [r.name for r in refs.branches] + [r.name for r in refs.tags]
    return normalize_refs(names)


def resolve_hf_model_sha(repo_id: str, revision: str) -> str:
    from huggingface_hub import HfApi

    info = HfApi().model_info(repo_id=repo_id, revision=revision)
    if not info.sha:
        raise RuntimeError(f"Hugging Face returned no SHA for {repo_id}@{revision}")
    return str(info.sha)


def resolve_hf_dataset_sha(repo_id: str, revision: str = "main") -> str:
    from huggingface_hub import HfApi

    info = HfApi().dataset_info(repo_id=repo_id, revision=revision)
    if not info.sha:
        raise RuntimeError(f"Hugging Face returned no SHA for dataset {repo_id}@{revision}")
    return str(info.sha)
