from __future__ import annotations

from typing import Any


class JevResponseError(ValueError):
    """Raised when a System One response cannot be normalized safely."""


def _numeric_probabilities(value: Any) -> dict[str, float]:
    if not isinstance(value, dict):
        return {}
    output: dict[str, float] = {}
    for key, probability in value.items():
        if isinstance(probability, (int, float)):
            output[str(key)] = float(probability)
    return output


def _choice_margin(probabilities: dict[str, float]) -> float | None:
    if len(probabilities) < 2:
        return None
    ordered = sorted(probabilities.values(), reverse=True)
    return round(ordered[0] - ordered[1], 6)


def _normalize_answer(answer: Any) -> dict[str, Any]:
    if not isinstance(answer, dict):
        raise JevResponseError("Each JEV answer must be an object")

    answer_type = answer.get("type")
    normalized: dict[str, Any] = {"type": answer_type or "unknown"}

    if answer_type == "choice":
        probabilities = _numeric_probabilities(answer.get("probabilities"))
        normalized["value"] = answer.get("choice")
        if "confidence" in answer:
            normalized["confidence"] = answer.get("confidence")
        normalized["probabilities"] = probabilities
        margin = _choice_margin(probabilities)
        if margin is not None:
            normalized["probability_margin"] = margin
        return normalized

    if answer_type == "score":
        normalized["value"] = answer.get("score")
        if "confidence" in answer:
            normalized["confidence"] = answer.get("confidence")
        normalized["probabilities"] = _numeric_probabilities(answer.get("probabilities"))
        if isinstance(answer.get("legend"), dict):
            normalized["legend"] = {
                str(key): value for key, value in answer["legend"].items()
            }
        return normalized

    if answer_type == "noul":
        value = answer.get("noul")
        normalized["value"] = value
        if isinstance(value, (int, float)):
            p_true = float(value)
            normalized["probabilities"] = {
                "true": p_true,
                "false": round(1.0 - p_true, 6),
            }
        if "confidence" in answer:
            normalized["confidence"] = answer.get("confidence")
        return normalized

    normalized["raw"] = answer
    return normalized


def normalize_system_one_response(body: dict[str, Any]) -> dict[str, Any]:
    """Normalize the documented TypeSafe System One response into a stable app schema."""
    if not isinstance(body, dict):
        raise JevResponseError("JEV response must be an object")

    answers = body.get("answers")
    if not isinstance(answers, dict):
        raise JevResponseError("JEV response is missing an answers object")

    normalized_answers = {
        str(question_id): _normalize_answer(answer)
        for question_id, answer in answers.items()
    }

    output: dict[str, Any] = {
        "model": body.get("model"),
        "judgments": normalized_answers,
    }

    usage = body.get("usage")
    if isinstance(usage, dict):
        output["usage"] = {
            key: value
            for key, value in usage.items()
            if isinstance(value, (int, float))
        }

    return output
