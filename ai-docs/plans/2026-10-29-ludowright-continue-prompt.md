# Continue prompt: ludowright and the everscout beat offer (repeat every session)

Written 2026-10-29. This prompt does not change between sessions; the state lives in `ai-docs/HANDOFF.md` and
`ai-docs/log.md`. Start a new session (Claude Code or Copilot) in `D:\m4bwa\Claude\Projects\Ai\ludowright` with:

```
Execute ai-docs/plans/2026-10-29-ludowright-continue-prompt.md
```

The original brief is `D:\m4bwa\Claude\Projects\Ai\prompts\2026-10-29-game-design-plugin-kickoff.md`; read it once
for the goals. Part 1 (evergreen beat offer) and most of Part 2 are built; this prompt carries the rest.

---

You are continuing ludowright, an evergreen game design plugin (one skill: design one-pagers, flaw reviews,
ranked improvements, balance maths, a versioned JSON findings contract), and the work around it. Work until each
item reaches a point that needs Mark, record everything, and end with the continue line.

## 1. Load the state (read, do not redo)

1. `git -C D:/m4bwa/Claude/Projects/Ai/ludowright status --short` and the branch. Do not touch changes you did
   not make.
2. `ai-docs/HANDOFF.md` ("Current state", "Next"), then the tail of `ai-docs/log.md`.
3. `AGENTS.md` (rules: the findings contract is a public interface; no book text; no AI attribution).
4. `skills/ludowright/evergreen.json` (say in one line if stale or failing), `SKILL.md`, `TESTS.md`.
5. Evergreen trunk: `D:/m4bwa/Claude/Projects/Ai/evergreen` (edit there, never `~/.agents`). The beat offer is
   `scripts/evergreen_scout.py`; PR m4bwav/evergreen-protocol#34 carries it.

## 2. Check what waits on Mark first

- The public repo exists (v0.1.0). Work on branches, open PRs, merge your own once checks pass, tag patch releases yourself.
- Is evergreen-protocol PR #34 merged, or does it have review comments? Act on comments; never merge it yourself.
- Has Mark reacted to a SpaceDeckBuilder2 review (section 4)? Route each reaction before anything else.

## 3. Work in this order, skipping what HANDOFF.md marks done

1. **The beat** (done 2026-10-29). Run the first `everscout-scan` on `game-design` when a refresh needs leads; read the six new subreddits' rules before any engagement.
   was finishing it on 2026-10-29). If not finished, run the `everscout-beat` skill, procedure A from step 3.
2. **Evals.** Write a harder fixture beside `tiny-colony` (a degenerate loop between two rules; a promise the
   design doc makes that the data or code drops) with outcome cases on it; run action-2, outcome-2 and runs 2-3
   of outcome-1 with and without the skill (evergreen-tester or `worth --ab`); log a T- entry and
   `evergreen.py tested`. A failing case goes to `evergreen-tune` (three iterations, then report).
3. **skill-tidy and worth.** `python D:/m4bwa/Claude/Projects/Ai/skill-tidy/skills/skill-tidy/scripts/tidy.py`
   on the skill, and `evergreen.py worth skills/ludowright --record` after an A/B.
4. **Release.** v0.1.0 done 2026-10-29 (wiki, banner, zip). For a patch: PR, CI green, bump plugin.json, tag, GitHub Release with the CHANGELOG
   entry, install from the mark-local marketplace, Copilot export as editwright does. Merge your own PRs once
   checks pass (global CLAUDE.md), add the books rows to `books/plugin-learnings/INDEX.md` and a track to
   `PROGRESS.md`.
5. **game-juice PR.** Read Swink's case-study chapters 12-16 with readwright, then open a separate PR on
   game-juice from `skills/ludowright/kb/feel-handoff.md` (what Swink adds that game-juice lacks).

## 4. The real-game round (read-only)

Run ludowright's review and improve procedures on SpaceDeckBuilder2
(`D:\Desktop\Create With Code Mark\SpaceDeckBuilder2`; start with `CODEMAP.md` and `Assets/Docs/designdoc.txt`).
Do not edit that repo, open the Unity Editor or touch saves; write the findings files into
`ludowright/ai-docs/reviews/` (gitignored). Show Mark the top findings and **stop**: ask which are right, which
are wrong, and what it missed. Route each reaction with `evergreen-learn` to the skill, a kb file or the rubric,
re-run the affected evals, release a patch. Repeat until he says it is good.

## 5. Before you stop

Update `ai-docs/HANDOFF.md` (state and the next action) and `ai-docs/log.md`, commit, and end your reply with:

```
Execute ai-docs/plans/2026-10-29-ludowright-continue-prompt.md
```

and the folder to start in (`D:\m4bwa\Claude\Projects\Ai\ludowright`).
