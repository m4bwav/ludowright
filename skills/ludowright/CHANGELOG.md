# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

### C-20261126-8 · 2026-11-26 · RPG book harvest 11: player-set risk, reward tiers, second resources, settlement logic (0.1.64)
- because: harvest: RPG book collection (ICRPG Magic; ICRPG Worlds; ICRPG Vigilante City; ICRPG Altered State; Kobold Campaign Builder: Cities and Towns; paraphrased, book rules unverified)
- files: kb/uncertainty.md (Principles 37-39), kb/systems-and-loops.md (35-40), kb/balance-and-economy.md (49-51), kb/levels-and-space.md (40-41), kb/worldbuilding-and-lore.md (Principles 16-17)
- Sixteen short principles in fresh wording. Skipped as a duplicate: show the rules before punishing (levels-and-space 9, teach before test). Triggers unchanged, so evals were not re-run.

### C-20261126-7 · 2026-11-26 · RPG book harvest 10: rewarding interaction, setup spacing, readable systems, branching shapes, rationed signals (0.1.63)
- because: harvest: RPG book collection (Kobold Guide to Dungeons; Kobold Guide to Roleplaying; Weis, Kobold Guide to Plots & Campaigns; Kobold Guide to Gamemastering read but added nothing new; paraphrased, book rules unverified)
- files: kb/levels-and-space.md (Principles 36-39), kb/narrative-design.md (Principles 10-13), kb/systems-and-loops.md (34), SKILL.md and ldw.py version brought back in line with the manifest
- Nine short principles in fresh wording. Skipped as duplicates: rest that costs nothing (levels-and-space 32) and failure that changes state (uncertainty 35). Triggers unchanged, so evals were not re-run.

### C-20261126-6 · 2026-11-26 · RPG book harvest 9: non-kill objectives, two-axis difficulty, paced character turns; cleanups (0.1.62)
- because: harvest: RPG book collection (5e Dungeon Master's Guide 2014; ICRPG Master Edition; 3.5 Dungeon Master's Guide); cleanup items from the session 8 handoff
- files: kb/levels-and-space.md (Principles 35), kb/systems-and-loops.md (33), kb/narrative-design.md (Principles 9, How to apply renumbered), CHANGELOG.md (stray template heading removed)
- Three short principles in fresh wording, plus removal of a template heading a past harvest left in the log and a duplicate item number.

