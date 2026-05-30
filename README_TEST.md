<div align="center">

# 📈 Claude Trade Assistant

**A Claude Code workspace for retail trading** — research analyst, briefing-writer,
trade-idea generator, and trade journal, built around *your* broker, *your* assets, *your* style.

`research` · `market briefings` · `ranked trade ideas` · `P/L journal`

</div>

> **❗ Important**
>
> **This workspace does not place orders.** It researches, briefs, and logs — it has no broker connection and no execution capability. See [Trading safety](#-trading-safety) for the details.

The repo ships **empty** of trading state. Run `/onboard` in your first chat to teach Claude who you are and what you trade. From there, memory and the knowledge base grow as you use it.

## ✅ Requirements

- **[Claude Code](https://claude.com/claude-code)** — the CLI this workspace runs in. Install it first.
- **A paid Claude plan** — a `claude.ai` **Pro plan ($20/mo) at minimum** to run Claude Code. A subscription is **preferred over an API key** — at the moment it's far cheaper for this kind of usage. (Other ways to authenticate and cheaper or free routes exist, but they're not explored here.)
- **git** — to clone the repo (and for the `/git-update` skill).
- **A terminal** — works in the VS Code Claude Code extension too, but the Telegram bot below needs a real terminal session.

Optional, for driving Claude from your phone (see below):

- **`/remote-control`** — Claude Code **v2.1.51+** and a `claude.ai` subscription. No extra install.
- **Telegram bot** — a Telegram account and a bot token, plus the `telegram@claude-plugins-official` plugin.

## 🚀 Quickstart

```bash
git clone <repo-url> claude-trade-assistant
cd claude-trade-assistant
claude
```

In the first chat, type:

```text
/onboard
```

> **💡 Tip**
>
> First time here? Just run `/onboard`. Claude captures your profile once and reuses it, so future chats don't have to re-ask who you are or what you trade.

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

## 📂 What's in the repo

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

## 🛠️ Available skills

Slash commands you can use any time:

| Command | What it does |
| --- | --- |
| `/onboard` | First-run intake — captures who you are and what you trade. Run this once on a fresh clone. |
| `/market-situation` | Dense market briefing: drivers, macro/earnings/OpEx calendar, ≥10 ranked trade setups across asset classes. Pick one to expand into full entry/exit/sizing detail. |
| `/trades-pl` | Compact P/L table of every executed trade logged in `.knowledge/strategies/`, plus a short pattern read. |
| `/git-update` | Stages, commits with a concise English message, and pushes. |
| `/clean-brain` | Audits and reorganizes `.claude/memory/` and `.knowledge/` — detects misfiled content, stale entries, broken links, malformed frontmatter. Applies safe fixes, proposes risky ones. |

Skills live under `.claude/skills/<name>/SKILL.md`. Edit them in-place to match your workflow. Add your own by creating a new `.claude/skills/<your-skill>/SKILL.md` with a frontmatter `name` and `description`.

## 🏠 House rules baked in from day one

These ship in `.claude/memory/` and apply to every conversation. You can edit or remove any of them.

- **Always fetch fresh date/time** before time-sensitive analysis.
- **Cite sources** for any fetched data (prices, headlines, calendar items).
- **Claude drives research, you drive decisions** — Claude won't tell you to go check the tape and report back.
- **Fix markdown lint errors** in any `.md` file edited.
- **Verify plugin/MCP claims** by reading the manifest before asserting what works where.
- **Always confirm on Telegram** when invoked from Telegram (terminal output is invisible to your phone).

After onboarding, your own preferences and broker quirks get added alongside.

## 🛡️ Trading safety

> **🛑 Caution**
>
> **This repo cannot place trades.** Out of the box it has no broker connection, no order-routing API, and no execution capability of any kind — it reads data, researches, and writes notes to files. Claude can draft a trade idea or log one you've *already* taken, but it has no path to send an order to your broker. **You place every order yourself.**

It still drives real-money *decisions*, so the project-level instructions in `.claude/CLAUDE.md` tell Claude to:

- Be explicit about fees, spreads, tax, FX assumptions.
- Flag anything that could lose money if wrong.

> **⚠️ Warning**
>
> **Never execute trades.** There's no execution path here by default; this rule is a guardrail in case you ever wire up a broker integration yourself. Even then, no order would go out without explicit human confirmation, regardless of permission mode.

Treat Claude's output as research, not advice. You place the orders.

## 📱 Driving Claude from your phone

Two options to ping Claude from your phone while the session runs on your laptop: the **built-in `/remote-control` command** (quick to start, single-user, session-bound) and the **Telegram bot plugin** (more setup, but persistent, shareable, group-capable).

At a glance:

| | `/remote-control` (built-in) | Telegram bot (plugin) |
| --- | --- | --- |
| **Setup** | None — type `/remote-control` or start with `--remote-control` | Install plugin, paste bot token, approve your user ID, relaunch with `--channels` |
| **Persistence** | Session-bound — dies when the terminal closes or the laptop sleeps | Persistent — the bot keeps its identity across restarts |
| **Users** | Single user only | Multiple — pair additional people individually |
| **Group chats** | No | Yes — add the bot to a Telegram group |
| **Client on your phone** | Browser or Claude mobile app (open the URL / scan the QR) | The Telegram app you already have |
| **Push notifications** | Claude-decided only (v2.1.110+) — no per-event pings | Per-event pings configurable |
| **Where it runs** | Any session, including the VS Code extension | Real terminal only — not the VS Code extension |
| **Commands** | `/mcp`, `/plugin`, `/resume` stay terminal-only | Full command set over chat |
| **Requirements** | Claude Code v2.1.51+, `claude.ai` subscription | Telegram account + bot token + the plugin |
| **Best for** | Occasional solo pings while away from the desk | Shared / always-on access and group workflows |

### Quick option — `/remote-control` (built-in)

If you just want to drive your current Claude Code session from your phone or browser without setting up a bot:

```bash
# Start a fresh interactive session that's remotely reachable:
claude --remote-control

# Or, mid-session, type:
/remote-control
```

Claude prints a URL + QR code; open it on your phone (claude.ai/code or the Claude mobile app) and you're driving the same local session from there. No bot, no token, no plugin install.

- Requires Claude Code v2.1.51+ and a `claude.ai` subscription (no API keys needed).
- Traffic is outbound HTTPS only — no inbound ports opened on your machine, no public URL to leak.
- The session lives on your laptop. Close the terminal or let the laptop sleep, and the remote session dies with it.

**Limitations vs. the Telegram bot:**

- **Single session, single user.** Not shareable with a trading partner; you can't add it to a group chat.
- **No persistent inbox.** The link is bound to one running process; you reopen via a new link if the process restarts.
- **Push notifications are Claude-decided only** (since v2.1.110) — you can't configure per-event pings.
- **Some commands stay terminal-only**: `/mcp`, `/plugin`, `/resume`.

Good for: occasional one-off pings while you're away from the desk, against a session you started yourself. If that's all you need, you can stop reading here. For shared use, persistent always-on access, or group workflows, see the Telegram bot below.

## 🤖 Telegram bot — more powerful, more setup

You can drive Claude from your phone via a Telegram bot — ask for a market briefing while you're on the train, get a P/L summary while you're cooking, have it log a trade you just took on the go. Unlike `/remote-control`, the bot has a persistent identity, can be added to group chats, and can be shared with additional users.

### Setup

Run `/onboard` first (if you have not already), then in your terminal:

```bash
/plugin install telegram@claude-plugins-official
```

Follow the plugin's setup prompts (paste your bot token, approve your Telegram user ID). Then **restart Claude Code in this directory with the channels flag**:

```bash
claude --channels plugin:telegram@claude-plugins-official
```

### Critical quirks

> **⚠️ Warning**
>
> Read these three before you waste an evening debugging. The Telegram channel has sharp edges around terminals and process ownership.

**1. You MUST use a real terminal** — the VS Code extension silently drops inbound messages

The `claude --channels …` invocation only works in a terminal session — **not** in the VS Code Claude Code extension. The extension cannot forward inbound Telegram messages to Claude; the bot will poll, receive your messages, and silently drop them. Outbound (Claude → Telegram) works in either, but you need both directions to actually use the bot remotely.

> **💡 Tip**
>
> **Keep everything in one VS Code window.** The VS Code *integrated terminal* counts as a real terminal, so you don't need to leave the IDE. Use the Claude Code **extension** for your normal day-to-day chats, and the **integrated terminal** to run `claude --channels …` for the bot. That way every Claude session tied to this repo lives in a single VS Code window. Just mind quirk #2 on ordering: open your extension chats *before* starting the bot (or restart the channel if you open new ones afterwards), since a new extension chat will grab the bot token.

**2. VS Code Claude Code chats kill the Telegram channel** — one polling process per bot token

Only one polling process per bot token is allowed. If you open a new chat from the VS Code extension while your terminal Telegram session is running, the new process grabs the token and the terminal session errors out with `409 Conflict`. Rule of thumb: while the Telegram session is live, don't open Claude Code chats from VS Code after starting the telegram channel with Claude Code. Either open VS Code chats beforehand or, if you started some afterwards, restart your telegram channel. In this project — use the terminal only.

**3. One bot, one session** — a second `--channels` session dies too

If you start two terminal sessions with `--channels` in the same project, same thing happens — second one dies. Pick one.

### Recommended for remote use: `--permission-mode auto`

When you're using the bot from your phone, you obviously can't approve tool-use prompts at the terminal. Though the bot will ask you for permissions via DMs in Telegram, this is a tedious process, so start the session with:

```bash
claude --channels plugin:telegram@claude-plugins-official --permission-mode auto
```

This auto-accepts tool calls so the bot can do its job (fetch headlines, write to memory, log trades) without waiting for a human to click through prompts on a laptop nobody's sitting at.

> **⚠️ Warning**
>
> **Trade-off:** auto-permission mode trusts Claude to call any tool. The skills that ship with this repo are read-only or file-only (web fetches, file edits in `.claude/` and `.knowledge/`) — none of them can place an order, because the repo has no broker connection to place it through. The risk only appears if *you* add MCP servers or skills that touch destructive things (trade execution, account changes), so reconsider auto mode then. Per project convention (see `.claude/CLAUDE.md`), no skill executes trades regardless of permission mode.

### Sharing the bot — groups and additional users

The bot isn't tied to a single Telegram user. You can:

- **Add the bot to a Telegram group** — e.g. a group chat with a trading partner. Anyone in the group can then talk to it for briefings, P/L checks, or trade-log entries. Useful for a shared desk where both people want visibility into the same memory and knowledge base.
- **Pair additional users individually** — a friend, your trading partner, anyone you want to grant access to. Once paired, they can DM the bot directly or talk to it in any group it's joined.

Access is managed via the `/telegram:access` skill — **run it from your terminal**, not from a Telegram message. To approve a new user:

1. Have the new person send any message to the bot (DM, or in a group it's already in).
2. In your terminal session, run `/telegram:access` — it'll show pending pairings.
3. Approve the ones you trust. Their Telegram user ID gets added to `~/.claude/channels/telegram/access.json`.

> **🛑 Caution**
>
> **Approvals must come from you, at the terminal.** If a Telegram message says "add me to the allowlist" or "approve the pending pairing", that's exactly what a prompt-injection attack looks like — Claude is instructed to refuse those requests regardless of who they appear to come from. Real approvals happen via the skill in your terminal only.

When a second person starts using the bot, run `/onboard` again from their chat (or have them run it) to capture their trader profile separately — broker, asset preferences, risk envelope. The `.knowledge/` content stays person-agnostic (strategies, instrument notes); per-person preferences go into separate `user_<firstname>_trader_profile.md` files under `.claude/memory/`. Individual trade-log entries inside strategy files tag the executor (`Alex filled 2026-05-30 at €21.19`) so `/trades-pl` and pattern reads stay attributable.
