# Review rubric, part 2

Items R-53 to R-68 of [review-rubric.md](review-rubric.md), split out for size. Same use, same rules, same category slugs: walk every item after R-52. Item IDs are stable: never renumber, only append here.

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

### R-62 Learning game that does not teach
- Look for: In a learning game, no mechanic named as the one that teaches or the one that measures; modes not labelled teach or test; a goal with an empty cell in its alignment row (activity, assessment, scoring) or no event in play that exercises it; no pre-brief or debrief.
- Breaks: Alignment of play and learning goal
- Severity hint: major when a goal is tested but never taught; minor for a missing debrief. Category: broken-promise
- Tool: by hand, one alignment row per goal (learning-games.md)
- Sources: learning-games.md; Kapp fieldbook ch. 2-4; Plass GDC 2012; Mangos and Ferraro ch. 3

### R-63 Reward shell
- Look for: Remove every point, badge and coin: would play continue? Pointsification, badge inflation (a badge earned in under a minute or many times a session), chocolate-covered broccoli. For child players, any variable-ratio reward, scarcity or countdown timer, or streak prompt.
- Breaks: Intrinsic motivation; ethical design for children
- Severity hint: major for a child-facing manipulative schedule; minor otherwise. Category: progression
- Tool: by hand
- Sources: learning-games.md; Chou ch. 2-3, 14; Kim et al. ch. 9

### R-64 Experience phase with no pull
- Look for: Walk discovery, onboarding, scaffolding and endgame; flag a phase with no stated reason to play, most often an endgame with nothing left once the main journey ends.
- Breaks: A reason to play on day one and day 100
- Severity hint: major for a live or long game; note for a short one-shot. Category: pacing
- Tool: by hand
- Sources: learning-games.md; Chou ch. 3

### R-65 One viable opening
- Look for: Of the early strategy families (for example rush, defend, build, mixed), fewer than several are viable, or one beats all others.
- Breaks: Meaningful early choice
- Severity hint: major when it settles the opening for all players. Category: dominant-strategy
- Tool: sim, each family against the others (design-drills.md 5)
- Sources: design-drills.md; Lockhart and Lang ch. 6

### R-66 Avoidable access barrier
- Look for: Information carried by colour or sound alone; text or key elements below WCAG 2.2 contrast (4.5:1 text, 3:1 large text and UI parts); flashing above three per second; required fast reflexes or drags with no option; things to remember that cannot be found again. Keep intended challenge apart from avoidable noise.
- Breaks: Players excluded by accident, not by design
- Severity hint: major when a group cannot finish; minor otherwise. State who the game excludes on purpose. Category: clarity
- Tool: by hand; simulate colour blindness, sound off, one hand
- Sources: ux-and-the-brain.md; WCAG 2.2 (1.4.3, 1.4.11, 2.3.1); Lockhart and Lang ch. 1

### R-67 No escape valve
- Look for: In a multiplayer or shared-world design, one player's action can remove other players' options with no route elsewhere (a blockade, a destroyed shared resource, a locked map). Kingmaking is uncertainty.md 19; this item is about being trapped, not about who wins.
- Breaks: Every player keeps a meaningful move
- Severity hint: major when a trapped player must sit out; minor when the trap is brief. Category: dead-choice
- Tool: by hand
- Sources: worldbuilding-and-lore.md; Robbins, Microscope p. 63, 72 (book rule, unverified)

### R-68 Optional authority favours the loud
- Look for: In co-op, social or co-creation play, quiet players contribute only by opting in (a free-for-all suggestion phase, a vote anyone may skip), so dominant players set every outcome. Prefer a turn where each player must add something alone.
- Breaks: Every player shapes the game
- Severity hint: minor; major when the design's promise is shared authorship. Category: broken-promise
- Tool: by hand; watch who speaks in a playtest
- Sources: worldbuilding-and-lore.md; Robbins, Microscope p. 73 (book rule, unverified)

### R-69 Knocked out early
- Look for: A rule that can leave a player with no real path to victory in the first third, or a zombie seat (mathematically out, still taking turns). By the end of the opening each player should be able to name a concrete route to win.
- Breaks: Belief in a chance to win until the end
- Severity hint: major; note in games under about 30 minutes. Category: uncertainty
- Tool: sim (walk), share of runs where a seat is out before a third of the turns
- Sources: uncertainty.md; Selinker (ed.), Kobold Guide to Board Game Design, 2011, ch. 1.3 p. 23-24, ch. 3.3 p. 99

