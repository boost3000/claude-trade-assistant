# Memory index

Persistent memories for the claude-trade-assistant project. Each entry points to a file in `memory/`.

The repo ships with general Claude-Code working preferences only — no trader profile yet. Run `/onboard` to capture your trading style, broker(s), and asset preferences as additional memories.

- [Always fetch fresh date/time](memory/feedback_confirm_session_time.md) — run `date` via Bash at the start of any analytical turn; never assume time-of-day from context
- [Fix all markdown lint issues](memory/feedback_markdown_lint.md) — resolve every markdown linter error and warning in any `.md` file authored or edited
- [Claude drives research, user drives decisions](memory/feedback_research_workflow.md) — never tell the user to "check and report back"; fetch data yourself, give specific ping times with what you'll have ready
- [Always cite sources](memory/feedback_cite_sources_always.md) — every answer using fetched data ends with a compact source list (outlet + date), Telegram replies included
- [Verify plugin claims before asserting](memory/feedback_verify_plugin_claims.md) — read `.mcp.json` / `plugin.json` before claiming what a plugin/channel/flag does; trust empirical evidence over priors
- [Always reply on Telegram when invoked from Telegram](memory/feedback_telegram_always_reply.md) — even for tasks completed locally; the terminal transcript is invisible to the Telegram sender
