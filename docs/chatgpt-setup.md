# ChatGPT setup

## 1. Run the server

Install the project and set `TYPESAFE_API_KEY`, then run:

```bash
jev-mcp
```

The default Streamable HTTP endpoint is `http://127.0.0.1:8000/mcp`.

## 2. Make the MCP endpoint reachable

A local development endpoint is not directly reachable from a cloud-hosted client. Use an approved secure tunnel or deploy the MCP server behind HTTPS. Do not expose the API key to the browser or place it in the repository.

## 3. Add the MCP server to ChatGPT

Add the reachable MCP endpoint as a custom MCP app in the relevant ChatGPT workspace. Exact UI labels can change, so follow the current ChatGPT MCP/app setup flow.

## 4. Add the companion Skill

The companion skill lives in:

```text
skill/jev-scientific-development/
```

It tells ChatGPT when to call each MCP tool and how to interpret JEV output without turning JEV into a prose generator.

## Intended interaction

Example:

```text
Use JEV while we revise Aim 2. Challenge the aim-method alignment after each substantive revision.
```

The Skill should cause ChatGPT to:

1. understand Aim 2 in context;
2. draft or revise normally;
3. send only the relevant section to `evaluate_proposal`;
4. inspect the JEV distribution/confidence;
5. investigate material disagreement;
6. revise only when the scientific issue is real.
