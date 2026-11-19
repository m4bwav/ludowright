# Ember Market (test fixture)

An invented design for ludowright's eval suite. Not a real game.

## Pitch
A competitive deckbuilder for 2-4 players, about 40 minutes. You run a forge town: buy cards from a shared market row with coin, spend ember to raise buildings, and race to six buildings.

## Pillars
1. Many engines: no single card or route is always the right buy.
2. Rivals clash: Raid cards let you steal ember from the player on your left, so you watch your neighbours, not only your own deck.
3. The Kiln is a real gamble: risk your coin for a bigger payout when you need to catch up.

## Rules
1. Start with the deck in `tuning.json`; draw 5 each turn.
2. Play any cards; their ember, coin and draw are in `cards.csv` (values are what one play gives). Ember and coin left at the end of your turn are lost.
3. Buy cards from the market row with coin; raise a building by paying its cost in ember. Buildings stay in front of you and are not cards in your deck.
4. Once a turn you may gamble at the Kiln: pay the stake in coin and roll; payouts are in `tuning.json`.
5. Whenever you draw a Spark during your turn (including draws from card effects), gain 1 ember.
6. The game ends at the end of the round in which anyone owns 6 buildings, or after round 12. Most VP wins; each building is worth 2 VP plus its listed VP.

## Design note: the Foundry snowball is on purpose
Foundry pays more the more buildings you own. We want that: the game is a race to six buildings, so a leader's snowball ends the game sooner rather than dragging it out, and the end trigger caps it. In twelve playtests the Foundry player won three of twelve four-player games, exactly the even share, and losing players said the end came "at the right time". Keep it.
