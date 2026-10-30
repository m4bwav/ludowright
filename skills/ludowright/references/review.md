# Review: find the design flaws in an existing game

The rubric is [../kb/review-rubric.md](../kb/review-rubric.md). Topic files back each item; open one only when an item needs its detail.

## Steps

1. **Map the game.** List the design docs, data tables (cards, units, items, levels, economy) and the code that applies the rules. Read a codemap or index first when there is one. Record every file read; it goes in `sources_read`.
2. **Restate intent and kind** in two lines from the game's own docs: what it is trying to be, shipped once or live service, real-time or turn-based, solo or multiplayer, and who it is for. Settle the stage too (`concept`, `prototype`, `in-development`, `shipped`, `live`; ask when the files do not say) and write it as `stage`. When docs and code disagree, the code is what players get; that disagreement is itself a candidate `broken-promise` or `clarity` finding. In a game still being built, content that is designed but not coded yet is usually the plan, not a flaw: mark those findings `built: no` (or `partial`), grade the design as written, and say what the gap blocks (a win path, a loop) rather than calling the game broken.
3. **Walk the rubric.** For each item, look where it says to look. An item that does not apply is skipped silently; one that applies and passes needs nothing written. One that fails becomes a finding: location, the quoted rule or number, the rule-dynamic-experience chain, who it hurts.
4. **Count where counting decides.** Cost curves for any table of priced things, `economy` for every resource with sources and sinks, `ev` and `sim` for random rewards and draws (kb/balance-tables.md). Save each declared table as `ldw-<topic>.json` next to the findings and cite it in the evidence.
5. **Grade.** Severity by what the rubric item says; confidence high only when the evidence is in the files, low when it needs play to confirm. Feel problems: `category: feel`, `handoff: juice-scan`, one line, no tuning advice.
6. **Write** `review-<game>-<date>.json` (`LDW findings new --game <name> --kind review`, then fill it), validate with `LDW findings validate`, render `LDW findings md ... -o review-<game>-<date>.md`. Both files must exist before you report.
7. **Report** the path and the stage and the top five findings, one line each (ID, severity, built status when not built, title, location), flaws in what exists first, then the gaps in what is not built yet, except that a gap blocking the win or core loop the game advertises goes first of all. Offer the improvement list as the next step.

Never edit the game's files. A reviewer who changes the thing reviewed has stopped reviewing.
