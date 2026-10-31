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

## How to apply

1. Fill a beat chart: a column per level, rows for goal, new element, enemies, hazards, pickups, expected minutes, intensity, light and music. Read across for clumping (too many new things), sameness, repeated colour or music, and late unlocks of the best tool.
2. Score each level's beats 0 to 10 in a pacing graph (`ldw.py curve` can check a curve if the numbers are in a table). Flag any run of three beats above 7 and any level whose top beat is not near the end.
3. Run the choice test on each fork: real problem, findable options, known consequences, meaningful outcome, right difficulty. A fork with no cue and nothing different behind each branch is arbitrary.
4. For every room list entry points, advantage points, cover, spawn points, items and expected time. Check a first-appearance beat exists for every new enemy and hazard.
5. For waves, compute simultaneous attackers, spawn visibility and the economy (health and ammo handed out against what the waves cost). `ldw.py economy` builds the faucet and sink table; `ldw.py sim` runs a seeded simulation. Name the player policy in any claim.
6. Record each finding with the room, the principle number and the fix. Mark feel-dependent findings `needs-playtest`.

Engine side (building, linting, playtest loops): the Level Up! references (one-pager, beat chart, playtest protocol) live in the game-design references of unity-agent, roblox-agent and madnesswright. Point to them; do not copy.

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

- Secrets marked by cracks, flashing or a sidekick prompt; a secret's key item useful only at its lock; a hidden reward strong enough to become the dominant route. Good secrets are hinted by the world, findable out of order and useful beyond their lock. [Yu Parts II, IV]
- Bosses that suspend the core rules (invulnerable until a puzzle, repeated). Prefer an upgraded regular enemy under the same rules, or a boss beaten through the core system. [Yu Part IV]
- Difficulty as one rising knob. Pace it: ebb and flow, a breather area, pain frontloaded, mood and suspicion later. [Yu Part IV]

## Where the books disagree

- When to hand over all tools: Rogers says by about three quarters, Bauer says most in the first two thirds. Ludowright treats it as a range and flags only key unlocks in the last quarter.
- Walking: Rogers says it is never gameplay, Totten values circulation and vistas as rest. Ludowright accepts walking with a stated purpose and flags walking with none.
- Random layouts: Bauer calls them costly, the procgen books defend them for replay-driven genres. Ludowright decides by whether replay is a pillar (see [procgen](procgen.md)).
- Adaptive difficulty: Rogers allows it, Bauer prefers fixed tested balance. Ludowright allows it only when offered by the player or invisible and switchable for testing.

Related: [ux-and-the-brain](ux-and-the-brain.md), [playtesting](playtesting.md), [procgen](procgen.md). Feel goes to game-juice (juice-scan, juice-principles). Engine work goes to unity-agent, roblox-agent, madnesswright.
