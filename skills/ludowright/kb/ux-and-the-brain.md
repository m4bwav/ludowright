# UX and the brain

Answers: will a player see, understand, remember and want to continue, and is any mechanism manipulating them. Load when reviewing UI specs, onboarding, tutorials, feedback, accessibility, retention or monetisation.

## Principles

1. Perception, attention and memory limits frame every UI review. Players notice few things at once, forget what is not on screen, and recognise far better than they recall. Display what they would otherwise have to remember. [Hodent ch. 2-4, 11; Koster ch. 6]
2. Count cognitive load and say which load is the challenge. Extra load that is not the challenge (menus, unclear icons, hidden state) is removed; the intended load is kept. Nested rules and chunk limits cap how many interacting rules a player holds. [Hodent ch. 5, 11; Koster]
3. Give every feature a state list, and for each state a sign and a feedback. Every input gets an immediate response, including refused ones. [Hodent ch. 11; Schell feedback lens; Swink input and response]
4. Never carry critical information on one channel only (colour alone, sound alone, an auto-timed pop-up). Pair each sound cue with a visual twin. [Hodent ch. 5, 11.2.7; Rogers LevelUp ch. 17]
5. Form follows function. Test icons and metaphors by showing them to outsiders and asking what they would guess. Same look should mean same behaviour; a deviation needs a reason. [Hodent ch. 11; Swink on control ambiguity]
6. Information starvation and information glut both kill decisions; check what the player knows at the moment of choice. Mark each decision hollow, obvious, uninformed, informed, weighted or dramatic, and aim for weighted and informed. [Sylvester ch. 3-4; Fullerton ch. 11]
7. Teach by doing, in context, with a reason to act. Walls of text and teaching without a reason fail; invisible training and implicit difficulty choice are better. Do not stack two hard lessons in a row. [Hodent ch. 12-13; Sylvester ch. 10; Gibson ch. 14-15]
8. Plan onboarding as a spreadsheet: one row per thing taught, with the method, the reason, and difficulty. Sort it to find adjacent hard items and to count new systems, controls and rules in the first ten minutes. [Hodent ch. 13; Wyman tutorial as deliverable]
9. Plan for return after a break: remind goals and controls. Guard destructive actions (delete, sell, spend, quit) with confirmation or undo. [Hodent ch. 4, 11.2.6]
10. Errors are design signals. If many players make the same mistake, the design invites it. Players should blame themselves, not the game; when they blame the game, check presentation before lowering the challenge. [Hodent ch. 11; Bauer ch. 7]
11. Boredom is the diagnostic. Classify it: too easy, arbitrary, too opaque, or learning exhausted. [Koster ch. 2-3]
12. Read motivation as competence, autonomy and relatedness, and look for perceptible evidence of each in the game. Extrinsic rewards can help or hurt depending on type. [Hodent ch. 6; Schell]
13. Difficulty follows a sawtooth with rest after peaks, not a straight line. Failure should be quick, explainable and cheap; an unexplained loss or a failure that worsens control or view spirals. [Hodent ch. 12; Swink on failure states; Rogers LevelUp ch. 13]
14. Design out abuse early: whatever pays will be exploited. [Hodent ch. 12.2.1; Fullerton ch. 10]
15. Ship defaults for the mainstream and settings for the rest: full control remap with reset, subtitles on by default, difficulty options, motion and flash limits. [Hodent ch. 11.2.7; Rogers LevelUp ch. 6]
16. Memory of an experience is peak-end weighted and unpleasant moments are recalled worse, so what you measure after play is not what happened during it. [Yannakakis ch. 4-5]
17. Praise real success with layered feedback and keep it for real achievements. [Rogers LevelUp ch. 13]
18. Show the lock before the key: tease the obstacle before handing over the tool. When a reward is earned, the player should be able to name what it lets them do. [Hodent 2e]
19. Tutorial text appears only while the player has not yet done the action, and a tooltip gallery lets returning players look things up. [Hodent 2e]
20. After a loss, show what the player did well (best combo, distance) to help reappraisal. Never add effects that cover the screen when the player is already losing. [Hodent 2e]

## How to apply

1. Take the UI spec or the screens and build the state table (feature, state, sign, feedback, channels). Empty cells are findings.
2. Walk the first ten minutes as a new player and count new controls, systems and rules. More than the player can chunk (Koster, Hodent) is first-session overload.
3. For each tutorial item note the type: doing in context, reading, or watching. Flag reading and watching items that teach a high-priority hard mechanic.
4. List every piece of information the player must remember across screens or sessions that could be shown instead.
5. For every irreversible action find the guard. For every currency, check the true price is computable at a glance.
6. Classify any retention or monetisation mechanism against the dark-pattern list below. Say what the mechanism does for the player and what it costs them.
7. Findings that need real players (does the icon read, is the tutorial clear) become playtest questions; see [playtesting](playtesting.md).

## Dark patterns to avoid

Sort each pressure mechanism four ways: dark pattern, nudge, bad UX or good UX. Name the pressure type (temporal, monetary, social capital), then test it: does the pressure serve play, and can the player see it? [Hodent 2e ch. 17]

- Login punishment: streaks that reset hard or punish absence. [Hodent ch. 12.2.2, 17]
- Currency obscuring cost: several virtual currencies so the real price is hard to compute. [Hodent ch. 17]
- Arbitrary punishment: a random event that erases long investment without warning. [Fullerton ch. 11]
- Exploitable reward: a behaviour that pays but harms other players or the game. [Hodent ch. 12.2.1]
- Fake urgency or a hidden odds table in a purchase path. [Hodent ch. 12, 17]
- Disguised currency, insidious pay-to-win, predatory ads. [Hodent 2e ch. 17]

## Failure patterns

- Single-channel cue: colour-only or sound-only critical information. [Hodent]
- False affordance or look-alike, act-different elements. [Hodent 11.2.3-11.2.4]
- Recall demand with no display; no return-after-break reminder. [Hodent]
- Unguarded destructive action. [Hodent 11.2.6]
- Same-error pile-up in logs at one spot. [Hodent 11.2.6]
- Text-wall tutorial, or two hard lessons back to back. [Hodent ch. 13]
- Static tutorial text for an action the player already did. [Hodent 2e]
- Flat difficulty, spiral failure, unexplained loss. [Hodent ch. 12]
- Test hygiene faults: team tests on itself, leading questions, intent inferred from behaviour. [Hodent ch. 14]
- Control ambiguity: simultaneous inputs the player cannot tell apart. [Swink]
- Data without a hypothesis: analytics events with no question. [Hodent ch. 15]

Citations: "Hodent" with a chapter number is the 2017 first edition; "Hodent 2e" is the 2026 second edition, where chapters moved (ethics ch. 17, AI ch. 18). Recheck a first-edition chapter number before quoting it against 2e.

## Where the books disagree

- Hodent aims at clarity and low friction; Costikyan says challenge needs uncertainty and opacity of outcome. Ludowright applies clarity to rules, interface and feedback, and leaves outcome uncertainty alone.
- Neuroscience framing: Hodent warns about neuro-hype, yet cites memory and attention findings that come from general psychology. Ludowright treats them as heuristics to check, not proofs.
- Extrinsic rewards: the literature is mixed. Ludowright asks which kind and what it does to the intrinsic motivation, and does not ban them.
- Retention benchmarks come from one mobile report. Ludowright does not apply them to premium games.

Related: [levels-and-space](levels-and-space.md), [playtesting](playtesting.md), [procgen](procgen.md). Feel and feedback juice go to game-juice (juice-scan, juice-principles). Engine UI work goes to unity-agent, roblox-agent, madnesswright.
