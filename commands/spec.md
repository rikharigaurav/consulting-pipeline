---
description: Stages 6 to 7 — testable spec and UI design from the signed BRD
argument-hint: "[optional focus]"
---

The agents named here are this pipeline's: with the consult-to-build plugin they are `consult-to-build:<name>` (for example `consult-to-build:red-team`); installed by hand, just `<name>`.

Run stages 6 and 7. Requires `brd/v1-signed.md`; if it is absent, stop and tell me Gate B has not been passed.

1. Run `spec-writer` against the signed BRD. Every acceptance criterion must be able to fail, and every NFR must carry a number.
2. Show me the spec and let me correct it before any design work starts.
3. Run `ui-designer` against the spec, then `design-reviewer` on its output. The designer never reviews itself.
4. Report the spec, the coverage table, and anything the designer could not cover, then stop at Gate C.

Do not sign anything. $ARGUMENTS
