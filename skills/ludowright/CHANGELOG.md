# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

### C-20261121-1 · 2026-11-21 · OSRS harvest lessons: rubric R-83 to R-86, three economy failure patterns (0.1.47)
- because: user request (general lessons from the Arvum Electrum OSRS harvest, 2026-11-20; each measured in that game's simulations)
- files: kb/review-rubric-more.md (R-83 to R-86), kb/review-rubric.md (How to run 11, Related), kb/balance-and-economy.md (Failure patterns), kb/INDEX.md, tests/test_ldw.py (KbSectionsTest)
- R-83 round trip that prints money, R-84 rounding eats small bonuses, R-85 shared resource with no claim, R-86 disasters with no spacing; failure patterns add the round trip, the remainder and a morale floor. Triggers unchanged, so evals were not re-run.

### C-20261120-4 · 2026-11-20 · Worldbuilding 10 to 14 and adapting block; rubric R-81, R-82; AI state explosion (0.1.46)
- because: user request (book round: Robbins, Microscope Explorer; Campos, Game Development Patterns with Godot 4 (Godot 4.3); book rules, unverified)
- files: kb/worldbuilding-and-lore.md (10 to 14, Adapting a co-made world), kb/review-rubric-more.md (R-81, R-82), kb/review-rubric.md (How to run 11, Related), kb/game-ai-for-designers.md (30), kb/INDEX.md, tests/test_ldw.py (KbSectionsTest)
- Adds focus rounds with legacies, setup-only category vetoes, concept setup lists with a change axis, the picture-it test with reasoned tone labels, stuck prompts, and six logged moves for adapting a co-made world. R-81 flags a quest whose stakes are an outcome players already know (railroaded player covers lost choice, not this). R-82 flags buff stacks with order-dependent results, no single removal or one shared duration. Item 30 splits a combined state machine into parallel families. Changelog 0.1.44 and 0.1.45 archived first. Triggers unchanged, so evals were not re-run.

Entries 0.1.45 and older are in [ai-docs/changelog-archive.md](../../ai-docs/changelog-archive.md), moved out to keep the installed folder small.
