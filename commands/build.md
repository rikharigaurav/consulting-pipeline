---
description: Stages 8 to 9 — compile the build contract, resolve ambiguities, then build
argument-hint: "[optional module to start with]"
---

The agents named here are this pipeline's: with the consult-to-build plugin they are `consult-to-build:<name>` (for example `consult-to-build:red-team`); installed by hand, just `<name>`.

Graph steps below use the repo-graph plugin: load its `repo-graph:graph-repo` skill with the Skill tool and run its script as the skill says (or use its `review_changes` / `graph_repo` tools when listed). If neither is available, or its script has no `diff` command (repo-graph older than 0.8.0), say so once, skip the graph steps, and carry on.

Run stages 8 and 9. Requires a signed BRD and a frozen design.

0. Record the baseline: write `build/baseline.txt` with the output of `git rev-parse HEAD`, the branch, the date, and whether the working tree had uncommitted changes. If the tree is dirty, ask me to commit or stash first; the baseline is what the build is measured against. Not a git repository: say the graph steps need one and skip them.
1. Run `contract-assembler` to compile `build/contract.md` from the signed files only. When `research/codebase-map.md` exists, give it the map as well, for two things only: to say where each contract item lands in the existing code (`path:line`), and to list every place the signed files and the existing code disagree under `OPEN DECISIONS`. The map is not a source of requirements.
2. Run `ambiguity-hunter` on that contract, cold.
3. Bring me `build/ambiguities.md` and wait. Do not choose for me, and do not start building with open ambiguities — that is the whole point of this step.
4. Once I have answered, fold my answers into the contract. Offer me the live review before building: repo-graph's `live` view of this folder with its UI tab (`live "<project folder>" --open --ui`, started in the background as the skill says) shows the app and each file as the agents change it, with Accept / Undo per file. If I start it, give me its URL; when its hook reports that I undid a change, the agent that made it re-reads the file and does not redo it.
   Then instance `module-dev` once per module, each on its own branch, one module per agent.
5. Run `fde-agent` on integration, real data and deployment wiring. It does not deploy.
6. Graph what the build changed: run repo-graph's `diff` on this folder `--from <baseline SHA>` (the head is what is on disk now) with `--out build/graph-diff`. If the modules are still on their own branches, run it once per branch (`--to <branch>`, `--out build/graph-diff/<branch>`) and combine the reviews. Then write `build/graph-diff.md`: the review it printed, followed by `## Outside the contract (G7)`, listing every new endpoint, external service, env var, package, agent, MCP server and top-level folder in the review that `build/contract.md` does not name, each with its `path:line`. Do not judge or fix them here. Append one row per item to `log/scope-stops.csv`, matching its header, with the decision left to me.
7. Report what was built, the real test output, and anything blocked. Then, from `build/graph-diff.md`: its "Check first" findings, the items outside the contract, and the tests it says to run that were not run. If anything is outside the contract, stop there: G7 says I decide whether it stays.

$ARGUMENTS
