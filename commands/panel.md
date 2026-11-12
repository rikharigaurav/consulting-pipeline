---
description: Run the full adversarial consulting panel on a question, in parallel, then synthesise where they disagree
argument-hint: "[the decision or question to put to the panel]"
---

The agents named here are this pipeline's: with the consult-to-build plugin they are `consult-to-build:<name>` (for example `consult-to-build:red-team`); installed by hand, just `<name>`.

Put this question to the consulting panel: **$ARGUMENTS**

## How to run it

Launch all relevant advisors **in parallel, in a single message** — one
`Agent` call each, all in the same block. Parallel execution is not an
optimisation here, it is the point: sequential agents read each other's
conclusions and anchor on them, which destroys the independence that makes
the panel worth running.

Choose from `mep-advisor`, `liability-advisor`, `market-analyst`,
`tech-feasibility`, `red-team`. Always include `red-team`. Include the others
by relevance — a question with no physical-safety dimension does not need
`mep-advisor`.

Give each agent the same brief: the full question, the relevant background, and
an instruction to research rather than reason from memory. Do not tell any agent
what the others think, and do not pass one agent's output into another's prompt.

## Then synthesise

Do not summarise the reports one after another. That is a filing exercise, not
advice. Instead:

**1. UNANIMOUS** — what every advisor independently concluded. Five lenses
reaching one answer is the strongest signal this process produces. Say so, and
say what it means for the decision.

**2. UNEXPECTED CONVERGENCE** — where advisors arrived at the same place by
completely different routes. This is usually the most valuable finding, and it
is invisible in any single report.

**3. CONTRADICTIONS** — lay the conflicting claims side by side and name what
each side would need to be true. Do not split the difference, do not average
them, and do not pick the more comfortable one. A contradiction between two
well-researched advisors means the question is genuinely open, and that is where
the real decision sits. This section is the point of the whole exercise.

**4. BLOCKING DECISIONS** — the calls that have to be made before any further
work matters, in dependency order.

**5. THE CHEAPEST NEXT TEST** — the single piece of evidence that would resolve
the most expensive uncertainty. Name what it costs and how long it takes.

**6. KILL CRITERIA** — carried through from `red-team`, each with a number and a
date.

## Rules for the synthesis

- Where advisors disagree, report the disagreement. Never resolve it silently.
- Never soften a verdict because the panel was harsh. If four of five say stop,
  the headline is stop.
- Flag any claim that only one advisor made and no other corroborated.
- Treat every figure as a lead to verify, not a fact. These are five prompted
  instances of one model, with shared blind spots and no site experience.
