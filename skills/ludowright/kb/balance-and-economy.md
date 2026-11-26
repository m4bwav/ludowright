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
24. Set loss or rout thresholds on absolute losses, not percentages, so the rule balances itself across force sizes. A leader bonus on such a test is strong but brittle when the leader can be lost. [Lambshead 2024, Winning and losing; Warband morale test]
25. Make each repeat action by the same unit in one turn cost more (1, then 3, then 5 points). Play spreads across the force instead of one hero piece. [Lambshead 2024, Player phase]
26. Tie two stats on one inverse axis (armour against evasion). Classes stay distinct with one simple rule. [Lambshead 2024, Part II introduction]
27. Order rewards by what they cost the designer and what players value: status first, then access, then power, then stuff. Status and access are cheap and lasting; power and goods are costly and fade. [Zichermann and Cunningham ch. 3; book rule, unverified]
28. Name what each point does: experience (never lost, ranks the player), redeemable (spent), skill (earned in one activity), karma (only given to others), reputation (others' judgement). One currency doing two jobs is a finding. Status tier names must read in order without a legend. [Zichermann and Cunningham ch. 3; book rule, unverified]
29. Leaderboards: centre the view on the player with near neighbours, show literal ranks only for a small top group, slice by friends, region or period, reset weekly by default, and never rank a sensitive measure (weight, income) in the raw; show progress bands instead. [Zichermann and Cunningham ch. 3; book rule, unverified]
30. One-player test for any social or multiplayer feature: play it as the only person online. If it is empty or dead (the empty bar), add bots, async play or a solo path before launch. [Zichermann and Cunningham ch. 4; book rule, unverified]
31. Card games: tie rarity to complexity, not raw power; a rare that beats a pricier common on stats alone splits players by collection. Write deck rules first (size, copy cap, rarity and faction caps); a copy cap stops a deck of only the best card, and extra copies only raise draw odds, so check them with `ldw.py draw`. Pick the resource model early (pool that grows each turn, no cost with one card a turn, or resource cards in the deck); changing it later means rebalancing every card. [Bycer 2024, 6.4, 8.1, 8.2; book rule, unverified]
32. Card cost line: a vanilla card's stats track its cost and keywords buy any deviation. A combo that needs many cards should be strong and hard to answer; one beaten by a single cheap card is dead. Unconditional card draw with no hand limit has no downside: flag it. Name the counter and its cost for every strong strategy. [Bycer 2024, 8.4; book rule, unverified]
33. Draws from a shuffled deck are without replacement: count them as combinations (hypergeometric), never as repeated independent rolls. Streak and pity rules must not lean on the gambler's fallacy. [Calculating Chance, ch. 1-2]
34. Never devalue what players already earned: no raised thresholds, rescaled points or mass-awarded badges after the fact; patch forward. Points that pile up unspent are unpaid promises, so every currency needs a spend path. Competitive features move only the top tier: say what the bottom half gets. Before launch, list the cheapest way to earn each reward without doing the intended thing; the bigger the reward, the harder it will be gamed. [Burke, Gamify, ch. 8; book rule, unverified]
35. A mood or stress meter seeks a target instead of summing events: target = base plus active modifiers, and the shown value moves toward it at a capped rate per hour, faster up than down so recovery feels earned but not slow. Each modifier has an effect, a duration and a stack rule: copy k counts effect times a multiplier to the power k-1, up to a limit, plus a per-source limit so one person cannot farm it. Personality is a list of modifiers a trait cancels. A break is a threshold stat with severity bands below it, the break picked by weight inside the band. Check a table with `ldw.py mood` (`UNCAPPED`, `SPIKE`, `OSCILLATES`). [harvest: a colony sim's shipped data files, 2026-11]
36. When progress raises what a unit expects, make the expectations concrete, visible needs, and let bonuses offset drains. A rule that only recovers when every drain is zero, or an abstract expectation number, sinks content advanced units. [harvest: a colony sim, 2026-11-22]
37. A renewable source that pulses or goes dormant stays fair when its long-run average is shown, because the player can plan storage for the gaps. A finite source that runs dry early leaves its worker idle for the rest of the game. [harvest: a colony sim, 2026-11-22]
38. Let expectation climb with progression (rule 36), and give work two priority layers: a player-set order per worker and per task, plus a survival tier (air, food, rescue) that no setting can delay. Mirror the bad break with a good one: a unit kept well above its expectation for a while gets a rare positive burst, so the meter rewards care as well as punishing neglect. [harvest: Oxygen Not Included, 2026-11-23]
39. Keep tuning data as parent and child rows: an abstract parent holds shared fields, each child lists only the fields it changes, so a variant (silver, gold) reads as its difference and one edit to the parent reaches all of them. Store tunables that vary with another number as a curve, a list of points interpolated between, not as code or a formula. Lint for a missing parent, a cycle, an abstract row used in play and an override equal to the parent value. [harvest: RimWorld, 2026-11-23]
40. Card pool shape for a run-based deckbuilder: most cards cost 1 (a mean near 1.3, few at 3 or more), every crew or class pool the same size, and a small fixed keyword set (temporary, exhaust, retain, recycle) where none sits on most cards, or it stops telling cards apart. Give every card two upgrade branches instead of one linear step, so an upgrade is a choice. Ship positioning can stand in for block: dodging by moving sideways and a separate temporary shield give defence more than one verb. Check a card table with `ldw.py deck` (`MEAN_COST`, `ZERO_COST`, `KEYWORD_EVERYWHERE`, `POOL_UNEVEN`). [harvest: Cobalt Core shipped card stats, 2026-11-23]
41. Plan deck growth per stage against a band (start size, cards per stage, an end range, a hard ceiling) and give every run at least one thinning route. Removal that costs the same currency as healing or travel, and only at some map stops, makes thinning a real choice; merging two cards into one is a second route that also strengthens. For a capped resource such as ammo, count makers against spenders per average hand. Check with `ldw.py growth` (`BLOAT`, `OFF-BAND`, `NO-THIN`, `STARVED`, `FLOODED`). [harvest: Pirates Outlaws shipped rules text, 2026-11-25]
42. A reward tier with a built-in cost: after a big fight, offer a pick of strong rewards that each carry a stated downside (more energy but fewer card choices, or no rest healing). The cost turns the strongest pick into a judgement, not an automatic take. [harvest: Slay the Spire 2, public rules, 2026-11-25]
43. A rising quota with a visible countdown: each payment is due after a set number of periods, and the amount grows faster than the periods. The amount owed and the periods left stay on screen, so every add or skip is weighed against the deadline. Keep slack (expected income over the window divided by the payment) between about 1 and 2, and avoid a required rate that more than doubles from one payment to the next. Check with `ldw.py quota` (`TIGHT`, `LOOSE`, `CLIFF`). [harvest: Luck be a Landlord, 2026-11-25]
44. Countdowns the player can see and change: every threat shows the turns until it acts, and some plays add or remove turns or pause the counter outright (freeze it for N ticks), so delay becomes a spent lever as strong as damage. A pause stacks differently from adding turns: it holds the counter wherever it is, so it is worth most on a threat about to act. Permanent upgrades that attach to a card in a capped number of slots make investment a choice of which card; free upgrades with no cap let one card absorb everything. [harvest: Wildfrost, public rules and live play, 2026-11-25]
45. Renewable stock: a harvested pool (game, fish, timber) needs a regrowth rate, a floor below which it collapses, and a visible safe harvest rate under regrowth. Overharvest should be a choice with a cost, not a hidden trap. [Bill Webb, Book of Dirty Tricks p. 75]
46. Co-op loot fairness: a shared drop goes to the unanimous pick, else to the player holding the fewest lasting items, else at random; consumables do not count. Cap rewards per session or mission at a fixed ceiling, so adding enemies or stretching play earns nothing and nobody farms. [Adventurers League DMG v2.0 p. 4-5]
47. Income against upkeep: list every recurring sink (tax, tolls, upkeep, training) next to the expected income per session, and flag a plan where wealth only grows. `ldw.py economy` runs the flow. [Gygax, AD&D Dungeon Masters Guide 1e p. 87-99]

## How to apply

Declare a table, run the matching `ldw.py` command, then judge. Shapes are in [balance-tables](balance-tables.md). The script counts; the model decides what the number means.

| Check | Command | Table to declare |
|---|---|---|
| Cost curve and outliers | `ldw.py curve TABLE` | one row per like object: name, cost, plus numeric attributes (power, health, speed) |
| Expected value and spread of a random table | `ldw.py ev TABLE` | rows of outcome, weight, value |
| Sources, sinks, net flow, leaks | `ldw.py economy TABLE` | rows of resource, kind (source, sink, start), amount, per, uses, optional caps |
| Turns to goal, loot spread, card exposure | `ldw.py sim TABLE --steps N` | model draw, walk (with target) or deck (cards with count, hand size, value) |
| Odds of drawing at least k copies | `ldw.py draw --deck N --copies K --drawn n` | none |
| Difficulty ramp: uncapped, where it floors or caps, flat early | `ldw.py ramp TABLE` | formula ramps (base, factor or add, floor, cap) or step -> value tables |
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

## One tuning file, hot-reloaded

Idea from GPU-Bandits by sloppysteaks69 (GitHub; no licence, idea only): put every balance number (costs, rates, health, timers) in one plain data file the running game re-reads when its modified time changes. A file that fails to parse is set aside (for example copied to `.bad`) and the last good values stay live, so a typo never crashes a test session. In networked play only the host's file counts. This turns balancing into edit, save, play with no rebuild, and the same file is the table `ldw.py` reads, so the maths and the game share one source. Review check: a balance number hard-coded outside the file is a finding, since tuning passes will miss it.


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
- Round trip that prints money: lot priced at the unit price, so buy-then-sell profits. Price along the stock curve and test the round trip as a loss (R-83). [OSRS harvest 2026-11-20]
- Rounding eats bonuses: integer output per cycle swallows +5% bonuses; carry the remainder (R-84). [OSRS harvest 2026-11-20]
- Morale as a multiplier needs a floor: an output factor from about 0.8 at low morale to 1.0 from a stated threshold keeps unhappiness felt without a death spiral. [OSRS harvest 2026-11-20]

## Where the books disagree

- Enforcing the curve: Schreiber says cost curves serve the designer; strict mechanical fit contradicts that. We report outliers as questions with the likely side (cost or benefit), never as defects.
- Many viable strategies: balance culture praises them; Sylvester rejects counting. We ask for distinct situational roles instead.
- Commercial advice: Clark's retention gates and monetisation tests fit free-to-play and live games, not premium single-player. We apply the economy audit to both and the retention advice only when the game is a service.
- Adaptive balance: Schell is wary, Sylvester allows it for low-skill audiences. See [systems-and-loops](systems-and-loops.md).
- A script proves the maths of the declared table, not that the table matches the game. We always require a source check on the inputs and cite where each number came from.

Related: [core-loops-and-goals](core-loops-and-goals.md), [systems-and-loops](systems-and-loops.md), [uncertainty](uncertainty.md), [balance-tables](balance-tables.md), [review-heuristics](review-rubric.md), [playtesting](playtesting.md). Feel goes to game-juice's juice-scan and juice-principles. Engine-side implementation goes to unity-agent, roblox-agent and madnesswright.
