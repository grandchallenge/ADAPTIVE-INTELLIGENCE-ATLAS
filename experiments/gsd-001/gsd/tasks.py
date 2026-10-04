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


TASKS: tuple[TaskSpec, ...] = ()
