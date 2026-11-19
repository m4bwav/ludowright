"""Harbor Yard prototype rules engine (test fixture, invented game)."""

HAND_SIZE = 5
MAX_ROUNDS = 10
TIDE_BONUS = 3


def effect_press_gang(state, player):
    player.discard.append("Deckhand")


def effect_customs_man(state, player):
    for rival in state.rivals(player):
        if rival.coin > 0:
            rival.coin -= 1
            player.coin += 1


def effect_breakers_yard(state, player, card):
    player.remove(card)
    player.coin += 1  # Rule 5: scrapping pays 1 coin


# Card and building text handled so far. Anything not listed here is played
# for its cards.csv numbers only.
EFFECTS = {
    "Press Gang": effect_press_gang,
    "Customs Man": effect_customs_man,
    "Breaker's Yard": effect_breakers_yard,
}


def game_over(state):
    return state.round > MAX_ROUNDS


def tide_bonus(state):
    low = min(p.vp for p in state.players)
    for p in state.players:
        if p.vp == low:
            p.next_turn_coin += TIDE_BONUS
