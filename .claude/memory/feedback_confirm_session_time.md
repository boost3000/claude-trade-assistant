---
name: Always fetch fresh date/time before time-sensitive analysis
description: Before any analysis, briefing, setup pitch, or trade advice, run `date` via Bash to get the current system time. Never assume the time from context or earlier in the conversation.
type: feedback
---

**Run `date '+%Y-%m-%d %H:%M:%S %Z (%A)'` via Bash on EVERY user prompt**, before any other tool call. No exceptions. Not "if relevant" — every turn.

**Why:** Time-of-day drives everything in this project — session windows, spread regimes, catalyst countdowns, "wait until X" advice, decay math on leveraged products. The system reminder gives the date but not the time. Without a fresh `date`, the model drifts from the last value it saw earlier in the conversation and keeps building advice on stale assumptions. Past failure pattern: assistant assumes it's still morning when it's actually late afternoon, gives a "wait until 09:15 to enter, exit 17:00" plan well after the session has closed.

**How to apply:**

- **Every prompt** — `date` is the **first** Bash call, every single turn, before any analysis. Cheap (~0 tokens, instant). Not a "consider it" — it's mandatory.
- Do not rely on the timestamp from earlier in the conversation, even if the previous turn was recent. Sessions pause, users walk away, time drifts.
- Do not infer current time from `ScheduleWakeup` return values — those are based on the runtime's internal clock that can drift.
- The `date` output drives: DST label, session position (your trading venue's open/close), countdowns to scheduled catalysts (CPI, FOMC, earnings BMO/AMC).
- If `date` is forgotten and you make any time-based claim, expect the user to correct you — the cost of being wrong is concrete trade-window damage.
