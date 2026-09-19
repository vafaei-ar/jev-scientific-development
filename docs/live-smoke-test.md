# Live JEV smoke test

The repository test suite does not require a real API key. Use the smoke command when you want to verify the current TypeSafe/JEV account and response contract.

## Run

With `TYPESAFE_API_KEY` configured in `.env`:

```bash
jev-smoke
```

The command sends only a synthetic randomized-trial sentence. It does not transmit manuscript, proposal, patient, or institutional data.

Expected shape:

```json
{
  "status": "ok",
  "model": "jev-...",
  "judgments": {
    "study_design": {
      "type": "choice",
      "value": "randomized_trial",
      "confidence": 0.0,
      "probabilities": {},
      "probability_margin": 0.0
    }
  },
  "usage": {}
}
```

The numeric values above are illustrative. Do not assert exact probabilities for future live calls because model versions and calibration can change.

## Verified live response

A live smoke test on September 18, 2026 returned:

- model: `jev-1.13.0`
- selected study design: `randomized_trial`
- confidence: `1.0`
- probability margin: `1.0`
- input tokens: `385`
- output tokens: `50`

The sanitized normalized response is stored in:

```text
tests/fixtures/jev_smoke_1_13_0.json
```

This fixture verifies the application-level response shape. It does not require or contain an API key.

## Why this is separate from CI

The normal pull-request CI is deterministic and secret-free. A live provider test depends on account access, rate limits, billing, and a network call, so it should remain an explicit smoke test rather than a required unit test.

If you later store `TYPESAFE_API_KEY` as a GitHub Actions secret, add a manual `workflow_dispatch` smoke workflow. Do not run live JEV calls automatically on every pull request.
