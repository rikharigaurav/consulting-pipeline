---
description: Scaffold the pipeline folders and write the problem brief for a new project
argument-hint: "[one line describing the problem]"
---

Set up a new run of the consult-to-build pipeline for: **$ARGUMENTS**

0. Install the guardrails and the log compiler in this project, from the plugin's own copies, without overwriting anything:
   - `AGENTS.md`: if the project root has none, copy `${CLAUDE_PLUGIN_ROOT}/templates/AGENTS.md` there unchanged. If one exists and isn't these guardrails, stop and ask me.
   - `CLAUDE.md`: if none exists, copy `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE.md` (the single line `@AGENTS.md`). If one exists, add `@AGENTS.md` as its first line unless it already imports it. Never ship `AGENTS.md` alone: Claude Code reads it only when there is no `CLAUDE.md`.
   - `scripts/log_compile.py`: if absent, copy `${CLAUDE_PLUGIN_ROOT}/scripts/log_compile.py` there. It needs `openpyxl` (`pip install openpyxl`).
   - The G2 hook ships with the plugin and is already active: nothing to install.
1. Create the folders if absent: `problem/ consult/ research/ decisions/ brd/ spec/ design/ build/ qa/ log/`, each with a one-line README naming what lands there and which stage writes it.
2. Create `log/` CSV headers for the seven sheets: timeline, gates, claims, conflicts, scope-stops, limitations, files.
3. Interview me to write `problem/brief.md`: what hurts, who has it, what I believe is true, what I am assuming. No solution. Ask at most five questions, one at a time.
4. Stop. Do not run the panel. Report the folder tree and tell me to run `/panel` when the brief reads true.

Do not write any solution, scope or requirement in this step. The brief is the problem only.
