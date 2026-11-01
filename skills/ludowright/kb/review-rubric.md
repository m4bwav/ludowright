# Review rubric

Use: the review skill walks every item below against the game's docs, data and code; each failing item becomes a finding in the JSON contract (validated by `python scripts/ldw.py findings validate`). Item IDs are stable: never renumber, only append.

## How to run

1. Restate the game's intent and its kind first: shipped once or live service, real-time or turn-based. Severity hints change with the kind.
2. Read the docs, then the data tables, then the code. Do not start from code.
3. Walk every item. For each, write a finding or move on. "No issue found" is a valid outcome; a review where every item fails is suspect.
4. Evidence must cite rules text, a number or a line of code. No evidence, no finding.
5. A finding traces rule, then dynamic, then player experience, and names who it hurts (new players, experts, one persona).
6. Run the named `ldw.py` tool when a table can be declared (see balance-tables.md) and name the player policy it assumed.
7. Feel items go to juice-scan; here they only get a short handoff note.
8. Anything only a playtest can settle is marked needs-playtest with confidence low.
9. Report outliers as questions, not errors; a deliberate break of a curve is allowed.
10. Use only these category slugs, which are the contract's. Severity hints are starting points; adjust and say why.

## dominant-strategy

One option wins everywhere, or one build makes the rest pointless.

### R-01 One best option
- Look for: A card, unit, build or tactic that is best in every situation, or that every rival must answer. Compare options per situation in the data; look for docs that say 'always pick X'.
- Breaks: Meaningful choice
- Severity hint: critical when it removes a core decision for all players; major when it dominates one phase
- Tool: ev, sim (same policy, compare options)
- Sources: systems-and-loops.md; uncertainty.md; Salen ch. 21, Sellers, Sylvester ch. 6
### R-02 Dominated option
- Look for: An item no better in any column and not cheaper than another; a row that loses to a sibling on every attribute.
- Breaks: Dominance and choice
- Severity hint: minor alone; major if it is a whole class of options
- Tool: curve
- Sources: balance-and-economy.md; Schreiber ch. 9
### R-03 Counter spiral
- Look for: Patch notes or rules that answer a strong option with a hard counter instead of fixing its cost; rock-paper-scissors sets that are really ordered.
- Breaks: Intransitive balance
- Severity hint: major when the counters stack into a forced build
- Tool: by hand (payoff matrix); sim
- Sources: systems-and-loops.md; Sellers ch. 7; Schreiber ch. 25


## degenerate-loop

Loops that feed themselves, stall or run away.

### R-04 Runaway leader
- Look for: Gains that scale with current lead (income, XP, snowball effects, win-more cards) with no cap, tax or catch-up lever.
- Breaks: Feedback balance
- Severity hint: critical if the winner is clear by mid game; major otherwise
- Tool: economy, sim
- Sources: systems-and-loops.md; Sellers ch. 7; Salen ch. 18; Adams ch. 6
### R-05 Self-feeding tool
- Look for: An output that raises its own input at no cost (a card that draws more of its kind, a building whose product pays for copies).
- Breaks: Positive loop without a price
- Severity hint: critical if it is an infinite or near-infinite combo; major if it only shortens the game
- Tool: sim (deck), economy
- Sources: systems-and-loops.md; Sylvester ch. 6; Adams App. B
### R-06 Deadlock loop
- Look for: A resource needed to earn that same resource, with no free starting stock or safety floor; converters that can both run dry.
- Breaks: Engine safety
- Severity hint: critical if a normal run can stall; major if recoverable by luck only
- Tool: economy
- Sources: systems-and-loops.md; Sellers ch. 7; Adams App. B
### R-07 Safe grind
- Look for: Repeatable, risk-free progress that undercuts the challenge or beats the intended route in reward per minute.
- Breaks: Risk and reward
- Severity hint: major; critical if it is the optimal way to play
- Tool: economy, sim (walk)
- Sources: balance-and-economy.md; Koster ch. 7; Sutton ch. 3


## dead-choice

Options that look like decisions and are not.

