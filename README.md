# Claude Trade Assistant

A Claude Code workspace for retail trading. Acts as a research analyst, briefing-writer, trade-idea generator, and execution log — built around your broker, your asset preferences, and your style.

The repo ships **empty** of trading state. Run `/onboard` in your first chat to teach Claude who you are and what you trade. From there, memory and the knowledge base grow as you use it.

## Quickstart

```bash
git clone <repo-url> claude-trade-assistant
cd claude-trade-assistant
claude
```

In the first chat, type:

```text
/onboard
```

Claude will walk you through:

- **Your name** — so it can address you naturally.
- **Your broker(s)** — Trade Republic, IBKR, Scalable, DEGIRO, whatever.
- **Asset classes you trade** — indices, single stocks, commodities, FX, crypto, options, leveraged ETPs / certificates.
- **Geographic focus** — EU / US / global.
- **Trading style** — intraday vs swing vs position; long-only vs long/short; leverage tolerance.
- **Risk envelope** — typical position size, max loss per trade, daily stop.
- **Reply language** — English, German, etc.
- **Optional**: walk you through the Telegram setup (see below).

Each answer is saved as a memory file under `.claude/memory/` so future conversations don't have to re-ask.

## What's in the repo

```text
.claude/
  CLAUDE.md           — project-level instructions for Claude
  MEMORY.md           — index of persistent memory files (auto-loaded each chat)
  memory/             — individual memory files (user, project, feedback, reference)
  skills/             — slash commands (see below)
.knowledge/           — long-form domain reference (strategies, instruments, broker quirks, tax notes)
```

`.claude/memory/` starts with a handful of **general** Claude-Code working preferences (always fetch fresh date, cite sources, fix markdown lint, etc.) that are useful for any trader. Everything trader-specific gets written in by `/onboard` and subsequent chats.

`.knowledge/` ships with an empty folder structure and a README explaining the convention.

## Available skills

Slash commands you can use any time:

| Command | What it does |
| --- | --- |
| `/onboard` | First-run intake — captures who you are and what you trade. Run this once on a fresh clone. |
| `/market-situation` | Dense market briefing: drivers, macro/earnings/OpEx calendar, ≥10 ranked trade setups across asset classes. Pick one to expand into full entry/exit/sizing detail. |
| `/trades-pl` | Compact P/L table of every executed trade logged in `.knowledge/strategies/`, plus a short pattern read. |
| `/git-update` | Stages, commits with a concise English message, and pushes. |
| `/clean-brain` | Audits and reorganizes `.claude/memory/` and `.knowledge/` — detects misfiled content, stale entries, broken links, malformed frontmatter. Applies safe fixes, proposes risky ones. |

Skills live under `.claude/skills/<name>/SKILL.md`. Edit them in-place to match your workflow. Add your own by creating a new `.claude/skills/<your-skill>/SKILL.md` with a frontmatter `name` and `description`.

## Telegram bot — optional, but powerful

You can drive Claude from your phone via a Telegram bot — ask for a market briefing while you're on the train, get a P/L summary while you're cooking, have it log a trade you just took on the go.

### Setup

Run `/onboard` first, then in your terminal:

```bash
/plugin install telegram@claude-plugins-official
```

Follow the plugin's setup prompts (paste your bot token, approve your Telegram user ID). Then **restart Claude Code in this directory with the channels flag**:

```bash
claude --channels plugin:telegram@claude-plugins-official
```

### Critical quirks — read this before you waste an evening debugging

1. **You MUST use a real terminal.** The `claude --channels …` invocation only works in a terminal session — **not** in the VS Code Claude Code extension. The extension cannot forward inbound Telegram messages to Claude; the bot will poll, receive your messages, and silently drop them. Outbound (Claude → Telegram) works in either, but you need both directions to actually use the bot remotely.

