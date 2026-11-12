---
description: Stages 8 to 9 — compile the build contract, resolve ambiguities, then build
argument-hint: "[optional module to start with]"
---

The agents named here are this pipeline's: with the consult-to-build plugin they are `consult-to-build:<name>` (for example `consult-to-build:red-team`); installed by hand, just `<name>`.

Run stages 8 and 9. Requires a signed BRD and a frozen design.

1. Run `contract-assembler` to compile `build/contract.md` from the signed files only.
2. Run `ambiguity-hunter` on that contract, cold.
3. Bring me `build/ambiguities.md` and wait. Do not choose for me, and do not start building with open ambiguities — that is the whole point of this step.
4. Once I have answered, fold my answers into the contract, then instance `module-dev` once per module, each on its own branch, one module per agent.
5. Run `fde-agent` on integration, real data and deployment wiring. It does not deploy.
6. Report what was built, the real test output, and anything blocked.

$ARGUMENTS
