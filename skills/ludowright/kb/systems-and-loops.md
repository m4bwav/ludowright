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
