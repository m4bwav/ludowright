---
title: One skill with task references, and the size budgets
date: 2026-10-29
summary: ludowright ships one skill (router plus references), not siblings; budgets green/yellow/red with the rubric setting the per-file ceiling
---

# One skill, and the size budgets

**Decision.** ludowright is one skill, `skills/ludowright/`, whose SKILL.md routes to four task procedures (`references/design.md`, `review.md`, `improve.md`, `balance.md`) and to the kb. No sibling skills.

**Why.** Agent Skills linters reject links that leave a skill folder, so sibling skills would each need a copy of the kb (everscout generates such copies; that is machinery this plugin does not need yet). Every sibling also adds an always-loaded description. Nothing in the research showed users asking for the tasks under different names that one description cannot cover. Revisit if a trigger eval shows one task under-triggering.

**Budgets** (`scripts/budget.py`, CI fails on red): description characters green 1,100, yellow 1,400; SKILL.md tokens 2,500 and 3,500; largest kb or reference file 5,500 and 7,000 tokens, set by `kb/review-rubric.md` (about 5,000), which a review reads whole, so splitting it would save nothing; installed skill folder 300 and 600 KB; tracked repository 1,024 and 3,072 KB.

Related: see also [../reading/inventory.md](../reading/inventory.md)
