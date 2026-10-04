from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True, order=True)
class CheckpointRef:
    step: int
    revision: str
    tokens_b: float | None = None


def parse_checkpoint_revision(name: str) -> CheckpointRef | None:
    prefix = "stage1-step"
    if not name.startswith(prefix):
        return None

    tail = name[len(prefix):]
    step_text, separator, token_text = tail.partition("-tokens")
    if not step_text.isdigit():
        return None

    tokens_b = None
    if separator:
        if not token_text.endswith("B"):
            return None
        numeric = token_text[:-1]
        try:
            tokens_b = float(numeric)
        except ValueError:
            return None

    return CheckpointRef(
        step=int(step_text),
        revision=name,
        tokens_b=tokens_b,
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


def stride_refs(
    refs: list[CheckpointRef],
    stride: int,
    *,
    include_final: bool = True,
) -> list[CheckpointRef]:
    if stride < 1:
        raise ValueError("stride must be >= 1")
    if not refs:
        return []
    selected = refs[::stride]
    if include_final and selected[-1] != refs[-1]:
        selected = [*selected, refs[-1]]
    return selected