### R-08 Cosmetic choice
- Look for: Options that change only a label or look, or where every branch leads to the same state a moment later.
- Breaks: Meaningful choice
- Severity hint: major if presented as a key decision; minor for flavour
- Tool: by hand
- Sources: core-loops-and-goals.md; Gibson ch. 1
### R-09 Idle or orphan mechanic
- Look for: A system the player can skip with no effect on outcomes, or whose result feeds nothing (no consumer in code).
- Breaks: Integrated systems
- Severity hint: major when it costs the player attention; minor if it is cheap
- Tool: by hand (search code for readers of the value)
- Sources: core-loops-and-goals.md; Salen ch. 3; Sellers ch. 5
### R-10 Dead step
- Look for: A stat or damage step that does not change hits-to-kill, thresholds or any outcome; two items sharing one niche.
- Breaks: Visible effect of a number
- Severity hint: minor per item; major if it covers a whole upgrade track
- Tool: curve
- Sources: balance-and-economy.md; Schreiber ch. 4; Sylvester ch. 2


## economy-leak

Currencies that accumulate, vanish or hide their price.

### R-11 Faucet without drain
- Look for: A resource with sources and no sink, or net positive flow with no cap, so it stops mattering.
- Breaks: Source and sink balance
- Severity hint: major; critical for the main currency
- Tool: economy
- Sources: balance-and-economy.md; Sellers ch. 7; Adams ch. 4
### R-12 Source-less or sink-less item
- Look for: A thing consumed with no way to obtain it, or obtained with no use. Check each resource name across data and code.
- Breaks: Closed economy
- Severity hint: critical if the main loop needs it; minor for flavour items
- Tool: economy
- Sources: balance-and-economy.md; Adams ch. 4
### R-13 Dragging brakes
- Look for: Upkeep or decay that can exceed income in ordinary play, or one large periodic drain that spikes.
- Breaks: Friction tuning
- Severity hint: critical if a normal run goes bankrupt; major if only a greedy run does
- Tool: economy
- Sources: systems-and-loops.md; Sellers ch. 7; Adams App. B
### R-14 No anchor currency
- Look for: Every currency can be bought or converted, so there is no play-only reference value to scale costs from.
- Breaks: Pricing anchor
- Severity hint: major; the cure is declaring one anchor
- Tool: curve, economy
- Sources: balance-and-economy.md; Schreiber ch. 5, 8; Clark ch. 9


## difficulty-spike

Sudden or unreadable jumps in challenge.

### R-15 Growth faster than power
- Look for: Challenge, enemy health or thresholds that grow faster than player power; a sudden change of ratio between consecutive thresholds.
- Breaks: Curve family
- Severity hint: critical if a wall appears before the middle of a run; major later
- Tool: curve, sim
- Sources: balance-and-economy.md; Schreiber ch. 4; Sellers ch. 10
### R-16 Power drift
- Look for: Player modifiers outpace (trivial late game) or lag (wall) enemy scaling across the declared run length.
- Breaks: Scaling parity
- Severity hint: major
- Tool: sim (walk), curve
- Sources: balance-and-economy.md; Clark ch. 10; Schreiber ch. 11
### R-17 Unseen demonstration
- Look for: A new hazard or rule first met by killing the player or under time pressure; a plan that states the player dies N times.
- Breaks: Teach before test
- Severity hint: critical for unavoidable deaths; major otherwise
- Tool: by hand
- Sources: levels-and-space.md; Totten; Rogers LevelUp ch. 12-13


## onboarding-gap

New players cannot learn what they need.

### R-18 Front-loaded tutorial
- Look for: Every control shown at once, a text wall, a new rule introduced under danger, or two hard lessons back to back.
- Breaks: Cognitive load
- Severity hint: major; critical if no run can start without it
- Tool: by hand
- Sources: core-loops-and-goals.md; ux-and-the-brain.md; Hodent ch. 13; Gibson ch. 12
### R-19 Tutorial last
- Look for: Onboarding unscheduled in the plan, or the first minutes need knowledge only given later; no title, settings, quit or resume in the flow.
- Breaks: Early experience
- Severity hint: major
- Tool: by hand
- Sources: production-and-scope.md; Wyman ch. 12; Lemarchand ch. 22; Hackett ch. 9
### R-20 Whole possibility space at once
- Look for: All systems, cards and districts open from minute one; best tool unlocked last; all new toys in the first level.
- Breaks: Gradual disclosure
- Severity hint: major
- Tool: by hand (list unlocks by time)
- Sources: levels-and-space.md; Totten; Bauer 8.1.3


