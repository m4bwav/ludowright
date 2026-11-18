# Narrative design

Answers: how a game's story is structured and tested as design, not how its prose is written. Load it for quest and mission structure, branching choices, the critical path and story playtests. Written 2026-11-18 from Heussner and others, The Game Narrative Toolbox (2nd ed.); book rules, unverified.

## Principles

1. Name the structure. A mission is a chapter of a linear story played in a fixed order; a quest is a self-contained story the player can take in any order. Mixing the two without saying which is which breaks continuity. [ch. 5]
2. Pick a theme on purpose. With none, a story drifts to good beats evil or win at any cost. A stated theme lets several writers make consistent calls fast. [ch. 5]
3. Each mission builds on what the player just did, so the player seems to drive the story. [ch. 5]
4. Write a linear core story first. Branch only when the branch clearly improves the story: every permanent branch multiplies work for art, audio, levels and tests. [ch. 5]
5. Branches rejoin at pinch points. The critical path is the chain of required quests; side quests hang off it and may never be found. [ch. 5]
6. A choice is real only when the player sees its consequence in the game, in the story, the rules or both. A choice with no visible result is a fake choice. [ch. 5]

## How to apply

1. Draw the quest graph: critical path, side quests, choice nodes, pinch points. For each choice node, name where its consequence shows. None found: report a fake choice.
2. Count permanent branches and the assets each needs. Cut a branch that adds cost but no story gain.
3. Skip test: play or trace the critical path with every optional quest skipped. The story must still make sense.
4. Knowledge checkpoints: for each story section, write what the player must know after it, then ask a tester. A miss is an information-flow gap.
5. Run variant setups the design allows (party makeup, early or late order of quests) and check that no required beat depends on a skipped one.
6. Read story feedback in two columns: feedback (how the player felt) is always valid; suggestions (what they would change) are leads only. For a negative reaction, check in order: did they understand what to do, did they feel free to choose, did a depiction put them off, were they reacting to unfinished art. [ch. 9]
7. Use fresh testers for story: people who know the plot stop seeing its holes. Do not explain the story before they play. [ch. 9]
8. Do not patch missing animation with extra lines; the lines turn redundant once the animation lands. [ch. 9]

## Failure patterns

- Fake choice. Symptom: a choice node with no visible consequence anywhere downstream. [ch. 5]
- Branch sprawl. Symptom: permanent branches added before the linear core works; scope grows faster than the story improves. [ch. 5]
- Optional-content dependency. Symptom: the critical path assumes a fact only taught in a side quest. [ch. 9]
- Railroaded player. Symptom: testers report they never felt free to decide, or characters act against motive to push the plot. [ch. 9]

Related: [worldbuilding-and-lore](worldbuilding-and-lore.md) (lore and canon), [playtesting](playtesting.md) (session scripts), [levels-and-space](levels-and-space.md) (environmental storytelling and pacing).
