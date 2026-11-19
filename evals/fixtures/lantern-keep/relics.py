"""Relic effects. Each effect_key in relics.csv maps to a function here."""


def oil_plus_1(state):
    state["oil_per_turn"] += 1


def double_burn(state):
    state["burn_per_lantern"] = 2


EFFECTS = {
    "oil_plus_1": oil_plus_1,
    "double_burn": double_burn,
}


def apply_relic(state, effect_key):
    effect = EFFECTS.get(effect_key)
    if effect is None:
        return  # unknown effect: relic does nothing
    effect(state)
