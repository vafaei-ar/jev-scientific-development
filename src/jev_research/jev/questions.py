from __future__ import annotations

from collections.abc import Mapping
from typing import Any


def choice_question(
    instructions: str,
    criteria: Mapping[str, str | None],
) -> dict[str, Any]:
    """Build the documented JEV Choice question shape."""
    if not instructions.strip():
        raise ValueError("instructions must not be empty")
    if len(criteria) < 2:
        raise ValueError("Choice questions require at least two criteria")
    if len(criteria) > 255:
        raise ValueError("JEV Choice supports at most 255 criteria")
    return {
        "type": "choice",
        "instructions": instructions.strip(),
        "criteria": dict(criteria),
    }
