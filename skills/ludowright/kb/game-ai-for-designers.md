# Game AI for designers

Answers: how should an opponent or NPC behave, how hard should it be, and which architecture fits. Load for enemy, ally, boss or bot design and for fairness reviews of AI.

## Principles

1. Success is fun and believability, not technique. Spend the smallest AI that meets the design goal. [Bourg ch. 1; Aversa ch. 1; Millington ch. 2]
2. Match depth to the perception window: how long and how closely the player watches the character. Incidental NPCs get two readable states. [Millington ch. 2]
3. The visible change of behaviour (spotted, alerted, fleeing) is what players notice. Animation, barks and gaze are a design deliverable, not decoration. [Millington ch. 2; Rabin ch. 1; Buckland]
4. Players read AI strategy, randomness and cheating poorly. Do not spend budget on subtlety they cannot perceive; build opposition from legible differences (health, speed, range). [Rabin ch. 4]
5. Players invent motives for accidental behaviour. Audit tie-breaks and target selection for biases they will read as hatred or favouritism. [Rabin ch. 4]
6. Sell fairness through senses: view cone, occlusion, hearing range, short-term memory of last-known position. Omniscient AI reads as cheating. [Buckland; Millington ch. 6, 11]
7. Difficulty levers, cheapest first: reaction delay (a few tenths of a second as a start), aim error, memory span, detection range, per-type bias. Expose them as data per enemy type. [Buckland; Millington ch. 14; Rabin ch. 1]
8. Visible error severity matters more than average error rate. A strong AI making a mistake no human would make breaks belief. [Rabin ch. 4]
9. Cheating is normal and acceptable when hidden, bounded and downward only. Quietly weaken the AI; never quietly strengthen it. Visible or upward cheating draws accusations. [Bourg ch. 1; Rabin ch. 4; Millington ch. 6]
10. Fairer than cheating: let the AI gather information (scout) and infer. [Bourg ch. 1]
11. Melee and action enemies are a timing design: telegraph, active, recovery, consistent response, light randomness. Learnable patterns are a feature. [Millington ch. 14; Yannakakis ch. 4]
12. Multi-enemy fights need a rate cap (attack tokens or a shared accuracy budget) so damage per second is tunable. Deliberate misses must look like pressure, not generosity. [Rabin ch. 33]
13. Both too-perfect and too-dumb opponents fail. Plan a mistake budget: where and how often the AI errs on purpose. [Aversa ch. 1; Buckland]
14. Add variety with light randomness around a deterministic core; isolate the nondeterministic part so it stays testable. Weighted choice among good options beats foolish moves. [Bourg ch. 1; Sutton ch. 2]
15. Avoid threshold cliffs and frame-by-frame oscillation between near-equal options: use smooth scores, a commitment bonus or a cooldown. [Buckland; Rabin ch. 13]
16. Learning AI is a testability and control risk. Constrain it to inspectable parameters and bound adaptation so tuned balance survives. [Millington ch. 7; Togelius ch. 8]
17. Companions fail more visibly than enemies (blocking, bad prediction). The player must stay the top decision-maker. [Millington ch. 6; Yannakakis ch. 4]
18. Turn-based and card opponents face unlimited human thinking time. Design rules so the AI can search or evaluate them, and give the AI distinct choices to make. [Millington ch. 6; Rabin ch. 4]
19. Make the AI legible when planning against it is the fun: visualise intent. AI-centred designs can use five patterns: visualised, role model, trainee, editable, guided. [Togelius ch. 8]
20. Ask whether a genre convention is deliberate design or a workaround for old AI limits before copying it. [Togelius ch. 8]
21. Cheap state machines go far: a shopkeeper with four states can feel alive. Several simple monsters attacking from different directions read as coordination with no shared planner. [Yu Parts I, III]
22. Behaviour trees handle success and failure well but cope badly with outside interrupts and threshold switches (an alarm, low ammo). The usual fix, a state machine over trees, means two authoring formats; budget the tooling for both. [Millington ch. 5]
23. Grow the enemy playable at every step: a minimal version first, then branches, shared sub-trees by name, rare-case sub-trees only when a playtest first needs them. [Millington ch. 5]
24. Path cost is a design lever. Mix distance with danger and exposure, weight it per unit type (a scout avoids open ground, a tank does not), and smooth paths so units do not zigzag. [Millington ch. 4, 6]
25. Favour data over code: techniques designers can tune in an editor win, and level knowledge comes from markup or an offline bake. Build AI inputs for flexibility first, because designers ask for new inputs late; optimise afterwards. [Millington ch. 12, 14]
26. Budget AI per frame and run each layer at its own rate: movement every frame, sensing less often, tactics every few seconds. A character that freezes while it plans looks dumb, so it moves on a rough answer first. Detail follows what the player would notice, not distance alone. [Millington ch. 10]
27. Give the player verbs that write into the AI's senses or memory: a knock, a thrown object, a decoy that sets the guard's last-known position and sends it to investigate. A stealth enemy with that memory becomes a puzzle the player plays, not just a hazard. Each lure needs a readable reaction and a cap, so it cannot loop a guard forever. [Cossu ch. 5]

## How to apply

