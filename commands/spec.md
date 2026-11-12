---
description: Stages 6 to 7 — testable spec and UI design from the signed BRD
argument-hint: "[optional focus]"
---

The agents named here are this pipeline's: with the consult-to-build plugin they are `consult-to-build:<name>` (for example `consult-to-build:red-team`); installed by hand, just `<name>`.

Run stages 6 and 7. Requires `brd/v1-signed.md`; if it is absent, stop and tell me Gate B has not been passed.

1. Run `spec-writer` against the signed BRD. Every acceptance criterion must be able to fail, and every NFR must carry a number.
   If `research/codebase-map.md` exists (this project changes existing code; `/map` writes it), give it to `spec-writer` too: it also writes `spec/coverage-vs-code.md`, one row per use case naming the existing endpoints, modules and data it extends (`path:line`) or saying "new", plus every place the signed BRD contradicts what the code does now. Those contradictions go to `conflicts.md` (G6). The map never adds a use case.
   If the map is older than the code (its commit isn't HEAD), say so and offer `/map` first.
2. Show me the spec (and the coverage table) and let me correct it before any design work starts.
3. Run `ui-designer` against the spec, then `design-reviewer` on its output. The designer never reviews itself.
4. Report the spec, the coverage table, and anything the designer could not cover, then stop at Gate C.

Do not sign anything. $ARGUMENTS
