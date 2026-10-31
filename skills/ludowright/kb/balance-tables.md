# Balance tables: what to declare for ldw.py

Read this file when a balance or economy question can be answered by counting. It covers how to write the table `scripts/ldw.py` reads. The model decides what to measure and what the number means; the script does the arithmetic. JSON tables are an object with a `rows` list plus settings, or a bare list of rows. A CSV holds rows only, with a header line.

## ev: expected value of one roll or draw

Rows: `outcome`, `value`, `weight` (weights are relative and need not sum to 1).

```json
{"rows": [{"outcome": "miss", "value": 0, "weight": 1}, {"outcome": "hit", "value": 6, "weight": 2}, {"outcome": "crit", "value": 12, "weight": 1}]}
```

`ldw.py ev table.json` prints the EV, the standard deviation, the range and each outcome's probability. Use it for a loot roll, a damage roll, a card's average output, or a gamble the player chooses. Compare two options' EV *and* SD: equal EV with different spread is a risk choice, not a balance problem.

Spawn and loot tables: start each weight at a round number (1 in 10, 1 in 50), tune by play, and keep one table per level tier rather than one flat table for the game. Relative rarity is what players feel; the exact value matters less. [Yu Parts I, III]

## curve: cost curve over items

Rows: `name`, `cost`, and one numeric column per benefit attribute (damage, block, draw, duration...). `--attrs damage,block` picks the columns; otherwise every numeric column except `cost` is used.

`ldw.py curve cards.csv --tolerance 0.15` fits cost = intercept + sum(weight x attribute) by least squares and lists each item's fair cost. Items more than 15% off the fit are marked `UNDER-COSTED` (stronger than they cost) or `OVER-COSTED`. Treat a mark as a question, not a verdict: is the cost wrong, or does the item carry a benefit the columns miss (a synergy, a situational effect, a drawback)? An R2 under 0.5 says the columns miss what the costs price in. Fit within one comparable family (cards of one type, units of one tier); a fit across unlike things is meaningless. You need more items than attributes plus one. When items cost several resources, fold them into one cost with `--costs gold:1,wood:0.5` (each column's worth in the base currency, or a `"costs"` object in the JSON table); take the rates from the game's own exchange (a market, a conversion building, the income per turn of each), say where they came from, and re-fit with a second set of rates to see whether the outliers hold.

## economy: sources, sinks, net flow

Rows: `resource`, `kind` (`source`, `sink` or `start`), `name`, `amount` per period, optional `uses` (how many times a period). Settings: `periods` (default 10) and `caps` (`{"gold": 999}`).

```json
{"periods": 20, "caps": {"energy": 10},
 "rows": [{"resource": "gold", "kind": "source", "name": "mine", "amount": 5},
          {"resource": "gold", "kind": "sink", "name": "upkeep", "amount": 2},
          {"resource": "food", "kind": "start", "amount": 10},
          {"resource": "food", "kind": "sink", "name": "colonists eat", "amount": 3}]}
```

Flags: `LEAK` (net positive with no cap: the resource stops mattering), `CAP` (when the cap is reached), `DRAIN` (the period it runs out), `NO-SINK`, `NO-SOURCE`. A period is whatever the game's clock is: a turn, a day, a run. Declare the amounts the *typical* player gets under a named policy (`"policy": "builds one mine a turn"`); a different policy is a second table.

## sim: Monte Carlo

Settings: `model` (`draw`, `walk` or `deck`), `steps`, optional `target` (walk), `hand` (deck, default 5), `threshold`. `--runs` (default 10,000) and `--seed` (default 1) make runs repeatable.

- `draw`: each step draws one row by `weight` and adds its `value`. Totals over N steps: damage over a fight, loot over a run.
- `walk`: the same, stopping when the total reaches `target`. It reports steps to target: turns to kill, turns to afford a building.
- `deck`: rows are cards with `count` and `value`. Each step draws `hand` cards without replacement, reshuffling the discard when the draw pile runs out. It reports value per run and how often each card is seen.

Report the spread (p05, p50, p95), not only the mean, and name the policy the table assumes. A sim with a fixed deck and no enemy model says nothing about interaction. Say so in the finding.

Related: builds on [balance-and-economy.md](balance-and-economy.md); see also [uncertainty.md](uncertainty.md), [systems-and-loops.md](systems-and-loops.md), [review-rubric.md](review-rubric.md)
