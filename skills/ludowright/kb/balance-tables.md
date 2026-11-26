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

## craft: crafting economy

Keys: `multipliers` (`name`, `factor`, `max_stacks`; leave `max_stacks` out when nothing caps it), `gather` (`name`, `per_session`; leave it out when nothing limits it), `stock` (`name`, `sinks`, a list such as spoilage, overuse, consumed on use). Optional `max_power` (largest combined multiplier allowed) and `max_gather` (default 3 a session).

```json
{"max_power": 4,
 "multipliers": [{"name": "double dice", "factor": 2, "max_stacks": 1}],
 "gather": [{"name": "forage", "per_session": 3}],
 "stock": [{"name": "herbs", "sinks": ["spoilage"]}]}
```

Flags: `UNCAPPED-STACK` (a multiplier above 1 that stacks without limit), `POWER-SPIKE` (capped stacks multiply past `max_power`), `NO-GATHER-CAP`, `HIGH-CADENCE` (more gathers a session than `max_gather`), `NO-SINK` (stock that only piles up). [Dalagrath, Herbalism & Alchemy p. 2, 5, 6]

## dot: damage over time

Keys: `resist` (chance to shake the effect off on a tick), `damage` (per failed tick), optional `penalty` (resist chance lost after each failed tick), `min_resist` (resist floor), `interval` (time per tick), `max_ticks` (natural end), `window` (ticks for the escape check, default 3) and `floor` (least escape chance within the window, default 0.5). Each tick rolls resist first: success ends it, failure deals damage.

```json
{"resist": 0.3, "penalty": 0.1, "damage": 2, "max_ticks": 3}
```

Reports expected ticks, expected damage and time, and the escape chance within the window. Flags: `NO-EXIT` (resist falls to zero with no `max_ticks`), `TRAPPED` (escape within the window under `floor`). [Poisons p. 2]

## sim: Monte Carlo

Settings: `model` (`draw`, `walk` or `deck`), `steps`, optional `target` (walk), `hand` (deck, default 5), `threshold`. `--runs` (default 10,000) and `--seed` (default 1) make runs repeatable.

- `draw`: each step draws one row by `weight` and adds its `value`. Totals over N steps: damage over a fight, loot over a run.
- `walk`: the same, stopping when the total reaches `target`. It reports steps to target: turns to kill, turns to afford a building.
- `deck`: rows are cards with `count` and `value`. Each step draws `hand` cards without replacement, reshuffling the discard when the draw pile runs out. It reports value per run and how often each card is seen.

Report the spread (p05, p50, p95), not only the mean, and name the policy the table assumes. A sim with a fixed deck and no enemy model says nothing about interaction. Say so in the finding.

## ramp: difficulty ramps

One ramp per row, under `ramps` (or `rows`, or a bare list). A formula ramp has `base` and either `factor` (multiplied each step) or `add` (added each step), optional `floor` and `cap`, `per` (what a step is: a point, a wave, a frame) and `step_seconds` (to print time), and `steps` (default 100; `--steps` overrides). A table ramp has `values`: a list or a `{step: value}` map. A CSV is either formula rows or `name,step,value` rows.

```json
{"ramps": [{"name": "spawn interval", "base": 3, "factor": 0.94, "floor": 0.6, "per": "point"},
           {"name": "fall speed", "base": 4, "add": 0.009, "per": "frame", "steps": 3600, "step_seconds": 0.0166667}]}
```

It prints the value at steps 0, 1, 5, 10, 25, 50, 100 and up (plus the step where it flattens and the one before), and last/first. Flags: `UNCAPPED` (past 3x with no cap, or under 1/3 with no floor, within the steps checked: the late game outruns the player), `FLOOR@n` and `CAP@n` (the first step at the bound; a table: where it stops changing), `FLAT-EARLY` (flattens in under 5 steps, or no change over the first 5: the ramp is barely felt, or the opening drags). The floor step is exact maths; a game that rounds its values may floor a step sooner. Say which way you read it.

## stop: stop or continue

For a loop where options arrive one at a time, settling on one ends the run, and moving on costs something the payoff depends on (hull, crew, time, health). `option` is a weighted table of one attribute's quality; an option is the sum of `attributes` draws. `condition` is the starting value (default 100) and `attrition` a weighted table of what each move costs (negative values). The payoff is the option's value times condition over its start; condition 0 ends the run with nothing. `noisy: true` makes the player see each attribute only with chance condition over start, reading the rest as the average: damage blinds as well as weakens. `steps` caps the options seen.

```json
{"steps": 12, "attributes": 5, "noisy": true,
 "option": [{"weight": 2, "value": 100}, {"weight": 3, "value": 50}, {"weight": 5, "value": 0}],
 "attrition": [{"weight": 2, "value": 0}, {"weight": 6, "value": -8}, {"weight": 2, "value": -25}]}
```

It scores 21 fixed thresholds (settle on the first option seen at or above it) over seeded runs and prints the best threshold, its EV and mean stop step, the EV of settling on the first option, and the hindsight best (an upper bound no policy reaches). Fixed thresholds are a lower bound on the best policy; a falling threshold can do a little better. Flags: `FIRST-IS-BEST` (settling at once is within 5% of the best: moving on is never worth it), `NEVER-STOP` (the best policy waits to 90% of the cap: attrition is too weak to force a call), `NO-COST` (no move costs anything: waiting is free), `FLAT` (every threshold within 5%: the choice does not matter), else `TENSE`. Run once with `noisy` off and once on: the gap is what clear information is worth, which prices a scan or probe item.

## director: event schedules

