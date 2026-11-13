# Design drills

Answers: what to run when a design is stuck or an idea needs testing, as text exercises an agent can do. Load for ideation, a stuck design lane, or a puzzle or rule change to check. Adapted from Lockhart and Lang's workbook forms (ch. 1-8). Written 2026-11-13.

1. Rule remix. Number the rules of a known game, lock one, change exactly one other, and write the new rule so a stranger could play it. Test by self-play or `ldw.py sim`, amend once, then allow several changes. After each change answer: does the dominant strategy survive, does first-player advantage survive. Output the old rule, the new rule and both answers. [ch. 1, 2, 6]
2. Seeded random grid. Four columns of six options (for example field, goal, players, turn order). Roll one per column with a stated seed, combine, specify fully, run twice. Reject a one-pager that ignores a rolled cell. It breaks the first-idea habit. [ch. 1-7]
3. Constraint-first ideation. Pick two accessibility groups (low vision, colour vision, one hand, deaf, motor, memory, motion sickness, photosensitivity) and invent a concept that works for both from the start. [ch. 1]
4. Puzzle solvability check. A puzzle level needs at least one solution and at least one way to get stuck it can recover from or signal. Run a solver or a written search for the solution and for unintended shortcuts. [ch. 8]
5. Strategy-family balance. List the four or so early strategies, play each against the others; every one must be viable and none dominate all. Try symmetry, then intransitivity, then asymmetric profiles. [ch. 6]
6. Playtest feedback hygiene. Do not step in during a session. A tester who blames themselves is reporting a problem with the game. Record problems, not proposed solutions (theirs or yours), and pair any analytics with a live session, since data shows what but not why. [ch. 6; see [playtesting](playtesting.md)]

Related: [balance-and-economy](balance-and-economy.md), [uncertainty](uncertainty.md), [review-rubric](review-rubric.md) R-65 and R-66.
