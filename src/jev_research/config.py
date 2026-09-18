from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class JevConfig:
    api_key: str
    endpoint: str = "https://api.typesafe.ai/v1/systemone"
    model: str = "jev-latest"
    timeout_seconds: float = 30.0

    @classmethod
    def from_env(cls) -> "JevConfig":
        api_key = os.getenv("TYPESAFE_API_KEY") or os.getenv("JEV_API_KEY")
        if not api_key:
            raise RuntimeError(
                "Missing JEV API key. Set TYPESAFE_API_KEY or JEV_API_KEY."
            )
        return cls(
            api_key=api_key,
            endpoint=os.getenv(
                "JEV_ENDPOINT", "https://api.typesafe.ai/v1/systemone"
            ),
            model=os.getenv("JEV_MODEL", "jev-latest"),
            timeout_seconds=float(os.getenv("JEV_TIMEOUT_SECONDS", "30")),
        )
