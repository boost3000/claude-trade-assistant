---
name: Always reply on Telegram when invoked from Telegram
description: Every time the user reaches you via the Telegram channel, send at least one Telegram reply confirming what you did — even when the actual work happens entirely in the terminal (e.g., /git-update, settings edits). The terminal transcript does NOT reach the Telegram user.
type: feedback
---

When a request arrives via the Telegram channel (any `<channel source="plugin:telegram:telegram" ...>` message), you MUST end the turn with at least one Telegram reply via `mcp__plugin_telegram_telegram__reply`. The Telegram sender cannot see the terminal transcript — silent local work looks like a dead bot.

**Why:** Without an explicit Telegram confirmation, the user on the phone has no way to know whether the request landed, succeeded, or silently failed. They're not at the terminal — the Telegram message is the only canonical output they can see.

**How to apply:**

- **Always reply on Telegram** when the invoking message came from Telegram, even when the entire task was completable locally without further Telegram interaction (`/git-update`, settings edits, memory writes, etc.).
- The reply must contain the **outcome** (commit hash, file path, success/failure, what changed) — not just an "ok". The user is away from the terminal, so the Telegram message has to stand alone.
- For long-running tasks: send an interim Telegram acknowledgement when starting ("Working on X, back shortly") so the user knows the bot received the request, then a second reply with the result. Use `edit_message` for progress on the same message or send a new reply at completion — `edit_message` doesn't push-notify, so the final result should be a new reply.
- For slash commands invoked through Telegram, the result of running the skill in terminal counts as "the work" but the **Telegram confirmation is mandatory**. Treat the terminal output as scratch space; the Telegram reply is the canonical user-visible output.
- If a tool errors or the task fails: report the failure on Telegram with the actual error, not a generic "command failed".

Linked: [[feedback_cite_sources_always]] (sources requirement applies to Telegram replies too).