## pacing

Rhythm of intensity, novelty and rest.

### R-21 Pacing clump
- Look for: Intense encounters adjacent in the plan or data with no rest; repeated system, lighting or music in adjacent stages.
- Breaks: Rhythm
- Severity hint: major
- Tool: by hand (tabulate encounter intensity per slot)
- Sources: levels-and-space.md; Totten; Bauer; Rogers LevelUp
### R-22 Stalled runway
- Look for: The game continues after nothing new can be learned; the middle repeats; updates add count, not new patterns.
- Breaks: Learning runway
- Severity hint: major
- Tool: by hand, curve
- Sources: core-loops-and-goals.md; Koster ch. 3-4; Sellers
### R-23 Flow gap
- Look for: Cooldowns with nothing else to do, unskippable animations, freeze-stuns, waits for other players or the AI.
- Breaks: Continuous engagement
- Severity hint: minor alone; major on the main loop
- Tool: by hand (time the loop)
- Sources: systems-and-loops.md; Sylvester ch. 5


## scope-risk

Plans that exceed what can be built or kept.

### R-24 Overscope
- Look for: Content volume out of proportion to the team; no vertical slice; riskiest tech scheduled last.
- Breaks: Scope control
- Severity hint: critical if the schedule has no cuts; major otherwise
- Tool: by hand (count content units against time per unit)
- Sources: production-and-scope.md; Gibson ch. 7; Wyman
### R-25 All priority one
- Look for: Every task a must-have, so no cuts are pre-decided; a goal so generic it never vetoes a feature.
- Breaks: Priorities
- Severity hint: major
- Tool: by hand
- Sources: production-and-scope.md; Lemarchand ch. 7, 19
### R-26 Unpriced promise and unknown unit cost
- Look for: Roadmap or store page lists features with no estimate; many levels or quests planned from one built with no time recorded.
- Breaks: Estimation
- Severity hint: major
- Tool: by hand
- Sources: production-and-scope.md; Schreier Pillars of Eternity ch. 1
### R-27 Moving target
- Look for: Schedule extended with no cut; late pivots; stretch goals with no reserve; solo project with no freeze; constants changed after dependent content exists.
- Breaks: Scope discipline
- Severity hint: major; critical for a shipped-once game near release
- Tool: by hand (read the changelog and handoff log)
- Sources: production-and-scope.md; Lemarchand ch. 13, 15; Hackett ch. 2; Schreier


## broken-promise

Presentation and mechanics disagree.

### R-28 Dressing mismatch
- Look for: Art, text or store page sells one experience and the mechanics teach another; a generic pitch that fits any setting.
- Breaks: Honest framing
- Severity hint: major; critical when the marketing hook is not in the build
- Tool: by hand
- Sources: core-loops-and-goals.md; Koster ch. 5; AI-ideation research
### R-29 Wish goal or missing feature
- Look for: A stated aim with no observable or number, or a feature promised in docs and absent from data or code.
- Breaks: Testable promises
- Severity hint: major
- Tool: by hand (grep doc claims in data and code)
- Sources: core-loops-and-goals.md; Wyman ch. 13; production-and-scope.md


## balance

Numbers that are out of line or unmeasured.

