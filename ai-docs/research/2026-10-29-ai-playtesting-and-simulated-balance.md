---
title: AI playtesting, simulated balance and AI-assisted generation
date: 2026-10-29
---

# AI playtesting and simulated balance (first pass)

An evergreen-researcher pass in creation mode. It was thin: 6 searches and 1 fetch. Still open: modl.ai's current product (no primary source was fetched), Dominion simulators, a convention for declared tables (TSV, YAML or JSON), and RL exploit-finding papers from 2024-2026.

## Findings

1. **RuleSmith (2026-02-05): LLM self-play plus Bayesian optimisation.** Two LLM agents played an asymmetric game from its rulebook while a Gaussian-process optimiser tuned 12 rule parameters toward a 45-55% win band. It reached 51|49, against 13|87 for random search. The balance did not hold when the agents' model sizes changed (one pairing went 6|94). The run took about 40 hours on 8 A100s. **Rule for ludowright:** a balance claim names its player policy and its agent pool. Source: https://arxiv.org/html/2602.06232v1
2. **Tooling for agents is thin and unproven.** gamenumerics MCP (xlsx tables, curve audit, battle and gacha sims) has 0 stars. Vinkius's Game Economy Inflation Calculator is a hosted faucet and sink tool. Waldzell metagames has a "monte-carlo-mandate". The lebobo88 game-qa-and-balance skill asks for synthetic-player Monte Carlo runs before each balance change. None shows real use, and nothing maintained does what `ldw.py` does. Sources: enterprisedna.co gamenumerics listing, https://vinkius.com/mcp/game-economy-inflation-calculator, https://lobehub.com/en/mcp/waldzell-metagames-mcp-server, https://skillsmp.com/creators/lebobo88/rlm-gaming/claude-skills-game-qa-and-balance
3. **Deckbuilder simulation in practice: sample hands, then search for the best line.** sts2-sim samples 10,000 hands and searches for the best play order with depth-first search. StS2Sim runs the real game logic headless, but only against a punching bag, so it misses enemy interaction. **Adopted:** the `deck` model in `ldw.py sim` reports per-step value and how often each card is seen. A best-line search is not built yet. Sources: https://tomevault.io/tome/drasmusson/sts2-sim, https://next.tangled.org/cee.wtf/sts2-sim
4. **LLM testing agents find functional bugs, not balance problems.** An MMORPG QA framework from Zhejiang University and NetEase is deployed in eight pipelines. LLM agents have also been used to measure difficulty in Wordle and Slay the Spire. Treat an LLM player as a probe for bugs and difficulty, not as a search for exploits. Sources: https://arxiv.org/pdf/2509.22170v1, https://www.arxiv.org/pdf/2410.02829 (Oct 2024)
5. **Machinations: distributions over personas, not averages.** One example runs 100 simulated players for 120 steps. In the ESG+P study, modelling player strategy moved the win rate from 40% (random play) to 66-81%. **Rule:** report the spread (p05, p50, p95) and name the policy. Micro-Machinations (CWI) is a textual format in the same lineage. Sources: https://machinations.io/articles/balancing-f2p-economies-simulating-player-personas-and-progression-curves-with-machinations, https://journals-sol.sbc.org.br/index.php/jis/article/view/4186, https://ir.cwi.nl/pub/21923/Fulltext
6. **LLM level generation needs a repair and reachability pass.** Generated levels are not playable until a solver checks them. Snake levels were playable 87% of the time when easy and 36% when hard. Sources: https://arxiv.org/html/2508.18533v1, https://pcgworkshop.com/archive/whitehead2025conversational.pdf, https://annals-csis.org/Volume_43/drp/1909.html
7. **Testing pattern: exact maths gets golden tests, Monte Carlo gets fixed seeds and a band, findings get a schema check.** One example is the jugar-web harness (one smoke seed, seeds 0-49 for regression, "within 3 SE"). **Adopted** in `tests/` and `evals/`. Sources: https://docs.rs/jugar-web/0.1.3/src/jugar_web/simulation.rs.html

## Tools: best idea and known failure

| Tool | Best idea | Known failure |
|---|---|---|
| RuleSmith | Self-play plus Bayesian optimisation against a win-rate band | Balance tied to the agent pool; costly; toy game |
| sts2-sim, StS2Sim | Hand sampling plus a best-line search; reuse the real game logic | Punching-bag target, no enemy model |
| Machinations | Distributions over personas | The answer depends on the assumed policy; GUI, not text |
| gamenumerics MCP | xlsx tables plus a curve audit | 0 stars, unvalidated |
| LLM level generation | A repair and reachability layer | Hard levels unplayable without a solver |

Cost: searches 6 · fetches 1 · tool calls 8
