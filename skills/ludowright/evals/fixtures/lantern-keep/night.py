"""The night loop."""

ROOF_LIMIT = 10
NIGHTS_TO_DAWN = 8


def check_end(state):
    if state["moths_on_roof"] >= ROOF_LIMIT:
        return "lose"
    if state["night"] > NIGHTS_TO_DAWN:
        return "dawn_win"
    return None