### R-30 Cost curve outlier
- Look for: An item far off the fitted line of benefit against cost. Report as a question, since a deliberate outlier may be intended.
- Breaks: Fair price
- Severity hint: major if one item shows up in every build; minor otherwise
- Tool: curve
- Sources: balance-and-economy.md; Schreiber ch. 8
### R-31 Viable-optimal gap
- Look for: The best build far above a typical one, so typical players lose to an option they cannot find.
- Breaks: Fairness
- Severity hint: major
- Tool: sim, curve
- Sources: balance-and-economy.md; Schreiber ch. 9
### R-32 Hidden or inline tuning
- Look for: Balance values buried in code with no list; batch edits that change two values between tests.
- Breaks: Tunability
- Severity hint: minor; major if code and docs disagree on a number
- Tool: by hand (grep numeric literals against data)
- Sources: balance-and-economy.md; Fullerton ch. 10; Lemarchand ch. 32
### R-33 Unnamed policy
- Look for: A balance claim or sim result with no player policy, agent pool, seed range or spread.
- Breaks: Evidence quality
- Severity hint: major for the claim; downgrade it to low confidence
- Tool: sim (--runs, --seed)
- Sources: ai-as-design-tool.md; playtesting.md; RuleSmith


## progression

Growth, reward and the shape of a run.

### R-34 Unrecoverable early error
- Look for: An early slip silently ruins the later game with no warning or recovery.
- Breaks: Recoverability
- Severity hint: critical in a long run; major in a short one
- Tool: by hand, sim
- Sources: systems-and-loops.md; Adams ch. 2
### R-35 Dead goals
- Look for: Only a distant story goal and nothing short-term between; goals not stated in a form the player can check.
- Breaks: Goal ladder
- Severity hint: major
- Tool: by hand
- Sources: levels-and-space.md; Totten p. 260; Wyman ch. 13
### R-36 Unclustered rewards
- Look for: A reward table or unlock curve that allows long streaks of the minimum, or pays for play other than the play shown.
- Breaks: Reward cadence
- Severity hint: major
- Tool: ev, sim (draw)
- Sources: balance-and-economy.md; Clark ch. 10


## clarity

Players cannot read state, cause or cost.

### R-37 Single-channel cue
- Look for: Critical information carried by colour only or sound only; false affordance; recall demand with no on-screen display.
- Breaks: Perception
- Severity hint: major; critical for lethal information
- Tool: by hand
- Sources: ux-and-the-brain.md; Hodent 11.2
### R-38 Obscured price or odds
- Look for: Several currencies hiding the real price, hidden odds in a purchase path, fake urgency, or streaks that punish absence. Report the pattern and let the user decide.
- Breaks: Honest cost
- Severity hint: major; critical for paid paths
- Tool: economy
- Sources: ux-and-the-brain.md; balance-and-economy.md; Hodent ch. 12, 17; Clark ch. 13
### R-39 Unguarded destructive action
- Look for: Delete, sell, discard or overwrite with no confirm or undo; two inputs the player cannot tell apart.
- Breaks: Error prevention
- Severity hint: major if it loses progress; minor otherwise
- Tool: by hand (read the handler)
- Sources: ux-and-the-brain.md; Hodent 11.2.6; Swink


## uncertainty

Randomness and hidden information.

### R-40 Solved or symmetric
- Look for: Perfect information, no random element and an obvious best line; strategy guides would be one sentence.
- Breaks: Uncertainty source
- Severity hint: critical for a replayed game; minor for a puzzle
- Tool: sim
- Sources: uncertainty.md; Costikyan ch. 6
### R-41 Single huge roll
- Look for: One random event overrides many skilled decisions, or a random outcome the player cannot influence or risk against.
- Breaks: Luck versus skill
- Severity hint: critical if it decides a run; major otherwise
- Tool: ev
- Sources: uncertainty.md; Costikyan ch. 5; Salen ch. 15
### R-42 Rigged-feeling odds
- Look for: A chance below about half gating progress with no pity timer, displayed odds or streak protection.
- Breaks: Perceived fairness
- Severity hint: major
- Tool: ev, sim (draw)
- Sources: uncertainty.md; Sellers ch. 9; Aversa ch. 3
### R-43 Hidden but unfair
- Look for: Hidden information the player cannot infer, mind-reading puzzles, bad events that erase long investment without warning.
- Breaks: Fair secrecy
- Severity hint: major
- Tool: by hand
- Sources: uncertainty.md; Costikyan ch. 5; Fullerton ch. 11


## level-design

Space, metrics and placement.

