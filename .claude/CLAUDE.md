# Claude Trade Assistant

Project for assisting with retail trading research, idea generation, and trade logging — broker-agnostic and asset-agnostic. The user picks the broker, the markets, and the style during `/onboard`; their answers shape every future conversation.

## First-run check

**Before answering the user's first request in any new conversation, check whether `.claude/memory/` contains a `user_*` profile file.** If it does not, the user has not been onboarded yet. Greet them briefly and suggest running `/onboard` to set up their profile before going further. They can still ask one-off questions without onboarding — but flag that without a profile you'll be making generic assumptions about broker, asset class, and style.

After `/onboard` runs, the user profile and per-session preferences live in `.claude/memory/`; read them on conversation start and use them to shape every response.

## Project structure

- `.claude/` — Claude Code workspace configuration and memory
  - `CLAUDE.md` — this file; project-level instructions for Claude
  - `MEMORY.md` — index of persistent memories (loaded into every conversation)
  - `memory/` — individual memory files referenced from `MEMORY.md`
  - `skills/` — slash commands (`/onboard`, `/market-situation`, `/trades-pl`, `/git-update`, `/clean-brain`)
- `.knowledge/` — trading knowledge base. Build this up over time with notes on strategies, instruments, broker mechanics, tax considerations, etc. Organize by topic (e.g. `.knowledge/strategies/`, `.knowledge/instruments/`, `.knowledge/<broker-name>/`).

## Memory location

Store all persistent memory for this project in `.claude/memory/` (not in the global `~/.claude/` path). The `MEMORY.md` index lives at `.claude/MEMORY.md`. Follow the standard memory format — frontmatter with `name`, `description`, `type` (user | feedback | project | reference), then the content. Add a one-line pointer in `MEMORY.md` for each memory file.

## Knowledge base

Treat `.knowledge/` as a growing reference library about trading. When the user shares insights, strategies, or hard-won lessons about trading or their broker specifically, capture them as markdown notes under the appropriate subfolder. Link related notes to each other. Prefer updating existing notes over creating new ones when the topic already has a home.

Knowledge base content is for long-lived domain reference (how options pricing works, what your broker's order types do, tax treatment of ETFs in your jurisdiction, etc.). Memory is for user/project/feedback context. Don't confuse the two.

**Tiebreaker — auto-load vs. lazy-load.** `MEMORY.md` is loaded into every conversation (with a 200-line index cap), so memory must stay thin. `.knowledge/` is read on demand, so it can grow to hundreds of pages of reference material without bloating every turn's context. If content would be useful *every time* the user starts a conversation, it belongs in memory. If it's *reference I only need when the topic comes up*, it belongs in knowledge.

## Trading context

This project deals with real financial decisions. When writing code or advice that could affect trades:

- Be explicit about assumptions (fees, spreads, tax, FX).
- Flag anything that could lose money if wrong.
- Never auto-execute trades without explicit confirmation from the user, even if a script appears authorized, and even when running in `--permission-mode auto`.
