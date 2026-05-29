---
name: onboard
description: First-run intake for a fresh clone of claude-trade-assistant. Captures the user's name, broker(s), traded asset classes, geographic focus, trading style, risk envelope, and reply-language preference; saves each as a memory file; optionally walks them through Telegram bot setup. Use when the user invokes `/onboard`, when `.claude/memory/` has no `user_*` profile file, or when the user asks how to get started.
---

# /onboard — first-run intake

Goal: turn a fresh clone of this repo into a configured workspace that knows who the user is and what they trade. By the end, `.claude/memory/` should have a `user_<name>_trader_profile.md`, `project_current_thesis.md` (if they share one), and updated `MEMORY.md`. Optionally, the user has the Telegram bot installed and running.

## Process

1. **Check current state.** Read `.claude/memory/` to see if any `user_*_trader_profile.md` already exists. If yes, ask whether the user wants to **update** the existing profile, **add a second person** (this repo supports multiple traders sharing a workspace), or **cancel**. If no profile exists, proceed with full onboarding.

2. **Greet briefly.** One sentence. Don't lecture. Something like: "Welcome. I'll ask a handful of questions to set up your trader profile, then offer to walk you through the Telegram bot. Each answer gets saved as memory so I won't ask again."

3. **Run the intake.** Ask the questions below **one at a time** (or in tight groups of 2–3 where they naturally cluster), wait for an answer, save it to the right memory file, then move on. Don't dump all questions in one block — the user will skim and undershoot.

   Use the `AskUserQuestion` tool when the answer space is small and pickable (asset classes, style, language). Use plain text questions when the answer is genuinely freeform (name, broker quirks, risk envelope).

   **Group A — identity (plain text):**
   - First name (so I can address you naturally).
   - Reply language preference (English, German, other) — use AskUserQuestion with the main options + Other.

   **Group B — broker (plain text + follow-ups):**
   - Which broker(s) do you trade with? (Trade Republic, IBKR, Scalable, DEGIRO, Comdirect, Robinhood, multiple, etc.)
   - For each broker named: any quirks I should know up front? (e.g. supports leveraged ETPs but no options; specific session windows; commission/spread structure). Take a short answer; depth comes later as the user shares.

   **Group C — what you trade (AskUserQuestion, multiSelect):**
   - Asset classes you actively trade: indices, single stocks, commodities, FX, crypto, bonds/rates, options, leveraged ETPs / certificates / turbos, ETFs (buy-and-hold).
   - Geographic focus: EU, US, UK, Asia, global.

   **Group D — style (AskUserQuestion, single-select):**
   - Trading horizon: intraday (close every day), swing (days to weeks), position (weeks to months), mixed.
   - Direction bias: long-only, long/short, mostly long with occasional shorts.
   - Leverage tolerance: none, modest (≤3x), high (>3x leveraged ETPs / turbos comfortable).

   **Group E — risk envelope (plain text):**
   - Typical position size in € / $ / local currency (rough number is fine).
   - Max loss per trade you accept (% or absolute).
   - Daily / weekly stop, if any.

   **Group F — context (plain text, optional):**
   - Anything else I should know up front? Active thesis, themes you're watching, instruments you want me to track, accounts you hold positions in (do not ask for account numbers or credentials — just whether you trade in a specific account they'd want me to reference).

4. **Save everything as you go.** Don't wait until the end. After each group:
   - Append to `.claude/memory/user_<firstname>_trader_profile.md` (create the file on first answer with proper frontmatter — see template below).
   - Add a `MEMORY.md` pointer the first time you create the file.

5. **Offer Telegram setup.** Once the profile is done, ask: "Want me to walk you through the Telegram bot now? It lets you ping me from your phone for briefings, P/L checks, or trade logs while you're away from the laptop. (You can also do this later — just say `set up telegram`.)"

   If **yes**, run the Telegram setup walkthrough (next section). If **no**, skip — just confirm onboarding is complete.

6. **Wrap.** End with a short summary:
   - "Profile saved at `.claude/memory/user_<name>_trader_profile.md`."
   - "Try `/market-situation` for a current briefing, or just describe what you're looking at."
   - "Run `/clean-brain` any time to audit what I've remembered."

## Telegram setup walkthrough

Only run this if the user agreed during step 5 (or invokes it later).