### R-44 Metrics drift
- Look for: Corridor, gap or board sizes unchanged after a new mover, speed or mechanic is added.
- Breaks: Consistent metrics
- Severity hint: major
- Tool: by hand (compare data sizes to movement values)
- Sources: levels-and-space.md; Totten
### R-45 Entrance dominance and single gate
- Look for: One cover point controls a room, or a single boss or fight is the only barrier.
- Breaks: Spatial variety
- Severity hint: minor to major
- Tool: by hand
- Sources: levels-and-space.md; Bauer
### R-46 Generator without a verifier
- Look for: Procedural content with no completability check, no seed-level solvability test, no quality proxy beyond designer eyeballing, or an LLM-made level accepted without a solver pass.
- Breaks: Verified generation
- Severity hint: critical for required content; major otherwise
- Tool: sim (many seeds)
- Sources: procgen.md; Short ch. 1, 11; Shaker ch. 1, 12


## ai-behaviour

Opponents that cheat, freeze or bore.

### R-47 Omniscient or instant AI
- Look for: Code that reads hidden player state with no sense or delay; zero reaction time; perfect aim.
- Breaks: Fair opponent
- Severity hint: major; critical if the AI also decides outcomes
- Tool: by hand (read the AI update)
- Sources: game-ai-for-designers.md; Buckland; Millington ch. 6, 14
### R-48 Opaque cheating
- Look for: AI income, vision or rolls differ from the player's with no disclosure or cap; adaptation drifting outside tuned balance.
- Breaks: Honest difficulty
- Severity hint: major
- Tool: by hand
- Sources: game-ai-for-designers.md; Bourg ch. 1; Togelius ch. 8
### R-49 Unreadable or relentless AI
- Look for: Attacks without telegraph, pursuit with no pause, crowd attackers with no cap, decision oscillation, enemies with no memory.
- Breaks: Readability
- Severity hint: major
- Tool: by hand
- Sources: game-ai-for-designers.md; Rabin ch. 1, 13, 33
### R-50 Undifferentiated or accidental AI
- Look for: Choices that give the same outcome, ties broken by name or order, skill values inline rather than per-type data, heavy machinery behind a two-state result.
- Breaks: Visible sophistication
- Severity hint: minor
- Tool: by hand
- Sources: game-ai-for-designers.md; Rabin ch. 4; Millington ch. 2; Buckland


## feel

Hand off to juice-scan; list only what the docs and code show.

### R-51 Misclassified or unmeasured feel
- Look for: Tight-controls promise for a game with no real-time control; 'floaty' or 'flat' notes with no timing or speed data.
- Breaks: Feel vocabulary
- Severity hint: minor; send to juice-scan
- Tool: by hand
- Sources: feel-handoff.md; Swink ch. 1, 5
### R-52 Accidental exploit or mass mismatch
- Look for: Diagonal or strafe speed over the cap; sensitive input mapped to a binary response; visual weight that contradicts the rules.
- Breaks: Control integrity
- Severity hint: major for the exploit; minor for the mismatch
- Tool: by hand
- Sources: feel-handoff.md; Swink ch. 7, 11

## Related

Related: [balance-and-economy.md](balance-and-economy.md), [balance-tables.md](balance-tables.md), [systems-and-loops.md](systems-and-loops.md), [uncertainty.md](uncertainty.md), [core-loops-and-goals.md](core-loops-and-goals.md), [levels-and-space.md](levels-and-space.md), [procgen.md](procgen.md), [game-ai-for-designers.md](game-ai-for-designers.md), [ux-and-the-brain.md](ux-and-the-brain.md), [playtesting.md](playtesting.md), [production-and-scope.md](production-and-scope.md), [feel-handoff.md](feel-handoff.md), [ai-as-design-tool.md](ai-as-design-tool.md)

