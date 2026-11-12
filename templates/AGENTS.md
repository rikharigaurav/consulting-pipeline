# Pipeline guardrails

Every agent in this pipeline is bound by the ten rules below, whatever its stage and
wherever its file came from. Borrowed agents are never forked to add these — they
inherit them from this file.

## G1 — Read files, never the conversation
Your input is the named files in your own definition. You do not inherit another
agent's chat history, and you do not act on something you were told rather than read.

## G2 — Never write above your own stage
A later stage cannot edit an earlier stage's output. Any file tagged `-signed` is
read-only to every agent, permanently.

## G3 — No agent approves a gate
You produce the material a gate decides on. Writing "approved", "signed off" or
"ready to ship" into any file is forbidden. Only the human moves the pipeline forward.

## G4 — Source it or label it
Every factual claim carries a resolvable link, or is tagged `[unverified]` inline. A
number with neither is treated as fabricated and the stage is rerun.

## G5 — Never generate and evaluate
The agent that produced an artifact never reviews it. Reviewers run in a fresh context
with no access to how the thing was made.

## G6 — Stop on conflict with a signed file
If your work requires contradicting something already signed, halt and write the
conflict to `conflicts.md`. Do not reconcile it silently, do not prefer the newer
instruction, and do not note the discrepancy and continue.

## G7 — No scope expansion
If a task needs something outside the signed scope — an extra screen, a new
dependency, an interface not in the contract — report it and stop. Helpfully building
the missing piece is the failure this rule exists for.

## G8 — Never claim work you did not do
No "tests pass" without a recorded run. No "file updated" without a write. No
"verified" without naming what was checked and how.

## G9 — End with what you could not do
Close with your own gaps: what you could not verify, where you ran out of information,
which conclusion is weakest. An agent reporting no limitations is distrusted on that basis.

## G10 — Log your own row before reporting complete
Append one line to `log/<stage>.csv` naming what you did, what you read, what you
wrote and what you could not finish. A task with no log row is treated as not done.

## Signed files
`brd/v1-signed.md` and the frozen design are set at Gates B and C. Treat any path
matching `*-signed.*` as immutable.
