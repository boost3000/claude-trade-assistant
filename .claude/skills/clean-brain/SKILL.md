---
name: clean-brain
description: Audit and reorganize the project's memory (`.claude/memory/`) and knowledge base (`.knowledge/`). Detects misfiled content, duplicates, stale entries, broken MEMORY.md links, malformed frontmatter, and files living in the wrong store. Applies safe fixes automatically, uses `WebSearch` / `WebFetch` to verify or refresh time-sensitive content, and surfaces risky moves — including deletions of confirmed-stale content — as proposals for the user to confirm. Ends with a health summary. Use when the user invokes `/clean-brain` or asks to clean up / audit / reorganize / refactor memory, knowledge, notes, or project docs.
---

# Clean-brain — memory & knowledge audit

Audit the project's two persistent stores, apply safe fixes, propose risky ones, deliver a feedback summary.

## The two stores (and their jobs)

- **`.claude/MEMORY.md`** — auto-loaded index (≤200 lines). One-line pointer per memory file.
- **`.claude/memory/*.md`** — user profile, feedback rules, project context, references. Small files, frontmatter required (`name`, `description`, `type` ∈ {user, feedback, project, reference}).
- **`.knowledge/README.md`** — knowledge base entry point / table of contents.
- **`.knowledge/**/*.md`** — long-form domain reference: strategies, instrument quirks, broker rules, tax notes. No frontmatter required; cross-linked freely.

**Auto-load vs. lazy-load is the tiebreaker** when content could plausibly live in either store — see `.claude/CLAUDE.md`. Memory is read every conversation and must stay thin. Knowledge is lazy-loaded and can grow without bounds.

## Process

1. **Inventory.**
   - List every file under `.claude/memory/` and `.knowledge/` (recursive).
   - Read each memory file's frontmatter; note line count.
   - Parse `MEMORY.md` entries and verify each points to a real file.

2. **Audit.** Categorize every finding:
   - **Broken link** — `MEMORY.md` entry points to a missing file.
   - **Orphan memory file** — file exists in `memory/` but has no `MEMORY.md` entry.
   - **Misfiled content:**
     - Memory file that reads like a reference/playbook (narrative, long, no clear user/feedback/project framing).
     - Knowledge file that reads like feedback/preference (short, corrects behavior, names the user).
   - **Duplicate / overlap** — two files cover the same topic; canonical location unclear.
   - **Stale content** — absolute dates written as "current as of X" that are now old; deprecated tickers, names, or thesis statements that no longer apply. When a fact is time-sensitive and externally verifiable (earnings dates, ticker renames, ETF domicile changes, tax rules, broker feature availability), use `WebSearch` / `WebFetch` to check the current reality before deciding whether to refresh the content or mark it for deletion. Never silently delete — always propose.
   - **Malformed frontmatter** — missing `name` / `description` / `type`, or `type` not in the allowed set.
   - **Feedback structure gap** — feedback files missing `**Why:**` and `**How to apply:**` lines.
   - **Index drift** — `MEMORY.md` pointer description no longer matches the file's current `description` frontmatter.
   - **Missing cross-links** — knowledge files on related topics with no mutual references.

3. **Apply safe fixes directly** (no user confirmation needed):
   - Remove `MEMORY.md` entries that point to deleted files.
   - Add `MEMORY.md` entries for orphan memory files, using each file's `description` frontmatter as the hook.
   - Update `MEMORY.md` hook text to match the current `description` when they've drifted.
   - Fix malformed frontmatter fields where the correct value is unambiguous (e.g. `type: feeback` → `type: feedback`).
   - Remove dead cross-links (links to files that no longer exist).

4. **Propose risky changes — do NOT apply without user confirmation.** For each, name the file(s), the proposed action, and the reason:
   - Moving a file between memory and knowledge.
   - Merging overlapping files into one canonical note.
   - Rewriting a memory file to add the missing user/feedback/project/reference structure.
   - Deleting stale content (including whole files) when web verification confirms the underlying fact has changed or no longer applies. Cite the source in the proposal so the user can sanity-check before approving.
   - Refreshing stale-but-still-relevant content with current facts pulled via `WebSearch` / `WebFetch` (e.g. updated ticker, new expiry, revised tax rate). Show the before/after diff in the proposal.
   - Splitting an over-long memory file (>~50 lines) into a thin memory pointer plus a knowledge note.

5. **Deliver the summary.** Output format below.

## Output format

End with this block:

### Clean-brain summary

- **Fixed automatically** (N): one-line list of each change.
- **Proposed changes, need your call** (M): numbered list, each with file path + proposed action + reason. Ask the user which to apply.
- **Health read:**
  - Memory: N files, M total lines, L-line index.
  - Knowledge: N files across K subfolders.
  - Biggest risk spotted (one line).
  - Biggest improvement opportunity (one line).

If nothing is wrong, say so in one line and stop. Don't pad.

## Rules

- **Never delete a file without user confirmation**, even if it looks like a clear duplicate — archival intent is often unclear.
- **Never rewrite feedback content.** If a feedback rule looks obsolete, propose flagging it, don't edit the Why.
- **Preserve the user's voice** when editing existing files — match tone, don't reflow prose.
- **Don't invent cross-links** to files that don't exist. Only link to confirmed present files.
- **When unsure whether content is misfiled, leave it** and surface as a proposal — false moves cost more than false alarms.
- **Fix markdown lint issues** per `memory/feedback_markdown_lint.md` on any file you edit.
- **Don't run this on a cold read** — if the user just asked for an audit, do the work; don't also ask clarifying questions about scope unless genuinely ambiguous.
- **Use web tools sparingly and only for verification** — reach for `WebSearch` / `WebFetch` when a stored fact is externally checkable and likely to have changed (dates, tickers, tax rates, broker features). Don't run web queries on user preferences, feedback rules, or project context — those aren't web-verifiable.
- **Cite sources in proposals** — any deletion or refresh driven by web research must include the URL(s) used, so the user can audit the call before approving.
