# Lantern Keep (prototype)

Status: prototype, week 3 of 10. Built so far: the night loop, three relics, the moth enemy.

A solo turn-based tower game. Each night moths climb the keep; you light lanterns to burn them.

## Rules

1. Each night has 6 turns. Each turn you gain 2 oil and may spend oil to light lanterns (1 oil each).
2. A lit lantern burns one moth on its floor per turn.
3. Relics are found after nights 2, 4 and 6 (see relics.csv).

## Winning

You win in one of two ways:

- **Dawn win:** survive 8 nights.
- **Beacon win:** carry the Sunstone relic to the roof and light it. This is the fast path the game is built around: a bold player should be able to win by night 5.

## Losing

You lose when 10 moths reach the roof.
