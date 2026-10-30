# Handoff

Resume with `Execute ai-docs/plans/2026-10-29-ludowright-continue-prompt.md` (start the session in this folder).

## Current state (2026-10-29)
- Name ludowright (gamewright clashes with the publisher Gamewright and Gamewright Studio). Local repo only: creating the public repo was refused by the permission check; waits on Mark's OK. Nothing pushed.
- Built: one skill `skills/ludowright/` (SKILL.md router, references design/review/improve/balance, 12 kb topic files plus balance-tables and the 52-item review rubric, `scripts/ldw.py` with 13 tests), evergreen layer (tier moderate, next due 2026-11-28), repo set (README with findings contract 1.0, AGENTS, CLAUDE, Copilot pointer, LICENSE, SECURITY, CI, budget green), decision `ai-docs/decisions/2026-10-29-one-skill-and-budgets.md`.
- Beat: everscout beat `game-design` finished 2026-10-29: beat-check 0 errors, probe 19 ok 0 bad, 19 sources (7 engage), 69 entities, 25 questions. Next action there: first scan. Subreddit rules pages unread: read before any engagement.
- Evals: T-20261029-1 triggers 3/3 (baseline 0/3), decoys quiet. T-20261029-2: new harder fixture `salt-road` (reputation loop, dropped storm promise) with outcome-3 and outcome-4; outcome cases now seed fixtures via case.yaml + fixture.sh (`--scaffold`). Result 1/4 cases: Windows plugin eval refuses Bash, so ldw.py never ran and the skill arm lost on a last-message haiku judge (outcome-4 0/3 vs 3/3). Lesson L-20261029-1. Description trimmed to under 1024 chars (skill-tidy ST005, C-20261029-2).
- SpaceDeckBuilder2 review done (read-only), 13 findings + 10 improvements in `ai-docs/reviews/` (gitignored), both validate OK. Shown to Mark; waiting on his reactions. The reviewer's skill gaps are in the log entry for the review (no rubric item for "data written, code never built"; settle the game's clock and units before counting; cost curve on free-text effects and multi-currency costs; economy tool cannot model players who adapt; sim stops at XP not levels; improve md re-sorts by severity; Unity GUID refs unresolvable).
- Evergreen PR m4bwav/evergreen-protocol#34 (beat offer, plus the BEAT-line fix the live run found, L-044) waits on Mark. everscout 0.6.0 released.
- Reading notes: 27 files in `books/plugin-learnings/round3-game-design/`; partial reads listed in `ai-docs/log.md`.

## Next
1. Route Mark's reactions to the SpaceDeckBuilder2 review (evergreen-learn), together with the reviewer's skill gaps above.
2. Tune for L-20261029-1: when LDW cannot run, lead with the findings and one caveat line; switch the outcome graders to the saved findings file (`source: file`) or re-run the A/B with evergreen-tester where a shell exists. Run action-2. Then `evergreen.py worth skills/ludowright --record`.
3. Release once Mark OKs the public repo (still not created). Then the game-juice PR (Swink ch. 12-16).
