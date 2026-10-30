# Changelog: ludowright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: MAINTENANCE.md.

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

### C-20261029-5 · 2026-10-29 · R-53: a gap blocking the advertised win ranks first (0.1.2)
- because: T-20261029-3 (outcome-5 judge), T-20261029-4, owner ruling 2026-10-29
- files: references/review.md (step 7), kb/review-rubric.md (R-53), LEARNINGS.md (L-20261029-2)
- A designed-but-uncoded piece that blocks the win or core loop the game advertises now leads the report; other unbuilt gaps still follow the flaws in what exists. The reply now names the stage and marks unbuilt findings, because the judge reads only the reply, not the findings file.

### C-20261029-4 · 2026-10-29 · No-shell fallback, findings first, contract 1.1 in SKILL.md; lantern-keep fixture (0.1.1)
- because: L-20261029-1 (T-20261029-2), L-20261029-2
- files: SKILL.md (LDW line, findings contract, Output), evals/fixtures/lantern-keep, evals/cases/outcome-5
- When no shell is allowed the skill says so in one line, counts by hand only what a finding needs and still writes the file. The reply leads with the findings and puts caveats last. SKILL.md now names contract 1.1 with `stage` and `built`. New prototype fixture with an uncoded win-path relic and an uncoded flavour relic tests R-53 (outcome-5).

### C-20261029-3 · 2026-10-29 · Stage and built: separate "not built yet" from "built wrong"; findings contract 1.1
- because: L-20261029-2 (user reaction to the SpaceDeckBuilder2 review)
- files: references/review.md (steps 2 and 7), kb/review-rubric.md (R-53), scripts/ldw.py (validator, md), README contract
- Review step 2 settles the game's stage; findings on designed-but-uncoded content carry `built: no|partial` and are reported after the flaws in what exists. New rubric item R-53. Contract 1.1 adds the optional `stage` and `built`; 1.0 files still validate.

### C-20261029-2 · 2026-10-29 · Description trimmed under 1024 chars
- skill-tidy ST005: the description was 1072 chars and some hosts drop longer ones. Cut 'sources and sinks', 'and questionnaires' and the 'how do I make my game better' trigger phrase (still covered by 'what's wrong with my game' and the improve route). Also added the salt-road fixture and outcome-3, outcome-4.
- because: skill-tidy lint

### C-20261029-1 · 2026-10-29 · Created as an evergreen unit
- because: user request
- files: SKILL.md, RESEARCH.md, LEARNINGS.md, evergreen.json (skills: also TESTS.md and evals/evals.json)
- Initial version. Tier `moderate`, interval 30d. See R-20261029-1 for the research basis; the first test run, for a skill, is logged in TESTS.md.
