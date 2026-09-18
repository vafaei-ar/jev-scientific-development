# Development

## Local checks

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python -m compileall -q src
```

## Add a new rubric

Keep provider-specific HTTP logic out of rubric code.

1. Define narrow scientific questions in `src/jev_research/rubrics.py`.
2. Use complete instructions. Do not rely on the question ID to carry meaning.
3. Prefer mutually distinguishable criteria.
4. Include an `insufficient_information` option when the source text may not support a judgment.
5. Expose the rubric through one high-level MCP tool.
6. Add tests that check the question schema.

## Result handling

V0.1 returns the raw provider response. Do not hard-code undocumented response fields in workflow logic yet. Once real account responses are captured as sanitized fixtures, add a normalization layer and regression tests.

## Security

Never commit `.env`, API keys, manuscript data, PHI, or sponsor-confidential proposal material. Test with synthetic fixtures.
