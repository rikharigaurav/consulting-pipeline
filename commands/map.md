---
description: Map an existing codebase with repo-graph so the spec and the build contract are written against the real code
argument-hint: "[repo URL, owner/repo or folder; default: this project]"
---

The agents named here are this pipeline's: with the consult-to-build plugin they are `consult-to-build:<name>` (for example `consult-to-build:red-team`); installed by hand, just `<name>`.

Map the codebase this project changes: **$ARGUMENTS** (if empty, this project's own folder; if that has no source code, ask me which repository).

This step uses the repo-graph plugin. Load its `repo-graph:graph-repo` skill with the Skill tool (or use its `graph_repo` / `explore_graph` / `search_graph` tools when they are listed). If neither is available, tell me to install repo-graph (marketplace `rikharigaurav/repo-graph-mcp`) and stop: do not map the code by reading files instead.

1. Build the graph exactly as the skill says, with `--out research/codebase-graph` (graph.html, graph.json, summary.txt land there; they are regenerated on every run). Map the repository I named and no other.
2. Show me the graph the way the skill says (artifact, or my browser).
3. Write `research/codebase-map.md` from the printed summary, plus `explore` / `search` on the saved graph for anything the summary only counts:
   - what the code is: languages, the main areas (top folders) and what each holds;
   - its surface: API endpoints with their handlers and who calls them, agents, MCP servers;
   - what it depends on: external services, env vars (and any `Warning:` line, verbatim), packages;
   - its hubs: the most-called functions and most-imported files, which any change will ripple through;
   - test reach: what has tests and what has none;
   - the commit it was mapped at (`git rev-parse HEAD`, or the SHA in the summary).
   Every line cites `path:line` or the graph (G4). Describe; do not propose. This file is evidence about the code, never a requirement: nothing in it enters the spec or the contract unless a signed file asks for it.
4. End the file with what the graph cannot see (G9): dynamic calls and reflection, languages it lists only as files, runtime config, anything outside the repo.
5. Append your row to `log/timeline.csv` and `log/files.csv`, matching each file's header (G10).
6. Report the map's headline in five lines and stop. Run `/spec` (or `/panel` when the problem is still open) next; both read the map when it exists.
