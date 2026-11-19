# Learning games

Answers: does a game meant to teach actually teach, does it measure what it claims, and is its motivation sound for the player it targets (children included). Load for any review or design of a learning, study or serious game. Written 2026-11-13.

## Review block

1. Name which mechanic teaches and which measures. A learning game needs both; borrowing either from commercial games is fine. [Plass, GDC 2012 abstract]
2. Label every mode teach or test. Quiz and trivia formats mostly test; new material must be taught somewhere before it is tested. [Kapp, fieldbook ch. 3]
3. One alignment row per learning goal: goal, activity, assessment, scoring. An empty cell is a defect, and a game verb below the goal's level (matching cannot teach "explain") is a mismatch. [Kapp ch. 3-4]
4. Pre-brief and debrief: name the topic before play (not the answer) and end with a short what-did-you-learn step. Experience without reflection stays stuck to that one game. [Kapp ch. 2]
5. Remove-all-rewards test: hide every point, badge and coin. If the player would no longer continue, motivation was a shell. [Chou ch. 2; Kim et al. ch. 9]
6. Score on at least two criteria (accuracy plus one more) and try to cheat your own scoring before anyone else does. [Kapp ch. 4, ch. 11]
7. Check each phase has a reason to play: discovery, onboarding, scaffolding (the repeated journey), endgame. Day-one and day-100 reasons differ. [Chou ch. 3]
8. Every learning goal has at least one event in play that exercises it; a goal no scenario triggers is untested. [Mangos and Ferraro ch. 3]
9. Write each adaptive feature as observe, assess, respond: the signal (answer, step order, pause), what it is taken to mean (a named misconception, low confidence), the change it makes (targeted retry, hint, harder content). Each part may stay simple. [Mangos and Ferraro ch. 6]
10. Rules before machine learning: rule-based adaptive difficulty already teaches well. Add a model only when rules cannot cover the errors and there is enough player data; aim at a success band, not a fixed level. For children, change difficulty between sessions, not mid-play. [Mangos and Ferraro ch. 6; adult training book, child use unverified]
11. Test a habit or study game over days, roughly 5 to 30, not one session: a single sitting cannot show whether behaviour changed. Plan the check-in points before the test starts. [Ferro ch. 8; book rule, unverified]
12. Split each feature's effect: what it motivates, and what about it gets in the way of learning for some player. A feature that pleases one group and annoys another (walking around, realism, sound) becomes an option, not a default. Common blockers to look for: content already known or out of reach, repeats, facts that contradict the lesson, typos, lag, loud audio, a wrong age band, a game that feels like homework. [Augmented Reality Games II ch. 2; book rule, unverified]
13. A mistake on the last step must not send the player back to the start or end on a game-over screen. Restart at the failed step and turn the error into a hint. [AR Games II ch. 2; book rule, unverified]
14. Fit one session to the real setting (a lesson slot, a bus ride) and let a stopped session resume later. Show where the skill is used outside the game. Item 10 already covers the success band. [AR Games II ch. 2; book rule, unverified]
15. A simulation that teaches must model the parts that define the real thing; a model that is wrong in those parts teaches the wrong lesson. List those parts and check each against a source. [AR Games II ch. 1; book rule, unverified]

## Question-driven play

Field rules from building a study RPG in 2026-11 (one child playtester; practice, not book rules, unverified beyond that game).

- Battles: each turn is one question. A right answer lands the hero's action, a miss means the foe's move lands. Cap a battle at a few questions (about 3) so one fight never becomes a test.
- A talk mode (convince the creature; lose resolve instead of hearts) can reuse the same turn engine with new words. Offer it mixed in or as an option, never as a way past the question.
- Bosses and dungeons ask the run's first-try misses first, then the hardest tier: a delayed retest dressed as a climax. A missed boss question comes back later in new words.
- Crafting and food stay downstream of answers: materials drop from battles won, recipes make cosmetics, helpers and small buffers (block the first 2 damage). No recipe may unlock content or skip a mastery gate, and nothing punishes the player for not eating.
- Scale by the hero's level between sessions, not inside a fight (item 10).
- Every power still asks a question. Class moves and spells are skins on the same one-question turn; mana fills from right answers (not time) and a missed spell spends none, so magic rewards knowing without bypassing it.
- Recharge with review, not a clock: a used ability (a waystone, a cooldown) comes back after one review question from mastered items, never a timer. Extra battle rounds and outposts in the wilds also draw from mastered questions, so spaced review lives in the world instead of a menu.
- Foes differ by numbers the player can read: own HP, about 3 named moves each, the foe card shows each move's damage and the next one coming. Show every hit as its sum (move + gear, move + elite bonus) so the player can see why a number is what it is.
- Spread encounters out and hide them until near (a rustle within about 3 tiles); a crowded map turns walking into back-to-back tests.
- Villagers give small fixed quests (bring 3 of a material, win 1-2 named fights) picked from the tile's hash, not a roll: the same place always offers the same task, which keeps rewards predictable for a child.
- Feedback hygiene on a busy screen: debounce bump messages (about 400 ms), cap the message strip at 3 and merge repeats, or messages bury the question.

## Named failures

- Pointsification: points, badges and leaderboards made the core, with no link to what is learned. [Kim et al. ch. 9; Werbach and Hunter ch. 6]
- Badge inflation: rewards so easy or so many that they mean nothing. Tie each to a mastery event. [Kim et al. ch. 9]
- Chocolate-covered broccoli: a quiz wrapped in unrelated play, where the game and the learning never touch. The fix is a mechanic that is the skill. [common term, after Bruckman 1999]
- Rewards-only push: once extrinsic rewards stop, motivation can fall below where it began. Keep rewards secondary and tied to mastery. [Chou ch. 3]

## Child and older players

- No variable-ratio rewards (loot rolls, random chests), no scarcity or countdown timers, no streak or one-more prompts that serve playtime rather than the child's goal. [Chou ch. 14; Werbach and Hunter ch. 6; Kim et al. ch. 7 treats these as neutral, we do not]
- Compare a lone child with their own past, not a public leaderboard; keep consequences light and retries immediate. [Kapp ch. 11]
- Older players: few clear steps, uncluttered screens, goals that adapt, and a plain account of what data is kept. [AR Games II ch. 7; book rule, unverified]

Related: [review-rubric](review-rubric.md) R-62 to R-64, [ux-and-the-brain](ux-and-the-brain.md) (motivation, dark patterns), [playtesting](playtesting.md).
