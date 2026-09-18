from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import httpx

from jev_research.config import JevConfig


class JevAPIError(RuntimeError):
    """Raised when the JEV provider returns an invalid or unsuccessful response."""


class JevClient:
    def __init__(
        self,
        config: JevConfig,
        *,
        http_client: httpx.Client | None = None,
    ) -> None:
        self.config = config
        self._owns_client = http_client is None
        self._http = http_client or httpx.Client(timeout=config.timeout_seconds)

    def close(self) -> None:
        if self._owns_client:
            self._http.close()

    def __enter__(self) -> "JevClient":
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        self.close()

    def evaluate(
        self,
        *,
        state: str | dict[str, Any] | list[Any],
        questions: Mapping[str, Mapping[str, Any]],
    ) -> dict[str, Any]:
        if not questions:
            raise ValueError("At least one JEV question is required")

        payload = {
            "model": self.config.model,
            "state": state,
            "questions": dict(questions),
        }
        try:
            response = self._http.post(
                self.config.endpoint,
                headers={
                    "Authorization": f"Bearer {self.config.api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
            )
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise JevAPIError(f"JEV request failed: {exc}") from exc

        try:
            body = response.json()
        except ValueError as exc:
            raise JevAPIError("JEV returned non-JSON content") from exc
        if not isinstance(body, dict):
            raise JevAPIError("JEV returned an unexpected response shape")
        return body
