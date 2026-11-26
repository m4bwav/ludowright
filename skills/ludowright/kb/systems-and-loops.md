# Systems and loops

Answers: how do the game's feedback loops, emergence and decisions behave, and do the choices matter. Load it for loop censuses, snowball and stall reviews, "are these decisions meaningful", and Machinations-style modelling. Written 2026-10-29.

## Principles

1. A positive feedback loop amplifies a lead; a negative one pulls toward balance. A loop that is only positive runs away, one that is only negative stalls. Classify every mechanism as one or the other. [Salen ch. 18; Sellers ch. 7; Schreiber ch. 2, 12]
2. Every positive loop needs a stopping mechanism: a cap, a cost on the leader, hidden standings, a short game, or an ending. Every engine needs a friction and every escalation an end. [Adams ch. 6, App. B; Schreiber ch. 12; Fullerton ch. 10]
3. Negative feedback must not erase earned advantage. Rubber banding is a negative loop, so check the trailing bonus is not larger than the skill gap. [Adams ch. 4; Schreiber ch. 2; Salen ch. 18]
4. Describe each loop by type, investment, return, speed, range and durability. Two to four major loops is the working target: fewer is dull, more is opaque. This is a rule of thumb, not a tested threshold. [Adams ch. 6]
5. Classify each system as engine, economy or ecology and apply that type's known failures. Engines runaway or deadlock, economies inflate, ecologies lose a species. [Sellers ch. 7]
6. Odd-count counter sets self-balance; two-sided ones tend to snowball. Patching an overpowered option with a hard counter starts a counter spiral. [Sellers ch. 7, 9]
7. Resource relationships to map: source, drain, converter, trader. A converter loop where two resources fuel each other needs a floor income, or it deadlocks. [Adams ch. 4, App. B]
8. Emergence comes from specific parameter relationships. Simple rules can produce deeper play than complex ones. A scripted game gives progression, an emergent one gives replay; name which the design leans on. [Salen ch. 18; Adams ch. 2]
9. Elegance smells to check before adding a mechanic: it interacts with other systems, its role does not overlap another's, it reuses existing parts, its numbers share a scale, and it adds no content restriction on later content. [Sylvester ch. 2]
10. A decision needs partial predictability: consistent, comprehensible rules are a precondition for meaningful choice. [Sylvester ch. 5; Salen ch. 3]
11. A meaningful decision has impact, several viable options and enough information. Strictly better, blind, converging and hollow choices fail. Decision types: hollow, obvious, uninformed, informed, weighted, dramatic. Aim for weighted and informed. [Schreiber ch. 9; Fullerton ch. 11; Sylvester ch. 5]
12. Information starvation and information glut are opposite decision-killers. Starvation hides what a choice does; glut hands over the answer. [Sylvester ch. 5]
13. Option count is not depth. Inflating the number of near-duplicate options adds symbols, not thinking. Two truly viable strategies per situation is enough. [Sylvester ch. 2, 6]
14. Plan decision pacing by scope (moment, tactical, strategic). Hunt flow gaps (forced waits, unskippable animations) and overflow spikes. [Sylvester ch. 5]
15. Do not stack fast reflexive demand with deep strategy at the same moment. Count what a new player must learn at once. [Sellers ch. 4, 9]
16. Cognitive load caps how many interacting rules a player holds. Complexity creep (add a mechanic, remove none) raises the entry barrier. [Koster ch. 7-8]
17. A verb the player cannot observe, or a state change with no signal, should be questioned. Hidden critical state is a failure of feedback. [Sellers ch. 8; Salen ch. 3]
18. Dynamic difficulty is a feedback loop with a fairness cost: document its sensor, comparator and actuator, bound it, and keep it away from expert exploitation. [Salen ch. 18; Sylvester ch. 3; Schell ch. 13]
19. Give the player, monsters and items one shared physical ruleset. When a rock, an arrow trap and a thrown monster all obey the same rules, simple systems meet and players tell the stories themselves. [Yu Parts I, III]
20. A free wild source must yield clearly less per hour of work than the invested source it competes with, or the investment has no reason to exist. Measure both on the same worker: in one test a forager on wild bushes out-earned a watered field fivefold until regrowth was slowed about fourfold. [harvest: a colony sim, 2026-11-22]
21. Turn a meter's extreme into a visible one-off event owned by one character, then reset the meter part way (to about 40-60%). A silent floor hides the crisis: in one test a third of a town sat at zero for over a hundred person-days with nothing on screen. [harvest: a colony sim, 2026-11-22]
22. A named bonus for completing a small set of pieces in one area turns placement into a goal. Show what is missing from the set. Only cancel the bonus for an area that qualifies twice when specialising is the point. [harvest: a colony sim, 2026-11-22]
23. Upgrade a card by filling a small, fixed number of slots with modules, not by swapping it for a stronger copy. The slot count is the budget: each module is a choice against the others, and the card stays recognisable. Pair it with capacity zones, where each zone holds a set amount and a building placed there changes that zone's rules, so placement and upgrades trade against one space limit. [harvest: Monster Train 2, 2026-11-23]
24. Present a decision as a situation card with typed commit slots (only certain kinds of card fit each slot), two clocks (how long it lingers unanswered, how long committed cards stay locked once it resolves) and outcomes in bands by what was committed. Always offer a legal ignore branch with its own known cost, so passing is a choice and not a failure. [harvest: Sultan's Game, 2026-11-23]
25. A deduction puzzle confirms a set of guesses all or nothing, and only after each term has appeared in several contexts. Feedback says whether the set is right, not which entry is wrong, and a check unlocks only when enough clues exist to solve it by reasoning rather than by trying every pairing. [harvest: Chants of Sennaar, 2026-11-23]
26. Build item synergy from a small trigger vocabulary (adjacent, one direction, empty neighbour) times a list of effects: a few rules give many distinct items, and directional triggers make rotation a decision. Count an empty cell as a neighbour type so gaps become a choice, not waste. A one-row slot layout supports the same idea with left, right and empty-beside triggers. Highlight the cells a placement will read and preview the change before the drop (feel belongs to game-juice). [harvest: Backpack Hero, 2026-11-23]
27. Let buildings on a grid read their neighbours (a bonus or a penalty per adjacent type), so placement is a choice and not only a target. Let a beaten threat offer a pick from its own themed cards, so each threat doubles as deck growth and the player chooses which threats to face for the loot. Keep the neighbour rules few enough to track by eye; live play owed to count how many a player follows. [harvest: 9 Kings, 2026-11-23]
28. Base-management loop: let the number of actions per turn jump at population thresholds, offer a dearer option that succeeds for sure beside a cheap risky one, and run a raid timer with a minimum gap so a threat returns but never stacks. [Posner, A Goblin's Tale DMG p. 6-7]
29. A failed craft or build roll should start an event (a flawed item, a visitor, a debt), not just return nothing. A null result teaches retrying, an event adds story. [GM Gems p. 3]
30. Button-press check: if one option of a choice is always right once the player knows the rules, it is a button, not a choice. Give each option a cost or a context where it wins. [Panshin p. 154-155]
31. Model a long task as a monster: a progress pool, a fixed count of milestones, and a big single result that also scores a milestone. Set a timer to milestones times the time per attempt, then tune. Cap milestone perks at one, or late tasks turn trivial. [Fallout 2d20 GM Toolkit p. 4-6]
32. Reputation as a named ladder (hostile to allied, about six rungs), each rung saying what trade, help and shelter the faction gives. Score a quest's effect from short yes or no lists of what the faction liked and disliked, and only for factions that were involved or watching. [Fallout 2d20 GM Toolkit p. 7-8]
33. Make a harder encounter harder on at least two of three axes: damage (what one hit costs), disruption (terrain or hazards that change what actions are good) and duration (a clock that ends the fight on the enemy's terms). Raising only hit points makes the fight longer, not harder. [Runehammer, ICRPG Master Edition p. 94-95]
34. When the player tries something the rules do not cover, rule for the fantasy the game promises, not for the nearest specific rule: allow the attempt, set the odds from the situation, and resolve it. A system that answers "no rule, so no" teaches players to stop trying. [Kobold Guide to Roleplaying p. 110]
35. Offer a trade of certainty now for lockout later: a guaranteed effect that is then disabled until the next rest. The player spends a future option to remove this turn's luck. [Runehammer, ICRPG Magic p. 19]
36. Gate the next tier of a power by how many of the tier below the player already owns, so progress reads straight off the collection shown on screen. [Runehammer, ICRPG Magic p. 19]
37. If every build can do everything, no character needs another and cooperation has no reason to exist. Give each role something only it covers. [Runehammer, ICRPG Worlds p. 14]
38. Unlimited mobility needs a scarce fuel and a limit the player does not control (weather, a timer, a hostile zone), or the map stops mattering. [Runehammer, ICRPG Worlds p. 66]
39. Let every hit drain a small second resource that refills fast, beside the slow main pool. Attrition then bites even tough characters within one fight without making it longer. [ICRPG Vigilante City p. 12]
40. Split a vehicle's or boss's damage across parts, each tied to one function, so it loses abilities one at a time and the fight changes shape as it goes. [ICRPG Altered State p. 35]
41. Keep improvised actions (anything a player tries outside the listed moves) weaker than a character's authored abilities. Otherwise the improvised option becomes the best one and the abilities lose their reason to exist. [Slavicsek and Baker, 4e Dungeon Master for Dummies p. 139]
42. Make command a budget: leaders spend points to act, and friction (distance, disorder, broken lines) raises the price, so not every unit moves every turn. [Autarch, Domains at War Battles p. 18]
43. Trigger morale on thresholds and resolve the checks one at a time in an order the side chooses, so one rout can tip the next and armies break in cascades. [Autarch, Domains at War Battles p. 23, 26]
44. Treat fatigue as a debt to repay with rest, not a speed cap: forced effort now buys a cost later. [Autarch, Domains at War Campaigns p. 55]
45. Fortifications turn a numbers fight into a frontage fight: only so many attackers fit, and damage to the walls widens the gap. [Autarch, Domains at War Campaigns p. 77]
46. Give every detailed subsystem an off-screen shortcut (one roll or a table) for when it is not the focus. [Autarch, Domains at War Campaigns p. 86]
47. Make travel a clock: roll on a fixed cadence (per day, per watch) rather than on whim, and let player choices move the odds, such as a cold camp lowering the night chance. [Assassin Games, Wilderness Encounters p. 2-3]
48. Keep random travel events mostly non-combat, and end the fights that do happen on morale so they stay short. Check the table's combat share. [Assassin Games, Wilderness Encounters p. 2, 4]
49. Chain encounters: let an event arm a later one (a clue leads to a site and a reward, or a scuffle brings a raid next watch). [Assassin Games, Wilderness Encounters p. 4, 15]
50. An influence game across factions: give the player a few actions to spend among factions whose scores stay hidden, show only a coarse public signal per faction (leaning, wavering, opposed), and resolve the outcome in public. Check that the signal tells the player enough to choose where to spend. [Trail of Tyranny p. 33-35]
51. Stage a damage-over-time effect: an onset effect, then a repeat effect on an interval. The interval decides use (per round reads as combat, per hour or day as intrigue), and the delivery route (touch, food, air, wound) is where counterplay lives. Run `ldw.py dot` to see expected ticks, total damage and the escape chance in the first few ticks; a resist that only falls with no end point is a death spiral. [Poisons p. 2-4]
52. Mark each escalation of a threat by breaking a rule players have learned about it (it now crosses running water, it now hunts by day), and make each break visible when it happens. [Open Grave p. 35]

## How to apply

Loop census (one table, from docs and code):

1. List every resource and give it a role: source, drain, converter or trader.
2. List every loop: what feeds what. Tag positive or negative, who it favours (leader, trailer, everyone), its speed, and where it is capped.
3. Count major loops. Fewer than two or more than four is a finding to explain, not an automatic fault.
4. For each positive loop ask: what stops it, and is the stop visible to the player before the spin-out? For each negative loop ask: does it erase earned advantage?
5. For an engine, remove randomness first to see structure, then add it back one place at a time. A strategy sweep on any scaling numeric choice (units built, upgrades bought) shows dominant invest-or-spend paths. [Adams ch. 6, 8]

Decision audit, per decision point:

1. What does the player know, and what are they choosing between?
2. Is one option best in every situation? Is any option dominated (no better in any column and not cheaper)? Is every option's outcome effectively the same?
3. Does the choice change state, and does that change reach a later decision?
4. Is there a way to tell what the choice did afterward?

Tools: `ldw.py sim` with a `walk` model turns a declared loop into turns-to-threshold and spread (how long a snowball takes); `economy` shows whether a loop's resource has a drain. Declare the player policy for every simulated claim; a sim of identical strategies proves little. [Adams ch. 8; AI-playtesting research 2026-10-29]. Table shapes are in [balance-tables](balance-tables.md).

Machinations patterns to reuse when modelling: source into pool into drain; a converter between two pools with a floor source; a register that gates a loop when a stock crosses a threshold; a trigger that fires a negative loop once a lead is large. Report distributions over simulated players, not one average, and name the persona behind each run. Treat a model as a simplification whose numbers were chosen by feel.

## Failure patterns

- Single-counter roster: every foe in a group falls to the same answer (one damage type, one tactic); pair foes so one covers another's weakness. [Webb, Book of Dirty Tricks, p. 56-57; tabletop advice, unverified for video games]
- Runaway leader: gains scale with current lead (income, XP, snowball cards, win-more effects) with no cap or catch-up. Symptom: winner obvious halfway through. [Sellers ch. 7; Salen ch. 18]
- Snowball loss with no comeback: destructive positive feedback, no lever for the trailer. [Adams ch. 6; Costikyan ch. 5]
- Surprise swing: slow, strong indirect negative feedback that flips outcomes late. [Adams ch. 6]
- Deadlock loop: a resource needed to earn that same resource, with no free start. [Sellers ch. 7; Adams App. B]
- Dragging brakes: upkeep or decay that can exceed income in normal play. [Sellers ch. 7]
- Rubber band opacity: adaptation invisible to players who would call it cheating, or large enough that outcomes ignore play. [Salen ch. 18; Adams ch. 4]
- Dominant strategy: one option best in every situation, or one that rivals must always answer. [Salen ch. 21; Sellers; Sylvester ch. 6]
- Self-feeding tool: output raises the input with no cost. [Sylvester ch. 6]
- Counter spiral: patches that add hard counters to cap one option. [Sellers ch. 7]
- Role overlap and gimmick: two items with one niche, or a mechanic used once and touched by nothing. [Sylvester ch. 2]
- Content restriction: a new capability that constrains every later level, card or encounter. [Sylvester ch. 2]
- Information starvation or glut: choices made before the player can learn what they do, or a tool that reveals the answer. [Sylvester ch. 5]
- Flow gap: cooldowns with nothing else to do, unskippable animations, freeze-stuns. [Sylvester ch. 5]
- Unrecoverable error: an early slip silently ruins the later game. [Adams ch. 2]
- Reactive balancing: patches fix one strategy and shift another; nobody checked the unaffected ones. [Sylvester ch. 6]
- Letter-versus-spirit loophole: legal by written rules but breaks implicit ones (stalling, kingmaking). [Salen ch. 21]
- Micromanagement: tasks that could merge into one decision. [Fullerton ch. 11]

## Where the books disagree

- Vocabulary: Adams uses engine, friction and escalation; Schreiber and Sellers use sources, sinks and positive or negative feedback. We map the first to the second in notes and use the second in findings so tool output and docs agree.
- Viable-strategy count: common balance talk says more viable strategies is better; Sylvester rejects counting. We follow Sylvester: ask whether strategies differ in situation and style, not how many exist.
- Hidden adaptation: Schell warns against dynamic difficulty, Sylvester allows a concealed, bounded version for low-skill audiences. We allow it only bounded, optional and documented, and flag it when an expert could exploit it.
- Identity knobs: Sylvester says lock a tool's identity and cut what cannot survive; for small indie scope that is costly. We report the cut as an option next to the retune.

Related: [core-loops-and-goals](core-loops-and-goals.md), [balance-and-economy](balance-and-economy.md), [uncertainty](uncertainty.md), [review-heuristics](review-rubric.md), [game-ai-for-designers](game-ai-for-designers.md). Feel goes to game-juice's juice-scan and juice-principles. Engine-side implementation goes to unity-agent, roblox-agent and madnesswright.
