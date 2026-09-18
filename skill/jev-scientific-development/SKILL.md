---
name: jev-scientific-development
description: Use JEV as an independent structured scientific evaluator while ChatGPT develops, reviews, or revises research manuscripts, grant proposals, Specific Aims, methods sections, scientific claims, and scientific prose. Trigger when the user asks to use JEV, wants a second-model scientific check, wants calibrated challenge of a paper/proposal/claim, or wants JEV integrated into document development. JEV must remain an evaluator rather than a prose writer; ChatGPT interprets JEV outputs and performs the actual writing, reasoning, citation work, and document editing.
---

# JEV Scientific Development

Use the JEV MCP server as a structured second evaluator inside a larger scientific workflow. Keep ChatGPT responsible for scientific reasoning, prose, revision, and final decisions.

## Core rule

Do not ask JEV to write reviewer comments or rewrite text. JEV returns typed judgments over predefined options. Use those judgments to identify disagreements, uncertainty, and issues worth investigating.

Do not describe a JEV judgment as proof, external validation, or factual verification. For factual claims, methods, citations, or current literature, use the appropriate evidence source and verify independently.

## Data boundary

Calling JEV transmits the supplied state to the configured external JEV provider.

- Send only the minimum relevant text.
- Do not send credentials, secrets, PHI, restricted identifiers, or data that the provider is not authorized to receive.
- If a document contains sensitive material, evaluate a de-identified excerpt when possible.
- Do not silently send an entire manuscript when a section is enough.

## Workflow

1. Understand the user's scientific goal and the local document context.
2. Perform normal scientific reasoning first. Do not outsource the whole problem to JEV.
3. Select the narrowest matching JEV MCP tool.
4. Send only the relevant text/state.
5. Inspect the returned choice distribution and confidence when available.
6. Treat close distributions or low confidence as unresolved, not as a verdict.
7. Compare JEV's judgment with the scientific reasoning already performed.
8. Investigate material disagreements using methods logic, source evidence, citations, code, or additional document context.
9. Revise only when the issue is scientifically justified.
10. If editing a DOCX, apply the appropriate document workflow after the scientific decision is made.

## Tool selection

Use `evaluate_paper` for manuscripts, article sections, methods/results/discussion text, or study-design critique. See `references/manuscript-workflow.md`.

Use `evaluate_proposal` for grants, Specific Aims, Significance, Innovation, Approach, protocols, or reviewer-readiness checks. See `references/proposal-workflow.md`.

Use `audit_scientific_writing` for clarity, specificity, scientific tone, and formulaic LLM-style patterns. This tool does not detect AI authorship. See `references/scientific-audit.md`.

Use `challenge_claim` for a single scientific claim when the user can supply or identify the supporting evidence and context.

Read `references/mcp-tools.md` when tool inputs/outputs or interpretation are unclear.

## Interpretation discipline

Prefer disagreement analysis over averaging models together.

If ChatGPT and JEV agree, continue only after checking whether the conclusion is supported by evidence and methods.

If ChatGPT and JEV disagree, identify the exact premise causing the disagreement. Check the source text, study design, analysis, or citation. Do not choose a side because one model appears more confident.

If JEV returns `insufficient_information`, obtain or inspect the missing context instead of forcing a judgment.

## Composition with other research workflows

Use citation/reference tooling for evidence verification rather than JEV alone. Use repository/code execution when a claim depends on actual analyses. Use document-editing tools for tracked changes and comments only after the scientific revision is determined.

For figures, do not use JEV as a substitute for inspecting source data, plotting code, or the actual figure.
