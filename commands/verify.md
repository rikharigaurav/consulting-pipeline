---
description: Stage 10 — independent acceptance and security review
argument-hint: "[optional scope]"
---

The agents named here are this pipeline's: with the consult-to-build plugin they are `consult-to-build:<name>` (for example `consult-to-build:red-team`); installed by hand, just `<name>`.

Run stage 10 with fresh context.

1. Launch `acceptance-tester` and `security-reviewer` in parallel.
2. `acceptance-tester` must not read `build/progress.md`, the build log, or any agent's notes. If it has, start it again clean.
3. Both report; neither approves.
4. Lay the two reports side by side, lead with the failures, and stop at Gate D.

Report what could not be tested as prominently as what failed. $ARGUMENTS
