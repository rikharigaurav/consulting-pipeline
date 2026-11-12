---
description: Print the current gate's checklist, branches and the file it decides on
argument-hint: "[A, B, C or D]"
---

Show me Gate **$ARGUMENTS** and hold me to it.

1. Name the file this gate decides on and confirm it exists. If it does not, say the gate is not reachable yet.
2. Print the gate's branches, including the reject path and which stage it returns to.
3. List what I should have read before deciding, and ask whether I have read it.
4. Record my decision in `log/gates.csv` with the date, what changed, and the code it was made on: `git rev-parse --short HEAD`, plus "with uncommitted changes" when `git status --porcelain` isn't empty (or "no git" outside a repository). Match the file's header; when it has no column for the commit, put it in the "what changed" text.

Gates:
- A, after the consult panel: continue, reframe, or kill. The kill branch is real.
- B, BRD sign-off: approve and tag `brd/v1-signed.md` read-only, or revise back to stage 5, or to stage 3 if evidence is missing.
- C, UI sign-off: approve and freeze the design, or revise back to stage 7, or to stage 6 if a use case is wrong.
- D, ship: ship and measure, fix back to stage 9, or hold if it passes tests but misses the metric. Read `qa/graph-report.md` and any open rows in `log/scope-stops.csv` with the two QA reports.

Never record a decision I have not actually made.
