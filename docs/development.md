# Development

## Python requirement

Python 3.10 or newer is required. CI tests the package on Python 3.10 and 3.12.

Before creating an environment:

```bash
python --version
```

If the active interpreter is older than 3.10, create a dedicated environment first. With Conda:

```bash
conda create -n jev-mcp python=3.11 -y
conda activate jev-mcp
```

## Local checks

```bash
python -m pip install --upgrade pip
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

The MCP returns a normalized application-level schema. Keep raw provider-response assumptions inside the provider adapter and normalization layer. Add sanitized fixtures when the live JEV response contract changes.

## Security

Never commit `.env`, API keys, manuscript data, PHI, or sponsor-confidential proposal material. Test with synthetic fixtures.
