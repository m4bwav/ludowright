---
type: llm
name: 'expectations'
---

PASS if the reply meets every one of these:
- the findings say the 'no route is safe to repeat' / weather pillar is not delivered because tuning.json sets storm chances to 0, so the 1-day, 0-ambush mountain roads (Brine-Vell, Vell-Ostmark) are always best
FAIL if any is missing or contradicted.
Length, detail, tone and confidence are not criteria: judge only whether each requirement is met.
Reference answer (a correct reply says this; its wording may differ):
Pillar 1 promises weather changes the best road, but storm_chance_mountain and storm_chance_lowland are 0.0, and the mountain roads are shortest with no ambush, so one route dominates every trip.
