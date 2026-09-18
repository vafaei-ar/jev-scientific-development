import pytest

from jev_research.jev.normalize import (
    JevResponseError,
    normalize_system_one_response,
)


def test_normalizes_documented_system_one_shapes() -> None:
    raw = {
        "model": "jev-1.13.0",
        "answers": {
            "department": {
                "type": "choice",
                "choice": "billing",
                "confidence": 0.8,
                "probabilities": {
                    "billing": 0.87,
                    "sales": 0.0,
                    "technical": 0.13,
                },
            },
            "frustration": {
                "type": "score",
                "score": 1.04,
                "confidence": 0.94,
                "legend": {"0": "Calm", "1": "Frustrated", "2": "Very angry"},
                "probabilities": {"0": 0.0, "1": 0.96, "2": 0.04},
            },
            "is_urgent": {
                "type": "noul",
                "noul": 0.95,
            },
        },
        "usage": {"input_tokens": 426, "output_tokens": 73},
    }

    normalized = normalize_system_one_response(raw)

    assert normalized["model"] == "jev-1.13.0"
    assert normalized["judgments"]["department"]["value"] == "billing"
    assert normalized["judgments"]["department"]["probability_margin"] == 0.74
    assert normalized["judgments"]["frustration"]["value"] == 1.04
    assert normalized["judgments"]["is_urgent"]["probabilities"]["false"] == pytest.approx(0.05)
    assert normalized["usage"]["input_tokens"] == 426


def test_rejects_missing_answers() -> None:
    with pytest.raises(JevResponseError):
        normalize_system_one_response({"model": "jev-latest"})
