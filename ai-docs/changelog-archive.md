# Changelog archive: ludowright

Entries from 2026-10-29 to 2026-11-26 (0.1.67 and older), moved out of the installed skill folder to keep it small. Newer entries: [skills/ludowright/CHANGELOG.md](../skills/ludowright/CHANGELOG.md).

### C-20261126-11 · 2026-11-26 · RPG book harvest 13: damage-over-time check, enemy variants, tier mix, return trips, influence games, half-blank decks (0.1.67)
- because: harvest: RPG book collection (New Twists on Familiar Monsters; Poisons; Manual of the Planes; Tome of Templates; Adventure Shorts; Trail of Tyranny; Draconomicon: Chromatic Dragons; Open Grave; paraphrased, book rules unverified)
- files: scripts/ldw.py (new `dot` command), tests/test_ldw.py, kb/balance-tables.md (dot), kb/game-ai-for-designers.md (Principles 36-37), kb/levels-and-space.md (43-47), kb/systems-and-loops.md (50-52), kb/uncertainty.md (41)
- Eleven principles in fresh wording and `ldw.py dot`, which gives expected ticks, damage and time for a damage-over-time effect and flags `NO-EXIT` and `TRAPPED`. Base-plus-modifier variants extend balance-and-economy 39 (parent and child rows) rather than repeat it. Triggers unchanged, so evals were not re-run.

### C-20261126-10 · 2026-11-26 · RPG book harvest 12: crafting economy check, command budgets, morale cascades, travel clocks (0.1.66)
- because: harvest: RPG book collection (Assassin Games, Wilderness Encounters; Autarch, Domains at War Battles; Autarch, Domains at War Campaigns; Dalagrath, Herbalism & Alchemy; paraphrased, book rules unverified)
- files: scripts/ldw.py (new `craft` command), tests/test_ldw.py, kb/balance-tables.md (craft), kb/balance-and-economy.md (Principles 56-62, How to apply table), kb/systems-and-loops.md (42-49), kb/uncertainty.md (40)
- Sixteen principles in fresh wording and `ldw.py craft`, which flags uncapped stacking multipliers, gathering with no per-session cap, high gather cadence, stock with no sink, and capped stacks past a power limit. Morale cascade kept apart from balance-and-economy 24 (absolute rout thresholds), which it extends. Triggers unchanged, so evals were not re-run.