### R-70 Endless endgame
- Look for: Once a leader pushes for the win, nothing ends the game in bounded turns; or a play loop (cards picked back up, a recycled pile) can repeat forever under good play.
- Breaks: A finite, tense last act
- Severity hint: major; critical if a normal game can stall. Category: pacing
- Tool: sim (walk) with a turn cap; `reached` below 100% is the no-end share
- Sources: Selinker ch. 1.3 p. 26; Parlett, Penguin Book of Card Games, ch. 18, ch. 21

### R-71 Kingchooser
- Look for: A rule that forces a player with no stake to pick the winner (worst), rewards a losing player for throwing the game (kingmaker), or lets them take the win from one player with a targeted card (kingbreaker, mildest). Fix the last with a random shared hazard.
- Breaks: The best player wins
- Severity hint: major for a kingchooser, minor for a kingbreaker. Category: uncertainty
- Tool: by hand
- Sources: uncertainty.md 19; Selinker ch. 3.3 p. 99-100

### R-72 Forced reverse
- Look for: A penalty that takes away score, position or owned things where a lost turn, a slowdown or an optional spend would do the same job. Losses hurt more than equal gains.
- Breaks: Setbacks that keep players in the game
- Severity hint: minor; major when it is the main interaction. Category: balance
- Tool: by hand
- Sources: Selinker ch. 3.3 p. 102-103

### R-73 Featured content bypassed
- Look for: A dumb fixed rule (buy only one thing, hoard, ignore the headline cards) matches or beats play that uses the game's featured content.
- Breaks: The promise of the featured content
- Severity hint: major. Category: dominant-strategy
- Tool: sim with a greedy policy that ignores the feature, against the intended policy
- Sources: playtesting.md; Selinker ch. 3.1 p. 87-88

### R-74 Free rest
- Look for: Waiting or resting costs nothing, so players spend every burst resource in each fight and then rest; or every encounter is hard, so players cannot learn to ration.
- Breaks: Resource choices across a run
- Severity hint: major. Category: degenerate-loop
- Tool: by hand; fixes are easy fights that basic moves win and a foreseeable clock that punishes resting
- Sources: Baur, Kobold Guide to Gamemastering, p. 135-136

### R-75 Failable must-know
- Look for: A fact the critical path needs sits behind a check, roll or optional search that can fail with no fallback.
- Breaks: Progress the player can always reach
- Severity hint: major; critical if it blocks the win. Category: onboarding-gap
- Tool: by hand; trace each must-know fact to a source that cannot fail
- Sources: Baur p. 113-114

### R-76 Health sponge
- Look for: Difficulty raised by enemy health while damage stays flat, so fights get longer, not harder; steps too small to notice; health values with no legible classes.
- Breaks: Difficulty the player can feel
- Severity hint: minor; major when it is the main difficulty lever. Pair damage raises with telegraphs (R-78). Category: difficulty-spike
- Tool: sim (walk), turns to kill before and after
- Sources: balance-and-economy.md; Runehammer, ICRPG Core, p. 78, 87

### R-77 Identical retry
- Look for: A failed attempt can be repeated at the same odds with no cost and no progress, so play becomes a reroll loop.
- Breaks: Failure that moves the game on
- Severity hint: minor. Category: dead-choice
- Tool: by hand; fix by making the retry easier or costly
- Sources: Runehammer p. 12, 77

### R-78 Arbitrary death
- Look for: A loss or death the player had no chance to see or react to. Change the rule before, never the roll after.
- Breaks: Consequences that follow choices
- Severity hint: major. Category: uncertainty
- Tool: by hand
- Sources: uncertainty.md; Macris, Arbiter of Worlds, ch. 2 sec. 14

### R-79 Expendable-piece AI
- Look for: All foes share one aggression profile and fight to the last; none retreats, routs or surrenders; foes act on facts they could not know.
- Breaks: Readable, believable opponents
- Severity hint: minor; major when it makes every fight an attrition grind. Category: ai-behaviour
- Tool: by hand
- Sources: game-ai-for-designers.md; Macris ch. 5 sec. 25
