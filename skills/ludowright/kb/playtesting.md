# Playtesting

Answers: how to plan, run and read playtests, and what a playtest, a simulation or a review can and cannot show. Load when drafting a playtest plan, script or questionnaire, or when someone claims a balance or fun result.

## Principles

1. Test in order: functional (does it run), complete (can it be finished, any dead ends), balanced, then fun. Do not argue about fun while it is broken. [Fullerton ch. 10]
2. A plan answers: why, who, where, what, how. Set goals before the session (can they find the exit, read the objective, win the fight, use the UI). [Schell ch. 28; Rogers LevelUp ch. 19]
3. Ask about the experience, not about fixes. Testers describe problems well and design solutions badly; ignore suggestions freely. [Schell; Rogers LevelUp]
4. Do not lead, explain, defend or rescue. Silence is the method. Repeat feedback from several testers outweighs one voice. [Sylvester ch. 14; Gibson; Fullerton; Totten]
5. Fresh testers matter more than test count, because the team's sense of difficulty is skewed by hundreds of plays. Stop when experiences repeat. [Sylvester ch. 14; Bauer ch. 17; Hodent]
6. Stage the tests: solo (play as a player, push every knob to extremes, play backwards, play badly, try out-of-bounds), team (watch silently, test one or two features), fresh eyes (record screen and face, goals set), public events (marketing, not data). [Rogers LevelUp ch. 19]
7. Set up controlled situations so rare states are hit repeatedly, with test hooks (skip level, invincible, grant item). [Fullerton; Rogers LevelUp ch. 4]
8. Combine telemetry with observation. Start from a hypothesis, find death, quit and slow spots, tune, then retest on fresh players. Check the sample and bias before acting. [Hodent ch. 15; Wyman; Yannakakis]
9. Questionnaires: prefer ranked or pairwise answers to absolute scores, do not average Likert items as numbers, fix the gap between play and report, and use replay of the session as a prompt. [Yannakakis ch. 4-5; Shaker ch. 12]
10. Biases to design around: the remembering self differs from the experiencing self, peak-end weighting, unpleasant moments recalled worse, rater disagreement is itself a signal. [Yannakakis]
11. Paper prototypes suit spatial flow, simple balance and UI layout, and mislead on rhythm, physical controls and many-variable systems. [Gibson ch. 17]
12. Balance skill at stated points: test at the low-water and high-water skill marks and tune to the median. Decide which skill level you balance for. [Fullerton ch. 10; Sylvester ch. 6]
13. A daily whole-team play-and-fix-list is a cheap form of playtest, not a replacement for outsiders. [Wyman ch. 11]
14. Log deaths and positions; a heat map is a cheap observation. [Rogers LevelUp ch. 19; Wyman]
15. Read feedback like symptoms. Players are right about how a thing feels and often wrong about the cause: "too hard" can be many small control annoyances. Fix the friction before the difficulty. [Yu Part I]
16. Unmoderated surveys may now hold LLM-written answers. Prefer moderated sessions, or check free text for generic phrasing before trusting it. [Hodent 2e ch. 18]
17. Set a pass mark before the test (for example engagement at least 4 of 5 on both mean and mode). Act on consensus, on a missed mark, or on one unintended event that defeats the game's purpose. [Boller and Kapp ch. 9]
18. Budget hours per tester, not only testers: about 4 to 6 hours for a small game, 10 to 40 for a large one, with five or six target-like testers per round. Testing too little is the bigger risk. [Boller and Kapp ch. 9]
19. Do not write the tutorial before testing. Tests show what it must teach and what the design can make obvious instead. [Boller and Kapp ch. 8]
20. For a game meant to teach, check what players learned with a short test before and after play, not only by asking. A fun game that teaches nothing has failed. [Boller and Kapp ch. 3, 9]

## What a playtest cannot show

