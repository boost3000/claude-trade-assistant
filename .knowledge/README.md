# Trading knowledge base

Long-lived reference notes about trading, your broker(s), and the markets you participate in. Empty on a fresh clone — grow it as you go.

## Suggested folder structure

- `strategies/` — trading strategies, entry/exit rules, trade logs (the source of `/trades-pl`)
- `instruments/` — notes on specific stocks, ETFs, derivatives, leveraged products
- `<broker-name>/` — broker-specific quirks: order types, fees, session windows, UI gotchas, supported product universe
- `tax/` — tax treatment relevant to your jurisdiction
- `market-mechanics/` — spreads, liquidity, market hours, order execution

Keep notes factual and source-linked where possible. Update existing notes rather than creating duplicates.

## Memory vs. knowledge

- **`.claude/memory/`** is auto-loaded into every conversation (capped at ~200 index lines). Use it for user profile, feedback rules, project context, references. Keep it thin.
- **`.knowledge/`** is read on demand. Use it for everything that's useful *when the topic comes up* — strategy playbooks, instrument deep-dives, broker quirks, tax notes. Can grow without bounds.

If you're unsure where something belongs, ask Claude. Run `/clean-brain` periodically to audit both stores.

## Multi-trader setup

This workspace supports two or more people sharing it (e.g. a trading partnership). Convention:

- Knowledge content stays **person-agnostic** — strategy playbooks, instrument notes, broker mechanics, tax notes.
- **Individual trade-execution entries** (inside a strategy file's "Trade log" section) tag the executor: `<Firstname> filled YYYY-MM-DD at <price>`. The distilled lesson goes back into the playbook in person-agnostic form.
- Per-person preferences, risk rules, instrument constraints belong in `.claude/memory/` as separate `user_<firstname>_trader_profile.md` files.

If you're the only trader, ignore this section.
