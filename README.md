# Consult to Build pipeline

Nineteen agents, four human gates, one combined workbook.

## Install: as a plugin (one copy, synced everywhere)

This repo is a Claude plugin, `consult-to-build`, in a marketplace of its own,
`consulting-pipeline`. Install it once per place you use Claude, and every chat there gets
the 18 agents, the stage commands and the G2 hook. Push to `main` and they all update.

- **Claude app** (desktop and web, including Claude Code chats there): Customize → Plugins →
  add a marketplace from GitHub, `rikharigaurav/consulting-pipeline`, then install
  **Consult to Build**. It follows `main`.
- **Claude Code on your computer**:

      /plugin marketplace add rikharigaurav/consulting-pipeline
      /plugin install consult-to-build@consulting-pipeline

  Later changes: `/plugin marketplace update consulting-pipeline`, then `/reload-plugins`.

Commands and agents are namespaced by the plugin: `/consult-to-build:panel` (plain `/panel`
works when nothing else takes the name) and `consult-to-build:red-team`.

If you installed the files by hand before (`install.ps1`), remove the copies in
`~/.claude/agents/` so each agent appears once.

Per project, run `/init-pipeline <problem>`: it copies the guardrails (`AGENTS.md` and a
`CLAUDE.md` that imports it) and `scripts/log_compile.py` into the project from the plugin.
The G2 hook needs nothing per project: it comes with the plugin and applies to every
`*-signed.*` file in every project while the plugin is on.

## Install: by hand (this computer only, no syncing)

`.\install.ps1` copies the agents into `~/.claude/agents`; `.\install.ps1 -Project <path>`
also sets up one project with the commands, guardrails, hook and log compiler. See
`INSTALL.md`.

## Running it

A pipeline with human gates cannot be one command. Six, with your decision between:

| Command | Stages | Then |
| --- | --- | --- |
| `/init-pipeline <problem>` | 1 | write the brief |
| `/panel <question>` | 2 | **Gate A** — continue, reframe or kill |
| `/evidence` | 3-5 | **Gate B** — sign the BRD |
| `/spec` | 6-7 | **Gate C** — sign the design |
| `/build` | 8-9 | |
| `/verify` | 10 | **Gate D** — ship |

`/gate A` prints any gate's checklist and records the decision.

## The one agent you write per project

`mep-advisor` is the construction instance of the domain-advisor slot. A project in
another domain needs its own. Write its `## Never` list first — that is where the
expertise sits.

## Guardrails

`templates/AGENTS.md` holds the ten rules every agent inherits, including borrowed ones. That is
why ECC and knowledge-work agents are copied unmodified rather than forked: upgrading
one is a re-copy, and your constraints still apply.

G8 and G10 need hooks to actually hold. Everything else is prompt-shaped.
