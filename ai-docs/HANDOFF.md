# Handoff

Resume with `Execute ai-docs/plans/2026-10-29-ludowright-continue-prompt.md` (start the session in this folder).

## Current state (2026-10-30, session 9)
- v0.1.5 (C-20261030-3, T-20261030-5): contract schema in references/findings-contract.md, batched reads. No turn or cost saving (about $1.10 a skill run against $0.35 bare); quality held at 6/6. Cost-cutting closed on this fixture. Main CI fixed (committed eval reports removed).
- v0.1.4 (C-20261030-2): review step 3 runs four book sweeps (promises, trigger pairs, whole-table curves, EV on every gamble); step 3b checks the designer's intent, stopping mechanism and the defence's arithmetic before filing.
- T-20261030-3: new ember-market fixture, first cases graded on the saved file. outcome-6 with 1.00, without 0.94 (bare misses the Bellows cost-curve outlier 2 of 6 runs); outcome-7 (misread playtest win share) ties 1.00/1.00.
- Mark ruled KEEP (2026-10-30). worth still says CUT: +7 points inside a 22-point noise margin at 3.1x cost. On a frontier model the books add little to raw detection; the measured edge is quiet counted flaws and precision.
- Evergreen PR m4bwav/evergreen-protocol#34 merged. Beat game-design built, first scan not run.
- T-20261030-4: a smaller rubric load saved nothing ($1.05 vs $1.06 a run); the cost is turns (about 16 against 6). Reverted.

## Waits on Mark
- Nothing blocking. Open question: is the skill's value worth 3x tokens when detection is close to bare Claude? Options in "Next".

## Next
1. Measure what is not graded yet: a case that greps the findings JSON for counted evidence (an `ldw` table cited, policy and spread named), and a SpaceDeckBuilder2-sized fixture where breadth matters; 5 runs a case so worth can leave the noise.
2. (Closed 2026-10-30, T-20261030-5: batching instructions did not cut turns.) Never commit evals/results; run `git status` before staging.
3. The other reviewer gaps in the log (clock and units, multi-currency costs, adaptive players, improve md sort, Unity GUIDs).
4. game-juice PR from kb/feel-handoff.md after reading Swink ch. 12-16.
5. First everscout scan on game-design when a refresh needs leads.
