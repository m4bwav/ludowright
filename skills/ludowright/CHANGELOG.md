# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-20261119-1 · 2026-11-19 · Shaping verb against a visible target; staged stuck-hints (0.1.41)
- because: user request (technique harvest from a commercial web platformer demo; ideas only, described fresh, no code, text or assets copied; one game, unverified beyond it)
- files: kb/core-loops-and-goals.md (Shaping verb against a visible target), kb/ux-and-the-brain.md (Staged stuck-hints), kb/INDEX.md, tests/test_ldw.py (KbSectionsTest)
- Adds terrain shaping as a core verb with a continuous error score between forgiving thresholds and several input routes, and a per-beat hint plan that escalates wait, hand, outline, then text, with touch and keyboard wording.

### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

### C-20261119-2 · 2026-11-19 · Rubric R-69 to R-79 from five design and GM books; encounter, playtest, fudge, abduction and card-family notes (0.1.42)
- because: user request (book round 6: Selinker (ed.), Kobold Guide to Board Game Design, 2011; Baur, Kobold Guide to Gamemastering; Macris, Arbiter of Worlds; Runehammer, ICRPG Core; Parlett, Penguin Book of Card Games; book rules, unverified; proposed IDs renumbered after R-68)
- files: kb/review-rubric-more.md (R-69 to R-79), kb/review-rubric.md (How to run 11, Related), kb/INDEX.md, kb/levels-and-space.md, kb/playtesting.md, kb/uncertainty.md, kb/procgen.md (How to apply each), kb/design-drills.md (7), README.md, tests/test_ldw.py (KbSectionsTest)
- Adds early knockout, endless endgame, kingchooser grades, forced reverse, featured content bypassed, free rest, failable must-know, health sponge, identical retry, arbitrary death and expendable-piece AI, plus Timer-Threat-Treat rooms, a distance gradient, first-plays and extreme-bot playtests, the fudge test, an abduction pass and a mechanism family menu.

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
