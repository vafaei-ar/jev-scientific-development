# MCP tool reference

## `evaluate_paper`

Inputs:
- `text`: relevant manuscript or paper text.
- `focus`: optional focus such as `methods`, `results`, `discussion`, or `overall`.

Use to obtain structured judgments on methodological validity, claim-evidence alignment, reproducibility, and the dominant scientific risk.

Do not treat `dominant_scientific_risk` as a complete review. It identifies one priority domain.

## `evaluate_proposal`

Inputs:
- `text`: relevant proposal text.
- `section`: e.g. `specific aims`, `significance`, `innovation`, `approach`, or `overall`.

Use to obtain structured judgments on significance, aim-method alignment, feasibility, overclaim risk, and likely dominant reviewer concern.

## `audit_scientific_writing`

Input:
- `text`: scientific prose.

Use for clarity, specificity, scientific tone, and predefined formulaic LLM-style patterns.

Never report the result as an AI-authorship detector. Phrase it as writing-pattern risk.

## `challenge_claim`

Inputs:
- `claim`: the exact scientific claim.
- `evidence`: evidence presented as support.
- `context`: optional study design or surrounding context.

Use to judge support strength, strongest defensible inference type, alternative-explanation risk, and recommended claim action.

## Normalized output

All tools return the same application-level shape:

- `model`: resolved JEV model identifier when returned by the provider.
- `judgments`: one object per rubric question.
- `usage`: token usage when returned.
- `tool`, `rubric_version`, and `provider`: provenance metadata.

For a Choice judgment, expect:
- `value`: selected criterion.
- `confidence`: provider confidence when present.
- `probabilities`: all criterion probabilities.
- `probability_margin`: top probability minus second-highest probability.

A small probability margin means the leading option is weakly separated from its nearest alternative. Do not convert the margin into a universal pass/fail threshold.

For Score and Noul, the normalizer preserves the provider's value and probabilities in a consistent shape.

Set `JEV_INCLUDE_RAW=true` only for debugging the provider contract. Normal document workflows should use the normalized fields.
