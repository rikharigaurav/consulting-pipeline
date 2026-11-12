---
description: Stage 10 — independent acceptance and security review
argument-hint: "[optional scope]"
---

The agents named here are this pipeline's: with the consult-to-build plugin they are `consult-to-build:<name>` (for example `consult-to-build:red-team`); installed by hand, just `<name>`.

Graph steps below use the repo-graph plugin: load its `repo-graph:graph-repo` skill with the Skill tool and run its script as the skill says (or use its `review_changes` / `graph_repo` tools when listed). If neither is available, or its script has no `diff` command (repo-graph older than 0.8.0), say so once, skip the graph steps, and carry on.

Run stage 10 with fresh context.

0. Before launching anyone, graph the change under review: run repo-graph's `diff` on this folder `--from <the SHA in build/baseline.txt>` with `--out qa/graph` and save its review as `qa/graph-report.md`. This is a tool's output, not an agent's judgement. No `build/baseline.txt`: ask me which commit, tag or branch to compare against.
1. Launch `acceptance-tester` and `security-reviewer` in parallel. Give `security-reviewer` `qa/graph-report.md` as its index of what changed: the new endpoints, services, env vars and packages, any env var warning, and code no test reaches. It still confirms each item in the code and reports beyond the list.
2. `acceptance-tester` must not read `build/progress.md`, the build log, `build/graph-diff.md`, `qa/graph-report.md`, or any agent's notes. If it has, start it again clean.
3. Both report; neither approves.
4. Lay the two reports side by side, lead with the failures, then add from `qa/graph-report.md`: the "Check first" findings neither report covers, the changed code no test reaches, and any open rows in `log/scope-stops.csv`. Stop at Gate D.

Report what could not be tested as prominently as what failed. $ARGUMENTS
