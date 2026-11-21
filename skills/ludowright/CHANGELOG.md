# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

### C-20261120-3 · 2026-11-20 · `ldw.py stop`: stop-or-continue check; uncertainty 32 to 34 (0.1.45)
- because: user request (technique harvest of a 2015 Twine web game, Seedship; source read and played, no licence, so ideas only, described fresh, no code, text or assets copied)
- files: scripts/ldw.py (stop), tests/test_ldw.py (StopTest), kb/balance-tables.md (stop), kb/uncertainty.md (32 to 34), kb/INDEX.md, references/balance.md, SKILL.md (routing row, step 4)
- New `stop` command scores fixed settle thresholds for a loop where moving on costs condition the payoff depends on, with an optional noisy mode where damage hides readings. Flags FIRST-IS-BEST, NEVER-STOP, NO-COST, FLAT, else TENSE. Three kb principles: attrition spread over named subsystems, damage that blinds as well as weakens, event deck pacing and named endings. Installed folder now 303 KB (yellow). Triggers unchanged, so evals were not re-run.

### C-20261120-2 · 2026-11-20 · Rubric R-80 no outcome preview; R-39 covers irreversible single-click choices (0.1.44)
- because: user request (technique harvest of a web card battler, source tianlinx/spire-echoes on GitHub, played and measured; ideas only, described fresh, no code, text or assets copied)
- files: kb/review-rubric.md (R-39, How to run 11, Related), kb/review-rubric-more.md (R-80), kb/INDEX.md, tests/test_ldw.py (rubric range)
- R-39 now also flags a choice that cannot be taken back (route node, event option, reward pick) committed on a single click, and names the select-then-confirm fix and its one-click cost. R-80 flags a targeted action with no forecast of damage and health before and after while aiming. Two older entries moved to ai-docs/changelog-archive.md to keep the installed folder at 300 KB. Triggers unchanged, so evals were not re-run (as for R-69 to R-79).
