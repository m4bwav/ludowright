# Tests: ludowright

Test runs for [SKILL.md](SKILL.md). Cases live in `evals/evals.json`. A failure that taught something is a lesson in [LEARNINGS.md](LEARNINGS.md); a fix it caused is logged in [CHANGELOG.md](CHANGELOG.md) with `because: T-...`; research it triggered is in [RESEARCH.md](RESEARCH.md); counts and the failing list are in `evergreen.json` under `tests`. Rules: MAINTENANCE.md (testing section) and the plugin's `protocol/TESTING.md`.

A test passes on evidence (a tool call in the trace, a file, a marker, a log line), never on the transcript's claim that something was done.

Entry shape: `### T-YYYYMMDD-n · date · harness · env · passed/total`, then one line per failing case (`id · kind · class · what the evidence showed`), then `led to:` (L-, C-, R- ids or none). Newest first. Budget 150 lines; archive older runs to `TESTS-ARCHIVE.md`.

## Runs

### T-20261029-1 · 2026-10-29 · not yet run · skill · 0/0
- Suite scaffolded; no run recorded. Write the cases in `evals/evals.json` (at least two trigger prompts, two decoys, one action case with evidence, one outcome case), run the baseline without the skill, then run with it (`evergreen-test`).
- led to: none

### T-20261029-1 · 2026-10-29 · claude plugin eval (trigger-1..3, decoy-1..3; sonnet judge, --no-publish); evergreen-tester (outcome-1, with and without, 1 run each) · owner-pc · 7/7 run cases pass; outcome-1 redundant
- trigger-1, -2, -3: with 3/3 each, without 0/3 each. decoy-1 (floaty jump, game-juice), decoy-2 (Unity coroutine), decoy-3 (story writing): quiet 6/6 each.
- outcome-1 (doubles as action-1's evidence): with the skill, review JSON validated "OK: 4 findings, 0 errors, 0 warnings", names Overclock and cards.csv, `ldw.py curve` and `economy` run, the gold table saved beside it; 8 tool calls. Without: one prose markdown file that also found Overclock and the gold overflow; no contract file, no counted table; 2 tool calls.
- The tiny-colony flaws are too obvious to separate the arms on detection: outcome-1 and outcome-2 are regression guards. The skill's measured difference here is the contract file and the counting. A harder fixture (a degenerate loop between two rules; a doc promise the code drops) is owed.
- Not yet run: action-2 (design one-pager), outcome-2 (holdout), runs 2 and 3 of outcome-1.
led to: none yet (harder fixture owed)
