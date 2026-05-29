---
name: Fix all markdown lint issues
description: Every markdown lint error and warning gets resolved in any markdown file authored or edited in this project.
type: feedback
---

Always fix all markdown linter errors and warnings in any markdown file that gets created or modified in this project.

**Why:** Standing preference that markdown files be lint-clean — not just the lines being edited, but the whole file after the change. Keeps memory, knowledge notes, and docs scannable and grep-friendly.

**How to apply:** After writing or editing any `.md` file (memory files, knowledge base notes, docs, etc.), check for lint issues (e.g. via markdownlint / IDE diagnostics) and fix them before considering the task done. Applies to files under `.claude/`, `.knowledge/`, and anywhere else in the repo. Project config in `.markdownlint.json` disables MD013 (line length) and MD041 (first-line H1) — rely on those defaults; flag if any other rule conflicts with content the user explicitly wants.
