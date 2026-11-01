# Production and scope

Answers: is this plan buildable by the people and time available, and what should be cut first. Load for one-pager scope sections, scope-risk review, and any "can we ship this" question.

## Principles

1. Write an experience goal (a feeling, not a mechanism) plus three or four design goals, and let them veto features. A goal that has never caused a cut is decoration. [Lemarchand ch. 7; Wyman ch. 14; Hackett ch. 7]
2. Make the goal observable: say what a player would do or say if the feeling occurred, and tie it to a prototype or playtest. Vision statements with no numbers (areas, levels, session length) cannot be checked. [Lemarchand ch. 7; Wyman ch. 13-14]
3. Prove the core verb is pleasant alone (a toy) before layering goals and progression. The minimum viable game is presentation, input, feedback and a loop. [Hackett ch. 6]
4. The vertical slice is a deliverable: core loop, controls and camera, one special sequence and one sample level at ship quality. If it is not compelling, stopping is a valid outcome. [Lemarchand ch. 10, 13, 21]
5. Build concentrically: primary mechanic finished first, then secondary, then tertiary. Build mid-game content before the opening and finale, which are the hardest to get right. [Lemarchand ch. 13, 28]
6. Test scope with arithmetic, not feeling: task hours (estimates rounded to 1, 2, 4, 8), people, weekly hours, and three priority tiers decided before the crunch, not during it. [Lemarchand ch. 19; Hackett ch. 7]
7. Measure cost per content unit on the first unit and multiply before committing to the count. [Schreier Pillars of Eternity ch. 1]
8. Price every public promise (stretch goal, announced feature, store-page line) before making it, and keep spare capacity for the optimistic case. [Schreier Pillars of Eternity ch. 1, Shovel Knight ch. 7; Wyman ch. 12]
9. Iteration time (edit to playable change) is a design-health metric. Slow loops predict late quality. [Schreier Destiny ch. 8, Dragon Age: Inquisition ch. 6]
10. Prove engine and tooling fit with real content in preproduction, not after the schedule is set. [Schreier Dragon Age: Inquisition ch. 6; Wyman ch. 12]
11. Lock the parameters and structure that other work depends on (movement constants, economy constants, story shape) before building content on them. A late structural rewrite is the costliest pivot. [Lemarchand ch. 13; Schreier Destiny ch. 8, Uncharted 4 ch. 2]
12. Fix scope, not the date. Moving a deadline and adding scope after alpha are the usual crunch drivers. [Lemarchand ch. 15, 28; Schreier Uncharted 4 ch. 2]
13. Prototype one question at a time and do not ship the prototype. Budget the gap between prototype and production quality. [Sellers ch. 12; Wyman ch. 12]
14. Hungry features (gamepad, rebinding, settings, music, localisation, accessibility, save and resume) must be listed and costed, along with the bookends: title, settings, credits, quit, resume. [Hackett ch. 3, 6, 9]
15. A save-it-for-the-sequel list is the cheapest cutting tool; use it as features are proposed, not only at crunch. [Hackett ch. 7]
16. Content restrictions are a hidden cost of every new ability: each one constrains every level and encounter built afterwards. [Sylvester ch. 13]
17. Unproven AI or generative features are scope risks. Keep a fallback that ships without them. [Togelius ch. 8]
18. Finishing is a skill. Do not restart; park new ideas for the next game; cut and scale down; cut side modes until the main one ships. Expect the last tenth (menus, polish, platform work) to take as long as the rest. [Yu Part III]
19. Small teams in one room iterate on feel fastest. Growing headcount to meet a funder's date buys bloat and lost ownership, not speed. [Schreier Press Reset ch. 1, 2, 7]
20. Name a closer: one person whose job is to say no, lock the core early and cut scope. [Schreier Press Reset ch. 2]
21. Plan the life after launch: free updates and ports bring sales back (a roguelike's best month can come two years in), and announce a final update on purpose rather than drifting on. [Schreier Press Reset ch. 3, 8]
22. Data-drive only what designers tune often, and give each such value a tool and a preview. Making everything data can leave a team slower than code. Set an acceptable wait for each kind of change and track it. [Gregory, Game Engine Architecture 2e (2014), sec. 14.3]
23. Budget the number of units a player commands (about a dozen for a tabletop skirmish). Lower it as each unit gains unique rules; raise it when units are uniform. [Lambshead 2024, Introduction]
24. Fast-play test: everything a player needs fits on one sheet, with no cross-referenced modifier tables and no mental arithmetic. [Lambshead 2024, Introduction]
25. Ship a named list of rules that can be dropped to speed play without losing much strategy. [Lambshead 2024, Speeding up game play]

## How to apply

1. Locate the experience goal in the one-pager. Ask what has been cut because of it. Write "none yet" if nothing; that is a finding.
2. Ask for a task list with hours, owner, priority tier. If absent, build a rough one with the user using 1/2/4/8 estimates.
3. Compute W (total hours of Must and Should tasks) against T (people times weekly hours times weeks). Keep roughly ten percent slack as a heuristic, not a law. Report the cut list needed to bring W under T, lowest tier first.
4. Run the shipped-tomorrow drill: if the build had to ship tomorrow, what is Must? Everything else is Could.
5. Check the slice: is there one section at final quality that proves the loop? If polish is deferred to the end, flag it.
6. Check the iteration loop: time from edit to playing the change. Over a couple of minutes, rank "shorten the loop" high among suggestions.
7. List hungry features and bookends against the scene or flow list.
8. Check the phase shape: preproduction (unschedulable, exploratory) then production (schedulable, locked). Ask what the gate between them is and what would fail it.
9. For content-heavy designs, ask for cost per unit of the first unit. For economy or difficulty tuning, plan a post-launch tuning budget and what telemetry would trigger it. `ldw.py economy` and `ldw.py curve` give the numbers a tuning budget depends on.
10. For a game with a fast headless core, say so: it makes `ldw.py sim` and playtest bots cheap (see [ai-as-design-tool.md](ai-as-design-tool.md)).

## Failure patterns

- Headcount ramp to a date. Symptom: team grows sharply to hit a funder's milestone while the core loop is still unproven. [Schreier Press Reset ch. 1, 7]
- Self-imposed crunch. Symptom: owners or revenue-share partners work unbounded hours because the game is theirs; it still burns people and partnerships. [Schreier Press Reset ch. 5, 8]
- Goal that vetoes nothing. Symptom: generic goal ("fun, engaging"), no cut ever attributed to it. [Lemarchand ch. 7]
- All priority one. Symptom: every task marked must-have, so no pre-decided cuts. [Lemarchand ch. 19]
- Unpriced promise. Symptom: roadmap or store page lists features with no estimate. [Schreier Pillars of Eternity ch. 1]
- Stretch-goal creep. Symptom: optional modes added with no capacity reserve. [Schreier Shovel Knight ch. 7]
- Unknown unit cost. Symptom: one level or quest built, many planned, no time-per-unit recorded. [Schreier Pillars of Eternity ch. 1]
- Late pivot. Symptom: rewritten scripts or recorded content in the changelog after production began. [Schreier Uncharted 4 ch. 2, Destiny ch. 8]
- Moving date. Symptom: schedule extended with no scope cut; "one more week" in the handoff log. [Lemarchand ch. 15; Schreier Uncharted 4 ch. 2]
- Faked demo. Symptom: trailer or pitch material not produced by the build. [Schreier Dragon Age: Inquisition ch. 6; Star Wars 1313 ch. 10]
- Tool mismatch. Symptom: genre-critical systems (dialogue, inventory, quests) not yet prototyped in the chosen engine. [Schreier Dragon Age: Inquisition ch. 6]
- Unbounded solo scope. Symptom: solo project with no outside deadline, no feature freeze, a stream of new features. [Schreier Stardew Valley ch. 3; Hackett ch. 2]
- Parallel project drain. Symptom: shared staff across projects with no staffing table. [Schreier Halo Wars ch. 5]
- Fiction coupled to mechanics. Symptom: a licence or setting swap would discard mechanics work. [Schreier Halo Wars ch. 5]
- Approval chain risk. Symptom: an external owner can veto direction late. [Schreier Star Wars 1313 ch. 10]
- Post-launch economy risk. Symptom: loot rates and difficulty ramps untested for the endgame, no telemetry plan. [Schreier Diablo III ch. 4]
- Patch regression loop. Symptom: fixes shipped without regression tests, producing new bugs. [Schreier Stardew Valley ch. 3]
- Feature smuggling. Symptom: features added after alpha under another name. [Lemarchand ch. 28]
- Defaults left in. Symptom: engine-default lighting, sound, UI or camera in a build called complete. [Lemarchand ch. 13]
- Unlocked parameters. Symptom: movement or economy constants changing after dependent content exists. [Lemarchand ch. 13]
- Tutorial last. Symptom: onboarding unscheduled until near the end. [Wyman ch. 12; Lemarchand ch. 22]
- Missing bookends. Symptom: no title, settings, credits, quit or resume in the flow. [Hackett ch. 9]
- Broken-main refactor. Symptom: a note saying the game does not run until a system is rewritten. [Hackett ch. 9]
- Prototype contamination. Symptom: prototype code or placeholders in the shipped tree. [Sellers ch. 12]
- Success overload. Symptom: no capacity or support plan if usage is ten times the estimate. [Wyman ch. 12]
- Batch balance edits. Symptom: two or more value changes between tests, effects unattributable. [Lemarchand ch. 32]

Schreier's chapters are journalism from interviews and selected for drama: treat each as a plausible risk, not a frequency, and cite by game and chapter only.

- Restart loop: rewrites or fresh vertical slices with no new content. Finishing is a skill: park new ideas for the next game, cut variant modes while the main one is unfinished, scale down. [Yu Part III]
- Estimates that leave out the last 10 percent: menus, stats, animation volume, localisation overflow, ratings and platform certification. [Yu Part III]

## Where the books disagree

- Locked scope after preproduction (Lemarchand) versus fast live change (Wyman ch. 12, social games). Ludowright locks scope for shipped products and allows live change only for live-service designs, and asks which the game is.
- Polish-as-you-go concentric development assumes a team that can afford full-quality slices. For solo or AI-assisted work, ludowright accepts one polished corner plus a thin slice, which Lemarchand ch. 10 itself concedes.
- "Make it only for you" (Hackett ch. 5) against market-aware positioning. Ludowright applies Hackett to hobby and small projects and asks about audience for anything commercial.
- Figures such as "seven testers", "80 percent of mistakes come from preproduction" and the ten percent margin are practitioner rules of thumb. Ludowright quotes them as rules of thumb.

Related: [game-ai-for-designers.md](game-ai-for-designers.md), [ai-as-design-tool.md](ai-as-design-tool.md), [feel-handoff.md](feel-handoff.md). Playtest protocol, one-pager and beat-chart templates live in the game-design references of roblox-agent and unity-agent; point to them. Feel and juice time-boxing go to game-juice (juice-apply). Engine tooling and fast-iteration settings go to unity-agent, roblox-agent, madnesswright.
