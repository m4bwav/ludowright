---
type: regex
name: 'rules.py ends at round 10 but the design says 14'
target: {source: file, path: harbor-yard/review.md}
pattern: '(MAX_ROUNDS|rules\.py|prototype|code)[^.]{0,120}\b10\b[\s\S]{0,250}\b14\b|\b14\b[\s\S]{0,250}(MAX_ROUNDS|rules\.py|prototype|code)[^.]{0,120}\b10\b'
flags: i
match: contains
arm: both
---