### C-20261126-9 · 2026-11-26 · RPG book harvest 11b: risk-gated XP, capped quest rewards, loot on the enemy, tension rhythm, test dangerous cards first (0.1.65)
- because: harvest: RPG book collection (AD&D 2e Dungeon Master's Guide; 4e Dungeon Master for Dummies; ICRPG 2e Core; Kobold Guide to Board Game Design; paraphrased, book rules unverified)
- files: kb/balance-and-economy.md (Principles 52-55), kb/levels-and-space.md (42), kb/systems-and-loops.md (41), kb/playtesting.md (Principles 26)
- Seven short principles in fresh wording. Skipped as duplicates: progress hanging on one secret (narrative-design 7, bottleneck), readable enemy target order (game-ai-for-designers 11 and 19), HP is not a difficulty dial (systems-and-loops 33), greedy baseline bot (review-rubric-more R-73), rarity is not a power budget (balance-and-economy 31). Triggers unchanged, so evals were not re-run.

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

### C-20261120-4 · 2026-11-20 · Worldbuilding 10 to 14 and adapting block; rubric R-81, R-82; AI state explosion (0.1.46)
- because: user request (book round: Robbins, Microscope Explorer; Campos, Game Development Patterns with Godot 4 (Godot 4.3); book rules, unverified)
- files: kb/worldbuilding-and-lore.md (10 to 14, Adapting a co-made world), kb/review-rubric-more.md (R-81, R-82), kb/review-rubric.md (How to run 11, Related), kb/game-ai-for-designers.md (30), kb/INDEX.md, tests/test_ldw.py (KbSectionsTest)
- Adds focus rounds with legacies, setup-only category vetoes, concept setup lists with a change axis, the picture-it test with reasoned tone labels, stuck prompts, and six logged moves for adapting a co-made world. R-81 flags a quest whose stakes are an outcome players already know (railroaded player covers lost choice, not this). R-82 flags buff stacks with order-dependent results, no single removal or one shared duration. Item 30 splits a combined state machine into parallel families. Changelog 0.1.44 and 0.1.45 archived first. Triggers unchanged, so evals were not re-run.

### C-20261120-3 · 2026-11-20 · `ldw.py stop`: stop-or-continue check; uncertainty 32 to 34 (0.1.45)
- because: user request (technique harvest of a 2015 Twine web game, Seedship; source read and played, no licence, so ideas only, described fresh, no code, text or assets copied)
- files: scripts/ldw.py (stop), tests/test_ldw.py (StopTest), kb/balance-tables.md (stop), kb/uncertainty.md (32 to 34), kb/INDEX.md, references/balance.md, SKILL.md (routing row, step 4)
- New `stop` command scores fixed settle thresholds for a loop where moving on costs condition the payoff depends on, with an optional noisy mode where damage hides readings. Flags FIRST-IS-BEST, NEVER-STOP, NO-COST, FLAT, else TENSE. Three kb principles: attrition spread over named subsystems, damage that blinds as well as weakens, event deck pacing and named endings. Installed folder now 303 KB (yellow). Triggers unchanged, so evals were not re-run.

### C-20261120-2 · 2026-11-20 · Rubric R-80 no outcome preview; R-39 covers irreversible single-click choices (0.1.44)
- because: user request (technique harvest of a web card battler, source tianlinx/spire-echoes on GitHub, played and measured; ideas only, described fresh, no code, text or assets copied)
- files: kb/review-rubric.md (R-39, How to run 11, Related), kb/review-rubric-more.md (R-80), kb/INDEX.md, tests/test_ldw.py (rubric range)
- R-39 now also flags a choice that cannot be taken back (route node, event option, reward pick) committed on a single click, and names the select-then-confirm fix and its one-click cost. R-80 flags a targeted action with no forecast of damage and health before and after while aiming. Two older entries moved to ai-docs/changelog-archive.md to keep the installed folder at 300 KB. Triggers unchanged, so evals were not re-run (as for R-69 to R-79).

### C-20261120-1 · 2026-11-20 · ldw.py ramp: difficulty ramp check (0.1.43)
- because: user request (technique harvest of an Apache-2.0 web arcade game, source luizbizzio/scandeck on GitHub: one spawn interval shrinks 6% per point to a floor, one fall speed grows every frame with no cap; method described fresh in our words, no code copied; source cited in the harvest notes)
- files: scripts/ldw.py (ramp, cmd_ramp, ramp_rows), kb/balance-tables.md (ramp), kb/balance-and-economy.md (command table), references/balance.md (step 1), SKILL.md (where the balance and pacing tools live), kb/INDEX.md, tests/test_ldw.py (RampTest), README.md
- Adds `ldw.py ramp TABLE [--steps N] [--json]` for formula ramps (base with factor or add, floor, cap, per, step_seconds) and step -> value tables: values at checkpoints, last/first ratio, and the flags UNCAPPED, FLOOR@n, CAP@n and FLAT-EARLY. Changelog entries 0.1.35 to 0.1.40 moved to ai-docs/changelog-archive.md and research entries R-20261029-1 to -6 to ai-docs/research-archive.md to keep the installed folder under 300 KB.

### C-20261119-2 · 2026-11-19 · Rubric R-69 to R-79 from five design and GM books; encounter, playtest, fudge, abduction and card-family notes (0.1.42)
- because: user request (book round 6: Selinker (ed.), Kobold Guide to Board Game Design, 2011; Baur, Kobold Guide to Gamemastering; Macris, Arbiter of Worlds; Runehammer, ICRPG Core; Parlett, Penguin Book of Card Games; book rules, unverified; proposed IDs renumbered after R-68)
- files: kb/review-rubric-more.md (R-69 to R-79), kb/review-rubric.md (How to run 11, Related), kb/INDEX.md, kb/levels-and-space.md, kb/playtesting.md, kb/uncertainty.md, kb/procgen.md (How to apply each), kb/design-drills.md (7), README.md, tests/test_ldw.py (KbSectionsTest)
- Adds early knockout, endless endgame, kingchooser grades, forced reverse, featured content bypassed, free rest, failable must-know, health sponge, identical retry, arbitrary death and expendable-piece AI, plus Timer-Threat-Treat rooms, a distance gradient, first-plays and extreme-bot playtests, the fudge test, an abduction pass and a mechanism family menu.

### C-20261119-1 · 2026-11-19 · Shaping verb against a visible target; staged stuck-hints (0.1.41)
- because: user request (technique harvest from a commercial web platformer demo; ideas only, described fresh, no code, text or assets copied; one game, unverified beyond it)
- files: kb/core-loops-and-goals.md (Shaping verb against a visible target), kb/ux-and-the-brain.md (Staged stuck-hints), kb/INDEX.md, tests/test_ldw.py (KbSectionsTest)
- Adds terrain shaping as a core verb with a continuous error score between forgiving thresholds and several input routes, and a per-beat hint plan that escalates wait, hand, outline, then text, with touch and keyboard wording.

### C-20261118-5 · 2026-11-18 · Question-driven play: powers, review recharge, readable foes, pacing (0.1.40)
- because: user request (studyquest list 3 field lessons, PRs #82-#91; one child playtester, unverified beyond that game)
- files: kb/learning-games.md (Question-driven play)
- Adds six bullets: spells and class moves still cost a question, abilities recharge by review not timers, foes with readable moves and damage shown as a sum, spread and hidden encounters, fixed hash-picked villager quests, message debounce and cap.

### C-20261118-4 · 2026-11-18 · Installed folder under the size line: dev-only material moved out (0.1.39)
- because: user request (installed skill folder was 311 KB against the 300 KB green line in scripts/budget.py)
- files: evals/fixtures (moved from skills/ludowright/evals/fixtures to the repository root; fixture.sh paths and the evals.json note updated), TESTS.md (runs T-20261029-1 to T-20261030-7 moved to ai-docs/tests-archive.md), ai-docs/changelog-archive.md (entries 2026-11-14 to 2026-11-17 moved out)
- No kb, reference or script text changed; the folder is now 285 KB. A scan for repeated sentences across kb files found one shared hand-off line and nothing worth merging.

### C-20261118-3 · 2026-11-18 · Story beats on the progress number, per-knower facts, verifiable runs, hot-reloaded tuning file (0.1.38)
- because: user request (technique-harvest repo round: voidstruck by vitaminclaude, PolyForm Strict, ideas only; spookery by legend-of-alan, agent and protocol crates MIT, engine ideas only; GPU-Bandits by sloppysteaks69, no licence, ideas only; all written fresh, no code copied)
- files: kb/narrative-design.md (Story keyed to progress, and who knows what), kb/uncertainty.md (Verifiable runs), kb/balance-and-economy.md (One tuning file, hot-reloaded), kb/INDEX.md
- Adds beats keyed to one progress number versus a quest graph, facts stored with their knowers so an AI GM sees only its character's view, seeded dice with a hash-chained replay journal, and one hot-reloaded tuning file with review checks for each.

### C-20261118-2 · 2026-11-18 · Narrative design kb file; flow channel; content lifespan and treadmill moves; dead-hand fix (0.1.37)
- because: user request (adopted technique-harvest book round 21: Heussner and others, The Game Narrative Toolbox, 2nd ed., ch. 5 and 9; Csikszentmihalyi, Flow, 1990, ch. 3 and 4; Kramarzewski, Practical Game Design, 2018, Content lifespan and Managing content treadmill; Brookes, Card Games, Oh hell and Beggar my neighbour; book rules, unverified)
- files: kb/narrative-design.md (new), kb/INDEX.md, SKILL.md (routing row), kb/ux-and-the-brain.md (Principles 24-25), kb/production-and-scope.md (Principles 26-27), kb/uncertainty.md (Principle 31)
- Adds quest structure, branching and story playtest checks, the flow conditions and rising channel, a content lifespan table and four cheaper moves than new content for live games, and exact-bid scoring as a fix for dead hands with a no-decision baseline.

### C-20261118-1 · 2026-11-18 · Learning games: question-driven play (battles, talks, bosses, crafting) (0.1.36)
- because: user request (lessons from building a study RPG's battles, bosses, dungeons, crafting and meals; practice from one game, unverified beyond it)
- files: kb/learning-games.md (Question-driven play)
- Adds one-question turns with a short cap, a talk skin on the same engine, bosses as delayed retests, and crafting that never skips a mastery gate.

### C-20261117-1 · 2026-11-17 · Learning games: motivator and blocker split, fair restarts, session fit, model fidelity; procgen: learned generators and degenerate quality (0.1.35)
- because: user request (adopted technique-harvest changes from Augmented Reality Games II, 2019, ch. 1, 2, 7, and Guzdial, Snodgrass and Summerville, Procedural Content Generation via Machine Learning, 2nd ed., ch. 4; book rules, unverified; the success band was already item 10 and the runaway weighted-sum item covers a different failure, so neither was repeated)
- files: kb/learning-games.md (Review block 12-15, Child and older players), kb/procgen.md (Principle 23, Failure patterns), ai-docs/changelog-archive.md (2026-11-14 entries 1 to 4 moved out)
- Adds a per-feature motivates-or-blocks check, a no-restart-from-start rule, session length and real-world use, a fidelity check for teaching simulations, one line on older players, and whole-level splits, a held-out target set, a two-ended temperature test and the cheapest-maximum check for generator metrics.

### C-20261114-5 · 2026-11-14 · Worldbuilding and lore kb file; rubric R-67 no escape valve, R-68 optional authority (0.1.34)
- because: user request (adopted technique-harvest changes from Robbins, Microscope, 2011; book rules, unverified; R-67 checked against uncertainty.md 19, which covers kingmaking only)
- files: kb/worldbuilding-and-lore.md (new), kb/review-rubric-more.md (R-67, R-68), kb/review-rubric.md (How to run 11, Related), kb/INDEX.md, SKILL.md (routing row)
- Adds bookends, an exceptions list, zoom levels, outcome-first entries, three canon checks and an open-gap ledger for lore, and two multiplayer review items for trapped players and loud-player authority.

### C-20261114-4 · 2026-11-14 · Fundamental tension, five-phase gate, playtest result triage; rubric split for size (0.1.33)
- because: user request (adopted technique-harvest changes from Gary, Think Like a Game Designer, ch. 9 to 13; book rules, unverified; random reward schedules not adopted); budget yellow on review-rubric.md
- files: kb/core-loops-and-goals.md (Fundamental tension), kb/production-and-scope.md (How to apply 13), kb/playtesting.md (How to apply 10-12), kb/review-rubric.md (How to run 11, Related), kb/review-rubric-more.md (new: R-53 to R-66 moved unchanged), kb/INDEX.md, references/review.md
- Adds a one-sentence tension with per-mechanic ratings, the five-phase gate that flags later-phase work before the engine is proven, and forgotten-rule, instinct and works/fails/mixed checks; the rubric now spans two files so the largest kb file is back under green.

### C-20261114-3 · 2026-11-14 · Procgen: constrain early, one exclusion system, backtrack, log fallbacks (0.1.32)
- because: user request (adopted technique-harvest changes from Short and Adams, eds., Procedural Storytelling in Game Design, 2019, ch. 2 and 22; book rules, unverified)
- files: kb/procgen.md (Principle 22, Failure patterns), ai-docs/changelog-archive.md (entries to 2026-11-13 moved out of the skill folder)
- Adds constraint order, shared exclusion tags, backtracking and fallback counts for generated entities, and asks whether a rule change fixes a generator fault.

### C-20261114-2 · 2026-11-14 · Playtest explain-back and multi-day tests for habit games (0.1.31)
- because: user request (adopted technique-harvest changes from Ferro, Gamification with Unity 5.x, 2016; book rules, unverified)
- files: kb/playtesting.md (Principle 22), kb/learning-games.md (Review block 11), ai-docs/changelog-archive.md (entries to 2026-11-10 moved out of the skill folder)
- Adds an explain-back check after play and a 5 to 30 day test window for habit and study games; old changelog entries moved to keep the folder under budget.

### C-20261114-1 · 2026-11-14 · Learning games: objective events, observe-assess-respond, rules first, calibrated AI judge (0.1.30)
- because: user request (adopted technique-harvest changes from Mangos and Ferraro, eds., AI and Gamification Technologies for Complex Work Simulation and Training; adult workplace and military training, child use unverified; book rules, unverified)
- files: kb/learning-games.md (Review block 8-10), kb/review-rubric.md (R-62), kb/ai-as-design-tool.md (Failure patterns)
- Adds a goal-has-an-event check, an observe-assess-respond checklist, rules-before-ML with between-session changes for children, and calibration of an AI judge against human labels.

### C-20261113-5 · 2026-11-13 · Gamify: no devaluation, spend path, bottom tier, loophole pass, campaign or endless (0.1.29)
- because: user request (adopted technique-harvest changes from Burke, Gamify, 2014; book rules, unverified)
- files: kb/balance-and-economy.md (Principle 34), kb/core-loops-and-goals.md (Principle 21)
- Adds a rule against devaluing earned rewards, a spend path for every currency, a bottom-tier check for competition, a pre-launch loophole pass, and campaign versus endless (scripted versus emergent) as a design choice.

### C-20261113-4 · 2026-11-13 · Card games: rarity, deck rules, cost line, draw odds (0.1.28)
- because: user request (adopted technique-harvest changes from Bycer, Game Design Deep Dive: Trading and Collectible Card Games, 2024, and Calculating Chance: Card and Casino Games; card rules are book rules, unverified; the draw maths is checked by golden tests)
- files: kb/balance-and-economy.md (Principles 31-33; How to apply table), scripts/ldw.py (`draw`), tests/test_ldw.py (DrawOdds)
- Adds rarity as complexity, a deck-rule list, resource models, the vanilla cost line, the counter-cost check, the free-draw flag and draws without replacement, plus `ldw.py draw` for at-least-k copy odds. Entries before 2026-11-01 moved to the repo's ai-docs to keep the skill folder small.

### C-20261113-3 · 2026-11-13 · Emotional Design and Gamification by Design: feel levels, rewards, leaderboards (0.1.27)
- because: user request (adopted technique-harvest changes from Norman, Emotional Design, 2004, and Zichermann and Cunningham, Gamification by Design, 2011; book rules, unverified)
- files: kb/ux-and-the-brain.md (Principles 14, 22, 23; Dark patterns), kb/balance-and-economy.md (Principles 27-30)
- Adds a three-level and four-pleasure feel lens, fear with a safety signal and a keepsake, confusion on purpose as a dark pattern, rollback-first exploit policy, the status-access-power-stuff ladder, five point kinds with ordered tier names (the rubric had no level-order rule), leaderboard patterns and a one-player test for social features.

### C-20261113-2 · 2026-11-13 · Lean Game Development: outcome plan, one new thing, removal test, triage (0.1.26)
- because: user request (adopted technique-harvest changes from Boeira, Lean Game Development, Apress 2017; book rules, unverified)
- files: kb/playtesting.md (How to apply 1 and 8), kb/production-and-scope.md (How to apply 11 and 12)
- The one-page plan lists outcomes and their actions before a test; a bad result is triaged as works-not-fun or fun-not-playable before fixes; prototypes add one new thing; a removal test decides milestone membership.

### C-20261113-1 · 2026-11-13 · Book harvest: learning games, drills, loops and arcs (0.1.25)
- because: user request (adopted technique-harvest changes from Lockhart and Lang, Kapp, Kim et al., Chou, Werbach and Hunter, Lost Garden, GDC Vault)
- files: kb/core-loops-and-goals.md (Loops versus arcs), kb/uncertainty.md (principles 29-30), kb/learning-games.md (new), kb/design-drills.md (new), kb/review-rubric.md (R-62 to R-66), kb/INDEX.md
- Adds the strip-the-arcs test and skill chains (skill atoms from secondary accounts), input versus output randomness with reducing tools, a learning-game review block, the four-phase audit, an early-strategy balance check, a drill catalogue and a WCAG-cited accessibility check. The rubric file is now yellow on the size budget.

Older entries (2026-10-29 to 2026-11-10) are in the repository at `ai-docs/changelog-archive.md`.

### C-20261110-1 · 2026-11-10 · harvest.json: technique-harvest targets for this unit
- because: user request 2026-11-10: plugins store their own technique-harvest targets (evergreen 1.1.0 harvest.json)
- files: harvest.json (new)
- Data file only; no skill text or version changed.

### C-20261106-1 · 2026-11-06 · Sfxwright, when installed (0.1.24)
- because: user request
- files: SKILL.md (sfxwright note)
- Hand sound effects to sfxwright when present and read its sounds.json; this plugin's own steps stay as the fallback.

### C-20261104-2 · 2026-11-04 · Pink, Drive: which rewards hurt (0.1.23)
- because: user request (pre-approved book changes)
- files: kb/ux-and-the-brain.md (principle 12, Where the books disagree)

The file said rewards help or hurt by type without naming the types; it now asks four questions. Checked against Cerasoli et al. 2014 and the blood-donation paper, whose effect held only for women.

### C-20261104-1 · 2026-11-04 · Omagari, Arcade Game Typography: text size is physical (0.1.22)
- because: user request (pre-approved book changes)
- files: kb/ux-and-the-brain.md (principle 21, failure pattern)

Text legibility had no rule in the UX file. Drawing pixel fonts goes to pixelwright.

### C-20261101-10 · 2026-11-01 · Morales, Grokking Deep RL: one agent per task, bandits for one-step choices, gamma and reward density as dials (0.1.21)
- because: user request (pre-approved book changes)
- files: kb/ai-as-design-tool.md ("When reinforcement learning is worth it", sources line and items 11-13)
- One trained agent per task since skills do not transfer; shop and difficulty picks are bandits (optimistic init or decaying epsilon-greedy, judged by regret); gamma and dense or sparse reward change play style, so playtest each.

### C-20261101-9 · 2026-11-01 · Graesser and Keng, Foundations of Deep RL: random-agent baseline, reward-hacking replays, reward signs (0.1.20)
- because: user request (pre-approved book changes)
- files: kb/ai-as-design-tool.md ("When reinforcement learning is worth it", items 8-10)
- Beat a random agent before trusting a curve; log rewards and replay extreme episodes, patching exploits as design bugs; positive/zero/negative rewards with no extremes, side scores only as shaping under the end condition.

### C-20261101-8 · 2026-11-01 · Lapan, Deep RL Hands-On: when reinforcement learning is worth it (0.1.19)
- because: user request (pre-approved book changes)
- files: kb/ai-as-design-tool.md (new block "When reinforcement learning is worth it")
- Reward per step not HUD score, demonstrations first, many headless env copies, PPO over several seeds, curiosity for sparse goals, checkpoint round-robins for self-play, learned preference rewards in rounds.

### C-20261101-7 · 2026-11-01 · Lambshead, One-hour Ancient and Medieval Skirmish Wargames: draw-count odds, random turn ends, absolute rout thresholds, unit budgets, zones of control (0.1.18)
- because: user request (pre-approved book changes)
- files: kb/uncertainty.md (Principles 26 to 28), kb/balance-and-economy.md (Principles 24 to 26), kb/production-and-scope.md (Principles 23 to 25), kb/levels-and-space.md (Principles 22, 23)
- Odds set by cards drawn, random turn ends and the reshuffle trade-off; absolute loss thresholds, escalating repeat-action costs and inverse stat axes; unit-count budgets, a one-sheet fast-play test and droppable rules; zones of control and scenarios that break a degenerate scrum.

### C-20261101-6 · 2026-11-01 · Unity 2018 AI Cookbook (Palacios) shared path costs and N-gram prediction (0.1.17)
- because: user request (pre-approved book changes)
- files: kb/game-ai-for-designers.md (Principles 28, 29)
- Chasers that raise each other's path costs read as flanking; an N-gram predictor punishes habits only when announced, capped and backed off while data is thin.

### C-20261101-5 · 2026-11-01 · Beginning Game AI with Unity (Cossu) player verbs that feed AI senses (0.1.16)
- because: user request (approved the ludowright row of the Cossu learnings note)
- files: kb/game-ai-for-designers.md (Principle 27)
- Lures that write into a guard's last-known position make stealth AI something the player plays; each needs a readable reaction and a cap.

### C-20261101-4 · 2026-11-01 · AI for Games 3e (Millington) in game AI, procgen and review (0.1.15)
- because: user request (approved the five ludowright rows of the AI for Games learnings note)
- files: kb/game-ai-for-designers.md (Principles 22 to 26, How to apply step 7, Failure patterns, Level-AI handoff checklist), kb/procgen.md (Principle 21, Failure patterns), references/review.md (step 3, AI depth sweep)
- Trees weak at interrupts, playable-first enemies, path cost per unit type, data over code, per-layer AI rates; cheaper techniques before costly ones; missing alarm beat, unguarded scripts and untested learners; level-AI checklist; seed streams per subsystem and capped reject loops; an AI-depth review sweep. Principles 2 and 3 (perception window, behaviour change) were already there.

### C-20261101-3 · 2026-11-01 · Generative Deep Learning 2e (Foster) world models as prototype worlds (0.1.14)
- because: user request (approved the ludowright row of the Generative Deep Learning learnings note)
- files: kb/ai-as-design-tool.md (Principle 21)
- Generative world models as quick prototype or playtest worlds, with exploits of the dream verified in the real build and a dated availability note for Genie 3.

### C-20261101-2 · 2026-11-01 · Game Engine Architecture (Gregory, 2014) in the rubric, feel, production and playtesting (0.1.13)
- because: user request (approved the Changes table of the Game Engine Architecture learnings note, seven ludowright rows)
- files: kb/review-rubric.md (R-58 to R-61), kb/feel-handoff.md (Failure patterns), kb/production-and-scope.md (Principle 22), kb/playtesting.md (Principle 21), README.md (61-item rubric)
- Frame-rate-bound play, raw input, unplannable physics and objectives welded to a level as rubric items; transitions as a reviewed table; selective data-driving with a wait budget; input and seed recording for playtests.

### C-20261101-1 · 2026-11-01 · Play to Learn (Boller and Kapp, 2017) in playtesting, balance and goals (0.1.12)
- because: user request (approved the Changes table of the Play to Learn learnings note, eleven kb rows)
- files: kb/playtesting.md (Principles 17 to 20, How to apply step 4, Where the books disagree), kb/balance-and-economy.md (Principles 21 to 23), kb/core-loops-and-goals.md (Principle 20, Failure patterns)
- Pass mark set before testing, hours per tester, no tutorial before testing, before-and-after learning check, closing questions, paper versus digital prototypes; scoring rules, a scoring spreadsheet check and achievement design; game goal apart from the outcome, wrong-skill mechanics and luck-decided wins.

### C-20261031-2 · 2026-10-31 · The Gamer's Brain 2e (Hodent, 2026) in UX and playtesting (0.1.11)
- because: user request (approved the Changes table of The Gamer's Brain learnings note, nine kb rows)
- files: kb/ux-and-the-brain.md (Principles 18 to 20, Dark patterns to avoid, Failure patterns, citations note), kb/playtesting.md (Principle 16, How to apply steps 2, 4 and 7)
- Dark-pattern sort and pressure test, lock before key, tutorial text only until done, reappraisal after loss, playtest method menu, goal and reward questions, issue log, LLM-written survey answers.

### C-20261031-1 · 2026-10-31 · Press Reset (Schreier) principles in production and procgen (0.1.10)
- because: user request (approved the Changes table of the Press Reset learnings note, five kb rows)
- files: kb/production-and-scope.md (Principles 19 to 21, Failure patterns), kb/procgen.md (Principles 20)
- Small teams in one room over a headcount ramp, a named closer, planned life after launch with a deliberate final update, self-imposed crunch as a failure pattern, and random content as a budget lever.

### C-20261030-7 · 2026-10-30 · Spelunky principles as kb principles in ten files (0.1.9)
- because: user request (approved the Changes table of the Spelunky learnings note, ten kb rows)
- files: kb/procgen.md, kb/systems-and-loops.md, kb/uncertainty.md, kb/levels-and-space.md, kb/core-loops-and-goals.md, kb/playtesting.md, kb/production-and-scope.md, kb/game-ai-for-designers.md (Principles), kb/balance-tables.md (ev), scripts/ldw.py (VERSION, stale at 0.1.6)
- 0.1.7 added Yu as failure patterns; this adds the positive rules: critical-path-only guarantee, fixed secrets, one shared ruleset, timer and seeded daily runs, difficulty as pacing, layered goals, feedback as symptoms, finishing, cheap state machines, round-number spawn odds per tier.

### C-20261030-6 · 2026-10-30 · Drop eval run output committed by mistake (0.1.8)
- because: budget check red on 0.1.7 (installed skill folder 719 KB, limit 600)
- files: skills/ludowright/evals/results/ (removed, now ignored), .gitignore
- 0.1.7 shipped a local eval run's report by accident; this removes it. Same skill content as 0.1.7.

### C-20261030-5 · 2026-10-30 · Spelunky (Yu) distilled into the kb; rubric R-54 to R-57 (0.1.7)
- because: user request (Mark added Derek Yu, Spelunky, to the reading pile)
- files: kb/procgen.md (template-grid generator, failure patterns), kb/levels-and-space.md, kb/production-and-scope.md, kb/uncertainty.md (failure patterns), kb/review-rubric.md (R-54 to R-57), README.md (57-item rubric)
- Notes in books/plugin-learnings/round3-game-design/yu-spelunky.md. New checks: a generator path that needs consumables, friction read as difficulty, signposted or dominant secrets, seeded runs whose loot is rolled on open.

### C-20261030-4 · 2026-10-30 · Reviewer gaps from the first real-game run (0.1.6)
- because: user request (HANDOFF Next 3, gaps logged after the 2026-10-29 private deck-builder game review)
- files: scripts/ldw.py (curve --costs), kb/balance-tables.md (curve), references/review.md (step 2), references/improve.md (step 4)
- The real-game review had to declare multi-resource costs by hand, missed that its doc and code ran on different clocks, and saw improve ids renumbered. `curve --costs gold:1,wood:0.5` (or a "costs" object in the table) folds several currencies into one cost at stated rates; review step 2 converts every counted rate to one clock and unit; improve ids are given once in rank order and never renumbered.

### C-20261030-3 · 2026-10-30 · Contract in its own reference; batched reads (0.1.5)
- because: T-20261030-5
- files: references/findings-contract.md (new, copy of the README section), SKILL.md (step 0, contract), references/review.md (steps 1 and 6)
- A traced run spent turns on a Grep and a full README read to find the contract schema, and read evergreen.json and the fixture files one turn each. The schema now sits in references/findings-contract.md; step 0 and review step 1 ask for one turn of parallel reads; step 6 runs tables, validate and md in one shell call, or writes JSON then md without a shell. Turns and cost did not fall in the A/B; kept for the shorter path in real runs.

### C-20261030-2 · 2026-10-30 · Review sweeps and an intent check from the books (0.1.4)
- because: T-20261030-3, user request ("improve it into usefulness with the learnings from the books")
- files: references/review.md (step 3 sweeps, new step 3b), evals/fixtures/ember-market, evals/cases/outcome-6, outcome-7, evals/evals.json
- Review step 3 now runs four sweeps a rubric walk misses: promises to the rows that deliver them (Wyman), trigger pairs for self-feeding chains (Adams and Dormans, Sylvester), a cost curve over every like-kind table with dominated pairs (Schreiber), and EV on every gamble (Elias et al., Costikyan). New step 3b checks the designer's stated intent, stopping mechanism and evidence before filing a loop or outlier: a defended, bounded dynamic is a note at most, unless its own numbers contradict it (win share against one in the player count, sample size).

### C-20261030-1 · 2026-10-30 · Keep test state out of replies; outcome-2 grader judges substance (0.1.3)
- because: T-20261030-1 (the skill told the user its own eval was failing), T-20261030-2
- files: SKILL.md (evergreen state line), evals/cases/outcome-2/graders/judge.md
- A non-empty `tests.failing` now means tune after the task and say nothing to the user. The outcome-2 grader no longer asks for the words "single capped sink" or "economy-leak"; any reply that says gold piles up because spending is capped, and names the file, passes.

### C-20261029-5 · 2026-10-29 · R-53: a gap blocking the advertised win ranks first (0.1.2)
- because: T-20261029-3 (outcome-5 judge), T-20261029-4, owner ruling 2026-10-29
- files: references/review.md (step 7), kb/review-rubric.md (R-53), LEARNINGS.md (L-20261029-2)
- A designed-but-uncoded piece that blocks the win or core loop the game advertises now leads the report; other unbuilt gaps still follow the flaws in what exists. The reply now names the stage and marks unbuilt findings, because the judge reads only the reply, not the findings file.

### C-20261029-4 · 2026-10-29 · No-shell fallback, findings first, contract 1.1 in SKILL.md; lantern-keep fixture (0.1.1)
- because: L-20261029-1 (T-20261029-2), L-20261029-2
- files: SKILL.md (LDW line, findings contract, Output), evals/fixtures/lantern-keep, evals/cases/outcome-5
- When no shell is allowed the skill says so in one line, counts by hand only what a finding needs and still writes the file. The reply leads with the findings and puts caveats last. SKILL.md now names contract 1.1 with `stage` and `built`. New prototype fixture with an uncoded win-path relic and an uncoded flavour relic tests R-53 (outcome-5).

### C-20261029-3 · 2026-10-29 · Stage and built: separate "not built yet" from "built wrong"; findings contract 1.1
- because: L-20261029-2 (user reaction to the private deck-builder game review)
- files: references/review.md (steps 2 and 7), kb/review-rubric.md (R-53), scripts/ldw.py (validator, md), README contract
- Review step 2 settles the game's stage; findings on designed-but-uncoded content carry `built: no|partial` and are reported after the flaws in what exists. New rubric item R-53. Contract 1.1 adds the optional `stage` and `built`; 1.0 files still validate.

### C-20261029-2 · 2026-10-29 · Description trimmed under 1024 chars
- skill-tidy ST005: the description was 1072 chars and some hosts drop longer ones. Cut 'sources and sinks', 'and questionnaires' and the 'how do I make my game better' trigger phrase (still covered by 'what's wrong with my game' and the improve route). Also added the salt-road fixture and outcome-3, outcome-4.
- because: skill-tidy lint

### C-20261029-1 · 2026-10-29 · Created as an evergreen unit
- because: user request
- files: SKILL.md, RESEARCH.md, LEARNINGS.md, evergreen.json (skills: also TESTS.md and evals/evals.json)
- Initial version. Tier `moderate`, interval 30d. See R-20261029-1 for the research basis; the first test run, for a skill, is logged in TESTS.md.
