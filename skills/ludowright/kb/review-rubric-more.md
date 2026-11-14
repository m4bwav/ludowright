# Review rubric, part 2

Items R-53 to R-66 of [review-rubric.md](review-rubric.md), split out for size. Same use, same rules, same category slugs: walk every item after R-52. Item IDs are stable: never renumber, only append here.

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
