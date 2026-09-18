from __future__ import annotations

import os
from typing import Any

from mcp.server import MCPServer

from jev_research.config import JevConfig
from jev_research.jev.client import JevClient
from jev_research.rubrics import (
    RUBRIC_VERSION,
    claim_questions,
    paper_questions,
    proposal_questions,
    writing_questions,
)

mcp = MCPServer(
    "JEV Scientific Development",
    instructions=(
        "Use JEV for narrow structured scientific judgments. JEV is not a prose writer. "
        "Interpret the returned probabilities and choices in the host model, and do not treat "
        "a JEV judgment as proof or external evidence."
    ),
)


def _evaluate(
    *,
    tool_name: str,
    state: str | dict[str, Any],
    questions: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    with JevClient(JevConfig.from_env()) as client:
        result = client.evaluate(state=state, questions=questions)
    return {
        "tool": tool_name,
        "rubric_version": RUBRIC_VERSION,
        "provider": "TypeSafe/JEV",
        "result": result,
    }


@mcp.tool()
def evaluate_paper(text: str, focus: str = "overall") -> dict[str, Any]:
    """Evaluate a paper or manuscript section with a fixed scientific rubric."""
    if not text.strip():
        raise ValueError("text must not be empty")
    state = {"document_type": "scientific_paper", "focus": focus, "text": text}
    return _evaluate(
        tool_name="evaluate_paper",
        state=state,
        questions=paper_questions(focus),
    )


@mcp.tool()
def evaluate_proposal(text: str, section: str = "overall") -> dict[str, Any]:
    """Evaluate a grant or research proposal section with a fixed scientific rubric."""
    if not text.strip():
        raise ValueError("text must not be empty")
    state = {"document_type": "research_proposal", "section": section, "text": text}
    return _evaluate(
        tool_name="evaluate_proposal",
        state=state,
        questions=proposal_questions(section),
    )


@mcp.tool()
def audit_scientific_writing(text: str) -> dict[str, Any]:
    """Audit scientific prose for clarity, specificity, tone, and formulaic style.

    This tool does not detect or determine AI authorship.
    """
    if not text.strip():
        raise ValueError("text must not be empty")
    state = {"document_type": "scientific_writing", "text": text}
    return _evaluate(
        tool_name="audit_scientific_writing",
        state=state,
        questions=writing_questions(),
    )


@mcp.tool()
def challenge_claim(
    claim: str,
    evidence: str,
    context: str = "",
) -> dict[str, Any]:
    """Stress-test one scientific claim against the supplied evidence and context."""
    if not claim.strip():
        raise ValueError("claim must not be empty")
    if not evidence.strip():
        raise ValueError("evidence must not be empty")
    state = {"claim": claim, "evidence": evidence, "context": context}
    return _evaluate(
        tool_name="challenge_claim",
        state=state,
        questions=claim_questions(),
    )


def main() -> None:
    transport = os.getenv("MCP_TRANSPORT", "streamable-http")
    if transport == "stdio":
        mcp.run("stdio")
        return
    if transport != "streamable-http":
        raise RuntimeError("MCP_TRANSPORT must be 'stdio' or 'streamable-http'")

    host = os.getenv("MCP_HOST", "127.0.0.1")
    port = int(os.getenv("MCP_PORT", "8000"))
    mcp.run(
        "streamable-http",
        host=host,
        port=port,
        streamable_http_path="/mcp",
        json_response=True,
        stateless_http=True,
    )


if __name__ == "__main__":
    main()
