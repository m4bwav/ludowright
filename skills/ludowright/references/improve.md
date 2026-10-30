# Improve: ranked suggestions for an existing game

An improvement list answers "what should I change next, and why". It starts from the same evidence as a review, then ranks by what each change buys for what it costs.

## Steps

1. **Start from a review.** Use the newest `review-*.json` for this game if one exists and is newer than the files it read; otherwise run [review.md](review.md) steps 1-4 first.
2. **Find the weak spots, not only the flaws:** the core loop's decision (is it interesting every time, kb/core-loops-and-goals.md), the progression curve (kb/balance-and-economy.md), onboarding (kb/ux-and-the-brain.md), pacing (kb/levels-and-space.md), and scope (kb/production-and-scope.md). A weak spot is something that works but under-delivers on the game's own promise.
3. **Write each suggestion as a finding** with `impact` (high, medium, low: how much of the experience goal it moves, and for how many players) and `effort` (S hours, M days, L weeks for this team), plus the reason: the principle and the evidence. A suggestion names the change and its size ("cost 2, not 1"; "add a second sink at turn 10"), never "consider balancing".
4. **Rank** high impact and small effort first; the markdown view sorts by severity, impact and effort. Keep the top ten; move the rest to a "later" note in `summary`.
5. **Cross-check** that no two suggestions fight each other, and that none breaks the game's player promise. Say which suggestions need a playtest to confirm.
6. **Write** `improve-<game>-<date>.json` (`kind: improve`), validate, render the markdown, and report the top five.
