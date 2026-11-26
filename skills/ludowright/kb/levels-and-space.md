# Levels and space

Answers: is this level, map or encounter plan well shaped, paced and teaching what it should. Load when reviewing or drafting a level plan, beat chart, wave plan or tutorial.

## Principles

1. Write one verb for the game and one goal per level (escape, explore, learn, survive), and check the geometry serves that verb. [Rogers LevelUp ch. 9; Totten; Bauer ch. 6-7]
2. Measure the world in hero units: height, passage width, speed, jump reach, weapon range, held in one editable place. Any new mover (vehicle, escort, bigger enemy) forces a re-check of corridors and gaps. [Rogers LevelUp ch. 5; Totten pp. 78-79]
3. Draw the level as a graph (rooms as nodes, links as edges, one-way and see-through links marked) and a map with a legend before building. Place set-piece rooms first, then connect them. [Totten; Rogers LevelUp ch. 9]
4. Decide alley or island. Corridors suit scripted beats and fixed cameras; open arenas give freedom but need landmarks and a next-step prompt. Alternate them. [Rogers LevelUp ch. 9; Bauer ch. 7]
5. Guide by landmark, light, line and constraint; guidance must be immediate, scarce, brief and clear. A landmark at each exit stops accidental backtracking. [Rogers LevelUp ch. 9; Gibson ch. 14; Totten]
6. Walking needs a purpose: rest, reward, reading the space or a tension build. A stretch that is only "then the player walks over there" gets cut or given something to do. [Rogers LevelUp ch. 5, 9; Totten on circulation and vistas]
7. Options per layout matter: how many exits, how often, where, at what rhythm. Longer lanes need more exits, and a dead end needs a visible risk and reward. [Bauer 7.4.4, 7.5.4]
8. A space needs several imperfect points of advantage so players move; one strong cover point at the entrance wastes the room. Cover with sight-line breaks makes back-and-forth fights, long open sightlines make cautious ones. [Bauer 7.5.3; Rogers LevelUp ch. 10]
9. Teach in stages: isolate one skill, repeat it, combine it, add danger, then raise difficulty. Show a hazard safely before it can kill. Lock before key: the player meets the problem, then gets the tool. [Gibson ch. 15; Totten pp. 184-186; Hodent ch. 12-13; Rogers LevelUp ch. 12]
10. Introduce two or three new things per level (the first level is the exception), pair each new threat with its answer, and keep the last quarter for using what was taught. Orchestrate in order: move and collect, one mechanic, a second, both, a hazard, enemies, enemies plus hazards, a twist. [Rogers LevelUp ch. 4, 12; Bauer 8.1.3]
11. Pace with a graph: beats scored 0 to 10 with durations, one top beat, quiet beats between, the last high beat as the highlight. Pacing is separate from difficulty. Intensity with no rest between is the commonest failure. [Bauer ch. 10; Totten pp. 82-84; Hodent ch. 12; Schell interest curve]
12. Do not stack big moments. Shift the player's emotion roughly every 15 to 20 minutes, and give a release (quiet room, supply cache) after a climax. [Rogers LevelUp ch. 9, 12]
13. Vary space and system: indoor and outdoor, wide and tight, elevation, light and colour. Never put the same gameplay system in two levels back to back. [Rogers LevelUp ch. 9]
14. Enemies are part of the space: soft walls, herders, pressure. Mix archetypes by synergy (blocker in front of shooter, big chaser with small flyers), engage the player with one or two at a time, and let the player choose the kill order. Give AI a readable objective, not only survival. [Rogers LevelUp ch. 11; Bauer ch. 14, 16; Totten]
15. Fairness: a new threat is shown before it hurts, no unseen instant death, no spawn in view or in melee range, no quick-turn patrols, no uncontested route or dominant vantage. Checkpoints face the way of travel, sit on flat ground, away from enemies. [Rogers LevelUp ch. 11-12; Bauer 14.3.3]
16. Never make an AI fight or boss the only gate; add an absolute (key, switch, timer). A finale where the last enemies must be hunted down is an anticlimax. [Bauer 16.1.2.1, 14.1.5.1]
17. Shortcuts are designed and priced as risk or skill; free bypasses skip content. Backtracking up to about twice is fine if the space changes on return. [Totten pp. 127-131; Rogers LevelUp ch. 9]
18. Resource-limited health makes exploring a risk decision; free regeneration plus checkpoints everywhere flattens it. [Totten p. 210]
19. Whiteblock before art, paper before whiteblock for flow. Keep a playground scene for metrics and an arena for spawning enemy mixes on demand. Build the tutorial last, or with fresh eyes. [Totten; Rogers LevelUp ch. 9; Bauer ch. 8; Gibson ch. 17]
20. Designers misjudge difficulty after many plays; judge challenge with new players, and balance late (ingredients, then per level, then global multipliers). [Bauer ch. 17; Rogers LevelUp ch. 13; Hodent]
21. Plan difficulty as pacing, not a ramp: put the hardest stretch early, then let it ebb and flow with breathers and mood. A steady climb tires players before the end. [Yu Part IV]
22. A zone of control (a short no-entry ring around each unit, lost when the unit is engaged or stunned) makes position a blocking tool for gaps, screens and rear protection. [Lambshead 2024, Zones of control]
23. When free play collapses into one degenerate pattern (a central melee scrum), reward the alternative (rear attacks are devastating) and give scenarios competing objectives in different parts of the map. [Lambshead 2024, Introduction to scenarios]
24. Schedule events with independent clocks, one per category: an on/off window (a few on-days, then off-days, a random count from a small range inside each window, a minimum spacing), a mean time between events, or one fixed day. Give threat clocks a start day (grace) and force the first threat to be a plain, readable one. Check the schedule with `ldw.py director`: it reports the longest gap, clumps and the first threat. [harvest: a colony sim's shipped data files, 2026-11]
25. Judge an open world by its density, not its size: count points of interest (a landmark, encounter, resource, secret or story beat) per minute of travel at the player's normal speed, along the routes players take. A bigger map with the same content is emptier, and every added square kilometre must earn its points or be cut. In 3D or underwater spaces count per volume the player can reach, not per map area. Rule of thumb, unverified by a book. [harvest: a solo developer's underwater sandbox postmortem, 2026-11]
26. Make a gate item a verb, not a key: it opens its gate and has at least one more use elsewhere (lights dark rooms, reveals hidden things, reaches a ledge), so old areas change when it arrives. Leave the order of gates to the player where the map allows, and show progress as the map fills in. A key useful only at its lock is a dead pickup. Live play owed to count uses per item and backtrack distance. [harvest: Animal Well, 2026-11-23]
27. For a one-session site, lay a five-role arc over the critical path: an entrance with a guardian, a puzzle or roleplay step, a setback that costs a resource (best the one the climax punishes), a climax with terrain that matters and a lever besides damage, and a reward with a twist or next hook. Steps 1 and 2 use different modes and spotlight different players. A role is a step, not a room: one role can span a maze, so keep loops around the path. `tt.py fiveroom` in tablewright checks a plan. [Johnn Four, 5 Room Dungeons, method section; one GM's advice, unverified]
28. Prep what the players will touch: an opening, about three leads (enough for a real choice, few enough to prep), people who each want something now, and a way for every fight to end early besides death or flight. Keep reusable parts (maps, foe groups, hazards) separate from places so they combine late. [Shea, The Lazy Dungeon Master, ch. V, XVII, XXI]
29. A trap has three parts: bait that draws the player in, a trigger, and a sense of safety that lowers the guard. Fire it just after a win or a rest, not where the player is already careful. [Book of Challenges p. 4]
30. Give an encounter a tactic, not just stats: box the player in, split the group rarely, deceive, drain one kind of resource, pair two effects that cover each other, or let the enemy escape to return later. [Book of Challenges p. 4]
31. A crowd fight should end on its own: let the number of minor foes drop sharply each round (about half), so the brawl peaks and fades without a hit-point grind. [Inns supplement p. 49]
32. Rest pressure is a pacing tool: when resting costs time or invites a threat, the player spends resources with care, and the space between fights becomes a choice. [Fast Combats]
33. Script a fight before running it: play it through in your head from both sides, note each spot where the foes struggle, answer each with one terrain feature, and repeat. Then test every patch of terrain: it has a purpose, offers a route choice, gives a reason to move, and is memorable. Two sides trading blows in place means the terrain is not working. [Wizards, 4e Dungeon Master's Guide p. 62-64]
34. Grade the climax. The party reaches it worn down by earlier fights, so a single pass-or-fail outcome turns attrition into a coin flip. Plan at least three outcome tiers (escape, drive off, full win) with the lowest reachable by a depleted party. [Advanced Gamemaster's Guide ch. 3 p. 56-57]
35. Give an encounter an objective other than "defeat everything" often enough that the party plans: make peace, guard someone, grab and carry something out, cross a gauntlet, slip in unseen, stop a ritual on a timer, remove one target from a crowd. A level with every room a kill-all room reads as one encounter repeated. [Wizards, 5e Dungeon Master's Guide (2014), Creating Encounters]
36. Make interactive features worth touching. Most levers, doors, chests and strange objects should help, inform or open a path, with only a few logical traps. A space where touching things only punishes teaches players to touch nothing. Count reward against punishment outcomes; a punishment-only set is a smell. [Kobold Guide to Dungeons p. 49-50]
37. Vary how long a setup waits for its payoff: many short pairs (a sign, then the thing it warns of a room later), a few long ones. Cap how many setups are open at once; too many unresolved threads make players anxious instead of curious. [Kobold Guide to Dungeons p. 14]
38. Show how a situation works (its physical, magical and social parts) so players can pick their own tools against it. Hide only the surprises you intend. A creative solution needs a readable system to work with. [Kobold Guide to Dungeons p. 14-15]
39. Of mood, story and player choice, a space can serve two well. Pick the two, write down which one is weaker, and accept it rather than half-serving all three. [Kobold Guide to Dungeons p. 80-83]
40. Alternate easy hordes with one overwhelming foe. Mowing down crowds shows the player's power, and the single foe makes that power felt by contrast. [ICRPG Vigilante City p. 32]
41. Lay the earliest paths first and let later buildings and roads follow them; a map grown that way reads as lived-in rather than planned on a grid. [Kobold Campaign Builder: Cities and Towns p. 35]
42. Tension rhythm for a session or chapter: open small, build, cut any scene that neither threatens nor advances, and end on a cliffhanger so the next one starts with a pull. [Slavicsek and Baker, 4e Dungeon Master for Dummies p. 135]

## How to apply

1. Fill a beat chart: a column per level, rows for goal, new element, enemies, hazards, pickups, expected minutes, intensity, light and music. Read across for clumping (too many new things), sameness, repeated colour or music, and late unlocks of the best tool.
2. Score each level's beats 0 to 10 in a pacing graph (`ldw.py curve` can check a curve if the numbers are in a table). Flag any run of three beats above 7 and any level whose top beat is not near the end.
3. Run the choice test on each fork: real problem, findable options, known consequences, meaningful outcome, right difficulty. A fork with no cue and nothing different behind each branch is arbitrary.
4. For every room list entry points, advantage points, cover, spawn points, items and expected time. Check a first-appearance beat exists for every new enemy and hazard.
5. For waves, compute simultaneous attackers, spawn visibility and the economy (health and ammo handed out against what the waves cost). `ldw.py economy` builds the faucet and sink table; `ldw.py sim` runs a seeded simulation. Name the player policy in any claim.
6. Record each finding with the room, the principle number and the fix. Mark feel-dependent findings `needs-playtest`.

Engine side (building, linting, playtest loops): the Level Up! references (one-pager, beat chart, playtest protocol) live in the game-design references of unity-agent, roblox-agent and madnesswright. Point to them; do not copy.

Per-encounter checks: a Timer (a visible countdown), a Threat and a Treat (a lever, item or weakness that rewards looking); Danger beyond damage, no lulls, one element of Wonder. Run the odd room with no timer. Gradient by distance: a safe hub, a frontier about a third out, danger rising with distance, a few hidden spikes near the start, no direct link from a starter area to end-game danger. [Runehammer, ICRPG Core, p. 84-86; Macris, Arbiter of Worlds, ch. 3 sec. 18, ch. 8 sec. 33]

## Failure patterns

- Pacing clump: intense encounters adjacent in the plan with no rest between. [Totten; Bauer]
- Metrics drift: corridor and gap sizes unchanged after a new mover or mechanic. [Totten]
- Unseen demonstration: a new hazard first met by killing the player. [Totten; Rogers LevelUp]
- Arbitrary junction: a branch with no cue and no difference. [Totten p. 192]
- Whole possibility space at once: all systems and districts open from minute one. [Totten]
- Dead goals: only a distant story goal, nothing short-term between. [Totten p. 260]
- Entrance dominance: one cover point controls the room. [Bauer]
- Single-point-of-failure gate: a boss or fight as the only barrier. [Bauer]
- Front-loaded toys: all new tools in the first level, or the best tool unlocked last. [Bauer 8.1.3]
- Repetition: same system twice in a row, same lighting and music in adjacent levels. [Rogers LevelUp]
- Target-death design: a plan stating the player dies N times here. [Rogers LevelUp ch. 12-13]
- Uncontested shortcut that skips content at no cost. [Totten]
- Free setback: a trap or reversal that costs the player nothing lasting. [Johnn Four, 5 Room Dungeons]
- One-key puzzle: a puzzle with a single solution and no clue planted earlier. [Johnn Four, 5 Room Dungeons]
- Prep sunk cost: steering players into content because of the effort spent making it. [Shea, The Lazy Dungeon Master, ch. V]

- Secrets marked by cracks, flashing or a sidekick prompt; a secret's key item useful only at its lock; a hidden reward strong enough to become the dominant route. Good secrets are hinted by the world, findable out of order and useful beyond their lock. [Yu Parts II, IV]
- Bosses that suspend the core rules (invulnerable until a puzzle, repeated). Prefer an upgraded regular enemy under the same rules, or a boss beaten through the core system. [Yu Part IV]
- Difficulty as one rising knob. Pace it: ebb and flow, a breather area, pain frontloaded, mood and suspicion later. [Yu Part IV]

## Where the books disagree

- When to hand over all tools: Rogers says by about three quarters, Bauer says most in the first two thirds. Ludowright treats it as a range and flags only key unlocks in the last quarter.
- Walking: Rogers says it is never gameplay, Totten values circulation and vistas as rest. Ludowright accepts walking with a stated purpose and flags walking with none.
- Random layouts: Bauer calls them costly, the procgen books defend them for replay-driven genres. Ludowright decides by whether replay is a pillar (see [procgen](procgen.md)).
- Adaptive difficulty: Rogers allows it, Bauer prefers fixed tested balance. Ludowright allows it only when offered by the player or invisible and switchable for testing.

Related: [ux-and-the-brain](ux-and-the-brain.md), [playtesting](playtesting.md), [procgen](procgen.md). Feel goes to game-juice (juice-scan, juice-principles). Engine work goes to unity-agent, roblox-agent, madnesswright.
