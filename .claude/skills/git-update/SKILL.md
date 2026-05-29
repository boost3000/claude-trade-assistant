---
name: git-update
description: Run a git commit followed by a push.
---

# Run a git commit followed by a push

## Workflow

1. Run `git status` and `git diff` in parallel to see all changes.
2. Run `git log --oneline -5` to match the repo's commit style.
3. Analyze all changes and write a concise commit message in English:
   - First line: short summary (max. 72 characters)
   - Focus on the **why**, not the what
4. Stage the relevant files with `git add` (only relevant files, no secrets).
5. Create the commit via HEREDOC:

   ```bash
   git commit -m "$(cat <<'EOF'
   <commit message>
   EOF
   )"
   ```

6. Run `git push`.
7. Confirm success with the commit hash.

## Rules

- Commit messages always in **English**
- Do not stage secrets, `.env` files, or credentials
- Never use `--no-verify` or `--force` unless explicitly requested
- On hook failure: fix the issue, then create a **new** commit (no `--amend`)
- If there is nothing to commit: report briefly and stop