### R-53 Authored, not built
- Look for: Cards, rewards, win paths or systems that the design doc or data tables define but no code applies (grep the code for each data id or effect key). Settle the stage first: in a prototype this is the to-do list, in a shipped game it is a broken promise.
- Breaks: Promises kept; the loop the design depends on
- Severity hint: in a game still being built, grade by what the gap blocks (a win condition or a core loop: major; flavour: note) and mark the finding `built: no` or `partial`; a gap that blocks the advertised win or core loop ranks above every flaw in what exists, other gaps rank after them; in a shipped or live game, `broken-promise`, major or critical
- Tool: none (a grep and a count)
- Sources: production.md; Lemarchand (vertical slice and scope); user correction 2026-10-29 (L-20261029-2)

### R-54 Generator needs consumables
- Look for: A level generator with no guaranteed start-to-exit path that needs no bombs, keys or tools, and no softlock test over many seeds.
- Breaks: Luck-independent wins; consumables as a real choice
- Severity hint: major when a run can be lost to layout alone; minor when only a resource is lost
- Tool: `ldw.py sim` over fixed seeds with a reachability check, or by hand on the generator rules
- Sources: procgen.md; Yu Part I

### R-55 Friction counted as difficulty
- Look for: Complaints that a game is too hard while common actions take many steps or buttons, controls lag, or ledge grace is missing. Count the steps per action before any enemy nerf.
- Breaks: Challenge that comes from the design, not the interface
- Severity hint: major when the friction sits on the core action
- Tool: by hand
- Sources: playtesting.md; Yu Parts I, III

### R-56 Signposted or dominant secrets
- Look for: Secrets marked by cracks, flashing or prompts; key items useful only at one lock; a hidden reward strong enough to become the standard route.
- Breaks: Discovery; build and route variety
- Severity hint: minor for signposting; major when the secret becomes the dominant strategy
- Tool: by hand
- Sources: levels-and-space.md; Yu Parts II, IV

### R-57 Seeded run not fixed by its seed
- Look for: Chest, crate or drop contents rolled when opened rather than at generation, in a game with daily, shared or replayed seeds.
- Breaks: Comparable seeded runs
- Severity hint: major for a daily or competitive seed mode; note otherwise
- Tool: grep the code for random calls inside open or pickup handlers
- Sources: procgen.md; Yu Part III

### R-58 Play tied to frame rate
- Look for: Speeds, cooldowns or timers counted per frame; a jump that goes higher or lower as the frame rate changes; no cap on the frame delta after a hitch, load or tab switch, so the simulation leaps.
- Breaks: The same game on every machine; fair timing
- Severity hint: major when it changes jump arcs or competitive timing; minor otherwise
- Tool: grep the update code for per-frame steps not scaled by delta time; by hand at two frame-rate caps
- Sources: feel-handoff.md; Gregory, Game Engine Architecture 2e (2014), sec. 7.5.2, 7.5.5

### R-59 Raw input reaches gameplay
- Look for: No rebinding; bindings to physical keys rather than named actions; no stick dead zone, or one far wider than needed; one button with two clashing uses and no rule for which wins.
- Breaks: Controls that answer what the player meant; access for other layouts and devices
- Severity hint: major when the clash or drift sits on the core action; minor for missing rebinding alone
- Tool: by hand on the input code and the binding list
- Sources: ux-and-the-brain.md; Gregory, Game Engine Architecture 2e (2014), sec. 8.5.1 to 8.5.3

### R-60 Physics players cannot plan around
- Look for: Core-loop outcomes decided by a physics result that is neither readable nor repeatable; no way back from a flipped, stuck or wedged state; AI that cannot path around objects that move.
- Breaks: Skill over chaos; recoverable failure
- Severity hint: major when the core loop depends on it; note when physics is only for show
- Tool: by hand, repeating the same action several times
- Sources: feel-handoff.md; Gregory, Game Engine Architecture 2e (2014), sec. 12.1.2, 12.1.3

### R-61 Objective welded to one level
- Look for: Objectives written into one map's code, so reordering, moving or cutting content means a code change rather than a data edit.
- Breaks: Cheap iteration on structure; scope cuts late in production
- Severity hint: minor; major when a planned cut or reorder is blocked by it
- Tool: grep the objective code for level names or scene ids
- Sources: production-and-scope.md; Gregory, Game Engine Architecture 2e (2014), sec. 14.1.2, 14.1.3
