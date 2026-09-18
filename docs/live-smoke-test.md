# Live JEV smoke test

The repository test suite does not require a real API key. Use the smoke command when you want to verify the current TypeSafe/JEV account and response contract.

## Run

```bash
export TYPESAFE_API_KEY="..."
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

The numeric values above are illustrative. Do not assert exact probabilities in tests.

## Why this is separate from CI

The normal pull-request CI is deterministic and secret-free. A live provider test depends on account access, rate limits, billing, and a network call, so it should remain an explicit smoke test rather than a required unit test.

If you later store `TYPESAFE_API_KEY` as a GitHub Actions secret, add a manual `workflow_dispatch` smoke workflow. Do not run live JEV calls automatically on every pull request.
