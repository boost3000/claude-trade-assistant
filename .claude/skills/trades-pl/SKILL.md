---
name: trades-pl
description: Output a P/L overview of all executed trades recorded in `.knowledge/strategies/`. Use when the user asks for a P/L summary, trade history, performance overview, or invokes /trades-pl.
---

# Trades P/L overview

Produce a compact P/L table of every **executed** trade logged in the knowledge base, plus a short pattern read.

## How to find trades

Trades live in trade-log sections inside `.knowledge/strategies/*.md`. Each strategy file may contain zero, one, or several entries under a `## Trade log` heading, with subheadings like `### YYYY-MM-DD — <name> — <OUTCOME>`.

1. List `.knowledge/strategies/` and grep for `## Trade log` / `### 20` to find every entry.
2. Read each matched section. Each trade entry typically contains: Instrument, Direction, Entry, Exit, Result/P&L, and a thesis/retro.
3. Extract: date, name, direction, notional, outcome label (WIN / SMALL WIN / LOSS / etc.), net P/L in the user's account currency.

## Filter rules — executed only

**Exclude any trade that was not entered.** Skip entries marked `MISSED`, `NOT ENTERED`, hypothetical, or any retro where the "Entry" field is `none` / blank. Missed setups are not trades.

If unsure whether an entry was executed, check the Entry line for a real fill (size + price + timestamp). No fill → not a trade.

## Output format

Markdown table, columns in this exact order:

| # | Date | Trade | Direction | Notional | Result | Net P/L |

- Date: ISO `YYYY-MM-DD`. For multi-day holds use `YYYY-MM-DD → MM-DD`.
- Trade: short label (instrument or setup name, optionally with ticker/identifier if it disambiguates).
- Direction: e.g. `Long`, `Short DAX`, `Short SPX`.
- Notional: amount at entry in the user's account currency (`€1,000`, `$1,000`, `~€1,000` if approximate).
- Result: bold outcome label + percent in parens — e.g. `**WIN** (+5.0%)`, `**LOSS** (−2.2%)`, `**SMALL WIN** (+0.25%)`.
- Net P/L: bold figure with sign — e.g. `**+€50.00**`, `**−€22.00**`.

Below the table:

1. **Aggregate realized: ±X.XX** across N executed trades. Win rate W/N.
2. A 2–4 sentence pattern read — what's actually carrying the book, which losses came from discipline vs. thesis, what regime/structural issue is showing up across recent trades. Be specific; reference dates or trades. Do not pad.

## Style

- Sort chronologically, oldest first.
- Use a real minus sign (`−`) for negative numbers, not a hyphen.
- Don't list sources at the bottom unless the user asks — they know where the data lives.
- Don't add columns beyond the seven specified. No "Strategy" or "Notes" column.
- Keep the response tight: table + aggregate line + pattern read. Nothing else.
- If `.knowledge/strategies/` has no executed trades yet, say so in one line and stop. Don't fabricate.
