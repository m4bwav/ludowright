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

Entries R-20261029-1 to R-20261029-6 (the creation pass) are in [ai-docs/research-archive.md](../../ai-docs/research-archive.md), moved out to keep the installed folder small.
