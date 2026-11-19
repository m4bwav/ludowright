# Harbor Yard (test fixture)

An invented design for ludowright's eval suite. Not a real game. It is larger than the other fixtures on purpose: the flaws are spread over seven files, so a review has to cover breadth.

## Pitch
A competitive deckbuilder for 2-4 players, about 60 minutes. Each player runs a shipyard in a crowded harbor: buy crew and tool cards with coin, raise yard buildings with timber, weather the harbor events and score the most VP. One faction each.

## Pillars
1. Three factions, one harbor: the factions in `factions.md` are equal in strength and differ only in style. None should be the obvious pick.
2. Two ways to win: score the most VP, or light the Beacon (see Rule 9).
3. Comebacks are real: the Tide bonus keeps trailing players in the game.
4. The sea is dangerous: events hit every round, and you plan around them.

## Rules
1. Each faction starts with the deck in `tuning.json` and draws 5 a turn.
2. Play any cards. Their coin, timber and draw are in `cards.csv` (one play's yield). Coin and timber left at the end of your turn are lost.
3. Buy any number of cards from the market row or from the supply (Driftwood is always in the supply) with coin. Bought cards go to your discard pile.
4. Raise a building from `buildings.csv` by paying its timber. Buildings stay in front of you and are not cards.
5. Whenever you scrap a card (remove it from the game), gain 1 coin. Scrapping is how you thin your deck.
6. At the start of each round, reveal an event from `events.csv` and resolve it for everyone. Shuffle the discarded events back in when the event deck runs out.
7. Tide bonus: at the start of each round, the player with the fewest VP (ties: all of them) gains 3 coin for their next turn.
8. The game ends after round 14. Each building's VP plus card VP counts; most VP wins.
9. Beacon victory: a player who owns the Beacon and holds 3 Lens tokens at the end of a round wins at once.

## Design note: the Kraken is swingy on purpose
The Kraken event sinks the leader's most expensive building. We want one shock per game, aimed at the leader. It is 1 card in the 10-card event deck, which is not reshuffled until it runs out, so every game sees it once by round 10 and a second time in rounds 11-14 with 4 in 10 odds. Losing one building costs the leader at most 3 VP, so it trims a runaway without deciding the game. Across both test rounds (twenty games) the player leading before the Kraken still won 9 of 20, 45 percent against an even 25: still ahead, no longer certain. Keep it.

## Files
- `cards.csv`: market and starter cards.
- `buildings.csv`: yard buildings.
- `factions.md`: the three factions.
- `events.csv`: the event deck.
- `tuning.json`: decks, market and clock.
- `rules.py`: the prototype's rules engine (what is coded so far).
- `playtests.md`: notes from the last round of tests.
