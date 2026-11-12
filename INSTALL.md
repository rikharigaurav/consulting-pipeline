# Installing the pipeline by hand

The simpler way is the plugin (README.md): one install per app, synced from GitHub, with the
G2 hook included. This page is the manual route, for this computer only.

Verified against code.claude.com docs, 11 Nov 2026. Two things differ from the
obvious approach — read the warnings.

## 1. Agents (global, all projects)

PowerShell:

    $d = "$env:USERPROFILE\.claude"
    New-Item -ItemType Directory -Force -Path "$d\agents" | Out-Null
    Copy-Item .\agents\*.md "$d\agents\"

18 files. **Restart Claude Code after this one** — agent files are normally
hot-reloaded within seconds, but creating the first file in a new `agents`
directory needs a restart.

Check with `/context`, not `/agents`: on recent builds `/agents` only prints a
reminder about where the files live rather than listing what loaded. If you are
on v2.1.283 or later, `/doctor prompt-audit` audits the agent files directly.

## 2. Commands (per project — see the caveat)

    New-Item -ItemType Directory -Force -Path .\.claude\commands | Out-Null
    Copy-Item .\commands\*.md .\.claude\commands\

`.claude/commands/` is the documented, confirmed path. A user-level
`~/.claude/commands/` is **not** currently documented — it may work, but don't
build on it. Slash commands have also been folded into skills, so the forward
path for new work is `.claude/skills/<name>/SKILL.md`. These files work today as
commands; if one stops being picked up, that is why.

`/reload-skills` rescans commands without a restart.

## 3. Guardrails (per project) — this is the part that was wrong

    Copy-Item .\templates\CLAUDE.md .
    Copy-Item .\templates\AGENTS.md .

**Do not ship AGENTS.md alone.** Claude Code loads `AGENTS.md` only when there
is no `CLAUDE.md`, `CLAUDE.local.md` or `.claude/CLAUDE.md` in the working
directory or any parent — and reading it at all needs v2.1.277+. The moment a
project gains a CLAUDE.md for any other reason, your guardrails silently stop
loading.

The `CLAUDE.md` here is one line, `@AGENTS.md`, which imports it. That pattern
works on every version and in other tools. Keep both files.

## 4. The log compiler (per project)

    New-Item -ItemType Directory -Force -Path .\scripts | Out-Null
    Copy-Item .\scripts\log_compile.py .\scripts\
    pip install openpyxl

Run `python scripts/log_compile.py` at each gate.

## 5. The one hook worth installing now

    New-Item -ItemType Directory -Force -Path .\.claude,.\hooks | Out-Null
    Copy-Item .\hooks\block_signed_writes.py .\hooks\
    Copy-Item .\dot-claude\settings.json .\.claude\settings.json

This is the G2 enforcement: a `PreToolUse` hook that denies any Write or Edit to
a path matching `*-signed.*`. Merge the JSON by hand if you already have a
`.claude/settings.json`.

**Test it before trusting it.** Create `brd/v1-signed.md`, ask Claude to edit it,
and confirm the refusal. Two reasons: the hook needs `python` on PATH, and it is
not documented whether settings-level hooks fire for tool calls made *inside* a
subagent. If they do not, this protects the main session only, and you will want
the same check as a `hooks:` entry in each agent's own frontmatter.

## The assumption that does not hold

Subagents do load the CLAUDE.md hierarchy by default, so the guardrails reach
them. But a subagent can set `omitClaudeMd: true` in its own frontmatter and skip
user, project and local CLAUDE.md entirely.

So a third-party agent file **can opt out of your guardrails**. Before copying any
ECC or knowledge-work agent in, grep it:

    Select-String -Path .\agents\*.md -Pattern "omitClaudeMd"

Nothing should match. For the rules you cannot afford to have skipped — G2, G8,
G10 — use hooks rather than the guardrails file, because a hook applies whatever
the agent's frontmatter says.
