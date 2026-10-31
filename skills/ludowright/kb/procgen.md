# Procedural generation

Answers: whether a game should generate content, how much authorial control to keep, and how to judge a generator, including AI-generated levels. Load when reviewing a generator spec, a seed-based mode, or any pipeline that uses a model to make levels or items.

## Principles

1. State the generator's role first: integral to the game, a drafting aid for designers, modal (a separate mode), or segmented. The role sets the schedule risk and the fallback if it fails. Also say who holds initiative: designer, player or machine. [Short ch. 1; Shaker ch. 1]
2. Do not generate what you cannot make by hand well. Hand-made exemplars define the quality target. [Short ch. 2]
3. Aim for pleasant surprise. The two failure poles are samey (oatmeal: many different bowls that taste the same) and chaotic; constraints move output between them. [Short ch. 2, 4]
4. Mark content necessary or optional. Necessary content (connectivity, solvability, the key before the door) needs hard guarantees; optional content may fail softly. [Shaker ch. 1; Short ch. 1, 11]
5. Players treat any unfair-looking level as typical of the game, so solvability is a trust issue as well as a correctness one. [Short]
6. Vary circumstances, not outcomes. Random setup, filler and genres built on it are fine; randomness attached to a player's choice or to information they rely on feels like cheating. Scheduled variation (pity timers, weighted reduction of repeats) beats pure probability for important events like bosses, shops and healing. [Short ch. 2; Bauer 7.2.4.2]
7. Reliability, controllability, expressivity and speed trade off; name which one the design buys. Constructive generation is fast, generate-and-test is valid but slower. [Shaker ch. 1-2]
8. Define the control surface: seed, parameters, a feature vector, sketches. Check that parameters actually change the output. [Shaker ch. 12]
9. Think in combination space: count combinations, count the null zone, build modules on a shared mechanic substrate, keep impact comparable, avoid overlap. Cycles and graphs before tiles give loops, shortcuts and lock-and-key patterns. [Short ch. 4; Short, graphs]
10. Stay inside the hero metrics, use templates and symmetry, and mix hand-made set pieces with generated filler. A system used fewer than three times is not worth building. [Rogers LevelUp ch. 9]
11. Keep a deterministic seed so runs replay, share and debug. [Short ch. 12; Shaker]
12. PCG cannot replace core mechanics. "Every atom procedural" is a risk when the loop is thin. [Short ch. 1]
13. Evaluate a generator by its distribution over many runs, with metrics at a distance from the input parameters, never by eyeballing five outputs. Sample until the distribution stops changing. [Shaker ch. 12; Short ch. 22]
14. Three evaluators: direct metrics on content, simulated agents, human judgment. Match agent skill to the question (playable versus enjoyable) and check agent results against human data. [Shaker ch. 2; Yannakakis]
15. A heuristic that fixes one failure often creates another (an empty start area). Test generator tweaks with player data, not only the target metric. [Short]
16. Reuse the generator's validity checker as a machine playtester for hand-made content. A well-validated generator moves early playtest effort from reachability to fun. [Shaker]
17. AI-generated levels need a repair and reachability pass, because they are not playable until a solver checks them. In one set of snake levels playability was 87 percent when easy and 36 percent when hard. [AI playtesting note, finding 6]
18. Random layouts need readable systems under them, or the variety is a slot machine. A few fixed secrets, the same in every seed, make a random world feel like a real place. [Yu Parts II, III, IV]
19. Guarantee only the critical path: entrance to exit with no consumable spent. Side rooms may stay sealed when the player can dig, bomb or climb in. [Yu Part I]

## How to apply

1. Decide whether to generate at all: is replay a pillar, can you hand-make good exemplars, is there a fallback? If not, hand-author. Bauer's cost scepticism wins when replay is not the pillar.
2. Classify the generator on the axes: necessary or optional, functional or decorative, stochastic or controllable, constructive or generate-and-test, runtime or offline, autonomous or mixed-initiative.
3. Write the guarantees: for necessary content list the invariants (start connected to exit, key reachable before lock, no spawn in view of the player, items within metrics).
4. Pick the metrics (examples: path length, number of branches, enemy density, resource per room). Generate a few hundred seeds, plot each metric, check the expressive range against exemplars, then change parameters and see that the plot moves (controllability).
5. For the economy of generated loot or waves use `ldw.py economy` and `ldw.py ev`; for outcome spread over seeds use `ldw.py sim` with fixed seeds, reporting p05, p50 and p95 and naming the policy.
6. For AI-generated levels: parse into a grid or graph, run reachability and solvability, repair or reject, record the reject rate by difficulty, and keep the accepted seed. Then a human plays a sample.
7. Check for oatmeal: do two outputs differ in anything a player would notice? Cluster by metric and by a visual look; low variance across clusters is oatmeal.
8. Check for over- and under-constraint (below).

A cheap generator that hides its seams: a small grid of rooms, a guaranteed path drawn first, each room filled from a template typed by its openings, some random cells and small chunk pools inside the template, then a second pass that places entities from the tiles around them. Write the generator's rules (entrance, exit, path with no items needed, no softlocks) before the code. [Yu Part I]

## Failure patterns

- No role statement or fallback in the spec. [Short ch. 1]
- No exemplars: generator specified with no hand-made reference. [Short ch. 2]
- Oatmeal: very different seeds, same experience. [Short]
- Over-constrained: one enemy or layout dominates because constraints stack. [Short ch. 2]
- Under-constrained: out-of-depth enemies, impossible placements, start-area ambushes. [Short ch. 2, 4]
- Outcome randomness: a random result decides a run with no counterplay. [Short; Bauer]
- Pure-probability spawns for key events with no schedule or pity. [Short]
- Counterfeit or overshadowing modules; direct set-piece coupling. [Short ch. 4]
- No seed-level solvability check. [Short ch. 1, 11; Shaker]
- Seed-only encoding fed to an optimiser; runaway objective in a weighted fitness sum. [Shaker ch. 2]
- Generator ships without any player-facing quality test, only designer eyeballing. [Shaker ch. 12]
- Wave rule chosen without checking snowball, stalling or fatigue. [Short ch. 14]
- Procedural claims that outpace the core loop. [Short ch. 1]
- LLM-made level accepted with no solver pass. [AI playtesting note]
- Consumables spent on generator repair: the layout can need a bomb, key or tool just to reach the exit. Guarantee a critical path that needs no consumable; a softlock test proves it. [Yu Part I]
- Random contents rolled on open (chests, crates) instead of at generation, so a fixed seed does not fix the run and daily or shared seeds break. [Yu Part III]
- Spawn odds set flat across an area; relative rarity and tiers within an area matter more than absolute odds, tuned by ballpark then play. [Yu Parts I, III]

## Where the books disagree

- Bauer treats random layouts as costly and rarely worth it; Short and Adams treat them as a pillar for replayable genres. Ludowright decides by whether replay is the pillar, and hand-authors otherwise.
- Shaker's metric examples (linearity, leniency) come from research prototypes and are not a standard set. Ludowright asks for metrics chosen for the game, independent of the inputs.
- Player-adaptive content: Shaker covers it, Rogers is more cautious (offered, not forced). Ludowright requires a stated player model, a visibility policy and an off switch for comparison.
- The books predate language-model generators. Ludowright borrows their tests but adds the repair and reachability pass from newer work.

Related: [levels-and-space](levels-and-space.md), [ux-and-the-brain](ux-and-the-brain.md), [playtesting](playtesting.md). Feel goes to game-juice (juice-scan, juice-principles). Engine implementation goes to unity-agent, roblox-agent, madnesswright; the Level Up! level references live there.
