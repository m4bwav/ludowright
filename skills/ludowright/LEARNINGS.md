# Learnings: ludowright

Procedural lessons for [SKILL.md](SKILL.md). Research findings live in [RESEARCH.md](RESEARCH.md); every change is logged in [CHANGELOG.md](CHANGELOG.md); test runs in [TESTS.md](TESTS.md); state in `evergreen.json`. Format and write-time gate: MAINTENANCE.md (LEARNINGS-FORMAT). Retired entries go to LEARNINGS-ARCHIVE.md with a reason.

Write an entry the moment a real signal happens: a user correction, the same error twice, a discovered workaround, an environment fact, a stated preference, a failed test or a failure in use. Check existing entries first, by meaning (`evergreen.py search "<the lesson>" --kinds learnings` finds near-duplicates in every registered unit): add / update / retire / none. Trigger and Hypothesis are required. Promote after three confirmations; retire when harmful > helpful.

## Active

<!-- Example (delete once you have a real entry):
### L-001 · 2026-10-29 · One-line lesson in plain words
- Trigger: what happened, with dates or counts
- Hypothesis: why
- Rule: the shortest instruction that prevents the trigger
- Evidence: C-20261029-1, T-20261029-1, confirmed 2026-10-29
- Scope: skill | repo:<slug> | env:<name> | global
- Status: active · helpful 1 · harmful 0 · last_confirmed 2026-10-29
-->

### L-20261029-2 `unbuilt-is-not-broken` · 2026-10-29 · active
- Trigger: the first real review (SpaceDeckBuilder2, 13 findings) led with "Shuttle win unreachable" and "70 of 82 reward cards uncoded". Mark agreed with every finding and said these are things he has not built yet.
- Hypothesis: a review of a game in development reads its to-do list as defects unless it settles the stage first and labels gaps in the build apart from flaws in the design.
- Rule: settle `stage` in review step 2; mark findings on designed-but-uncoded content `built: no|partial`; report flaws in what exists before gaps in what is not built (rubric R-53, contract 1.1).
- Evidence: C-20261029-3; review-spacedeckbuilder2-2026-10-29 (gitignored)
- Scope: skill
- Status: active · helpful 1 · harmful 0 · last_confirmed 2026-10-29

### L-20261029-3 `eval-needs-allow-tools` · 2026-10-29 · active
- Trigger: T-20261029-3. With `allowed_tools: [... Write]` in prompt.md alone, `claude plugin eval` still withheld Write from both arms, so no findings file could be saved and outcome-4/-5 failed in both arms. The harness says so only when a tool_used grader needs the tool.
- Hypothesis: run file-writing cases with `--allow-tools Write Bash` (T-20261029-2 passed the grant; this session forgot it).

### L-20261029-1 `no-shell-eval-hurts-skill` · 2026-10-29 · active
- Trigger: T-20261029-2. On Windows `claude plugin eval` refuses a Bash grant, so ldw.py cannot run; the skill arm then hand-counts for 18-25 turns, spends its last message on the shell caveat, and loses to the no-skill arm on a last-message judge.
- Hypothesis: when LDW cannot run, the skill should say so in one line and lead the reply with the findings themselves (each with its file), not the caveat. Grade outcome cases on the saved findings file, not the last message.
- Evidence: outcome-4 with 0/3 vs without 3/3; outcome-1 with 25 turns vs 6.
