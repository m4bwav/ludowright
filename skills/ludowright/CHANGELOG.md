# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

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
