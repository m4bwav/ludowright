# Uncertainty and randomness

Answers: where does the game's uncertainty live, is there too little or too much, and is randomness designed or just present. Load it for "feels flat", "feels unfair", dice and card odds, luck versus skill, hidden information and catch-up mechanics. Written 2026-10-29.

## Principles

1. Play needs uncertainty somewhere, not only in who wins. Ask where it lives: outcome, score, path, solution, or other players. A game whose uncertainty is gone is solved for that player. [Costikyan ch. 3]
2. Contingency (if A then B) is not uncertainty. A static puzzle is full of contingencies and its only uncertainty is the solver's ability. [Costikyan ch. 3]
3. Interface clarity is a goal; challenge clarity is not. Keep rules and state legible, keep outcome uncertain, and separate friction that serves the challenge from friction that merely obstructs. [Costikyan ch. 3; Hodent]
4. Costikyan's eleven sources work as a checklist: performative, solver's, player unpredictability, randomness, analytic complexity, hidden information, narrative anticipation, development anticipation, schedule, perception, semiotic. It is one author's lens, not a standard. [Costikyan ch. 5]
5. Randomness has five jobs: moment-to-moment tension, symmetry breaking, variety, drama, and simulation. Name the job before adding a roll. [Costikyan ch. 5]
6. Many small rolls average out and reward skill; one big roll dominates and gives drama. Choose by what the game is for. [Costikyan ch. 5; Schreiber ch. 17]
7. Certainty, risk and uncertainty differ: only risk (known odds) is fully computable by the designer. Perfect or imperfect information and randomness are independent axes. [Salen ch. 15; Schreiber ch. 2]
8. Luck and skill are separate from determinism. Judge by the decisions available and the information visible, not by whether dice exist. [Schreiber ch. 2, 19; Fullerton ch. 11]
9. Chance still needs choices around it. Pure-chance passivity (outcomes with no stake or influence) is a failure. [Salen ch. 15; Costikyan ch. 5]
10. Preparation before the challenge (loadout, hand-building, positioning) turns chance into skill. [Koster ch. 7]
11. Pair every risky option with a safe one (triangularity) and check reward against odds; surface the odds where fairness feel matters. [Schell ch. 11; Sellers ch. 9]
12. Players misread probability: they trust streaks, fear small chances and overvalue long shots. Players' sense of fairness trumps true probability. Price designs for the misreading. [Salen ch. 15; Schreiber ch. 20; Sellers ch. 9]
13. Where fairness feel matters, smooth random draws (shuffle bags, pity counters, streak caps) and clustering so long minimum streaks cannot occur. Note it changes the true odds. [Clark ch. 10; Schreiber ch. 20]
14. Randomness inside a growth engine amplifies early luck but can break a dominant strategy. Strip randomness first, then add it back one place at a time. [Adams ch. 6, App. B]
15. Information structure (open, hidden, mixed, dynamic) is a design choice. Hidden information supports exploration and variety but hurts when the player has no basis to infer from. [Fullerton ch. 11; Costikyan ch. 5; Sylvester ch. 5]
16. Too little uncertainty: perfect information plus symmetry gives an obvious best move. Remedy by adding hidden information, asymmetry, randomness or interaction. Too much: paralysis, outcomes unrelated to actions, external helper tools. Remedy with information design, not by deleting the source. [Costikyan ch. 6]
17. Changing difficulty usually turns the dial on one source. A step change comes from adding a different source (random levels to a platformer, puzzle logic to a shooter). [Costikyan ch. 6]
18. Match uncertainty to the audience: performative suits core action players, analytic and hidden information suit lean-back players. [Costikyan ch. 5]
19. Positive feedback kills endgame tension (a winner is evident early). Offer negative feedback, a way for the loser to matter, or a visible end. Kingmaking, sandbagging and turtling arise from specific conditions: list the conditions and break one. [Costikyan ch. 5; Schreiber ch. 12]
20. Catch-up must be bounded: a trailing bonus larger than the skill gap makes outcomes independent of play, and hidden adaptation reads as cheating. [Adams ch. 4; Salen ch. 18; Schell ch. 13]
21. Time gates and energy are schedule uncertainty and a retention tool. Flag absence-punishing mechanics and treat them with an ethics caution. [Costikyan ch. 5; Gibson ch. 8; Clark ch. 13]
22. Lowering legibility is a difficulty lever. An accessibility review separates intended perceptual challenge from avoidable noise. [Costikyan ch. 5]
23. Randomness from pseudorandom sources should be seeded and saved, so runs replay and save-scumming is a known choice. [Schreiber ch. 21]

## How to apply

Uncertainty census:

