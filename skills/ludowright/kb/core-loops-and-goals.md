# Core loops and goals

Answers: what is this game's core loop, what experience and promises does it make, and is the one-pager specific enough to build from. Load it for one-pagers, pitch critique and "what is this game about" reviews. Written 2026-10-29.

## Principles

1. Name the core loop as a verb: the action the player repeats most, which everything else must serve or be cut. [Rogers Level Up! ch. 4; Sellers ch. 7]
2. "Core loop" has no settled definition, so state the sense used: the most-repeated action, the fastest loop, or the most important one. Then list the loop's time scales (seconds, minutes, session, campaign) and check each has a decision. [Sellers ch. 7; Clark ch. 6]
3. Clark's three loops give a one-pager its skeleton: core (the repeated play), context (what changes it from session to session) and cultural (what players do around it). A pitch that fills only the first is a mechanic, not a game. [Clark ch. 6]
4. State the essential experience first, then dynamics, then mechanics (aesthetic target before rules), and test every feature against that experience. [Schell ch. 2-3; Gibson MDA]
5. Check the four elements (mechanics, story, look, technology) for harmony around one theme; a feature that fits none of them is a candidate for cutting. [Schell tetrad]
6. An experience goal is only useful when it names an observable: what players do, say or feel at which moment. "Tense" is a wish; "players hesitate before the last card" is a goal. [Wyman ch. 13; Schell]
7. Goals should be clear, concrete, at both short and long range, related to each other, and chosen by the player where possible. [Schell ch. 3]
8. A player promise is what the pitch, title, art and first minute imply the game will deliver. Review the middle and end against it. [Koster ch. 5; Gibson]
9. Fun as learning is one useful lens: list what the player learns at each stage and when that runs out. Boredom is the diagnostic, so separate too easy, arbitrary, too opaque and learning exhausted before touching numbers. [Koster ch. 3]
10. A good loop has the required parts: preparation, a space, a core mechanic, a range of challenges, real choices and a skill requirement. Scan for the missing one. [Koster ch. 7]
11. Meaningful play means actions are discernable (the player sees the result) and integrated (the result feeds what comes later). An activity whose result never feeds anything is an orphan. [Salen ch. 3]
12. A choice that never changes state is cosmetic, not a decision. [Gibson ch. 1; Salen ch. 6]
13. The first minute should contain a win in the core loop, and a new player should face two or three new things per stage, not all controls at once. [Sellers ch. 7; Rogers ch. 4]
14. Skill-chance and mental-physical positioning should match the audience, and uncertainty types should match them too: lean-forward players want performative challenge, lean-back players want analytic or hidden-information challenge. [Fullerton ch. 11; Costikyan ch. 5]
15. A pitch is specific when it names a verb, a constraint that bends that verb, and a hook that the nearest comparable game lacks. Abstract feature lists and "like X but better" fail that test. [Rogers one-sheet; AI-ideation research 2026-10-29]
16. Put numbers in the vision: session length, number of areas or levels, run length, share of time per activity. Vague visions drift and cannot be rechecked. [Wyman ch. 14; Rogers ten-pager]
17. Overscoping is the common killer. Scope to a vertical slice that proves the loop, and tackle the riskiest unknown first. [Gibson ch. 7; Schell risk list; Lemarchand]
18. Layer goals instead of a difficulty menu: shortcuts for the impatient, a main ending for most, a hidden harder goal for experts. Each player picks their own challenge inside the game. [Yu Part II]
19. Let the world be indifferent and teach through itself. Rewards handed out on a predictable schedule can weaken players' own reasons to play. [Yu Parts II, III]

## How to apply

The one-pager fields (the engine-side template lives in the game-design references of the engine plugins; do not copy it here):

