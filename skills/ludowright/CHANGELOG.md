# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

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

 · 2026-11-10 · harvest.json: technique-harvest targets for this unit
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

Older entries (2026-10-29 to 2026-10-31) are in the repository at `ai-docs/changelog-archive.md`.
