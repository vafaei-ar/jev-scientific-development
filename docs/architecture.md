# Architecture

## Core principle

JEV is the evaluator, not the writer.

The host model, usually ChatGPT, owns document understanding, explanation, synthesis, and revision. The MCP server decomposes selected research judgments into predefined JEV Choice questions and returns the raw structured result to the host.

```text
user document
    |
    v
ChatGPT + JEV Skill
    |
    | selects narrow evaluation
    v
MCP tool
    |
    | state + typed questions
    v
JEV
    |
    | structured choices/probabilities/confidence
    v
ChatGPT
    |
    | interprets disagreement and uncertainty
    v
revision / recommendation / further verification
```

## Why not ask JEV to review a paper in one prompt?

JEV does not generate free-form prose. More importantly, the useful design pattern is to decompose a broad review into narrow judgments whose possible outputs are known in advance. This makes the result easier to compare across document versions and easier to combine with deterministic checks.

## V0.1 provider boundary

`src/jev_research/jev/client.py` is the only provider-specific HTTP adapter. The rest of the application builds provider-independent scientific rubrics.

The current adapter uses:

```text
POST https://api.typesafe.ai/v1/systemone
Authorization: Bearer <key>
```

with top-level `model`, `state`, and `questions`.

## Planned layers

1. V0.1: paper, proposal, writing, and claim judgments.
2. V0.2: exact Noul/Score support after production-schema validation; result normalization and uncertainty helpers.
3. V0.3: citation-evidence and cross-document consistency workflows.
4. V0.4: project memory and version comparison.
5. V0.5: optional GitHub/RunRelay execution hooks for code-backed analysis verification.

## Trust model

JEV outputs are model judgments. They are not evidence, peer review, or verification. The host should investigate important disagreements rather than automatically accepting the JEV result.
