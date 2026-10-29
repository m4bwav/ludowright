---
title: How people use AI for game design: ideation, GDDs, critique, existing skills
date: 2026-10-29
---

# AI for game design: ideation and critique (first pass)

An evergreen-researcher pass in creation mode. It was thin: 6 searches and 1 fetch, against the 8+ fetches creation mode asks for. Most tool rows come from search snippets. Next pass: read the top skill repos' SKILL.md files in full, check awesome-copilot's `agents/` and `chatmodes/`, and search hn.algolia.com and r/gamedesign directly.

## Findings

1. **Practice: AI helps most at ideation, not authorship.** In the GDC 2026 State of the Industry survey, 81% of developers using AI named research or brainstorming as their most common use. A 2025 qualitative synthesis agrees. Sources: https://www.techspot.com/news/111128-more-than-50-game-developers-generative-ai-harming-the-industry, https://arxiv.org/pdf/2509.11898 (Sep 2025).
2. **Practice: generic output is the documented failure.** LLMs suggest few-word guidelines that need a lot of design work before they become a game (LLMs and Games survey, Feb 2024). Board game designers in a TTGDA survey called AI material derivative. About a quarter had used it for ideas, and more than half were strongly opposed. Sources: https://arxiv.org/pdf/2402.18659, https://boardgamewire.com/index.php/2026/03/27/more-than-half-of-board-game-designers-in-ttgda-survey-have-used-generative-ai-in-their-work/ (2026-03-27). **Guard for ludowright:** a one-pager names a specific verb, a constraint and a hook, and abstract feature lists are rejected.
3. **Practice: designers distrust qualitative LLM critique.** The Alexandrian and an r/RPGdesign thread report LLMs misreading a game's core principles. A 2025 controlled study, not about games, found that sycophantic chatbots reinforce misconceptions. Sources: https://thealexandrian.net/wordpress/tag/ai, r/RPGdesign thread (May 2024), https://arxiv.org/pdf/2510.03667 (Oct 2025). **Guards:** restate the design's intent before critiquing it, require evidence that cites the rules text for every flaw, and allow an explicit "no issue found".
4. **Testing and practice: MeepleLM is the best published grounded critique.** It is a virtual playtester trained on 1,727 rulebooks and 150K reviews. It uses MDA reasoning (rule, then dynamic, then aesthetic) and simulates player personas. The paper reports it beat GPT-5.1 and Gemini 3-Pro, with 70% user preference (ACL 2026). Source: https://arxiv.org/pdf/2601.07251. **Adopted:** each review finding traces rule, then dynamic, then experience, and names who it hurts (persona).
5. **Tooling: the Claude game-design skill space is crowded and immature.** No official Anthropic or Copilot game-design skill was found, and none ships evals. See the table below.
6. **Practice:** an LLM-written hyper-casual GDD was rated 4.71/5 against 3.29 for a human expert's. That is one game and a small panel, so the evidence is weak. LLMs do well at document structure. Source: https://openaccess.izu.edu.tr/entities/publication/b51838a1-dd18-4aa8-b6de-1d5450c8a0e2/full
7. **Practice:** in a mixed-methods study (42 respondents, 9 interviews), AI sped up ideation and prototyping and raised worries about originality and dependency. Source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12193870/ (2025).
8. **Practice:** in the Ink Splotch Effect case study (2024), ChatGPT worked as a muse, and player feedback was dominated by feel and controls, which a paper design cannot show. Source: https://arxiv.org/pdf/2403.02454. **Guard:** findings that depend on feel are marked `needs-playtest` or handed to juice-scan.

## Tools: best idea and known failure

| Tool | Tier, use | Best idea | Known failure |
|---|---|---|---|
| davila7/claude-code-templates game-development | skills.sh, about 536 installs | Orchestrator routing to sub-skills | Broad, no design critique, no evals seen |
| jarrodmedrano game-design-theory | skills.sh, 43 installs, first seen 2026-01-24 | Judge by player experience, not designer intent (Rouse) | No workflow, no output format, no evals |
| playableintelligence/game-creator design-game | community | Juice and polish checklist | Ignores gameplay logic |
| MeepleLM (research) | ACL 2026 | MDA chain plus persona playtesting | A model, not a skill; board games only |

Cost: searches 6 · fetches 1 · tool calls 8
