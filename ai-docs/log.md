# Log

## [2026-10-29] start | name, inventory, research, ldw.py
Name check, book inventory (Lemarchand found; Carillo, Gupta, Baldwin, Steele, Game AI Pro 1/2/4 missing), two research notes, ldw.py with 13 tests. Readers launched.

## [2026-10-29] reading | balance books done
Romero and Schreiber, Adams and Dormans, Clark notes written. Gaps: Game Balance ch. 7 (trading), ch. 14 (matchmaking), the spreadsheet chapters and the analysing-existing-games pages; Adams and Dormans ch. 9-12. Reader note for readwright: in big PDFs rw.py section numbers drift from the printed chapters and neighbouring sections repeat text, so cite chapters, not section numbers.

## [2026-10-29] reading | Swink and Gibson Bond done (partial)
Swink: principles and metrics read; case-study chapters 12-16 (Asteroids, Mario, Bionic Commando, Mario 64, Raptor Safari) only from the toc, so the game-juice PR still needs a read of them for the measured cases. Gibson Bond Part I read in the main; the probability maths in ch. 11 and the group-testing half of ch. 10 only from the toc.

## [2026-10-29] reading | Schell, Koster, Sylvester done (partial)
Schell: about 70 of the 112 lenses (questions only), ch. 13 balance, ch. 14 puzzles, ch. 16 interest curves opening, ch. 27 playtesting. Koster: read by per-page excerpts, not word for word; ch. 7 list cut off and not recorded. Sylvester: ch. 2, 3, 5, 6, 11, 13 and emergent story; ch. 7 (game theory, yomi) and ch. 8 (reinforcement schedules) worth a second pass for uncertainty and ai-npc.

## [2026-10-29] reading | Fullerton, Salen and Zimmerman, Elias et al. done (partial)
About 25-30k words read per book. Fullerton: ch. 5, 9, 10, 11 in large part; dilemmas, accessibility and AI-in-the-creative-process seen as headings only. Salen and Zimmerman: meaningful play, choice, rules, emergence, uncertainty, information, feedback, conflict, rule-breaking; Units 3-4 unread. Elias et al.: cited by epub section (s4.2), no page numbers.

## [2026-10-29] reading | game AI technique books done (partial)
Millington (ch. 2, parts of 5-7 and 11, most of ch. 14), Buckland, Bourg and Seemann, Game AI Pro 3 (ch. 1, 4, 33 in full; 13, 31, 32 partial), Aversa (pointers to unity-agent). Highest value: Millington ch. 14, Game AI Pro 3 ch. 4 and 33. Small-sample caveats flagged in the notes.

## [2026-10-29] reading | production books done
Lemarchand (most of the production chapters), Hackett (full), Schreier (sampled, about a third to half per chapter: check case details against the book before quoting), Wyman (thin: PDF text is one long line per section), Nystrom (design-relevant patterns only). Parallel readers overwrote each other in the shared scratchpad; next time give each reader its own scratch subfolder in the brief.

## [2026-10-29] reading | Sellers, Costikyan, Hodent done (partial)
Sellers ch. 4-10 and 12 in part (analytical balance and telemetry unread). Costikyan ch. 3, 5 (all eleven uncertainty sources), 6. Hodent application sections of ch. 3-8, usability heuristics and pillars, onboarding plan; dark patterns and AI sections half read.

## [2026-10-29] reading | level design and procgen books done; all nine groups in
Totten, Bauer, Short and Adams, Shaker-Togelius-Nelson written, each compared with the Level Up! distillation. 27 notes files in books/plugin-learnings/round3-game-design/. Next: step 4 synthesis into kb/.

## [2026-10-29] review | first real-game run: SpaceDeckBuilder2 (read-only)
Review (13 findings, validate OK) and improve list (10) in ai-docs/reviews/ (gitignored), with ldw-xp-sim, ldw-deck-growth, ldw-energy and ldw-buildings-curve tables. Top: Shuttle win unreachable (no Fuel Cell / Spacecraft Component producer), Launchpad-then-wait wins at turn 30, 70 of 82 reward cards uncoded. Skill gaps seen: no step for "doc and code disagree on the clock", rubric lacks an "implemented vs authored" check, curve needs multi-resource costs declared by hand, economy has no fractional/policy guidance, improve.md ids get renumbered by the md sort.

## [2026-10-29] evals | salt-road fixture, outcome A/B, tidy
Harder fixture salt-road plus outcome-3/-4; outcome cases seeded by case.yaml scaffolds. plugin eval on Windows: no shell grant possible, so the skill arm hand-counts and loses on last-message grading (T-20261029-2, L-20261029-1, about $17 of eval runs). skill-tidy: description cut under 1024 chars; ST021 nested kb links kept by design. Repo m4bwav/ludowright still absent; evergreen-protocol#34 open, no comments.

