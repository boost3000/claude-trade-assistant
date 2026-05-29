---
name: User drives decisions, Claude drives research
description: Don't ask the user to fetch data or check market levels for you. You drive the research; the user just needs to know when to ping you for a decision. Be specific about ping moments and what you'll have prepared.
type: feedback
---

When setting up future trade decisions, **never ask the user to come back with data** ("ping me with where the index is", "let me know X's close", "check the consensus and report back"). The user's contribution is **decisions and execution**, not research.

**Why:** Treating the user as a data-gathering input misuses their time and reverses the value of the assistant. The user pays you for research; you don't pay them.

**How to apply:**

- For each upcoming decision moment, give the user a **specific time to ping** (e.g. "ping me Tue 21:00 local") and **what I'll have prepared by then** (closes, consensus, narrative, instrument availability, go/no-go criteria).
- Between pings, do the data work proactively: pull current prices, fresh headlines, calendar, instrument availability via WebSearch / WebFetch.
- If a decision needs intraday data (e.g. a gap level at the open), commit to fetching it yourself when the user pings — don't ask them to read it off their screen unless the data source is genuinely unreachable from your tools.
- **Acceptable ask:** clarifying questions about user state (account size, risk tolerance, what they've already executed) — those aren't research, those are inputs only the user has.
- **Not acceptable:** "check X and tell me", "report back with Y", "let me know what the tape is doing" — these put the research burden on the user.
