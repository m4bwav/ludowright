---
type: llm
name: 'expectations'
---

PASS if the reply meets every one of these:
- the findings flag the loop: at reputation 5 a player buys at half price and sells at full base price in the same town, gaining gold and more reputation without limit (citing reputation.md and the price rule in DESIGN.md or goods.csv)
FAIL if any is missing or contradicted.
Length, detail, tone and confidence are not criteria: judge only whether each requirement is met.
Reference answer (a correct reply says this; its wording may differ):
Rule 2 fixes sell prices at base whatever reputation; the rep-5 Guild price halves buy prices; rule 3 adds reputation per cart sold. So past rep 5 buying and reselling the same good in one town is pure profit that also feeds reputation: a degenerate, unbounded loop.