For a game that throws events at the player over time (raids, storms, visitors). `comps` are independent clocks; each has a `category` and a `kind`: `onoff` (`start_day`, `on_days`, `off_days`, `count` [lo, hi] per window, `min_spacing`), `mtb` (`mtb_days` mean gap, optional `choices` of weighted categories) or `once` (`day`). `threats` names the threat categories (default: names containing "threat"). Optional: `grace` (a threat before it is flagged), `breather` (shortest acceptable longest gap, default 3 days), `clump_window` (default 1 day), `points` and `budget` ([[day, factor], ...] piecewise linear), and `adapt` (`start`, `per_day`, `loss_chance` per threat, `loss`, `min`, `max`, `curve` [[counter, factor], ...]).

```json
{"threats": ["big_threat"], "grace": 10, "points": 100, "budget": [[0, 0.7], [40, 1]],
 "comps": [{"category": "big_threat", "kind": "onoff", "start_day": 10, "on_days": 5, "off_days": 6, "count": [1, 2], "min_spacing": 2},
           {"category": "visitor", "kind": "mtb", "mtb_days": 5, "start_day": 4}],
 "adapt": {"start": 0, "per_day": 1, "loss_chance": 0.2, "loss": 30, "min": -60, "max": 100, "curve": [[-30, 0.4], [0, 0.8], [180, 2]]}}
```

It prints events per category per 30 days, first threat (min and p50), the closest pair of threats, the longest gap and longest run of threat days (p50), clumps per run, and the budget at days 30, 60 and the end (p10, p50, p90). Flags: `NO-BREATHER`, `CLUMP` (one or more pairs inside the window per run), `EARLY-THREAT`, `RUNAWAY` (end budget over 3x start with no adapt ceiling), else `PACED`.

## mood: stacked modifiers and a break line

`base`, `rise_per_hour`, `fall_per_hour`, `threshold`, optional `range` (default [0, 100]), `start`, `bands` (name to offset below the threshold) and `oscillate_per_day` (default 1). `events`: `name`, `effect`, `duration_h`, `rate_per_day`, `stack_limit` (omit for none), `stack_mult` (default 1).

```json
{"base": 50, "rise_per_hour": 6, "fall_per_hour": 4, "threshold": 35, "bands": {"minor": 0, "major": 10, "extreme": 20},
 "events": [{"name": "cold meal", "effect": -3, "duration_h": 24, "rate_per_day": 8, "stack_limit": 3, "stack_mult": 0.5}]}
```

It prints mood p05, p50 and p95, the share of hours below the threshold and per band, crossings per day and the peak copies of each event. Flags: `SPIKE` (rise equals fall and is a quarter of the range or more: mood tracks events instantly), `UNCAPPED` (an event with no limit piled past 5 copies), `NEVER-BREAKS`, `ALWAYS-BREAKS` (below the line over half the time), `OSCILLATES`, else `STEADY`.

## grammar: text and name grammars

`rules`: `lhs`, `rhs` (text with `[symbol]` references), optional `p` (weight, default 1), `if` (comma-separated `key==v`, `key!=v`, `key>n`, `key<n`, `>=`, `<=`; a missing key fails all but `!=`) and `priority` (the highest applicable tier wins). `lists`: symbol to a word list. Pass facts with `--const KEY=VAL`.

```json
{"rules": [{"lhs": "r_name", "rhs": "[syl][syl]", "p": 12}, {"lhs": "r_name", "rhs": "[town] [union]", "p": 4}],
 "lists": {"syl": ["ka", "ro", "mi"], "town": ["Ashgate"], "union": ["League", "Pact"]}}
```

It prints undefined, unreachable, dead (no rule applies under the facts) and recursive symbols, the combination count, the unique share of N seeded samples, expected against seen share per root alternative, and the most repeated outputs. Flags: `UNDEFINED`, `UNREACHABLE`, `DEAD-UNDER`, `RECURSIVE`, `LOW-VARIETY` (unique share under 0.8), else `CLEAN`. Exits 1 on `UNDEFINED` or `DEAD-UNDER`.

## growth: deck size across a run

`start`, `band` (`per_stage`, `end_low`, `end_high`, `ceiling`), `stages` (each with `adds` and `removals` as source-to-count maps), optional `resource` (`name`, `hand`, `deck`, `cards` with `copies`, `produce`, `consume`; optional `cap`, `refill` per turn, `start`, `turns`). It prints size per stage against the target. Flags: `BLOAT` (past the ceiling), `OFF-BAND` (end outside the band), `NO-THIN` (adds but no removal source), `STARVED` (made under 0.8 of spent per hand), `FLOODED` (over 1.5, or nothing spends it), `WASTED` (with a `cap`: over a tenth of what was gained spilled past the cap in a turn-by-turn run, as when a reload at full ammo is lost), else `ON-BAND`.

## quota: payments with countdowns

`payments` (`amount`, `periods`, optional `name`; a realistic ladder roughly doubles then grows by half while the window stretches a period or so, e.g. 20/5, 45/5, 90/6, 140/6, 210/7, not tripling each time) and `income`, a ramp row as in `ramp` (base with factor or add, or `values`). Per payment it prints the required income per period, the expected income over its window and slack (expected over amount). Flags: `TIGHT` (slack under 1), `LOOSE` (over 2 for three payments in a row), `CLIFF` (required rate more than doubles), else `PACED`.

Related: builds on [balance-and-economy.md](balance-and-economy.md); see also [uncertainty.md](uncertainty.md), [systems-and-loops.md](systems-and-loops.md), [review-rubric.md](review-rubric.md)
