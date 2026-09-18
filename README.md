# JEV Scientific Development

A research-development bridge between ChatGPT and TypeSafe AI's JEV model.

JEV is used here as a fast, structured evaluator. It receives scientific text as state and answers predefined judgment questions with calibrated structured outputs. ChatGPT remains responsible for interpretation, scientific reasoning, writing, and document editing.

## Why this architecture

JEV is not a chat model and does not generate reviewer prose. Its strength is narrow, typed decisions that can be embedded inside a larger workflow. This repository exposes those decisions through an MCP server and pairs the server with a ChatGPT Skill that defines when and how to use them.

```text
ChatGPT
  |
  |  jev-scientific-development Skill
  v
JEV MCP server
  |
  +-- evaluate_paper
  +-- evaluate_proposal
  +-- audit_scientific_writing
  +-- challenge_claim
  |
  v
TypeSafe / JEV System One API
```

## V0.1 tools

- `evaluate_paper`: structured judgments on study validity, claim alignment, reproducibility, and the dominant scientific risk.
- `evaluate_proposal`: structured judgments on significance, aim-method alignment, feasibility, overclaim, and likely reviewer concern.
- `audit_scientific_writing`: structured judgments on clarity, specificity, scientific tone, formulaic wording, and rhetorical over-structuring.
- `challenge_claim`: stress-tests a scientific claim against supplied evidence and context.

The MCP returns normalized `judgments` so ChatGPT does not depend on vendor-specific response details.

## Setup

Python 3.11+ is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

Put the JEV key in `.env`:

```text
TYPESAFE_API_KEY=...
```

The application loads `.env` from the current working directory and never commits it.

Run the local MCP server:

```bash
jev-mcp
```

The default endpoint is `http://127.0.0.1:8000/mcp`.

### ChatGPT connection

V0.1 deliberately permits loopback binds only. Use OpenAI Secure MCP Tunnel to connect ChatGPT to the local/private server. Do not expose this server directly to the public internet.

See `docs/chatgpt-setup.md`.

## Live JEV smoke test

After configuring the key:

```bash
jev-smoke
```

This sends a synthetic study-design sentence only. It does not send any manuscript, proposal, patient, or institutional data.

See `docs/live-smoke-test.md`.

## JEV provider configuration

```text
POST https://api.typesafe.ai/v1/systemone
model: jev-latest
```

Environment variables:

```text
TYPESAFE_API_KEY=...
JEV_API_KEY=...                  # optional alias
JEV_ENDPOINT=https://api.typesafe.ai/v1/systemone
JEV_MODEL=jev-latest
JEV_TIMEOUT_SECONDS=30
JEV_INCLUDE_RAW=false
JEV_ENV_FILE=...                # optional .env path
MCP_TRANSPORT=streamable-http
MCP_HOST=127.0.0.1
MCP_PORT=8000
```

## Research-data boundary

Calling a JEV tool sends the supplied state to the configured JEV provider. Do not send credentials, restricted identifiers, PHI, or other data that the provider is not authorized to receive. Prefer the minimum text needed for the judgment.

For unpublished manuscripts and proposals, use the same institutional and sponsor data-handling rules that apply to any external AI service.

## Development

```bash
pytest
python -m compileall -q src
```

See `docs/architecture.md`, `docs/chatgpt-setup.md`, and `docs/development.md`.

## Status

V0.1 is an initial research scaffold. The next technical step after a successful live smoke test is to capture a sanitized real response fixture and then expand the rubric library.
