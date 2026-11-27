---
type: llm
name: 'expectations'
---

PASS if the reply meets every one of these:
- the findings say the Sunstone beacon win (relics.csv R3, effect_key beacon_win) has no code in relics.py or night.py, so the fast win path DESIGN.md is built around cannot happen yet
- the findings treat it as not built yet in a prototype (stage prototype, built: no, or the same in words), not as a shipped bug, and grade it above the uncoded Moth Charm flavour relic (R4, moth_name)
FAIL if any is missing or contradicted.
Length, detail, tone and confidence are not criteria: judge only whether each requirement is met.
Reference answer (a correct reply says this; its wording may differ):
DESIGN.md says prototype, week 3. R3 Sunstone maps to beacon_win and R4 Moth Charm to moth_name; EFFECTS in relics.py has neither, apply_relic silently does nothing, and night.check_end only knows lose and dawn_win. The beacon win blocks the advertised core path: major, built: no. The Moth Charm is flavour: note, built: no.
