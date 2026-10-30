# ludowright

![A game designer's table in warm lamp light: a hand-drawn hex-map prototype with wooden pawns and dice, index cards sketched with loop arrows, an open notebook and a red pen, and a hand pencilling notes onto the map](https://raw.githubusercontent.com/m4bwav/ludowright/main/.github/images/banner.jpg)

Game design with the work shown. ludowright pitches new games as one-pagers, ranks improvements to an existing game, and reviews a game's design for flaws, and every finding points at the file, rule or number it rests on and names the design principle it breaks. Its knowledge is distilled from the design canon (Schell, Fullerton, Salen and Zimmerman, Sylvester, Koster, Sellers, Romero and Schreiber, Adams and Dormans, Costikyan, Hodent, Elias, Garfield and Gutschera, Totten, Lemarchand and the game AI literature), paraphrased with chapter citations.

It is one agent skill plus a small standard-library Python tool. It works in Claude Code, Claude Desktop and GitHub Copilot, and in any agent that reads `SKILL.md`.

## What it does

| Ask | You get |
|---|---|
| "Design a game about...", "jam ideas for this theme" | `design-<slug>.md`: hook, experience goal, core loop as a verb, mechanics, progression, scope, risks with the cheapest test for each, and two or three contrasting alternatives |
| "Review my game's design", "what's wrong with my game" | `review-<game>-<date>.json` and `.md`: findings from a 52-item rubric, each with a location, evidence and the broken principle |
| "How do I make my game better" | `improve-<game>-<date>.json` and `.md`: suggestions ranked by impact and effort |
| "Is this card overpowered", "does my economy leak", "how many turns to afford X" | a counted answer from `ldw.py` (expected value, cost curve, sources and sinks, Monte Carlo) and the table it counted |
| Levels, onboarding, playtest questionnaires, randomness, procedural generation, enemy AI | an answer from the matching kb file, with sources |

It reads the game's docs, data and code and never edits them. Feel (juice, screen shake, hit-stop) goes to [game-juice](https://github.com/m4bwav/game-juice); engine code goes to the engine plugins.

## Install

**Claude Code:** add the repository as a marketplace, then install:

```
claude plugin marketplace add m4bwav/ludowright
claude plugin install ludowright@ludowright
```

**Claude Desktop:** download the repository as a ZIP and add `skills/ludowright` as a skill.

**GitHub Copilot and other agents:** copy `skills/ludowright` into your agent's skills folder (for Copilot, `.github/skills/` or `~/.copilot/skills/`).

Python 3.9 or newer runs the tool; nothing else is needed.

## Quick start

```
Review the design of my game. The docs are in docs/ and the card data is in data/cards.csv.
```

```
python skills/ludowright/scripts/ldw.py curve data/cards.csv --attrs damage,block,draw
python skills/ludowright/scripts/ldw.py findings validate review-mygame-2026-10-29.json
```

## Findings contract

Other plugins and agents can ask ludowright to evaluate a design or a game and read the result without parsing prose. This is the contract they rely on. Format `ludowright-findings`, version **1.1** (1.1 added the optional `stage` and `built`). Minor versions only add optional fields or categories; a breaking change is version 2.0.

```json
{
  "format": "ludowright-findings",
  "version": "1.1",
  "game": "Tiny Colony",
  "kind": "review",
  "date": "2026-10-29",
  "stage": "prototype",
  "sources_read": ["DESIGN.md", "cards.csv"],
  "summary": "optional one paragraph",
  "findings": [
    {
      "id": "F-001",
      "severity": "major",
      "category": "dominant-strategy",
      "title": "Overclock is the only right pick at cost 1",
      "location": {"file": "cards.csv", "rule": "Overclock"},
      "principle": {"name": "no dominant strategy", "source": "kb/review-rubric.md R-01; Romero and Schreiber ch. 8"},
      "evidence": "cost 1, output 6, draw 1; the other cost-1 cards give 2 of one thing",
      "suggestion": "cost 2, or drop the draw",
      "impact": "high",
      "effort": "S",
      "confidence": "high",
      "rubric": "R-01"
    }
  ]
}
```

| Field | Required | Values |
|---|---|---|
| `kind` | yes | `review`, `improve`, `design-check` |
| `id` | yes | `F-001`, unique in the file |
| `severity` | yes | `critical`, `major`, `minor`, `note` |
| `category` | yes | `dominant-strategy`, `degenerate-loop`, `dead-choice`, `economy-leak`, `difficulty-spike`, `onboarding-gap`, `pacing`, `scope-risk`, `broken-promise`, `balance`, `progression`, `clarity`, `uncertainty`, `level-design`, `ai-behaviour`, `feel`, `other` |
| `location` | yes | `file` (a path, or `design` for a pitch) plus at least one of `section`, `rule`, `symbol`, `line` |
| `principle` | yes | `name`, and `source` (a kb file or book citation) |
| `evidence`, `suggestion`, `title` | yes | text; evidence quotes or names the rule, number or line |
| `impact`, `effort` | in `improve` files | `high`/`medium`/`low`; `S`/`M`/`L` |
| `stage` | no | the game's stage: `concept`, `prototype`, `in-development`, `shipped`, `live` |
| `built` | no | on a finding about content the design or data promises but the code does not have yet: `no` or `partial`. It separates "not built yet" from "built wrong" |
| `confidence`, `handoff`, `rubric` | no | `high`/`medium`/`low`; a skill name (feel findings hand off to `juice-scan`); an `R-` item |

`ldw.py findings validate FILE` exits 0 when the file meets the contract and 1 when it does not; `ldw.py findings md FILE -o FILE.md` writes the readable view, sorted by severity, impact and effort.

## How it was built

The reading notes (27 books, read in sections with [readwright](https://github.com/m4bwav/readwright), paraphrased with citations) were merged into twelve topic files and the review rubric. Two web research passes on how designers use AI shaped the rules: designs must be specific, critique must restate intent and cite rules text, and balance claims must name the player policy they assume. The plugin is an evergreen unit: it re-researches itself on a schedule, and an everscout beat watches the design community between refreshes.

## Privacy

ludowright reads the files you point it at and writes its output beside them. It sends nothing anywhere.

## License

MIT. See [LICENSE](LICENSE). Security reports: [SECURITY.md](SECURITY.md).
