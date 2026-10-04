from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TaskSpec:
    family: str
    name: str
    strategy: str
    k: int = 0
    joiner: str = "\n"
    n_seeds: int = 4


TASKS: tuple[TaskSpec, ...] = (
    TaskSpec("flipped_answer", "sst2", "balanced", 64, "\n\n"),
    TaskSpec("flipped_answer", "imdb", "balanced", 24, "\n\n"),
)
