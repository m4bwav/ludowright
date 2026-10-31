# Handoff

Resume with `Execute ai-docs/plans/2026-10-29-ludowright-continue-prompt.md` (start the session in this folder).

## Current state (2026-10-31, session 15)
- evergreen PR m4bwav/evergreen#15 merged: `worth` now reports the mean grader score per arm with its own noise margin and counts a score gain beyond it. outcome-8 re-scored: 0.85 vs 0.65, margin 0.23, so still CUT (+20 inside 23). Five more runs an arm could clear it.
- T-20261030-8: harbor-yard quieter (playtest hints removed) and its Kraken defence fixed (it failed its own arithmetic). with 0.97, without 1.00. Breadth does not separate the arms; counted evidence (outcome-8) is the only measured edge.
- T-20261030-7: big breadth fixture harbor-yard (outcome-9, ten flaws over seven files plus a defended Kraken). with 0.94, without 0.97: breadth does not separate the arms. One skill run failed Kraken precision, unverified (no review kept).
- game-juice 1.3.0 released (PR m4bwav/game-juice#5, tag, zips, installed): juice-scan Step 2 classifies the feel (P-23) and lists inferred movement and rule properties (P-24, P-25); report header carries both. The Swink list in kb/feel-handoff.md is now fully delivered. The PR showed no CI checks; local check_scan and check_skills passed.
- game-juice 1.2.0 released (m4bwav/game-juice PRs #3, #4, tag v1.2.0, installed as game-juice@game-juice): Swink ch. 12-16 read; juice-principles gained P-23 to P-27, lenses J13-J14 and references/feel-cases.md (method only). HANDOFF Next 4 done; the "what Swink adds" list in kb/feel-handoff.md is now delivered except the juice-scan report field and feel-metrics checklist (not done: juice-scan untouched).
- v0.1.6 (C-20261030-4): curve --costs for multi-currency tables, clock and units check in review step 2, stable improve ids. PR #11 merged, tagged and released with the zip, updated from mark-local. Installed folder 297 KB, 3 KB under the green line: trim before adding kb.
- T-20261030-6: new outcome-8 grades counted evidence on ember-market (cost table, Kiln odds, loop count, 25% win share), 5 runs an arm: with 0.85, without 0.65. The first case where the arms separate on mean score; bare Claude finds the flaws but rarely shows the counting (cost table 2/5, win share 1/5). worth still says CUT because it scores all-graders pass rate (40% vs 20%, noise 57); not recorded.
- v0.1.5 (C-20261030-3, T-20261030-5): contract schema in references/findings-contract.md, batched reads. No turn or cost saving (about $1.10 a skill run against $0.35 bare); quality held at 6/6. Cost-cutting closed on this fixture. Main CI fixed (committed eval reports removed).
- v0.1.4 (C-20261030-2): review step 3 runs four book sweeps (promises, trigger pairs, whole-table curves, EV on every gamble); step 3b checks the designer's intent, stopping mechanism and the defence's arithmetic before filing.
- T-20261030-3: new ember-market fixture, first cases graded on the saved file. outcome-6 with 1.00, without 0.94 (bare misses the Bellows cost-curve outlier 2 of 6 runs); outcome-7 (misread playtest win share) ties 1.00/1.00.
- Mark ruled KEEP (2026-10-30). worth still says CUT: +7 points inside a 22-point noise margin at 3.1x cost. On a frontier model the books add little to raw detection; the measured edge is quiet counted flaws and precision.
- Evergreen PR m4bwav/evergreen-protocol#34 merged. Beat game-design built, first scan not run.
- T-20261030-4: a smaller rubric load saved nothing ($1.05 vs $1.06 a run); the cost is turns (about 16 against 6). Reverted.

## Waits on Mark
- Nothing blocking. Open question: is the skill's value worth 3x tokens when detection is close to bare Claude? Options in "Next".

## Next
1. (Done 2026-10-31: worth scores per-grader means, evergreen#15.) Left: top outcome-8 up to 10 runs an arm to see if +20 clears the score margin (about $7); optionally make the Kraken skip the Beacon so the precision grader is unambiguous.
2. (Closed 2026-10-30, T-20261030-5: batching instructions did not cut turns.) Never commit evals/results; run `git status` before staging.
3. Reviewer gaps left: adaptive players, Unity GUIDs (clock and units, multi-currency costs and improve ids done in 0.1.6).
4. (Done: game-juice 1.2.0 and 1.3.0.) Swink list closed.
5. First everscout scan on game-design when a refresh needs leads.
