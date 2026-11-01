# Balance and economy

Answers: are the costs, rewards, sources, sinks and progression curves sound, and which table to declare so `ldw.py` can check them. Load it for cost curves, expected value, economy audits, progression pacing and dominant-strategy reviews. Written 2026-10-29.

## Principles

1. Balance has several kinds (variables, dynamics, starting conditions, skill, fairness). Say which one a claim is about, and the intended audience and difficulty, before judging. [Schreiber ch. 1; Fullerton ch. 10; Schell]
2. Pick one anchor (a reference item or a play-only currency) and scale everything from it. If every currency can be bought, there is no play-only reference value. [Schreiber ch. 5, 8; Clark ch. 9]
3. For transitive mechanics (more cost buys more power), fit benefit against cost and look at the residuals. For intransitive ones (rock, paper, scissors) solve a payoff matrix instead. Classify first. [Schreiber ch. 8, 25]
4. List an object's costs and benefits numerically; treat conditional or limited benefits as non-negative, never zero. [Schreiber ch. 8]
5. Curves are servants: break them deliberately and within bounds. One above-curve outlier does more harm than many weak ones. Report outliers as questions, not errors. [Schreiber ch. 8]
6. Choose the curve family on purpose (linear, exponential, logarithmic, triangular, custom). Challenge growth faster than power growth is a mismatch. Check the ratio of consecutive thresholds for a runaway or a sudden change of base. [Schreiber ch. 4; Sellers ch. 10]
7. A damage or stat step that does not change hits-to-kill is dead. A pack that is cheaper per unit when smaller is non-monotonic pricing. [Schreiber ch. 4]
8. Expected value is computable from a declared table. Report it with the spread, the odds and a sample-size caveat; compare variance, not only the mean. [Schreiber ch. 17; Gibson ch. 9, 11; Schell]
9. Economy health is sources minus sinks per player over time. Tabulate currency in and out per phase; a resource that only grows has no drain, one that is consumed with no source is a dead item. [Schreiber ch. 6; Adams ch. 4; Sellers ch. 7]
10. Inflation is faucets outrunning drains. Single-player games may skip inflation yet still hit a surplus, where gold is useless late. [Schreiber ch. 6; Sellers ch. 7]
11. A utility matrix is an audit prompt: for each kind of utility the game offers, find its source and its sink. A utility with neither, or two items doing one job, is a finding. [Clark ch. 7, 9]
12. An economy summary in four lines (growth, money supply, price setting, trade limits) plus the four audit questions covers a design on one page. [Fullerton ch. 5]
13. Fixed-price vendors with unlimited demand remove the trade decision. Risk-free farming and bottom-feeding are rational responses and should be looked for. [Sellers ch. 7; Koster ch. 7]
14. Dominant strategy and a constricted decision space are one failure seen in two places. Fix it by giving different options different strengths in different situations, not by flattening the numbers. [Sellers ch. 5, 9; Fullerton ch. 10; Sylvester ch. 6]
15. Balance strategies in situations, not tools against tools; do not balance reactively, since every change shifts others. [Sylvester ch. 6]
16. Perceived difficulty has separate knobs (information, execution, resources, opponent power); pick which one a ramp moves. The gap between viable and optimal builds decides whether the final boss feels right. [Schreiber ch. 1, 9, 11]
17. Power drift: player modifiers outpacing or lagging enemy scaling. Plot player power against enemy power per stage and flag spikes and plateaus. [Schreiber ch. 11; Clark ch. 10]
18. Skill balance: test at both skill extremes and tune to the median. Decide which skill level the balance targets. [Fullerton ch. 10; Sylvester ch. 3]
19. Use data with a question, a hypothesis and enough sample, and watch confounders and the quiet majority. Data-informed, not data-driven. [Schreiber ch. 13; Sellers ch. 7]
20. A balance claim names its player policy and its agent pool. A result tuned against one policy may not hold against another. [AI-playtesting research 2026-10-29, RuleSmith; Adams ch. 8]
21. Scoring is the strongest signal of what a game is about: players do the scored action. Keep scores simple, visible to the player, tied to the skill wanted, varied enough to separate players, and in large values (100, not 1). [Boller and Kapp ch. 7]
22. Check scoring in a spreadsheet: per level, total the maximum points and the penalties, and test that a non-perfect player can advance and that early points do not make the rest trivial. Expect several passes; cut rules testers cannot trace to their score. [Boller and Kapp ch. 7]
23. Achievements: measurement (one to three stars against a standard) over completion badges, and a completion badge only if it depends on performance. Expected ones set goals, unexpected ones reward exploration; hold competitive ones back until players know the game. [Boller and Kapp ch. 7]

## How to apply

Declare a table, run the matching `ldw.py` command, then judge. Shapes are in [balance-tables](balance-tables.md). The script counts; the model decides what the number means.