### C-20261126-5 · 2026-11-26 · RPG book harvest 8: encounter scripts, quest-structure flaws, graded climax, dice spread, content removal, task pools (0.1.61)
- because: harvest: RPG book collection (4e Dungeon Master's Guide; Advanced Gamemaster's Guide; Dungeon Master's Guide II; Fallout 2d20 GM Toolkit; paraphrased, book rules unverified)
- files: kb/levels-and-space.md (Principles 33-34), kb/narrative-design.md (Principles 7-8), kb/uncertainty.md (36), kb/systems-and-loops.md (31-32), kb/balance-and-economy.md (48)
- Eight short principles in fresh wording: encounter script with the four-point terrain test, graded climax after an attrition run, bottleneck, railroad, cluelessness and sidelining as plan flaws, no kill-count quests, narrower dice widening gaps at the extremes, removal breaking balance with rule changes failing toward the player, progress-pool tasks and reputation ladders. The railroad flaw is a plan check; the existing Railroaded player failure pattern stays the playtest symptom. Triggers unchanged, so evals were not re-run.

### C-20261126-4 · 2026-11-26 · RPG book harvest 7: loot fairness, reward ceilings, premise layers, fail forward, generator discipline (0.1.60)
- because: harvest: RPG book collection (Adventurers League DMG v2.0; Game Ideas collection with S. John Ross, The Big List of RPG Plots; Lankhmar Gamemaster's Guide; Gygax, AD&D Dungeon Masters Guide 1e; paraphrased, book rules unverified)
- files: kb/balance-and-economy.md (46-47), kb/narrative-design.md (7), kb/uncertainty.md (35), kb/procgen.md (27)
- Five short principles in fresh wording: co-op loot split with fixed reward ceilings, income against upkeep, premise plus twist with distinct hook and real layers, failed check as complication, and bounded table-driven generation with a separate placement record. Triggers unchanged, so evals were not re-run.

### C-20261126-3 · 2026-11-26 · RPG book harvest 6: traps, encounter tactics, base loops, enemy lessons, playtest forms (0.1.59)
- because: harvest: RPG book collection (Book of Challenges; Posner, A Goblin's Tale DMG; Campaign Planner collection; Campaign Creation Guide; Bill Webb, Book of Dirty Tricks; Fast Combats; an Inns supplement; GM Gems; 650 City; Panshin; paraphrased, book rules unverified)
- files: kb/levels-and-space.md (Principles 29-32), kb/systems-and-loops.md (28-30), kb/game-ai-for-designers.md (35), kb/playtesting.md (23-25), kb/procgen.md (26), kb/balance-and-economy.md (45), kb/production-and-scope.md (29)
- Fourteen short principles in fresh wording: trap anatomy, encounter tactics, crowd decay, rest pressure, base-management loop, failed craft as event, button-press check, one-lesson enemy, three-tier fight review, feedback form, idle-player check, generator filter, renewable stock, campaign walls and the one-fifth rut change. No ldw.py command for renewable stock yet. Triggers unchanged, so evals were not re-run.

### C-20261126-2 · 2026-11-26 · RPG book harvest 3: lore tied to present conflict, single-counter roster (0.1.58)
- because: harvest: RPG book collection (Kobold Guide to Worldbuilding; Bill Webb, Book of Dirty Tricks; paraphrased, book rules unverified)
- files: kb/worldbuilding-and-lore.md (15), kb/systems-and-loops.md (Failure patterns)
- Two short lines; the skill is near its size line. Triggers unchanged, so evals were not re-run.

### C-20261126-1 · 2026-11-26 · RPG book harvest 1: five-role arc, session prep, three failure patterns (0.1.57)
- because: harvest: RPG book collection (Johnn Four, 5 Room Dungeons; Shea, The Lazy Dungeon Master; paraphrased, book rules unverified)
- files: kb/levels-and-space.md (Principles 27-28, Failure patterns)
- Adds the five-role site arc laid over the critical path, prep-what-they-touch guidance, and the free setback, one-key puzzle and prep sunk cost failures. Triggers unchanged, so evals were not re-run.

### C-20261125-2 · 2026-11-25 · Live-play corrections: quota rows, capped resource waste, countdown pauses (0.1.56)
- because: harvest: live play of Luck be a Landlord, Pirates Outlaws and Wildfrost on 2026-11-25 corrected 0.1.55
- files: scripts/ldw.py (growth), kb/balance-tables.md (growth, quota), kb/balance-and-economy.md (44), tests/test_ldw.py (QuotaTest, GrowthTest)
- The quota test and docs tripled each payment; measured rent roughly doubles then grows by half while the window stretches, so the fixture is now an invented ladder of that shape (20/5, 45/5, 90/6, 140/6, 210/7). `growth` takes an optional resource `cap` with `refill`, `start` and `turns` and flags WASTED when refills spill past the cap (a reload at full ammo). Rule 44 now covers pausing a countdown for N ticks as well as adding turns. Triggers unchanged, so evals were not re-run.

### C-20261125-1 · 2026-11-25 · Steam harvest wave 2: `ldw.py growth`, `ldw.py quota`, intents, cost tier, countdowns (0.1.55)
- because: harvest: local game harvest 2026-11-25 (idea sources: Pirates Outlaws, Slay the Spire 2, Wildfrost, Luck be a Landlord; rules text and public play knowledge only, methods paraphrased, nothing copied)
- files: scripts/ldw.py (growth, quota), kb/balance-and-economy.md (41-44), kb/game-ai-for-designers.md (34), kb/balance-tables.md (growth, quota), tests/test_ldw.py
- New `growth` command projects deck size per stage against a target band and a capped resource's maker/spender ratio (BLOAT, OFF-BAND, NO-THIN, STARVED, FLOODED). New `quota` command checks rising payments with countdowns against an income ramp (TIGHT, LOOSE, CLIFF). Kb rules: thinning routes, a reward tier with a built-in cost, quota with countdown, visible adjustable countdowns with capped attachment slots, turn-based exact intents. Also brings SKILL.md and ldw.py back in line with the manifest version. Triggers unchanged, so evals were not re-run.

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
