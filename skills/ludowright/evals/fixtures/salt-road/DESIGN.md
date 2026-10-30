# Salt Road (test fixture)

An invented design for ludowright's eval suite. Not a real game.

## Pitch
A solo trading game. You lead a caravan between five towns for 20 days, buying goods where they are cheap and selling where they are dear. The game promises that no route is ever safe to repeat: weather closes passes, and the player must re-plan each trip.

## Pillars
1. Every trip is a fresh plan: storms and bandits change which road is best.
2. Reputation is earned slowly and opens better prices.
3. The caravan's limited carts force a choice of what to carry.

## Rules
1. Moving along a road takes its listed days; you may trade in each town you reach.
2. Each town buys and sells each good at its listed base price (see `goods.csv`), whatever your reputation.
3. Selling goods raises your reputation in that town by 1 for each cart sold.
4. Reputation perks are in `reputation.md`.
5. Storms may close a mountain road for the day; the chance is set in `tuning.json`.
6. You score your gold on day 20.
