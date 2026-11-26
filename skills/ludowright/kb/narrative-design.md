# Narrative design

Answers: how a game's story is structured and tested as design, not how its prose is written. Load it for quest and mission structure, branching choices, the critical path and story playtests. Written 2026-11-18 from Heussner and others, The Game Narrative Toolbox (2nd ed.); book rules, unverified.

## Principles

1. Name the structure. A mission is a chapter of a linear story played in a fixed order; a quest is a self-contained story the player can take in any order. Mixing the two without saying which is which breaks continuity. [ch. 5]
2. Pick a theme on purpose. With none, a story drifts to good beats evil or win at any cost. A stated theme lets several writers make consistent calls fast. [ch. 5]
3. Each mission builds on what the player just did, so the player seems to drive the story. [ch. 5]
4. Write a linear core story first. Branch only when the branch clearly improves the story: every permanent branch multiplies work for art, audio, levels and tests. [ch. 5]
5. Branches rejoin at pinch points. The critical path is the chain of required quests; side quests hang off it and may never be found. [ch. 5]
6. A choice is real only when the player sees its consequence in the game, in the story, the rules or both. A choice with no visible result is a fake choice. [ch. 5]
7. Four structure flaws to check in a quest or adventure plan: a bottleneck (progress hangs on one action or clue, so give two ways forward and make a found clue an edge, not a key), a railroad (events land whatever the player chose; a dungeon with no branches counts), cluelessness (many open options and no hint, as bad as none), and sidelining (a companion or NPC who could do the hero's job). [Wizards, 4e Dungeon Master's Guide p. 101]
8. A quest is a story goal with more than one way to solve it. "Kill ten of these" only pays the core loop twice; fold it into the loop or give it a goal. [Wizards, 4e Dungeon Master's Guide p. 103]
9. Pace a character's turn (a change of loyalty, faith or side) one step at a time, with some story time between steps, and make each step follow something the character did, not something they announced. A turn in one scene reads as a retcon. [Wizards, 3.5 Dungeon Master's Guide]

## How to apply

1. Draw the quest graph: critical path, side quests, choice nodes, pinch points. For each choice node, name where its consequence shows. None found: report a fake choice.
2. Count permanent branches and the assets each needs. Cut a branch that adds cost but no story gain.
3. Skip test: play or trace the critical path with every optional quest skipped. The story must still make sense.
4. Knowledge checkpoints: for each story section, write what the player must know after it, then ask a tester. A miss is an information-flow gap.
5. Run variant setups the design allows (party makeup, early or late order of quests) and check that no required beat depends on a skipped one.
6. Read story feedback in two columns: feedback (how the player felt) is always valid; suggestions (what they would change) are leads only. For a negative reaction, check in order: did they understand what to do, did they feel free to choose, did a depiction put them off, were they reacting to unfinished art. [ch. 9]
7. Record each quest as a premise plus a twist, and give a two-layer quest a hook premise the player sees first and a different real premise underneath. If the same premise comes up twice in a campaign, reverse it the second time (the rescuer needs rescuing, the thief was the owner) so it reads as new; pair a physical goal with a personal stake when two plots run at once. [S. John Ross, The Big List of RPG Plots, in a Game Ideas collection p. 8-9, 11]
8. Use fresh testers for story: people who know the plot stop seeing its holes. Do not explain the story before they play. [ch. 9]
9. Do not patch missing animation with extra lines; the lines turn redundant once the animation lands. [ch. 9]

## Story keyed to progress, and who knows what

Two patterns from open-source games (ideas only, written fresh here; sources: voidstruck by vitaminclaude, and spookery by legend-of-alan, both on GitHub).

1. Beats on the progress number. When a game has one number that only moves one way (distance left, depth, days survived), key the story to it instead of a quest graph: a list of beats, each with a threshold, the text, an optional quest it unlocks and an optional reveal flag for the twist. A beat fires once when the number crosses its threshold. It needs no state beyond the number and a fired set, cannot dead-end, and pacing is tuned by moving thresholds. [voidstruck]
2. Pick a quest graph instead when the player chooses order or can fail a branch; beats on one number cannot express "either this or that". A mix works: beats gate which quests exist, the graph runs inside them.
3. Review checks for beats: no two beats so close the second buries the first; the reveal sits after the knowledge checkpoint it depends on; a player who rushes the number still sees every required beat.
4. Hidden facts with per-knower views. Store each fact once with the list of characters who know it, and give every viewer (a player, an AI game master, an NPC agent) only the facts their character knows. An AI GM or model player then cannot leak or act on what its character could not know; a secret is just a fact with one knower. [spookery, MIT agent and protocol crates]
5. Review check: for each secret, name who knows it and how others can learn it. A secret with no route to discovery is dead weight; one every viewer sees is not a secret.


## Failure patterns

- Fake choice. Symptom: a choice node with no visible consequence anywhere downstream. [ch. 5]
- Branch sprawl. Symptom: permanent branches added before the linear core works; scope grows faster than the story improves. [ch. 5]
- Optional-content dependency. Symptom: the critical path assumes a fact only taught in a side quest. [ch. 9]
- Railroaded player. Symptom: testers report they never felt free to decide, or characters act against motive to push the plot. [ch. 9]

Related: [worldbuilding-and-lore](worldbuilding-and-lore.md) (lore and canon), [playtesting](playtesting.md) (session scripts), [levels-and-space](levels-and-space.md) (environmental storytelling and pacing).
