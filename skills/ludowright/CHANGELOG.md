# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

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
- because: user request (HANDOFF Next 3, gaps logged after the 2026-10-29 SpaceDeckBuilder2 review)
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
- because: L-20261029-2 (user reaction to the SpaceDeckBuilder2 review)
- files: references/review.md (steps 2 and 7), kb/review-rubric.md (R-53), scripts/ldw.py (validator, md), README contract
- Review step 2 settles the game's stage; findings on designed-but-uncoded content carry `built: no|partial` and are reported after the flaws in what exists. New rubric item R-53. Contract 1.1 adds the optional `stage` and `built`; 1.0 files still validate.

### C-20261029-2 · 2026-10-29 · Description trimmed under 1024 chars
- skill-tidy ST005: the description was 1072 chars and some hosts drop longer ones. Cut 'sources and sinks', 'and questionnaires' and the 'how do I make my game better' trigger phrase (still covered by 'what's wrong with my game' and the improve route). Also added the salt-road fixture and outcome-3, outcome-4.
- because: skill-tidy lint

### C-20261029-1 · 2026-10-29 · Created as an evergreen unit
- because: user request
- files: SKILL.md, RESEARCH.md, LEARNINGS.md, evergreen.json (skills: also TESTS.md and evals/evals.json)
- Initial version. Tier `moderate`, interval 30d. See R-20261029-1 for the research basis; the first test run, for a skill, is logged in TESTS.md.
