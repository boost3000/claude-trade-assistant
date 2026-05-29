---
name: verify-plugin-claims
description: Don't assert what Claude Code plugins/channels/flags can or can't do without checking the plugin manifest first.
type: feedback
---

When the user asks "does X work with the VS Code extension / can I use Y flag / does this plugin support Z" — check the plugin's `.mcp.json`, `.claude-plugin/plugin.json`, and `~/.claude/plugins/installed_plugins.json` BEFORE answering. Don't lean on training-data knowledge of "channels" vs "plugins" vs "flags" — the system evolves and priors are unreliable.

**Why:** Past failure: assistant confidently asserted a plugin needed a specific CLI flag and didn't work in VS Code, both wrong. A 5-minute file-check would have prevented the mistake. Trust manifests and running processes over recalled defaults.

**How to apply:**

- When asked about plugin/channel/MCP behavior: read `.mcp.json` and `plugin.json` first.
- When asked "does it work in VS Code": check whether there's a real launcher dependency, or whether MCP-server auto-load handles it.
- If empirical evidence (running processes, `ps` output) contradicts your prior belief, trust the evidence and update — don't insist on the prior.
