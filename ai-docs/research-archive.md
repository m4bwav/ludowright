# Research archive: ludowright

Findings log entries moved out of the installed skill folder to keep it small. Newer entries: [skills/ludowright/RESEARCH.md](../skills/ludowright/RESEARCH.md).

### R-20261029-6 · 2026-10-29 · Testing: golden maths, seeded sims in a band, schema-checked findings
- Summary: game-sim harnesses keep exact results apart from Monte Carlo estimates: golden tests for exact maths, fixed seeds plus a standard-error band for sims. Adopted in tests/test_ldw.py and the findings validator.
- Track: testing
- Sources: https://docs.rs/jugar-web/0.1.3/src/jugar_web/simulation.rs.html
- Magnitude: n/a (initial)
- Applied: C-20261029-1

### R-20261029-5 · 2026-10-29 · Tooling: game-design skills exist but none reviews with evidence or ships evals
- Summary: davila7/claude-code-templates game-development (about 536 installs) routes to sub-skills; jarrodmedrano game-design-theory (43 installs) applies Rouse's player-experience view with no workflow or output format; playableintelligence design-game is a juice checklist; gamenumerics and other balance MCP servers have no visible users. ludowright's evidence rule, findings contract and suite are the differentiators. Read from snippets and one fetch; read the top two in full next refresh.
- Track: tooling
- Sources: ludowright ai-docs/research/2026-10-29-ai-for-game-design-ideation-critique.md, ai-docs/research/2026-10-29-ai-playtesting-and-simulated-balance.md
- Magnitude: n/a (initial)
- Applied: C-20261029-1

### R-20261029-4 · 2026-10-29 · Practice: balance by simulation depends on the player policy
- Summary: RuleSmith (Feb 2026) tuned an asymmetric game with LLM self-play, and the balance broke when the agents changed; Machinations' persona runs and the ESG+P study show the assumed strategy moves win rates from 40% to 66-81%. Rule 4 and references/balance.md make every balance claim name its policy and report a spread.
- Track: practice
- Sources: https://arxiv.org/html/2602.06232v1, https://machinations.io/articles/balancing-f2p-economies-simulating-player-personas-and-progression-curves-with-machinations, https://journals-sol.sbc.org.br/index.php/jis/article/view/4186
- Magnitude: n/a (initial)
- Applied: C-20261029-1

### R-20261029-3 · 2026-10-29 · Practice: LLM design critique misreads intent and flatters
- Summary: designers report LLM critiques that misread a game's core; sycophancy reinforces mistakes. MeepleLM (ACL 2026) grounds critique in rules with an MDA chain and personas. Rules 1-3 (restate intent, evidence or nothing, rule then dynamic then experience) come from this.
- Track: practice
- Sources: https://arxiv.org/pdf/2601.07251, https://arxiv.org/pdf/2510.03667, https://thealexandrian.net/wordpress/tag/ai
- Magnitude: n/a (initial)
- Applied: C-20261029-1

### R-20261029-2 · 2026-10-29 · Practice: AI is used for ideation; generic output is the failure
- Summary: GDC 2026 survey, 81% of AI-using developers use it for research and brainstorming; LLM ideas arrive as few-word feature lists; board game designers call the output derivative. Rule 6 and the design procedure's specificity gate come from this.
- Track: practice
- Sources: https://www.techspot.com/news/111128-more-than-50-game-developers-generative-ai-harming-the-industry, https://arxiv.org/pdf/2402.18659, https://boardgamewire.com/index.php/2026/03/27/more-than-half-of-board-game-designers-in-ttgda-survey-have-used-generative-ai-in-their-work/
- Magnitude: n/a (initial)
- Applied: C-20261029-1

### R-20261029-1 · 2026-10-29 · Creation pass
- Summary: the design canon read in nine groups by reading subagents (27 notes files, chain steps 1-3), merged into twelve kb topic files and a 52-item review rubric (steps 4-5); two web research passes on AI for game design (thin: 12 searches, 2 fetches). Partial reads are listed in ai-docs/log.md. cost: searches 12 · fetches 2 · tool calls about 600 across subagents
- Track: subject
- Sources: books listed in ai-docs/reading/inventory.md (owner's copies; not redistributed)
- Magnitude: n/a (initial)
- Applied: C-20261029-1