## [2026-10-29] release | public repo, v0.1.0, wiki; review reaction routed
Mark OK'd the public repo and objected to no review finding (unbuilt items are just not built yet). Created m4bwav/ludowright, PR #1 (banner, CI: no Python 3.9 on Ubuntu 26.04) and PR #2 (contract 1.1 `stage`/`built`, rubric R-53, L-20261029-2, package.py) merged, v0.1.0 released with the zip, wiki pushed after a browser click created it, social preview uploaded, installed from mark-local. Bash heredocs with apostrophes broke again; wiki pages written with Write.

## [2026-10-29] tune | 0.1.1: no-shell fallback, lantern-keep, eval grants
SKILL.md: one-line no-shell fallback, findings before caveats, contract 1.1 named. New fixture lantern-keep (uncoded beacon win and flavour relic) with outcome-5; action cases got graders. plugin eval needs `--allow-tools Write`; granting Bash fails on Windows (no sandbox). action-2 passes; outcome-5 ties because of the flaws-first order (question for Mark). About $6 of runs.

## [2026-10-30] tune | 0.1.2: R-53 ruling applied
Mark chose "core-win gap first": a designed-but-uncoded piece that blocks the advertised win or core loop now leads the review; other unbuilt gaps follow the flaws. First re-run scored 0/3 in both arms because the judge reads only the reply and the reply never said "prototype"; step 7 now names stage and built status. Re-run: with 0.67, without 0.33. PowerShell --scaffold fails (WSL bash); Git Bash works. About $5 of runs.

## [2026-10-30] evals | 0.1.3, outcome A/B, worth CUT
SKILL.md stops quoting test state to users; outcome-2 grader reworded. A/B outcome-1..4 (T-20261030-2): ties or noise; outcome-4 flipped 0.00 to 1.00 between identical runs. worth --record: CUT, no gain beyond noise at 3.2x cost; put to Mark. PR #5 merged, v0.1.3 tagged and released, installed. Harness traps: target . finds no cases, repeated --case keeps the last, timeout 590 killed a run. About $17.

## [2026-10-30] tune | 0.1.4: book sweeps and intent check; worth still CUT
Mark: keep ludowright and make it useful with the book learnings. New ember-market fixture (five planted flaws, two quiet, plus a defended Foundry snowball) graded on the saved review.md, the first file-graded value cases (outcome-6, holdout outcome-7). review.md gained four sweeps (promises, trigger pairs, whole-table curves, EV on every gamble) and step 3b, an intent check with the defence's arithmetic. outcome-6: 0.83/0.89 before, 1.00/0.94 after (bare misses the cost-curve outlier 2 of 6); outcome-7 ties. worth stays CUT (+7 inside noise 22, x3.1 cost). Fixture bug caught by the skill: "five of twelve, close to even share" in 4p is 42%. Harness: llm graders take no target; regex `target: {source: file, path}` and `match: not_contains` work. About $17.

## [2026-10-30] evals | rubric index tried for cost, reverted
evergreen-protocol#34 is merged. HANDOFF Next 2 tested: a one-line-an-item rubric index in place of the 20 KB rubric. outcome-6 held (with 1.00, without 0.83) but the skill arm cost the same ($1.05 vs $1.06 a run, 16 turns). Cost is turn count, not context size; reverted. T-20261030-4. About $4.6.

## [2026-10-30] tune | 0.1.5: contract reference, batched reads; CI unbroken
Traced outcome-6 (HANDOFF Next 2). Turn sinks: one file a turn, plus a Grep and a full README read to find the contract. Added references/findings-contract.md and one-turn parallel-read instructions. A/B: with 1.00 (3/3), without 0.83; turns 13-21 and $1.07-1.19 a run, so no saving. Cost is the model's pacing, not the instructions; stop chasing it on this fixture (T-20261030-5). Main CI had been red since #8: eval report folders were committed under evals/results (gitignored); untracked them, budget green. ldw VERSION was stuck at 0.1.2; now 0.1.5. About $7.3.

## [2026-10-30] evals | outcome-8: counted evidence separates the arms
New case on the ember-market prompt with four regex graders for shown arithmetic (cost table, Kiln odds, loop count from the starting deck, 25% win share). 5 runs each arm: with 0.85, without 0.65; bare missed the cost table 3/5 and the win-share sum 4/5. worth still CUT on the all-pass rate (40/20, noise 57, x2.69 cost); not recorded. T-20261030-6. About $7.3.

## [2026-10-30] tune | 0.1.6: three reviewer gaps closed
HANDOFF Next 3. `ldw.py curve --costs gold:1,wood:0.5` (or a "costs" object in the table) folds multi-resource costs into one at stated rates, with a test; review step 2 now checks the clock and the units (turns vs seconds, per turn vs per round); improve ids are given once in rank order and never renumbered. No eval re-run: the rubric and SKILL.md rules did not change, only references and the CLI. Installed skill folder is 297 KB against a 300 KB green line. Still open from that list: adaptive players, Unity GUIDs.