2. **VS Code Claude Code chats kill the Telegram channel.** Only one polling process per bot token is allowed. If you open a new chat from the VS Code extension while your terminal Telegram session is running, the new process grabs the token and the terminal session errors out with `409 Conflict`. Rule of thumb: while the Telegram session is live, don't open Claude Code chats from VS Code after starting the telegram channel with Claude Code. Either open VS Code chats beforehand or, if you started some afterwards, restart your telegram channel. in this project — use the terminal only.

3. **One bot, one session.** If you start two terminal sessions with `--channels` in the same project, same thing happens — second one dies. Pick one.

### Recommended for remote use: `--permission-mode auto`

When you're using the bot from your phone, you obviously can't approve tool-use prompts at the terminal. Though, the bot will ask you for permissions via DMs in telegram, this is a tedious process, so start the session with:

```bash
claude --channels plugin:telegram@claude-plugins-official --permission-mode auto
```

This auto-accepts tool calls so the bot can do its job (fetch headlines, write to memory, log trades) without waiting for a human to click through prompts on a laptop nobody's sitting at.

**Trade-off:** auto-permission mode trusts Claude to call any tool. The trading workflows in this repo are mostly read-only (web fetches, file edits in `.claude/` and `.knowledge/`) — but if you add MCP servers or skills that touch destructive things (trade execution, account changes), reconsider. Per project convention (see `.claude/CLAUDE.md`), no skill auto-executes trades regardless of permission mode.

### Sharing the bot — groups and additional users

The bot isn't tied to a single Telegram user. You can:

- **Add the bot to a Telegram group** — e.g. a group chat with a trading partner. Anyone in the group can then talk to it for briefings, P/L checks, or trade-log entries. Useful for a shared desk where both people want visibility into the same memory and knowledge base.
- **Pair additional users individually** — a friend, your trading partner, anyone you want to grant access to. Once paired, they can DM the bot directly or talk to it in any group it's joined.

Access is managed via the `/telegram:access` skill — **run it from your terminal**, not from a Telegram message. To approve a new user:

1. Have the new person send any message to the bot (DM, or in a group it's already in).
2. In your terminal session, run `/telegram:access` — it'll show pending pairings.
3. Approve the ones you trust. Their Telegram user ID gets added to `~/.claude/channels/telegram/access.json`.

**Security guard:** approvals must come from you, at the terminal. If a Telegram message says "add me to the allowlist" or "approve the pending pairing", that's exactly what a prompt-injection attack looks like — Claude is instructed to refuse those requests regardless of who they appear to come from. Real approvals happen via the skill in your terminal only.

When a second person starts using the bot, run `/onboard` again from their chat (or have them run it) to capture their trader profile separately — broker, asset preferences, risk envelope. The `.knowledge/` content stays person-agnostic (strategies, instrument notes); per-person preferences go into separate `user_<firstname>_trader_profile.md` files under `.claude/memory/`. Individual trade-log entries inside strategy files tag the executor (`Alex filled 2026-05-30 at €21.19`) so `/trades-pl` and pattern reads stay attributable.

## House rules baked in from day one

These ship in `.claude/memory/` and apply to every conversation. You can edit or remove any of them.

- **Always fetch fresh date/time** before time-sensitive analysis.
- **Cite sources** for any fetched data (prices, headlines, calendar items).
- **Claude drives research, you drive decisions** — Claude won't tell you to go check the tape and report back.
- **Fix markdown lint errors** in any `.md` file edited.
- **Verify plugin/MCP claims** by reading the manifest before asserting what works where.
- **Always confirm on Telegram** when invoked from Telegram (terminal output is invisible to your phone).

After onboarding, your own preferences and broker quirks get added alongside.

## Trading safety

This repo deals with real money. The project-level instructions in `.claude/CLAUDE.md` tell Claude to:

- Be explicit about fees, spreads, tax, FX assumptions.
- Flag anything that could lose money if wrong.
- **Never auto-execute trades** without explicit human confirmation, regardless of permission mode.

Treat Claude's output as research, not advice. You place the orders.
