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

## Output handling

V0.1 returns the raw JEV provider result under `result`, plus tool and rubric metadata. Prefer the provider's probabilities/confidence when present. A winning choice with a close alternative is weak evidence for acting automatically.