1. Write the behaviour list first, as what the player sees in the first ten seconds of the encounter. Then choose the cheapest architecture.
2. Architecture by design need, not fashion: state machine when designers must read and tune it; behaviour tree for layered reactive behaviour; utility scoring when designers should own preferences as data; planners only when sequences must emerge; search for turn-based with a clear score. Implementation (steering, pathfinding, sensors, trees) goes to unity-agent.
3. Run the fairness table: for each piece of information the AI reads, can the player know it? If not, is it disclosed, capped and downward?
4. List difficulty knobs per enemy type. Missing knobs mean tuning by rewriting code.
5. Check telegraphs: windup, active, recovery, reaction delay, consistent responses.
6. Compute worst-case burst: all active enemies hitting at once. `ldw.py ev` gives expected damage per attack; `ldw.py sim` can run a fight model with fixed seeds. If worst case is a spike, propose tokens or a cap.
7. Compute streaks: chance of five misses in a row at the stated hit rate. If it hurts, propose a pity counter or streak cap.
   - Before reaching for the costly ones: a random or weighted pick before utility scoring; a fuzzy blend for gradual mood (bravery building up), with few inputs; smart objects that advertise what they offer before goal planning; scripted set pieces where a sequence must land, each with a fallback; blackboards rarely. Learning only after comparing its cost (data, validation, wrong lessons) with hand-authoring. Assistive AI that acts for the player can reuse enemy modules only when they work without a global strategy. [Millington ch. 2, 5, 7, 14]
8. Pick the test axes for a bot or test agent: win versus experience, player role versus non-player role. List the human limits it models (reaction time, errors, pauses). See [ai-as-design-tool.md](ai-as-design-tool.md).
9. Playtest questions: ask what players think the AI is trying to do and compare with the truth; ask whether anything felt like cheating. Do not ask players to state how the AI works.

## Failure patterns

- Over-engineered enemy. Symptom: learning or planning whose output looks like a two-state machine. [Millington ch. 2]
- Silent AI. Symptom: few animations, barks or reactions per behaviour. [Rabin ch. 1]
- Relentless AI. Symptom: pursuit with no pause, back-off or hesitation. [Rabin ch. 1]
- Omniscient AI. Symptom: code reading hidden player state with no sense or delay. [Buckland; Millington ch. 6]
- Instant reactions. Symptom: zero reaction delay, perfect aim, frame-perfect parry. [Millington ch. 14; Rabin ch. 1]
- No memory. Symptom: enemy drops all knowledge once the player leaves sight. [Buckland]
- Hard-coded skill. Symptom: accuracy and reaction values inline rather than per-type data. [Buckland]
- Unreadable telegraph. Symptom: attacks without windup or with inconsistent responses. [Millington ch. 14]
- Damage spike from crowds. Symptom: no cap on simultaneous attackers. [Rabin ch. 33]
- Visible generosity. Symptom: obviously deliberate misses. [Rabin ch. 33]
- Accidental story. Symptom: tie-break by name, order or position. [Rabin ch. 4]
- Decision oscillation. Symptom: no commitment bonus or cooldown. [Rabin ch. 13]
- Opaque cheating. Symptom: AI income, vision or rolls differ from the player's with no disclosure or cap. [Bourg ch. 1; Yannakakis ch. 4]
- Unconstrained learning. Symptom: online adaptation with no replayable learned state. [Millington ch. 7; Bourg ch. 1]
- Unbounded adaptation. Symptom: difficulty drift outside the tuned balance. [Togelius ch. 8]
- Teammate overrules player. Symptom: squad plans that fight the player's movement. [Millington ch. 6]
- Undifferentiated choices. Symptom: all AI options give about the same outcome, so sophistication is invisible. [Rabin ch. 4]
- Opaque AI mechanic. Symptom: the design says outsmart the AI but gives no way to read it. [Togelius ch. 8]
- Streaky randomness. Symptom: 50 percent chances with no streak protection. [Aversa ch. 3]
- Missing alarm beat. Symptom: a designer-authored tree with no visible disposition change (alerted, panicked) between calm and attacking. [Millington ch. 5]
- Scripted sequence with no fallback. Symptom: a set piece that stalls or breaks when the player blocks, kills or skips part of it. [Millington ch. 5]
- Learners that fight each other. Symptom: several learning parts tested alone, each one task, never together. [Millington ch. 7]

## Level-AI handoff checklist

Level design and AI are one job; hand the level team this list. [Millington ch. 4, 6]

- Passages wide enough for the AI that must move through them, in groups where it moves in groups.
- Cover, sniper and other tactical points placed and tagged by hand, with a debug view that draws them.
- Jump, drop and climb links marked where the navigation cannot find them.
- Simple tags (cover, sniper, ambush) first; runtime tactical analysis only when tags fail a playtest.

## Where the books disagree

- Predictable (Millington) versus adaptive enemies (director systems). Ludowright defaults to predictable for action and platform games, where learnable patterns are the skill, and allows a director only when it tracks one validated signal and is bounded. [Yannakakis ch. 4, 10]
- Cheating: Millington and Buckland warn it gets caught, Rabin ch. 4 suggests quiet help. Ludowright allows it downward only and invisible, and never upward.
- Players cannot identify AI strategy or cheating (Rabin ch. 4) versus perception fidelity (Buckland). Ludowright keeps fair senses for stealth and shooters, where players judge them, and spends nothing on hidden subtlety elsewhere. Rabin's study was about a dozen students and one game: a strong anecdote.
- Research favours learning (Yannakakis); industry uses trees and machines. Ludowright does not recommend learning for enemy behaviour by default.
- Lose more often than win (Buckland) is a default, not a law for hard-challenge games.

Related: [production-and-scope.md](production-and-scope.md), [ai-as-design-tool.md](ai-as-design-tool.md), [feel-handoff.md](feel-handoff.md). Telegraph animation, miss presentation, startle cues and gaze go to game-juice (juice-scan, juice-principles). Steering, pathfinding, behaviour trees, utility, sensors and tokens implementation go to unity-agent, roblox-agent, madnesswright. Dice and streak maths: ldw.py ev; uncertainty theory lives in the uncertainty kb file when present.
