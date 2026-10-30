# Findings contract (format 1.1)

Copy of the README section, kept here so a run reads one small file. Change both together.

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

