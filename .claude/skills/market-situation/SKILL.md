---
name: market-situation
description: Produce an in-depth market situation briefing — current political and macro drivers, macro data calendar, earnings calendar, options expiries/positioning, and their impact across the user's tradeable universe (commodities, indices, FX, rates, single stocks, crypto if relevant). Deliver ≥10 compact ranked trade setups (user picks one to expand). Use when the user asks "what's the market doing", wants a read on the current situation, is looking for trade ideas, or asks about a specific catalyst (Fed, OPEC, earnings, headline event, war escalation, OpEx).
---

# Market situation briefing

Deliver a **dense, actionable** briefing: current drivers → market impact → concrete trade setups. Cover breadth (macro + single-name + positioning), not just commodities.

**Target length: under ~700 words.** Dense, no filler, no generic macro takes.

## Process

1. **Load context.** Read `.claude/MEMORY.md` for user profile + feedback rules. Read the active user profile (`user_<name>_trader_profile.md`) for:
   - **Asset classes** the user actually trades — don't pitch FX setups to an equity-only trader.
   - **Geographic focus** — don't ladder US setups for an EU-only trader unless the EU side is thin.
   - **Trading horizon** — intraday vs swing vs position changes which catalysts matter.
   - **Leverage tolerance** — calibrates instrument selection in step 3.
   - **Any active focus / themes** the user has called out.
   If no user profile exists, run `/onboard` first or ask the user briefly what they trade — don't pitch blind. Skim `.knowledge/strategies/` for relevant playbooks (don't restate them — reference by path).

2. **Fetch current state.** Use WebSearch / WebFetch. Never invent prices, headlines, or calendar dates.
   - **Instruments:** filter to the user's asset classes and geography from step 1. A typical broad set: WTI, Brent, natural gas, silver (XAG), gold (XAU), copper, DXY, EUR/USD, US 10y, 2y, S&P, Nasdaq, DAX, VIX, plus any user-watched single stocks.
   - **Headlines (last 24–48h):** geopolitics (Iran, Ukraine, Middle East, China/Taiwan), US politics, central bank commentary, OPEC, major corporate news.
   - **Macro calendar (next 1–5 sessions):** FOMC/ECB/BoE/BoJ decisions + pressers; CPI / PPI / PCE (US + EZ); NFP / unemployment / jobless claims / JOLTS; retail sales; PMIs (S&P Global, ISM); GDP; consumer confidence / UMich sentiment; Germany IFO / ZEW; central bank speakers. Include exact date + time in the user's preferred timezone (default CET if not stated).
   - **Earnings calendar (next 1–5 sessions):** mega-caps (MAG7, major European names: SAP, ASML, Novo, LVMH, Rheinmetall, Siemens), plus any single names relevant to the user's watchlist. Note pre- vs post-market in the correct timezone.
   - **Options / positioning:** monthly OpEx (3rd Friday), quarterly OpEx / triple witching, major index (SPX, NDX, DAX) notable gamma levels or large-OI strikes if reported, VIX expiry (Weds before monthly), and any single-name earnings-IV crush setups. Flag when OpEx is within the setup horizon — pinning, vanna/charm flows, and post-OpEx unclenches often dominate price in the 48h around expiry.
   - **OPEC / other commodity catalysts:** OPEC+ meetings, EIA inventory (Wed 16:30 CET), API (Tue 22:30 CET), USDA reports where relevant.

3. **Synthesize** into the output structure below. Don't dump the full calendar — filter to what actually moves the user's tradeable universe in the next 1–5 sessions.

## Output structure

### Snapshot

6–10 bullets. Key levels + 1d / 1w change on user-relevant instruments across asset classes (commodities, FX, rates, indices, VIX, any watched single stocks). Only include what's actually moving or what frames the setups below.

### Key drivers

3–5 bullets. Each: **driver → direction of pressure on which market → why (one mechanism)**. Include at least one positioning / flow driver (OpEx, gamma, post-earnings drift, seasonals) when relevant. No generic "uncertainty" takes.

### Calendar (next 1–5 sessions)

Group by type so the user can scan:

