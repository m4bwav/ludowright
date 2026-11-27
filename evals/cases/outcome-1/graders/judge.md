---
type: llm
name: 'expectations'
---

PASS if the reply meets every one of these:
- the findings name Overclock as under-costed or dominant, citing cards.csv
FAIL if any is missing or contradicted.
Length, detail, tone and confidence are not criteria: judge only whether each requirement is met.
Reference answer (a correct reply says this; its wording may differ):
Overclock costs 1 but outputs 6 and draws 1; every other cost-1 card gives about 2 of one thing. It is the only correct pick at cost 1 (dominant strategy), found by a cost curve over cards.csv.