| Check | Command | Table to declare |
|---|---|---|
| Cost curve and outliers | `ldw.py curve TABLE` | one row per like object: name, cost, plus numeric attributes (power, health, speed) |
| Expected value and spread of a random table | `ldw.py ev TABLE` | rows of outcome, weight, value |
| Sources, sinks, net flow, leaks | `ldw.py economy TABLE` | rows of resource, kind (source, sink, start), amount, per, uses, optional caps |
| Turns to goal, loot spread, card exposure | `ldw.py sim TABLE --steps N` | model draw, walk (with target) or deck (cards with count, hand size, value) |
| Growth ratio, pack price monotonicity, dead damage step | `curve` or by hand | cost or threshold per level or tier |
| Dominated option | `curve` residuals plus a manual column comparison | all columns of the like objects |
| Payoff matrix for intransitive sets | by hand (no command yet) | matrix of outcomes; say it is unchecked by script |

Procedure for an economy review:

1. Anchor: name the reference value. If none, say so.
2. Declare every source and sink with amount per use and uses per period. Run `economy`; read net flow, leak and drain flags.
3. Ask who pays for what: for each utility, what is its source and what its sink.
4. Check the inflation direction over the whole game, not one session, and the elder-game state after content runs out.
5. State the player policy (which actions the simulated player takes, how greedy) beside the result. Rerun with a second policy; if the verdict flips, report both.

Procedure for a cost curve:

1. Pick like objects only (cards of one type, units of one tier). Mixing kinds hides outliers.
2. Run `curve`, then read the flagged items as "is the cost wrong or the benefit wrong".
3. Look at the top outlier first and whether it is deliberate. Also look for dominated options that the fit does not flag.
4. Never conclude from fewer items than attributes plus two; the tool refuses, and so should the review.

Procedure for a random table: run `ev`, compare the mean to the intended payoff, check probabilities sum to one, and read the spread against the number of draws a player will see. For fairness feel, see [uncertainty](uncertainty.md).

Sim reporting: show p05, p50 and p95, the fixed seed, steps and runs, and the policy. A single mean from one policy is not a balance claim.

## Failure patterns

- Cost curve outlier: an item far off the fitted line. Symptom: one card or unit in every build. [Schreiber ch. 8]
- Dominated option: an item no better in any column and not cheaper than another. [Schreiber ch. 9]
- Dead damage step: values that do not change hits to kill. [Schreiber ch. 4]
- Runaway growth: consecutive thresholds with a sudden change of ratio. [Schreiber ch. 4; Sellers ch. 10]
- Faucets without drains: a currency that only accumulates. [Sellers ch. 7; Adams ch. 4]
- Source-less item: consumed with no way to obtain it. [Adams ch. 4]
- Anchor missing: all currencies purchasable. [Clark ch. 9]
- Safe grind: repeatable risk-free progress that undercuts the challenge. [Koster ch. 7]
- Fixed-price market: infinite-demand vendors, no trade decision. [Sellers ch. 7]
- Variance blind spot: balance by mean damage or yield only. [Gibson ch. 9, 11]
- Unclustered payouts: tables that allow long streaks of the minimum. [Clark ch. 10]
- Power drift: player modifiers outpace or lag enemy scaling. [Clark ch. 10; Schreiber ch. 11]
- Viable-optimal gap: best build far above a typical one. [Schreiber ch. 9]
- Obfuscated premium currency or non-monotonic bulk pricing. [Schreiber ch. 4]
- Hidden variables: tuning values buried in code with no list. [Fullerton ch. 10]
- Reactive balancing: patch log shows each fix breaking something unreviewed. [Sylvester ch. 6]
- Unnamed policy: a balance verdict with no stated player policy or agent pool. [AI-playtesting research]
- Time-gated and dark-pattern economy: pay-to-win exposure, urgency without justification, obscured prices. Report the pattern and let the user decide. [Clark ch. 13; Gibson ch. 8; Hodent]

## Where the books disagree

- Enforcing the curve: Schreiber says cost curves serve the designer; strict mechanical fit contradicts that. We report outliers as questions with the likely side (cost or benefit), never as defects.
- Many viable strategies: balance culture praises them; Sylvester rejects counting. We ask for distinct situational roles instead.
- Commercial advice: Clark's retention gates and monetisation tests fit free-to-play and live games, not premium single-player. We apply the economy audit to both and the retention advice only when the game is a service.
- Adaptive balance: Schell is wary, Sylvester allows it for low-skill audiences. See [systems-and-loops](systems-and-loops.md).
- A script proves the maths of the declared table, not that the table matches the game. We always require a source check on the inputs and cite where each number came from.

Related: [core-loops-and-goals](core-loops-and-goals.md), [systems-and-loops](systems-and-loops.md), [uncertainty](uncertainty.md), [balance-tables](balance-tables.md), [review-heuristics](review-rubric.md), [playtesting](playtesting.md). Feel goes to game-juice's juice-scan and juice-principles. Engine-side implementation goes to unity-agent, roblox-agent and madnesswright.