## [2026-10-30] handoff | game-juice 1.2.0 from Swink's case studies
HANDOFF Next 4. Read Swink ch. 12-16 (openings and summaries of all five; Mario 64's What's Important) with readwright (`rw.py read -s`, not `outline`). game-juice PR #3: P-23 classify feel, P-24 space and motion as a pair, P-25 rules are feel, P-26 direct or simulated per axis, P-27 bottom-up; lenses J13, J14; references/feel-cases.md (method only, no per-game numbers). PR #4 bumped the second manifest (.claude-plugin/plugin.json, which pack.py reads). Both merged, v1.2.0 released with the zips, plugin updated from its own marketplace (game-juice@game-juice, not mark-local). juice-scan untouched.

## [2026-10-30] handoff | game-juice 1.3.0: juice-scan feel type and inferred properties
HANDOFF Next 4 remainder. juice-scan Step 2 now classifies the feel (P-23: control, space, polish) before judging and writes down speed, jump height, gravity, HP and caps with file:line (P-24, P-25); report-template header gained both lines. PR #5 merged (no CI checks reported; local tests passed), v1.3.0 tagged and released, plugin updated. Evals not re-run: triggers unchanged.

## [2026-10-30] evals | harbor-yard breadth fixture: tie
HANDOFF Next 1. New fixture harbor-yard and outcome-9 (11 regex graders on review.md). 3 runs an arm: with 0.94, without 0.97; bare Claude covers all ten flaws. One skill run failed the Kraken precision grader, text not kept. Clock grader tightened after it matched the fixture itself. T-20261030-7. About $5.6.

## [2026-10-30] evals | harbor-yard quieter, Kraken defence fixed: still a tie
HANDOFF Next 1. Removed the three outright hints from playtests.md. --keep-temp reviews showed the Kraken defence contradicted its own numbers (both arms said so); fixed the fixture. Re-run with 0.97, without 1.00. T-20261030-8. Trap: never delete claude-eval-* temp folders while an eval runs; it voided one run. About $14.6.

## [2026-10-31] evals | worth scores the mean grader score (evergreen#15)
HANDOFF Next 1 remainder. evergreen `ab_report` adds score_with/without, score_delta and a Welch score_margin (floor 5 points); `verdict` gives KEEP or TRIM when all-pass ties but the score gain clears its margin. Test added, CI green on six jobs, merged. CI caught a foreign T- id in the evergreen CHANGELOG (check_links); cite other repos' runs without the id. ludowright outcome-8: 0.85 vs 0.65, margin 0.23, still CUT.

## [2026-10-31] evals | outcome-8 top-up: the edge was noise
HANDOFF Next 1. 5 more runs an arm: with 0.60, without 0.70. Pooled 10 an arm 0.725 vs 0.675, +5 inside noise. Detection and counted evidence both tie bare Claude on these fixtures. T-20261031-1. About $7.8.

## [2026-10-30] handoff | session 17: nothing to do without Mark
SpaceDeckBuilder2 has no game changes since the 2026-10-29 review (askpicks tool and snapshot docs only), so no re-review. Round 1 had no objections; the loop waits on Mark saying good or naming misses. Detection A/B spending stopped (session 16). Open, non-blocking: adaptive players, Unity GUIDs, first game-design scout scan.

## [2026-10-30] review | Mark: SpaceDeckBuilder2 review was good
Continue prompt section 4 stop condition met. No misses named, so nothing routed to the skill, kb or rubric and no patch release. Remaining open items are optional: adaptive players, Unity GUIDs, first game-design scout scan.

## [2026-10-30] handoff | session 19: idle check
All continue-prompt items done or optional; PR #34 merged; no reactions owed. Nothing run.

## [2026-10-30] kb | Spelunky (Yu) distilled, 0.1.7
Reader notes yu-spelunky.md (225 lines, all four parts). Folded into procgen, levels-and-space, production-and-scope, uncertainty; rubric R-54 to R-57.

## [2026-10-30] fix | 0.1.8 drops committed eval results
0.1.7 was merged with the budget check red: `git add -A` picked up skills/ludowright/evals/results/. Removed and gitignored. Lesson: check `gh pr checks` for any non-pass before merging, and stage paths, not -A.

## [2026-10-30] kb | Spelunky learnings table applied, 0.1.9
Ten approved rows from the vault learnings note (indie-ai-scout books/spelunky) added as numbered principles in eight kb files plus a spawn-table note in balance-tables. ldw.py VERSION had drifted to 0.1.6; now 0.1.9. Budget yellow is review-rubric.md, unchanged.
