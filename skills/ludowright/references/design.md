# Design: a one-pager for a new game

Load [../kb/core-loops-and-goals.md](../kb/core-loops-and-goals.md) and [../kb/production-and-scope.md](../kb/production-and-scope.md); add [../kb/systems-and-loops.md](../kb/systems-and-loops.md) for a systems-heavy idea, and [../kb/uncertainty.md](../kb/uncertainty.md) when chance or hidden information is central.

## Steps

1. **Pin the seed.** Restate what the user gave (a prompt, genre, constraint, platform, team size, time box, their own idea) in one line. Read any notes or prior designs they point to. A user's own idea is the design; your job is to sharpen it, not swap it for yours.
2. **Find the verb and the promise.** Name the core loop as a verb the player does most, and the experience goal as what the player should feel. Write the player promise: the one thing the game guarantees.
3. **Draft the one-pager** to `design-<slug>.md`, these sections in order:
   - Title, one-line hook, platform, audience, session length.
   - Experience goal and player promise.
   - Core loop (verb, the loop in 3-5 steps, the decision at its heart).
   - Core mechanics (3-6), each with the choice it creates.
   - Progression (what grows, over what time, what the player masters).
   - Scope (team, time box, the smallest playable version, what is cut first).
   - Risks (the top 3-5: design, scope, market; each with the cheapest test that would retire it).
   - Comparables (two or three released games, and how this differs).
4. **Make two or three contrasting alternatives,** each a short block with its verb, promise, hook and its main risk. Contrast on a real axis (a different verb, a different audience, a different scope), not cosmetics.
5. **Run the specificity gate** on every section: could this sentence describe a different game? Rewrite or cut. A design with no constraint and no hook is not finished (kb/ai-as-design-tool.md, the guards).
6. **Check it against the rubric** quickly: run the dominant-strategy, degenerate-loop, scope-risk and broken-promise items of [../kb/review-rubric.md](../kb/review-rubric.md) against the draft. Write any that fire as a `design-check` findings file next to it (`LDW findings new --kind design-check`) and fix what you can in the draft.
7. **Confirm the file exists,** then report: path, the hook, the verb, the top risk, and the alternatives in one line each.

Prototype advice is engine-specific: point to unity-agent's or roblox-agent's game-design reference for the build-side one-pager and beat chart rather than writing one here.
