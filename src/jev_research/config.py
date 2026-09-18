from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


def load_environment() -> None:
    """Load a local .env file without overriding already-exported variables."""
    configured = os.getenv("JEV_ENV_FILE")
    dotenv_path = Path(configured).expanduser() if configured else Path.cwd() / ".env"
    if dotenv_path.exists():
        load_dotenv(dotenv_path=dotenv_path, override=False)


@dataclass(frozen=True)
class JevConfig:
    api_key: str
    endpoint: str = "https://api.typesafe.ai/v1/systemone"
    model: str = "jev-latest"
    timeout_seconds: float = 30.0

    @classmethod
    def from_env(cls) -> "JevConfig":
        load_environment()
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
