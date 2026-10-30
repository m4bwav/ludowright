# AGENTS.md

Rules for any AI agent (Claude Code, Copilot, Cursor, Codex, Gemini CLI) working in this repository. `CLAUDE.md` imports this file and `.github/copilot-instructions.md` points here.

## What this is

ludowright: a cross-agent plugin with one skill, `skills/ludowright/`, for game design. SKILL.md holds the rules, the routing and the findings contract; `references/` holds the four task procedures (design, review, improve, balance); `kb/` holds the design knowledge in small files read on demand (start at `kb/INDEX.md`; the review rubric is `kb/review-rubric.md`); `scripts/ldw.py` is the single standard-library CLI (findings validator and markdown view, expected value, cost curve, economy flows, Monte Carlo). Evergreen companions sit beside SKILL.md (RESEARCH, CHANGELOG, LEARNINGS, TESTS, MAINTENANCE, `evergreen.json`, `evals/evals.json` with the `tiny-colony` fixture). Unit tests are in `tests/`; research, reading notes, decisions, the log and the handoff under `ai-docs/` (start with `ai-docs/HANDOFF.md`).

## Rules

- The findings contract (README, "Findings contract") is a public interface other plugins rely on. A change that removes or renames a field, or narrows an allowed value, is a major format version (2.0) and needs a decision entry in `ai-docs/decisions/`; adding an optional field or a category is a minor version (1.x). `FORMAT_VERSION` in `ldw.py`, the README and SKILL.md change together.
- `ldw.py` stays one standard-library Python file (3.9 or newer) for Windows, macOS and Linux, UTF-8 and LF. Every change gets a test in `tests/test_ldw.py`: exact maths as golden values, simulations with a fixed seed and a standard-error band. Run `python -m unittest discover -s tests` before committing.
- The kb paraphrases published books with chapter citations. Never paste a book's text, tables, figures or worked examples here; quotes stay under about ten words. Local paths to the owner's copies stay in `ai-docs/reading/inventory.md` only.
- Fixtures are invented games written for the suite. Never commit another person's game, design documents or data, or a review of a real game. Reviews are written beside the game they review.
- Size budget: `python scripts/budget.py` (red fails CI; tell the maintainer about a yellow in one line). Keep SKILL.md under 200 lines.
- The skill is an evergreen unit. Before editing it read `skills/ludowright/evergreen.json`; if `next_due` has passed or `contradiction` is set, say so and refresh after the task. Every change is logged in the skill's `CHANGELOG.md` with its reason; lessons go to `LEARNINGS.md` with Trigger and Hypothesis. Re-run the eval suite after SKILL.md or rubric changes. The linked everscout beat `game-design` feeds refreshes as leads (protocol §4).
- A release bumps the version in `.claude-plugin/plugin.json`, `plugin.json`, `VERSION` in `ldw.py`, `metadata.version` in SKILL.md and the CHANGELOG together, then tags `vX.Y.Z` and publishes a GitHub Release.
- Neighbours: game-juice owns feel (link, never copy); unity-agent, roblox-agent and madnesswright own engine work and the engine-side design references; readwright reads books and PDFs.
- This is a public repository: no person named other than the author credit and published authors, no machine, no absolute local path outside the reading inventory, no credential. Plain short sentences, no em dashes, relative markdown links, never wikilinks.
- No AI attribution anywhere: no Co-Authored-By trailers, no "generated with" lines in commits, pull requests, releases or files.

## Commands

- Tests: `python -m unittest discover -s tests`
- Budget: `python scripts/budget.py`
- Validate a findings file: `python skills/ludowright/scripts/ldw.py findings validate <file>`
- Plugin manifest: `claude plugin validate .`
- Evals: `claude plugin eval . --no-publish --trust-plugin --case "trigger-*"`

## everlast (session knowledge, load on demand)

- `ai-docs/INDEX.md` lists what past sessions learned here. Scan it at the start of a task and open only matching entries; read `ai-docs/HANDOFF.md` when continuing unfinished work.
- Before finishing a task that hit a dead end, verified a non-obvious command or made a design choice, record it in `ai-docs/` and rewrite `HANDOFF.md` when work is left unfinished.