- **Macro data:** US CPI/PPI/PCE, NFP/jobless claims, JOLTS, retail sales, PMIs, GDP, ISM, EZ CPI, German IFO/ZEW, BoJ/PBoC fixings. Date + time + consensus when meaningfully priced.
- **Central banks:** FOMC/ECB/BoE/BoJ decisions, pressers, key speakers.
- **Earnings:** mega-caps and user-relevant names. Mark BMO / AMC in the correct timezone. Note expected IV and the post-print move priced in where relevant.
- **Options / flow:** monthly OpEx (3rd Fri), quad witching, VIX expiry, any notable gamma levels or single-name IV events.
- **Commodity-specific:** OPEC+ meetings, EIA (Wed 16:30 CET), API (Tue 22:30 CET), USDA.
- **Unscheduled risk:** active geopolitical flashpoints or pending headline threats.

### Market analysis

3–5 sentences of structural read that ties the data and drivers together. Cross-asset relationships (e.g. DXY ↔ commodities, rates ↔ growth names), regime read (risk-on / risk-off / rotation / vol regime), what's under-priced vs. priced-in. This is the "depth" layer — skip if the picture is thin, don't pad with boilerplate.

### Setups (≥10) — compact first pass

**Deliver at least 10 setups**, ranked by conviction of winning (strongest first). Cover different asset classes (commodity, index, single-stock, FX/rates, vol/VIX) and mix directions (long + short + mean-revert + event) so the user has real optionality — don't stack multiple setups in the same underlying.

**Respect the user profile from step 1:**

- Only pitch asset classes the user trades.
- Match horizon — no multi-week swings for an intraday-only trader, no scalps for a position trader.
- If the user listed an active focus / theme, rank setups matching that focus in the top slots first, then fill the rest. If they de-prioritized a playbook, only include it when the setup is exceptionally clean and tag it as off-focus.
- Still meet the ≥10 / multi-asset / direction-mix requirements within the user's universe. If their universe is too narrow to find 10 clean setups (e.g. EU-indices-only), say so and deliver what's there.

**Lead with the why, not the mechanics.** Each setup = **direction + asset + 1–2 sentences explaining the key factors / causal chain that makes it a pick**. No tickers, no trigger prices, no instrument identifiers, no "risk:" tags in the first pass — those front-load low-value technical detail and bury the thesis. The user decides what to pursue based on the reasoning; execution detail comes in the expansion step.

Example good first-pass line:
`**1. WTI short** — ceasefire extended open-ended, Hormuz reopening rumors, Brent already broke $103→$98. War premium is actively draining and there's no catalyst in the next 48h to reverse it.`

**Factor concentration note** at the top of the list — if 5 setups lean on the same theme (e.g. all Hormuz-escalation), say so honestly so the user sees the correlation risk.

**Apply a vol-vs-cost filter silently:** drop setups where expected underlying move × leverage doesn't dominate round-trip broker spread + fees. Note at the bottom how many were filtered and why (one line). If the user hasn't told you their broker spreads yet, use a conservative estimate and flag the assumption.

If fewer than 10 clean setups exist, say so and deliver what you have rather than padding with weak ideas. If no clean setup exists at all, **say so and stop**. Do not force a trade.

### After user picks a setup — full detail

When the user confirms interest in a specific setup, expand it with:

- **Entry levels** (specific price triggers, session timing for the user's broker)
- **Invalidation / stop** (specific level and what it implies)
- **Targets** (T1, T2, and exit-by time)
- **Sizing guidance** (based on stop distance + leverage + the user's risk envelope from memory)
- **Vol-vs-cost math** (expected underlying move × leverage vs. round-trip broker spread + fee, shown explicitly)
- **Full pattern-break risks** (OpEx, earnings, data-print timing, liquidity windows)
- **Logging offer** — point to the relevant playbook log under `.knowledge/strategies/`, or offer to create one if the pattern is new.

## Rules

- **Fetch, don't guess.** If tools are unavailable or you can't get current data, state that and stop — do not fabricate levels or headlines.
- **Causal chains required.** Every directional claim needs "because" — one mechanism, not vibes.
- **Match horizon.** Pull from the user profile. If the user trades intraday on leveraged products, no multi-week buy-and-hold pitches.
- **Reference playbooks.** If a setup matches an existing strategy file, link to it instead of restating the rules.
- **Flag pattern-break risks inline**, not as a footnote.
- **Verify instrument identifiers are live** before recommending a specific product — issuers reshuffle ranges. If you can't verify, say "confirm identifier with your broker before entry."
- **No emojis in code/configs you write.**
- **Cite sources** at the bottom per `feedback_cite_sources_always.md`.

## After briefing

If the user picks a setup to expand, deliver the full-detail block above. If the user then acts on the setup, offer to log the trade (entry, thesis, outcome) to `.knowledge/strategies/<playbook>-log.md` for later review — the edge is in tracking what works.
