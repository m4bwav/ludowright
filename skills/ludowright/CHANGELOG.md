# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

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
