# Research: ludowright

Findings that back [SKILL.md](SKILL.md). Changes they caused are logged in [CHANGELOG.md](CHANGELOG.md); procedural lessons live in [LEARNINGS.md](LEARNINGS.md); test runs and their evidence in [TESTS.md](TESTS.md); schedule and state in `evergreen.json`. Protocol: MAINTENANCE.md.

Topic: game design craft: core loops, systems, balance and economy, levels, UX and onboarding, playtesting, uncertainty, procedural generation, game AI design, and AI-assisted design and critique. Tier `moderate`. Last refresh 2026-10-29; next due 2026-11-28.

## Current understanding

- The design canon (Schell, Fullerton, Salen and Zimmerman, Sylvester, Koster, Sellers, Romero and Schreiber, Adams and Dormans, Costikyan, Hodent, Elias and others, read for this plugin on 2026-10-29; notes outside this repo) agrees on the core: a game is a loop of meaningful decisions; balance is checked against a declared intent; economies need sinks that match their sources; uncertainty is a tool with distinct sources; onboarding teaches by doing. The kb records where the books disagree and which view the plugin takes.
- AI helps designers most at ideation and document structure, least at authorship. Generic output is the documented failure (R-20261029-2), so designs must name a verb, a constraint and a hook.
- LLM design critique turns sycophantic or misreads the design unless it restates intent and cites the rules text (R-20261029-3). Grounded critique traces rule, dynamic and experience, per player type (MeepleLM, ACL 2026).
- Simulated balance answers depend on the assumed player policy and the agent pool (R-20261029-4). Report distributions and name the policy. LLM playtesters find bugs and difficulty, not exploits.
- Tooling: no maintained skill, plugin or MCP server does design review with evidence, a findings contract or evals; the closest are broad orchestrators and checklists (R-20261029-5). Confidence: medium; the tooling pass read snippets, not repos.
- Testing: exact maths gets golden tests, Monte Carlo gets fixed seeds and a standard-error band, findings get a schema check (R-20261029-6).
- Linked everscout beat `game-design` (2026-10-29) watches the craft and AI-for-design communities between refreshes; its notes are leads only.

## Open questions

- The creation pass was thin (12 searches, 2 fetches in all): read the top game-design skills in full (davila7 game-development, jarrodmedrano game-design-theory), awesome-copilot's agents, hn.algolia.com and r/gamedesign.
- modl.ai's current product and Dominion-style simulators: no primary source yet.
- Is there a convention for declared balance tables (TSV, YAML, JSON) worth adopting over ldw.py's own?
- RL exploit-finding papers 2024-2026 not yet searched.
- Books not on disk: Carillo, Gupta, Baldwin, Steele, Game AI Pro 1, 2 and 4; Totten 2nd ed.

## Search plan

Four tracks; every refresh runs at least one query on each (scope each to the period since the last refresh; add the year). Protocol §4 explains the tracks and how tooling, practice and testing findings are judged.

Subject (the goal and the latest thinking on reaching it):

- `game design critique LLM OR "design review" 2026`
- `game balance simulation Monte Carlo OR self-play designers 2026`
- Official forums of each tool, platform or vendor this unit depends on (announcements, deprecations, breaking changes and known bugs often land there before the docs): no single vendor; r/gamedesign and r/truegamedev (practitioners), GDC Vault talks (gdcvault.com), Game Developer (gamedeveloper.com) design category; a vendor Discourse, community site or the tool repository's GitHub Discussions. Search announcements first, then known issues, since the last check (`site:<forum host> <terms> 2026-11`, or Discourse `/latest.json`, a category `.rss`, `search.json?q=<terms> after:<date>`). Staff posts are primary sources; user posts are leads to confirm.

Tooling (skills, plugins, MCP servers, scripts, knowledge graphs built for this subject):

- `path:SKILL.md "game design"` on GitHub code search, sorted by recently updated; `npx skills find "game design"` and skills.sh for install counts
- `https://registry.modelcontextprotocol.io/v0/servers?search=game design`; fallback `"game design" mcp server site:glama.ai OR site:pulsemcp.com`
- `"game design" skill OR plugin OR "mcp server" 2026 site:github.com`
- Most used: skills.sh weekly and 24-hour installs for `game design` (never all-time; exclude meta and installer skills); `anthropics/claude-plugins-official` and `claude-plugins-community` searched for `game design` (record the tier)
- Practitioner test on every candidate: commit in the last 90 days, issues answered, no bundled `*.test.*` or `conftest.py` from an unknown author, author has other work in the area, ships `evals/` or paired results; `path:SKILL.md "game design" evals OR benchmark`
- Provenance tiebreaker: which model and reasoning setting wrote each candidate (`evals.json` / frontmatter `model`, README or changelog credit, commit messages); prefer the latest frontier model at its highest reasoning setting, read over inferred
- Supersession sweep: `"game design" skill deprecated OR superseded OR archived 2026`; archive flag on every tool already listed here

Most discussed and the converged thinking (comment volume over points; what the most-used and most-discussed sources agree on becomes a claim in Current understanding):

- `hn.algolia.com/api/v1/search_by_date?query=game design` and `site:reddit.com/r/ClaudeAI OR r/ClaudeCode "game design" 2026-11`
- OpenAlex `works?search=game design agent&sort=cited_by_count:desc&filter=from_publication_date:2026-10-29`; the two most-cited through Semantic Scholar

Practice (how others use AI agents on this goal, and everything in between):

- `"how I use" OR "my workflow" "game design" "claude code" OR codex OR cursor 2026`
- `site:arxiv.org "game design" agent "case study" OR empirical OR telemetry 2026`
- `"game design" site:simonwillison.net OR site:latent.space OR site:anthropic.com/engineering 2026`; hn.algolia.com `"game design" agent` sorted by date

Testing (how work on this subject is verified, and how skills for it are tuned):

- `"game design" verify OR validate OR "smoke test" OR checker agent 2026` (what evidence shows the job was done)
- `path:SKILL.md "game design" test OR eval OR evals` on GitHub; `"game design" evals OR "eval suite" OR regression "agent skill" 2026`
- `site:arxiv.org "game design" agent evaluation OR benchmark 2026`; promptfoo, Inspect or DeepEval docs for assertion types that fit this subject

Best sources (primary first): GDC talks and the State of the Industry survey; arXiv cs.AI and the FDG, CoG and AIIDE proceedings; the book canon in kb/; skills.sh, the MCP registry and the anthropics plugin catalogs for tooling. Sources that proved noisy: SEO MCP directories (enterprisedna, claudskills listings), sponsored modl.ai listicles.

## Findings log

Newest first. One entry per material finding; a quiet refresh gets one entry saying so. `Track` is subject, tooling, practice, or testing.

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
