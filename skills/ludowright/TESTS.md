# Tests: ludowright

Test runs for [SKILL.md](SKILL.md). Cases live in `evals/evals.json`. A failure that taught something is a lesson in [LEARNINGS.md](LEARNINGS.md); a fix it caused is logged in [CHANGELOG.md](CHANGELOG.md) with `because: T-...`; research it triggered is in [RESEARCH.md](RESEARCH.md); counts and the failing list are in `evergreen.json` under `tests`. Rules: MAINTENANCE.md (testing section) and the plugin's `protocol/TESTING.md`.

A test passes on evidence (a tool call in the trace, a file, a marker, a log line), never on the transcript's claim that something was done.

Entry shape: `### T-YYYYMMDD-n · date · harness · env · passed/total`, then one line per failing case (`id · kind · class · what the evidence showed`), then `led to:` (L-, C-, R- ids or none). Newest first. Budget 150 lines; archive older runs to `TESTS-ARCHIVE.md`.

## Runs

### T-20261030-2 · 2026-10-30 · claude plugin eval (outcome-1..5, 3 runs each arm, --scaffold, --allow-tools Write, skills/ludowright as target, Git Bash) · owner-pc Windows · outcome-1 1.00/1.00, outcome-2 0.67/1.00 after the grader fix (0/0 before), outcome-3 0.67/0.67, outcome-4 1.00/0.67 on re-run (0.00/0.67 first)
- outcome-4 swung from 0.00 to 1.00 between two identical runs: three runs a case are too few to separate the arms on these fixtures. Read single A/B results as noise unless a case loses twice.
- outcome-2 · grader: the old wording wanted jargon; reworded (C-20261030-1). outcome-3 · flaky in both arms.
- outcome-5 cut off by a 590 s `timeout` wrapper (no aggregate); last measured 0.67/0.33 in T-20261030-1.
- Harness notes: target `skills/ludowright` (target `.` finds no cases; `--eval-dir` inside skills/ is refused); `--case` takes one glob, repeated flags keep only the last, brackets do not match. Do not wrap in `timeout`. About $17.
- led to: C-20261030-1

### T-20261030-1 · 2026-10-30 · claude plugin eval (outcome-5, 3 runs each arm, --scaffold, --allow-tools Write, from Git Bash) · owner-pc Windows · outcome-5 with 0.67, without 0.33
- First run after the R-53 ruling: both arms led with the beacon gap, but 0/3 each, because the reply never said "prototype" or that the Moth Charm was unbuilt (both were only in the file). Fixed by naming stage and built status in the reply; re-run as above.
- From PowerShell `--scaffold` fails: `/bin/bash` resolves to WSL and the Windows path loses its backslashes. Run evals from Git Bash.
- Seen: the skill arm told the user that its own self-test outcome-5 was failing (it read evergreen.json). Should not be in a user reply; open.
- led to: C-20261029-5


### T-20261029-3 · 2026-10-29 · claude plugin eval (action-2, outcome-4, outcome-5; 1 run each arm, --scaffold, --allow-tools Write; Bash refused: no Windows sandbox) · owner-pc Windows · action-2 pass (with 1, without 0); outcome-5 tie (1/3 votes each arm); outcome-4 0 vs 1 without the Write grant
- action-2 gained graders (Skill fired, Write of design-*.md); action-1 got the matching review-*.json grader, not run.
- First outcome-4/-5 runs forgot `--allow-tools Write`: neither arm could save a file (L-20261029-3). Re-run outcome-5 with Write: both arms find the uncoded beacon_win; the skill files it as F-002 `built: no` after a design flaw (flaws first, C-20261029-3), and the judge wanted it ranked first. Open question for the owner: does R-53's flaws-first order hold when the gap blocks the advertised core win?
- Cost about $6.

### T-20261029-2 · 2026-10-29 · claude plugin eval (outcome-1..4, 3 runs each arm, haiku judge on the last message, --scaffold, Write granted, no shell) · owner-pc Windows · 1/4 cases pass both arms
- Harness: cases now seed the fixture with case.yaml + fixture.sh (the first run, without scaffolds, scored 0 on all 24 runs because the sandbox could not read the plugin folder). Windows cannot confine Bash, so `plugin eval` refuses a shell grant: ldw.py never ran and the skill arm did the counting by hand (18-25 turns against 6-8 without).
- outcome-1 · outcome · flaky · with 1/3, without 2/3; replies that pass and fail look alike in substance.
- outcome-2 · outcome · grader · 0/3 both arms although every reply names gold piling up past turn 6 with the one-card-a-turn sink; the expectation's wording ("single capped sink", "economy-leak") is stricter than the judge can match.
- outcome-3 (new salt-road fixture, reputation loop) · pass 3/3 with, 3/3 without: the loop is found either way.
- outcome-4 (holdout, dropped storm promise) · with 0/3, without 3/3. The skill's replies name storms at 0.0 in tuning.json but lead with the shell caveat and a short top list; the judge wanted the dominant mountain roads in the last message.
- Not run: action-2 (design one-pager).
- led to: L-20261029-1; next: grade the saved findings file, not the last message, and run the A/B where a shell exists (evergreen-tester, or plugin eval on macOS/Linux).

### T-20261029-1 · 2026-10-29 · not yet run · skill · 0/0
- Suite scaffolded; no run recorded. Write the cases in `evals/evals.json` (at least two trigger prompts, two decoys, one action case with evidence, one outcome case), run the baseline without the skill, then run with it (`evergreen-test`).
- led to: none

### T-20261029-1 · 2026-10-29 · claude plugin eval (trigger-1..3, decoy-1..3; sonnet judge, --no-publish); evergreen-tester (outcome-1, with and without, 1 run each) · owner-pc · 7/7 run cases pass; outcome-1 redundant
- trigger-1, -2, -3: with 3/3 each, without 0/3 each. decoy-1 (floaty jump, game-juice), decoy-2 (Unity coroutine), decoy-3 (story writing): quiet 6/6 each.
- outcome-1 (doubles as action-1's evidence): with the skill, review JSON validated "OK: 4 findings, 0 errors, 0 warnings", names Overclock and cards.csv, `ldw.py curve` and `economy` run, the gold table saved beside it; 8 tool calls. Without: one prose markdown file that also found Overclock and the gold overflow; no contract file, no counted table; 2 tool calls.
- The tiny-colony flaws are too obvious to separate the arms on detection: outcome-1 and outcome-2 are regression guards. The skill's measured difference here is the contract file and the counting. A harder fixture (a degenerate loop between two rules; a doc promise the code drops) is owed.
- Not yet run: action-2 (design one-pager), outcome-2 (holdout), runs 2 and 3 of outcome-1.
led to: none yet (harder fixture owed)
