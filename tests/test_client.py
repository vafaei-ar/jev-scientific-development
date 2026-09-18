from __future__ import annotations

import httpx

from jev_research.config import JevConfig
from jev_research.jev.client import JevClient


def test_client_posts_documented_payload() -> None:
    captured: dict[str, object] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["url"] = str(request.url)
        captured["authorization"] = request.headers.get("Authorization")
        captured["body"] = request.content.decode("utf-8")
        return httpx.Response(200, json={"answers": {"decision": {"choice": "a"}}})

    http_client = httpx.Client(transport=httpx.MockTransport(handler))
    config = JevConfig(api_key="test-key", endpoint="https://example.test/v1/systemone")
    client = JevClient(config, http_client=http_client)

    result = client.evaluate(
        state="state",
        questions={
            "decision": {
                "type": "choice",
                "instructions": "Choose.",
                "criteria": {"a": None, "b": None},
            }
        },
    )

    assert result["answers"]["decision"]["choice"] == "a"
    assert captured["url"] == "https://example.test/v1/systemone"
    assert captured["authorization"] == "Bearer test-key"
    assert '"model":"jev-latest"' in str(captured["body"])
    assert '"state":"state"' in str(captured["body"])
