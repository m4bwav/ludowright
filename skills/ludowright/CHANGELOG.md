# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

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

