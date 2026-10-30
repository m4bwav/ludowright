# Synthesis brief: chain step 4, notes into kb/

Inputs: every `*.md` in `D:/m4bwa/Claude/Projects/Ai/books/plugin-learnings/round3-game-design/` (except the READER-BRIEF), plus `D:/m4bwa/Claude/Projects/Ai/books/plugin-learnings/game-design-level-up.md`, plus the two research notes in `D:/m4bwa/Claude/Projects/Ai/ludowright/ai-docs/research/`. Read each notes file's Distillation, Review checks, and Disagreements sections first; dip into Section notes only for your topics.

Output: the kb files named in your prompt, in `D:/m4bwa/Claude/Projects/Ai/ludowright/kb/`. Write nothing else, anywhere. No git, no Unity Editor, no saves. Use your own scratch subfolder if you need one (not a shared filename).

Each kb file is loaded on demand by a skill, so it must be short and dense: 80 to 160 lines, plain markdown, no em dashes, absolute dates.

Shape of each kb file:
1. `# <Topic>` and one line: what question this file answers, and when a skill should load it.
2. `## Principles`: numbered, each one sentence or two in our own words, with sources in brackets by short name and chapter, e.g. `[Schell lens 23; Sylvester ch. 6]`. Merge duplicates across books into one principle with several sources. No quotes over ten words, nothing copied from tables or examples.
3. `## How to apply`: the procedure a designer or reviewer runs for this topic (questions to ask, numbers to compute, which `ldw.py` command helps: `ev`, `curve`, `economy`, `sim`).
4. `## Failure patterns`: named patterns, each with the symptom you would see in a game's docs, data or code, and the sources.
5. `## Where the books disagree`: each disagreement, which view ludowright takes, and why (one or two lines).
6. `Related:` line linking the other kb files by relative link (`[title](file.md)`), and pointers out: feel goes to game-juice's juice-scan and juice-principles; engine implementation to unity-agent, roblox-agent, madnesswright; Level Up! engine-side references (one-pager, beat chart, playtest protocol) live in those plugins' game-design references: point to them rather than copying.

Copyright: paraphrase only; these files ship in a public repo.

Reply with the files written and line counts, and the three biggest disagreements you resolved, one line each.