1. List the sources present, with an example moment for each. Mark the primary one.
2. Ask the four questions: what uncertainties does the player face, are they enough for the intended challenge, are they the kind the audience wants, would adding, removing or changing one source help.
3. For a design that feels flat, look for inherited uncertainty that was weakened in a port or cut-down. For one that feels overwhelming, look for noisy information tools and uncontrollable inputs (camera, controls).

Randomness audit, per random event:

1. Name its job (principle 5). No job means no roll.
2. Does the player influence it, risk something, or respond to the result? If none, flag no-stake randomness.
3. Run `ldw.py ev` on the declared outcome table: mean, spread and odds. Compare spread to the draws a player will see; a high spread over few draws is variance-dominated.
4. Run `ldw.py sim` with `draw` or `deck` (declare hand size and card counts) to see streak risk, the p05 to p95 band and how often each card appears. Fix the seed and the number of runs.
5. Note the player policy beside the result (always take the safe option, always take the risky one). A luck claim without a policy is not a claim.
6. Check whether a single roll can override many skilled decisions.

Information audit: for each decision, list what is visible, hidden and inferable. A hidden fact that cannot be inferred from earlier play is a fairness finding. A visible fact that removes the thinking is a glut finding.

Catch-up and end-state audit: find the positive loops in [systems-and-loops](systems-and-loops.md), then ask what keeps the trailing player in the game, and whether the bonus is visible and bounded.

Table shapes for `ev` and `sim` are in [balance-tables](balance-tables.md). Findings that depend on how randomness feels (screen reaction, near-miss timing) are marked `needs-playtest`.

## Failure patterns

- Solved or symmetric: perfect information, symmetric positions, no random element, obvious best play. Symptom: strategy guides list one line. [Costikyan ch. 6]
- No-stake randomness: random outcomes the player cannot influence and risks nothing on. [Costikyan ch. 5; Salen ch. 15]
- Single huge roll: one random event overrides many skilled decisions. [Costikyan ch. 5]
- Luck compounding: random early production amplified by an engine. [Adams App. B]
- Snowball ending: winner obvious long before the end; loser has no lever. [Costikyan ch. 5; Schreiber ch. 12]
- Mind-reading puzzle: solutions that depend on guessing an arbitrary designer order, with unhelpful failure messages. [Costikyan ch. 5]
- Analysis paralysis: many options and no way to prune. [Costikyan ch. 6; Sylvester ch. 5]
- Hidden but unfair: hidden information that cannot be inferred. [Costikyan ch. 5]
- Fallacy exposure: designs that need players to read odds correctly, or reward the long shot over the safe bet. [Salen ch. 15]
- Rigged-feeling odds: a chance below about 50 percent that gates progress, with no safeguard or displayed odds. [Sellers ch. 9]
- Unclustered payouts: long streaks of the minimum possible. [Clark ch. 10]
- Uncertainty from controls: camera, input or physics the player cannot predict. [Costikyan ch. 6]
- Static content as only source: all challenge in hand-made content with little replay value. [Costikyan ch. 5]
- Skill gap isolation: performative challenge with no matchmaking or tiers. [Costikyan ch. 5]
- Rubber band opacity: invisible adaptation. [Salen ch. 18]
- Arbitrary punishment: bad random events that erase long investment without warning. [Fullerton ch. 11]
- Mismatch of audience and source. [Costikyan ch. 5]

- Slot-machine variety: content shuffles over shallow systems. Randomness pays only when the systems under it are worth learning. [Yu Part III]
- Unlimited looting with no time or space pressure, so collecting holds no dilemmas; a soft, telegraphed timer turns it into decisions. [Yu Part II]

## Where the books disagree

- Is uncertainty of outcome the key feature: Costikyan disputes Salen's quantifiable-outcome view. For ludowright it is enough that uncertainty must live somewhere; we ask where, not which definition wins.
- Hidden information fairness: Costikyan values it for exploration; Sylvester warns about starvation. We allow it when the player can infer or learn it, and flag it when not.
- Smoothed randomness: Clark and Schreiber endorse streak smoothing for fairness feel; purists say it changes the game. We allow it where it is declared and disclosed in the odds, and require the true distribution to be reported.
- Adaptive difficulty: see [systems-and-loops](systems-and-loops.md). Taxonomy limits: gendered audience generalisations in Costikyan are dated, and we do not use them; test with real players instead.

Related: [core-loops-and-goals](core-loops-and-goals.md), [systems-and-loops](systems-and-loops.md), [balance-and-economy](balance-and-economy.md), [balance-tables](balance-tables.md), [procgen](procgen.md), [game-ai-for-designers](game-ai-for-designers.md), [review-heuristics](review-rubric.md). Feel of chance beats (near-miss, reveal, loot burst) goes to game-juice's juice-scan and juice-principles. Engine-side implementation goes to unity-agent, roblox-agent and madnesswright.
