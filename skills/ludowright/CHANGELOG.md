# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-20261126-15 · 2026-11-26 · Slimmer install: eval cases to the repo root, changelog archived, Actions pinned (0.1.71)
- because: user request (installed folder 412 KB against a 300 KB green line)
- files: evals/cases (moved from skills/ludowright/evals/cases), CHANGELOG.md (0.1.67 and older to ai-docs/changelog-archive.md), .github/workflows/tests.yml
- Eval case folders now sit at the plugin root, where `claude plugin eval` expects them (it refuses an eval directory inside skills/); fixture.sh paths shortened. evals.json stays canonical beside SKILL.md. Workflow actions pinned to commit SHAs. Installed folder 412 KB to 377 KB; no kb text moved or cut. Triggers unchanged, so evals were not re-run.

### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

### C-20261126-14 · 2026-11-26 · RPG book harvest 16: stealth-to-chase pacing, two fronts, retreat to a safe zone, short-range finders, escape-first levels (0.1.70)
- because: harvest: RPG book collection (CORE 1-2 Cog in the Wheel; CORE 1-3 A Hole in the World; Adventure Awaits, Crow's Rest; Dungeons on Demand, Dungeon Delves; paraphrased, book rules unverified)
- files: kb/levels-and-space.md (Principles 50-54)
- Five principles in fresh wording. The environmental clock joins the escape-first line rather than repeat 49's antagonist clock. Also moved entry 13 out of the entry-shape line. Triggers unchanged, so evals were not re-run.

### C-20261126-13 · 2026-11-26 · RPG book harvest 15: horror pacing, a visible antagonist clock, faction deterrents (0.1.69)
- because: harvest: RPG book collection (A Guide to Curse of Strahd; CORE 1-1 A Scream in the Night; Dungeons on Demand, Of Crown and Kingdom; paraphrased, book rules unverified)
- files: kb/levels-and-space.md (Principles 48-49), kb/worldbuilding-and-lore.md (19)
- Three principles in fresh wording. Horror pacing extends levels-and-space 47 rather than repeat its dread beats. Triggers unchanged, so evals were not re-run.

### C-20261126-12 · 2026-11-26 · RPG book harvest 14: diverge then converge, three review roles, if-nothing timelines, profiling opponents, petition talks (0.1.68)
- because: harvest: RPG book collection (Never Unprepared; Focal Point; Deep Carbon Observatory; Unframed; paraphrased, book rules unverified)
- files: kb/production-and-scope.md (Principles 30-31, How to apply step 3 slack range, Where the books disagree), kb/narrative-design.md (Principle 12 extended, 14-18), kb/game-ai-for-designers.md (38-39), kb/worldbuilding-and-lore.md (18), kb/levels-and-space.md (12 extended)
- Twelve principles in fresh wording; slack is now a 10 to 20 percent range. Decaying rewards and the tension loop extend existing principles rather than repeat them. Triggers unchanged, so evals were not re-run.

Older entries (0.1.67 and earlier): [ai-docs/changelog-archive.md](../../ai-docs/changelog-archive.md).
