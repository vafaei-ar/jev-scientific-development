# ChatGPT setup

## 1. Run the server locally

Install the project, copy `.env.example` to `.env`, add `TYPESAFE_API_KEY`, then run:

```bash
jev-mcp
```

The process loads `.env` from the current working directory without overriding variables you already exported.

The default endpoint is:

```text
http://127.0.0.1:8000/mcp
```

V0.1 intentionally refuses non-loopback binds. Do not change `MCP_HOST` to `0.0.0.0` or expose this endpoint directly to the internet.

## 2. Connect ChatGPT with Secure MCP Tunnel

ChatGPT cannot connect directly to a local MCP server. For a server running on your laptop or private network, use OpenAI Secure MCP Tunnel so the endpoint remains private rather than publicly exposed.

Keep the local MCP server bound to loopback and point the tunnel at:

```text
http://127.0.0.1:8000/mcp
```

Follow the current ChatGPT workspace setup flow for Secure MCP Tunnel and custom MCP apps.

## 3. Create the custom app

In the applicable ChatGPT workspace:

1. Enable developer mode.
2. Create a custom MCP app.
3. Use the Secure MCP Tunnel endpoint.
4. Scan the MCP tools.
5. Keep the app private/draft until the tools and data boundary are verified.

Exact UI labels can change, so use the current ChatGPT MCP/app setup screens.

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
4. inspect the normalized JEV distribution/confidence;
5. investigate material disagreement;
6. revise only when the scientific issue is real.

## Future remote deployment

If this project is later deployed as a public remote MCP service, add standards-compliant OAuth 2.1 resource-server authentication before enabling a public bind. The MCP Python SDK supports bearer-token verification and protected-resource metadata. Do not deploy the current V0.1 server directly on a public interface.
