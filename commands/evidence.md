---
description: Stages 3 to 5 — gather evidence, hold the working session, draft and audit the BRD
argument-hint: "[optional focus]"
---

The agents named here are this pipeline's: with the consult-to-build plugin they are `consult-to-build:<name>` (for example `consult-to-build:red-team`); installed by hand, just `<name>`.

Run stages 3 to 5. Gate A must already be passed; if `consult/` holds no panel output, stop and say so.

1. Launch `evidence-gatherer` and `case-study-analyst` in parallel, scoped to the open questions in `consult/`.
2. When both return, bring me the contradictions and work through them with me here. Record what I decide, and why, in `decisions/log.md`. Do not proceed until that log exists.
3. Run `brd-writer` against the brief, the research files and the decision log.
4. Run `claim-checker` on the BRD it produced. Never let `brd-writer` check its own work.
5. Report the BRD and the claim audit together, then stop at Gate B.

Do not sign anything. $ARGUMENTS