1. Working title, platform, audience, session length.
2. Core loop as one verb plus the cycle around it (verb, result, spend or upgrade, new situation). Give the loop's time scale.
3. Experience goal with its observable (principle 6).
4. Three or four player promises, each testable by a scene or a number.
5. Constraint and hook: what bends the verb, and what the nearest comparable lacks.
6. Progression and goals: short, mid, long, and who chooses them.
7. Systems list, each with a reason it serves the goal (an idle system is a cut candidate).
8. Scope: slice, content volume, riskiest unknown and how it is tested first.
9. Risks, and two or three contrasting alternatives that differ in verb or constraint, not in theme.

Specificity test for a pitch (run it on any one-pager, including ours):

- Can the core verb be said in one or two words, and is it not "explore", "manage" or "build" alone?
- Does the constraint make the verb costly or interesting (limited hand, shared resource, timer, risk)?
- Would swapping the theme leave the design unchanged? If yes it is generic.
- Does the hook differ from the comparable game in the mechanic, not the setting?

Review procedure for an existing game:

1. Write the loop as a verb and time scales from docs and code, not from the marketing text.
2. List the promises, then find the scene, card or system that delivers each. An undelivered promise is a finding.
3. Run the required-element scan (principle 10) and the learning runway: list what is newly learnable per stage and flag long stretches with nothing new.
4. Mark each player choice as state-changing or cosmetic.
5. State the experience goal's observable and whether any data or test could show it. If not, mark `needs-playtest`.

`ldw.py` does not help here; the numbers come in [balance-and-economy](balance-and-economy.md).

## Failure patterns

- Verb soup: the loop cannot be said as one verb; docs list five equal activities. Symptom: no cut rule, features pile up. [Rogers; Sellers]
- Mechanic without a game: only the core loop exists; no context or cultural loop, so session two looks like session one. [Clark ch. 6]
- Generic pitch: swap the setting and the doc still reads true; comparables carry the whole hook. [AI-ideation research]
- Wish goal: "feels epic" with no observable or number. [Wyman ch. 13]
- Broken promise: art or text sells one thing, mechanics teach another (dressing mismatch). [Koster ch. 5]
- Cosmetic choices: options that change only labels or looks and are presented as decisions. [Gibson ch. 1]
- Orphan mechanic: activity whose result never feeds anything. [Salen ch. 3]
- Idle system: feature players can skip with no effect on outcomes. [Sellers ch. 5]
- Stalled runway: the game continues after nothing new can be learned; the middle repeats. [Koster ch. 3; Sellers flat middle]
- Count inflation: updates add more of the same element with no new pattern. [Koster ch. 4]
- Front-loaded tutorial: every control shown at once, or a new rule introduced under danger. [Gibson ch. 12; Sellers]
- Overscope: content volume out of proportion to team, no slice, riskiest tech last. [Gibson ch. 7; Wyman]
- Audience mismatch: analytic-heavy design pitched at action or casual players, or the reverse. [Costikyan ch. 5]

## Where the books disagree

- What fun is: Schell says pleasure with surprise, Koster says learning, Sylvester separates emotion triggers. Ludowright treats them as lenses on one question and uses learning for runway checks, pleasure and surprise for moment checks. They disagree in vocabulary more than in advice.
- Fiction versus system: Koster says fiction dressing wears off and the system carries long-run value; Schell treats story as one of four equal elements. We weigh the system first in a review, and use the tetrad to check the dressing does not contradict it.
- Locked scope versus live change: Lemarchand wants scope fixed after preproduction, Wyman wants fast live changes in social games. Ludowright picks by game type: lock for premium single-player, allow change for live service.

Related: [systems-and-loops](systems-and-loops.md), [balance-and-economy](balance-and-economy.md), [uncertainty](uncertainty.md), [production-and-scope](production-and-scope.md), [review-heuristics](review-rubric.md). Feel and juice go to game-juice's juice-scan and juice-principles. The one-pager, beat chart and playtest protocol templates live in the game-design references of unity-agent, roblox-agent and madnesswright; point to them rather than copying.
