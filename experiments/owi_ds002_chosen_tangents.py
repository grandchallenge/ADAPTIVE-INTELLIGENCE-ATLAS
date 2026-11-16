#!/usr/bin/env python3
"""OWI-DS-002: charged, chosen-run tangent-query capability.

This object must be constructed from a ConditionalReplay belonging to ONE
episode. It cannot call a branch which was not already executed for the
requested examples. A derivative query is additional work, not a free reward
signal. This module does not claim to differentiate discrete branch choices.
"""
from __future__ import annotations

from dataclasses import dataclass
import time

import torch

from owi_ec005_conditional import ConditionalReplay


@dataclass(frozen=True)
class TangentReceipt:
    branch: int
    examples: int
    elapsed_seconds: float
    # A JVP may involve substantial internal differentiation work, and is NOT
    # accurately counted by the primal dense-MAC proxy.


class ChosenRunTangents:
    """Authorize JVPs only against the already selected, actually run suffixes.

    Index checks are per-example: selecting branch 0 for row 1 does not allow
    queries on branch 0 for row 2. Return only the tangent of the final scalar
    logit; do not expose the replayed hidden states or primals.
    """

    def __init__(self, replay: ConditionalReplay):
        self._replay = replay
        self.receipts: list[TangentReceipt] = []

    def query(self, branch: int, indices: torch.Tensor,
              direction: torch.Tensor) -> torch.Tensor:
        replay = self._replay
        if type(branch) is not int or branch not in (0, 1):
            raise ValueError("branch must be 0 or 1")
        if not isinstance(indices, torch.Tensor) or indices.dtype != torch.long:
            raise TypeError("indices must be a long tensor")
        if indices.ndim != 1 or indices.numel() == 0:
            raise ValueError("indices must be a nonempty vector")
        if indices.device.type != "cpu":
            raise ValueError("current CPU replay uses CPU indices")
        n = len(replay.batch.x)
        if bool(((indices < 0) | (indices >= n)).any()):
            raise IndexError("out-of-range example index")
        if torch.unique(indices).numel() != indices.numel():
            raise ValueError("duplicate example indices")
        if not bool(replay.ready[branch][indices].all()):
            raise PermissionError("unexecuted branch/example: no tangent capability")

        initial = replay.batch.checkpoints[branch][indices]
        if (not isinstance(direction, torch.Tensor) or
            direction.shape != initial.shape or
            direction.dtype != initial.dtype or
            direction.device != initial.device or
            not bool(torch.isfinite(direction).all())):
            raise ValueError("direction must be finite and checkpoint-shaped")
        prefix = replay.cfg.length - replay.cfg.suffix
        suffix = replay.batch.x[indices, prefix:, branch:branch + 1].detach()
        module = replay.core.branches[branch]
        head = replay.core.heads[branch]

        def chosen_logit(checkpoint: torch.Tensor) -> torch.Tensor:
            # Differentiation is with respect to the actual selected replay's
            # checkpoint, keeping the selected input suffix fixed.
            _, h = module(suffix, checkpoint.unsqueeze(0))
            return head(h.squeeze(0)).squeeze(1)

        start = time.perf_counter()
        with torch.enable_grad():
            # No training graph and no hidden primal is returned.
            _, tangent = torch.autograd.functional.jvp(
                chosen_logit, initial.detach(), direction.detach(),
                create_graph=False, strict=False)
        elapsed = time.perf_counter() - start
        self.receipts.append(TangentReceipt(
            branch=branch, examples=int(indices.numel()),
            elapsed_seconds=elapsed))
        return tangent.detach()

    def accounting(self) -> dict:
        return {
            "charged_jvp_queries": len(self.receipts),
            "charged_jvp_examples": sum(r.examples for r in self.receipts),
            "jvp_elapsed_seconds": sum(r.elapsed_seconds for r in self.receipts),
            "jvp_macs": None,
            "note": "JVP compute is additional, measured in time and examples; "
                    "no exact physical MAC/FLOP count has been established.",
        }
