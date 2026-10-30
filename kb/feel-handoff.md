# Feel handoff

Answers: how a design review spots feel problems from docs and code, and when to stop and hand the finding to game-juice's juice-scan. Load whenever a review finds a feel promise, a control complaint, or a "tight", "satisfying" or "juicy" claim.

## Principles

1. Ludowright reviews rules and structure. Feel is game-juice's job. Ludowright's part is to spot the signs, mark them `needs-playtest`, and hand over. [Swink ch. 1]
2. Classify first. Game feel needs three building blocks: real-time control, simulated space, polish. A turn-based or menu game has polish only, so its feel goals are presentation goals, not control goals. [Swink ch. 1]
3. Feel has six measurable areas: input, response, context, polish, metaphor, rules. A complaint that names none of them is not yet a finding. [Swink ch. 5]
4. Rules are part of feel: health, damage and reward structure convey mass and the value of skill. [Swink ch. 11, 17]
5. Context and avatar tune as a pair: object spacing against avatar speed, and collision. [Swink ch. 5]
6. Hard metrics (input to response timing, speed curves) turn vague reports into located faults; soft metrics (player reports) say where to look. [Swink ch. 5]

## How to apply

Signs a ludowright review can see without running the game:

1. Feel promise against feel type: the doc promises tight or satisfying controls but the game has no continuous real-time control. Flag; hand to juice-scan.
2. Ambiguous simultaneous inputs: two near-simultaneous commands resolved in a way the player cannot predict. This is a rules and UX finding too, so ludowright keeps it. [Swink ch. 17]
3. No timing instrumentation: no log or overlay of input to response. Suggest one.
4. Decay or overshoot: top speed that appears briefly then drops, or diagonal or strafe input exceeding the cap (an exploit and a fatigue source). [Swink ch. 7]
5. Binary response to an analogue input: continuous device values collapsed to on or off. [Swink ch. 7]
6. One canned animation for a high-frequency action or for every failure. [Swink ch. 17]
7. Perceived mass mismatch: a heavy-looking object with few hit points or light feedback, or the reverse. [Swink ch. 11, 17]
8. Spacing mismatch: obstacles or pickups too tight or too wide for the avatar's speed. [Swink ch. 5]
9. Long lockout the player did not choose and cannot cancel. A chosen, risky lockout that fits the world is fine. [Swink ch. 2]
10. Enemy telegraphs and miss presentation (see [game-ai-for-designers.md](game-ai-for-designers.md)) are feel items; hand the animation side over.

Handoff format: for each item write the location (file, scene, doc section), the sign, which of the six areas it belongs to, the line `needs-playtest`, and "route: juice-scan". Do not propose numbers (hit-stop length, shake strength); juice-principles owns those and dates them.

Never let a feel change alter rules: damage, scores, card effects and saves must behave the same with every juice toggle off.

## Failure patterns

- Misclassified feel. Symptom: "tight controls" promised for a game with no real-time control. [Swink ch. 1]
- Unmeasured complaint. Symptom: "feels floaty" in notes, no timing or speed data. [Swink ch. 5]
- Accidental exploit. Symptom: strafe or diagonal speed above the cap. [Swink ch. 7]
- Wasted device. Symptom: sensitive input mapped to a binary response. [Swink ch. 7]
- Canned failure. Symptom: one animation for all deaths or errors. [Swink ch. 17]
- Mass mismatch. Symptom: visual weight disagrees with the rules. [Swink ch. 11]

## Where the books disagree

- Swink limits "game feel" to real-time avatar control; modern usage (juice) stretches to menus and turn-based play. Ludowright uses Swink as a classifier, not a gate: polish-only games still get juice advice, from game-juice.
- Swink's animation preferences and some 2009 platform assumptions are craft opinion and dated; accessibility (reduce motion, flash limits) is game-juice's rule and wins any conflict.

## What Swink adds that game-juice lacks (list for a separate game-juice PR)

Not edited here. Targets are in game-juice, for its maintainer.

- Feel-type classifier: the three building blocks and what a game with no real-time control gets. Target: juice-scan step 1 and juice-principles.
- Real-time control continuity test with the chosen-lockout exception. Target: extends P-02 and lens J2.
- Context as a tuning pair (spacing against speed, collision as feel). Target: new principle and a "Context fit" lens.
- Polish as perception manipulation, with an "inferred physical property per object" field in the juice-scan report.
- The six metric areas as a measurement frame. Target: a feel-metrics reference and a juice-scan checklist.
- Input and response sensitivity, input classification, position, rate and magnitude mappings. Target: feel-metrics reference; unity-agent for analogue axes.
- Response vocabulary: ADSR envelope, floaty, tight, twitchy, stiff as shapes; decay as exploit; sustain as limit.
- Rules metrics as feel, with a two-way link to ludowright's balance kb.
- The eight principles (predictable results, instantaneous response, easy but deep, novelty, appealing response, organic motion, harmony, ownership) as lenses.
- Control ambiguity, state overwhelm and staging pitfalls.
- Soft and hard metrics in a feel playtest plan.
- Method-only case studies of classic games; needs a full read of Swink's case chapters first, and no per-game numbers are to be copied.

Related: [production-and-scope.md](production-and-scope.md), [game-ai-for-designers.md](game-ai-for-designers.md), [ai-as-design-tool.md](ai-as-design-tool.md). Feel analysis goes to game-juice (juice-scan, juice-principles, juice-apply); engine input implementation to unity-agent.
