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
    TaskSpec("flipped_answer", "rotten_tomatoes", "balanced", 64, "\n\n"),
    TaskSpec("flipped_answer", "poem_sentiment", "balanced", 64, "\n\n"),
    TaskSpec("flipped_answer", "yahoo_health_computers", "balanced", 64, "\n\n"),
    TaskSpec("flipped_answer", "yahoo_business_science", "balanced", 64, "\n\n"),
    TaskSpec("flipped_answer", "emotion", "balanced", 100, "\n\n"),
    TaskSpec("flipped_answer", "emotion_anger_joy", "balanced", 100, "\n\n"),
    TaskSpec("repetitive_answer", "code_tracing", "random", 8),
    TaskSpec("repetitive_answer", "letter_counting", "random", 4),
    TaskSpec("repetitive_answer", "logic", "random", 64),
    TaskSpec("repetitive_answer", "algebra/original", "random", 0),
    TaskSpec("repetitive_answer", "algebra/v2fmt", "random", 0),
    TaskSpec("repetitive_answer", "algebra/numbered", "random", 0),
    TaskSpec("repetitive_answer", "algebra/instruction", "random", 0),
    TaskSpec("successive_answer", "number_words", "ordered", 10),
    TaskSpec("successive_answer", "letters", "ordered", 10),
    TaskSpec("successive_answer", "arithmetic", "ordered", 32),
    TaskSpec("successive_answer", "even", "ordered", 32),
    TaskSpec("truthy_answer", "surprising_truth", "random", 8),
    TaskSpec("truthy_answer", "common_misconception", "random", 100),
    TaskSpec("intuitive_answer", "crt", "none", 0, "\n", 1),
)