1. **Explain the constraint first** — the Telegram bot only works end-to-end in a **terminal** Claude Code session, not the VS Code extension. Outbound (Claude → Telegram) works in VS Code, but inbound (Telegram → Claude) is silently dropped by the extension. So if they want to be able to message the bot and have you respond, they need a terminal.

2. **Get the bot token.** Direct them:
   - On Telegram, message `@BotFather`.
   - Send `/newbot`, follow prompts, choose a name and username.
   - Copy the HTTP API token BotFather returns (looks like `123456789:ABC-DEF...`).

3. **Install the plugin** — in their terminal in this repo:

   ```bash
   /plugin install telegram@claude-plugins-official
   ```

   Follow the plugin's prompts to paste the token and set the allowlist (their own Telegram user ID — they can get it from `@userinfobot`).

4. **Restart Claude Code with the channels flag.** Tell them to **exit this session** and re-run from the terminal in this directory:

   ```bash
   claude --channels plugin:telegram@claude-plugins-official
   ```

   For unattended use from the phone (no one at the laptop to click prompts), recommend adding `--permission-mode auto`:

   ```bash
   claude --channels plugin:telegram@claude-plugins-official --permission-mode auto
   ```

   Flag the trade-off: auto-permission accepts all tool calls without confirmation. This project's skills are mostly read-only (web fetches + memory/knowledge writes), and `.claude/CLAUDE.md` explicitly forbids auto-executing trades regardless of permission mode — but they should reconsider before installing MCP servers or skills that touch destructive things.

5. **Warn about the VS Code conflict.** While the terminal Telegram session is running, they must **not** open Claude Code chats from the VS Code extension in this project — only one polling process per bot token is allowed, and the VS Code session would steal the token and kill the terminal bot with `409 Conflict`. Same project, two terminal sessions: same issue. One bot, one session.

6. **Quick smoke test.** Once they restart, ask them to send any message to their bot on Telegram. The bot should respond from the terminal Claude. If it doesn't, check:
   - `cat ~/.claude/channels/telegram/bot.pid && ps -p $(cat ~/.claude/channels/telegram/bot.pid)` — is the bot process alive?
   - Did the terminal session start cleanly with the `--channels` flag visible in `ps`?

## `user_<firstname>_trader_profile.md` template

```markdown
---
name: <firstname>-trader-profile
description: <Firstname>'s trader profile — broker(s), assets traded, style, risk envelope. Captured via /onboard on <YYYY-MM-DD>.
type: user
---

# <Firstname>

## Identity

- Reply language: <English / German / …>

## Broker(s)

- <Broker name> — <quirks the user mentioned, leave blank if none>

## What they trade

- Asset classes: <list>
- Geographic focus: <list>

## Style

- Horizon: <intraday / swing / position / mixed>
- Direction: <long-only / long-short / …>
- Leverage tolerance: <none / ≤3x / >3x>

## Risk envelope

- Typical position size: <amount>
- Max loss per trade: <% or absolute>
- Daily/weekly stop: <amount or "none">

## Active focus / themes

- <freeform notes the user shared>

## Notes

- Update this file as preferences evolve. Use `/clean-brain` periodically to audit.
```

## Rules

- **One question at a time, or tight groups.** Don't paste the whole questionnaire in one block.
- **Use AskUserQuestion only for pickable answers.** Names, brokers, risk numbers, and freeform notes should be plain text exchanges.
- **Save incrementally** — write the profile file after each group, not at the end. If the user drops off mid-onboarding, what you have is preserved.
- **Don't push for what they don't want to share.** If they skip the risk envelope or refuse to name an active thesis, just leave that section blank or omit it. Move on.
- **No account numbers, no credentials, no API keys.** If the user offers them, refuse and explain why. The profile is for style and preferences, not secrets.
- **Single-trader is the default.** Multi-trader (a second person sharing this workspace) is supported — if the user mentions a partner / friend who'll also use the repo, create a second `user_<name>_trader_profile.md` and tag entries accordingly in `MEMORY.md`. But don't pitch this unless asked.
- **Confirm before saving anything controversial** — if the user gives a number that looks like a typo (e.g. "€10 million typical position size" from someone who later mentions a retail account), confirm before writing.
- **Stay in their language.** If they answer in German, ask the next question in German. Match.
