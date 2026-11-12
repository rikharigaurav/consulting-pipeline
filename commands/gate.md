---
description: Print the current gate's checklist, branches and the file it decides on
argument-hint: [A, B, C or D]
---

Show me Gate **$ARGUMENTS** and hold me to it.

1. Name the file this gate decides on and confirm it exists. If it does not, say the gate is not reachable yet.
2. Print the gate's branches, including the reject path and which stage it returns to.
3. List what I should have read before deciding, and ask whether I have read it.
4. Record my decision in `log/gates.csv` with the date and what changed.

Gates:
- A, after the consult panel: continue, reframe, or kill. The kill branch is real.
- B, BRD sign-off: approve and tag `brd/v1-signed.md` read-only, or revise back to stage 5, or to stage 3 if evidence is missing.
- C, UI sign-off: approve and freeze the design, or revise back to stage 7, or to stage 6 if a use case is wrong.
- D, ship: ship and measure, fix back to stage 9, or hold if it passes tests but misses the metric.

Never record a decision I have not actually made.
