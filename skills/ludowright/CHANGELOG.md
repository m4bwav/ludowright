# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

### C-20261123-3 · 2026-11-23 · Cobalt Core harvest: card pool shape rule and `ldw.py deck` (0.1.54)
- because: harvest: local game harvest 2026-11-23 (Cobalt Core; aggregate counts from shipped readable data, nothing copied)
- files: kb/balance-and-economy.md (40), scripts/ldw.py (deck), tests/test_ldw.py
- New `deck` command prints a card table's cost histogram, keyword shares, pool sizes and branching-upgrade share, and flags MEAN_COST, ZERO_COST, KEYWORD_EVERYWHERE and POOL_UNEVEN. Rule 40 gives the reference bands. Triggers are unchanged, so the evals were not re-run.

### C-20261123-2 · 2026-11-23 · Runner-up harvest: spatial triggers, neighbour effects and themed loot, parent rows and curves, gate verbs (0.1.53)
- because: harvest: local game harvest runners-up 2026-11-23 (Backpack Hero, 9 Kings, RimWorld, Animal Well; play and evaluator notes only, nothing copied)
- files: kb/systems-and-loops.md (26-27), kb/balance-and-economy.md (39), kb/levels-and-space.md (26)
- Four design rules: a trigger-by-effect vocabulary with empty cells as neighbours, grid neighbour effects with beaten threats offering themed cards, parent and child data rows with override-only fields and point-list curves, gate items as multi-use verbs with free order. Triggers unchanged, so evals were not re-run.

### C-20261123-1 · 2026-11-23 · Local game harvest: slot upgrades, situation cards, deduction sets, survival tier, threat-gated income (0.1.52)
- because: harvest: local game harvest 2026-11-23 (Monster Train 2, Sultan's Game, Oxygen Not Included, Chants of Sennaar, Thronefall; play only, methods paraphrased, nothing copied)
- files: kb/systems-and-loops.md (23-25), kb/balance-and-economy.md (38), kb/core-loops-and-goals.md (22)
- Five design rules: slot-limited modular upgrades with capacity zones, situation cards with typed slots and two clocks, all-or-nothing deduction checks, two-layer work priority with a survival tier and a mirrored good break, income paid only for what survived. Triggers unchanged, so evals were not re-run.

### C-20261122-2 · 2026-11-22 · Colony-sim lessons: wild vs invested, meter extremes, sets, needs, pulses, time-left, gross flows, lenses, music rest, start rings, staffing ranks, frame budget (0.1.51)
- because: harvest: Oxygen Not Included local harvest 2026-11-22 (tier A only: play, wiki, shipped plain-text data; methods and paraphrase, numbers from our own simulations)
- files: kb/systems-and-loops.md (20-22), kb/balance-and-economy.md (36-37), kb/ux-and-the-brain.md (26-29), kb/procgen.md (25), kb/game-ai-for-designers.md (32-33)
- Thirteen design rules, each with the number our simulation measured. Before this the kb had no rule on wild against invested yield, meter floors, set bonuses, pulsing sources, time-left readouts, gross flows, map lenses, music rest, ring guarantees, staffing ranks or decision budgets. Triggers unchanged, so evals were not re-run.

### C-20261122-1 · 2026-11-22 · Point-of-interest density and port-when-proven (0.1.50)
- because: harvest: Reddit post 1y2w5yy (an underwater sandbox postmortem), items 9 and 10
- files: kb/levels-and-space.md (25), kb/production-and-scope.md (28)
- Levels had landmarks but no density measure for open worlds; production had prototype rules but nothing on when to port script code to native. Both marked unverified by a book. Triggers unchanged, so evals were not re-run.

### C-20261121-3 · 2026-11-21 · Event director, mood meter and grammar checks (0.1.49)
- because: harvest: RimWorld local harvest 2026-11-21 (technique observed in RimWorld's shipped defs, 2026-11-21; methods and a few paraphrased numbers only, code written fresh)
- files: scripts/ldw.py (director, mood, grammar), kb/balance-tables.md (three shapes), kb/levels-and-space.md (24), kb/game-ai-for-designers.md (31), kb/balance-and-economy.md (35), kb/procgen.md (24), kb/INDEX.md, SKILL.md (Count with the script), evals/grammar-fixture.json, tests/test_ldw.py (Director, Mood, Grammar)
- `director` simulates independent event clocks (on/off windows, mean gap, once) with grace, spacing, budget curves and a clamped adapt counter; `mood` runs a seek-to-target meter with capped stacks and severity bands; `grammar` checks a weighted, conditional rewrite grammar. Before this, no command scheduled events, stacked modifiers or measured a grammar. Triggers unchanged, so evals were not re-run.

### C-20261121-2 · 2026-11-21 · Light-touch onboarding and a daily find (0.1.48)
- because: user request (technique harvest of a browser game's shipped scripts; no licence, so methods and numbers only)
- files: kb/ux-and-the-brain.md (Light-touch onboarding and a daily find), tests/test_ldw.py (KbSectionsTest)
- Character's note beside its target, a tour that runs on whichever targets exist with seen-state and replay, and a once-a-day hidden find with an in-fiction refusal. Changelog 0.1.46 archived first. Triggers unchanged, so evals were not re-run.

### C-20261121-1 · 2026-11-21 · OSRS harvest lessons: rubric R-83 to R-86, three economy failure patterns (0.1.47)
- because: user request (general lessons from the Arvum Electrum OSRS harvest, 2026-11-20; each measured in that game's simulations)
- files: kb/review-rubric-more.md (R-83 to R-86), kb/review-rubric.md (How to run 11, Related), kb/balance-and-economy.md (Failure patterns), kb/INDEX.md, tests/test_ldw.py (KbSectionsTest)
- R-83 round trip that prints money, R-84 rounding eats small bonuses, R-85 shared resource with no claim, R-86 disasters with no spacing; failure patterns add the round trip, the remainder and a morale floor. Triggers unchanged, so evals were not re-run.


Entries 0.1.46 and older are in [ai-docs/changelog-archive.md](../../ai-docs/changelog-archive.md), moved out to keep the installed folder small.