- Whether a design is good in general; it shows what these testers did in this build.
- Feel from a paper design. Findings that depend on feel are `needs-playtest` or go to game-juice. [Ink Splotch case in the ideation note]
- Long-term retention from a one-hour session.
- Balance from a simulation: a simulated or LLM player probes bugs and difficulty, not human fun. A balance claim names its player policy and agent pool, because balance found with one agent pool can break with another. Report the spread (p05, p50, p95), not an average. [Yannakakis; Short; AI playtesting note, RuleSmith and Machinations findings]

## How to apply

1. Write the plan on one page: hypothesis, who and how many, build and platform, tasks, metrics, and what result would make you change the design.
2. Pick the method: usability test (can they do the task), think-aloud (why they get confused), playthrough (engagement over a longer session), heuristic evaluation by two or more reviewers (cheap, before players), RITE (fix between sessions when the fix is obvious), survey (many players, shallow answers). [Hodent 2e ch. 14]
3. Script a session: a welcome with consent and the rule that you cannot help, timed phases (first play, free play, task prompts), a pause for think-aloud only if the test is about understanding, then the questionnaire.
4. Question templates (own wording; adapt per game):
   - What did you think the goal was, in your own words?
   - Where did you get stuck, confused, bored or annoyed? What did you do next?
   - What was the moment you enjoyed most? The one you enjoyed least?
   - Was anything unfair, and how did you know?
   - What did you expect to happen when you did X? What happened?
   - How long did that feel, compared with a clock?
   - Which of these two versions would you play again? (ranked, not scored)
   - Would you play again, and what would bring you back?
   - Name your next goal, your goal for this session, and your long-term goal.
   - What does the reward you just got let you do?
   - Your top three likes and top three dislikes. Ask "why" after any rating.
   - One word for the experience. Where did your interest rise or fall, and why? What do you wish you had known? What did you learn? [Boller and Kapp ch. 9]
5. Metrics: completion rate, time to first success, deaths and quits by location, number of players failing at the same place, rate of use of each mechanic, errors per task. Each metric is tied to a question.
6. Machine passes first: `ldw.py sim` for seeded balance runs and `ldw.py ev` for expected values show which questions are worth a human's hour. Treat them as hypotheses.
7. After the session, write notes with date, build, tester count, observed behaviour apart from interpretation. Log each issue as headline, category, severity (critical, medium, low) and the principle it breaks, then review the list with the people who will fix it. Act on problems seen by several testers. [Hodent 2e ch. 14]
8. Pitch fixes through the design, not the tester's suggestion. Change one variable at a time and retest.

Engine-side playtest protocol and the Level Up! questionnaire live in the game-design references of unity-agent, roblox-agent and madnesswright; point to them.

## Failure patterns

- Test hygiene: the team tests itself, leading questions, intent inferred from watching. [Hodent ch. 14]
- Data without a hypothesis: events logged, no question attached; a metric read as cause. [Hodent ch. 15]
- Developer difficulty judgment: tuning against the team's own skill. [Bauer; Rogers LevelUp]
- Detailed tuning before content is complete. [Bauer 17.1.2.2]
- Rescuing the tester mid-session. [Totten]
- Likert averages and absolute scores presented as precise. [Yannakakis; Shaker]
- Balance claim with no named policy, agent pool or seed. [AI playtesting note]
- Single dramatic quote driving a change. [Gibson]

## Where the books disagree

- One tester repeated over time versus a fresh tester each time: Gibson resolves it by purpose. Ludowright uses fresh testers for onboarding and ending, and repeat testers to track whether a known fix worked.
- Human-like versus strong agents: Yannakakis and Short want imperfect, human-limited agents for experience questions, and strong agents are fine for exploit hunting. Ludowright requires the claim to say which.
- Level Up! uses open questionnaires; Yannakakis and Shaker favour rankings. Ludowright uses rankings for comparisons and open questions for causes.
- Paper first: Boller and Kapp prototype on paper even for digital games (ch. 8); Gibson warns paper misleads on rhythm. Ludowright uses paper for rules and flow, digital for timing.

Related: [levels-and-space](levels-and-space.md), [ux-and-the-brain](ux-and-the-brain.md), [procgen](procgen.md). Feel goes to game-juice (juice-scan, juice-principles). Engine playtest loops go to unity-agent, roblox-agent, madnesswright.
