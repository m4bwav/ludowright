# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

### C-20261120-1 · 2026-11-20 · ldw.py ramp: difficulty ramp check (0.1.43)
- because: user request (technique harvest of an Apache-2.0 web arcade game: one spawn interval shrinks 6% per point to a floor, one fall speed grows every frame with no cap; method described fresh in our words, no code copied; source cited in the harvest notes)
- files: scripts/ldw.py (ramp, cmd_ramp, ramp_rows), kb/balance-tables.md (ramp), kb/balance-and-economy.md (command table), references/balance.md (step 1), SKILL.md (where the balance and pacing tools live), kb/INDEX.md, tests/test_ldw.py (RampTest), README.md
- Adds `ldw.py ramp TABLE [--steps N] [--json]` for formula ramps (base with factor or add, floor, cap, per, step_seconds) and step -> value tables: values at checkpoints, last/first ratio, and the flags UNCAPPED, FLOOR@n, CAP@n and FLAT-EARLY. Changelog entries 0.1.35 to 0.1.40 moved to ai-docs/changelog-archive.md and research entries R-20261029-1 to -6 to ai-docs/research-archive.md to keep the installed folder under 300 KB.

### C-20261119-2 · 2026-11-19 · Rubric R-69 to R-79 from five design and GM books; encounter, playtest, fudge, abduction and card-family notes (0.1.42)
- because: user request (book round 6: Selinker (ed.), Kobold Guide to Board Game Design, 2011; Baur, Kobold Guide to Gamemastering; Macris, Arbiter of Worlds; Runehammer, ICRPG Core; Parlett, Penguin Book of Card Games; book rules, unverified; proposed IDs renumbered after R-68)
- files: kb/review-rubric-more.md (R-69 to R-79), kb/review-rubric.md (How to run 11, Related), kb/INDEX.md, kb/levels-and-space.md, kb/playtesting.md, kb/uncertainty.md, kb/procgen.md (How to apply each), kb/design-drills.md (7), README.md, tests/test_ldw.py (KbSectionsTest)
- Adds early knockout, endless endgame, kingchooser grades, forced reverse, featured content bypassed, free rest, failable must-know, health sponge, identical retry, arbitrary death and expendable-piece AI, plus Timer-Threat-Treat rooms, a distance gradient, first-plays and extreme-bot playtests, the fudge test, an abduction pass and a mechanism family menu.

### C-20261119-1 · 2026-11-19 · Shaping verb against a visible target; staged stuck-hints (0.1.41)
- because: user request (technique harvest from a commercial web platformer demo; ideas only, described fresh, no code, text or assets copied; one game, unverified beyond it)
- files: kb/core-loops-and-goals.md (Shaping verb against a visible target), kb/ux-and-the-brain.md (Staged stuck-hints), kb/INDEX.md, tests/test_ldw.py (KbSectionsTest)
- Adds terrain shaping as a core verb with a continuous error score between forgiving thresholds and several input routes, and a per-beat hint plan that escalates wait, hand, outline, then text, with touch and keyboard wording.
