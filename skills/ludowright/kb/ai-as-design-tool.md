# AI as a design tool

Answers: where AI (procedural generation, player models, simulated playtests, automated balance, LLM ideation and critique) helps a designer, where it fails, and which guards ludowright applies. Load before using any of these in a one-pager, review, balance claim or playtest plan.

## Principles

1. Fix an agent's purpose on two axes before using it: win or experience, player role or non-player role. An agent that wins by exploit says something different from one that mimics a human. [Yannakakis ch. 4]
2. An optimiser is an exploit detector. If a search or learning agent finds one dull dominant tactic, assume humans will, and log it as a balance finding. [Yannakakis ch. 4; Sutton ch. 3]
3. Reward hacking is the formal twin of a degenerate strategy: an agent maximises the stated score, not the intent. Audit every score or progress signal for what an optimiser could do to raise it without advancing the real goal. [Sutton ch. 3]
4. An agent that finds nothing has not shown nothing exists. Any "automated playthrough found no exploit" claim must say how the agent explored. [Sutton ch. 1-2]
5. Human-like testing needs human limits: reaction time, mistakes, pauses, exploration habits. List which a test agent models, and compare its output with a few human sessions. [Yannakakis ch. 4, 9]
6. Describe each target player as weights on goals (a persona) and run one agent per persona. Report distributions across personas, not an average. [Yannakakis ch. 4; research 2026-10-29 playtesting note]
7. A balance claim names its player policy and agent pool. Balance found against one pool can collapse against another. [RuleSmith, 2026-02-05]
8. A trained agent shows what is exploitable for that agent, not what is fun. Pair every simulation with human playtests. [Sutton; Yannakakis ch. 9]
9. Headless, fast-forwardable game logic is the enabling condition for simulated playtests, automated balance and search-based generation. [Yannakakis ch. 5, 9]
10. Scripted heuristic bots or tree search are usually cheaper than reinforcement learning for small card or strategy games. [Sutton caution; Yannakakis ch. 4]
11. Classify any generator before judging it: necessary or optional content, functional or decorative, constructive or generate-and-test, runtime or offline, autonomous or mixed-initiative. [Yannakakis ch. 7; Shaker ch. 1]
12. Necessary content needs an automatic completability check; decorative content needs taste. Generated levels are not playable until a solver says so. [Yannakakis ch. 7; Shaker ch. 1; research 2026-10-29 playtesting note]
13. Judge a generator on quality and diversity separately and show its reach with an expressive-range plot over designer-chosen metrics that are not the inputs. Sample until the distribution stops changing. [Shaker ch. 12; Short ch. 22]
14. Three evaluators: direct features, simulated agents, human ratings. Match the agent's skill to the question (playable versus enjoyable). [Shaker ch. 2; Yannakakis ch. 8]
15. Give a generator a control surface (parameters, feature vector, sketch), not just a seed. [Shaker ch. 2, 12; Yannakakis ch. 7]
16. Mixed-initiative is the realistic form: the machine proposes variants and checks constraints, the designer owns the objective. Reuse the validity checker as a machine playtester. [Shaker ch. 10; Yannakakis ch. 7]
17. Adaptive systems need a player model, a visibility policy and an off switch for comparison. Start with one tracked dimension (a director) and validate it against player reports. [Shaker ch. 10; Yannakakis ch. 10]
18. Playtest instruments: prefer ranked or pairwise judgments over absolute ratings, fix the time between play and report, expect peak-end bias, and triangulate with behaviour logs (where players stall, quit, which path they pick). [Yannakakis ch. 2, 10; Shaker ch. 12]
19. LLMs help most at ideation and first drafts of text-like content. They are weak at spatial planning and guaranteed correctness: treat output as input to a checker. [Yannakakis ch. 5; research 2026-10-29 ideation note]
20. Player modelling for adaptation or monetisation raises consent and data-ownership issues. Flag them; do not design them without a privacy note. [Yannakakis ch. 15]
21. A generative world model (a learned simulator or interactive video model, such as Google DeepMind's Genie line) can stand in as a quick prototype or playtest world. Agents and players will find exploits of the model's hallucinated dream that the real game does not have, so verify every finding in the real build. Access is perishable: as of 2026-01-30 Genie 3 was open only as Project Genie, a Google Labs prototype for US AI Ultra subscribers with 60-second sessions (Google DeepMind launch coverage, techbriefly.com, 2026-01-30). [Foster ch. 12]

## When reinforcement learning is worth it

Principle 10 still holds: try scripted bots and search first. If RL is chosen, these apply. Source: Lapan, Deep RL Hands-On 3rd ed.

1. The reward is the design. Pay for per-step changes the agent causes (a kill, a death), not the HUD running score, and check how long the payoff is delayed. [Lapan ch. 1]
2. Record a few player demonstrations before training. A handful of demos beats hours from scratch on tasks that are hard to discover. [Lapan ch. 14]
3. Many fast headless copies of the environment matter more than a bigger model. [Lapan ch. 9, 12]
4. Start with PPO and compare over several seeds. A single run misleads. [Lapan ch. 16]
5. Sparse key-then-door goals need curiosity or count bonuses. [Lapan ch. 18]
6. Judge self-play by round-robins between saved checkpoints, not by the loss. [Lapan ch. 20]
7. When the wanted style cannot be written as a reward, learn one from pairwise clip preferences, in rounds. The agent exploits flaws in the reward model, so refresh it. [Lapan ch. 19]

## How to apply

Guards ludowright adopts, run on its own output:

1. Specificity. A one-pager names a specific verb, a constraint and a hook, not a few-word guideline. If it reads like any game, rewrite it.
2. Restate intent first. Before any critique, write the design's own stated intent in one or two sentences and check it with the user if unsure. Critique against that intent, not against a generic ideal.
3. Cite the rules text. Every finding quotes or points to the location (file, section, line) it rests on, and traces rule, then dynamic, then player experience, and names which persona it hurts.
4. A no-issue path. A review may say "no issue found" for a check. Never invent a flaw to fill a rubric.
5. Feel-dependent findings are marked `needs-playtest` or handed to juice-scan ([feel-handoff.md](feel-handoff.md)). Paper cannot show feel.
6. Balance claims name the policy (random, greedy, heuristic, search, persona weights) and the agent pool. No "balanced" without both.
7. Seeded simulations are reported as distributions: p05, p50, p95 and the seed range, never a single run. Exact maths gets golden tests; Monte Carlo gets fixed seeds and a tolerance band.

Procedure:

1. Decide the question: exploit hunt, winnability, difficulty band, economy drift, or generator coverage. Each calls for a different agent.
2. Pick the cheapest agent: closed-form first (`ldw.py ev`, `ldw.py curve`, `ldw.py economy`), then seeded Monte Carlo (`ldw.py sim`), then a search or heuristic bot, then RL only if the game justifies a simulator and reward.
3. For deckbuilders, sample hands and report per-step value and how often each card is seen; a best-line search is a separate step and not yet built into `ldw.py sim`. A bot that fights a punching bag misses enemy interaction.
4. For an LLM player, treat it as a probe for bugs and difficulty, not as a search for exploits.
5. For generators, fill in a generator card: role, content type, control surface, evaluator, validity guarantee, expressive-range plan.
6. Compare any simulation against at least a few human sessions before trusting a balance verdict.

## Failure patterns

- Generic ideation. Symptom: one-pager that fits any game; no verb, constraint or hook. [research ideation note; LLMs and Games survey]
- Sycophantic critique. Symptom: review praises, misreads core principles, cites no rules text. [research ideation note]
- Invented flaws. Symptom: every rubric line has a finding. [research ideation note]
- Pool-bound balance. Symptom: win band reported with no agent pool; collapses when the pool changes. [RuleSmith]
- Single-run claim. Symptom: one simulated result, no spread or seed range. [research playtesting note]
- Exploration-blind test. Symptom: "no exploit found" with no description of agent exploration. [Sutton ch. 1]
- Missing per-step cost. Symptom: a task with no time cost, so an agent (or player) idles or farms. [Sutton ch. 3]
- Proxy reward. Symptom: scoring that pays for kills, combos or resources as ends in themselves. [Sutton ch. 3]
- Superhuman test bot. Symptom: bot spec has instant reactions, never fails or idles, never compared to humans. [Yannakakis ch. 4]
- Generator without a verifier. Symptom: necessary content with no completability check. [Yannakakis ch. 7, 9; Shaker ch. 1]
- Seed-only generator. Symptom: tuning means rerolling. [Yannakakis ch. 7]
- Unmeasured diversity. Symptom: no coverage metric; repeated-feel worlds. [Yannakakis ch. 8]
- Proxy-free level quality. Symptom: levels judged by eye only. [Togelius ch. 7]
- Absolute-score survey. Symptom: averaged 1 to 5 ratings with no baseline. [Yannakakis ch. 2]
- Late-recall survey. Symptom: feedback long after play, dominated by the ending. [Yannakakis ch. 2]
- Unvalidated director. Symptom: adaptive difficulty tracking a signal nobody checked against player reports. [Yannakakis ch. 10]
- Runaway weighted-sum fitness. Symptom: one objective dominates a generator's score. [Shaker ch. 2]

## Where the books disagree

- Research favours learning agents; practice favours scripted bots and tree search for small games. Ludowright starts with the cheapest agent and escalates only when it cannot answer the question.
- Ratings versus ranks (Yannakakis, Shaker) against common Likert practice. Ludowright offers ranks as the better default and does not forbid ratings; it asks for a baseline and a sample size.
- The 20 to 40 percent cost saving claim for simulated playtesting comes from a vendor-linked source (Yannakakis ch. 7). Ludowright does not quote it.
- LLM-written GDDs scored well in one small panel study (hyper-casual game), while designers report derivative output. Ludowright trusts structure and drafts, not originality or critique, and applies the guards above.
- Capability claims date from mid-2025 (Yannakakis ch. 5) and early 2026 (RuleSmith, MeepleLM, board games only); treat tooling claims as perishable and recheck before relying on them.

Related: [game-ai-for-designers.md](game-ai-for-designers.md), [production-and-scope.md](production-and-scope.md), [feel-handoff.md](feel-handoff.md). Headless harnesses, batch generation and metric export to CSV are engine work for unity-agent and roblox-agent. Feel goes to game-juice (juice-scan, juice-principles). The one-pager, beat chart and playtest protocol templates live in those plugins' game-design references.
