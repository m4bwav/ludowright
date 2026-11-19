# Tests: ludowright

Test runs for [SKILL.md](SKILL.md). Cases live in `evals/evals.json`. A failure that taught something is a lesson in [LEARNINGS.md](LEARNINGS.md); a fix it caused is logged in [CHANGELOG.md](CHANGELOG.md) with `because: T-...`; research it triggered is in [RESEARCH.md](RESEARCH.md); counts and the failing list are in `evergreen.json` under `tests`. Rules: MAINTENANCE.md (testing section) and the plugin's `protocol/TESTING.md`.

A test passes on evidence (a tool call in the trace, a file, a marker, a log line), never on the transcript's claim that something was done.

Entry shape: `### T-YYYYMMDD-n · date · harness · env · passed/total`, then one line per failing case (`id · kind · class · what the evidence showed`), then `led to:` (L-, C-, R- ids or none). Newest first. Budget 150 lines; archive older runs to [ai-docs/tests-archive.md](../../ai-docs/tests-archive.md) (outside the installed folder).

## Runs

### T-20261031-1 · 2026-10-31 · claude plugin eval (outcome-8 top-up: 5 more runs each arm, --scaffold, --allow-tools Write, -j 4) · owner-pc Windows · with 0.60, without 0.70
- Second batch reversed the first (0.85 vs 0.65). Pooled 10 runs an arm: with 0.725, without 0.675, +5 points, inside noise. The skill arm missed the Kiln odds 2/5 and the cost table 3/5 this time.
- led to: none. The counted-evidence edge from T-20261030-6 was noise. No graded case now separates the arms; value rests on Mark's KEEP ruling (contract JSON, real-game depth). About $7.8.

### T-20261030-8 · 2026-10-30 · claude plugin eval (outcome-9 on a quieter harbor-yard; 3 runs each arm, --scaffold, --allow-tools Write, -j 4) · owner-pc Windows · with 0.97, without 1.00
- Change: playtests.md no longer names the Driftwood trick, the unbought Rope Ladder or the Tidecaller win rate. First run with --keep-temp: 0.94/0.94.
- Kept reviews showed a fixture bug, found by both arms: the Kraken defence failed its own arithmetic (no-reshuffle deck means a Kraken every game, not 6 of 20; twenty games against ten in the notes; it hit every player, not the leader). Fixed DESIGN.md and events.csv so the defence holds. Re-run: 0.97/1.00; one skill run still filed the Kraken major, partly fairly (the Beacon is always the highest-timber building, so the Kraken always sinks it).
- A run where a cleanup deleted live sandbox files (0.24/1.00) is void.
- led to: none. Breadth and quieter notes do not separate the arms on a frontier model; the measured edge stays counted evidence (outcome-8). About $14.6.

Older runs (T-20261029-1 to T-20261030-7): [ai-docs/tests-archive.md](../../ai-docs/tests-archive.md).
