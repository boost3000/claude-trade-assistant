---
name: Always cite sources for fetched data
description: When delivering market analysis, briefings, or any answer that uses fetched data (WebSearch, WebFetch, external info), end the message with a compact source list — outlet + date in plain text, not just URLs. Telegram replies included.
type: feedback
---

Always include a source list at the end of any message that contains fetched data — prices, headlines, calendar items, earnings results, geopolitical developments, anything you didn't already know from training.

**Why:** The user wants an evidence trail for every claim derived from external data. Without sources, briefings become indistinguishable from confident hallucinations.

**How to apply:**

- Format: compact list at the end of the message. One line per source. Include outlet + date + brief topic, not just bare URLs. Example:
  - "Sources: Bloomberg (Brent intraday, 14.05.), CNBC (Trump-Xi summit live, 14.05.), Reuters (PPI April release, 13.05.)"
- Match the language of the reply (German "Quellen:", English "Sources:").
- Telegram inline links blow up the message visually — prefer outlet-name-and-date over full URLs unless a specific URL is essential.
- For multi-source briefings: list every outlet you pulled from, dedupe by outlet name.
- When recalling from memory or training (no fresh fetch), no source list needed — but say "from memory / no fresh fetch" so the user knows.
- Skip only for trivial pings, acknowledgements, or pure-procedural responses (commands, confirmations).

Linked: [[feedback_research_workflow]] (Claude drives research; sources are the evidence trail).
